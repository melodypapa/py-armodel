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

        # Update __init__.py
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()
            if f'from .{type_name} import {type_name}' not in init_content:
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'\nfrom .{type_name} import {type_name}\n')

        # Generate test case
        module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}.{type_name}'
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{type_name}.py'

        test_code = generate_test_case(type_name, class_info, package_path, module_path, requirements_dir)

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
        print(f"  ✗ Error: Package is a single file ({package_file.name})")
        print(f"     Class '{class_name}' should be added to {package_file.relative_to(project_root)}")
        print("     This requires manual implementation or script enhancement.")
        return False

    module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}.{class_name}'
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

        # Update __init__.py
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()

            if f'from .{class_name} import {class_name}' not in init_content:
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'\nfrom .{class_name} import {class_name}\n')
                print(f"  ✓ Updated: {parent_init.relative_to(project_root)}")

        # Generate test
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{class_name}.py'

        test_code = generate_test_case(class_name, class_info, package_path, module_path, requirements_dir)

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
