# Demo-path copy: no rooms, no mixed-language labels

Owner: claude
Branch: claude/demo-path-copy
Date: 2026-10-02

## What changed

Found by walking the demo path (workflows page → AI Space → Mission Station)
on a local build after flyto-cloud #418.

- `locales/cloud/*/spaceOperations.json` (en, zh-TW, zh-CN): `spaces.guide.help`,
  `spaces.guide.railLabel`, `spaces.ops.live`, `spaces.roomInfo.title` and
  `spaces.narrative.failure.unverifiedResult` say Mission Station instead of
  "room".
  `spaces.roomInfo.link`, `.tasks` and `.spaceId` read Connection / 連線,
  Open tasks / 進行中任務 and Space ID.
- `locales/cloud/*/aiSpace.json`:
  - `aiSpace.workspace.featureMissions` is now Mission cards / 任務卡 / 任务卡.
  - New key `aiSpace.resources.machineBindings.noRunnableWorkflows`.
- `locales/cloud/*/templateBuilder.json`: the `templateBuilder.missionSetup.*`
  title, discard and save-error strings name Mission cards setup. The station
  kind strings say zone kind.
- `locales/cloud/*/templateFolders.json`: `templateFolders.allTemplates` names
  workflows.
- `locales/modules/{zh-TW,zh-CN}/warroom.json`: Warroom module labels say
  Warroom.
- Tests:
  - module label pins, `spaces.ops.live` pins and the runner-binding key set
    (23 → 24) are updated;
  - the cumulative key count is 12,519 → 12,520;
  - the three runtime value digests are re-pinned, with a comment.

## Verified

- `npm run lint`, `npm test` (120 passed), `npm run build` and `npm run verify`,
  with the pinned venv (Python 3.12, ruff 0.15.15).
- `python3 scripts/validate.py --strict`: 4,896 files, 0 errors.

## Not verified

- Other locales keep their own wording for the changed English strings.
- The Cloud side (bundled sync, the new key's reader) lands in the matching
  flyto-cloud pull request.
