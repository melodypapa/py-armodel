# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-armodel is a Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files. It follows the AUTOSAR standard specifications and supports versions from 4.0.3 to R24-11, with particular focus on CP R23-11 standard compliance.

**Current Version**: 1.9.2
**Python Requirements**: >= 3.7 (CI tests on 3.8-3.12)
**License**: MIT
**Repository**: http://github.com/melodypapa/py-armodel

## Critical Architecture Concepts

### V1 vs V2 Models

The codebase contains two model architectures:

**V1 Models** (`armodel.models`):
- Legacy architecture with wildcard imports
- Uses TYPE_CHECKING blocks for forward references
- Allows circular dependencies
- Relative imports permitted
- Located in `src/armodel/models/`

**V2 Models** (`armodel.v2.models`):
- Modern architecture with absolute imports only
- String annotations for forward references (no TYPE_CHECKING)
- Prohibits circular dependencies
- Explicit `__all__` exports
- Located in `src/armodel/v2/models/`
- **100% API compatible with V1** - only import paths change

**Recommendation**: Use V2 models for new code. V2 is drop-in compatible with V1.

### AUTOSAR M2 Meta-model Structure

The codebase follows the AUTOSAR M2 meta-model hierarchy:

```
src/armodel/
├── models/M2/                 # V1 AUTOSAR M2 meta-model
│   ├── MSR/                   # Meta-model semantic rules (AsamHdo, DataDictionary, Documentation, CalibrationData)
│   └── AUTOSARTemplates/      # AUTOSAR template models by domain
│       ├── AutosarTopLevelStructure    # AUTOSAR singleton
│       ├── CommonStructure            # ARObject, Referrable, Identifiable, ServiceNeeds
│       ├── SWComponentTemplate        # Components, port interfaces, datatypes, behavior
│       ├── SystemTemplate             # System signals, ECU instances, communication
│       ├── BswModuleTemplate          # BSW module descriptions, behavior, implementation
│       └── ECUCDescriptionTemplate    # ECUC configuration values
└── v2/models/M2/             # V2 AUTOSAR M2 meta-model (same structure, improved code)
```

**Key Pattern**: AUTOSAR uses deep package hierarchies matching the M2 specification. Always verify package structure before adding classes.

### AUTOSAR Singleton Pattern

`AUTOSAR` class uses singleton pattern:
- `AUTOSAR.getInstance()` - Get/create the singleton instance
- `AUTOSAR.new()` - Clear and create fresh instance
- `AUTOSAR.setARRelease(version)` - **MUST** be called before parsing/writing to select correct XML schema

**Critical**: Always set AUTOSAR version before parsing or writing ARXML files.

### Parent-Child Object Graph

AUTOSAR model objects maintain bi-directional references:
- Every object has a `parent` attribute pointing to its container
- Parents hold collections of children
- ARPackage hierarchy is the primary containment structure
- When manipulating models, maintain parent-child relationships carefully
- Use `addElement()` methods rather than directly appending to lists

### Element Naming

