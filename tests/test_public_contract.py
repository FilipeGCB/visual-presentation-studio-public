from pathlib import Path
import unittest
from scripts.validate_repo import validate_repository

class PublicRepositoryContractTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]

    def test_repository_contract(self):
        self.assertEqual([], validate_repository(self.root))

    def test_public_safety_documents_are_fail_closed(self):
        agents = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        security = (self.root / "SECURITY.md").read_text(encoding="utf-8")
        for token in ("SECRET", "UNKNOWN", "fail closed"):
            self.assertIn(token.lower(), agents.lower())
        self.assertIn("Do not report secrets by pasting them into a public issue", security)

    def test_starters_are_local_first(self):
        for rel in ("templates/standalone-16x9/index.html", "templates/standalone-scroll/index.html"):
            html = (self.root / rel).read_text(encoding="utf-8")
            self.assertIn("<!doctype html>", html.lower())
            self.assertIn("prefers-reduced-motion", html)
            self.assertNotIn("http://", html)
            self.assertNotIn("https://", html)

if __name__ == "__main__":
    unittest.main()
