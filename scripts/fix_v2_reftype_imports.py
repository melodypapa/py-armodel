#!/usr/bin/env python3
"""
Script to fix missing RefType imports in V2 model files.

This script adds the missing import for RefType to all V2 model files
that use RefType but don't import it.
"""
import os
import re
from pathlib import Path

# Find all Python files in V2 models
v2_models_dir = Path("/Users/ray/Workspace/py-armodel/src/armodel/v2/models/M2")

# Import statement to add
REFTYPE_IMPORT = "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType"

# Pattern to match files that use RefType
reftype_usage_pattern = re.compile(r"\bRefType\b")

# Pattern to match existing RefType import
reftype_import_pattern = re.compile(r"from.*PrimitiveTypes.*import.*RefType")

# Pattern to match the first import block
first_import_pattern = re.compile(r"(from abc import ABC, abstractmethod\nfrom typing import List, Optional, Dict, Any\n)")

def fix_file(file_path):
    """Fix a single Python file by adding RefType import if needed."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has RefType import
    if reftype_import_pattern.search(content):
        return False

    # Skip if doesn't use RefType
    if not reftype_usage_pattern.search(content):
        return False

    # Check if it has the standard import block pattern
    match = first_import_pattern.search(content)
    if match:
        # Add RefType import after the typing import
        new_content = content.replace(
            match.group(1),
            match.group(1) + REFTYPE_IMPORT + "\n"
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {file_path}")
        return True
    else:
        print(f"Skipped (no standard import pattern): {file_path}")
        return False

def main():
    """Main function to process all V2 model files."""
    fixed_count = 0
    skipped_count = 0

    # Recursively find all Python files
    for py_file in v2_models_dir.rglob("*.py"):
        if fix_file(py_file):
            fixed_count += 1
        else:
            skipped_count += 1

    print(f"\nFixed {fixed_count} files, skipped {skipped_count} files")

if __name__ == "__main__":
    main()