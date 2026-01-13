# Agent Guidelines for py-armodel

## Build, Lint, and Test Commands

### Testing
- Run all tests: `pytest` or `npm run pytest`
- Run tests with coverage: `pytest --cov=armodel --cov-report term-missing` or `npm run pytest-cov`
- Run specific test file: `pytest tests/test_armodel/parser/test_arxml_parser.py`
- Run specific test method: `pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method`
- Run tests with verbose output: `pytest -v`
- Run tests with print output: `pytest -s`

### Linting
- Run flake8: `npm run flake8` (or `flake8 --select=E9,F63,F7,F82 .`)
- CI runs both syntax checks and complexity checks with max-line-length=127

### Building
- Create distribution: `python setup.py bdist_wheel`
- Create source and wheel: `python setup.py sdist bdist_wheel --universal`

## Code Style Guidelines

### Imports
- Standard library imports first (typing, xml, os, logging, getopt, re)
- Third-party imports next (colorama, openpyxl, lxml)
- Local imports using relative notation (e.g., `from ..models.M2...`)
- Imports organized alphabetically within groups
- Long import lists are common due to extensive AUTOSAR model classes

### Naming Conventions
- Classes: PascalCase (e.g., `ARXMLParser`, `AUTOSAR`, `RoleBasedDataAssignment`)
- Methods: camelCase (e.g., `getShortName`, `setRole`, `getUsedDataElement`)
- Variables: camelCase or lowercase_with_underscores
- Constants: UPPER_CASE (e.g., `CATEGORY_TYPE_REFERENCE`)
- Private attributes: underscore prefix (e.g., `_appl_impl_type_maps`)
- Test classes: `Test` prefix (e.g., `TestRoleBasedDataAssignment`)
- Test methods: lowercase_with_underscores

### Type Hints
- Use typing module (List, Dict, Optional, etc.)
- Type hints are used but not comprehensive
- Comments like `# type: List[Sdg]` for complex types
- When adding type annotations, only reference classes that exist in the codebase
- Add proper imports for existing types or remove annotations for non-existent types to avoid F821 errors

### Formatting
- Indentation with spaces
- Max line length: 127 characters (per CI flake8 config)
- Docstrings are optional but follow standard format when used
- Method chaining: setters return `self`
- Comment style: `# inline comments` (not doc comments)

### Error Handling
- Raise `ValueError`, `NotImplementedError`, `TypeError`, `Exception`
- Use descriptive error messages
- Abstract classes raise TypeError in `__init__`
- Error logging via `self.logger.error()` when warning mode enabled
- Use `self.raiseError()`, `self.notImplemented()`, `self.raiseWarning()` parser methods

### Architecture
- Follow AUTOSAR M2 schema structure for model organization
- Layered architecture: models/ (M2 structure), parser/, writer/, cli/, lib/, data_models/, transformer/, report/
- Test structure mirrors source structure (tests/models/ mirrors src/models/)
- Use singleton pattern for `AUTOSAR` class via `getInstance()`
- Abstract base classes use ABCMeta metaclass
- Separation of concerns between parser and writer modules

### AUTOSAR Specifics
- XML namespace: `http://autosar.org/schema/r4.0`
- AUTOSAR versions: 4.0.3 to R24-11 (especially R23-11)
- XSD mappings in `release_xsd_mappings` dictionary
- Follow AUTOSAR XML schema definitions
- Use proper AUTOSAR element types and references

### Testing
- Use pytest framework
- Test files mirror source structure
- Test methods are small and focused
- Use sample ARXML files from `tests/test_files/` for validation
- Run flake8 linting before committing

### Important Notes
- Python >= 3.5 required
- Do NOT add comments unless asked
- Follow PEP 8 coding conventions
- When modifying code, check that flake8 passes (especially E9,F63,F7,F82 errors)
- Run tests after changes to ensure no regressions
- Test folder structure must match source folder structure
