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
