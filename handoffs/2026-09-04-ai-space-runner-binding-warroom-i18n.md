# AI Space runner binding and War Room dispatch i18n

Owner: codex
Branch: codex/ai-space-runner-binding-i18n
Date: 2026-09-04

## What changed

- Added 23 reviewed keys to `locales/cloud/{en,zh-TW,zh-CN}/aiSpace.json`
  for workflow runner placement, runner save state, and the War Room's
  dispatchable-workflow inventory.
- Rebuilt the corresponding tracked Cloud and aggregate distribution bundles.
- Added `tests/test_ai_space_runner_binding_catalog.py` to pin the exact key
  set, reviewed copy, unique ownership, placeholder parity, and distribution
  equality.
- Updated project state, decision, changelog, tasks, and this handoff registry.

## Why

AI Space needed an explicit workflow-to-machine tree without implying that a
robot, camera, NAS endpoint, or adapter is itself the workflow runner. The copy
now preserves the authority boundary: War Room schedules across capabilities,
AI Space executes locally, and hardware retains its own refusal logic.

## Verified

- `.venv/bin/python -m pytest -q tests/test_ai_space_runner_binding_catalog.py`
  — 4 passed.
- `.venv/bin/python scripts/validate.py --strict` — 4,784 files validated,
  zero errors.
- `python3 scripts/build-dist.py` — rebuilt all distributions; official Cloud
  catalogs contain 12,187 keys and aggregate catalogs contain 24,593 keys.
- `PATH="$PWD/.venv/bin:$PATH" npm run verify` — lint, generated-reference
  freshness, deterministic builds, strict catalog validation, and all 105
  tests passed.

## Not verified

- The consuming Flyto Cloud frontend verification is recorded in that
  repository's own handoff after synchronization.

## Follow-ups

- Native translations for non-official Cloud locales can be added later; they
  continue using the repository's existing fallback behavior.
