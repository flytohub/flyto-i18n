# flyto-i18n — latest-main lint/parity convergence (2026-10-10)

## Source of truth and safety

- Started from **latest remote `main` `56d580871`**, not the stale local `main` (`c481c5f6c`) or the older `fix/cloud-i18n-parity-20261010` branch (`fec64e41c`). The remote main had gained 16 commits past the local origin/main cache and already incorporated subsequent language work.
- Worked in an isolated checkout (`fix/i18n-main-lint-and-parity-20261010`). The original `/Users/chester/flytohub/flyto-i18n` working directory has 52 pre-existing uncommitted changes and must not be reset, rebased, cleaned, or overwritten.
- Remote branch cleanup is safe **only after** this exact verified commit is available on `origin/main`. Never force-push or delete `main`. If branch protection refuses a fast-forward, merge by reviewed PR first and defer cleanup until the merge is confirmed.

## Ruff closure

Ruff on latest remote main initially reported **221** findings (the older branch had a different 209/208-issue baseline). They were corrected in scripts, tests and executable modes, with **0 remaining findings** for `ruff check scripts tests translate_th.py`.

- Imported necessary future annotations to support the product's Python **3.9** runtime after safe typing modernization; verified imports/tests rather than assuming Python 3.10+.
- Made 32 shebang-bearing CLI scripts executable (EXE001), and added a narrowly scoped `.ruff.toml` exemption only for **N999** on historical hyphen-named script entrypoints. Renaming those scripts would break existing CLI and automation entrypoints.
- Replaced silent or blind exception handling in source catalog readers with targeted exceptions and diagnostics; retained one *documented intentional* external SDK batch-catch where recoverability needs it.
- Converted legacy list/type/import style to Ruff-compliant form. No global rule shutdown or broad test-exclusion was introduced.

## Official Cloud locale closure

- Current-main `dist/cloud/{en,zh-TW,zh-CN}.json` already matched the shipping Cloud approved runtime dictionary **except for exactly five missing keys per locale**. This was checked by comparing flattened key/value dictionaries; there were no mismatched existing values or extra runtime keys.
- Added in the existing single-owner source catalogs for all three locales: `templateBuilder.header.saved`, `.saving`, `.unsaved`, `userSettings.aiSourceOllama`, `userSettings.aiSourceOpenAICompatible`. Rebuilt committed `dist` and manifests.
- The final flattened dictionaries match current Cloud exactly: **en 12,997**, **zh-TW 12,976**, **zh-CN 12,976**, with **zero missing keys, zero extra keys and zero unequal values**. No historical robot/demo keys were reintroduced.
- Updated the cumulative source-key-count contract from **13,945 to 13,950** with a note explaining the additive five keys.
- The earlier `fec64e41c` feature branch is **superseded** by this rebased, tested outcome on the newer `main`; do not merge that old branch wholesale over the newer Cloud copy. It has additional old generated artifacts from an earlier source snapshot.

## Verifications before main push

```sh
ruff check scripts tests translate_th.py
npm run verify
python3 scripts/sync-from-cloud.py --check --cloud-path <current-flyto-cloud-worktree>
```

- **Ruff: 0 findings**.
- **npm run verify: passed**, including Python unit suite **131 passed / 1 skipped**, strict locale validation **4,915 files / 0 errors**, docs reference freshness, generated bundles and SEO manifest.
- Cloud key synchronization check: **PASS**, and independent en/zh-TW/zh-CN bundle equality check: **all equal**.
- These are source/distribution checks, **not** CDN, mobile screenshot, end-user locale or production deployment acceptance.

## Remote branch hygiene

The remote originally had exactly two heads: `main` and `fix/cloud-i18n-parity-20261010`. After the verified fast-forward, prune the obsolete remote feature head and reconfirm the remote head list. **Do not delete unrelated local branches/worktrees or tags.** If the remote cannot be safely reduced to `main`, leave the other branch and report the actual blocking condition rather than claiming success.
