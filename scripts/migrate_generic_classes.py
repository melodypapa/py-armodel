#!/usr/bin/env python3
"""
Migration script for GenericStructure classes.
Merges single-class files into target files according to class-package.json.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
CLASS_PACKAGE_JSON = 'docs/requirements/class-package.json'
SOURCE_DIR = 'src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure'
TEMPLATE_NAME = 'GenericStructure'


def load_class_mapping() -> Dict[str, Dict]:
    """Load class-package.json mapping."""
    with open(CLASS_PACKAGE_JSON, 'r') as f:
        data = json.load(f)
    
    # Filter for GenericStructure classes only
    classes = [c for c in data['classes'] 
               if 'v2' in c['python_file'] and TEMPLATE_NAME in c['python_file']]
    
    # Group by target file
    mapping = {}
    for cls in classes:
        target = cls['python_file']
        if target not in mapping:
            mapping[target] = []
        mapping[target].append(cls['name'])
    
    return mapping


def get_class_definition_from_file(filepath: str, class_name: str) -> str:
    """
    Extract class definition from a source file.
    Returns the full class definition including all methods and properties.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find class definition
    class_start = -1
    for i, line in enumerate(lines):
        if f'class {class_name}(' in line:
            class_start = i
            break
    
    if class_start == -1:
        return ""
    
    # Extract the class (until next class or end of file)
    class_lines = []
    indent_level = len(lines[class_start]) - len(lines[class_start].lstrip())
    
    for i in range(class_start, len(lines)):
        line = lines[i]
        class_lines.append(line)
        
        # Check if we've reached the next class definition at same or lower indent
        if i > class_start and line.strip().startswith('class '):
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= indent_level:
                # This is a new class, remove it and stop
                class_lines.pop()
                break
    
    return ''.join(class_lines)


def find_source_file(class_name: str) -> Tuple[str, str]:
    """
    Find the source file for a class.
    Returns (filepath, class_content).
    """
    for py_file in Path(SOURCE_DIR).rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue
        
        # Check if file contains the class
        with open(py_file, 'r') as f:
            content = f.read()
            if f'class {class_name}(' in content:
                return (str(py_file), content)
    
    return (None, None)


def migrate_class(class_name: str, target_file: str) -> bool:
    """
    Migrate a single class to the target file.
    Returns True if successful, False otherwise.
    """
    # Find source file
    source_file, source_content = find_source_file(class_name)
    if not source_file:
        print(f"  ✗ {class_name} - file not found")
        return False
    
    # Extract class definition
    class_def = get_class_definition_from_file(source_file, class_name)
    if not class_def:
        print(f"  ✗ {class_name} - class definition not found")
        return False
    
    # Create target directory if needed
    target_path = Path(target_file)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Append to target file
    with open(target_file, 'a') as f:
        f.write('\n')
        f.write(class_def)
        f.write('\n')
    
    print(f"  ✓ {class_name} from {Path(source_file).name}")
    return True


def main():
    """Main migration function."""
    print(f"=== {TEMPLATE_NAME} Migration ===")
    
    # Load mapping
    mapping = load_class_mapping()
    
    total_classes = sum(len(classes) for classes in mapping.values())
    target_files = len(mapping)
    
    print(f"Total classes to migrate: {total_classes}")
    print(f"Target files: {target_files}")
    print()
    
    # Migrate each target file
    for target_file, class_names in sorted(mapping.items()):
        print(f"Migrating {len(class_names)} classes to {target_file}:")
        
        # Migrate each class
        migrated = []
        for class_name in class_names:
            if migrate_class(class_name, target_file):
                migrated.append(class_name)
        
        # Delete old source files
        for class_name in migrated:
            source_file, _ = find_source_file(class_name)
            if source_file and Path(source_file).exists():
                os.remove(source_file)
                print(f"  → Deleted {Path(source_file).name}")
        
        if migrated:
            print(f"  → Created {target_file}")
        print()
    
    print("=== Migration Complete ===")


if __name__ == '__main__':
    main()