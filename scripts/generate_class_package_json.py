#!/usr/bin/env python3
"""
Generate class-package.json from mapping.json with python_file field.

This script reads mapping.json and generates class-package.json with additional fields:
- python_file: The Python file path where the class should be defined
- package_structure: "leaf" or "non-leaf" based on CODING_RULE_STYLE_00008

Based on:
- CODING_RULE_STYLE_00008: Python Package Structure
- CODING_RULE_STYLE_00009: Class Organization per AUTOSAR Mapping
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Set


def load_mapping(mapping_path: str) -> List[Dict]:
    """Load mapping.json file."""
    with open(mapping_path, 'r') as f:
        data = json.load(f)
    return data.get('types', [])


def package_to_dir_path(package_path: str) -> str:
    """
    Convert AUTOSAR package path to directory path.

    Example:
        M2::AUTOSARTemplates::BswModuleTemplate::BswOverview
        -> M2/AUTOSARTemplates/BswModuleTemplate/BswOverview
    """
    return package_path.replace('::', '/')


def get_package_subdirectories(v2_base_path: str, package_path: str) -> List[str]:
    """
    Get list of subdirectories for a given package.

    Args:
        v2_base_path: Base path to V2 models (src/armodel/v2/models/)
        package_path: AUTOSAR package path (e.g., M2::AUTOSARTemplates::...)

    Returns:
        List of subdirectory names
    """
    dir_path = os.path.join(v2_base_path, package_to_dir_path(package_path))

    if not os.path.exists(dir_path):
        return []

    if not os.path.isdir(dir_path):
        return []

    subdirs = []
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            # Skip __pycache__ and similar
            if not item.startswith('__'):
                subdirs.append(item)

    return subdirs


def is_leaf_package(v2_base_path: str, package_path: str) -> bool:
    """
    Determine if a package is a leaf or non-leaf package.

    Based on CODING_RULE_STYLE_00008:
    - Leaf package: no subdirectories, classes in .py file
    - Non-leaf package: has subdirectories, classes in __init__.py

    Args:
        v2_base_path: Base path to V2 models
        package_path: AUTOSAR package path

    Returns:
        True if leaf package, False if non-leaf
    """
    # Check if directory exists
    dir_path = os.path.join(v2_base_path, package_to_dir_path(package_path))

    if not os.path.exists(dir_path):
        # Directory doesn't exist yet, assume leaf package
        return True

    if not os.path.isdir(dir_path):
        # Not a directory (it's a file), so this must be a leaf package
        return True

    # Check for subdirectories (excluding __pycache__)
    subdirs = get_package_subdirectories(v2_base_path, package_path)
    return len(subdirs) == 0


def generate_python_file_path(package_path: str, is_leaf: bool) -> str:
    """
    Generate the Python file path for a given package.

    Based on CODING_RULE_STYLE_00008:
    - Leaf: PackageName.py
    - Non-leaf: __init__.py

    Args:
        package_path: AUTOSAR package path (e.g., M2::AUTOSARTemplates::...)
        is_leaf: Whether this is a leaf package

    Returns:
        Python file path relative to src/armodel/v2/models/
    """
    dir_path = package_to_dir_path(package_path)

    if is_leaf:
        # Leaf package: Use .py file with package name
        # Get the last component of the path
        parts = dir_path.split('/')
        package_name = parts[-1]
        return f"{dir_path}.py"
    else:
        # Non-leaf package: Use __init__.py
        return f"{dir_path}/__init__.py"


def build_full_python_path(python_file: str) -> str:
    """
    Build full path from project root.

    Args:
        python_file: Path relative to src/armodel/v2/models/

    Returns:
        Full path from project root
    """
    return f"src/armodel/v2/models/{python_file}"


def generate_class_package_json(
    mapping_path: str,
    output_path: str,
    v2_base_path: str = "src/armodel/v2/models/"
) -> None:
    """
    Generate class-package.json from mapping.json.

    Args:
        mapping_path: Path to mapping.json
        output_path: Path to write class-package.json
        v2_base_path: Base path to V2 models directory
    """
    print(f"Loading mapping from: {mapping_path}")
    types = load_mapping(mapping_path)

    print(f"Processing {len(types)} types...")

    results = []
    leaf_count = 0
    non_leaf_count = 0
    manually_maintained_count = 0

    # Packages that are manually maintained (contain base classes)
    manually_maintained_packages = {
        'M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes',
        'M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject',
        'M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable',
    }

    for type_entry in types:
        name = type_entry['name']
        type_type = type_entry['type']
        package_path = type_entry['package_path']

        # Check if this is a manually maintained package
        is_manually_maintained = package_path in manually_maintained_packages

        # Determine if this is a leaf or non-leaf package
        is_leaf = is_leaf_package(v2_base_path, package_path)
        package_structure = "leaf" if is_leaf else "non-leaf"

        # Generate python_file path
        python_file_rel = generate_python_file_path(package_path, is_leaf)
        python_file = build_full_python_path(python_file_rel)

        # Build result entry
        result_entry = {
            "name": name,
            "type": type_type,
            "package_path": package_path,
            "python_file": python_file,
            "package_structure": package_structure
        }

        # Mark manually maintained packages
        if is_manually_maintained:
            result_entry["manually_maintained"] = True
            manually_maintained_count += 1

        results.append(result_entry)

        if is_manually_maintained:
            pass  # Don't count manually maintained in leaf/non-leaf stats
        elif is_leaf:
            leaf_count += 1
        else:
            non_leaf_count += 1

    # Write output
    print(f"Writing output to: {output_path}")
    with open(output_path, 'w') as f:
        json.dump({"types": results}, f, indent=2)

    # Print summary
    print("\n=== Summary ===")
    print(f"Total types: {len(types)}")
    print(f"Leaf packages: {leaf_count}")
    print(f"Non-leaf packages: {non_leaf_count}")
    print(f"Manually maintained: {manually_maintained_count}")
    print(f"Output written to: {output_path}")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    mapping_path = project_root / "docs" / "requirements" / "mapping.json"
    output_path = project_root / "docs" / "requirements" / "class-package.json"
    v2_base_path = str(project_root / "src" / "armodel" / "v2" / "models")

    generate_class_package_json(
        str(mapping_path),
        str(output_path),
        v2_base_path
    )


if __name__ == "__main__":
    main()
