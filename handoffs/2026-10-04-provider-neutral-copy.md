# Provider-neutral equipment copy

Owner: claude
Branch: claude/provider-neutral-copy (PR #179)
Date: 2026-10-04

## What changed

`locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json` and `aiSpace.json`:
new `spaces.kind.equipment`, `spaces.hud.evidenceKind.resource.arrival`,
`spaces.hud.verdict.*`; robot wording in AI Space hints, placeholders, live and
range-scan copy made neutral. Legacy `spaces.hud.sweep.*` and
`spaces.kind.robot` kept for released-Desktop tasks. dist rebuilt.

## Verified

`make test` (validate --strict: 0 errors) and `make build`.

## Not verified

Rendered only through flyto-cloud vitest, not in a browser.

## Follow-ups

Retire `spaces.hud.sweep.*` and `spaces.kind.robot` when Cloud's legacy
compat package is removed.

## Review fix (2026-10-04, Owner: claude)

CI `validate` (pytest) failed on `test_complete_cloud_manifest_survives_selective_build`:
the English total grew by this branch's seven keys (12,987 -> 12,994). `make test`
(unittest) does not run that assertion. Fixed in `586492e42`; pytest 120 passed,
CI validate green.
