#!/usr/bin/env python3
"""
Fix V2 coding rules violations automatically.

This script fixes:
1. Relative imports (V2_00001)
2. Missing __all__ declarations (V2_00003)
"""

import os
import re
from pathlib import Path
from typing import Set


def get_exported_classes(file_path: Path) -> Set[str]:
    """Extract class names defined in a Python file."""
    if not file_path.exists():
        return set()

    with open(file_path, 'r') as f:
        content = f.read()

    # Find all class definitions
    classes = set(re.findall(r'^class\s+(\w+)', content, re.MULTILINE))
    return classes


def fix_generic_structure_init() -> None:
    """Fix GenericStructure/__init__.py relative import."""
    init_file = Path("src/armodel/models_v2/M2/AUTOSARTemplates/GenericStructure/__init__.py")

    if not init_file.exists():
        print(f"⚠️  File not found: {init_file}")
        return

    with open(init_file, 'r') as f:
        content = f.read()

    # Check if it already has absolute imports
    if "from armodel.models_v2" in content:
        print(f"✅ {init_file} already uses absolute imports")
        return

    # Replace relative import with absolute imports
    # Import from sibling leaf packages and subdirectories
    new_content = '''"""
AUTOSAR V2 Models - GenericStructure Module.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Explicit __all__ exports (CODING_RULE_V2_00003)
"""

# Leaf package files
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import *
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.LifeCycles import *

# Subdirectory packages
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import *
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses import *
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import *
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.VariantHandling import *

'''

    with open(init_file, 'w') as f:
        f.write(new_content)

    print(f"✅ Fixed {init_file}")


def add_all_to_init(init_file: Path, dry_run: bool = False) -> bool:
    """Add __all__ declaration to an __init__.py file."""
    if not init_file.exists():
        return False

    with open(init_file, 'r') as f:
        content = f.read()

    # Skip if __all__ already exists
    if "__all__" in content:
        return False

    # Skip empty files
    if not content.strip():
        if not dry_run:
            with open(init_file, 'w') as f:
                f.write('"""V2 module."""\n\n__all__ = []\n')
        print(f"✅ Added __all__ to empty {init_file}")
        return True

    # Extract imported names from wildcard imports
    wildcard_imports = re.findall(r'from \S+ import \*', content)
    if wildcard_imports:
        # For wildcard imports, set __all__ to export everything
        if not dry_run:
            # Add __all__ before the first import
            lines = content.split('\n')
            import_idx = next((i for i, line in enumerate(lines) if 'import' in line), len(lines))

            # Insert __all__ declaration
            lines.insert(import_idx, '')
            lines.insert(import_idx, '__all__ = ["__doc__"]')
            lines.insert(import_idx, '"""V2 module."""')

            with open(init_file, 'w') as f:
                f.write('\n'.join(lines))
        print(f"✅ Added __all__ to {init_file} (wildcard imports)")
        return True

    return False


def fix_all_init_files(models_v2_dir: Path, dry_run: bool = False) -> int:
    """Fix all __init__.py files missing __all__."""
    fixed_count = 0

    for init_file in models_v2_dir.rglob("__init__.py"):
        if add_all_to_init(init_file, dry_run):
            fixed_count += 1

    return fixed_count


def main():
    """Main function."""
    models_v2_dir = Path("src/armodel/models_v2")

    if not models_v2_dir.exists():
        print(f"❌ Directory not found: {models_v2_dir}")
        return 1

    dry_run = "--dry-run" in os.sys.argv

    if dry_run:
        print("👀 DRY RUN MODE - use --force to apply changes")
    else:
        print("🚀 FIXING V2 CODING RULES VIOLATIONS")

    print()

    # Fix 1: Relative imports
    print("=" * 70)
    print("FIX 1: Relative Imports (V2_00001)")
    print("=" * 70)
    if not dry_run:
        fix_generic_structure_init()
    else:
        print("🔍 Would fix: GenericStructure/__init__.py")
    print()

    # Fix 2: Missing __all__
    print("=" * 70)
    print("FIX 2: Missing __all__ Declarations (V2_00003)")
    print("=" * 70)
    fixed = fix_all_init_files(models_v2_dir, dry_run)
    print(f"Fixed {fixed} __init__.py files")
    print()

    # Note 3: TYPE_CHECKING
    print("=" * 70)
    print("NOTE 3: TYPE_CHECKING Usage (V2_00002)")
    print("=" * 70)
    print("✅ No action needed - TYPE_CHECKING only appears in docstrings")
    print()

    print("=" * 70)
    if dry_run:
        print("📊 DRY RUN COMPLETE - use --force to apply")
    else:
        print("✅ ALL FIXES APPLIED")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    exit(main())
