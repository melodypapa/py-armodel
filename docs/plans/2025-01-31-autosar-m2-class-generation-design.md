# Design: Automated AUTOSAR M2 Model Class Generation System

**Date**: 2025-01-31
**Status**: Design Approved
**Authors**: Generated via brainstorming session

## Executive Summary

This document describes a system to automatically generate 1,195 missing AUTOSAR M2 model classes by extracting class definitions from M2 documentation, generating Python code following project patterns, and validating against XSD schemas. The system ensures quality-first implementation while dramatically reducing manual effort.

## Problem Statement

The py-armodel project currently has **1,195 missing AUTOSAR M2 model classes** identified in the deviation report (`docs/requirements/deviation_package.md`). Manual implementation is challenging due to:

1. Complex inheritance hierarchies across the AUTOSAR meta-model
2. Need to accurately define properties and methods for each class
3. Proper package structure (leaf vs. non-leaf packages)
4. Maintaining consistency with existing 569 implemented classes

## Solution Overview

Generate classes automatically from three trusted sources:
1. **M2 Documentation** (`docs/requirements/M2/`) - 1,709 markdown files with structured class metadata
2. **Deviation Package** - List of missing classes with expected paths
3. **XSD Schema** (`docs/requirements/xsd/AUTOSAR_00046.xsd`) - Validation authority

## Architecture

### System Components

```
┌─────────────────────┐
│  Deviation Parser   │
│  (deviation.md)     │
└──────────┬──────────┘
           │ Missing classes list
           ▼
┌─────────────────────┐
│  M2 Documentation   │
│  Analyzer           │
│  (1,709 .md files)  │
└──────────┬──────────┘
           │ Class metadata index
           ▼
┌─────────────────────┐
│  Python Class       │
│  Generator          │
│  (Core engine)      │
└──────────┬──────────┘
           │ Generated .py files
           ▼
┌─────────────────────┐
│  XSD Validator      │
│  (Quality gate)     │
└─────────────────────┘
```

### Component 1: Deviation Parser

**Purpose**: Extract missing classes from deviation report and create prioritized work list.

**Implementation Details**:
- Reads `deviation_package.md` table
- Filters only rows marked `✗ MISSING`
- Parses M2 path: `M2::AUTOSARTemplates::CommonStructure::InternalBehavior::InternalBehavior`
- Parses expected Python path: `armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.InternalBehavior`
- Identifies abstract classes (marked in M2 name)
- Groups by domain for batch processing (CommonStructure, BswModuleTemplate, AdaptivePlatform, etc.)

**Output**: JSON work list indexed by domain

### Component 2: M2 Documentation Analyzer

**Purpose**: Build structured index of class definitions from markdown documentation.

**Implementation Details**:
- Scans all 1,709 files in `docs/requirements/M2/`
- Extracts metadata from frontmatter using regex:
  - **Package**: M2 namespace path
  - **Type**: Abstract vs. Concrete
  - **Parent**: Direct parent class
  - **Base Classes**: All base classes (multiple inheritance)
  - **Children**: Contained child classes
  - **Document Source**: PDF references
- Caches results in JSON for fast reload
- Handles edge cases: multi-line lists, special characters, missing fields

**Output**: In-memory class definition index keyed by class name

### Component 3: Python Class Generator

**Purpose**: Generate Python class code following project patterns.

**Generation Steps** for each missing class:

1. Look up class metadata in M2 index
2. Determine file structure:
   - Leaf package → `.py` file
   - Non-leaf package → directory with `__init__.py`
3. Generate class definition:
   - Import statements (ABC, parent classes, dataclasses)
   - Class docstring with requirements section
   - `__init__` method with parent reference
   - Getter/setter methods (AUTOSAR camelCase convention)
   - Type annotations (Python 3.10+ syntax)
   - Abstract base class handling (`@abstractmethod` where needed)
4. Create/update file in correct location
5. Add wildcard export to parent `__init__.py`
6. Update `src/armodel/models/__init__.py`

**Templates**:
- Simple dataclass pattern
- Complex with children pattern
- Abstract base pattern
- Multiple inheritance pattern

**Output**: Python source files in `src/armodel/models/M2/AUTOSARTemplates/`

### Component 4: XSD Validator

**Purpose**: Validate generated classes against XSD schema for correctness.

**Validation Levels**:

1. **Structural Validation**:
   - Python package path matches XSD namespace hierarchy
   - Leaf packages use `.py` files
   - Non-leaf packages use `__init__.py`

2. **Inheritance Validation**:
   - Python class inheritance matches XSD type extensions
   - Abstract classes inherit from ABC
   - `@abstractmethod` decorators on abstract methods

3. **Property Validation**:
   - XSD attributes/elements represented in Python class
   - Reports missing properties as warnings
   - Checks enum types exist for XSD enumerations

**Feedback Loop**: Re-run deviation package script after generation to identify:
- Previously missing classes now found
- New path mismatches
- Regression issues

**Output**: Validation report with checklist for each class

## Validation Strategy

### Manual Review Checklist

