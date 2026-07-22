#!/usr/bin/env python3
"""
build-dist.py - Build merged locale files for CDN distribution

Usage:
    python scripts/build-dist.py

This script:
1. Merges locale files by scope (cloud, landing, all)
2. Converts flat keys to nested format for vue-i18n compatibility
3. Outputs to dist/{scope}/{locale}.json for efficient CDN loading
4. Generates manifest.json with locale metadata

Directory structure:
- locales/cloud/{locale}/*.json   - Cloud UI translations
- locales/modules/{locale}/*.json - Core module translations
- locales/landing/{locale}/*.json - Landing page translations
- locales/shared/{locale}/*.json  - Shared/common translations

Scopes (output):
- dist/cloud/{locale}.json   - cloud + modules + shared (flyto-cloud)
- dist/landing/{locale}.json - landing + shared (flyto-landing-page)
- dist/app/{locale}.json     - shared(app) + cloud(template) + shared(common)
- dist/{locale}.json          - all translations (admin/full access)
"""

import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime  # noqa: F401  # kept for backward-compat callers

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from i18n_contract import LANGUAGE_META, PROJECT_DIRS, build_locale_meta  # noqa: E402

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
DIST_DIR = PROJECT_ROOT / 'dist'
REPOSITORY_MANIFEST = PROJECT_ROOT / 'manifest.json'

# Define scopes: which project directories to include, and optional file filters
# Each scope entry: list of (project_dir, file_filter_or_None, key_prefix_to_restore)
# key_prefix_to_restore: the original prefix added back to translation keys for backward compat
SCOPES = {
    # Shared UI used by the self-hosted Flyto2 Flow parent. Hosted-only
    # surfaces stay out of this scope; flyto-cloud layers those on top through
    # its own edition source while reusing the same base UI translations.
    'flow': [
        ('cloud', [
            'accessibility.json', 'actionLabel.json', 'aiAgent.json',
            'alerts.json', 'alt.json', 'aria.json', 'autoForm.json',
            'backoffType.json', 'batch.json', 'binary.json', 'bindings.json',
            'breakpoint.json', 'browser.json', 'categories.json',
            'checkpoint.json', 'checkpointTooltip.json', 'code.json',
            'colorPicker.json', 'common.json', 'completionEffect.json',
            'component.json', 'confirmDialog.json', 'container.json',
            'coreUpdate.json', 'createModal.json', 'credentials.json',
            'cronPreset.json', 'debug.json', 'debugTab.json', 'error.json',
            'errors.json', 'errorStrategy.json', 'errorWorkflow.json',
            'execution.json', 'executionHistory.json',
            'executionModal.json', 'expression.json', 'flow.json', 'footer.json',
            'form.json', 'gridLayout.json', 'http.json',
            'iconPicker.json', 'lineage.json', 'llmChain.json', 'message.json',
            'metrics.json', 'moduleCard.json', 'moduleLab.json',
            'modules.json', 'mcpStudio.json', 'myTemplates.json', 'node.json', 'nodeOutput.json',
            'notFound.json', 'observability.json', 'offline.json', 'outputs.json',
            'pluginStatus.json', 'pluginType.json',
            'portLabel.json', 'preview.json', 'recorder.json', 'replayMode.json',
            'scheduler.json', 'simpleToolView.json',
            'stateMachine.json', 'status.json', 'subflow.json', 'switchCase.json',
            'template.json', 'templateBuilder.json', 'templateCard.json',
            'templateCategory.json', 'templateFolders.json', 'templateForm.json',
            'templateToolbar.json', 'terminal.json', 'testStep.json', 'time.json',
            'traces.json', 'triggers.json', 'ui.json', 'validation.json',
            'valueSource.json', 'variables.json', 'variableSelector.json',
            'vectorStore.json', 'versionDiff.json', 'versions.json',
            'workflow.json', 'workflowCanvas.json', 'workflowNode.json',
        ], 'cloud'),
        ('modules', None, 'modules'),
        ('shared', None, 'common'),
    ],
    'cloud': [
        ('cloud', None, 'cloud'),
        ('modules', None, 'modules'),
        ('shared', None, 'common'),
    ],
    'landing': [
        ('landing', None, 'landing'),
        ('shared', None, 'common'),
    ],
    'app': [
        ('app', None, 'app'),
        ('cloud', ['template.json'], 'cloud.template'),
        ('shared', None, 'common'),
    ],
    'code': [
        ('code', None, 'code'),
        ('shared', None, 'common'),
    ],
    'console': [
        ('console', None, 'console'),
        ('shared', None, 'common'),
    ],
    'data': [
        ('data', None, 'data'),
        ('shared', None, 'common'),
    ],
    'engine': [
        ('engine', None, 'engine'),
        ('shared', None, 'common'),
    ],
}


def get_locales() -> list:
    """Discover available locales from the cloud project (primary)."""
    cloud_dir = LOCALES_DIR / 'cloud'
    if not cloud_dir.exists():
        return []
    return sorted([d.name for d in cloud_dir.iterdir() if d.is_dir()])


