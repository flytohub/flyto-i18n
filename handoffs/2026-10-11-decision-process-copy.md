# Decision-process view and station copy

Owner: claude
Branch: claude/decision-process-copy
Date: 2026-10-11

## What changed

- New namespace `locales/cloud/{en,zh-TW,zh-CN}/decisionProcess.json`
  (category `cloud.decisionProcess`, 97 keys) for flyto-cloud's
  decision-process view (`GET /api/spaces/{space}/tasks/{task}/decision-process`).
- 24 new `spaces.lifecycle.*`, `spaces.receipt.*` and `spaces.station.*` keys
  in `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`.
- `dist/` rebuilt with `scripts/build-dist.py`; the ledger in
  `tests/test_cloud_runtime_cumulative_keys.py` moves to 14,084 keys and 266
  merged files.

The values are exactly the ones flyto-cloud's bundled catalogs carry on
`claude/converge-20261011`, so syncing the bundles back is a no-op diff.

## Why

flyto-cloud's bundled catalogs are generated from this repository; keys added
there first would be dropped by the next `check-i18n.py --fix`.

## Verified

- `python3 scripts/validate.py --strict`: 4918 files, 0 errors.
- `python3 -m pytest -q`: 134 passed.
- `python3 scripts/generate-reference.py`: current.
- `npm run verify`: see the PR checks.

## Not verified

- Other locales carry no copy for these keys (they fall back to English),
  as with the other newer Cloud keys.

## Follow-ups

- None.
