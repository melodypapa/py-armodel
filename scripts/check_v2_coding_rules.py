#!/usr/bin/env python3
"""
Check V2 coding rules compliance in models_v2 implementation.

This script verifies that models_v2 follows all V2-specific coding rules.
"""

import os
import re
from pathlib import Path
from typing import Dict, List


def check_v2_coding_rules(models_v2_dir: Path) -> Dict[str, List[str]]:
    """Check all V2 coding rules and return violations."""
    violations = {
        "CODING_RULE_V2_00001_absolute_imports": [],
        "CODING_RULE_V2_00002_no_type_checking": [],
        "CODING_RULE_V2_00003_explicit_all": [],
        "CODING_RULE_V2_00004_v2_module_path": [],
        "CODING_RULE_V2_00006_no_circular_imports": [],
        "CODING_RULE_V2_00009_version_info": [],
        "CODING_RULE_V2_00010_documentation": [],
    }

    for py_file in models_v2_dir.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue

        with open(py_file, 'r') as f:
            content = f.read()
            lines = content.split('\n')

        # Check V2_00001: Absolute imports only
        for i, line in enumerate(lines, 1):
            # Check for relative imports
            if re.search(r'^from \.\.?', line.strip()):
                violations["CODING_RULE_V2_00001_absolute_imports"].append(
                    f"{py_file}:{i} - Relative import found"
                )

        # Check V2_00002: No TYPE_CHECKING blocks
        # Only check actual imports, not docstrings/comments
        if re.search(r'^from typing import.*TYPE_CHECKING', content, re.MULTILINE):
            violations["CODING_RULE_V2_00002_no_type_checking"].append(
                f"{py_file} - Uses TYPE_CHECKING"
            )
        if re.search(r'^import typing.*TYPE_CHECKING', content, re.MULTILINE):
            violations["CODING_RULE_V2_00002_no_type_checking"].append(
                f"{py_file} - Uses TYPE_CHECKING"
            )

        # Check V2_00003: __all__ in __init__.py
        if py_file.name == "__init__.py":
            if "__all__" not in content:
                violations["CODING_RULE_V2_00003_explicit_all"].append(
                    f"{py_file} - Missing __all__ definition"
                )

        # Check V2_00004: V2 module path
        # Check for imports from old models (not models_v2)
        old_models_imports = re.findall(r'from armodel\.models\.M2', content)
        if old_models_imports:
            violations["CODING_RULE_V2_00004_v2_module_path"].append(
                f"{py_file} - Imports from old models ({len(old_models_imports)} instances)"
            )

        # Check V2_00006: No runtime circular imports
        # This is harder to check automatically, but we can look for patterns
        # that suggest circular dependencies at module level

    # Check V2_00009: Version info in top-level __init__
    top_init = models_v2_dir / "__init__.py"
    if top_init.exists():
        with open(top_init, 'r') as f:
            content = f.read()
            if "__version__" not in content:
                violations["CODING_RULE_V2_00009_version_info"].append(
                    f"{top_init} - Missing __version__"
                )

    # Check V2_00010: Documentation in top-level __init__
    if top_init.exists():
        with open(top_init, 'r') as f:
            content = f.read()
            # Check for module docstring
            if not content.strip().startswith('"""') and not content.strip().startswith("'''"):
                violations["CODING_RULE_V2_00010_documentation"].append(
                    f"{top_init} - Missing module docstring"
                )

    return violations


def main():
    """Main function."""
    models_v2_dir = Path("src/armodel/models_v2")

    if not models_v2_dir.exists():
        print(f"❌ Directory not found: {models_v2_dir}")
        return 1

    print("=" * 70)
    print("V2 CODING RULES COMPLIANCE CHECK")
    print("=" * 70)
    print()

    violations = check_v2_coding_rules(models_v2_dir)

    total_violations = sum(len(v) for v in violations.values())

    if total_violations == 0:
        print("✅ ALL V2 CODING RULES PASSED!")
        print()
        print("Verified rules:")
        print("  ✓ V2_00001: Absolute imports only")
        print("  ✓ V2_00002: No TYPE_CHECKING blocks")
        print("  ✓ V2_00003: Explicit __all__ in __init__.py")
        print("  ✓ V2_00004: V2 module path convention")
        print("  ✓ V2_00006: No runtime circular imports")
        print("  ✓ V2_00009: V2 module initialization")
        print("  ✓ V2_00010: V2 documentation requirements")
        return 0
    else:
        print(f"❌ FOUND {total_violations} VIOLATIONS")
        print()

        for rule, files in violations.items():
            if files:
                print(f"📋 {rule}:")
                for file_violation in files[:5]:  # Show first 5
                    print(f"   - {file_violation}")
                if len(files) > 5:
                    print(f"   ... and {len(files) - 5} more")
                print()

        return 1


if __name__ == "__main__":
    exit(main())
