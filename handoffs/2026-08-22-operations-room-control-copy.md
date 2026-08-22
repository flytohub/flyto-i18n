# Operations Room control-copy closure

Date: 2026-08-22

## Scope

The three reviewed Cloud locales now own the output-wall labels, exact-target
selection errors, optional mission-input label, protocol/status labels, and
management entry used by the live Flyto2 Cloud Operations Room.

## Ownership boundary

`flyto-i18n` remains the source of truth. Flyto2 Cloud's bundled JSON is a
consumer projection and may be replaced only by a current `dist/cloud` build;
it must not carry keys absent from the reviewed source catalogs.

## Verification contract

The cumulative Cloud runtime regression pins exact values, sole non-empty
catalog ownership, placeholder parity, and equality through both `dist/cloud`
and aggregate bundles. Required host verification is:

- `python3 scripts/validate.py --strict`
- `python3 scripts/build-dist.py`
- `npm run verify`
- `flyto-index verify . --strict --json`
