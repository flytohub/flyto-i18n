# Mission Station deck words for flyto-cloud

Owner: claude
Branch: claude/polish-copy
Date: 2026-10-12

## What changed

Twenty-two new keys in `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`,
values copied verbatim from flyto-cloud's bundled catalogs on its polish
branch (which carried them first):

- `spaces.lifecycle.stage.{verified,notVerified,unproven,ran,executionFailed,blocked,refused}`
- `spaces.needsYou.{level,submittedBy}`
- `spaces.station.equipmentLabel`, `spaces.station.environment.{physical,simulation}`
- `spaces.receipt.photos`
- `spaces.hud.evidenceFact.{clearance,displacement,rotation,distance_m,speed_mps,yaw_radians,place,clearance_m,minimum_m}`

Twelve zh-TW / zh-CN values changed so one concept has one word (English
unchanged): `spaces.ops.verificationStatusVerified`, `spaces.station.result.verified`,
`spaces.hud.verdict.verified`, `spaces.hud.sweep.verified`, `spaces.receipt.title`,
`spaces.ops.verificationStatusExecutionFailed`, `spaces.narrative.{taskState,stepState,task,step}.blocked`,
`spaces.timeline.stage.blocked`, `spaces.ops.verificationStateBlocked`.
`tests/test_space_verification_loop_catalog.py` pins the new 已驗證 / 已验证.

`dist/` rebuilt; the cumulative Cloud key ledger moves to 14,157.

## Verified

- `validate.py --strict` (0 errors), `coverage.py`, pytest 133 passed /
  1 skipped, ruff clean, `build-dist.py`, `build-seo-manifest.py`,
  `generate-reference.py` current.
- flyto-cloud `scripts/check-i18n.py --i18n-path` against this branch was run
  before the commit to list the keys (orphans and sync check).

## Not verified

- Other locales fall back to English for these keys.
- No native-speaker review of the zh-CN wording.

## Follow-ups

- flyto-cloud: run `scripts/check-i18n.py --fix` against this commit.
