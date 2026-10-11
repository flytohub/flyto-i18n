# Live channel words for flyto-cloud

Owner: claude
Branch: claude/live-copy
Date: 2026-10-12

## What changed

Thirty `spaces.live.*` keys flyto-cloud's Live channels (`flyto.live-channels.v1`
tiles on the station and the resource detail) read, in en, zh-TW and zh-CN,
added to `locales/cloud/*/spaceOperations.json` beside the existing
`spaces.live.*` frame-viewer keys:

- `spaces.live.kind.{video,scan,pose,telemetry}`
- `spaces.live.phase.{connecting,live,stale,ended,unavailable}`
- `spaces.live.reason.{hostOffline,notApproved,notDeclared,unsupported,noAddress,expired,revoked,closed,sourceUnreachable,sourceUnusable}`
- `spaces.live.{title,titleFor,loading,noneDeclared,unavailable,waiting,retry,scanAlt,scanAltEmpty,poseAlt,poseAltEmpty}`

English values are flyto-cloud's in-code fallbacks verbatim; zh-TW and zh-CN
follow the catalog's existing Live words (即時 / 畫格). `dist/` rebuilt; the
cumulative Cloud key ledger moves to 14,135.

## Why

flyto-cloud's `scripts/check-i18n.py` reported the keys as unbundled and
`sync-from-cloud.py --check` as missing from the catalog.

## Verified

- `validate.py --strict` (0 errors), `coverage.py`, pytest 133 passed /
  1 skipped, `build-dist.py`, `build-seo-manifest.py`, `generate-reference.py`.

## Not verified

- Other locales fall back to English for these thirty keys, as for prior copy PRs.
- No native-speaker review of the zh-CN wording.

## Follow-ups

- flyto-cloud: run `scripts/check-i18n.py --fix` against this commit.
