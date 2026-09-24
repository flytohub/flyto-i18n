# SPM infrastructure attribution i18n — 2026-09-24

Repository: flyto-i18n  
Branch: codex/spm-infrastructure-i18n  
Consumer: flyto-code / codex/spm-infrastructure-authority-ui

## Scope

Add the canonical copy required by Flyto2 first-party SPM infrastructure
attribution controls without changing runtime ownership or scoring authority.

## Added

27 Code keys covering:
- Domain / IP / CIDR / ASN infrastructure labels
- attribution authority and evidence labels
- company-provided vs independent-evidence receipts
- end-attribution vs review-required removal states
- domain-attribution confirmation copy

English, Traditional Chinese and Simplified Chinese are reviewed. The remaining
Code locales use the established explicit English fallback for these additive
keys. Existing locale keys are unchanged.

## Truth boundary

The copy does not say an operator can erase authoritative ownership evidence.
Independent evidence remains review-gated. Runtime attribution behavior belongs
to flyto-engine; presentation belongs to flyto-code.

## Verification

Completed locally:
- `python3 scripts/validate.py --strict` — 4,854 catalogs, 0 errors.
- `python3 scripts/build-dist.py` — all tracked scopes rebuilt successfully.
- `git diff --check` — clean.

Consumer CI must bump its pinned flyto-i18n SHA after this change lands.
