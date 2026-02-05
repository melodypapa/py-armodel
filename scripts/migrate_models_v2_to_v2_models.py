#!/usr/bin/env python3
"""
Migrate models_v2 to v2/models.

This script moves the models_v2 directory to v2/models and updates all imports.
"""

import os
import re
import shutil
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src" / "armodel"
MODELS_V2_DIR = SRC_DIR / "models_v2"
V2_MODELS_DIR = SRC_DIR / "v2" / "models"

def main():
    print("=" * 80)
    print("Migrating models_v2 to v2/models")
    print("=" * 80)

    # Check if models_v2 exists
    if not MODELS_V2_DIR.exists():
        print(f"ERROR: {MODELS_V2_DIR} does not exist")
        return 1

    # Check if v2 directory exists
    if not SRC_DIR.joinpath("v2").exists():
        print(f"Creating v2 directory...")
        SRC_DIR.joinpath("v2").mkdir(parents=True, exist_ok=True)

    # Check if v2/models already exists
    if V2_MODELS_DIR.exists():
        print(f"ERROR: {V2_MODELS_DIR} already exists")
        return 1

    # Step 1: Move models_v2 to v2/models
    print(f"\n[Step 1] Moving {MODELS_V2_DIR} to {V2_MODELS_DIR}...")
    try:
        shutil.move(str(MODELS_V2_DIR), str(V2_MODELS_DIR))
        print(f"✓ Successfully moved to {V2_MODELS_DIR}")
    except Exception as e:
        print(f"✗ ERROR: Failed to move directory: {e}")
        return 1

    # Step 2: Update imports in v2/models files
    print(f"\n[Step 2] Updating imports in v2/models files...")
    update_count = update_imports_in_directory(V2_MODELS_DIR)
    print(f"✓ Updated {update_count} files")

    # Step 3: Update test files
    print(f"\n[Step 3] Updating test files...")
    test_dir = PROJECT_ROOT / "tests" / "test_armodel" / "models_v2"
    if test_dir.exists():
        test_update_count = update_imports_in_directory(test_dir)
        print(f"✓ Updated {test_update_count} test files")
    else:
        print(f"⚠ Test directory not found: {test_dir}")

    # Step 4: Update documentation
    print(f"\n[Step 4] Updating documentation...")
    docs_files = [
        PROJECT_ROOT / "AGENTS.md",
        PROJECT_ROOT / "docs" / "development" / "coding_rules_v2.md",
    ]
    docs_update_count = 0
    for doc_file in docs_files:
        if doc_file.exists():
            count = update_imports_in_file(doc_file)
            if count > 0:
                docs_update_count += count
                print(f"✓ Updated {doc_file.relative_to(PROJECT_ROOT)}")
    print(f"✓ Updated {docs_update_count} documentation files")

    # Step 5: Update scripts
    print(f"\n[Step 5] Updating scripts...")
    scripts_dir = PROJECT_ROOT / "scripts"
    if scripts_dir.exists():
        scripts_update_count = update_imports_in_directory(scripts_dir)
        print(f"✓ Updated {scripts_update_count} script files")

    print("\n" + "=" * 80)
    print("Migration completed successfully!")
    print("=" * 80)
    print(f"\nNext steps:")
    print(f"1. Review the changes in {V2_MODELS_DIR}")
    print(f"2. Run tests: pytest tests/test_armodel/models_v2/ -v")
    print(f"3. If tests pass, remove the old models_v2 backup (if any)")
    print(f"4. Commit the changes")

    return 0

def update_imports_in_directory(directory: Path) -> int:
    """Update all imports in Python files in a directory."""
    count = 0
    for py_file in directory.rglob("*.py"):
        if update_imports_in_file(py_file):
            count += 1
    return count

def update_imports_in_file(file_path: Path) -> int:
    """Update imports in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace armodel.models_v2 with armodel.v2.models
        content = re.sub(
            r'from armodel\.models_v2\b',
            'from armodel.v2.models',
            content
        )

        # Replace armodel.v2.models.M2 with armodel.v2.models.M2
        content = re.sub(
            r'armodel\.models_v2\.M2',
            'armodel.v2.models.M2',
            content
        )

        # Replace armodel.v2.models.utils with armodel.v2.models.utils
        content = re.sub(
            r'armodel\.models_v2\.utils',
            'armodel.v2.models.utils',
            content
        )

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return 1

    except Exception as e:
        print(f"✗ ERROR processing {file_path}: {e}")

    return 0

if __name__ == "__main__":
    exit(main())