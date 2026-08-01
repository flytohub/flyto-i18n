# Workflow Contracts

Every workflow must use least-privilege permissions, keep generated writes
separate from validation, and expose failure through a non-zero exit status.

`validate.yml` owns the complete test/build gate. `check-dist-fresh.yml` owns
source-to-distribution drift. `build-dist.yml` updates tracked generated
artifacts on main. `sync-cloud.yml` owns the hourly and manually dispatchable
pull from private Flyto2 Cloud source, validates the complete repository, and
opens a review-required pull request without copying Cloud source. Other
workflows own cache purge, Core sync, downstream notification, security, or
release packaging as listed in the root README.
