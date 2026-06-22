# Sync Tooling Complexity Guard

Date: 2026-06-22 Asia/Taipei

## Context

The Flyto2 workspace reverse audit still marked `flyto-i18n` as a C-grade
internal tooling repo. The live indexer audit reported complexity as the weakest
dimension, with `scripts/sync-to-projects.py` among the top hotspots.

## Change

- Split locale sync, stale target deletion, manifest sync, app-build delegation,
  and summary output into small helpers.
- Added standard-library unittest coverage for dry-run safety, stale locale
  deletion, and manifest update behavior.
- Split `add-locale.py` locale coverage counting/status formatting into pure
  helpers with unittest coverage.
- Kept locale data unchanged; this closure only changes tooling and tests.

## Verification

```text
/opt/homebrew/bin/python3.11 -m unittest discover -s tests -p 'test_*.py'
/opt/homebrew/bin/python3.11 scripts/validate.py
/opt/homebrew/bin/python3.11 scripts/sync-to-projects.py --dry-run
/opt/homebrew/bin/python3.11 -m src.cli scan /Users/chester/flytohub/flyto-i18n --full
/opt/homebrew/bin/python3.11 -m src.cli verify /Users/chester/flytohub/flyto-i18n --full-scan --json
```

Notes:

- The dry-run still reports that `flyto-cloud` bundled files would be raw-format
  updated. That was not applied in this closure.
- Consuming project i18n semantic checks remain the authority before applying a
  live sync.
