"""Validate V2 structure and coding rules."""

import sys
from pathlib import Path


def validate_v2():
    """Validate V2 structure."""
    models_v2 = Path("src/armodel/models_v2")

    if not models_v2.exists():
        print("✗ models_v2 does not exist")
        return 1

    # Check for TYPE_CHECKING
    type_checking_files = []
    for py_file in models_v2.rglob("*.py"):
        if "TYPE_CHECKING" in py_file.read_text():
            type_checking_files.append(py_file)

    if type_checking_files:
        print(f"✗ Found TYPE_CHECKING in {len(type_checking_files)} files:")
        for f in type_checking_files:
            print(f"  - {f}")
        return 1

    # Check for relative imports
    relative_import_files = []
    for py_file in models_v2.rglob("*.py"):
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
