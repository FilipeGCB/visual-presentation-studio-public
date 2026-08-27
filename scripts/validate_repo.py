from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "SECURITY.md",
    "skill/visual-presentation-studio/SKILL.md",
    "skill/visual-presentation-studio/references/workflow.md",
    "skill/visual-presentation-studio/references/quality-gates.md",
    "methodology/presentation-contract.md",
    "quality/visual-qa.md",
    "patterns/anti-patterns/generic-ai-ui.md",
    "examples/generic-acceptance/proposal.md",
    "templates/standalone-16x9/index.html",
    "templates/standalone-scroll/index.html",
    "templates/exploratory-react/package.json",
]

FORBIDDEN_PUBLIC_PREFIXES = (
    "eval/",
    "private/",
    "private-data/",
    "real-presentations/",
    "presentation-workspace/",
    "deliverables/",
    "exports/",
    "local-data/",
)

def validate_repository(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required path: {relative}")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative.startswith(FORBIDDEN_PUBLIC_PREFIXES):
            errors.append(f"forbidden public path: {relative}")
    skill = root / "skill/visual-presentation-studio/SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        for token in ("Gate 1", "Gate 2", "Visual Inspection", "0 BLOCKER", "0 MAJOR"):
            if token not in text:
                errors.append(f"central skill missing invariant: {token}")
    return errors

if __name__ == "__main__":
    problems = validate_repository(Path(__file__).resolve().parents[1])
    if problems:
        raise SystemExit("\n".join(problems))
    print("public repository contract: PASS")
