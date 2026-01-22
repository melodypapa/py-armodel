#!/usr/bin/env python3
"""
Class Hierarchy Deviation Check Script for py-armodel

This script checks for deviations between:
1. The documented AUTOSAR M2 class hierarchy (docs/requirements/software_components_hierarchy.md)
2. The actual Python implementation class hierarchy (src/armodel/models/M2/)

It generates a deviation report in docs/requirements/deviation_class_hierarchy.md

The hierarchy checker validates:
- Parent-child inheritance relationships
- Abstract class annotations
- Complete class tree structure
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional


def parse_hierarchy_md(file_path: str) -> Dict[str, Tuple[str, bool]]:
    """
    Parse the software_components_hierarchy.md file to extract the expected class hierarchy.

    Returns a dict: {class_name: (parent_class_name, is_abstract)}
    """
    hierarchy = {}
    path_stack = []  # Stack to track current path hierarchy

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip() or line.strip().startswith('#'):
                continue

            # Count leading spaces to determine hierarchy level
            indent = len(line) - len(line.lstrip())

            # Extract the element name (remove * prefix if present)
            element = line.lstrip().lstrip('*').strip()

            if not element:
                continue

            # Check if abstract
            is_abstract = '(abstract)' in element
            class_name = element.replace('(abstract)', '').strip()

            # Adjust path stack based on indent level
            # Each level is approximately 2 spaces
            level = indent // 2

            # Pop stack to the appropriate level
            while len(path_stack) > level:
                path_stack.pop()

            # Parent is the last item in the stack
            parent_class = path_stack[-1] if path_stack else None

            # Add current class to stack
            path_stack.append(class_name)

            # Store hierarchy info
            hierarchy[class_name] = (parent_class, is_abstract)

    return hierarchy


def get_class_info_from_file(file_path: str) -> Dict[str, Tuple[str, bool]]:
    """
    Extract class names and their inheritance info from a Python file using AST parsing.

    Returns: {class_name: (parent_class_name, is_abstract)}
    """
    classes = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content, filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Extract parent class name
                    parent_class = None
                    if node.bases:
                        for base in node.bases:
                            if isinstance(base, ast.Name):
                                parent_class = base.id
                                break

                    # Check if abstract (has ABCMeta metaclass or abstract methods or instantiation check)
                    is_abstract = False
                    # Check metaclass
                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Name):
                            if decorator.id == 'abstractmethod':
                                is_abstract = True
                                break
                        elif isinstance(decorator, ast.Call):
                            if isinstance(decorator.func, ast.Name) and decorator.func.id == 'ABCMeta':
                                is_abstract = True
                                break

                    if not is_abstract:
                        # Check for abstract methods
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                for decorator in item.decorator_list:
                                    if isinstance(decorator, ast.Name) and decorator.id == 'abstractmethod':
                                        is_abstract = True
                                        break
                                if is_abstract:
                                    break

                    if not is_abstract:
                        # Check for instantiation check pattern in __init__ method
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                                for stmt in ast.walk(item):
                                    if isinstance(stmt, ast.If):
                                        # Check if it's a type(self) is ClassName check
                                        if (isinstance(stmt.test, ast.Compare) and 
                                            len(stmt.test.ops) == 2 and
                                            isinstance(stmt.test.ops[0], ast.Call) and
                                            isinstance(stmt.test.ops[1], ast.Name) and
                                            isinstance(stmt.test.left, ast.Call) and
                                            isinstance(stmt.test.left.func, ast.Name) and
                                            stmt.test.left.func.id == 'type' and
                                            stmt.test.comparators[0].id == 'is' and
                                            isinstance(stmt.test.left.args[0], ast.Name) and
                                            stmt.test.left.args[0].id == 'self' and
                                            stmt.test.right.id == node.name):
                                            is_abstract = True
                                            break
                                if is_abstract:
                                    break

                    classes[node.name] = (parent_class, is_abstract)
    except (SyntaxError, UnicodeDecodeError):
        # Skip files that can't be parsed
        pass
    return classes


def scan_python_hierarchy(source_dir: str) -> Dict[str, Tuple[str, bool]]:
    """
    Scan the Python source code to build a map of class names to their inheritance info.

    Returns: {class_name: (parent_class_name, is_abstract)}
    """
    class_map = {}
    m2_path = Path(source_dir) / 'armodel' / 'models' / 'M2'

    if not m2_path.exists():
        print(f"Warning: {m2_path} does not exist")
        return class_map

    for py_file in m2_path.rglob('*.py'):
        # Extract classes from the file
        classes = get_class_info_from_file(py_file)
        class_map.update(classes)

    return class_map


def check_hierarchy_deviations(
    documented_hierarchy: Dict[str, Tuple[str, bool]],
    actual_hierarchy: Dict[str, Tuple[str, bool]]
) -> Tuple[List[Dict], int]:
    """
    Check for deviations between documented and actual class hierarchy.

    Returns a tuple of (deviations list, match count)
    """
    deviations = []
    match_count = 0

    for class_name, (doc_parent, doc_abstract) in documented_hierarchy.items():
        if class_name not in actual_hierarchy:
            # Class not found in source
            deviations.append({
                'status': '✗ MISSING',
                'class_name': class_name,
                'documented_parent': doc_parent,
                'documented_abstract': doc_abstract,
                'actual_parent': 'Not Found',
                'actual_abstract': 'N/A',
                'notes': f'Class not found in source code'
            })
            continue

        actual_parent, actual_abstract = actual_hierarchy[class_name]

        # Check parent match
        parent_match = doc_parent == actual_parent

        # Check abstract match
        abstract_match = doc_abstract == actual_abstract

        if parent_match and abstract_match:
            match_count += 1
        else:
            issues = []
            if not parent_match:
                issues.append(f'parent mismatch (expected {doc_parent}, got {actual_parent})')
            if not abstract_match:
                issues.append(f'abstract mismatch (expected {doc_abstract}, got {actual_abstract})')

            deviations.append({
                'status': '⚠ MISMATCH',
                'class_name': class_name,
                'documented_parent': doc_parent,
                'documented_abstract': doc_abstract,
                'actual_parent': actual_parent,
                'actual_abstract': actual_abstract,
                'notes': ', '.join(issues)
            })

    return deviations, match_count


def find_extra_classes(
    documented_hierarchy: Dict[str, Tuple[str, bool]],
    actual_hierarchy: Dict[str, Tuple[str, bool]]
) -> List[Dict]:
    """
    Find classes that exist in source but are not documented.
    """
    extra_classes = []
    for class_name, (parent, is_abstract) in actual_hierarchy.items():
        if class_name not in documented_hierarchy:
            extra_classes.append({
                'status': '+ EXTRA',
                'class_name': class_name,
                'documented_parent': 'N/A',
                'documented_abstract': 'N/A',
                'actual_parent': parent,
                'actual_abstract': is_abstract,
                'notes': f'Class exists but not documented'
            })

    return extra_classes


def generate_hierarchy_report(
    deviations: List[Dict],
    extra_classes: List[Dict],
    match_count: int,
    total_documented: int,
    output_path: str
):
    """
    Generate a markdown hierarchy deviation report.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Class Hierarchy Deviation Report\n\n')
        f.write('This report shows deviations between the documented AUTOSAR M2 class hierarchy\n')
        f.write('and the actual Python implementation class hierarchy.\n\n')

        f.write('## Summary\n\n')
        total_missing = sum(1 for d in deviations if d['status'] == '✗ MISSING')
        total_mismatch = sum(1 for d in deviations if d['status'] == '⚠ MISMATCH')
        total_extra = len(extra_classes)

        f.write(f'- ✓ **Match**: {match_count} classes with correct hierarchy\n')
        f.write(f'- ✗ **Missing**: {total_missing} classes documented but not found\n')
        f.write(f'- ⚠ **Hierarchy Mismatch**: {total_mismatch} classes with wrong parent/abstract\n')
        f.write(f'- + **Extra**: {total_extra} undocumented classes\n')
        f.write(f'- **Total Documented Classes**: {total_documented}\n')
        f.write(f'- **Total Deviations**: {len(deviations) + total_extra}\n\n')

        # Deviations Table
        if deviations:
            f.write('## Hierarchy Deviations Table\n\n')
            f.write('| Status | Class | Documented (Parent, Abstract) | Actual (Parent, Abstract) | Notes |\n')
            f.write('|--------|-------|-------------------------------|---------------------------|-------|\n')

            for d in sorted(deviations, key=lambda x: x['class_name']):
                doc_info = f"{d['documented_parent']}, {d['documented_abstract']}"
                act_info = f"{d['actual_parent']}, {d['actual_abstract']}"
                f.write(f"| {d['status']} | {d['class_name']} | {doc_info} | {act_info} | {d['notes']} |\n")

            f.write('\n')

        # Extra Classes Table
        if extra_classes:
            f.write('## Extra Classes (Not Documented)\n\n')
            f.write('| Status | Class | Documented (Parent, Abstract) | Actual (Parent, Abstract) | Notes |\n')
            f.write('|--------|-------|-------------------------------|---------------------------|-------|\n')

            for d in sorted(extra_classes, key=lambda x: x['class_name']):
                doc_info = f"{d['documented_parent']}, {d['documented_abstract']}"
                act_info = f"{d['actual_parent']}, {d['actual_abstract']}"
                f.write(f"| {d['status']} | {d['class_name']} | {doc_info} | {act_info} | {d['notes']} |\n")

            f.write('\n')

        if not deviations and not extra_classes:
            f.write('## Result\n\n')
            f.write('✓ No deviations found! All documented classes have correct hierarchy.\n\n')

        f.write('## Legend\n\n')
        f.write('- ✓ MATCH: Class has correct parent and abstract status\n')
        f.write('- ✗ MISSING: Class documented but not found in source\n')
        f.write('- ⚠ MISMATCH: Class has wrong parent or abstract status\n')
        f.write('- + EXTRA: Class exists but not documented\n')


