#!/usr/bin/env python3
"""
Code Utilities Module for py-armodel

This module provides utility functions for code validation, formatting,
parsing, and merging.
"""

import ast
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Tuple


def validate_code(code: str, class_name: str) -> Tuple[bool, List[str]]:
    """Validate that generated code is syntactically correct.

    Args:
        code: Generated Python code
        class_name: Name of the class (for error reporting)

    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    try:
        ast.parse(code)
        return True, []
    except SyntaxError as e:
        error_msg = f"Syntax error at line {e.lineno}: {e.msg}"
        if e.text:
            error_msg += f"\n  {e.text.strip()}"
        errors.append(error_msg)
        return False, errors


def format_code_with_ruff(file_path: Path) -> bool:
    """Format a Python file using ruff.

    Args:
        file_path: Path to the Python file to format

    Returns:
        True if formatting succeeded, False otherwise
    """
    try:
        result = subprocess.run(
            ['python3', '-m', 'ruff', 'format', str(file_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # ruff not available, skip formatting
        return False


def parse_existing_class(class_file: Path) -> Dict[str, Any]:
    """Parse an existing class file to extract methods and attributes.

    Args:
        class_file: Path to the existing class file

    Returns:
        Dictionary with 'methods', 'attributes', 'imports', 'docstring',
        'class_def', 'init_code'
    """
    result = {
        'methods': {},  # method_name: (signature, full_code)
        'attributes': set(),  # attribute names
        'imports': [],  # import lines
        'docstring': '',  # class docstring
        'class_def': '',  # class definition line
        'init_code': '',  # __init__ method code
    }

    try:
        with open(class_file, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content, filename=str(class_file))

        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    result['imports'].append(f'import {alias.name}')
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                names = ', '.join(alias.name for alias in node.names)
                result['imports'].append(f'from {module} import {names}')

        # Find class definition
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                result['class_def'] = f'class {node.name}({", ".join([ast.unparse(base) for base in node.bases])}):'

                # Extract docstring
                if (node.body and isinstance(node.body[0], ast.Expr) and
                        isinstance(node.body[0].value, ast.Constant)):
                    result['docstring'] = ast.unparse(node.body[0].value)

                # Extract methods and attributes
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_name = item.name
                        method_code = ast.unparse(item)

                        if method_name == '__init__':
                            result['init_code'] = method_code
                        else:
                            # Extract just the signature line
                            signature = f'def {method_name}({ast.unparse(item.args)}):'
                            result['methods'][method_name] = (signature, method_code)

                    elif isinstance(item, ast.Assign) or isinstance(item, ast.AnnAssign):
                        # Extract attribute assignments from __init__
                        targets = item.targets if isinstance(item, ast.Assign) else [item.target]
                        for target in targets:
                            if isinstance(target, ast.Name):
                                result['attributes'].add(target.id)
                break

    except (SyntaxError, IOError, UnicodeDecodeError) as e:
        print(f"  ⚠️  Could not parse existing class: {e}")

    return result


def merge_class_with_existing(
    generated_code: str,
    existing_info: Dict[str, Any],
    class_name: str
) -> Tuple[str, List[str]]:
    """Merge generated class code with existing implementation.

    Args:
        generated_code: Newly generated class code
        existing_info: Information about existing class (from parse_existing_class)
        class_name: Name of the class

    Returns:
        Tuple of (merged_code, list_of_changes_made)
    """
    changes = []

    # Parse generated code
    try:
        gen_tree = ast.parse(generated_code)
    except SyntaxError:
        return generated_code, ['Failed to parse generated code']

    # Extract generated elements
    gen_methods = {}
    gen_docstring = ''
    gen_init_code = ''
    gen_bases = []

    for node in gen_tree.body:
        if isinstance(node, ast.ClassDef):
            # Extract bases for class definition
            gen_bases = [ast.unparse(base) for base in node.bases]

            # Extract docstring
            if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Constant)):
                gen_docstring = node.body[0].value.value

            # Extract methods
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_code = ast.unparse(item)
                    if item.name == '__init__':
                        gen_init_code = method_code
                    else:
                        gen_methods[item.name] = method_code
            break

    # Build merged code
    merged_lines = []
    added_methods = []

    # Collect and merge imports
    existing_imports = set(existing_info.get('imports', []))
    all_imports = set(existing_imports)

    # Add imports from generated code
    for line in generated_code.split('\n'):
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from '):
            if stripped not in all_imports:
                all_imports.add(stripped)

    # Write imports
    for imp in sorted(all_imports):
        merged_lines.append(imp)

    merged_lines.append('')

    # Write class definition
    bases_str = ', '.join(gen_bases) if gen_bases else 'ARObject'
    merged_lines.append(f'class {class_name}({bases_str}):')

    # Write docstring (prefer generated if it has sources)
    docstring = gen_docstring if 'Sources:' in gen_docstring else existing_info.get('docstring', gen_docstring)
    if docstring:
        merged_lines.append('    """')
        for line in docstring.split('\n'):
            merged_lines.append(f'    {line}')
        merged_lines.append('    """')

    def indent_code(code: str, indent: int = 4) -> List[str]:
        """Indent code lines for class body."""
        lines = []
        for line in code.split('\n'):
            if line.strip():  # Only indent non-empty lines
                lines.append(' ' * indent + line)
            else:
                lines.append(line)
        return lines

    # Write __init__ (prefer existing, otherwise generated)
    init_code = existing_info.get('init_code') or gen_init_code
    if init_code:
        merged_lines.append('')
        merged_lines.extend(indent_code(init_code))

    # Write existing methods
    existing_methods = existing_info.get('methods', {})
    for method_name in sorted(existing_methods.keys()):
        _, method_code = existing_methods[method_name]
        merged_lines.append('')
        merged_lines.extend(indent_code(method_code))

    # Write generated methods that don't exist
    for method_name in sorted(gen_methods.keys()):
        if method_name not in existing_methods:
            merged_lines.append('')
            merged_lines.extend(indent_code(gen_methods[method_name]))
            added_methods.append(method_name)
            changes.append(f"Added method: {method_name}")

    if added_methods:
        changes.append(f"Added {len(added_methods)} missing method(s)")

    return '\n'.join(merged_lines) + '\n', changes


