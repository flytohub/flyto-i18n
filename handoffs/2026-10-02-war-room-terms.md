# One name for the War Room, one for Mission Stations

Owner: claude
Branch: claude/war-room-terms
Date: 2026-10-02

## What changed

- `locales/cloud/{en,zh-TW,zh-CN}`: 67 strings. zh-TW 作戰室 and zh-CN 作战室
  became 戰情室 / 战情室. English "Operations room" / "Operations Room" became
  "War Room". The Mission Stations tab and panel title became "Mission
  Stations" / 任務站點 / 任务站点. The other 13 Cloud locales do not carry
  these keys and fall back to English.
- `dist/**` and `docs/generated/**` were regenerated.
- Two tests pinned the old copy and were updated. The English key count in
  `test_cloud_runtime_cumulative_keys.py` was already failing on `main`
  (12,519 vs 12,506, from the 13 Agent Hub keys in #160) and is corrected.

## Why

flyto-cloud's architecture docs (flyto-cloud #414) now define the War Room as
a Space's control room at `/spaces/:id`. The UI used two Chinese names for it,
and gave its own name to a settings tab that configures something else.

## Verified

Run with the pinned requirements (Python 3.12, ruff 0.15.15):

- `npm run lint`, `npm run verify` (including `validate.py --strict` and
  pytest, 120 passed), `npm test` and `npm run build` all passed.

## Not verified

- The rendered Cloud UI. flyto-cloud's bundled copy and code fallbacks are
  updated in a follow-up flyto-cloud PR after this merges.
