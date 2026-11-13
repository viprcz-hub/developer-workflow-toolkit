import unittest
from toolkit.changelog import parse_conventional_commit, format_changelog_section

class TestChangelog(unittest.TestCase):
    def test_parse_conventional(self):
        res = parse_conventional_commit("feat(auth): add OAuth2 token refresh")
        self.assertEqual(res["type"], "feat")
        self.assertEqual(res["scope"], "auth")
        self.assertEqual(res["description"], "add OAuth2 token refresh")

    def test_format_changelog_section(self):
        commits = [
            "feat(api): support pagination",
            "fix(db): handle connection timeouts",
            "docs: update readme usage"
        ]
        res = format_changelog_section(commits)
        self.assertIn("### ✨ Features", res)
        self.assertIn("### 🐛 Bug Fixes", res)
        self.assertIn("### 📝 Documentation", res)

if __name__ == "__main__":
    unittest.main()