def flat_to_nested(flat_dict: dict) -> dict:
    """
    Convert flat keys to nested object for vue-i18n compatibility.

    Handles key conflicts (audit 2026-05-17):
    - SPECIFIC child wins the dict slot at "a.b" so vue-i18n / engine
      can drill into "a.b.c".
    - GENERIC parent value is preserved as "a.b._self" instead of
      being silently dropped. Without this preservation engine's
      TranslateError step-2 generic fallback never resolves and
      non-en locales fall through to raw English on any error whose
      slug doesn't match a specific key.
    - Engine's flatten() lifts "*._self" back to bare parent keys.
      vue-i18n consumers ignore the _self leaf (no path queries it).
    """
    result = {}

    # Sort keys by length descending - longer keys first
    # This ensures children are set before parents try to overwrite
    sorted_keys = sorted(flat_dict.keys(), key=len, reverse=True)

    for key in sorted_keys:
        value = flat_dict[key]

        # Strip "cloud." prefix for cloud keys
        normalized_key = key[6:] if key.startswith('cloud.') else key

        parts = normalized_key.split('.')
        current = result

        # Navigate/create path to parent
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]

        final_key = parts[-1]
        existing = current.get(final_key)
        if existing is None:
            current[final_key] = value
        elif isinstance(existing, dict):
            # Collision: generic string vs children dict. Park at
            # _self instead of dropping the generic.
            if '_self' not in existing:
                existing['_self'] = value

    return result


def collect_files(locale: str, project: str, file_filter: list = None) -> list:
    """Get translation files for a locale from a specific project directory.

    Args:
        locale: Locale code (e.g., 'en', 'zh-TW')
        project: Project directory name (e.g., 'cloud', 'modules')
        file_filter: Optional list of specific filenames to include
    """
    locale_dir = LOCALES_DIR / project / locale
    if not locale_dir.exists():
        return []

    files = []
    for json_file in sorted(locale_dir.glob('*.json')):
        if file_filter and json_file.name not in file_filter:
            continue
        files.append(json_file)
    return files


def load_translations(files: list, key_prefix: str) -> dict:
    """Load and merge translations from files, restoring the original key prefix.

    Files no longer have the prefix in their name (e.g., admin.json instead of cloud.admin.json),
    but the translation keys inside still use the full prefix (e.g., "cloud.admin.title").
    We just read the keys as-is from the translations dict.
    """
    merged = {}
    count = 0
    for json_file in files:
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
        if 'translations' in data:
            merged.update(data['translations'])
            count += 1
    return merged, count


def build_locale(locale: str, scope: str = None) -> dict:
    """Build merged translations for a locale.

    Args:
        locale: The locale code (e.g., 'en', 'zh-TW')
        scope: Optional scope name ('cloud', 'landing', 'app', or None for all)
    """
    flat_merged = {}
    files_count = 0

    if scope and scope in SCOPES:
        # Build from scope definition
        for project, file_filter, _prefix in SCOPES[scope]:
            files = collect_files(locale, project, file_filter)
            translations, count = load_translations(files, _prefix)
            flat_merged.update(translations)
            files_count += count
    else:
        # Build all: collect from every project directory
        for project in PROJECT_DIRS:
            files = collect_files(locale, project)
            translations, count = load_translations(files, project)
            flat_merged.update(translations)
            files_count += count

    if not flat_merged:
        return {}

    # Convert to nested format
    nested = flat_to_nested(flat_merged)

    # Get language metadata
    meta = LANGUAGE_META.get(locale, {'name': locale, 'native': locale, 'region': locale[:2].upper()})

    # Content-derived version (audit 2026-05-17): a wall-clock
    # datetime.now() makes every build "dirty" git even when the
    # translations didn't change — caused check-dist-fresh to alarm
    # forever once it started gating on push. Hash the flat content
    # so version only changes when translations actually change.
    payload = json.dumps(flat_merged, sort_keys=True, ensure_ascii=False).encode('utf-8')
    version = hashlib.sha256(payload).hexdigest()[:12]

    return {
        'locale': locale,
        'name': meta['name'],
        'native': meta['native'],
        'region': meta['region'],
        'version': version,
        'files_merged': files_count,
        'total_keys': len(flat_merged),
        'translations': nested
    }


