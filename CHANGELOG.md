# Changelog

## Unreleased

### Added

- Added Product Verification cockpit and scheduler translations for `flyto-code`
  plus the shared `common.running` key used by action buttons.
- Added unittest coverage for `scripts/sync-to-projects.py` dry-run, stale
  locale deletion, manifest sync behavior, and `scripts/add-locale.py` locale
  coverage status calculation.
- Added project memory files, workflow docs, and handoff registry.

### Changed

- Reduced `scripts/sync-to-projects.py` complexity by extracting locale,
  manifest, deletion, app-build, and summary helpers without changing locale
  data.
- Reduced `scripts/add-locale.py` list complexity by extracting locale coverage
  counting and status formatting helpers.
