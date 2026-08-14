# Space Operations near-real-time local camera

Date: 2026-08-14

## Scope

The three reviewed Cloud locales now own truthful War Room camera copy in
`spaceOperations.json`. `spaces.ops.live` reports room connection, and
`spaces.ops.subtitle` names mission operations and evidence. Eight additive
camera keys cover local near-real-time frame rate, delayed images, last-image
age, disconnected and permission-denied states, startup, on-device privacy,
and accessible image alt text.

## Product boundary

The copy promises local, near-real-time camera images only. It does not claim a
continuous video stream, live camera, inference, or recording. The privacy
label states that camera images stay on the device.

## Generated contract

Canonical distribution generation owns the corresponding `dist/cloud` and
aggregate locale bundles plus their manifests. The cumulative Cloud runtime
test pins exact reviewed values, sole source ownership, `{fps}` and `{seconds}`
placeholder parity, non-empty equality through both distribution layers, and a
guard against false camera-live wording.

## Required host verification

- `npm run verify`
- strict Flyto Indexer verification
- a second canonical distribution build with no resulting diff

No commit, push, publish, or deployment is part of this handoff.
