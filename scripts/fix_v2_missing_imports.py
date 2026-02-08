#!/usr/bin/env python3
"""
Fix missing parent class imports in V2 model files.

This script scans all V2 model .py files, identifies missing parent class imports,
and adds them based on the authoritative mapping.json file.

Usage:
    python scripts/fix_v2_missing_imports.py
"""

import ast
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple


def load_mapping(mapping_path: Path) -> Dict[str, str]:
    """Load class-to-package mapping from mapping.json."""
    with open(mapping_path, 'r') as f:
        data = json.load(f)
    
    # Create a dictionary: class_name -> package_path
    mapping = {}
    for item in data.get('types', []):
        if item.get('type') == 'Class':
            mapping[item['name']] = item['package_path']
    
    return mapping


def convert_package_to_import(package_path: str) -> str:
    """Convert AUTOSAR package path to Python import path.
    
    Example:
        M2::AUTOSARTemplates::CommonStructure::Implementation
        -> armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation
    """
    # Replace :: with . and prefix with armodel.v2.models
    parts = package_path.split('::')
    if parts[0] == 'M2':
        return 'armodel.v2.models.' + '.'.join(parts)
    return 'armodel.v2.models.' + '.'.join(parts)


def extract_parent_classes(file_path: Path) -> Set[str]:
    """Extract parent class names from a Python file using AST."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        parent_classes = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Extract parent class names from class definition
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        parent_classes.add(base.id)
                    elif isinstance(base, ast.Attribute):
                        # Handle attributes like module.ClassName
                        if isinstance(base.value, ast.Name):
                            parent_classes.add(base.attr)
        
        return parent_classes
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return set()


def get_existing_imports(file_path: Path) -> Set[str]:
    """Extract imported class names from a Python file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        imported_classes = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                # Get module path and imported names
                for alias in node.names:
                    imported_classes.add(alias.name)
        
        return imported_classes
    except Exception as e:
        print(f"Error parsing imports in {file_path}: {e}")
        return set()


def find_insert_position(content: str) -> int:
    """Find the position to insert new import statements."""
    lines = content.split('\n')
    
    # Find the last import line
    last_import_line = -1
    in_docstring = False
    docstring_end_line = -1
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track docstrings
        if i == 0 and stripped.startswith('"""'):
            in_docstring = True
        elif in_docstring and '"""' in stripped:
            in_docstring = False
            docstring_end_line = i
            continue
        
        # Skip lines before docstring ends
        if in_docstring:
            continue
        
        # Skip docstring continuation
        if docstring_end_line != -1 and i <= docstring_end_line:
            continue
        
        # Track import statements
        if stripped.startswith('from ') or stripped.startswith('import '):
            last_import_line = i
        elif last_import_line != -1 and not stripped.startswith('#') and stripped:
            # End of import block
            break
    
    # If no imports found, insert after docstring
    if last_import_line == -1:
        if docstring_end_line != -1:
            return docstring_end_line + 1
        return 0
    
    return last_import_line + 1


def add_missing_imports(file_path: Path, mapping: Dict[str, str]) -> int:
    """Add missing parent class imports to a file. Returns number of imports added."""
    parent_classes = extract_parent_classes(file_path)
    existing_imports = get_existing_imports(file_path)
    
    # Filter out built-in types and types that don't need imports
    skip_types = {'ABC', 'str', 'int', 'float', 'bool', 'list', 'dict', 'set', 'tuple', 'Optional'}
    missing_imports = []
    
    for parent_class in parent_classes:
        if parent_class in skip_types:
            continue
        if parent_class in existing_imports:
            continue
        if parent_class not in mapping:
            continue
        
        package_path = mapping[parent_class]
        import_path = convert_package_to_import(package_path)
        missing_imports.append((parent_class, import_path))
    
    if not missing_imports:
        return 0
    
    # Read file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find insert position
    insert_line = find_insert_position(content)
    lines = content.split('\n')
    
    # Insert new imports
    for parent_class, import_path in sorted(missing_imports, key=lambda x: x[1]):
        import_statement = f"from {import_path} import {parent_class}"
        lines.insert(insert_line, import_statement)
        insert_line += 1
    
    # Add blank line after imports if not present
    if insert_line < len(lines) and lines[insert_line].strip():
        lines.insert(insert_line, '')
    
    # Write back to file
    with open(file_path, 'w') as f:
        f.write('\n'.join(lines))
    
    return len(missing_imports)


def main():
    """Main function to fix missing imports."""
    # Paths
    project_root = Path(__file__).parent.parent
    mapping_path = project_root / 'docs' / 'requirements' / 'mapping.json'
    v2_models_path = project_root / 'src' / 'armodel' / 'v2' / 'models' / 'M2' / 'AUTOSARTemplates'
    
    print("Loading mapping.json...")
    mapping = load_mapping(mapping_path)
    print(f"Loaded {len(mapping)} class mappings")
    
    # Find all Python files in V2 models (excluding __init__.py)
    py_files = list(v2_models_path.rglob('*.py'))
    py_files = [f for f in py_files if f.name != '__init__.py']
    
    print(f"Found {len(py_files)} Python files to check")
    
    # Process each file
    total_imports_added = 0
    files_modified = 0
    
    for py_file in py_files:
        imports_added = add_missing_imports(py_file, mapping)
        if imports_added > 0:
            files_modified += 1
            total_imports_added += imports_added
            print(f"Added {imports_added} imports to {py_file.relative_to(project_root)}")
    
    print(f"\nSummary:")
    print(f"  Files modified: {files_modified}")
    print(f"  Total imports added: {total_imports_added}")


if __name__ == '__main__':
    main()