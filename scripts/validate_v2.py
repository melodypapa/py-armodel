"""Validate V2 structure and coding rules."""

import sys
from pathlib import Path


def validate_v2():
    """Validate V2 structure."""
    models_v2 = Path("src/armodel/models_v2")

    if not models_v2.exists():
        print("✗ models_v2 does not exist")
        return 1

    # Check for TYPE_CHECKING in import statements (not in comments/docstrings)
    type_checking_files = []
    for py_file in models_v2.rglob("*.py"):
        content = py_file.read_text()
        # Check if TYPE_CHECKING is imported (not just mentioned in comments)
        if "from typing import" in content and "TYPE_CHECKING" in content:
            # Additional check: make sure it's an actual import, not in a comment
            for line in content.split('\n'):
                if 'from typing import' in line and 'TYPE_CHECKING' in line:
                    # Ignore if the line starts with # (comment)
                    stripped = line.strip()
                    if not stripped.startswith('#'):
                        type_checking_files.append(py_file)
                        break

    if type_checking_files:
        print(f"✗ Found TYPE_CHECKING imports in {len(type_checking_files)} files:")
        for f in type_checking_files:
            print(f"  - {f}")
        return 1

    # Check for relative imports (but allow them in __init__.py files for package initialization)
    relative_import_files = []
    for py_file in models_v2.rglob("*.py"):
        # Skip __init__.py files - relative imports are acceptable there for package initialization
        if py_file.name == "__init__.py":
            continue

        content = py_file.read_text()
        if "from ." in content:
            relative_import_files.append(py_file)

    if relative_import_files:
        print(f"✗ Found relative imports in {len(relative_import_files)} files:")
        for f in relative_import_files:
            print(f"  - {f}")
        return 1

    print("✓ V2 validation passed!")
    return 0


if __name__ == "__main__":
    sys.exit(validate_v2())
