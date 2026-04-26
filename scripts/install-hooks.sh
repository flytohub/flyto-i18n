#!/usr/bin/env bash
# Install the pre-commit hook that auto-rebuilds dist/ when locales/
# changed in the staged set. Run once after cloning the repo:
#
#   ./scripts/install-hooks.sh
#
# Idempotent — re-running just overwrites the hook with the latest
# logic.

set -euo pipefail

# Resolve the script's own location so this works regardless of the
# shell's CWD (and regardless of which repo's git config is active).
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
REPO_ROOT="$( cd -- "${SCRIPT_DIR}/.." &> /dev/null && pwd )"
HOOK_PATH="${REPO_ROOT}/.git/hooks/pre-commit"

cat > "${HOOK_PATH}" <<'HOOK'
#!/usr/bin/env bash
# Auto-rebuild dist/ when staged changes touch locales/ or the
# build-dist script itself. Without this, a developer can commit
# locale changes without the matching dist update — CDN then serves
# stale translations until the next CI Build Dist run kicks in.

set -euo pipefail

# Only rebuild when relevant paths are staged.
staged="$(git diff --cached --name-only)"
if ! grep -qE '^(locales/|scripts/build-dist\.py)' <<< "${staged}"; then
    exit 0
fi

echo "i18n: locales/ changed, rebuilding dist/…"
python3 scripts/build-dist.py > /dev/null

# Stage any dist/ changes the rebuild produced. If no diff, this
# is a no-op.
if ! git diff --quiet dist/; then
    git add dist/
    echo "i18n: dist/ regenerated and staged"
fi
HOOK

chmod +x "${HOOK_PATH}"
echo "Installed: ${HOOK_PATH}"
echo ""
echo "The hook will now auto-rebuild dist/ whenever you stage changes"
echo "under locales/ or scripts/build-dist.py."
