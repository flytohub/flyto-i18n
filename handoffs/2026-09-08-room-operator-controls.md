# Room operator reply and attachment controls

## Scope

Own nineteen additive `spaces.schedule`, `spaces.hud`, `spaces.narrative`, and
`spaces.voice` keys in each Cloud `spaceOperations.json` catalog. English and
both Chinese variants have reviewed text; other locales retain explicit English
fallback. The copy describes replying and continuing, paused timing, upload
limits, upload progress, rejection, retry, and removal. It does not claim that
files uploaded successfully have already been processed by an AI.

## Integration

Build `dist/cloud` and aggregate distributions with `scripts/build-dist.py`, then
synchronize only Cloud with `scripts/sync-to-projects.py --project cloud`.
Cloud's temporary overrides return to the existing empty-object contract.
The complete English Cloud inventory is now 12,469 keys; its pinned test rises
by exactly the nineteen newly owned keys. No runtime authorization or execution
behavior belongs to this catalog change.

## Verification

`npm run verify` passed using the repository virtual environment: lint,
generated documentation, distribution build, strict source validation of 4,816
files, and 120 tests. Final indexer task validation passed Ruff and all 120 tests. Its host-supplied
changed-path inventory includes all 55 actual Git changes and retained file
hashes; this avoids the diff collector's 4 MiB limit on generated single-line
JSON without omitting generated distributions. Strict workspace verification
passed 21 checks for each of Cloud and i18n, with no project warnings or failures.
The dependency-drift check also passed. Two workspace-level findings remain:
contract endpoints were not extractable, and some Cloud product surfaces lack
UI test signals. The workspace command exited zero; these findings are not
proof of complete Cloud product acceptance.
The original local verification did not publish or deploy.

## Subsequent main integration

The user authorized updating local and remote main. Verified local changes were
first checkpointed in `96da041eb`, then merged with upstream `fe432b4f2`. Thirteen
canonical catalogs had adjacent-addition text conflicts but no conflicting
translation values. A three-way key merge retained both branches' changed
values across all affected canonical files. Generated bundle and manifest
conflicts were rebuilt from that combined source, not selected from one side.
The repository verification suite again passed all 120 tests and validated
4,816 catalog files. An ordinary Git push is authorized; CDN publication and
consumer deployment are separate outcomes and are not claimed here.
