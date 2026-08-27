from __future__ import annotations

import argparse
from pathlib import Path
import re


SKIP_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".venv",
    "venv",
    "__pycache__",
}

ENV_ALLOWED = {".env.example", ".env.sample", ".env.template"}
KEY_BASENAMES = {
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    ".netrc",
    ".npmrc",
    ".pypirc",
}
KEY_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".jks", ".keystore"}

PLACEHOLDER_MARKERS = (
    "replace",
    "placeholder",
    "example",
    "changeme",
    "change-me",
    "dummy",
    "fake",
    "not-a-secret",
    "redacted",
    "your-",
    "<",
    "${",
    "***",
)

PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "private key material",
        re.compile(
            r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----",
            re.IGNORECASE,
        ),
    ),
    (
        "possible access token",
        re.compile(
            r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
            r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,}|"
            r"xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|"
            r"sk_live_[A-Za-z0-9]{20,})"
        ),
    ),
    (
        "possible bearer credential",
        re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}", re.IGNORECASE),
    ),
    (
        "credential-bearing connection string",
        re.compile(
            r"\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp|https?)://"
            r"[^\s/:@]+:([^\s/@]+)@[^\s]+",
            re.IGNORECASE,
        ),
    ),
    (
        "possible credential assignment",
        re.compile(
            r"(?im)^\s*(?:password|passwd|pwd|api[_-]?key|access[_-]?token|"
            r"refresh[_-]?token|client[_-]?secret|secret|private[_-]?key|token)"
            r"\s*[:=]\s*[^\s#;]+"
        ),
    ),
)


def _placeholderish(text: str) -> bool:
    lowered = text.lower().strip().strip("'\"")
    if lowered in {"password", "passwd", "secret", "token", "api-key", "apikey"}:
        return True
    return any(marker in lowered for marker in PLACEHOLDER_MARKERS)


def _iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            relative = path.relative_to(root)
        except ValueError:
            continue
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        yield path, relative


def _read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > 2_000_000:
            return None
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan_repository(root: Path) -> list[str]:
    issues: list[str] = []
    root = root.resolve()

    for path, relative in _iter_files(root):
        rel = relative.as_posix()
        lowered_name = path.name.lower()

        if lowered_name.startswith(".env") and lowered_name not in ENV_ALLOWED:
            issues.append(f"tracked environment file: {rel}")

        if lowered_name in KEY_BASENAMES or path.suffix.lower() in KEY_SUFFIXES:
            issues.append(f"credential/key file: {rel}")

        text = _read_text(path)
        if text is None:
            continue

        for label, pattern in PATTERNS:
            for match in pattern.finditer(text):
                snippet = match.group(0)
                if label == "credential-bearing connection string":
                    credential = match.group(1) if match.lastindex else snippet
                    if _placeholderish(credential):
                        continue
                elif label == "possible credential assignment":
                    value = re.split(r"[:=]", snippet, maxsplit=1)[-1].strip()
                    if _placeholderish(value):
                        continue
                elif _placeholderish(snippet):
                    continue
                issues.append(f"{label}: {rel}")
                break

    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a candidate public repository tree for obvious secrets")
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="tree to scan; defaults to repository root",
    )
    args = parser.parse_args()
    findings = scan_repository(args.root)
    if findings:
        raise SystemExit("\n".join(findings))
    print("public safety scan: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
