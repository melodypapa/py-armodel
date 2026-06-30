#!/usr/bin/env python3
"""
Deviation Check Script for py-armodel

This script checks for deviations between:
1. The documented AUTOSAR M2 model structure (docs/requirements/autosar_models.md)
2. The actual Python implementation (src/armodel/models/M2/)

It generates a deviation report in reports/deviation_package.md

Python Package Structure Rules for py-armodel:
==============================================
This project follows specific rules for Python package organization:

1. Leaf Packages (no subdirectories):
   - Classes defined in a single .py file
   - Package name = file name (without .py extension)
   - Example: CommonStructure/ImplementationDataType.py
   - Import: from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataType
   - Module path: armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataType

2. Non-Leaf Packages (have subdirectories):
   - Classes defined in __init__.py of the directory
   - Package name = directory name
   - Example: CommonStructure/__init__.py (has subdirectories like InternalBehavior/)
   - Import: from armodel.models.M2.AUTOSARTemplates.CommonStructure
   - Module path: armodel.models.M2.AUTOSARTemplates.CommonStructure

The deviation checker validates:
- Leaf packages should use flat .py files (not directories with __init__.py)
- Non-leaf packages should use __init__.py (not flat .py files)
"""

import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple


def parse_requirements_md(file_path: str) -> List[Tuple[str, str]]:
    """
    Parse the autosar_models.md file to extract the expected M2 hierarchy.

    Returns a list of tuples: (full_path, indent_level)
    """
    requirements = []
    path_stack = []  # Stack to track current path hierarchy

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue

            # Count leading spaces to determine hierarchy level
            indent = len(line) - len(line.lstrip())

            # Extract the element name (remove * prefix if present)
            element = line.lstrip().lstrip('*').strip()

            if not element:
                continue

            # Adjust path stack based on indent level
            # Each level is approximately 2 spaces
            level = indent // 2 + 1

            # Pop stack to the appropriate level
            while len(path_stack) >= level:
                path_stack.pop()

            # Build full path
            path_stack.append(element)
            full_path = '::'.join(path_stack)

            requirements.append((full_path, element, indent))

    return requirements


def get_python_classes_from_file(file_path: str) -> Set[str]:
    """
    Extract class names from a Python file using AST parsing.
    """
    classes = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content, filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.add(node.name)
    except (SyntaxError, UnicodeDecodeError):
        # Skip files that can't be parsed
        pass
    return classes


def scan_python_code(source_dir: str) -> Dict[str, str]:
    """
    Scan the Python source code to build a map of class names to their full paths.

    Returns: {class_name: full_python_path}
    """
    class_map = {}
    m2_path = Path(source_dir) / 'armodel' / 'models' / 'M2'

    if not m2_path.exists():
        print(f"Warning: {m2_path} does not exist")
        return class_map

    for py_file in m2_path.rglob('*.py'):
        # Get the relative path from M2 directory
        rel_path = py_file.relative_to(m2_path)
        filename = rel_path.parts[-1]  # Get filename with extension

        # Convert file path to module path based on py-armodel rules:
        # 1. For __init__.py: package = directory name (non-leaf packages)
        # 2. For regular .py files: package = directory name + filename (leaf packages)

        if filename == '__init__.py':
            # Non-leaf package: use directory path only
            module_parts = list(rel_path.parts[:-1])  # Remove __init__.py
            module_path = '.'.join(module_parts) if module_parts else ''
        else:
            # Leaf package: include filename (without .py extension) in the path
            # Example: ImplementationDataType.py -> ...CommonStructure.ImplementationDataType
            dir_parts = list(rel_path.parts[:-1])  # Directory path
            file_part = rel_path.parts[-1].replace('.py', '')  # Filename without extension
            module_parts = dir_parts + [file_part] if dir_parts else [file_part]
            module_path = '.'.join(module_parts) if module_parts else ''

        # Extract classes from the file
        classes = get_python_classes_from_file(py_file)

        # Build full Python path for each class
        for cls in classes:
            if module_path:
                full_path = f'armodel.models.M2.{module_path}.{cls}'
            else:
                full_path = f'armodel.models.M2.{cls}'
            class_map[cls] = full_path

    return class_map


