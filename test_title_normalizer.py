"""Tests for title normalization."""

import unittest

from title_normalizer import normalize_title


class NormalizeTitleTests(unittest.TestCase):
    """Verify titles are normalized consistently."""

    def test_trims_whitespace_and_lowercases(self) -> None:
        self.assertEqual(normalize_title("  Hello World  "), "hello-world")

    def test_collapses_non_alphanumeric_runs(self) -> None:
        self.assertEqual(
            normalize_title("Python___Tips:   Testing & Quality"),
            "python-tips-testing-quality",
        )

    def test_trims_leading_and_trailing_hyphens(self) -> None:
        self.assertEqual(normalize_title("---Release Notes!!!"), "release-notes")

    def test_preserves_unicode_alphanumeric_characters(self) -> None:
        self.assertEqual(
            normalize_title("Caf\u00e9 d\u00e9j\u00e0 vu"),
            "caf\u00e9-d\u00e9j\u00e0-vu",
        )

    def test_returns_empty_string_when_no_alphanumeric_characters_exist(self) -> None:
        self.assertEqual(normalize_title("  --_!?  "), "")


if __name__ == "__main__":
    unittest.main()
