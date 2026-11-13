import unittest
from toolkit.env_checker import check_binary, audit_environment

class TestEnvChecker(unittest.TestCase):
    def test_python_installed(self):
        ok, detail = check_binary("python3")
        self.assertTrue(ok)
        self.assertIn("Python", detail)

    def test_audit_structure(self):
        res = audit_environment()
        self.assertIn("required", res)
        self.assertIn("recommended", res)
        self.assertIn("git", res["required"])

if __name__ == "__main__":
    unittest.main()