def parse_m2_path(m2_path: str) -> Tuple[str, str, str]:
    """
    Parse an M2 path into components.

    Returns: (top_level, package, class_name)
    e.g., "M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDefinitionCollection"
    -> ("M2", "AUTOSARTemplates", "EcucDefinitionCollection")

    For deeper paths like "M2::AUTOSARTemplates::ECUCParameterDefTemplate::SubPackage::Class"
    -> ("M2", "AUTOSARTemplates::ECUCParameterDefTemplate::SubPackage", "Class")
    """
    parts = m2_path.split('::')
    if len(parts) < 3:
        return (parts[0] if parts else '', '', '')

    # Last part is the class name
    class_name = parts[-1]

    # First part is M2
    top_level = parts[0]

    # Everything in between is the package path
    package = '::'.join(parts[1:-1])

    return (top_level, package, class_name)


def python_path_from_m2_path(m2_path: str) -> str:
    """
    Convert an M2 path to expected Python path.

    e.g., "M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDefinitionCollection"
    -> "armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.EcucDefinitionCollection"
    """
    parts = m2_path.split('::')
    if parts[0] == 'M2':
        parts = parts[1:]  # Remove M2 prefix

    # Convert :: to .
    python_path = 'armodel.models.M2.' + '.'.join(parts)
    return python_path


def check_deviations(requirements: List[Tuple[str, str, int]], class_map: Dict[str, str]) -> Tuple[List[Dict], int]:
    """
    Check for deviations between requirements and actual implementation.

    Returns a tuple of (deviations list, match count)
    """
    deviations = []
    match_count = 0

    for full_path, element_name, indent in requirements:
        # Skip non-leaf nodes (these are packages/categories, not classes)
        # We check if it's a leaf by seeing if there are any items with deeper indent
        is_leaf = True
        for req_full_path, _, req_indent in requirements:
            if req_full_path.startswith(full_path + '::') and req_indent > indent:
                is_leaf = False
                break

        if not is_leaf:
            continue  # Skip package nodes, only check actual classes

        # Parse M2 path
        top_level, package, class_name = parse_m2_path(full_path)

        if not class_name:
            continue

        # Expected Python path
        expected_python_path = python_path_from_m2_path(full_path)

        # Check if class exists
        actual_python_path = class_map.get(class_name)

        if actual_python_path:
            # Class exists - check if path matches
            if actual_python_path == expected_python_path:
                match_count += 1
            else:
                status = "⚠ PATH_MISMATCH"
                deviations.append({
                    'status': status,
                    'm2_path': full_path,
                    'expected_python': expected_python_path,
                    'actual_python': actual_python_path,
                    'notes': 'Class exists but in different location'
                })
        else:
            status = "✗ MISSING"
            deviations.append({
                'status': status,
                'm2_path': full_path,
                'expected_python': expected_python_path,
                'actual_python': 'Not Found',
                'notes': f'Class {class_name} not found in source code'
            })

    return deviations, match_count


def find_extra_classes(requirements: List[Tuple[str, str, int]], class_map: Dict[str, str]) -> List[Dict]:
    """
    Find classes that exist in source but are not documented.
    """
    # Get all documented class names
    documented_classes = set()
    for full_path, element_name, indent in requirements:
        _, _, class_name = parse_m2_path(full_path)
        if class_name:
            documented_classes.add(class_name)

    extra_classes = []
    for class_name, python_path in class_map.items():
        if class_name not in documented_classes:
            extra_classes.append({
                'status': '+ EXTRA',
                'm2_path': 'Not Documented',
                'expected_python': 'N/A',
                'actual_python': python_path,
                'notes': 'Class exists but not documented'
            })

    return extra_classes


