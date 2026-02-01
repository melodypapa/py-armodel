# Package Structure Migration Design

**Date**: 2026-02-01
**Status**: Draft
**Author**: Claude Code

## Overview

This document describes the design for automatically migrating between single-file and directory package structures in the py-armodel codebase. The `fix-package-implementation.py` script will detect when a package's structure doesn't match the AUTOSAR requirements and automatically migrate it to the correct structure.

## Problem Statement

The py-armodel codebase has an inconsistent package structure:
- Some packages use single `.py` files (e.g., `ECUCDescriptionTemplate.py`)
- Other packages use directories with `__init__.py` (e.g., `BswModuleTemplate/BswOverview/`)
- Some packages have hybrid structures (both file AND directory exist)

This inconsistency causes confusion and makes the codebase harder to maintain.

## Solution: Automatic Migration

The script will automatically detect and fix structure mismatches based on AUTOSAR requirements JSON.

### Decision Rule

**Use a DIRECTORY when:**
- Package has subpackages (based on requirements JSON)
- Package has both classes file AND subpackages

**Use a SINGLE FILE when:**
- Package has only classes, no subpackages (leaf package)

### Implementation Approach

#### 1. Detection

Load the package JSON from `docs/requirements/packages/M2_<PackagePath>.json`:

```python
{
  "subpackages": [...],  # Check if non-empty
  "files": {
    "classes": "packages/..."  # Check if exists
  }
}
```

**Logic:**
- `subpackages.length > 0` → Directory structure
- `subpackages.length == 0` → Single file structure

#### 2. Migration Scenarios

**Scenario A: File → Directory (Split)**

When requirements say "directory" but `.py` file exists:

1. Parse the `.py` file using Python's `ast` module
2. Extract all imports and class definitions
3. Create directory with `__init__.py`
4. For each class:
   - Create `<ClassName>.py` in the directory
   - Write imports + class definition
   - Add `from .<ClassName> import *` to `__init__.py`
5. Delete the original `.py` file
6. Create `.backup` before starting

**Scenario B: Directory → File (Merge)**

When requirements say "file" but directory exists:

1. Scan directory for all `.py` files (except `__init__.py`)
2. Parse each file to extract classes
3. Collect unique imports across all files
4. Create merged `.py` file with:
   - Consolidated imports at top
   - All class definitions concatenated
   - Proper spacing between classes
5. Delete the directory after successful merge
6. Create `.backup` before starting

#### 3. Safety Measures

**Backup Strategy:**
- Create `<file>.backup` or `<dir>.backup/` before migration
- Use atomic operations (write to temp file, then rename)
- Keep backups until script completes successfully

**Error Handling:**
```python
try:
    create_backup(file_path)
    migrate_file_to_directory(file_path)
    validate_migration(file_path)
except Exception as e:
    restore_from_backup(file_path)
    print(f"✗ Migration failed: {e}")
    print(f"  Rolled back using backup")
```

**Validation Steps:**
1. Parse generated files with `ast.parse()` for valid Python syntax
2. Verify all expected class files exist
3. Verify `__init__.py` exists and is valid
4. Run import test: `python -c "from package import Class"`

#### 4. Integration with fix-package-implementation.py

**Updated workflow:**

1. Load requirements → Get package list with expected structure
2. For each package:
   - Determine expected structure (file vs directory) from JSON
   - Check current filesystem state
   - If mismatch detected:
     - Create backup
     - Run migration (file↔directory)
     - Verify migration success
   - After structure matches:
     - Find missing classes
     - Generate individual class files
     - Generate/update `__init__.py` with wildcard imports
     - Generate tests

**New helper functions:**
- `determine_package_structure(requirements_dir, package_path)` → Returns `'file'` or `'directory'`
- `migrate_file_to_directory(file_path, package_path)` → Splits file into directory
- `migrate_directory_to_file(dir_path, output_file)` → Merges directory into file
- `detect_current_structure(path)` → Returns `'file'`, `'directory'`, or `'none'`

#### 5. Edge Cases

**Circular Dependencies:**
- Handle relative imports correctly when splitting files
- Ensure both classes exist before validating

**Non-standard Class Locations:**
- Detect classes defined in `__init__.py` instead of separate files
- Scan `__init__.py` for class definitions

**Duplicate Class Names:**
- Warn user and skip migration if same class name in multiple files
- Requires manual resolution

**Complex Imports:**
- Preserve import structure (`from . import X` vs `from ..package import X`)
- Keep relative imports intact when moving classes

**Docstrings and Comments:**
- Extract docstrings from AST nodes
- Preserve module-level comments in `__init__.py`

**Type Annotations:**
- Forward references like `"ClassName"` remain valid when moved to separate files
- No special handling needed

**Empty Directories:**
- Directory with only `__init__.py` (no classes)
- Convert to single `.py` file with just imports if needed

**Enumeration Classes:**
- Treat same as regular classes (already handled by AST parser)

## Related Files

- `scripts/fix-package-implementation.py` - Main script to implement
- `scripts/compare-package-implementation.py` - Already has detection logic (lines 459-489)
- `scripts/lib/code_generator.py` - Code generation logic
- `scripts/lib/test_generator.py` - Test generation logic

## Next Steps

1. Implement migration functions in `fix-package-implementation.py`
2. Add validation and rollback mechanisms
3. Test migration on sample packages
4. Update documentation

## References

- `docs/requirements/` - AUTOSAR requirements JSON files
- `reports/package_comparison.md` - Current structure comparison report
- `CLAUDE.md` - Project documentation
