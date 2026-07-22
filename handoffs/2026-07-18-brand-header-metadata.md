# 2026-07-18 Flyto2 i18n Brand and Metadata Refresh

## Summary

This pass tightened `flyto-i18n` as the shared public source for Flyto2
localization, multilingual SEO, and package-index discovery.

## Changed

- Added `package.json` description, homepage, repository, bugs, and SEO keyword
  metadata.
- Updated source locale values and generated `dist/` bundles from
  the retired API-key header to `X-Flyto2-API-Key`.
- Replaced visible standalone retired-brand copy in Japanese/Korean landing story text
  and Thai cloud labels with Flyto2 wording.
- Corrected the README license badge from Apache-2.0 to MIT and refreshed
  coverage numbers from the generated manifest.
- Rebuilt `dist/` and `dist/seo-manifest.json`.

## Verification

```bash
npm run verify
python3 scripts/validate.py --strict
flyto-indexer verify
flyto-indexer scan_secrets
```

Value-only JSON scan after the build reported zero visible standalone retired
brand or retired API-key header values in `locales/` and `dist/`.

## Follow-Up

- Ensure `flyto-engine` accepts preferred `X-Flyto2-API-Key` headers before any
  downstream client depends only on the new header spelling.
