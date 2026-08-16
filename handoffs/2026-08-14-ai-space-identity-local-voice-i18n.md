# AI Space identity and local-voice i18n closure

Date: 2026-08-14

## Scope

I1 adds exactly 19 `aiSpace.settings.*` identity and local-voice keys to all 16
Cloud locale catalogs. The owner catalog is
`locales/cloud/<locale>/aiSpace.json`; the generated outputs are the matching
`dist/cloud/<locale>.json` and aggregate `dist/<locale>.json` bundles, their
manifests, and repository-manifest coverage.

## Implementation

- Preserved the existing eight `aiSpace.settings.*` keys and unrelated catalog
  values while adding the exact 19-key contract in every locale.
- Kept the reviewed English, Traditional Chinese, and Simplified Chinese copy
  exact and required every other locale to provide non-empty localized copy
  instead of a wholesale English fallback.
- Applied the audited translation corrections: Korean `identity` is exactly
  `정체성`; Indonesian `voiceLocale` is exactly `Lokal pengenalan suara`; and
  Hindi `voiceSafety` is exactly `सक्रियण शब्द केवल आपको इस Space तक ले जाते
  हैं। वे अनुमति नहीं देते और अनुमोदन को दरकिनार नहीं करते।`
- Regenerated both distribution shapes and manifests from the source catalogs.
  Focused regression coverage checks exact19/all16 ownership and localization,
  the existing eight suffixes, reviewed three-locale copy, source equality in
  both generated shapes, and manifest totals against flattened translations.

## Gates and boundary

The governed gates are the focused unittest, strict catalog validation,
`npm run verify`, deterministic second-pass distribution/reference generation,
and strict Indexer verification. Cloud UI/runtime adoption is downstream and is
not part of I1. This repository change does not modify, deploy, or validate a
consumer UI or runtime.