def generate_deviation_report(deviations: List[Dict], extra_classes: List[Dict], match_count: int, output_path: str):
    """
    Generate a markdown deviation report.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Deviation Report: M2 Model Structure\n\n')
        f.write('This report shows deviations between the documented AUTOSAR M2 model structure\n')
        f.write('and the actual Python implementation.\n\n')

        f.write('## Summary\n\n')
        total_missing = sum(1 for d in deviations if d['status'] == '✗ MISSING')
        total_mismatch = sum(1 for d in deviations if d['status'] == '⚠ PATH_MISMATCH')
        total_extra = len(extra_classes)
        total_documented = match_count + total_missing + total_mismatch

        f.write(f'- ✓ **Match**: {match_count} classes correctly implemented\n')
        f.write(f'- ✗ **Missing**: {total_missing} classes documented but not found\n')
        f.write(f'- ⚠ **Path Mismatch**: {total_mismatch} classes in wrong location\n')
        f.write(f'- + **Extra**: {total_extra} undocumented classes\n')
        f.write(f'- **Total Documented Classes**: {total_documented}\n')
        f.write(f'- **Total Deviations**: {len(deviations) + total_extra}\n\n')

        # Deviations Table
        if deviations:
            f.write('## Deviations Table\n\n')
            f.write('| Status | Path (M2 / Expected / Actual) | Notes |\n')
            f.write('|--------|------------------------------|-------|\n')

            for d in sorted(deviations, key=lambda x: x['m2_path']):
                # Combine paths into one cell with line breaks
                combined_path = f"M2: {d['m2_path']}<br>Expected: {d['expected_python']}<br>Actual: {d['actual_python']}"
                f.write(f"| {d['status']} | {combined_path} | {d['notes']} |\n")

            f.write('\n')

        # Extra Classes Table
        if extra_classes:
            f.write('## Extra Classes (Not Documented)\n\n')
            f.write('| Status | Path (M2 / Expected / Actual) | Notes |\n')
            f.write('|--------|------------------------------|-------|\n')

            for d in sorted(extra_classes, key=lambda x: x['actual_python']):
                # Combine paths into one cell with line breaks
                combined_path = f"M2: {d['m2_path']}<br>Expected: {d['expected_python']}<br>Actual: {d['actual_python']}"
                f.write(f"| {d['status']} | {combined_path} | {d['notes']} |\n")

            f.write('\n')

        if not deviations and not extra_classes:
            f.write('## Result\n\n')
            f.write('✓ No deviations found! All documented classes are implemented correctly.\n\n')

        f.write('## Legend\n\n')
        f.write('- ✓ MATCH: Class exists in expected location\n')
        f.write('- ✗ MISSING: Class documented but not found in source\n')
        f.write('- ⚠ PATH_MISMATCH: Class exists but in different package\n')
        f.write('- + EXTRA: Class exists but not documented\n')


def main():
    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    requirements_file = project_root / 'docs' / 'requirements' / 'autosar_models.md'
    source_dir = project_root / 'src'
    output_file = project_root / 'reports' / 'deviation_package.md'

    print("Py-ARModel Deviation Check Script")
    print("=" * 50)
    print(f"Requirements file: {requirements_file}")
    print(f"Source directory: {source_dir}")
    print(f"Output file: {output_file}")
    print()

    # Step 1: Parse requirements
    print("Step 1: Parsing requirements from autosar_models.md...")
    requirements = parse_requirements_md(str(requirements_file))
    print(f"  Found {len(requirements)} elements in requirements")

    # Step 2: Scan Python source code
    print("Step 2: Scanning Python source code...")
    class_map = scan_python_code(str(source_dir))
    print(f"  Found {len(class_map)} classes in source code")

    # Step 3: Check for deviations
    print("Step 3: Checking for deviations...")
    deviations, match_count = check_deviations(requirements, class_map)
    print(f"  Found {len(deviations)} deviations (missing or mismatched)")
    print(f"  Found {match_count} matches (correctly implemented)")

    # Step 4: Find extra classes
    print("Step 4: Finding extra (undocumented) classes...")
    extra_classes = find_extra_classes(requirements, class_map)
    print(f"  Found {len(extra_classes)} extra classes")

    # Step 5: Generate report
    print("Step 5: Generating deviation report...")
    generate_deviation_report(deviations, extra_classes, match_count, str(output_file))
    print(f"  Report written to: {output_file}")

    print()
    print("=" * 50)
    print("Deviation check complete!")
    print(f"[*] Matches: {match_count}")
    print(f"[x] Missing: {sum(1 for d in deviations if d['status'] == '✗ MISSING')}")
    print(f"[!] Mismatched: {sum(1 for d in deviations if d['status'] == '⚠ PATH_MISMATCH')}")
    print(f"[+] Extra: {len(extra_classes)}")
    print(f"Total deviations: {len(deviations) + len(extra_classes)}")


if __name__ == '__main__':
    main()
