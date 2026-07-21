# Community Product Loop i18n Closure

## Summary

Added the source and generated locale contract used by the self-hosted Flyto2
Warroom CE onboarding product loop.

## Scope

- Added loading, error, empty, action, surface, metric, evidence, safe-mode, and
  Enterprise-overlay labels under `code.communityLoop.*` for all supported
  locales.
- Added native Traditional and Simplified Chinese product copy.
- Marked the namespace critical and non-empty in locale validation.
- Rebuilt `dist/` and synchronized the consuming `flyto-code` bundles.

## Verification

```text
/opt/homebrew/bin/python3.11 scripts/validate.py --strict
/opt/homebrew/bin/python3.11 -m unittest discover -s tests
/opt/homebrew/bin/python3.11 scripts/build-dist.py
/opt/homebrew/bin/python3.11 scripts/sync-to-projects.py --project code --dry-run
```

Result: pass; the final dry run reports no pending locale updates.
