#!/usr/bin/env python3
"""
Fix imports in models_v2 to use models_v2 instead of models.

This script replaces all imports from 'armodel.models' with 'armodel.models_v2'
in the models_v2 directory.
"""

import os
import re
from pathlib import Path


def fix_imports_in_file(file_path: Path, dry_run: bool = False) -> int:
    """Fix imports in a single file. Returns number of changes made."""
    with open(file_path, 'r') as f:
        content = f.read()

    original_content = content

    # Replace 'from armodel.models.M2' with 'from armodel.v2.models.M2'
    # But NOT if it's already 'from armodel.v2.models'
    pattern = r'from armodel\.models\.M2'
    replacement = 'from armodel.v2.models.M2'

    content = re.sub(pattern, replacement, content)

    changes = len(re.findall(pattern, original_content))

    if changes > 0 and not dry_run:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"✅ Fixed {file_path} ({changes} import(s))")
    elif changes > 0 and dry_run:
        print(f"🔍 Would fix {file_path} ({changes} import(s))")

    return changes


def main():
    """Main function."""
    models_v2_dir = Path("src/armodel/models_v2")

    if not models_v2_dir.exists():
        print(f"❌ Directory not found: {models_v2_dir}")
        return 1

    dry_run = True  # Start with dry run for safety
    if "--force" in os.sys.argv:
        dry_run = False
        print("🚀 Running in LIVE mode (changes will be applied)")
    else:
        print("👀 Running in DRY RUN mode (use --force to apply changes)")

    print()

    total_changes = 0
    files_changed = 0

    for py_file in models_v2_dir.rglob("*.py"):
        # Skip __pycache__ and similar
        if "__pycache__" in str(py_file):
            continue

        changes = fix_imports_in_file(py_file, dry_run=dry_run)
        if changes > 0:
            total_changes += changes
            files_changed += 1

    print()
    print("=" * 60)
    if dry_run:
        print(f"📊 DRY RUN RESULTS:")
        print(f"   Files to be changed: {files_changed}")
        print(f"   Total imports to fix: {total_changes}")
        print()
        print("Run with --force to apply these changes:")
        print(f"   python {__file__} --force")
    else:
        print(f"✅ COMPLETED:")
        print(f"   Files changed: {files_changed}")
        print(f"   Total imports fixed: {total_changes}")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
