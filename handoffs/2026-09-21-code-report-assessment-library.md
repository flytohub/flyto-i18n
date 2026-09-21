# 2026-09-21 — Code report and assessment library copy

## Scope

Flyto2 Code now presents Reports and Assessments as separate first-class
library concepts, with the same terminology reused by the CTEM compliance
dialog. This catalog change supplies the reviewed runtime copy only; Code owns
the UI, Engine owns compliance evaluation, and this repository does not claim
consumer deployment.

## Copy contract

Added 24 source-owned keys for:

- Report Library and Assessment Library tabs, counts, search results and format
  metadata.
- Evidence-backed assessment state, evaluated-control counts, explicit
  pass/partial/fail counts and the honest not-assessed state.
- Evidence-pack, report-editor and control-review actions.
- CTEM compliance-dialog tabs and the Report Center handoff.

English, Traditional Chinese and Simplified Chinese carry reviewed copy. The
remaining Code locales use the existing explicit English-fallback pattern for
these additive keys; existing translations were not replaced.

## Truth boundary

The assessment wording is intentionally evidence-aware. A framework without a
current Engine evaluation is labelled not assessed; missing evidence is never
presented as a pass. The UI may expose only frameworks actually implemented by
the Engine, rather than mirroring third-party framework catalogs that Flyto2
cannot evaluate.

## Verification

- `python3 scripts/validate.py --strict`: PASS, 4,854 source catalog files,
  zero errors.
- `python3 scripts/build-dist.py`: PASS; Code and aggregate distributions
  regenerated for all 16 Code locales.
- Consumer browser, TypeScript, report/CTEM component tests and release gates
  remain Code-owned and are recorded in its paired handoff.
