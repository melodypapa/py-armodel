#!/usr/bin/env python3
"""
Migrate tests from test_armodel/models_v2 to test_armodel/v2/models.

This script moves the V2 test directory to align with the new V2 model structure.
"""

import os
import shutil
from pathlib import Path

def main():
    """Main migration function."""
    print("=" * 80)
    print("Migrating tests from test_armodel/models_v2 to test_armodel/v2/models")
    print("=" * 80)
    print()

    # Define paths
    project_root = Path(__file__).parent.parent
    old_dir = project_root / "tests" / "test_armodel" / "models_v2"
    new_dir = project_root / "tests" / "test_armodel" / "v2" / "models"

    print(f"[Step 1] Moving {old_dir} to {new_dir}...")

    # Check if old directory exists
    if not old_dir.exists():
        print(f"✓ Old directory does not exist: {old_dir}")
        print("Migration already completed or directory never existed.")
        return

    # Check if new directory already exists
    if new_dir.exists():
        print(f"✗ New directory already exists: {new_dir}")
        print("Please remove it first or check if migration was already done.")
        return

    # Create parent directory if needed
    new_dir.parent.mkdir(parents=True, exist_ok=True)

    # Move the directory
    try:
        shutil.move(str(old_dir), str(new_dir))
        print(f"✓ Successfully moved to {new_dir}")
    except Exception as e:
        print(f"✗ Error moving directory: {e}")
        return

    print()
    print("[Step 2] Verifying migration...")

    # Verify files were moved
    if new_dir.exists():
        files = list(new_dir.rglob("*.py"))
        print(f"✓ Found {len(files)} Python files in new location")
    else:
        print(f"✗ New directory not found: {new_dir}")
        return

    if not old_dir.exists():
        print(f"✓ Old directory removed: {old_dir}")
    else:
        print(f"⚠ Old directory still exists: {old_dir}")

    print()
    print("=" * 80)
    print("Migration completed successfully!")
    print("=" * 80)
    print()
    print("Next steps:")
    print("1. Review the changes in tests/test_armodel/v2/models")
    print("2. Run tests: pytest tests/test_armodel/v2/models/ -v")
    print("3. If tests pass, the migration is complete")
    print()

if __name__ == "__main__":
    main()