For each generated class:
- ✓ Package path matches M2 hierarchy
- ✓ Parent class correctly inherited
- ✓ Abstract classes use ABC
- ✓ Getter/setter methods follow AUTOSAR camelCase
- ✓ Wildcard export in parent `__init__.py`
- ✓ Included in `src/armodel/models/__init__.py`
- ✓ File follows PEP 8 conventions (79 char line length)
- ⚠ Properties covered (X% of XSD attributes)

### Quality Gates

Before committing generated classes:

1. **Syntax Check**: `flake8 --select=E9,F63,F7,F82`
2. **Import Check**: Verify all imports resolve
3. **Test Execution**: `python scripts/run_tests.py --unit` for module
4. **Coverage Check**: Baseline test coverage for new classes
5. **Round-Trip Test**: Parse → write → re-parse if ARXML samples exist

## Testing Approach

### Automated Test Generation

For each generated class, create test file in `tests/test_armodel/models/M2/`:

1. **Basic Existence Test**: Import and instantiate (or TypeError for abstract)
2. **Inheritance Test**: Verify parent class inheritance
3. **Getter/Setter Tests**: Test each generated method
4. **Parent Reference Test**: Validate parent attribute
5. **Package Structure Test**: Verify wildcard export

Uses existing test files as templates for consistency.

### Incremental Implementation

**Phase 1**: One domain (e.g., CommonStructure ~150 classes)
- Run full validation
- Fix generator issues
- Commit and tag

**Phase 2-N**: Repeat for remaining domains
- Improve generator each phase
- Track deviation report progress

### Progress Tracking

Dashboard showing:
- Classes generated vs. remaining (per domain, total)
- Validation pass/fail rate
- Test coverage percentage
- Current phase and status

## Data Flow Example

```
Input: BswEvent (abstract)
  ↓
Deviation Parser: MISSING → M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswEvent
  ↓
M2 Analyzer: Extract metadata
  - Package: BswModuleTemplate.BswBehavior
  - Type: Abstract
  - Parent: (none specified)
  - Base Classes: Identifiable
  - Children: BswScheduleEvent, BswInterruptEvent, ...
  ↓
Generator:
  - Create BswBehavior/BswEvent/__init__.py
  - Import ABC, Identifiable
  - class BswEvent(ABC, Identifiable)
  - Add @abstractmethod decorators
  - Export from parent __init__.py
  ↓
XSD Validator:
  - Check schema type extension
  - Verify abstract base
  - Report property coverage
  ↓
Output: src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswEvent/__init__.py
```

## Implementation Plan

### Phase 1: Tooling Development (2-3 days)
1. Create `scripts/generate_missing_classes.py` main script
2. Implement DeviationParser class
3. Implement M2DocumentationAnalyzer class
4. Implement PythonClassGenerator class
5. Implement XSDValidator class

### Phase 2: Testing Generation (1 day)
1. Implement TestGenerator class
2. Create test templates
3. Add quality gate checks

### Phase 3: Pilot Implementation (2-3 days)
1. Generate one small domain (e.g., GenericStructure ~50 classes)
2. Run validation and fix issues
3. Run tests and fix failures
4. Commit as proof-of-concept

### Phase 4-N: Domain Rollout (ongoing)
1. Generate CommonStructure (~150 classes)
2. Generate BswModuleTemplate (~200 classes)
3. Generate AdaptivePlatform (~300 classes)
4. Continue until all 1,195 classes implemented

## File Structure

```
scripts/
  generate_missing_classes.py         # Main entry point
  deviation_parser.py                 # Deviation report parser
  m2_documentation_analyzer.py        # M2 markdown parser
  python_class_generator.py           # Code generation engine
  xsd_validator.py                    # XSD validation
  test_generator.py                   # Test file generator

docs/plans/
  2025-01-31-autosar-m2-class-generation-design.md  # This document

src/armodel/models/M2/AUTOSARTemplates/
  (generated classes)

tests/test_armodel/models/M2/
  (generated tests)

docs/requirements/
  deviation_package.md                # Updated after each phase
  generation_progress.json            # Progress tracking
```

## Success Criteria

- [ ] All 1,195 missing classes generated
- [ ] All generated classes pass XSD validation
- [ ] All generated classes have test coverage
- [ ] All quality gates pass (flake8, pytest, coverage)
- [ ] Deviation report shows 0 missing classes
- [ ] No regression in existing 569 classes
- [ ] Code follows PEP 8 and project coding standards

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| XSD schema incomplete for some classes | Medium | Use M2 docs as primary source, XSD for validation |
| Generated code has subtle bugs | High | Comprehensive testing, manual review checklist |
| Package structure errors | Medium | Path validation, deviation reconciliation |
| Property inaccuracies from XSD inference | High | Manual review of abstract/concrete classes |
| Breaking existing functionality | High | Round-trip testing, regression tests |

## Next Steps

1. Review and approve this design document
2. Create implementation plan with detailed tasks
3. Set up git worktree for isolated development
4. Begin Phase 1: Tooling Development

---

**End of Design Document**
