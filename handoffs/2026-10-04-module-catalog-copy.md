# Module catalog copy

Owner: claude
Branch: claude/catalog-titles
Date: 2026-10-04
Status: Active (committed, not pushed)

## What changed

- `locales/code/{en,zh-TW,zh-CN}/code.json`: six keys the flyto-engine module
  catalog references but this repo never had:
  `code.projects.feature.core` / `coreDesc`, `vrm` / `vrmDesc`,
  `supplyChain` / `supplyChainDesc`. English matches the catalog's
  `display_name` and `description`. Keys stay sorted; `total_keys` updated.
- `dist/` rebuilt with `scripts/build-dist.py`.
- `tests/test_module_catalog_copy.py`:
  - reads `internal/modulecatalog/catalog.yaml` (from `FLYTO_ENGINE_CATALOG`,
    or a sibling `../flyto-engine` checkout) and requires every `title_key` /
    `description_key` to resolve as `code.<key>` in en, zh-TW and zh-CN;
  - requires every `code.projects.feature.X` / `XDesc` pair in English to
    exist, non-empty, in zh-TW and zh-CN (no engine checkout needed).

## Why

Warroom's "Modules & licences" table rendered raw keys (`core`, `vrm`,
`supply_chain_intelligence`) because the catalog had no title keys for some
modules and `projects.feature.core` had no copy. The engine catalog is the only
module registry (flyto-engine `claude/catalog-titles`, 1602d21b): every module
now must declare both keys, and the engine's `scripts/check-i18n-keys.py`
fails when one is missing here. This change supplies the copy, and the new test
checks the same contract from this side, against the catalog, with no copied
module list.

## Merge order

Merge this before flyto-engine `claude/catalog-titles`; the engine's i18n
check reads this repo's `locales/code/en/code.json`.

## Verified

- `python3 scripts/build-dist.py`: done, dist updated (8 files).
- `python3 scripts/validate.py --strict`: PASS, 0 errors.
- `FLYTO_ENGINE_CATALOG=<engine worktree catalog> python3 -m unittest discover -s tests`:
  78 tests OK. Without the variable: 78 OK, 1 skipped (catalog test).
- Negative check: with the locale changes stashed, the catalog test fails on
  exactly the 18 missing entries (6 keys x 3 locales).
- `flyto-index scan .` then `flyto-index verify --strict` in the worktree: exit 0,
  all checks PASS.

## Not verified

- MCP `verify(strict=true)` / `task(action='validate')` (MCP pinned to another
  repo; CLI verify used instead).
- In CI the catalog test skips, because this repo's workflows do not check out
  flyto-engine. The enforcing gate in CI is the engine's
  `scripts/check-i18n-keys.py`.
- No native-speaker review of the zh-TW / zh-CN copy.
- Other locales fall back to English, as usual.

## Follow-ups

- TODO: after merge, bump the flyto-i18n SHA pinned in flyto-code CI /
  deploy workflows and in flyto-engine's i18n check, if pinned (merged SHA not
  known yet; do not guess it).
