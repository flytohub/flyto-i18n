# Historical One-Off Migrations

These scripts preserve previously reviewed bulk translation migrations. They
are not supported public APIs and are excluded from normal build execution.

Inspect constants, target paths, dependencies, overwrite behavior, and diff
size before running one. Use a disposable branch, prefer dry-run where
available, then run `npm run verify` and review source plus generated output.

The root `translate_th.py` is another reviewed historical batch. It is retained
at its compatibility path but now requires explicit CLI execution and supports
`--dry-run`; importing it does not write files.
