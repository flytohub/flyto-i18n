# Module editions copy (Basic / Full, purchase page)

Owner: claude
Branch: claude/module-editions-copy (on top of 730564f52, the catalog name alignment)
Date: 2026-10-04

## What changed

Flat `code.*` keys in `locales/code/{en,zh-TW,zh-CN,ja}/code.json`, consumed by
flyto-code `claude/module-editions-ui`:

- `code.modules.edition.*`: the one edition label a module carries after launch
  (Basic, Full, Trial · N days, Read-only until date, Not owned).
- `code.modules.purchase.*`: the separate "Purchase modules" page (phase notes,
  Basic vs Full columns, actions: Upgrade to Full, Buy from partner, Request a
  PoC, Request a higher limit, Return to Full).
- `code.modules.unit.*` (counted form, zh carries its measure word) and
  `code.modules.unitName.*` (standalone form) for the engine's limit units;
  `code.modules.limit.*` and `code.modules.usage.*` templates ("1 / 1 個根網域").
- `code.modules.reason.moduleLimitReached` / `moduleUpgradeRequired` for the two
  new engine reasons; `code.modules.gate.viewPlans`;
  `code.modules.request.paymentSoonNote`.
- `code.entitlement.*`: toasts for 402 `module_limit_reached`,
  `module_upgrade_required` and `basic_pinned`, and the "Upgrade" action label.
- `code.org.licences.col.edition` / `col.usage`.

Copy is domain-neutral (units name what the engine counts, nothing product- or
industry-specific). Older keys the UI no longer reads
(`code.projects.coverage.badge.includedTesting`, `...locksAtLaunch`,
`...cta.purchaseAtLaunch`, `code.modules.request.purchaseAtLaunchNote`) were left
in place so an older flyto-code pin keeps resolving; remove them after the
flyto-code change is merged and pinned.

## Review fixes (second commit)

- Toasts: `code.entitlement.basicLimitReached` / `moduleLimitReached` take one
  `{usage}` ("1 / 1 root domains") instead of bare `{limit}` / `{used}`;
  `basicPinned` drops the unexplained `({used})`.
- `code.modules.usage.unbounded` reads "3 root domains in use (no limit)" /
  "已使用 3 個根網域（不限）"; `code.modules.edition.locked` is "Not purchased" /
  "未購買" / "未购买"; `code.modules.purchase.unpinNoChange` reworded (the UI now
  offers Return to Full only when the engine says it would work).
- New: `code.modules.purchase.inUseProject`, `usageUnavailable`, `selected`;
  `code.modules.gate.viewPlansNewTab`; `code.projects.coverage.action.create`
  and `action.openPurchase` (accessible descriptions of what a tile does).
- One pronoun (您) across the module-commerce flow in zh-TW and zh-CN: every
  `code.modules.*`, `code.projects.coverage.*`, `code.entitlement.*` and
  `code.projects.wizard.*` string that used 你.
- `code.projects.wizard.enforcedNote` and `testingNote` are no longer read by
  flyto-code; they stay for older pins (same policy as the keys above).

## Verified

- `python3 scripts/build-dist.py` (dist regenerated and committed)
- `python3 scripts/validate.py --strict`: PASS, 0 errors
- `python3 -m unittest discover -s tests`: 82 tests OK
- `flyto-index verify . --strict`: no FAIL or WARN
- flyto-code's full vitest run against this dist (via the worktree symlink).

## Not verified

- Not pushed or merged. flyto-code CI pins flyto-i18n to a commit on i18n
  main, so after merging, bump that pin in every flyto-code workflow.
