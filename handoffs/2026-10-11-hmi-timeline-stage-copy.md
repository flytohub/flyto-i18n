# Timeline words for a goal sent or a step decided on a resource's panel

Owner: claude
Branch: claude/hmi-timeline-stages (local worktree `.claude/worktrees/hmi-stages`, not pushed, not merged)
Date: 2026-10-11
Copy commit: `7bdc3be4e` on origin/main `8bb5a7c2d` (#209); rebased from `3d65506b6` (on `bf1d35c87`)
Companion: flyto-cloud `claude/hmi-cloud-closure` (local worktree
`flyto-cloud/.claude/worktrees/hmi-closure`), whose bundles are synced from this branch

## What changed

- `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`: two stage keys.

  | key | en | zh-TW | zh-CN |
  | --- | --- | --- | --- |
  | `spaces.timeline.stage.hmi_submission` | Goal sent from the resource's panel | 由資源面板送出目標 | 由资源面板发出目标 |
  | `spaces.timeline.stage.hmi_approval` | Step decided on the resource's panel | 在資源面板決定步驟 | 在资源面板决定步骤 |

  The other 13 locales carry none of the newer stage keys
  (`needs_operator`, `handing_over`, `task_reported`), and these follow that.
- `dist/` rebuilt with `scripts/build-dist.py` and `build-seo-manifest.py`.
- `CHANGELOG.md` entry.
- `tests/test_cloud_runtime_cumulative_keys.py`: the cumulative English count
  goes from 13,961 (#209) to 13,963.
- Rebase onto origin/main `8bb5a7c2d`: the conflicts were in the CHANGELOG
  (both entries kept), the key ledger (both comments kept, total 13,963) and
  `dist/` (rebuilt from source, not hand-merged).

## Why

flyto-cloud records `hmi_submission` and `hmi_approval` on a task's decision
timeline when a goal is sent, or a step is allowed or denied, from a
resource-scoped panel (HMI). With no copy the Mission Station printed the raw
ids, and Cloud's `test_timeline_vocabulary_copy.py` and `check-i18n.py`
check 5 fail. `hmi_approval` covers both allow and deny, hence "decided".

The rebase was needed because flyto-cloud main (#529) already ships a bundle
built after #209; syncing Cloud from the old base would have dropped
`spaces.receipt.erpAcknowledged`.

## Verified

At `7bdc3be4e`, in this worktree:

- `make verify` (`PYTHON` = the Cloud worktree's private `.venv-hmi`
  Python 3.12.13, ruff 0.15.15 from a scratch venv, as `requirements.txt`
  pins): exit 0. `ruff check` "All checks passed!"; reference "current
  (387 declarations)"; `validate.py --strict` "Total: 4915 files, 0 errors /
  Status: PASS"; pytest "134 passed, 3560 subtests passed"; build ran;
  the tree stayed clean.
- `flyto-index scan .` then `flyto-index verify --strict`: Status PASS,
  21 pass / 0 warn / 0 fail.
- flyto-cloud `scripts/check-i18n.py --i18n-path <this worktree>` on the
  Cloud branch: "All checks passed!".

## Not verified

- CI on GitHub: the branch is not pushed.
- The 13 locales without the two keys fall back to English, as the other new
  stage keys do.

## Follow-ups

- Merge this before flyto-cloud `claude/hmi-cloud-closure`: the Cloud PR's
  i18n Sync Check reads flyto-i18n main and flags the two stage keys until
  then.
