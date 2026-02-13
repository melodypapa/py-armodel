#!/usr/bin/env python3
"""
Script to fix V2 model syntax errors.

This script fixes two types of syntax errors in V2 model files:
1. Malformed import statements: Multiple block imports concatenated with ')from'
2. Orphaned import items: Items like 'FibexElement,' without proper 'from' statement

Usage:
    python scripts/fix_v2_syntax_errors.py --dry-run      # Preview changes
    python scripts/fix_v2_syntax_errors.py                # Apply fixes
    python scripts/fix_v2_syntax_errors.py --verify       # Verify no syntax errors
"""

import argparse
import ast
import re
import sys
from pathlib import Path


# Orphaned imports and their correct import paths
ORPHANED_IMPORTS = {
    'FibexElement': 'from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement',
    'PredefinedChapter': 'from armodel.v2.models.M2.MSR.Documentation.Chapters import PredefinedChapter',
}


def fix_malformed_imports(content: str, filepath: str) -> tuple[str, list[str]]:
    """
    Fix malformed import statements where multiple block imports are concatenated with ')from'.

    The pattern is:
        from X import (A, B,)from Y import (C,)from Z import (D,)

    Should become:
        from X import (A, B,)
        from Y import (C,)
        from Z import (D,)
    """
    changes = []

    # Find lines with ')from' pattern
    lines = content.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        # Check if this line has the malformed pattern
        if ')from' in line:
            # Split the line by ')from'
            parts = line.split(')from')

            if len(parts) > 1:
                # Get the indentation from the original line
                indent_match = re.match(r'^(\s*)', line)
                indent = indent_match.group(1) if indent_match else ''

                # Process each part
                for j, part in enumerate(parts):
                    if j == 0:
                        # First part ends with ')', keep it as is
                        fixed_lines.append(part + ')')
                    else:
                        # Subsequent parts start with the import statement
                        # Add 'from' at the beginning with proper indentation
                        fixed_lines.append(indent + 'from' + part)

                changes.append(f"Split line {i+1} into {len(parts)} import statement(s)")
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines), changes


def fix_orphaned_imports(content: str, filepath: str) -> tuple[str, list[str]]:
    """
    Fix orphaned import items by adding proper 'from' statements.

    Args:
        content: File content
        filepath: Path to the file being fixed

    Returns:
        Tuple of (fixed content, list of changes made)
    """
    changes = []
    lines = content.split('\n')
    fixed_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for orphaned import items (indented item names followed by comma)
        for orphaned_name, import_statement in ORPHANED_IMPORTS.items():
            if orphaned_name in line and 'from' not in line:
                # Check if this line is just the orphaned item
                if re.match(r'^\s*' + re.escape(orphaned_name) + r',?\s*$', line.strip()):
                    # Find the indentation
                    indent_match = re.match(r'^(\s*)', line)
                    indent = indent_match.group(1) if indent_match else ''

                    # Insert the import statement before the orphaned line
                    fixed_lines.append(import_statement)
                    changes.append(f"Added import for {orphaned_name}")

        fixed_lines.append(line)
        i += 1

    return '\n'.join(fixed_lines), changes


def verify_syntax(root_dir: str) -> tuple[bool, list[str]]:
    """
    Verify all Python files in the V2 models directory can be parsed.

    Args:
        root_dir: Root directory to check

    Returns:
        Tuple of (all_valid, list of error messages)
    """
    errors = []
    v2_models_dir = Path(root_dir) / 'src' / 'armodel' / 'v2' / 'models'

    if not v2_models_dir.exists():
        errors.append(f"V2 models directory not found: {v2_models_dir}")
        return False, errors

    for filepath in v2_models_dir.rglob('*.py'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content, str(filepath))
        except SyntaxError as e:
            errors.append(f"{filepath}:{e.lineno}: {e.msg}")

    all_valid = len(errors) == 0
    return all_valid, errors


def main():
    parser = argparse.ArgumentParser(
        description='Fix V2 model syntax errors'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without applying them'
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Verify no syntax errors in V2 models'
    )
    args = parser.parse_args()

    root_dir = Path(__file__).parent.parent

    # Verify mode
    if args.verify:
        all_valid, errors = verify_syntax(root_dir)
        if all_valid:
            print("✓ All V2 model files have valid syntax")
            return 0
        else:
            print(f"✗ Found {len(errors)} syntax error(s):")
            for error in errors[:50]:  # Limit to 50 errors
                print(f"  {error}")
            if len(errors) > 50:
                print(f"  ... and {len(errors) - 50} more")
            return 1

    # Fix mode
    v2_models_dir = root_dir / 'src' / 'armodel' / 'v2' / 'models'
    total_changes = 0
    files_changed = 0

    for filepath in v2_models_dir.rglob('*.py'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fixed_content = content
        all_changes = []

        # Fix malformed imports
        fixed_content, changes = fix_malformed_imports(fixed_content, str(filepath))
        all_changes.extend(changes)

        # Fix orphaned imports
        fixed_content, changes = fix_orphaned_imports(fixed_content, str(filepath))
        all_changes.extend(changes)

        # Only write if changes were made
        if fixed_content != content:
            files_changed += 1
            total_changes += len(all_changes)
            if args.dry_run:
                print(f"\n{filepath}:")
                for change in all_changes:
                    print(f"  - {change}")
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"Fixed {filepath} ({len(all_changes)} change(s))")

    if args.dry_run:
        print(f"\nDry run: {total_changes} change(s) across {files_changed} file(s)")
    else:
        print(f"\nApplied {total_changes} change(s) across {files_changed} file(s)")

    # Verify after fixes
    if not args.dry_run:
        print("\nVerifying syntax after fixes...")
        all_valid, errors = verify_syntax(root_dir)
        if all_valid:
            print("✓ All V2 model files have valid syntax")
        else:
            print(f"✗ Still found {len(errors)} syntax error(s):")
            for error in errors[:50]:  # Limit to 50 errors
                print(f"  {error}")
            if len(errors) > 50:
                print(f"  ... and {len(errors) - 50} more")
            return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())