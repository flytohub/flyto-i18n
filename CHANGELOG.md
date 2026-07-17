# Changelog

## Unreleased

### Added

- Added `scripts/i18n_contract.py` as the shared locale/project metadata source
  for build, validation, coverage, and add-locale tooling.
- Added `seo/public-surfaces.json` and generated `dist/seo-manifest.json` for
  landing/docs/blog multilingual SEO, `hreflang`, sitemap, `og_locale`, and
  long-tail keyword planning.
- Added unittest coverage for the SEO manifest builder and wired unittest
  discovery into `npm test` / `make test`.
- Added Product Verification cockpit and scheduler translations for `flyto-code`
  plus the shared `common.running` key used by action buttons.
- Added unittest coverage for `scripts/sync-to-projects.py` dry-run, stale
  locale deletion, manifest sync behavior, and `scripts/add-locale.py` locale
  coverage status calculation.
- Added project memory files, workflow docs, and handoff registry.

### Changed

- `scripts/build-dist.py` now generates `dist/locale-meta.json` from the shared
  contract and reports translated completion from unique merged keys instead of
  double-counting duplicated source keys.
- `scripts/coverage.py` and `scripts/add-locale.py` now include the `engine`
  scope through the shared contract.
- Updated root project memory and manifest coverage numbers for the current
  Flyto2 localization and public SEO role.
- Reduced `scripts/sync-to-projects.py` complexity by extracting locale,
  manifest, deletion, app-build, and summary helpers without changing locale
  data.
- Reduced `scripts/add-locale.py` list complexity by extracting locale coverage
  counting and status formatting helpers.
