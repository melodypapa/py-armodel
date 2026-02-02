#!/usr/bin/env python3
"""
Package Implementation Fix Script for py-armodel

This script fixes missing AUTOSAR M2 package implementations and generates test cases.
It performs the following:
- Generates missing classes based on requirements
- Generates pytest test cases for generated classes
- Runs ruff check on generated code
- Runs pytest to verify generated code

Usage:
    python scripts/fix-package-implementation.py
    python scripts/fix-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate
    python scripts/fix-package-implementation.py -p M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
    python scripts/fix-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate --dry-run
"""

import argparse
from pathlib import Path
from typing import Dict, List, Any

# Import from our modular library
from lib import (
    get_all_packages,
    find_class_in_requirements,
    build_type_index,
    update_cache_for_new_class,
    get_generation_report,
    reset_generation_report,
    get_missing_types_to_generate,
    clear_missing_types_to_generate,
    generate_class_code,
    generate_test_case,
    print_generation_report,
    validate_code,
    format_code_with_ruff,
    parse_existing_class,
    merge_class_with_existing,
    run_tests,
    run_flake8_check,
)


# Global cache to track created classes
created_classes = set()

# Global dry_run flag
dry_run_mode = False


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Fix missing AUTOSAR M2 package implementations and generate tests',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s M2::xxx::xxx                   Fix single package
  %(prog)s M2::xxx::xxx::xxx             Fix subpackage
  %(prog)s M2::xxx::xxx --dry-run         Preview fixes
  %(prog)s M2::xxx::xxx --merge           Merge updates into existing classes
        """
    )
    parser.add_argument(
        'package',
        type=str,
        help='Specific package to fix (format: M2::xxx::xxxx)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without modifying files'
    )
    parser.add_argument(
        '--merge',
        action='store_true',
        help='Merge generated code into existing classes (preserves manual changes)'
    )
    return parser.parse_args()


def create_missing_class_from_json(
    project_root: Path,
    requirements_dir: Path,
    type_name: str,
    depth: int = 0
) -> bool:
    """Create a missing class from JSON requirements if found.

    This function will also recursively generate any missing attribute type classes.

    Args:
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory
        type_name: Name of the class to create
        depth: Recursion depth (to prevent infinite loops)

    Returns:
        True if class was created, False otherwise
    """
    from lib import (
        find_class_in_requirements,
        generate_class_code,
        update_cache_for_new_class,
        generate_test_case,
        get_missing_types_to_generate,
        clear_missing_types_to_generate,
    )

    if type_name in created_classes:
        return True

    # Prevent infinite recursion
    if depth > 10:
        print(f"  ⚠️  Maximum recursion depth reached for {type_name}")
        return False

    created_classes.add(type_name)

    class_data = find_class_in_requirements(requirements_dir, type_name)

    if not class_data:
        return False

    class_info = class_data['class_info']
    package_path = class_data['package_path']

    # Determine the file location
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'
    else:
        relative = package_path.replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'

    # Check if this package is implemented as a single file
    if package_file.exists():
        print(f"  ⚠️  Package is a single file ({package_file.name}), cannot create {type_name}")
        return False

    class_file = package_dir / f'{type_name}.py'

    # Skip if already exists
    if class_file.exists():
        update_cache_for_new_class(project_root, type_name, package_path)
        return True

    if dry_run_mode:
        print(f"  [Would create missing class from JSON: {type_name}]")
        update_cache_for_new_class(project_root, type_name, package_path)
        return True

    # Step 1: Generate code to discover missing types
    # This populates the _missing_types_to_generate set
    try:
        code = generate_class_code(class_info, package_path, project_root, requirements_dir)

        # Validate code before writing
        is_valid, errors = validate_code(code, type_name)
        if not is_valid:
            print(f"  ✗ Validation failed for {type_name}:")
            for error in errors:
                print(f"    {error}")
            return False
    except Exception as e:
        print(f"  ✗ Error generating code for '{type_name}': {e}")
        return False

    # Step 2: Recursively generate missing attribute types first
    missing_types = get_missing_types_to_generate()
    if missing_types:
        print(f"  → Found {len(missing_types)} missing attribute type(s) for {type_name}")
        for missing_type in sorted(missing_types):
            if missing_type not in created_classes:
                print(f"    → Recursively generating {missing_type}")
                if not create_missing_class_from_json(
                    project_root, requirements_dir, missing_type, depth + 1
                ):
                    print(f"    ⚠️  Failed to generate {missing_type}, continuing...")

        # Clear the missing types set for the next class
        clear_missing_types_to_generate()

        # Regenerate code now that dependencies exist
        code = generate_class_code(class_info, package_path, project_root, requirements_dir)

    # Step 3: Write the main class file
    try:
        package_dir.mkdir(parents=True, exist_ok=True)
        with open(class_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')

        update_cache_for_new_class(project_root, type_name, package_path)

        # Update or create __init__.py with wildcard import
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()
            if f'from .{type_name} import *' not in init_content:
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'from .{type_name} import *\n')
        else:
            # Create __init__.py with wildcard import
            with open(parent_init, 'w', encoding='utf-8') as f:
                f.write(f'from .{type_name} import *\n')

        # Generate test case
        # For package directories, import from package (not class module)
        module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}'
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{type_name}.py'

        test_code = generate_test_case(type_name, class_info, package_path, module_path, requirements_dir, project_root)

        if dry_run_mode:
            print(f"  [Would create test file: {test_file.relative_to(project_root)}]")
        else:
            test_dir.mkdir(parents=True, exist_ok=True)
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_code + '\n')

            test_parent_init = test_dir / '__init__.py'
            if not test_parent_init.exists():
                with open(test_parent_init, 'w', encoding='utf-8') as f:
                    f.write('')

        return True
    except Exception as e:
        print(f"  ✗ Error creating class '{type_name}': {e}")
        return False


def get_package_has_subpackages(requirements_dir: Path, package_path: str) -> bool:
    """Check if a package has subpackages based on requirements JSON.

    Args:
        requirements_dir: Path to requirements directory
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)

    Returns:
        True if package has subpackages, False otherwise
    """
    import json

    # Remove M2:: prefix (4 characters)
    if package_path.startswith('M2::'):
        package_path = package_path[4:]

    # Replace :: with _ to match JSON file naming
    json_name = 'M2_' + package_path.replace('::', '_') + '.json'
    json_file = requirements_dir / 'packages' / json_name

    if not json_file.exists():
        return False

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return bool(data.get('subpackages', []))
    except (json.JSONDecodeError, IOError):
        return False


def determine_package_structure(requirements_dir: Path, package_path: str) -> str:
    """Determine the expected package structure from requirements.

    Args:
        requirements_dir: Path to requirements directory
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate)

    Returns:
        'directory' if package should be a directory, 'file' if single file
    """
    has_subpackages = get_package_has_subpackages(requirements_dir, package_path)
    return 'directory' if has_subpackages else 'file'


def detect_current_structure(project_root: Path, package_path: str) -> str:
    """Detect the current filesystem structure for a package.

    Args:
        project_root: Root directory of the project
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate)

    Returns:
        'file', 'directory', 'hybrid', or 'none'
    """
    # Remove M2:: prefix
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
    else:
        relative = package_path.replace('::', '/')

    python_path = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
    py_file = python_path.with_suffix('.py')

    file_exists = py_file.exists()
    dir_exists = python_path.is_dir()

    if file_exists and dir_exists:
        return 'hybrid'
    elif file_exists:
        return 'file'
    elif dir_exists:
        return 'directory'
    else:
        return 'none'


def create_backup(file_or_dir: Path) -> Path:
    """Create a backup of a file or directory.

    Args:
        file_or_dir: Path to file or directory to backup

    Returns:
        Path to the backup location
    """
    import shutil

    if file_or_dir.is_dir():
        backup_path = file_or_dir.with_suffix('.backup')
        if backup_path.exists():
            shutil.rmtree(backup_path)
        shutil.copytree(file_or_dir, backup_path)
    else:
        backup_path = file_or_dir.with_suffix(file_or_dir.suffix + '.backup')
        shutil.copy2(file_or_dir, backup_path)

    return backup_path


def restore_from_backup(file_or_dir: Path) -> bool:
    """Restore a file or directory from its backup.

    Args:
        file_or_dir: Path to file or directory to restore

    Returns:
        True if successful, False otherwise
    """
    import shutil

    if file_or_dir.is_dir():
        backup_path = file_or_dir.with_suffix('.backup')
        if backup_path.is_dir():
            if file_or_dir.exists():
                shutil.rmtree(file_or_dir)
            shutil.copytree(backup_path, file_or_dir)
            return True
    else:
        backup_path = file_or_dir.with_suffix(file_or_dir.suffix + '.backup')
        if backup_path.exists():
            shutil.copy2(backup_path, file_or_dir)
            return True

    return False


def migrate_file_to_directory(file_path: Path, package_path: str, project_root: Path, requirements_dir: Path) -> bool:
    """Migrate a single .py file to a directory structure.

    Splits a single .py file containing multiple classes into separate files
    in a directory, with __init__.py providing wildcard imports.

    Args:
        file_path: Path to the .py file to split
        package_path: Package path (for creating __init__.py content)
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory

    Returns:
        True if successful, False otherwise
    """
    import ast
    import shutil

    print(f"  [Migrate] Splitting {file_path.name} into directory structure")

    # Create backup
    backup_path = create_backup(file_path)
    print(f"  ✓ Backup created: {backup_path.relative_to(project_root)}")

    try:
        # Parse the Python file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content, filename=str(file_path))

        # Extract imports, classes, and module-level docstring
        imports = []
        classes = []
        module_docstring = None

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(ast.unparse(node))
            elif isinstance(node, ast.ImportFrom):
                imports.append(ast.unparse(node))
            elif isinstance(node, ast.ClassDef):
                classes.append(node)
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                if module_docstring is None and isinstance(node.value.value, str):
                    module_docstring = node.value.value

        # Create directory
        dir_path = file_path.parent / file_path.stem
        dir_path.mkdir(exist_ok=True)

        # Create __init__.py
        init_path = dir_path / '__init__.py'
        with open(init_path, 'w', encoding='utf-8') as f:
            if module_docstring:
                f.write(f'"""\n{module_docstring}\n"""\n\n')
            for imp in imports:
                f.write(imp + '\n')
            for cls in classes:
                f.write(f'from .{cls.name} import *\n')

        # Create individual class files
        for cls in classes:
            class_file = dir_path / f'{cls.name}.py'
            with open(class_file, 'w', encoding='utf-8') as f:
                # Write imports
                for imp in imports:
                    f.write(imp + '\n')
                f.write('\n')
                # Write class definition
                f.write(ast.unparse(cls) + '\n')

        # Delete original file
        file_path.unlink()
        print(f"  ✓ Deleted original file: {file_path.relative_to(project_root)}")
        print(f"  ✓ Created directory: {dir_path.relative_to(project_root)}/")
        print(f"    - {len(classes)} class file(s)")
        print(f"    - __init__.py with wildcard imports")

        return True

    except Exception as e:
        print(f"  ✗ Migration failed: {e}")
        print(f"  ↻ Rolling back...")
        if restore_from_backup(file_path):
            print(f"  ✓ Rollback complete")
        else:
            print(f"  ✗ Rollback failed - backup may be at: {backup_path}")
        return False


def migrate_directory_to_file(dir_path: Path, package_path: str, project_root: Path) -> bool:
    """Migrate a directory structure to a single .py file.

    Merges all class files from a directory into a single .py file,
    then deletes the directory.

    Args:
        dir_path: Path to the directory to merge
        package_path: Package path (for documentation)
        project_root: Root directory of the project

    Returns:
        True if successful, False otherwise
    """
    import ast
    import shutil

    print(f"  [Migrate] Merging directory {dir_path.name}/ into single file")

    # Create backup
    backup_path = create_backup(dir_path)
    print(f"  ✓ Backup created: {backup_path.relative_to(project_root)}")

    try:
        # Collect all imports and classes
        all_imports = {}  # Use dict to deduplicate
        all_classes = []

        for py_file in dir_path.glob('*.py'):
            if py_file.name == '__init__.py':
                continue

            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                tree = ast.parse(content, filename=str(py_file))

            # Extract imports
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    imp_str = ast.unparse(node)
                    all_imports[imp_str] = True

            # Extract classes
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    all_classes.append(node)

        # Sort classes by line number for consistent ordering
        all_classes.sort(key=lambda c: c.lineno)

        # Determine output file path
        output_file = dir_path.parent / f'{dir_path.name}.py'

        # Create merged file
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write deduplicated imports
            if all_imports:
                for imp in sorted(all_imports.keys()):
                    f.write(imp + '\n')
                f.write('\n')

            # Write all classes
            for cls in all_classes:
                f.write('\n')
                f.write(ast.unparse(cls) + '\n')

        # Delete directory
        shutil.rmtree(dir_path)
        print(f"  ✓ Deleted directory: {dir_path.relative_to(project_root)}/")
        print(f"  ✓ Created file: {output_file.relative_to(project_root)}")
        print(f"    - {len(all_classes)} class(es)")
        print(f"    - {len(all_imports)} unique import(s)")

        return True

    except Exception as e:
        print(f"  ✗ Migration failed: {e}")
        print(f"  ↻ Rolling back...")
        if restore_from_backup(dir_path):
            print(f"  ✓ Rollback complete")
        else:
            print(f"  ✗ Rollback failed - backup may be at: {backup_path}")
        return False


def remove_inline_class_from_init(init_file: Path, class_name: str) -> bool:
    """Remove an inline class definition from __init__.py.

    This is used when a class is being moved from __init__.py to its own file.
    The function parses the __init__.py, removes the class definition, and
    rewrites the file without the class.

    Args:
        init_file: Path to the __init__.py file
        class_name: Name of the class to remove

    Returns:
        True if successful, False otherwise
    """
    import ast

    try:
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if class is defined inline
        if f'class {class_name}(' not in content:
            return True  # Nothing to remove

        # Parse the file
        tree = ast.parse(content, filename=str(init_file))

        # Find and remove the class definition
        new_nodes = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                continue  # Skip this class
            new_nodes.append(node)

        # Reconstruct the file without the class
        new_tree = ast.Module(body=new_nodes, type_ignores=[])
        new_content = ast.unparse(new_tree)

        # Ensure file ends with newline
        if not new_content.endswith('\n'):
            new_content += '\n'

        # Write back
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True
    except Exception as e:
        print(f"  ✗ Error removing class from __init__.py: {e}")
        return False


def fix_missing_class(
    class_name: str,
    class_info: Dict[str, Any],
    package_path: str,
    project_root: Path,
    requirements_dir: Path,
    dry_run: bool = False,
    merge: bool = False
) -> bool:
    """Fix a missing class by generating and writing the class code.

    Args:
        class_name: Name of the class to fix
        class_info: Class information dictionary
        package_path: Full package path
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory
        dry_run: Whether this is a dry run
        merge: Whether to merge with existing code

    Returns:
        True if successful, False otherwise
    """
    from lib import generate_class_code, generate_test_case

    print(f"\n[Fix] Generating missing class: {class_name}")

    # Build package paths
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'
    else:
        relative = package_path.replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'

    # Check requirements to determine expected package structure
    expected_structure = determine_package_structure(requirements_dir, package_path)
    current_structure = detect_current_structure(project_root, package_path)

    # Auto-migrate if structure doesn't match
    if current_structure == 'hybrid':
        print(f"  ⚠️  Hybrid structure detected (both file and directory exist)")
        print(f"     Expected: {expected_structure} based on requirements")
        # Choose the correct migration based on expected structure
        if expected_structure == 'directory':
            # Keep directory, remove file
            print(f"  [Migrate] Will keep directory, remove file")
            file_to_remove = package_file
            if not dry_run:
                file_to_remove.unlink()
                print(f"  ✓ Removed file: {file_to_remove.relative_to(project_root)}")
        else:
            # Keep file, remove directory
            print(f"  [Migrate] Will keep file, remove directory")
            dir_to_remove = package_dir
            if not dry_run:
                import shutil
                shutil.rmtree(dir_to_remove)
                print(f"  ✓ Removed directory: {dir_to_remove.relative_to(project_root)}")

    elif expected_structure == 'directory' and current_structure == 'file':
        print(f"  ⚠️  Structure mismatch: should be directory but is file")
        if not dry_run:
            if not migrate_file_to_directory(package_file, package_path, project_root, requirements_dir):
                print(f"  ✗ Migration failed")
                return False
    elif expected_structure == 'file' and current_structure == 'directory':
        print(f"  ⚠️  Structure mismatch: should be file but is directory")
        if not dry_run:
            if not migrate_directory_to_file(package_dir, package_path, project_root):
                print(f"  ✗ Migration failed")
                return False
    else:
        # Structure matches or nothing exists yet
        if expected_structure == 'directory':
            # Ensure directory exists
            if not package_dir.exists():
                print(f"  ℹ️  Creating package directory: {package_dir.relative_to(project_root)}")
                if not dry_run:
                    package_dir.mkdir(parents=True, exist_ok=True)

            # Check for __init__.py
            init_file = package_dir / '__init__.py'
            if not init_file.exists() and not dry_run:
                print(f"  ✓ Creating __init__.py to make it a proper package")
                with open(init_file, 'w', encoding='utf-8') as f:
                    f.write('')
        else:
            # Ensure parent directory exists
            if not package_dir.parent.exists():
                if not dry_run:
                    package_dir.parent.mkdir(parents=True, exist_ok=True)

    module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}'
    class_file = package_dir / f'{class_name}.py'

    if not class_file.exists():
        package_dir.mkdir(parents=True, exist_ok=True)

    try:
        code = generate_class_code(class_info, package_path, project_root, requirements_dir)
    except Exception as e:
        print(f"  ✗ Error generating code: {e}")
        return False

    # Validate generated code before writing
    is_valid, errors = validate_code(code, class_name)
    if not is_valid:
        print("  ✗ Validation failed:")
        for error in errors:
            print(f"    {error}")
        return False

    # Check if file exists and handle merge mode
    if class_file.exists() and merge:
        print("  [Merge] Existing class found, merging...")
        existing_info = parse_existing_class(class_file)
        merged_code, changes = merge_class_with_existing(code, existing_info, class_name)

        if changes:
            print("  [Merge] Changes made:")
            for change in changes:
                print(f"    - {change}")
        else:
            print("  [Merge] No changes needed - class is up to date")
            return True

        # Create backup
        backup_file = class_file.with_suffix('.py.backup')
        if not dry_run:
            import shutil
            shutil.copy2(class_file, backup_file)
            print(f"  [Merge] Backup created: {backup_file.relative_to(project_root)}")

        code = merged_code

    if dry_run:
        if class_file.exists() and merge:
            print(f"  [Dry Run] Would merge changes into: {class_file.relative_to(project_root)}")
        else:
            print(f"  [Dry Run] Would create file: {class_file.relative_to(project_root)}")
        print("  [Dry Run] Class code preview:")
        print("  " + "\n  ".join(code.split('\n')[:10]))
        if len(code.split('\n')) > 10:
            print("  ...")
        return True

    try:
        class_file.parent.mkdir(parents=True, exist_ok=True)
        with open(class_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')

        # Auto-format with ruff
        if not dry_run:
            format_code_with_ruff(class_file)

        if merge and class_file.exists():
            print(f"  ✓ Merged: {class_file.relative_to(project_root)}")
        else:
            print(f"  ✓ Created: {class_file.relative_to(project_root)}")

        # Update or create __init__.py with wildcard import
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            # First, remove inline class definition if it exists
            remove_inline_class_from_init(parent_init, class_name)

            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()

            if f'from .{class_name} import *' not in init_content:
                # Ensure file ends with newline before appending
                if init_content and not init_content.endswith('\n'):
                    with open(parent_init, 'a', encoding='utf-8') as f:
                        f.write('\n')
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'from .{class_name} import *\n')
                print(f"  ✓ Updated: {parent_init.relative_to(project_root)}")
        else:
            # Create __init__.py with wildcard import
            with open(parent_init, 'w', encoding='utf-8') as f:
                f.write(f'from .{class_name} import *\n')
            print(f"  ✓ Created: {parent_init.relative_to(project_root)}")

        # Generate test
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{class_name}.py'

        test_code = generate_test_case(class_name, class_info, package_path, module_path, requirements_dir, project_root)

        if dry_run:
            print(f"  [Dry Run] Would create test file: {test_file.relative_to(project_root)}")
        else:
            test_dir.mkdir(parents=True, exist_ok=True)
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_code + '\n')
            print(f"  ✓ Created test: {test_file.relative_to(project_root)}")

            test_parent_init = test_dir / '__init__.py'
            if not test_parent_init.exists():
                with open(test_parent_init, 'w', encoding='utf-8') as f:
                    f.write('')

        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Main entry point."""
    args = parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    requirements_dir = project_root / 'docs' / 'requirements'

    # Reset report for this run
    reset_generation_report()

    print("=" * 60)
    print("Package Implementation Fix Script")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Requirements directory: {requirements_dir}")
    print(f"Package filter: {args.package}")
    print()

    # Set global dry_run flag
    global dry_run_mode
    dry_run_mode = args.dry_run

    print("Loading requirements...")
    try:
        packages = get_all_packages(requirements_dir, args.package)
        if not packages:
            print("Error: No packages found")
            print(f"  Package '{args.package}' not found in requirements")
            return 1
        print(f"  Found {len(packages)} package(s) to process")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    # Build type index
    build_type_index(project_root)

    print("\nFinding missing classes...")
    comparisons = []

    for pkg in packages:
        pkg_name = pkg['name']
        required_classes = pkg['classes']

        classes = []
        for cls_name, cls_info in required_classes.items():
            class_file = None
            if pkg_name.startswith('M2::'):
                relative = pkg_name[4:].replace('::', '/')
                package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
                class_file = package_dir / f'{cls_name}.py'

            if class_file and class_file.exists():
                status = '✅ Implemented'
                implemented = True
                location = str(class_file.relative_to(project_root))
                notes = "Line 1"
            else:
                status = '❌ Missing'
                implemented = False
                location = '-'
                notes = 'Not found in implementation'

            classes.append({
                'name': cls_name,
                'status': status,
                'required': True,
                'implemented': implemented,
                'location': location,
                'notes': notes
            })

        comparisons.append({
            'package': pkg_name,
            'classes': classes,
            'required_classes_data': required_classes
        })

    missing_count = sum(1 for comp in comparisons for cls in comp['classes'] if cls['status'] == '❌ Missing')

    if args.merge:
        print(f"  Merge mode: Will process {len([cls for comp in comparisons for cls in comp['classes']])} class(es)")
    elif missing_count == 0:
        print("  No missing classes found!")
        return 0
    else:
        print(f"  Found {missing_count} missing class(es)")

    print("\n" + "=" * 60)
    print("Applying Fixes")
    print("=" * 60)

    if args.merge:
        print("[MERGE MODE - Will merge into existing classes]")
    if args.dry_run:
        print("[DRY RUN MODE - No files will be modified]")

    stats = {'classes_fixed': 0, 'errors': 0}

    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']
        required_classes_data = comp.get('required_classes_data', {})

        print(f"\nPackage: {pkg_name}")

        for cls in classes:
            should_process = (cls['status'] == '❌ Missing') or args.merge

            if should_process:
                class_info = required_classes_data.get(cls['name'], {})
                if class_info:
                    if fix_missing_class(
                        cls['name'], class_info, pkg_name,
                        project_root, requirements_dir,
                        args.dry_run, args.merge
                    ):
                        stats['classes_fixed'] += 1
                    else:
                        stats['errors'] += 1
                else:
                    print(f"  ✗ Warning: No class info found for {cls['name']}")
                    stats['errors'] += 1

    print("\n" + "=" * 60)
    print("Fix Summary")
    print("=" * 60)
    print(f"Classes fixed: {stats['classes_fixed']}")
    print(f"Errors: {stats['errors']}")

    # Print generation report
    report = get_generation_report()
    print_generation_report(
        report.get('unresolved_types', {}),
        report.get('errors', []),
        report.get('warnings', [])
    )

    if args.dry_run:
        print("\n[DRY RUN COMPLETE - No files were modified]")
        return 0

    if stats['classes_fixed'] > 0:
        test_stats = run_tests(comparisons, project_root, args.dry_run)

        print("\n" + "=" * 60)
        print("Test Summary")
        print("=" * 60)
        print(f"Test files run: {test_stats['tests_run']}")
        print(f"Tests passed: {test_stats['tests_passed']}")
        print(f"Tests failed: {test_stats['tests_failed']}")

        # Run flake8 check
        print("\n" + "=" * 60)
        print("Flake8 Check")
        print("=" * 60)

        generated_files = []
        for comp in comparisons:
            pkg_name = comp['package']
            for cls in comp['classes']:
                if cls['status'] == '❌ Missing':
                    if pkg_name.startswith('M2::'):
                        relative = pkg_name[4:].replace('::', '/')
                        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
                        class_file = package_dir / f'{cls["name"]}.py'
                        if class_file.exists():
                            generated_files.append(str(class_file))

        run_flake8_check(generated_files, project_root)

        if test_stats['tests_failed'] == 0:
            print("\n✅ All fixes applied and tests passed!")
            return 0
        else:
            print(f"\n⚠️ {test_stats['tests_failed']} test(s) failed")
            return 1

    return 0


if __name__ == '__main__':
    exit(main())
