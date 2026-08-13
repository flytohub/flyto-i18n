# Cloud cumulative runtime i18n closure

Date: 2026-08-13

## Scope

Cloud PR156 exposed a cumulative catalog split: the accepted local Cloud bundle
contained 134 reviewed runtime keys not present in the current generated i18n
Cloud bundle, while i18n already contained newer Space Operations additions.
The Cloud checkout was used as read-only provenance and was not modified.

## Implementation

- Additively imported exactly 59 `aiSpace.*`, 25 `myTemplates.*`, and 50
  `templateBuilder.missionSetup.*` values into the English, Traditional Chinese,
  and Simplified Chinese source catalogs.
- Added reviewed `accessibility.modal` copy in the same official locales.
- Preserved the complete pre-existing dirty baseline, including all 21
  `spaces.draw.*` and `spaces.voice.*` keys and their fail-closed additions.
- Added `tests/test_cloud_runtime_cumulative_keys.py` to pin the exact 134-key
  namespace/count contract, unique designated source-catalog ownership, and
  canonical per-locale value digests from the accepted Cloud provenance. It
  also pins official-locale non-empty and placeholder parity, source-to-dist
  identity, modal coverage, Space Operations preservation, and deterministic
  tracked Cloud output.
- Rebuilt tracked Cloud, Flow, aggregate, manifest, and generated Python-symbol
  outputs. No Cloud file, credential, deployment, commit, or remote was touched.

## Verification

- `python3 scripts/build-dist.py`: completed; official Cloud bundles contain
  11,842 keys across 254 source files.
- The focused cumulative runtime suite now declares 5 tests (previously 3).
- `python3 scripts/validate.py --strict`: 4,598 files, zero errors.
- `PYTHONPYCACHEPREFIX=/tmp/flyto-i18n-pycache npm run verify`: passed generated
  reference freshness (271 declarations), strict validation, coverage, 56 unit
  tests, distribution generation, and SEO generation.
- `PYTHONPYCACHEPREFIX=/tmp/flyto-i18n-pycache flyto-index verify . --strict
  --json`: 19 pass, 0 warn, 0 fail; fingerprint
  `2d0b13986cdccdafda951e9484a04d0d065506a2d49b363c36e2fef271e2f4bb`.
