# Attack validation safety, benchmark, and cost i18n

Date: 2026-07-29

## Outcome

The Code catalog now covers the full attack-validation product closure:
proof-of-control, proof-pack digest and eligibility, tenant-local benchmark
rates and exclusions, exact allowlists, tamper-evident audit status,
workspace/campaign/run hard budgets, settlement, and the emergency kill switch.
The 65-key addition also exposes complete benchmark method and outcome
populations, proof stages and causal references, audit-chain context, and
versioned control-change context.

English, Traditional Chinese, and Simplified Chinese values are reviewed. The
other supported Code locales were synchronized through the canonical locale
tooling so key parity remains deterministic.

## Verification

- `python3 scripts/sync-locales.py --project code`
- `python3 scripts/validate.py --strict`
- `python3 scripts/build-dist.py`
- `npm run verify`
- strict validation covered 4,560 locale files with zero errors
- strict Indexer verification and Gitleaks both passed with zero secret
  findings

The resulting tracked `dist/code`, aggregate bundles, manifests, and locale
metadata are part of this change. The frontend worktree consumed the generated
Code bundles for Vitest and production-build evidence.
