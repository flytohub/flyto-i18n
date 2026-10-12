# Rejected routes label for flyto-cloud

Owner: claude
Branch: claude/one-merge-copy
Date: 2026-10-12

## What changed

One new key, `decisionProcess.omitted.rejected_routes`, in
`locales/cloud/{en,zh-TW,zh-CN}/decisionProcess.json`, values copied verbatim
from flyto-cloud's bundled catalogs on claude/converge-20261012 (which carried
it first). `dist/` rebuilt; the cumulative Cloud key ledger moves to 14,227.

## Verified

- `make docs-check test build` (generate-reference, validate.py --strict,
  coverage.py, pytest, build-dist, build-seo-manifest) passed on this branch.

## Not verified

- `make lint` locally: the local ruff reports 20 pre-existing findings in
  untouched scripts; CI is the judge.
- Other locales fall back to English for this key.

## Follow-ups

- flyto-cloud: run `scripts/check-i18n.py --fix` against this commit.
