#!/usr/bin/env python3
"""
Check deviation between V2 models and class-package.json specification.

This script verifies that V2 model classes are in the correct Python files
as specified in docs/requirements/class-package.json.
"""

import ast
import json
from pathlib import Path


def main():
    # Load specification
    spec_path = Path('docs/requirements/class-package.json')
    if not spec_path.exists():
        print(f"ERROR: Specification file not found: {spec_path}")
        return 1

    with open(spec_path, 'r') as f:
        classes = json.load(f)['types']

    # Filter for V2 classes only
    v2_classes = {c['name']: c for c in classes if c['python_file'].startswith('src/armodel/v2/models')}

    # Get all actual V2 Python files and track ALL occurrences of each class
    actual_classes_all = {}  # class_name -> list of files
    for py_file in Path('src/armodel/v2/models').rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue

        try:
            with open(py_file, 'r') as f:
                tree = ast.parse(f.read(), filename=str(py_file))

            file_path = str(py_file)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    if class_name not in actual_classes_all:
                        actual_classes_all[class_name] = []
                    actual_classes_all[class_name].append(file_path)
        except Exception:
            pass

    # Find deviations
    missing = []
    wrong_location = []
    duplicates = []  # New: track duplicate definitions
    verified = []

    for class_name, spec in v2_classes.items():
        expected_file = spec['python_file']
        actual_files = actual_classes_all.get(class_name, [])

        if len(actual_files) == 0:
            # Class not found anywhere
            missing.append((class_name, expected_file))
        elif len(actual_files) == 1:
            # Class found in exactly one file
            actual_file = actual_files[0]
            if actual_file != expected_file:
                wrong_location.append((class_name, expected_file, actual_file, None))
            else:
                verified.append(class_name)
        else:
            # Class found in multiple files (duplicates)
            # Check if one matches the expected location
            correct_file = None
            wrong_files = []
            for f in actual_files:
                if f == expected_file:
                    correct_file = f
                else:
                    wrong_files.append(f)

            if correct_file:
                # Found in correct location + duplicates elsewhere
                verified.append(class_name)
                for wrong_file in wrong_files:
                    duplicates.append((class_name, expected_file, correct_file, wrong_file))
            else:
                # Not found in correct location, but found in multiple wrong locations
                # Report first as wrong location, others as duplicates
                first_file = actual_files[0]
                wrong_location.append((class_name, expected_file, first_file, actual_files[1:]))
                for other_file in actual_files[1:]:
                    duplicates.append((class_name, expected_file, first_file, other_file))

    # Find extra files (files that exist but not in spec)
    actual_v2_files = set(str(p) for p in Path('src/armodel/v2/models').rglob('*.py')
                          if '__pycache__' not in str(p))
    expected_v2_files = set(c['python_file'] for c in v2_classes.values())
    extra_files = actual_v2_files - expected_v2_files

    # Find file/directory conflicts
    conflicts = []
    for f in actual_v2_files:
        if f.endswith('.py'):
            file_dir = f[:-3]
            if Path(file_dir).is_dir():
                conflicts.append(f)

    # Print report
    print('=' * 70)
    print('V2 MODELS vs class-package.json VALIDATION')
    print('=' * 70)
    print()
    print(f'Total V2 classes in specification: {len(v2_classes)}')
    print()

    # Summary table
    print('SUMMARY:')
    print(f'  ✅ Verified in correct location: {len(verified)} ({len(verified)*100//len(v2_classes)}%)')
    print(f'  ⚠️  Wrong location: {len(wrong_location)}')
    print(f'  📋 Duplicate definitions: {len(duplicates)}')
    print(f'  ❌ Missing (not in codebase): {len(missing)}')
    print(f'  📄 Extra files (not in spec): {len(extra_files)}')
    print(f'  ⚠️  File/directory conflicts: {len(conflicts)}')
    print()

    # Determine pass/fail
    # Missing classes are critical failures
    # Wrong location and duplicates are warnings (codebase still works)
    # Extra files and conflicts are warnings
    passed = len(missing) == 0

    if duplicates:
        print(f'DUPLICATE DEFINITIONS ({len(duplicates)} instances):')
        for class_name, expected, correct, duplicate in duplicates[:15]:
            print(f'  {class_name}')
            print(f'    Expected:  {expected}')
            print(f'    Correct:   {correct}')
            print(f'    Duplicate: {duplicate}')
        if len(duplicates) > 15:
            print(f'  ... and {len(duplicates) - 15} more duplicates')
        print()

    if wrong_location:
        print(f'WRONG LOCATION ({len(wrong_location)} classes):')
        for item in wrong_location[:10]:
            class_name, expected, actual, other_files = item
            print(f'  {class_name}')
            print(f'    Expected: {expected}')
            print(f'    Actual:   {actual}')
            if other_files:
                print(f'    Also in:  {", ".join(other_files)}')
        if len(wrong_location) > 10:
            print(f'  ... and {len(wrong_location) - 10} more')
        print()

    if missing and len(missing) <= 50:
        print(f'MISSING ({len(missing)} classes):')
        for class_name, expected in missing[:20]:
            print(f'  {class_name}')
            print(f'    Expected in: {expected}')
        if len(missing) > 20:
            print(f'  ... and {len(missing) - 20} more')
        print()
    elif missing:
        print(f'MISSING: {len(missing)} classes (use --verbose for details)')
        print()

    if extra_files:
        print(f'EXTRA FILES: {len(extra_files)} files not in specification (warnings only)')
        print()

    if conflicts:
        print(f'FILE/DIRECTORY CONFLICTS: {len(conflicts)} (violates CODING_RULE_STYLE_00008)')
        print()

    # Save report
    report_path = Path('reports/v2_validation_report.md')
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, 'w') as f:
        f.write('# V2 Models Validation Report\n\n')
        f.write('## Summary\n\n')
        f.write(f'- **Total V2 classes**: {len(v2_classes)}\n')
        f.write(f'- **Verified**: {len(verified)} ({len(verified)*100//len(v2_classes)}%)\n')
        f.write(f'- **Wrong location**: {len(wrong_location)}\n')
        f.write(f'- **Duplicate definitions**: {len(duplicates)}\n')
        f.write(f'- **Missing**: {len(missing)}\n')
        f.write(f'- **Extra files**: {len(extra_files)}\n')
        f.write(f'- **Conflicts**: {len(conflicts)}\n\n')

        if duplicates:
            f.write('## Duplicate Definitions\n\n')
            f.write(f'Total: {len(duplicates)} instances\n\n')
            for class_name, expected, correct, duplicate in duplicates:
                f.write(f'### {class_name}\n')
                f.write(f'- **Expected**: `{expected}`\n')
                f.write(f'- **Correct location**: `{correct}`\n')
                f.write(f'- **Duplicate in**: `{duplicate}`\n\n')

        if wrong_location:
            f.write('## Classes in Wrong Location\n\n')
            for item in wrong_location:
                class_name, expected, actual, other_files = item
                f.write(f'### {class_name}\n')
                f.write(f'- **Expected**: `{expected}`\n')
                f.write(f'- **Actual**: `{actual}`\n')
                if other_files:
                    f.write(f'- **Also defined in**: `{", ".join(other_files)}`\n')
                f.write('\n')

        if missing:
            f.write('## Missing Classes\n\n')
            f.write(f'Total: {len(missing)}\n\n')
            for class_name, expected in missing:
                f.write(f'- `{class_name}` → `{expected}`\n')
            f.write('\n')

        f.write('## Status\n\n')
        if passed:
            if wrong_location or duplicates:
                f.write(f'⚠️ **PASSED WITH WARNINGS**: All required classes exist.\n\n')
                if wrong_location:
                    f.write(f'{len(wrong_location)} classes are in non-standard locations.\n')
                if duplicates:
                    f.write(f'{len(duplicates)} duplicate class definitions found.\n')
            else:
                f.write('✅ **PASSED**: All classes are in their correct locations.\n')
        else:
            f.write(f'❌ **FAILED**: {len(missing)} required classes are missing from the codebase.\n')

    print('=' * 70)
    if passed:
        if wrong_location or duplicates:
            print('STATUS: ⚠️  PASSED WITH WARNINGS')
            if wrong_location:
                print(f'  {len(wrong_location)} classes in non-standard locations')
            if duplicates:
                print(f'  {len(duplicates)} duplicate definitions found')
        else:
            print('STATUS: ✅ PASSED')
    else:
        print('STATUS: ❌ FAILED')
        print(f'  {len(missing)} required classes missing')
    print('=' * 70)
    print()
    print(f'Report saved to: {report_path}')

    return 0 if passed else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
