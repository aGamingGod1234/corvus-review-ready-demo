# Corvus Review-Ready Demo

A deliberately small Python project used to demonstrate a governed Corvus change. The starting repository contains only a basic application entry point; the agent adds the requested helper, focused tests, and documentation inside an isolated worktree.

## Run

```bash
python app.py
```

## Normalize a title

Use `normalize_title` to produce a lowercase, hyphen-separated title:

```python
from title_normalizer import normalize_title

normalized_title = normalize_title("  Corvus: Review-Ready Demo!  ")
print(normalized_title)  # corvus-review-ready-demo
```
