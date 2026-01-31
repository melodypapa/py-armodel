# Test-Driven Package Implementation Generator Design

**Date:** 2025-01-31
**Status:** Design Approved
**Author:** AI (Claude) + User Collaboration

## Overview

This document describes the design for enhancing the `compare-package-implementation.py` script to include test-driven code generation capabilities. The enhanced script will generate structural unit tests, use test results to drive code generation with smart import resolution, and iteratively fix issues until tests pass.

## Problem Statement

The current `compare-package-implementation.py` script can:
- Compare AUTOSAR M2 package requirements with Python implementations
- Generate markdown comparison reports
- Generate basic class stubs via `--fix` flag

**Limitations:**
- Generated code has hardcoded imports that are often incorrect
- No validation that generated code actually works
- Cannot handle complex import paths or wildcard imports
- Missing methods and attributes not detected systematically

## Proposed Solution

Implement a **test-driven code generation loop** that:
1. Generates structural unit tests from requirements
2. Runs tests to identify specific failures
3. Uses test failures to guide intelligent code generation
4. Resolves imports correctly by scanning existing codebase
5. Iterates until tests pass or manual intervention needed

## Architecture

### High-Level Workflow

```
Requirements JSON → Generate Structural Tests → Run Pytest
                                      ↓
                                Parse Failures
                                      ↓
                        Enhanced Fix with Smart Imports
                                      ↓
                          Generate Correct Python Code
                                      ↓
                              Re-run Tests (Verify)
```

### Three Modes of Operation

1. **Compare Mode** (existing - unchanged)
   - Generate markdown comparison report
   - No code generation

2. **Generate Tests Mode** (new)
   - Generate pytest test files from requirements
   - Tests validate class structure (existence, inheritance, methods)
   - Follow existing project test conventions

3. **Smart Fix Mode** (new)
   - Generate tests → run tests → parse failures
   - Generate code with correct imports based on failures
   - Iterate until tests pass
   - Handle import resolution, inheritance, methods

## Components

### 1. ImportResolver Class

**Purpose:** Scan codebase and resolve correct import paths

**Methods:**
- `build_class_map(project_root: Path) -> ImportMap`
  - Recursively scan `src/armodel/models/M2/`
  - Parse each `.py` file with AST
  - Extract class definitions with full module paths
  - Return `{ClassName: (module_path, file_path, line_number)}`

- `resolve_import(class_name: str, target_file: Path) -> str`
  - Look up class in ImportMap
  - Calculate relative import from target_file to class location
  - Return correct import statement

- `get_relative_import(source: Path, target: Path) -> str`
  - Calculate relative path between two files
  - Handle sibling, parent, and cousin directory relationships
  - Return import string (e.g., `from ..CommonStructure import ARObject`)

**Data Structures:**
```python
ImportMap = Dict[str, ClassLocation]

ClassLocation = TypedDict('ClassLocation', {
    'name': str,              # ClassName
    'module': str,            # armodel.models.M2.AUTOSARTemplates.xxx
    'file_path': Path,        # src/armodel/models/M2/...
    'line_number': int,
    'is_exported': bool       # True if in __init__.py wildcard
})
```

### 2. TestGenerator Class

**Purpose:** Generate pytest test files from requirements

**Methods:**
- `generate_test_file(package_info: Dict) -> Path`
  - Create `test_<Package>Structure.py` file
  - Follow existing test directory structure
  - Add imports, test class, and test methods

- `generate_class_tests(class_info: Dict) -> List[str]`
  - Generate test methods for each class
  - Test class exists and can be imported
  - Test class inheritance is correct
  - Test getter/setter methods exist

- `generate_method_tests(class_name: str, methods: List[str]) -> List[str]`
  - For each attribute, generate getter/setter tests
  - Use `hasattr()` to check method existence

**Test Pattern:**
```python
class Test{ClassName}:
    def test_class_exists(self):
        """Test that {ClassName} class can be imported"""
        from armodel.models.M2.{PackagePath} import {ClassName}
        assert {ClassName} is not None

    def test_class_inheritance(self):
        """Test that {ClassName} inherits from {ParentClass}"""
        from armodel.models.M2.{PackagePath} import {ClassName}
        from armodel.models.M2.{ParentPath} import {ParentClass}
        assert issubclass({ClassName}, {ParentClass})

    def test_has_getter_methods(self):
        """Test that {ClassName} has expected getter methods"""
        instance = {ClassName}(parent, "test")
        assert hasattr(instance, 'get{Attr}()')

    def test_has_setter_methods(self):
        """Test that {ClassName} has expected setter methods"""
        instance = {ClassName}(parent, "test")
        assert hasattr(instance, 'set{Attr}()')
```

