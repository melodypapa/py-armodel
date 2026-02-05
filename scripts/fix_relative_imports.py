#!/usr/bin/env python3
"""
Fix all relative imports in models_v2.

Converts:
  from .SiblingModule import ClassName
To:
  from armodel.v2.models.M2.AUTOSARTemplates.ParentModule.SiblingModule import ClassName
"""

import os
import re
from pathlib import Path


def convert_relative_to_absolute(file_path: Path, content: str) -> str:
    """Convert relative imports to absolute imports."""
    lines = content.split('\n')
    result = []

    # Calculate the module path from file path
    parts = file_path.parts
    models_v2_idx = parts.index('models_v2')

    # Build base module path
    if models_v2_idx >= 0:
        base_path = '.'.join(parts[:models_v2_idx + 1])
        parent_dir = file_path.parent

        for line in lines:
            # Match: from .SiblingModule import ...
            match = re.match(r'^from \.(\w+)\s+import\s+(.+)', line.strip())

            if match:
                sibling_module = match.group(1)
                import_clause = match.group(2)

                # Build absolute import path
                # Remove leading '.' and construct full path
                relative_path = str(parent_dir.relative_to(Path("src/armodel/models_v2")))
                module_path = f"armodel.models_v2.{relative_path.replace('/', '.')}.{sibling_module}"

                new_line = f"from {module_path} import ({import_clause}"
                result.append(new_line)
            else:
                result.append(line)
    else:
        result = lines

    return '\n'.join(result)


def fix_file(file_path: Path, dry_run: bool = False) -> bool:
    """Fix relative imports in a single file."""
    if not file_path.exists():
        return False

    with open(file_path, 'r') as f:
        content = f.read()

    # Check if file has relative imports
    if not re.search(r'^from \.\w', content, re.MULTILINE):
        return False

    # Convert relative to absolute
    new_content = convert_relative_to_absolute(file_path, content)

    if new_content != content and not dry_run:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"✅ Fixed {file_path}")
        return True
    elif new_content != content and dry_run:
        print(f"🔍 Would fix {file_path}")
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
        print("🚀 FIXING RELATIVE IMPORTS")

    print()

    fixed_count = 0
    for py_file in models_v2_dir.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue

        if fix_file(py_file, dry_run):
            fixed_count += 1

    print()
    print(f"{'🔍' if dry_run else '✅'} {'Would fix' if dry_run else 'Fixed'} {fixed_count} files")

    return 0


if __name__ == "__main__":
    exit(main())
