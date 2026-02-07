#!/usr/bin/env python3
"""
Script to remove _validate_abstract() method from V2 model classes.
"""

import os
import re
from pathlib import Path


def remove_validate_abstract_method(file_path: str) -> bool:
    """
    Remove _validate_abstract() method from a file.
    Returns True if successfully removed, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match _validate_abstract method
        # Matches the method definition with docstring and body
        pattern = r'\n    def _validate_abstract\(self\) -> None:\n        """[^"]*"""\n        pass\n?'

        # Replace with empty string
        new_content = re.sub(pattern, '', content)

        if new_content == content:
            return False  # No changes made

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    # Directory to scan
    directory = Path("src/armodel/v2/models/")

    if not directory.exists():
        print(f"Directory {directory} does not exist")
        return

    # Find all Python files
    py_files = list(directory.rglob("*.py"))

    print(f"Scanning {len(py_files)} Python files for _validate_abstract methods...")

    success_count = 0
    for py_file in py_files:
        if remove_validate_abstract_method(str(py_file)):
            success_count += 1
            print(f"✓ Removed _validate_abstract from {py_file.relative_to(directory)}")

    print(f"\nSummary:")
    print(f"Total files processed: {len(py_files)}")
    print(f"Successfully removed from: {success_count}")


if __name__ == "__main__":
    main()