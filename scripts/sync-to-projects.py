#!/usr/bin/env python3
"""
sync-to-projects.py - Sync dist/ to consuming projects' bundled i18n files

When keys are added or DELETED from flyto-i18n, this script pushes those
changes to each project's local bundled/copied i18n files.

Projects handled:
  - flyto-cloud:  src/ui/web/frontend/src/i18n/bundled/{locale}.json  (scope: cloud)
  - flyto-code:   public/i18n/{scope}/{locale}.json                   (all scopes)
  - flyto-app:    assets/i18n/{locale}.json                           (via build-app.py)

Usage:
    python scripts/sync-to-projects.py [--dry-run] [--project NAME]

Options:
    --dry-run       Show changes without writing files
    --project NAME  Only sync to a specific project (cloud, code, app)
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DIST_DIR = PROJECT_ROOT / 'dist'
PARENT_DIR = PROJECT_ROOT.parent

# Project sync configurations
# Each entry: (project_dir, target_subpath, scope, locales_filter)
# scope=None means copy all scopes; locales_filter=None means all locales
SYNC_TARGETS = {
    'cloud': {
        'repo': 'flyto-cloud',
        'targets': [
            {
                'scope': 'cloud',
                'dest': 'src/ui/web/frontend/src/i18n/bundled',
                'locales': ['en', 'zh-TW', 'zh-CN'],
                'mode': 'single-scope',  # copy dist/cloud/{locale}.json -> dest/{locale}.json
            },
        ],
    },
    'code': {
        'repo': 'flyto-code',
        'targets': [
            {
                'scope': scope,
                'dest': f'public/i18n/{scope}',
                'locales': None,  # all locales
                'mode': 'single-scope',
            }
            for scope in ['cloud', 'code', 'console', 'data', 'app', 'cortex']
        ] + [
            {
                'scope': scope,
                'dest': f'public/i18n/{scope}',
                'locales': None,
                'mode': 'single-scope-with-manifest',  # also copy manifest.json
            }
            for scope in []  # manifests are handled below
        ],
    },
    'app': {
        'repo': 'flyto-app',
        'targets': [
            {
                'scope': 'app',
                'dest': 'assets/i18n',
                'locales': ['en', 'zh-TW'],
                'mode': 'build-app',  # use build-app.py instead of direct copy
            },
        ],
    },
}


def get_dist_locales(scope: str) -> list:
    """Get available locales for a scope from dist/."""
    scope_dir = DIST_DIR / scope
    if not scope_dir.exists():
        return []
    return sorted([
        f.stem for f in scope_dir.glob('*.json')
        if f.stem != 'manifest'
    ])


def sync_single_scope(
    scope: str,
    dest_dir: Path,
    locales_filter: list = None,
    dry_run: bool = False,
    copy_manifest: bool = False,
) -> dict:
    """Sync a single scope's dist files to a destination directory.

    Returns stats: {added, updated, deleted, unchanged}
    """
    source_dir = DIST_DIR / scope
    stats = {'added': 0, 'updated': 0, 'deleted': 0, 'unchanged': 0}

    if not source_dir.exists():
        print(f"    Warning: dist/{scope}/ does not exist, skipping")
        return stats

    # Get source locales
    available_locales = get_dist_locales(scope)
    if locales_filter:
        target_locales = [l for l in locales_filter if l in available_locales]
    else:
        target_locales = available_locales

    # --- Sync locale files ---
    for locale in target_locales:
        src_file = source_dir / f'{locale}.json'
        dst_file = dest_dir / f'{locale}.json'

        if not src_file.exists():
            continue

        src_data = src_file.read_text(encoding='utf-8')

        if dst_file.exists():
            dst_data = dst_file.read_text(encoding='utf-8')
            if src_data == dst_data:
                stats['unchanged'] += 1
                continue
            else:
                action = 'update'
                stats['updated'] += 1
        else:
            action = 'add'
            stats['added'] += 1

        if dry_run:
            print(f"    Would {action}: {dst_file.name}")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            dst_file.write_text(src_data, encoding='utf-8')
            print(f"    {action.capitalize()}d: {dst_file.name}")

    # --- Delete locale files that no longer exist in dist ---
    if dest_dir.exists():
        existing_files = set(f.name for f in dest_dir.glob('*.json'))
        expected_files = set(f'{l}.json' for l in target_locales)

        if copy_manifest:
            expected_files.add('manifest.json')

        # Only delete locale json files (not manifest or other config)
        deletable = set()
        for f in existing_files:
            stem = f.replace('.json', '')
            # It's a locale file if it matches locale pattern (xx or xx-XX)
            if stem != 'manifest' and stem != 'landing' and len(stem) >= 2:
                if f not in expected_files:
                    deletable.add(f)

        for filename in sorted(deletable):
            filepath = dest_dir / filename
            stats['deleted'] += 1
            if dry_run:
                print(f"    Would delete: {filename} (removed from i18n source)")
            else:
                filepath.unlink()
                print(f"    Deleted: {filename} (removed from i18n source)")

    # --- Copy manifest if requested ---
    if copy_manifest:
        src_manifest = source_dir / 'manifest.json'
        dst_manifest = dest_dir / 'manifest.json'
        if src_manifest.exists():
            src_data = src_manifest.read_text(encoding='utf-8')
            needs_update = True
            if dst_manifest.exists():
                needs_update = dst_manifest.read_text(encoding='utf-8') != src_data
            if needs_update and not dry_run:
                dst_manifest.write_text(src_data, encoding='utf-8')

    return stats


def sync_project(name: str, config: dict, dry_run: bool = False):
    """Sync all targets for a project."""
    repo_path = PARENT_DIR / config['repo']

    if not repo_path.exists():
        print(f"  Skip: {config['repo']}/ not found")
        return

    print(f"\n[{config['repo']}]")

    total = {'added': 0, 'updated': 0, 'deleted': 0, 'unchanged': 0}

    for target in config['targets']:
        scope = target['scope']
        dest = repo_path / target['dest']
        locales = target.get('locales')
        mode = target.get('mode', 'single-scope')

        if mode == 'build-app':
            # For flyto-app, delegate to build-app.py
            print(f"  [{scope}] -> {target['dest']}/ (via build-app.py)")
            if not dry_run:
                import subprocess
                result = subprocess.run(
                    [sys.executable, str(PROJECT_ROOT / 'scripts' / 'build-app.py')],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    print(f"    build-app.py completed successfully")
                else:
                    print(f"    build-app.py failed: {result.stderr}")
            else:
                print(f"    Would run build-app.py")
            continue

        print(f"  [{scope}] -> {target['dest']}/")
        copy_manifest = mode == 'single-scope-with-manifest'
        stats = sync_single_scope(scope, dest, locales, dry_run, copy_manifest)

        for k in total:
            total[k] += stats[k]

    # --- Also sync manifests for flyto-code ---
    if name == 'code':
        for scope_dir in (DIST_DIR).iterdir():
            if scope_dir.is_dir():
                src_manifest = scope_dir / 'manifest.json'
                if src_manifest.exists():
                    dest_manifest = repo_path / 'public' / 'i18n' / scope_dir.name / 'manifest.json'
                    if dest_manifest.parent.exists():
                        src_data = src_manifest.read_text(encoding='utf-8')
                        needs_update = True
                        if dest_manifest.exists():
                            needs_update = dest_manifest.read_text(encoding='utf-8') != src_data
                        if needs_update:
                            if dry_run:
                                print(f"    Would update manifest: {scope_dir.name}/manifest.json")
                            else:
                                dest_manifest.write_text(src_data, encoding='utf-8')
                                print(f"    Updated manifest: {scope_dir.name}/manifest.json")

    # Summary
    changes = total['added'] + total['updated'] + total['deleted']
    if changes:
        parts = []
        if total['added']:
            parts.append(f"+{total['added']} added")
        if total['updated']:
            parts.append(f"~{total['updated']} updated")
        if total['deleted']:
            parts.append(f"-{total['deleted']} deleted")
        print(f"  Summary: {', '.join(parts)} ({total['unchanged']} unchanged)")
    else:
        print(f"  Already in sync ({total['unchanged']} files)")


def main():
    parser = argparse.ArgumentParser(
        description='Sync dist/ translations to consuming projects'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without writing files'
    )
    parser.add_argument(
        '--project',
        choices=['cloud', 'code', 'app'],
        help='Only sync a specific project'
    )

    args = parser.parse_args()

    print("Syncing flyto-i18n/dist/ -> consuming projects")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 60)

    if not DIST_DIR.exists():
        print("Error: dist/ not found. Run build-dist.py first.")
        sys.exit(1)

    targets = SYNC_TARGETS
    if args.project:
        targets = {args.project: SYNC_TARGETS[args.project]}

    for name, config in targets.items():
        sync_project(name, config, args.dry_run)

    print("\n" + "=" * 60)
    if args.dry_run:
        print("Run without --dry-run to apply changes")
    else:
        print("Sync complete!")
        print("\nNext steps:")
        print("  1. Review changes in each project")
        print("  2. Commit and push each project")
        print("  3. Run each project's check-i18n.py to verify")


if __name__ == '__main__':
    main()
