# Module Marketplace copy (模組商城)

Owner: claude
Branch: claude/module-marketplace-copy
Date: 2026-10-04

## What changed

- `locales/cloud/<locale>/modulePacks.json` (new namespace `cloud.modulePacks`,
  164 keys) in all 16 locales; en, zh-TW and zh-CN are written, the other 13
  carry the keys empty, as every new namespace does.
- `plugins.tabs.modulePacks` in every `plugins.json` (en "Module Marketplace",
  zh-TW 模組商城, zh-CN 模块商城).
- `dist/` rebuilt with `scripts/build-dist.py` and `scripts/build-seo-manifest.py`.
- `tests/test_cloud_runtime_cumulative_keys.py`: the Cloud seal moves from
  12,987 to 13,152 (+165) and `files_merged` from 263 to 264, each with its
  ledger line.

## Why

flyto-cloud `claude/module-marketplace` adds the Module Marketplace tab to the
plugin store (browse, install on this computer, publish a private or public
pack, signing keys, administrator review) and one translated sentence per
stable refusal code the marketplace and the Desktop installer return. The
wording is domain-neutral and has no price, checkout, entitlement or trial.

## Verified

- `make test` (validate --strict, coverage, unittest): exit 0, 0 errors.
- `python3 -m pytest -q tests`: 120 passed.
- flyto-cloud `scripts/check-i18n.py --fix --i18n-path <this worktree>` synced
  the bundled baselines; the re-check reports baselines in sync and no
  `modulePacks` orphan (the 16 remaining orphans are `spaces.*` and
  `notifications.*` keys from other unmerged Cloud branches).

## Not verified

- `make lint`: ruff reports 220 findings in `scripts/` and `tests/` that exist
  on `main` too; this change only edits a comment and two numbers in one test.

## Follow-ups

- Merge before (or with) flyto-cloud `claude/module-marketplace`, then re-sync
  that branch's bundled locales from merged `main`.
