# Module commerce copy (flyto-code Phase 1f)

Owner: claude
Branch: claude/ops-copy
Date: 2026-10-04

## What changed

- `locales/code/{en,zh-TW,zh-CN}/code.json`: about 100 new `code.*` keys for
  module licences, coverage tiles, request dialog, read-only banners, gate
  reasons (`code.modules.gate.*`, `code.modules.reason.*`) and entitlement
  toasts.
- `code.entitlement.actionRequired*` now says to contact an org admin instead
  of suggesting an upgrade, in all three locales.
- Review follow-up: `code.projects.coverage.cta.askOwner`,
  `code.projects.wizard.viewerAccountsNote`, `code.projects.wizard.modulesFailed`,
  `code.projects.wizard.openProject` and `code.projects.wizard.retryModules`
  for the flyto-code wizard and coverage fixes, in all three locales.
- `dist/` rebuilt with `scripts/build-dist.py`.

## Why

flyto-code `claude/ops-handoff` renders the engine's per-module entitlement
answer. Old `openBilling`, `freeNote` and `actionRequired` keys stay because
src-product (CE) still uses them. Other locales fall back to English, as in #175.

## Verified

- `python3 scripts/validate.py --strict`: PASS, 0 errors.
- `python3 -m unittest discover -s tests`: 75 tests OK.
- `flyto-index verify . --strict --json`: 21/21 pass.
- flyto-code `npx vitest run` and `npm run release:gate` pass against this dist.

## Not verified

- MCP `verify(strict=true)` / `task(action='validate')` (MCP pinned elsewhere).
- No translation review by a native speaker.

## Follow-ups

- After merge, bump the flyto-i18n SHA pinned in flyto-code
  `.github/workflows/ci.yml` and `deploy-cloudflare.yml`.
