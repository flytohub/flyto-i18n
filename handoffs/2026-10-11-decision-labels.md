# Decision-process clearance labels

- Owner: claude
- Branch: claude/decision-labels
- Status: PR opened with auto-merge

## What changed

- `decisionProcess.fact.clearance_m` and `decisionProcess.code.clearance_minimum`
  in en / zh-TW / zh-CN (`locales/cloud/*/decisionProcess.json`).
- `dist/` rebuilt with `scripts/build-dist.py`; ledger in
  `tests/test_cloud_runtime_cumulative_keys.py` moved to 14,093.
- Consumer: flyto-cloud `composables/spaces/decisionProcess/codeWords.js`
  (code -> words, falling back to `decisionProcess.code.<code>`).

## Verified

- `python3 scripts/validate.py --strict`: 4918 files, 0 errors.
- `python3 -m pytest -q`: 133 passed, 1 skipped.
- `python3 scripts/generate-reference.py`: current.

## Not verified

- flyto-indexer `verify --strict` was not run on this repository.
