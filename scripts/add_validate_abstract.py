#!/usr/bin/env python3
"""
Script to add _validate_abstract() method to concrete classes in V2 models.
This fixes mypy "Cannot instantiate abstract class" errors.
"""

import os
import re
from pathlib import Path
from typing import List, Set


def find_concrete_classes_needing_validation(directory: Path) -> Set[str]:
    """
    Find concrete classes that need _validate_abstract() method.
    Returns a set of (file_path, class_name) tuples.
    """
    needed_fixes = set()

    # Find all Python files in the directory
    py_files = list(directory.rglob("*.py"))

    for py_file in py_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find all class definitions
            class_pattern = r'^class\s+(\w+)'
            classes = re.findall(class_pattern, content, re.MULTILINE)

            for class_name in classes:
                # Skip if class already has _validate_abstract method
                if '_validate_abstract' in content:
                    continue

                # Skip if it's an abstract class (contains ABC or @abstractmethod)
                if 'ABC' in content or '@abstractmethod' in content:
                    continue

                # Add to fixes needed
                needed_fixes.add((str(py_file), class_name))

        except Exception as e:
            print(f"Error processing {py_file}: {e}")

    return needed_fixes


def add_validate_abstract_method(file_path: str, class_name: str) -> bool:
    """
    Add _validate_abstract() method to a concrete class.
    Returns True if successfully added, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the class definition
        class_pattern = rf'^class\s+{class_name}\([^)]*\):'
        match = re.search(class_pattern, content, re.MULTILINE)

        if not match:
            print(f"Could not find class definition for {class_name} in {file_path}")
            return False

        # Find the __init__ method within this class
        class_start = match.end()
        # Find the next class or end of file
        next_class = re.search(r'^class\s+\w+', content[class_start:], re.MULTILINE)
        if next_class:
            class_end = class_start + next_class.start()
        else:
            class_end = len(content)

        class_content = content[class_start:class_end]

        # Find __init__ method
        init_pattern = r'def __init__\(self[^)]*\):'
        init_match = re.search(init_pattern, class_content)

        if init_match:
            # Insert _validate_abstract after __init__
            insert_pos = class_start + init_match.end()
            method_to_add = "\n\n    def _validate_abstract(self) -> None:\n        \"\"\"Validate this is a concrete class.\"\"\"\n        pass"

            # Check if we need to add blank lines
            # Look for next method or end of class
            remaining_content = content[insert_pos:class_end]
            next_method = re.search(r'^\s*def \w+|^class ', remaining_content, re.MULTILINE)
            if next_method:
                next_method_pos = insert_pos + next_method.start()
                # Insert before next method
                new_content = (content[:insert_pos] +
                             method_to_add +
                             "\n" +
                             content[insert_pos:next_method_pos] +
                             content[next_method_pos:])
            else:
                # Insert at end of class
                new_content = content[:insert_pos] + method_to_add + content[insert_pos:]

            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True
        else:
            # No __init__ method found, add at class level
            insert_pos = class_start + len(class_content.split('\n')[0]) + 1
            method_to_add = "\n    def _validate_abstract(self) -> None:\n        \"\"\"Validate this is a concrete class.\"\"\"\n        pass"

            new_content = content[:insert_pos] + method_to_add + content[insert_pos:]

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True

    except Exception as e:
        print(f"Error processing {file_path} for class {class_name}: {e}")
        return False


def main():
    # Directory to scan
    directory = Path("src/armodel/v2/models/")

    if not directory.exists():
        print(f"Directory {directory} does not exist")
        return

    print("Scanning for concrete classes needing _validate_abstract() method...")
    needed_fixes = find_concrete_classes_needing_validation(directory)

    print(f"Found {len(needed_fixes)} classes needing fixes")

    # Process each fix
    success_count = 0
    for file_path, class_name in needed_fixes:
        if add_validate_abstract_method(file_path, class_name):
            success_count += 1
            print(f"✓ Added _validate_abstract to {class_name} in {file_path}")

    print(f"\nSummary:")
    print(f"Total fixes needed: {len(needed_fixes)}")
    print(f"Successfully applied: {success_count}")
    print(f"Failed: {len(needed_fixes) - success_count}")


if __name__ == "__main__":
    main()