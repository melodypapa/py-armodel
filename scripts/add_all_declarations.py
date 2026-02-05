#!/usr/bin/env python3
"""
Add __all__ declarations to files missing them.
"""

import os
import re
from pathlib import Path
from typing import List, Set


def extract_classes_from_content(content: str) -> List[str]:
    """Extract class names from Python file content."""
    # Find all top-level class definitions
    classes = re.findall(r'^class\s+(\w+)\s*\(', content, re.MULTILINE)
    return classes


def add_all_to_file(file_path: Path, dry_run: bool = False) -> bool:
    """Add __all__ declaration to a Python file."""
    if not file_path.exists():
        return False

    with open(file_path, 'r') as f:
        content = f.read()

    # Skip if __all__ already exists
    if "__all__" in content:
        return False

    # Extract classes defined in this file
    classes = extract_classes_from_content(content)

    if not classes:
        # No classes found, add minimal __all__
        all_decl = '\n__all__ = []\n'
    else:
        # Create __all__ with class names
        class_list = ', '.join(f'"{c}"' for c in classes)
        all_decl = f'\n__all__ = [{class_list}]\n'

    # Find where to insert __all__ (after imports, before first class)
    lines = content.split('\n')

    # Find last import line
    last_import_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith('from ') or line.strip().startswith('import '):
            last_import_idx = i
        elif line.strip() and not line.strip().startswith('#') and last_import_idx >= 0:
            # Found first non-import, non-comment line after imports
            break

    if last_import_idx >= 0:
        # Insert __all__ after imports
        insert_idx = last_import_idx + 1

        # Skip blank lines after imports
        while insert_idx < len(lines) and not lines[insert_idx].strip():
            insert_idx += 1

        lines.insert(insert_idx, all_decl)

        new_content = '\n'.join(lines)

        if not dry_run:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print(f"✅ Added __all__ to {file_path} ({len(classes)} classes)")
            return True
        else:
            print(f"🔍 Would add __all__ to {file_path} ({len(classes)} classes)")
            return True

    return False


def main():
    """Main function."""
    models_v2_dir = Path("src/armodel/models_v2")

    if not models_v2_dir.exists():
        print(f"❌ Directory not found: {models_v2_dir}")
        return 1

    dry_run = "--dry-run" in os.sys.argv

    if dry_run:
        print("👀 DRY RUN MODE")
    else:
        print("🚀 ADDING __all__ DECLARATIONS")

    print()

    fixed_count = 0
    for py_file in models_v2_dir.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue

        if add_all_to_file(py_file, dry_run):
            fixed_count += 1

    print()
    print(f"{'🔍' if dry_run else '✅'} {'Would add' if dry_run else 'Added'} __all__ to {fixed_count} files")

    return 0


if __name__ == "__main__":
    exit(main())