### 3. TestRunner Class

**Purpose:** Execute pytest and parse results

**Methods:**
- `run_tests(test_files: List[Path]) -> TestResult`
  - Execute pytest programmatically via `pytest.main()`
  - Capture output and exit code
  - Return structured results

- `parse_results(test_output: str) -> List[Failure]`
  - Parse pytest output for failures and errors
  - Extract test names, error types, messages
  - Categorize by failure type

- `categorize_failures(failures: List[Failure]) -> Dict[str, List[Failure]]`
  - Group by: import errors, inheritance errors, method errors
  - Return categorized dictionary

**Data Structures:**
```python
TestResult = TypedDict('TestResult', {
    'passed': int,
    'failed': int,
    'errors': int,
    'duration': float,
    'failures': List[Failure]
})

Failure = TypedDict('Failure', {
    'test_name': str,
    'error_type': str,        # ImportError, AttributeError, AssertionError, etc.
    'message': str,
    'class_name': str,
    'category': str           # import, inheritance, method, attribute
})
```

### 4. EnhancedCodeGenerator Class

**Purpose:** Generate correct Python code with smart imports

**Methods:**
- `generate_class_with_imports(class_info: Dict, resolver: ImportResolver) -> str`
  - Resolve all imports (parent class, attribute types)
  - Generate complete class with __init__, getters, setters
  - Include proper import statements

- `generate_init_method(attributes: Dict, parent_class: str) -> str`
  - Generate `__init__(self, parent: ParentClass, short_name: str)`
  - Call `super().__init__(parent, short_name)`
  - Initialize all attributes with correct types

- `generate_getter_setters(attributes: Dict) -> List[str]`
  - For each attribute, generate getter and setter
  - Follow AUTOSAR naming: `get{Attr}()`, `set{Attr}(value)`
  - Return `self` for method chaining
  - Handle multiplicity: single, Optional, List

**Code Generation Pattern:**
```python
# Imports (resolved by ImportResolver)
from ..CommonStructure import Identifiable
from typing import List, Optional

# Class definition
class {ClassName}({ParentClass}):
    def __init__(self, parent: {ParentClass}, short_name: str):
        super().__init__(parent, short_name)
        self._{attr}: {Type} = {default}

    def get{Attr}(self) -> {Type}:
        return self._{attr}

    def set{Attr}(self, value: {Type}):
        self._{attr} = value
        return self
```

## Import Resolution Strategy

### Building the Class Map

1. Scan `src/armodel/models/M2/` recursively
2. Parse each `.py` file with AST
3. Extract class definitions:
   - Class name
   - Base classes (inheritance)
   - Full module path
   - File path and line number
4. Check if class is exported via `__init__.py` wildcard
5. Store in ImportMap dictionary

### Resolving Imports

Given:
- Target file: `BswModuleTemplate/NewClass.py`
- Parent class: `ARObject` in `GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`

Steps:
1. Find `ARObject` in ImportMap
2. Get its file path
3. Calculate relative path from target to parent
4. Generate import statement:
   - Same directory: `from .ARObject import ARObject`
   - Parent directory: `from ..CommonStructure import ARObject` (if wildcard)
   - Different branch: `from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARObject`

### Handling Wildcard Imports

Check if parent class is exported via package `__init__.py`:
```python
# Check __init__.py for "from .ClassName import *"
if is_exported_via_wildcard(parent_class):
    # Import from package instead of file
    import_stmt = f"from {package_module} import {ClassName}"
else:
    # Import from specific file
    import_stmt = f"from {file_module} import {ClassName}"
```

## Error Handling and Categorization

### Test Failure Categories

1. **ImportError / ModuleNotFoundError**
   - **Cause:** Generated import path is incorrect
   - **Detection:** Test fails at import statement
   - **Fix:** Re-scan codebase, update ImportMap, regenerate import
   - **Retry:** Up to 3 attempts with different import strategies

2. **AttributeError: 'module' has no attribute 'ClassName'**
   - **Cause:** Class not exported from `__init__.py`
   - **Detection:** Import succeeds but class not accessible
   - **Fix:** Add `from .ClassName import *` to package `__init__.py`

3. **TypeError: abstract class instantiation**
   - **Cause:** Generated concrete class for abstract requirement
   - **Detection:** Test fails when instantiating class
   - **Fix:** Add ABC import and TypeError check in `__init__`

4. **AttributeError: 'ClassName' has no attribute 'getX'**
   - **Cause:** Missing getter/setter method
   - **Detection:** `hasattr()` check fails in test
   - **Fix:** Generate missing method(s)

