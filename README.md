# Corvus Review-Ready Demo

A deliberately small Python project used to demonstrate a governed Corvus change. The starting repository contains only a basic application entry point; the agent adds the requested helper, focused tests, and documentation inside an isolated worktree.

## Requirements

Use a supported Python 3 release. The demo and its tests use only the standard
library, so no packages need to be installed. Run commands from the repository
root. If your Python 3 executable is named `python3` or `py`, use that in place
of `python` below.

## Check a change

```bash
python -m unittest discover -v
```

The smoke tests run the actual application in a subprocess and check that
importing `app` does not print anything. Test discovery also includes new
`test_*.py` files added by later demo changes.

GitHub Actions runs the suite on pull requests to `main` and pushes to `main`,
using Python 3.11 and 3.15, the oldest and newest supported stable series as of
October 2026. See the [Python version status](https://devguide.python.org/versions/)
for the upstream support lifecycle.

## Run

The command prints `Corvus review-ready demo` and exits.

```bash
python app.py
```
