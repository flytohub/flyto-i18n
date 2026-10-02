# Each Space has a Mission Station; War Room is reserved

Owner: claude
Branch: claude/mission-station-terms
Date: 2026-10-02

## What changed

- `locales/cloud/{en,zh-TW,zh-CN}`: 83 strings.
  - The room at `/spaces/:id` is now Mission Station / 任務站點 / 任务站点.
  - The legacy Mission Stations feature is now Mission cards / 任務卡 / 任务卡.
  - The zh Warroom recipe import reads "Warroom".
- `dist/**` and `docs/generated/**` were regenerated.
- Two tests were updated, and the zh runtime value digests were re-pinned.

## Why

This is Chester's naming. War Room is the top layer of the product line, and
it should name the layer above all Spaces, which does not exist yet. A Space's
own control room is its Mission Station. #162 (earlier the same day) had called
the per-Space room War Room. That would have made the future global layer
nameless, and would have kept 戰情室 on screens that are not the War Room.

## Verified

- With the pinned requirements (Python 3.12, ruff 0.15.15): `npm run lint`,
  `npm run verify`, `npm test` and `npm run build` all passed.

## Not verified

- The rendered Cloud UI; flyto-cloud's matching PR follows.
- The repository's gitleaks history scan still fails on `main` with one
  finding that predates this change; it is tracked as a separate task.
