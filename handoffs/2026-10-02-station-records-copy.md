# Mission Station records in words, and the Agents tab

Owner: claude
Branch: claude/demo-path-layout-copy
Date: 2026-10-02

## What changed

New keys (cumulative English count 12,520 → 12,600). Each family is keyed by
the identifier the backend serves, so Cloud builds the key from the value and
holds no copy of the backend's set:

- `spaces.hud.gate.<gate>`:
  - Gate ids come from `assignment_types.GATE_*`.
- `spaces.hud.gateSkip.<code>`:
  - The codes come from `assignment_types.SKIP_CODES`, which Cloud now serves
    beside each skipped gate's sentence.
- `spaces.hud.refusal.<code>`:
  - The codes come from `refusals.REASON_*`.
- `spaces.hud.orderBasis.<basis>`:
  - The values are `travel_time` and `dispatch_preference`.
- Evidence keys (from `evidence_models`):
  - `spaces.hud.evidenceState.<STATE>`;
  - `spaces.hud.reason.<code>`;
  - `spaces.hud.waitsOn.<human|system>.decision`;
  - `spaces.hud.conclusion.<CONCLUSION>`;
  - `spaces.hud.conclusionMeaning.<CONCLUSION>`;
  - `spaces.hud.conclusionMissing`;
  - `spaces.hud.reasonObserved` / `reasonRequired`.
- `spaces.timeline.source.<source>`:
  - The sources come from `decisions.SOURCE_*`, plus `unknown`.
- `spaces.timeline.originalNote`.
- `aiSpace.agents.*` and `aiSpace.workspace.tabs.agents`.

Changed values:
- `aiSpace.resources.inertMachines` and `inertMachinesHint`;
- `templateToolbar.searchPlaceholder` and `searchLabel`.

## Verified

- `npm run lint`, `npm test` (120 passed), `npm run build` and `npm run verify`,
  with the pinned venv (Python 3.12, ruff 0.15.15).
- The Cloud side has a spec that reads `assignment_types.py` and fails when a
  gate or skip code has no en or zh-TW copy.

## Not verified

- Locales other than en, zh-TW and zh-CN keep English for the new keys.
