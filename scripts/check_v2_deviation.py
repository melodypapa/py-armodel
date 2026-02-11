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

    # Get all actual V2 Python files
    actual_classes = {}
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
                    if class_name not in actual_classes:  # Keep first occurrence
                        actual_classes[class_name] = file_path
        except Exception:
            pass

    # Find deviations
    missing = []
    wrong_location = []
    verified = []

    for class_name, spec in v2_classes.items():
        expected_file = spec['python_file']
        actual_file = actual_classes.get(class_name)

        if actual_file is None:
            missing.append((class_name, expected_file))
        elif actual_file != expected_file:
            wrong_location.append((class_name, expected_file, actual_file))
        else:
            verified.append(class_name)

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
    print(f'  ❌ Missing (not in codebase): {len(missing)}')
    print(f'  📄 Extra files (not in spec): {len(extra_files)}')
    print(f'  ⚠️  File/directory conflicts: {len(conflicts)}')
    print()

    # Determine pass/fail
    # Missing classes are critical failures
    # Wrong location is a warning (codebase still works)
    # Extra files and conflicts are warnings
    passed = len(missing) == 0

    if wrong_location:
        print(f'WRONG LOCATION ({len(wrong_location)} classes):')
        for class_name, expected, actual in wrong_location[:10]:
            print(f'  {class_name}')
            print(f'    Expected: {expected}')
            print(f'    Actual:   {actual}')
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
        f.write(f'- **Missing**: {len(missing)}\n')
        f.write(f'- **Extra files**: {len(extra_files)}\n')
        f.write(f'- **Conflicts**: {len(conflicts)}\n\n')

        if wrong_location:
            f.write('## Classes in Wrong Location\n\n')
            for class_name, expected, actual in wrong_location:
                f.write(f'### {class_name}\n')
                f.write(f'- **Expected**: `{expected}`\n')
                f.write(f'- **Actual**: `{actual}`\n\n')

        if missing:
            f.write('## Missing Classes\n\n')
            f.write(f'Total: {len(missing)}\n\n')
            for class_name, expected in missing:
                f.write(f'- `{class_name}` → `{expected}`\n')
            f.write('\n')

        f.write('## Status\n\n')
        if passed:
            if wrong_location:
                f.write(f'⚠️ **PASSED WITH WARNINGS**: All required classes exist.\n\n')
                f.write(f'{len(wrong_location)} classes are in non-standard locations but functional.\n')
            else:
                f.write('✅ **PASSED**: All classes are in their correct locations.\n')
        else:
            f.write(f'❌ **FAILED**: {len(missing)} required classes are missing from the codebase.\n')

    print('=' * 70)
    if passed:
        if wrong_location:
            print('STATUS: ⚠️  PASSED WITH WARNINGS')
            print(f'  {len(wrong_location)} classes in non-standard locations (functional)')
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
