# Report Export Format i18n

Flyto2 Reports now sources its export-format selector and PowerPoint `.pptx`
name from the canonical Code catalog. English, Traditional Chinese, and
Simplified Chinese contain reviewed copy; the remaining 13 supported locales
carry deterministic English fallbacks until native translations are reviewed.

The change is limited to two additive `code.reports.*` keys. Generated Code and
aggregate distributions are rebuilt from source, then the Code scope is
synchronized into `flyto-code/public/i18n/code`.

Verification:

- `npm run verify`: 4,592 catalogs, 38 tests, Ruff, documentation freshness,
  deterministic distributions, and SEO build passed
- focused report export contract: 2 tests passed across source and generated
  bundles
- strict Indexer: 19/19 passed with zero warnings/failures
- scoped `dist/code/` synchronization into
  `flyto-code/public/i18n/code/` after the full-project dry-run exposed
  unrelated pre-existing Cloud bundle drift
