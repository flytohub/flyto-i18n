# Product Verification i18n Closure

## Summary

Added the missing `flyto-code` translations for the Product Verification
cockpit, scheduler controls, and project creation next-step entry.

## Scope

- Added English, Traditional Chinese, and Simplified Chinese source keys under
  `locales/code/*/code.json`.
- Added shared `common.running` under `locales/shared/*/common.json` for en,
  zh-TW, and zh-CN.
- Rebuilt `dist/` and synced bundled baselines to consuming projects.

## Verification

```text
python3 scripts/validate.py
python3 ../flyto-code/scripts/check-i18n.py
python3 ../flyto-cloud/scripts/check-i18n.py
```

Result: pass.

## Notes

The Product Verification frontend now fails closed on future missing i18n keys
through `flyto-code/scripts/check-i18n.py`; no allowlist entry was added.
