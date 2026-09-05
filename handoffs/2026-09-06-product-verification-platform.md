# Product Verification platform catalog

The `productVerification.platform` namespace adds 103 keys across 16 Code
catalogs. English, Traditional Chinese, and Simplified Chinese are reviewed;
other locales retain explicit English fallback text. Source catalogs own all
copy; generated distributions and manifests are rebuilt from those sources.

The catalog covers suite/case/step configuration, environment and adapter
setup, run lifecycle, evidence, retry, and all eight runtime outcomes. It does
not claim that unavailable adapters ran or that a missing receipt passed.

Full `npm run verify` passed with 4,800 valid catalogs, 105 tests and 2,702
subtests. The frontend must consume the final exact catalog revision before
its own release checks. Product UI and deployed acceptance remain pending;
this change does not authorize public publication.

The initial 94-key snapshot passed the full suite and deterministic rebuild.
Nine additional form and evidence labels are now included in source; final
distribution verification remains required before consumer pinning.
