## 2026-07-21 -- Add title normalization helper

### What Was Implemented

- Added a typed helper that normalizes titles into lowercase, hyphen-separated text.
- Added focused standard-library unit tests for whitespace, separators, edge trimming, Unicode, and empty results.
- Documented the helper with a usage example.

### Files Modified

- `title_normalizer.py` -- implements title normalization.
- `test_title_normalizer.py` -- verifies the normalization rules and edge cases.
- `README.md` -- shows how to import and use the helper.
- `PROJECT_LOG.md` -- records the completed work and verification context.

### Assumptions Made (flag these for review)

- Alphanumeric characters follow Python's Unicode-aware regular-expression semantics.
- The public helper is named `normalize_title` and accepts a string.

### Known Issues / Deferred

- Test execution is blocked because this environment has no Python executable on PATH.

### Suggested Next Steps

- Run `python -m unittest -v` in an environment with Python available.
- Review the focused change and let Corvus manage any contribution or publishing workflow.