def main():
    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    hierarchy_file = project_root / 'docs' / 'requirements' / 'software_components_hierarchy.md'
    source_dir = project_root / 'src'
    output_file = project_root / 'docs' / 'requirements' / 'deviation_class_hierarchy.md'

    print(f"Py-ARModel Class Hierarchy Deviation Check Script")
    print(f"=" * 50)
    print(f"Hierarchy file: {hierarchy_file}")
    print(f"Source directory: {source_dir}")
    print(f"Output file: {output_file}")
    print()

    # Step 1: Parse documented hierarchy
    print("Step 1: Parsing documented hierarchy from software_components_hierarchy.md...")
    documented_hierarchy = parse_hierarchy_md(str(hierarchy_file))
    print(f"  Found {len(documented_hierarchy)} documented classes")

    # Step 2: Scan Python source code
    print("Step 2: Scanning Python source code for class hierarchy...")
    actual_hierarchy = scan_python_hierarchy(str(source_dir))
    print(f"  Found {len(actual_hierarchy)} classes in source code")

    # Step 3: Check for hierarchy deviations
    print("Step 3: Checking for hierarchy deviations...")
    deviations, match_count = check_hierarchy_deviations(documented_hierarchy, actual_hierarchy)
    print(f"  Found {len(deviations)} deviations (missing or mismatched)")
    print(f"  Found {match_count} matches (correct hierarchy)")

    # Step 4: Find extra classes
    print("Step 4: Finding extra (undocumented) classes...")
    extra_classes = find_extra_classes(documented_hierarchy, actual_hierarchy)
    print(f"  Found {len(extra_classes)} extra classes")

    # Step 5: Generate report
    print("Step 5: Generating hierarchy deviation report...")
    generate_hierarchy_report(deviations, extra_classes, match_count, len(documented_hierarchy), str(output_file))
    print(f"  Report written to: {output_file}")

    print()
    print("=" * 50)
    print("Hierarchy deviation check complete!")
    print(f"[*] Matches: {match_count}")
    print(f"[x] Missing: {sum(1 for d in deviations if d['status'] == '✗ MISSING')}")
    print(f"[!] Mismatched: {sum(1 for d in deviations if d['status'] == '⚠ MISMATCH')}")
    print(f"[+] Extra: {len(extra_classes)}")
    print(f"Total deviations: {len(deviations) + len(extra_classes)}")


if __name__ == '__main__':
    main()