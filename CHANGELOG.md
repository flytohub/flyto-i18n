# Changelog

## Unreleased

### Added

- Added the Flyto2 Warroom CE deterministic product-loop copy for all supported
  `flyto-code` locale catalogs, including loading, error, evidence, surface,
  metric, safe-mode, and Enterprise-boundary states.
- Added validation coverage that prevents the critical
  `code.communityLoop.*` namespace from regressing to empty Traditional or
  Simplified Chinese values.
- Added package metadata, backlink fields, and SEO-focused keywords so the
  i18n source is clearer on GitHub and package indexes.
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

- Rebuilt distribution bundles and synchronized the CE product-loop catalog to
  the consuming `flyto-code` package.
- Updated public locale values to use the Flyto2 brand and the preferred
  `X-Flyto2-API-Key` header text.
- Corrected the README license badge to match the MIT license file and refreshed
  generated coverage numbers.
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