- AUTOSAR elements use "short name" as primary identifier (not Python's `__name__`)
- Short names must be unique within their containing package/context
- Use `findXXX()` methods for lookups by short name; they return `None` if not found (not exceptions)
- Same short name can exist in different packages or with different types

### Wildcard Import Pattern (V1 Models)

V1 models use wildcard imports in `__init__.py` files:
```python
from .my_class import *
```

This allows imports like:
```python
from armodel.models.M2.AUTOSARTemplates import SwcInternalBehavior
```

**V2 models use explicit imports and `__all__` exports instead.**

### Abstract Base Class Pattern

AUTOSAR uses proper Python ABC (Abstract Base Class) pattern with `@abstractmethod` decorator.

**V2 Implementation (Proper ABC Pattern):**
```python
from abc import ABC, abstractmethod

class ARObject(ABC):
    @abstractmethod
    def _validate_abstract(self) -> None:
        """Abstract method to enforce abstract base class pattern."""
        pass

    def __init__(self) -> None:
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")
        self._validate_abstract()

class SwComponentType(ARObject):
    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass
```

**V1 models may use informal ABC or ABCMeta metaclass.**

### Enum Usage: AREnum vs Python Enum

**CRITICAL**: Use `AREnum` base class instead of Python's `enum.Enum` for AUTOSAR compliance.

```python
# Correct - Use AREnum for AUTOSAR enums
from armodel.models.base import AREnum

class BswEntryKindEnum(AREnum):
    PROVIDED = "PROVIDED"
    REQUIRED = "REQUIRED"

# Incorrect - Do NOT use Python Enum
from enum import Enum  # Don't do this
class MyEnum(Enum):   # Violates AUTOSAR compliance
    VALUE = "value"
```

## Development Commands

### Testing

**Recommended test runner** (colored output, comprehensive summaries):
```bash
python scripts/run_tests.py              # All tests (unit + integration)
python scripts/run_tests.py --unit       # Unit tests only
python scripts/run_tests.py --integration # Integration tests only
python scripts/run_tests.py --coverage   # With coverage reports
```

**Using pytest directly**:
```bash
pytest --cov=armodel --cov-report term-missing
pytest tests/test_armodel/parser/test_arxml_parser.py  # Specific test file
pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method  # Specific method
pytest -v  # Verbose output
pytest -s  # Show print output
```

**Test markers** (use with `-m` flag):
- `integration`: Integration tests (slower, parse/write cycle)
- `slow`: Slow-running tests (skip with `-m "not slow"`)
- `datatypes`, `components`, `bsw`, `system`, `blueprint`, `lifecycle`: Domain-specific tests

### Integration Tests

The project includes comprehensive integration tests in `tests/integration_tests/`:
- 29 ARXML files tested from `test_files/` directory
- Round-trip validation: Parse → Write → Re-parse → Compare
- Auto-detects AUTOSAR version from XSD schema (4.0.3 to R24-11)
- Configurable via `tests/integration_tests/config.yaml`

```bash
# Run integration tests
python scripts/run_tests.py --integration

# Run specific test categories
pytest tests/integration_tests/ -k "datatypes"
pytest tests/integration_tests/ -k "bsw"
```

### Linting

**Primary linter: Ruff**
```bash
ruff check .               # Check all files
ruff check --fix .         # Auto-fix issues
ruff check --show-source . # Show detailed violations
ruff check src/armodel/v2/ # V2 models only
```

**Type checking: MyPy** (for V2 models)
```bash
mypy src/armodel/v2/                           # V2 models
mypy src/armodel/v2/models/                   # Specific submodule
mypy src/armodel/v2/reader/                    # Reader module
mypy src/armodel/v2/writer/                    # Writer module
```

**V2 Type Checking Status**: 6348 mypy errors (mostly missing type annotations). This is acceptable for gradual type annotation adoption. Focus on new code and critical paths first.

### Building and Installation

```bash
pip install -e .              # Install in editable mode
python -m build               # Create source and wheel distributions
twine check dist/*            # Check distribution
twine upload dist/*           # Upload to PyPI
```

## Module Organization

```
src/armodel/
├── models/                   # V1 AUTOSAR data model classes (M2 schema structure)
├── v2/                       # V2 models with improved architecture
│   ├── models/              # V2 AUTOSAR data model classes
│   ├── reader/              # V2 ARXML deserialization
│   ├── writer/              # V2 ARXML serialization
│   └── utils/               # V2 shared utilities
├── parser/                   # ARXML parsing (arxml_parser.py)
├── writer/                   # ARXML writing (arxml_writer.py)
├── cli/                      # Command-line interface tools (10+ utilities)
├── lib/                      # Library utilities
├── data_models/              # Data model definitions (sw_connector.py)
├── transformer/              # Data transformation
└── report/                   # Report generation
```

### CLI Tools (console_scripts)

- `arxml-dump` - Dump ARXML data to screen
- `arxml-format` - Format ARXML files
- `armodel-component` - List SwComponentType
- `connector2xlsx` - Export SwConnector to Excel
- `connector-update` - Update SwConnector from Excel
- `armodel-system-signal` - List system signals
- `armodel-memory-section` - Memory section operations
- `armodel-file-list` - List files
- `armodel-uuid-checker` - UUID validation
- `format-xml` - XML formatting

### Development Scripts

The `scripts/` directory contains utility scripts for development:

**Testing and Quality:**
- `run_tests.py` - Comprehensive test runner with colored output (recommended)
- `check_v2_deviation.py` - Check V2 model deviations

**Code Generation and Migration:**
- `generate_v2_models.py` - Generate V2 model classes
- `generate_class_package_json.py` - Generate class package mapping
- `migrate_bsw_classes.py` - Migrate BSW module classes
- `migrate_common_classes.py` - Migrate common structure classes
- `migrate_diagnostic_classes.py` - Migrate diagnostic classes
- `migrate_generic_classes.py` - Migrate generic structure classes
- `migrate_swcomponent_classes.py` - Migrate SW component classes
- `migrate_system_classes.py` - Migrate system template classes

**Validation and Analysis:**
- `deviation-package.py` - Generate package structure deviation reports
- `deviation-class-hierarchy.py` - Generate class hierarchy deviation reports
- `scan_existing_classes.py` - Scan and catalog existing classes
- `compare-package-implementation.py` - Compare package structure

**Utilities:**
- `add_validate_abstract.py` - Add abstract validation to V2 models
- `copy_base_classes.py` - Copy base classes during migration

## Common Development Tasks

### Adding a new AUTOSAR model class

**For V1 models**:
1. Determine if it should be a leaf package (`.py` file) or non-leaf package (`__init__.py`)
2. Create the file in `src/armodel/models/M2/AUTOSARTemplates/`
3. Add wildcard import in parent `__init__.py`: `from .my_class import *`
4. Add import to `src/armodel/models/__init__.py`
5. Create test in `tests/test_armodel/models/M2/`
6. Run tests and linting: `python scripts/run_tests.py`
7. Verify package structure: `python scripts/deviation-package.py`

**For V2 models**:
1. Determine if it should be a leaf package (`.py` file) or non-leaf package (`__init__.py`)
2. Create the file in `src/armodel/v2/models/M2/AUTOSARTemplates/`
3. Use **absolute imports** and **block import style**:
   ```python
   from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
       ARObject,
   )
   ```
4. Add explicit `__all__` export in parent `__init__.py`:
   ```python
   from armodel.v2.models.M2.AUTOSARTemplates.MyModule import MyClass

   __all__ = ["MyClass"]
   ```
5. If creating abstract class, use `@abstractmethod`
6. If creating concrete class, implement `_validate_abstract()`
7. Create test in `tests/test_armodel/models_v2/M2/`
8. Run V2 checks: `ruff check src/armodel/v2/models/ && pytest tests/test_armodel/models_v2/`

### Parser Usage

```python
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

# MUST set AUTOSAR version first
AUTOSAR.setARRelease('R23-11')

# Get singleton instance and clear
document = AUTOSAR.getInstance()
document.clear()

# Parse ARXML file
parser = ARXMLParser()
parser.load('example.arxml', document)

# Or with warning mode for development
parser = ARXMLParser(options={"warning": True})
parser.load('example.arxml', document)
```

### Writer Usage

```python
from armodel.models import AUTOSAR
from armodel.writer.arxml_writer import ARXMLWriter

# MUST set AUTOSAR version first
AUTOSAR.setARRelease('R23-11')

# Write to ARXML file
writer = ARXMLWriter()
writer.save('output.arxml', AUTOSAR.getInstance())
```

### Finding Elements by Short Name

```python
from armodel.models import AUTOSAR

autosar = AUTOSAR.getInstance()

# Find returns None if not found (no exceptions)
component = autosar.findAtomicSwComponentType('MyComponent')
if component is not None:
    behavior = autosar.getBehavior(component)
```

## Important Implementation Details

### Type Annotations
- Use Python 3.10+ union syntax: `str | None` instead of `Optional[str]`
- Use forward references with string literals for circular dependencies: `List["MyClass"]`
- Only reference classes that exist in the codebase to avoid F821 flake8 errors
- **V2 models**: Use string annotations for forward refs (no TYPE_CHECKING blocks)

### Package Structure Rules

**CODING_RULE_STYLE_00008: Class Location and Package Structure**

Classes must be located in the correct package according to AUTOSAR M2 model hierarchy.

**Leaf packages** (no subdirectories): Classes defined in `.py` file with package name = filename
**Non-leaf packages** (have subdirectories): Classes defined in `__init__.py` of the directory
**Never** create double nesting like `ImplementationDataTypes/ImplementationDataTypes.py`
Always verify package exists before adding classes

**Example - Leaf Package (actual project file):**
```
src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
```
This file defines: `ImplementationDataType`, `AbstractImplementationDataTypeElement`, `ImplementationDataTypeElement`
Import: `from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType`

**Example - Non-Leaf Package (actual project directory):**
```
src/armodel/models/M2/AUTOSARTemplates/CommonStructure/
├── __init__.py          # Defines: ValueSpecification, ConstantSpecification
├── ImplementationDataTypes.py
├── SwDataDefProps.py
└── FlatMap.py
```
Import: `from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification`

**CODING_RULE_STYLE_00009: Class Export and Module Organization**

All classes must be properly exported from their modules and be importable via the expected AUTOSAR M2 path.
- All classes must be exportable via wildcard imports (`from .module import *`)
- Classes must be importable from the module path specified in `docs/requirements/mapping.json`
- Run `python scripts/deviation-package.py` to verify compliance

### Parent-Child Relationships
- Always maintain parent-child relationships
- Use `addElement()` methods rather than directly appending to lists
- Parent references are used for navigation and serialization

### Common Pitfalls

**Import Errors**:
- Ensure proper package structure when adding new classes
- Check that wildcard imports in `__init__.py` files include new classes (V1)
- Check that `__all__` lists include new classes (V2)
- Run `python scripts/deviation-package.py` to verify compliance

**Enum Usage**:
- Always use `AREnum` base class, never Python's `enum.Enum`
- Import from `armodel.models.base import AREnum`
- Parser and writer expect AREnum instances for proper serialization

## Troubleshooting

### Common Issues

**ImportError when adding new classes:**
- Verify the class is in the correct package (leaf vs. non-leaf)
- Check that wildcard imports in `__init__.py` include the new class (V1)
- Check that `__all__` lists include the new class (V2)
- Run `python scripts/deviation-package.py` to verify package structure

**Type checking errors with mypy:**
- Use `from __future__ import annotations` for forward references
- Use string annotations for circular dependencies: `"ClassName"`
- Only reference classes that actually exist in the codebase
- Check V2 coding rules in `docs/development/coding_rules_v2.md`

**Linting errors with ruff:**
- AUTOSAR methods use camelCase (N802 ignored)
- AUTOSAR modules use PascalCase (N999 ignored)
- Line length warnings are allowed for clarity (E501, W505 ignored)
- V2 models have specific ignores for AUTOSAR patterns

**Test failures:**
- Always set AUTOSAR version before parsing: `AUTOSAR.setARRelease("R23-11")`
- Clear singleton between tests: `AUTOSAR.getInstance().clear()`
- Use `ARXMLParser(options={"warning": True})` for development
- Check that test file structure mirrors source structure

**Package structure violations:**
- Run `python scripts/deviation-package.py` to identify issues
- Check `reports/deviation_package.md` for current status
- Follow CODING_RULE_STYLE_00008 and CODING_RULE_STYLE_00009
- Use actual project file paths as examples

### Getting Help

1. Check project documentation in `docs/` directory
2. Review design documents in `docs/plans/`
3. Run deviation reports to identify structural issues
4. Use custom slash commands: `/quality`, `/test`, `/req`

## CI/CD

GitHub Actions (`.github/workflows/python-package.yml`):
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Linting with flake8:
  - Critical errors: `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`
  - All errors: `flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`
- Testing: `pytest --ignore=tests/integration_tests/test_class_mapping.py`
- Auto-merge: PRs by repo owner (melodypapa) are automatically merged after CI passes
- All lint and test checks must pass before merge

### Local Linting with Ruff
```bash
ruff check .               # Check all files
ruff check --fix .         # Auto-fix issues
ruff check --show-source . # Show detailed violations
ruff check src/armodel/v2/ # V2 models only
```

### V2 Quality Status
- **V2 Validation**: 1937 classes, 100% verified (all in correct locations)
- **V2 Linting**: 113 ruff errors (all intentional patterns: AUTOSAR naming, circular dependencies)
- **V2 Type Checking**: 6348 mypy errors (mostly missing type annotations)
- **V2 Tests**: All 2357 tests passing (unit + integration)

## Reports and Tracking

The project maintains comprehensive tracking reports in the `reports/` directory:

- **`deviation_package.md`** - Package structure deviations between documented AUTOSAR M2 model and implementation (610 match, 1189 missing, 87 path mismatch, 207 extra)
- **`v2_validation_report.md`** - V2 models validation status (1937 classes verified)
- **`run_tests_report.md`** - Test execution reports

### Deviation Tracking Scripts

```bash
# Generate package structure deviation report
python scripts/deviation-package.py

# Generate class hierarchy deviation report
python scripts/deviation-class-hierarchy.py

# Check V2 deviations
python scripts/check_v2_deviation.py

# Scan existing classes in the codebase
python scripts/scan_existing_classes.py
```

## Custom Slash Commands

The project includes custom slash commands in `.claude/commands/` for automating common workflows:

### `/gh-workflow` - GitHub Workflow Automation
Automates the complete GitHub workflow: create issue → create branch → commit → push → create PR.

```bash
/gh-workflow
/gh-workflow Implement new parser for AUTOSAR models
```

### `/test` - Test Runner
Run the project test suite with comprehensive reporting.

```bash
/test                    # Run all tests
/test --unit            # Run only unit tests
/test --integration     # Run only integration tests
```

### `/quality` - Quality Check
Run all quality checks (linting, type checking, testing).

```bash
/quality        # Run all quality checks
/quality --fix  # Auto-fix linting issues
```

### `/req` - Requirement Management
Manage AUTOSAR project requirements with traceability.

```bash
/req add SWR_WRITER_00007 "Add support for custom markdown templates"
/req check traceability
/req list draft
```

### `/merge-pr` - Pull Request Merging
Merge pull requests with proper validation.

See `.claude/commands/README.md` for complete command documentation.

## Additional Documentation

- `AGENTS.md` - Additional guidelines for AI agents
- `IFLOW.md` - Chinese language project guide
- `docs/development/coding_rules.md` - Comprehensive coding rules (V1)
- `docs/development/coding_rules_v2.md` - V2-specific coding rules (15 rules)
- `docs/development/v2_migration_guide.md` - V1 to V2 migration guide
- `docs/requirements/software_components_hierarchy.md` - Complete class hierarchy
- `.claude/commands/README.md` - Custom slash commands documentation

### Design and Planning Documents

The `docs/plans/` directory contains design and implementation documents:

- `2025-02-05-models-v2-design.md` - V2 models architecture design
- `2025-02-05-models-v2-implementation.md` - V2 models implementation details
- `2026-02-07-v2-arxml-reader-writer-design.md` - V2 reader/writer architecture
- `2026-02-01-package-structure-migration-design.md` - Package structure migration plan
- `2026-02-06-mypy-v2-fixes-design.md` - MyPy type checking fixes
- `2025-01-31-autosar-m2-class-generation-design.md` - Automated class generation design

## References

- AUTOSAR: https://www.autosar.org/
- GitHub: http://github.com/melodypapa/py-armodel
- PyPI: https://pypi.org/project/armodel/
- Docs: https://py-armodel.readthedocs.io/
