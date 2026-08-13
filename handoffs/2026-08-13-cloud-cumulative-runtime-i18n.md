# Cloud cumulative runtime i18n closure

Date: 2026-08-13

## Scope

Cloud PR156 exposed a cumulative catalog split: the accepted local Cloud bundle
contained 134 reviewed runtime keys not present in the current generated i18n
Cloud bundle, while i18n already contained newer Space Operations additions.
The Cloud checkout was used as read-only provenance and was not modified.

## Implementation

- Corrected `aiSpace.workspace.openOperations` to the accepted Cloud UI labels
  `Operations room`, `作戰室`, and `作战室`. A focused regression pins the exact
  three-locale contract and source-to-Cloud-dist equality.
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
  tracked Cloud output. The final integration seal builds the complete Cloud
  manifest in memory through the selective distribution API, requires exact
  equality with tracked `dist/cloud/manifest.json`, pins complete English,
  Traditional Chinese, and Simplified Chinese records at 11,842 keys and 254
  files, and exercises `--scope cloud --locale en` against a temporary
  destination to reject manifest truncation.
- Rebuilt tracked Cloud, Flow, aggregate, manifest, and generated Python-symbol
  outputs. No Cloud file, credential, deployment, commit, or remote was touched.

## Verification

- The focused cumulative runtime suite passed all 6 tests.
- `python3 scripts/validate.py --strict`: 4,598 files, zero errors.
- `PYTHONPYCACHEPREFIX=/tmp/flyto-i18n-pycache npm run verify`: passed generated
  reference freshness (299 declarations), strict validation, coverage, 68 unit
  tests, distribution generation, and SEO generation.
- `PYTHONPYCACHEPREFIX=/tmp/flyto-i18n-pycache flyto-index verify . --strict
  --json`: 19 pass, 0 warn, 0 fail; fingerprint
  `2d0b13986cdccdafda951e9484a04d0d065506a2d49b363c36e2fef271e2f4bb`.
