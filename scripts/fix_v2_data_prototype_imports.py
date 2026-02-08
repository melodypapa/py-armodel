#!/usr/bin/env python3
"""Fix import paths in V2 Datatype modules.

This script fixes import paths that were incorrectly added by fix_v2_missing_imports.py.
The mapping.json pointed to DataPrototypes package for many classes that are actually
in the Datatype package, causing circular imports.
"""

import re
from pathlib import Path

# Map of incorrect import paths to correct ones
IMPORT_FIXES = {
    # DataPrototype should be imported from Datatype package
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import DataPrototype": (
        "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototype import (\n"
        "    DataPrototype,\n"
        "    )"
    ),

    # AutosarDataPrototype should be imported from Datatype package
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype": (
        "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.AutosarDataPrototype import (\n"
        "    AutosarDataPrototype,\n"
        "    )"
    ),

    # ApplicationCompositeElementDataPrototype should be imported from Datatype package
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationCompositeElementDataPrototype": (
        "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.ApplicationCompositeElementDataPrototype import (\n"
        "    ApplicationCompositeElementDataPrototype,\n"
        "    )"
    ),
}


def fix_imports_in_file(file_path: Path) -> bool:
    """Fix import paths in a single file.

    Args:
        file_path: Path to the file to fix

    Returns:
        True if file was modified, False otherwise
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        original_content = content

        for incorrect, correct in IMPORT_FIXES.items():
            if incorrect in content:
                content = content.replace(incorrect, correct)

        if content != original_content:
            file_path.write_text(content, encoding="utf-8")
            print(f"Fixed: {file_path}")
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to fix all import paths."""
    # Target directory
    datatype_dir = Path(
        "src/armodel/v2/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype"
    )

    if not datatype_dir.exists():
        print(f"Directory not found: {datatype_dir}")
        return

    # Process all Python files in Datatype directory
    py_files = list(datatype_dir.rglob("*.py"))

    fixed_count = 0
    for py_file in py_files:
        if fix_imports_in_file(py_file):
            fixed_count += 1

    print(f"\nFixed {fixed_count} files")


if __name__ == "__main__":
    main()
