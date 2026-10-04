# Words for a recovery stopped by the computer's AI

Owner: claude
Branch: claude/recovery-failure-copy (PR #182)
Date: 2026-10-04

## What changed

`locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`: new
`spaces.narrative.errorCode.planner_unavailable` and `.planner_timeout`, and
`spaces.timeline.stage.continuation_unavailable` reworded (the computer was
reached; its AI could not continue). dist rebuilt.

`tests/test_cloud_runtime_cumulative_keys.py`: English total 13,290 -> 13,292.

`Makefile`: `make test` runs pytest instead of `unittest discover`.

## Why

flyto-cloud reports `planner_unavailable` / `planner_timeout` when a recovery
stops because the selected computer's AI could not answer; without the keys
the narrative after "Gave up" showed the raw code.

`make test` used `unittest discover`, which does not collect function-style
pytest tests, so it reported green while CI's `npm test` (pytest) failed on
the key total. The same miss happened on PR #179. It now runs the CI runner.

## Verified

Rebased on main 14c765d53. `make test` (validate --strict PASS, 127 pytest
passed), `npm test` (127 passed), `make build`, `scripts/generate-reference.py`
current. The three keys present in `dist/{en,zh-TW}.json` and
`dist/cloud/en.json`.

## Not verified

`ruff check` was not run with CI's ruff version locally; CI lint is the gate.
Not rendered in a browser.

## Follow-ups

flyto-cloud's bundled baseline (`src/ui/web/frontend/src/i18n/bundled/`)
lacks these keys until its i18n sync runs; the CDN loader reads
flyto-i18n `main` at runtime.
