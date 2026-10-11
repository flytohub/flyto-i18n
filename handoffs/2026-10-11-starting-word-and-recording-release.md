# The Start button's in-flight word; recording upload names Desktop 0.7.13

Owner: claude
Branch: claude/narrative-starting-0713
Date: 2026-10-11

## What changed

- `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`: new key
  `spaces.narrative.action.starting` ("Starting…" / 「啟動中…」 / 「启动中…」).
  flyto-cloud #513 already reads it on the Needs you Start button while the
  Start request is in flight, with an English fallback.
- `locales/cloud/{en,zh-TW,zh-CN}/aiSpace.json`:
  `aiSpace.resources.dispatchRules.uploadRecordingsRequires` names Desktop
  0.7.13 instead of 0.7.12. v0.7.12 was tagged but never published
  (flytohub/flyto2 has v0.7.11, then v0.7.13).
- `dist/**` rebuilt with `scripts/build-dist.py`.
- Tests: `tests/test_cloud_runtime_copy.py` gains two tests;
  `tests/test_cloud_runtime_cumulative_keys.py` count 13,958 -> 13,959.
- Merged in the same session: #206 (`fix/cloud-safe-send-20261011`, squash
  5d07579b4), the safe-send and receipt provenance keys.

## Why

The released Desktop is 0.7.13; the copy pointed operators at a version that
does not exist. The in-flight word was English-only in zh locales.

## Verified

- The two new tests fail on origin/main 5d07579b4 (2 failed, 1 passed) and
  pass here.
- `python3 scripts/validate.py --strict`: 4,915 files, 0 errors.
- `python3 -m pytest -q`: 133 passed, 1 skipped.
- `flyto-index verify --strict`: 21 PASS, exit 0.

## Not verified

- flyto-cloud's bundled catalogs are synced in the paired flyto-cloud PR
  (`claude/closure-d7-c7-20261011`); until it lands, flyto-cloud's i18n Sync
  Check on main reports the dist as stale.
- jsDelivr purge runs from `purge-cdn.yml` on the push to main; its output was
  not inspected beyond the run status.

## Follow-ups

- PR #207 (`claude/destination-blocked-copy`) adds one key too and must bump
  the cumulative count to 13,960 after this lands.
