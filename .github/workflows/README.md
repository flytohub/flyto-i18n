# Workflow Contracts

Every workflow must use least-privilege permissions, keep generated writes
separate from validation, and expose failure through a non-zero exit status.

`validate.yml` owns the complete test/build gate. `check-dist-fresh.yml` owns
source-to-distribution drift. `build-dist.yml` updates tracked generated
artifacts on main. Other workflows own cache purge, reviewed sync, downstream
notification, security, or release packaging as listed in the root README.
