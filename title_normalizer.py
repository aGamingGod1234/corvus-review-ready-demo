"""Utilities for normalizing human-readable titles."""

import re


NON_ALPHANUMERIC_RUN = re.compile(r"[\W_]+", flags=re.UNICODE)


def normalize_title(title: str) -> str:
    """Return a lowercase, hyphen-separated form of *title*."""
    stripped_title = title.strip()
    hyphenated_title = NON_ALPHANUMERIC_RUN.sub("-", stripped_title)
    return hyphenated_title.lower().strip("-")
