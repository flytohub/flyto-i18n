# Module catalog copy

Owner: claude
Branch: claude/catalog-titles
Date: 2026-10-04
Status: Active (committed, not pushed)

## What changed

- `locales/code/{en,zh-TW,zh-CN,ja}/code.json`: copy for every key the
  flyto-engine module catalog references: `core`, `vrm`, `supplyChain`
  (+ `Desc`), and `thirdPartyMonitoring`, `codeSecurityAutofix` (+ `Desc`) for
  the engine change that gives `continuous_monitoring` and `autofix` their own
  keys. `ja` also gained the catalog keys it had empty (cspm, container,
  darkWeb, vulnMgmt, identity, productVerification, agentFirewall).
- Removed `code.projects.feature.supply` / `supplyDesc` from all 16 locales.
  Grep found no consumer in flyto-code, flyto-admin (main and
  `catalog-driven-modules` worktrees), flyto-cloud, flyto-console,
  flyto-engine, flyto-landing-page or flyto-vscode, and no dynamic
  `projects.feature.${...}` key construction.
- `dist/` and `manifest.json` rebuilt; `docs/generated/python-symbols.md`
  regenerated.
- `tests/test_module_catalog_copy.py`:
  - reads `internal/modulecatalog/catalog.yaml` and requires every
    `title_key` / `description_key` to resolve as `code.<key>` in en, zh-TW,
    zh-CN and ja (the engine's PRIMARY_LOCALES);
  - catalog lookup: `FLYTO_ENGINE_CATALOG` (must exist if set), else a
    `flyto-engine` sibling of any ancestor directory, so agent worktrees reach
    the workspace clone. With `CI=true` and no catalog it fails, never skips;
  - the English-derived pair check is removed: it could not see a key missing
    from en and was a second, implicit module list.
- `.github/workflows/validate.yml`: sparse checkout of
  `flytohub/flyto-engine@main:internal/modulecatalog/catalog.yaml` into
  `.sync-source/flyto-engine`, `FLYTO_ENGINE_CATALOG` exported to `npm test`.

## Why

Warroom's "Modules & licences" table rendered raw keys (`core`, `vrm`,
`supply_chain_intelligence`). The engine catalog is the only module registry;
this repo only supplies copy for the keys it names. Review found the
catalog contract test skipped in CI and in worktrees, so the contract was not
enforced. It now runs and fails in CI.

## Merge order

Merge this before flyto-engine `claude/catalog-titles`; the engine's i18n
check reads this repo's code locales.

## Verified

- `python3 scripts/validate.py --strict`: PASS, 0 errors.
- `python3 scripts/build-dist.py` + `build-seo-manifest.py`: done.
- `npm test` (no env): 0 skipped; the catalog test found the workspace
  `flyto-engine` clone through the ancestor lookup.
- Catalog test with `CI=true` against three catalogs: engine `origin/main`,
  the workspace `flyto-engine` checkout, and the engine `catalog-titles`
  worktree (including its uncommitted thirdPartyMonitoring /
  codeSecurityAutofix keys): all pass.
- Negative: blanking ja `code.projects.feature.vrm` fails the test;
  `CI=true FLYTO_ENGINE_CATALOG=/nope` fails with CatalogNotFound.
- ruff 0.15.15 (the pinned version), `compileall`, `generate-reference.py`:
  pass.
- `flyto-index verify --strict` in the worktree: see the commit report.

## Not verified

- The authoritative catalog-copy gate is flyto-engine's `catalog-copy` CI job
  (flyto-engine reads this public repository). This repository is public and
  must not read the internal engine, so `validate.yml` gains no engine
  checkout and needs no secret; the test here runs only when a workspace
  checkout or `FLYTO_ENGINE_CATALOG` provides the catalog, and skips otherwise.
- No native-speaker review of zh-TW / zh-CN / ja copy.
- The 12 other code locales render these keys through each consumer's
  `fallbackLocale`; no consumer's i18n setup was checked or tested.
- `contMon` / `addons` keys are kept: other surfaces may still use them once
  the engine stops referencing them. Not audited.

## Follow-ups

- None for the gate: flyto-engine `catalog-copy` covers it.
