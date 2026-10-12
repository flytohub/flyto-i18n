# Space statistics words for flyto-cloud

Owner: claude
Branch: claude/stats-copy
Date: 2026-10-12

## What changed

Sixty-nine new keys in `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`,
values copied verbatim from flyto-cloud's bundled catalogs on its statistics
branch (which carried them first):

- UI: `spaces.stats.{title,back,group,allGoals,retry,loading,outcomes,rate,rateTitle,durationTitle,streaks,noStreaks,shortest,median,longest,seconds,minutesSeconds,unreadable,capped,window,windowCapped,loadingTasks,noTasks,openDecisions,openInStation,more,listCount}`,
  `spaces.stats.range.{label,all,month,week,day}`, `spaces.stats.message.{runs,empty}`
- Refusal rules: `spaces.stats.rule.{plan_contract,planner_unavailable,unknown_command}`
- Metrics: `spaces.stats.metric.<id>.{label,definition}` for tasks, verified,
  not_proven, failed, blocked, cancelled, refused, open, runs_settled,
  false_success, duration, approvals, steps_executed, steps_with_result,
  streak_current, streak_longest.

`dist/` rebuilt; the cumulative Cloud key ledger moves to 14,226.

## Verified

- `make verify` (lint, docs-check, validate.py --strict, coverage.py, pytest,
  build-dist, build-seo-manifest) passed on this branch.

## Not verified

- Other locales fall back to English for these keys.
- No native-speaker review of the zh-CN wording.

## Follow-ups

- flyto-cloud: run `scripts/check-i18n.py --fix` against this commit.
