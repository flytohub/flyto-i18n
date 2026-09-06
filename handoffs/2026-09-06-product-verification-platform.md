# Product Verification platform catalog

The `productVerification.platform` namespace adds 103 keys across 16 Code
catalogs. English, Traditional Chinese, and Simplified Chinese are reviewed;
other locales retain explicit English fallback text. Source catalogs own all
copy; generated distributions and manifests are rebuilt from those sources.

The catalog covers suite/case/step configuration, environment and adapter
setup, run lifecycle, evidence, retry, and all eight runtime outcomes. It does
not claim that unavailable adapters ran or that a missing receipt passed.

Full `npm run verify` passed with 4,816 valid catalogs, 107 tests and 2,702
subtests. The frontend must consume the final exact catalog revision before
its own release checks. Product UI and deployed acceptance remain pending;
this change does not authorize public publication.

All 103 keys passed canonical distribution generation after integration of
AI Gate and Adoption main at eb97d6c1c18ddf1d0de52f0c329b8fb265d59195.
Strict verification passed 19 checks with no warnings or failures. The final
locale batch passed complete pytest and artifact intent validation; intermediate
per-locale checkpoints required remaining manifest generation and were not
release candidates. Consumer pinning must use this PR's actual merge SHA.
