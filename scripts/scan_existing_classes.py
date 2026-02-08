"""
Scan the codebase to discover all existing classes in AUTOSARTemplates.

This script walks through the source code and discovers all classes that are
actually implemented, so we can verify only those against mapping.json.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Set, Tuple

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import importlib


def get_all_py_files(base_path: Path) -> List[Path]:
    """Get all Python files (including __init__.py) under base_path."""
    py_files = []

    for py_file in base_path.rglob("*.py"):
        py_files.append(py_file)

    return py_files


def convert_file_to_module_path(py_file: Path, base_src: Path) -> str:
    """Convert a Python file path to a Python module path."""
    # Get relative path from src directory
    rel_path = py_file.relative_to(base_src)

    # Convert to module path (replace / with . and remove .py extension)
    module_path = str(rel_path.with_suffix("")).replace(os.sep, ".")

    return module_path


def get_classes_in_module(module_path: str) -> Tuple[Set[str], bool, str]:
    """
    Get all classes defined in a module.

    Returns:
        (set of class names, success flag, error message)
    """
    try:
        module = importlib.import_module(module_path)

        classes = set()
        for name in dir(module):
            if not name.startswith("_"):
                obj = getattr(module, name)

                # Check if it's a class (type)
                # Note: ABCMeta is a subclass of type, so isinstance works for ABCs too
                try:
                    if isinstance(obj, type):
                        # Filter out built-in types and imported types from other modules
                        # Check if the class was defined in this module
                        if hasattr(obj, "__module__"):
                            if obj.__module__ == module_path:
                                classes.add(name)
                        else:
                            # No __module__ attribute, add it anyway
                            classes.add(name)
                except Exception:
                    pass

        return classes, True, ""

    except Exception as e:
        return set(), False, f"{type(e).__name__}: {e}"


def main():
    """Main function to scan and save existing classes."""
    base_src = Path(__file__).parent.parent / "src"
    base_path = base_src / "armodel" / "models" / "M2" / "AUTOSARTemplates"

    print(f"Scanning directory: {base_path}")
    print("=" * 80)

    # Get all Python files
    py_files = get_all_py_files(base_path)
    print(f"Found {len(py_files)} Python files (including __init__.py)")

    # Scan each file and collect classes
    results = {}
    total_classes = 0
    successful_modules = 0
    failed_modules = 0

    for py_file in py_files:
        # Convert to module path
        module_path = convert_file_to_module_path(py_file, base_src)

        # Get classes in this module
        classes, success, error = get_classes_in_module(module_path)

        if success:
            if classes:
                results[module_path] = sorted(list(classes))
                total_classes += len(classes)
                successful_modules += 1
                print(f"[OK] {module_path}: {len(classes)} classes")
            else:
                # Track modules with no classes defined in them
                results[module_path] = []
                successful_modules += 1
        else:
            failed_modules += 1
            print(f"[FAIL] {module_path}: {error}")

    print("=" * 80)
    print("\nSummary:")
    print(f"  Total modules scanned: {len(py_files)}")
    print(f"  Successful imports: {successful_modules}")
    print(f"  Failed imports: {failed_modules}")
    print(f"  Total classes found: {total_classes}")

    # Save to JSON
    output_file = Path(__file__).parent.parent / "reports" / "existing_classes.json"

    # Prepare output data
    output_data = {
        "classes": results,
        "total_classes": total_classes,
        "total_modules": len(py_files),
        "successful_modules": successful_modules,
        "failed_modules": failed_modules,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")

    # Print some sample classes
    print("\n" + "=" * 80)
    print("Sample classes found:")
    count = 0
    for module_path, class_list in results.items():
        if class_list:
            for class_name in class_list[:3]:  # Show first 3 classes per module
                print(f"  {module_path}.{class_name}")
                count += 1
                if count >= 20:  # Show max 20 samples
                    break
        if count >= 20:
            break


if __name__ == "__main__":
    main()
