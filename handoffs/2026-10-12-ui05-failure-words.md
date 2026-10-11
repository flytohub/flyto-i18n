# UI-05 failure words for flyto-cloud

Owner: claude
Branch: claude/w3-copy
Date: 2026-10-12

## What changed

Ten keys flyto-cloud's UI-05 work (operator words for every Settings and form
failure) added to its bundled catalogs, now in the source of truth, in en,
zh-TW and zh-CN:

- `errors.code.FORBIDDEN`, `errors.code.RATE_LIMITED`,
  `errors.code.SERVICE_UNAVAILABLE`, `errors.code.UNAUTHORIZED`
  (`locales/cloud/*/errors.json`)
- `spaces.triggers.inbound.actionFailed`, `.createFailed`, `.loadFailed`
  (`locales/cloud/*/spaceOperations.json`)
- `subscriptions.cancelFailed`, `subscriptions.upgradeFailed`
  (`locales/cloud/*/subscriptions.json`)
- `triggers.cronCheckFailed` (`locales/cloud/*/triggers.json`)

Values are copied verbatim from flyto-cloud's bundled en / zh-TW / zh-CN.
`dist/` rebuilt (`make build`); the cumulative Cloud key ledger moves to 14,105.

## Why

flyto-cloud's `scripts/check-i18n.py` reported the ten keys as present in its
bundles but deleted from `dist/cloud/`, and six of them as orphans.

## Verified

- `make test`: validate --strict, coverage, pytest 133 passed / 1 skipped.
- `make build`; ruff on scripts/tests; generate-reference check.

## Not verified

- Other locales fall back to English for these ten keys, as for prior copy PRs.

## Follow-ups

- flyto-cloud: run `scripts/check-i18n.py --fix` against this commit.
