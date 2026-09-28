# SPM rating explanation copy — 2026-09-28

## Scope

Canonical Code copy for flyto-code's first-party SPM Rating Tree. The consumer
renders Engine-authored rating/vector/finding explanation data; this repository
owns the labels only and does not define scoring behavior.

## Added source keys

- 19 `code.external.ratingTree*` keys in English and Traditional Chinese.
- Other locales intentionally use the existing English fallback contract for
  these additive keys.

The boundary note is explicit: domain penalty points are domain-level scorer
deductions, not additive organization-rating points. Projected gains remain
model output until re-observed or verified.

## Verification

- `python3 scripts/validate.py --strict --project code`: PASS, 102 files, 0 errors.
- `python3 scripts/build-dist.py`: tracked Code and aggregate distributions rebuilt.
- `git diff --check`: PASS.
- `npm run verify` reaches the repository-wide Python lint step but is blocked by
  203 pre-existing ruff/executable-bit findings in unrelated scripts/tests on
  current upstream main. No changed file in this copy-only patch is part of
  that Python lint surface.

Consumer UI verification and deployment are recorded in flyto-code.
