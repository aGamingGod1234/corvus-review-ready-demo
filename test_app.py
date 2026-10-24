"""Smoke tests for the demo's command-line entry point."""

from pathlib import Path
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parent


class AppTests(unittest.TestCase):
    def test_script_prints_demo_name(self) -> None:
        result = subprocess.run(
            [sys.executable, "app.py"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "Corvus review-ready demo\n")
        self.assertEqual(result.stderr, "")

    def test_import_does_not_run_application(self) -> None:
        result = subprocess.run(
            [sys.executable, "-c", "import app"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