5. **AssertionError: issubclass failed**
   - **Cause:** Wrong parent class in inheritance
   - **Detection:** Inheritance test assertion fails
   - **Fix:** Verify parent class name, update ImportMap lookup

### Safety Features

1. **Backup before modification**
   - Create `.py.bak` files before overwriting
   - Keep backups until verification succeeds

2. **Dry-run mode**
   - Preview all changes without writing files
   - Show what would be generated

3. **Rollback on failure**
   - If all tests fail after fixes, restore from backups
   - Report errors for manual review

4. **Verbose logging**
   - Show each step for debugging
   - Log import resolution decisions
   - Display test output in real-time

## Complete Smart Fix Workflow

### Phase 1: Initial Scan
1. Build ImportMap from existing codebase
2. Compare requirements vs implementation
3. Identify missing classes and methods

### Phase 2: Test Generation
1. Generate `test_<Package>Structure.py` files
2. Tests initially FAIL (classes don't exist yet)

### Phase 3: Code Generation
For each missing class:
1. Resolve parent class location via ImportMap
2. Calculate correct import statements
3. Generate class with `__init__`, getters, setters
4. Write to correct file location
5. Update `__init__.py` if needed

### Phase 4: Test Execution
1. Run pytest on generated tests
2. Parse failures and categorize

### Phase 5: Iterative Fix
For each failure:
1. Determine root cause
2. Fix imports/methods/inheritance
3. Regenerate affected code
4. Re-test
5. Repeat until max iterations or all tests pass

### Phase 6: Final Report
1. Markdown report with test results
2. List of generated files
3. Any remaining issues (manual review needed)

## Command-Line Interface

### New Arguments

```bash
# Generate unit test files only
--generate-tests

# Generate tests and run them (report results)
--run-tests

# Enhanced fix with test-driven generation
--smart-fix

# Iterate on test failures until passing
--iterative

# Custom test output directory
--test-dir PATH

# Max fix iterations (default: 3)
--max-iterations N

# Don't regenerate existing test files
--skip-existing
```

### Usage Examples

```bash
# Compare only (existing behavior)
python scripts/compare-package-implementation.py

# Generate structural tests
python scripts/compare-package-implementation.py --generate-tests

# Generate tests and run them
python scripts/compare-package-implementation.py --run-tests

# Smart fix with test-driven generation
python scripts/compare-package-implementation.py --smart-fix

# Full workflow: tests + smart fix + iterate
python scripts/compare-package-implementation.py --smart-fix --iterative --verbose

# Preview what would be done
python scripts/compare-package-implementation.py --smart-fix --dry-run

# Focus on specific package
python scripts/compare-package-implementation.py \
  --package M2::AUTOSARTemplates::BswModuleTemplate \
  --smart-fix
```

## File Structure

### Generated Test Files

```
tests/test_armodel/models/M2/AUTOSARTemplates/
├── BswModuleTemplate/
│   ├── test_BswBehaviorStructure.py       # NEW: Structural tests
│   ├── test_BswBehavior.py                # EXISTING: Functional tests
│   ├── test_BswImplementationStructure.py # NEW
│   └── test_BswImplementation.py          # EXISTING
├── CommonStructure/
│   ├── test_InternalBehaviorStructure.py  # NEW
│   └── test_InternalBehavior.py           # EXISTING
└── ...
```

### Generated Source Files

```
src/armodel/models/M2/AUTOSARTemplates/
├── BswModuleTemplate/
│   ├── BswBehavior/
│   │   ├── BswModuleEntity.py             # GENERATED
│   │   ├── BswCalledEntity.py             # GENERATED
│   │   └── __init__.py                    # UPDATED (wildcard import)
│   └── __init__.py                         # UPDATED
└── ...
```

## Implementation Phases

### Phase 1: Infrastructure (Foundation)
- Implement ImportResolver class
- Build ImportMap scanning logic
- Implement import resolution algorithm
- Add unit tests for ImportResolver

### Phase 2: Test Generation
- Implement TestGenerator class
- Generate test file structure
- Create test methods for classes and methods
- Follow existing test patterns
- Add unit tests for TestGenerator

### Phase 3: Test Execution
- Implement TestRunner class
- Integrate with pytest API
- Parse test results
- Categorize failures
- Add unit tests for TestRunner

### Phase 4: Enhanced Code Generation
- Implement EnhancedCodeGenerator class
- Integrate with ImportResolver
- Generate correct class definitions
- Generate getter/setter methods
- Update `__init__.py` files
- Add unit tests for EnhancedCodeGenerator

### Phase 5: CLI Integration
- Add new command-line arguments
- Implement mode selection (compare, generate-tests, smart-fix)
- Integrate all components
- Add progress reporting
- Update documentation

### Phase 6: Testing and Validation
- End-to-end testing with real packages
- Validate generated code passes tests
- Performance testing with large codebases
- User acceptance testing

## Success Criteria

1. **Correctness**
   - Generated code has 100% correct imports
   - Generated code passes structural tests
   - No import errors or circular dependencies

2. **Coverage**
   - All missing classes can be generated
   - All inheritance chains are correct
   - All required methods are generated

3. **Usability**
   - Simple CLI interface
   - Clear progress reporting
   - Helpful error messages
   - Works with existing --fix flag

4. **Performance**
   - ImportMap builds in < 5 seconds
   - Test generation takes < 10 seconds
   - Full smart-fix workflow completes in < 60 seconds for typical package

## Risks and Mitigations

### Risk 1: Complex Import Scenarios
**Risk:** Some import patterns may be too complex to resolve automatically
**Mitigation:**
- Provide manual override for imports
- Flag unresolved imports for manual review
- Document edge cases

### Risk 2: Test False Positives
**Risk:** Tests may pass for incorrect implementations
**Mitigation:**
- Structural tests are minimal (existence, inheritance, methods)
- Functional tests still written manually
- Code reviews required for generated code

### Risk 3: Circular Dependencies
**Risk:** Generated code may create circular imports
**Mitigation:**
- ImportResolver detects potential cycles
- Defers problematic imports to runtime
- Warns user of potential issues

### Risk 4: Breaking Existing Code
**Risk:** Auto-fixing may break working code
**Mitigation:**
- Always create backups
- Dry-run mode for preview
- Only write new files, don't modify existing implementations
- Manual confirmation required for destructive changes

## Future Enhancements

1. **Functional Test Generation**
   - Generate tests that instantiate classes
   - Test getter/setter functionality
   - Test method chaining

2. **Integration Tests**
   - Generate tests for parser integration
   - Test writer integration
   - Validate with ARXML files

3. **Attribute Type Validation**
   - Generate tests for attribute types
   - Validate type annotations
   - Check multiplicity (1, 0..1, *)

4. **Documentation Generation**
   - Generate docstrings from requirements
   - Include requirement IDs in comments
   - Generate class documentation

5. **Interactive Mode**
   - Step-by-step review of generated code
   - Accept/reject individual changes
   - Edit generated code before writing

## References

- Existing script: `scripts/compare-package-implementation.py`
- Test patterns: `tests/test_armodel/models/M2/`
- Coding standards: `docs/development/coding_rules.md`
- Project structure: `CLAUDE.md`

## Appendix: Example Output

```
============================================================
Package Implementation Comparison Script
============================================================
Project root: /Users/ray/Workspace/py-armodel
Mode: Smart Fix with Test Generation
Package: All packages

[1/5] Building import map from codebase...
  Scanned 847 classes across 156 files
  Built import map for 234 packages

[2/5] Comparing requirements vs implementation...
  Found 24 packages with differences
  - 12 missing classes
  - 8 classes with missing methods
  - 4 classes with incorrect imports

[3/5] Generating structural tests...
  Created: tests/test_armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/test_BswBehaviorStructure.py
  Created: tests/test_armodel/models/M2/AUTOSARTemplates/...

[4/5] Running tests to identify failures...
  pytest tests/... -v
  ================= 54 failed, 102 passed in 2.3s =================

[5/5] Generating code with smart imports...
  [Fix] Generating missing class: BswModuleEntity
    Resolved import: from ..CommonStructure import Identifiable
    ✓ Created: src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswModuleEntity.py
    ✓ Updated: __init__.py (added wildcard import)

  [Fix] Generating missing class: BswCalledEntity
    Resolved import: from ..CommonStructure import InternalBehavior
    ✓ Created: src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswCalledEntity.py

[6/6] Re-running tests to verify fixes...
  pytest tests/... -v
  ================= 2 failed, 154 passed in 1.8s =================

  Iteration 2: Fixing remaining failures...
  [Fix] Adding missing method getCalledEntityRef() to BswCalledEntity
  ✓ Updated: BswCalledEntity.py

Final Results:
  ✓ 156 classes validated
  ✓ 12 new classes generated
  ✓ 8 classes enhanced with missing methods
  ⚠  2 classes need manual review (see report)

Report: docs/requirements/package_comparison.md
```

---

**End of Design Document**