def build_manifest(locales_data: dict, flat_counts: dict) -> dict:
    """Build manifest with locale metadata.

    `version` is derived from the SHA-256 of the per-locale versions
    so two builds with identical content produce identical manifests.
    `generated_at` intentionally omitted — including it would defeat
    the content-stability promise."""
    locale_versions = sorted(
        f"{loc}:{data.get('version', '')}" for loc, data in locales_data.items()
    )
    manifest_version = hashlib.sha256(
        ' '.join(locale_versions).encode('utf-8')
    ).hexdigest()[:12]
    manifest = {
        'version': manifest_version,
        'locales': {}
    }

    for locale, data in locales_data.items():
        total = data.get('total_keys', 0)
        translated = flat_counts.get(locale, 0)

        meta = LANGUAGE_META.get(locale, {'name': locale, 'native': locale, 'region': locale[:2].upper()})

        manifest['locales'][locale] = {
            'name': meta['name'],
            'native': meta['native'],
            'region': meta['region'],
            'total_keys': total,
            'translated_keys': translated,
            'completion': round(translated / total * 100, 1) if total > 0 else 0,
            'files_merged': data.get('files_merged', 0)
        }

    return manifest


def count_translated(locale: str, scope: str = None) -> int:
    """Count non-empty unique translations for a locale after merge semantics."""
    merged = {}

    if scope and scope in SCOPES:
        for project, file_filter, _prefix in SCOPES[scope]:
            for json_file in collect_files(locale, project, file_filter):
                with open(json_file, encoding='utf-8') as f:
                    data = json.load(f)
                if 'translations' in data:
                    merged.update(data['translations'])
    else:
        for project in PROJECT_DIRS:
            for json_file in collect_files(locale, project):
                with open(json_file, encoding='utf-8') as f:
                    data = json.load(f)
                if 'translations' in data:
                    merged.update(data['translations'])

    return sum(1 for value in merged.values() if value)


def sync_repository_manifest(distribution_manifest: dict, manifest_path: Path = REPOSITORY_MANIFEST) -> bool:
    """Synchronize root locale coverage from the aggregate distribution manifest."""
    repository_manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    changed = False
    for locale, info in distribution_manifest.get('locales', {}).items():
        locale_record = repository_manifest.get('locales', {}).get(locale)
        if locale_record is None:
            continue
        completion = info.get('completion', 0)
        if locale_record.get('coverage') != completion:
            locale_record['coverage'] = completion
            changed = True
    rendered = json.dumps(repository_manifest, indent=2, ensure_ascii=False) + '\n'
    if manifest_path.read_text(encoding='utf-8') != rendered:
        manifest_path.write_text(rendered, encoding='utf-8')
        changed = True
    return changed


def main():
    """Build all deterministic translation bundles and manifests."""
    print("Building dist/ for CDN distribution")
    print()

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # Get all locales
    locales = get_locales()

    # Build scoped files first
    for scope in SCOPES:
        scope_dir = DIST_DIR / scope
        scope_dir.mkdir(parents=True, exist_ok=True)
        print(f"[{scope}]")

        scope_locales_data = {}
        scope_flat_counts = {}

        for locale in locales:
            data = build_locale(locale, scope=scope)
            scope_locales_data[locale] = data
            scope_flat_counts[locale] = count_translated(locale, scope=scope)

            # Write merged file
            output_file = scope_dir / f"{locale}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

            print(f"  → dist/{scope}/{locale}.json ({data.get('total_keys', 0)} keys, {data.get('files_merged', 0)} files)")

        # Write scope manifest
        manifest = build_manifest(scope_locales_data, scope_flat_counts)
        manifest_file = scope_dir / 'manifest.json'
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"  → dist/{scope}/manifest.json")
        print()

    # Build full (all translations) for admin/full access
    print("[all]")
    all_locales_data = {}
    all_flat_counts = {}

    for locale in locales:
        data = build_locale(locale, scope=None)
        all_locales_data[locale] = data
        all_flat_counts[locale] = count_translated(locale, scope=None)

        # Write merged file
        output_file = DIST_DIR / f"{locale}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print(f"  → dist/{locale}.json ({data.get('total_keys', 0)} keys, {data.get('files_merged', 0)} files)")

    # Write root manifest
    manifest = build_manifest(all_locales_data, all_flat_counts)
    manifest_file = DIST_DIR / 'manifest.json'
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("  → dist/manifest.json")
    sync_repository_manifest(manifest)
    print("  → manifest.json coverage")
    locale_meta_file = DIST_DIR / 'locale-meta.json'
    with open(locale_meta_file, 'w', encoding='utf-8') as f:
        json.dump(build_locale_meta(locales), f, indent=2, ensure_ascii=False)
        f.write('\n')
    print("  → dist/locale-meta.json")
    print()
    print("=" * 50)
    print("Build complete!")
    print()

    # Show summary for each scope
    for scope in list(SCOPES.keys()) + ['all']:
        scope_dir = DIST_DIR / scope if scope != 'all' else DIST_DIR
        manifest_file = scope_dir / 'manifest.json'
        if manifest_file.exists():
            with open(manifest_file, encoding='utf-8') as f:
                manifest = json.load(f)
            print(f"[{scope}]")
            for locale, info in manifest['locales'].items():
                status = "OK" if info['completion'] == 100 else ".."
                print(f"  {status} {locale}: {info['completion']}% ({info['translated_keys']}/{info['total_keys']})")
            print()


if __name__ == '__main__':
    main()
