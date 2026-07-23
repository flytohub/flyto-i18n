# CE Direct Repository Onboarding i18n

Warroom CE now has bundled locale keys for the direct public repository URL
dialog: title, description, field label, supported-host hint, connect action,
connect/scan progress, and URL validation failures. English and Traditional
Chinese carry reviewed copy; the remaining supported code locales contain
synchronized fallback entries.

Verification:

- `python3 scripts/validate.py --strict`
- `python3 scripts/build-dist.py`

The generated `dist/code`, aggregate `dist`, and manifests are tracked release
artifacts. No credentials, tokens, or API keys are part of the copy.
