#!/usr/bin/env python3
"""
Generate mapping.json and class-package.json from package definition files.

This script:
1. Reads .classes.json, .enums.json, and .primitives.json from docs/requirements/packages/
2. Generates docs/requirements/mapping.json
3. Generates docs/requirements/class-package.json (with python_file paths)
4. Verifies output matches existing class-package.json (source of truth)

Based on:
- CODING_RULE_STYLE_00008: Python Package Structure
- CODING_RULE_STYLE_00009: Class Organization per AUTOSAR Mapping
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def package_to_dir_path(package_path: str) -> str:
    """
    Convert AUTOSAR package path to directory path.

    Example:
        M2::AUTOSARTemplates::BswModuleTemplate::BswOverview
        -> M2/AUTOSARTemplates/BswModuleTemplate/BswOverview
    """
    return package_path.replace("::", "/")


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
            if not item.startswith("__"):
                subdirs.append(item)

    return subdirs


def is_leaf_package(v2_base_path: str, package_path: str) -> bool:
    """
    Determine if a package is a leaf or non-leaf package.

    Based on CODING_RULE_STYLE_00008:
    - Leaf package: classes in .py file (no directory)
    - Non-leaf package: classes in __init__.py (directory exists)

    Args:
        v2_base_path: Base path to V2 models
        package_path: AUTOSAR package path

    Returns:
        True if leaf package, False if non-leaf
    """
    dir_path = os.path.join(v2_base_path, package_to_dir_path(package_path))

    # If directory exists, it's non-leaf (classes in __init__.py)
    # If no directory exists, it's leaf (classes in .py file)
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return False
    return True


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
        parts = dir_path.split("/")
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


def scan_package_files(
    packages_dir: Path,
) -> Tuple[List[Path], List[Path], List[Path]]:
    """Find all classes, enums, and primitives JSON files."""
    classes_files = sorted(packages_dir.glob("*.classes.json"))
    enums_files = sorted(packages_dir.glob("*.enums.json"))
    primitives_files = sorted(packages_dir.glob("*.primitives.json"))
    return classes_files, enums_files, primitives_files


def extract_types_from_classes(classes_file: Path) -> List[Dict]:
    """Extract type entries from a .classes.json file."""
    with open(classes_file, encoding="utf-8") as f:
        data = json.load(f)
    package_path = data["package"]
    return [
        {"name": cls["name"], "type": "Class", "package_path": package_path}
        for cls in data.get("classes", [])
    ]


def extract_types_from_enums(enums_file: Path) -> List[Dict]:
    """Extract type entries from a .enums.json file."""
    with open(enums_file, encoding="utf-8") as f:
        data = json.load(f)
    package_path = data["package"]
    return [
        {"name": enum["name"], "type": "Enumeration", "package_path": package_path}
        for enum in data.get("enumerations", [])
    ]


def extract_types_from_primitives(primitives_file: Path) -> List[Dict]:
    """Extract type entries from a .primitives.json file."""
    with open(primitives_file, encoding="utf-8") as f:
        data = json.load(f)
    package_path = data["package"]
    return [
        {"name": prim["name"], "type": "Primitive", "package_path": package_path}
        for prim in data.get("primitives", [])
    ]


def add_package_metadata(
    types: List[Dict], v2_base_path: str, existing_class_package: Optional[Dict]
) -> List[Dict]:
    """
    Add python_file and package_structure to types (class-package.json format).

    Always computes from V2 directory structure to ensure accuracy.
    """
    results = []
    for entry in types:
        package_path = entry["package_path"]

        # Compute leaf/non-leaf from directory structure
        is_leaf = is_leaf_package(v2_base_path, package_path)
        python_file_rel = generate_python_file_path(package_path, is_leaf)

        result = entry.copy()
        result["python_file"] = build_full_python_path(python_file_rel)
        result["package_structure"] = "leaf" if is_leaf else "non-leaf"

        results.append(result)
    return results


def load_existing_class_package(path: Path) -> Optional[Dict]:
    """Load existing class-package.json for verification."""
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compare_class_package(generated: Dict, existing: Dict) -> List[str]:
    """Compare generated vs existing, return list of differences."""
    differences = []

    gen_types = {t["name"]: t for t in generated.get("types", [])}
    exist_types = {t["name"]: t for t in existing.get("types", [])}

    gen_names = set(gen_types.keys())
    exist_names = set(exist_types.keys())

    # Check for new types (in generated but not in existing)
    new_types = gen_names - exist_names
    if new_types:
        for name in sorted(new_types):
            differences.append(f"NEW TYPE: {name}")

    # Check for removed types (in existing but not in generated)
    removed_types = exist_names - gen_names
    if removed_types:
        for name in sorted(removed_types):
            differences.append(f"REMOVED TYPE: {name}")

    # Check for changed types
    common_types = gen_names & exist_names
    for name in sorted(common_types):
        gen_type = gen_types[name]
        exist_type = exist_types[name]

        # Compare key fields
        for key in ["type", "package_path", "python_file", "package_structure"]:
            gen_val = gen_type.get(key)
            exist_val = exist_type.get(key)
            if gen_val != exist_val:
                differences.append(
                    f"CHANGED {name}.{key}: '{exist_val}' -> '{gen_val}'"
                )

    return differences


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    packages_dir = project_root / "docs" / "requirements" / "packages"
    mapping_path = project_root / "docs" / "requirements" / "mapping.json"
    class_package_path = project_root / "docs" / "requirements" / "class-package.json"
    v2_base_path = str(project_root / "src" / "armodel" / "v2" / "models")

    print("=" * 80)
    print("Generate mapping.json and class-package.json from package files")
    print("=" * 80)

    # Step 1: Scan and extract types
    print("\n[Step 1] Scanning package files...")
    classes_files, enums_files, primitives_files = scan_package_files(packages_dir)
    print(f"  Found {len(classes_files)} classes files")
    print(f"  Found {len(enums_files)} enums files")
    print(f"  Found {len(primitives_files)} primitives files")

    all_types = []
    class_count = 0
    enum_count = 0
    primitive_count = 0

    for cf in classes_files:
        types = extract_types_from_classes(cf)
        all_types.extend(types)
        class_count += len(types)

    for ef in enums_files:
        types = extract_types_from_enums(ef)
        all_types.extend(types)
        enum_count += len(types)

    for pf in primitives_files:
        types = extract_types_from_primitives(pf)
        all_types.extend(types)
        primitive_count += len(types)

    print(f"\n  Extracted types:")
    print(f"    - Classes: {class_count}")
    print(f"    - Enumerations: {enum_count}")
    print(f"    - Primitives: {primitive_count}")
    print(f"    - Total: {len(all_types)}")

    # Sort for consistent output
    all_types.sort(key=lambda x: (x["package_path"], x["name"]))

    # Step 2: Generate mapping.json
    print(f"\n[Step 2] Generating {mapping_path.name}...")
    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump({"types": all_types}, f, indent=2)
    print(f"  Written: {mapping_path}")

    # Step 3: Generate class-package.json (with metadata)
    # Load existing class-package.json first (for source of truth on leaf/non-leaf)
    existing_class_package = load_existing_class_package(class_package_path)

    print(f"\n[Step 3] Generating {class_package_path.name}...")
    class_package_types = add_package_metadata(
        all_types, v2_base_path, existing_class_package
    )

    # Count leaf vs non-leaf
    leaf_count = sum(1 for t in class_package_types if t["package_structure"] == "leaf")
    non_leaf_count = sum(
        1 for t in class_package_types if t["package_structure"] == "non-leaf"
    )
    print(f"  Package structure:")
    print(f"    - Leaf packages: {leaf_count}")
    print(f"    - Non-leaf packages: {non_leaf_count}")

    generated = {"types": class_package_types}

    # Step 4: Verify against existing class-package.json
    print(f"\n[Step 4] Verifying against existing {class_package_path.name}...")

    if existing_class_package is None:
        print("  No existing file found, skipping verification")
    else:
        differences = compare_class_package(generated, existing_class_package)

        if differences:
            print(f"\n  VERIFICATION RESULT: {len(differences)} differences found")
            for diff in differences[:30]:  # Show first 30
                print(f"    - {diff}")
            if len(differences) > 30:
                print(f"    ... and {len(differences) - 30} more differences")
        else:
            print("  VERIFICATION PASSED: Generated matches existing class-package.json")

    # Write new class-package.json
    with open(class_package_path, "w", encoding="utf-8") as f:
        json.dump(generated, f, indent=2)
    print(f"\n  Written: {class_package_path}")

    print("\n" + "=" * 80)
    print("Generation complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