def run_tests(
    comparisons: List[Dict[str, Any]],
    project_root: Path,
    dry_run: bool = False
) -> Dict[str, Any]:
    """Run pytest on generated test files to verify the generated class code.

    Args:
        comparisons: List of comparison dictionaries with package and class info
        project_root: Root directory of the project
        dry_run: Whether this is a dry run (skip actual testing)

    Returns:
        Dictionary with test statistics
    """
    print("\n" + "=" * 60)
    print("Running Tests on Generated Classes")
    print("=" * 60)

    if dry_run:
        print("[DRY RUN MODE - Tests will not be executed]")
        return {'tests_run': 0, 'tests_passed': 0, 'tests_failed': 0, 'test_files': []}

    test_files = []
    stats = {
        'tests_run': 0,
        'tests_passed': 0,
        'tests_failed': 0,
        'test_files': []
    }

    # Collect test files
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']

        for cls in classes:
            if cls['status'] == '❌ Missing':
                class_name = cls['name']

                if pkg_name.startswith('M2::'):
                    relative = pkg_name[4:].replace('::', '/')
                    test_file = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative / f'test_{class_name}.py'

                if test_file.exists():
                    test_files.append(str(test_file))

    if not test_files:
        print("No new test files found to run.")
        return stats

    print(f"Found {len(test_files)} test file(s) to run")

    # Collect class files for ruff check
    class_files = []
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']

        for cls in classes:
            if cls['status'] == '❌ Missing':
                class_name = cls['name']

                if pkg_name.startswith('M2::'):
                    relative = pkg_name[4:].replace('::', '/')
                    class_file = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative / f'{class_name}.py'

                if class_file.exists():
                    class_files.append(str(class_file))

    # Run ruff check first
    if class_files:
        print("\nRunning ruff check on generated class files...")
        try:
            result = subprocess.run(
                ['python3', '-m', 'ruff', 'check'] + class_files,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print(f"  ✓ Ruff check passed for {len(class_files)} file(s)")
            else:
                print("  ✗ Ruff check failed:")
                print(f"  {result.stdout}")
                print(f"  {result.stderr}")
        except Exception as e:
            print(f"  ✗ Error running ruff: {e}")

    # Run pytest on each test file
    for test_file in test_files:
        print(f"\nRunning: {test_file}")
        try:
            result = subprocess.run(
                ['python3', '-m', 'pytest', test_file, '-v'],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print("  ✓ All tests passed")

                for line in result.stdout.split('\n'):
                    if 'passed' in line:
                        print(f"  {line.strip()}")

                stats['tests_passed'] += 1
            else:
                print("  ✗ Some tests failed")
                print(f"  Output:\n{result.stdout}")
                print(f"  Errors:\n{result.stderr}")
                stats['tests_failed'] += 1

            stats['tests_run'] += 1
            stats['test_files'].append(test_file)

        except subprocess.TimeoutExpired:
            print("  ✗ Test timed out")
            stats['tests_failed'] += 1
        except Exception as e:
            print(f"  ✗ Error running test: {e}")
            stats['tests_failed'] += 1

    return stats


def run_flake8_check(generated_files: List[str], project_root: Path) -> None:
    """Run flake8 check on generated files.

    Args:
        generated_files: List of file paths to check
        project_root: Root directory of the project
    """
    if not generated_files:
        print("No generated files to check")
        return

    print(f"Running flake8 on {len(generated_files)} generated file(s)...")
    try:
        result = subprocess.run(
            ['flake8', '--select=E9,F63,F7,F82'] + generated_files,
            cwd=project_root,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("✅ Flake8 check passed - no syntax errors")
        else:
            print("⚠️ Flake8 check found issues:")
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
    except FileNotFoundError:
        print("⚠️ Flake8 not found - skipping syntax check")
    except Exception as e:
        print(f"⚠️ Error running flake8: {e}")
