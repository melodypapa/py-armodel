# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-armodel is a Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files. It supports AUTOSAR model processing with various tools and CLI utilities for handling AUTOSAR data structures.

## Architecture

The project is organized into the following key modules:

- **models**: Contains all AUTOSAR data model classes organized according to AUTOSAR XML schema (M2 structure)
  - M2/MSR/AsamHdo: ASAM HDO (Hardware Description Objects) related models
  - M2/AUTOSARTemplates: Core AUTOSAR template models organized by domain
    - CommonStructure: Common AUTOSAR elements
    - SWComponentTemplate: Software component models
    - SystemTemplate: System-level models
    - BswModuleTemplate: Basic Software module models
    - ECUCDescriptionTemplate: ECUC (Embedded Component and Configuration) models
    - etc.

- **parser**: ARXML parsing functionality
  - arxml_parser.py: Main parser class for reading ARXML files
  - abstract_arxml_parser.py: Abstract base parser
  - connector_xlsx_parser.py: Excel connector parsing

- **writer**: ARXML writing functionality
  - arxml_writer.py: Main writer class for writing ARXML files
  - abstract_arxml_writer.py: Abstract base writer

- **cli**: Command-line interface tools
  - Various CLI utilities for different AUTOSAR operations

## Development Commands

### Testing
- Run all tests: `pytest`
- Run tests with coverage: `pytest --cov=armodel --cov-report term-missing`
- Run specific test: `pytest path/to/test_file.py`
- Run specific test method: `pytest path/to/test_file.py::TestClass::test_method`

### Linting
- Run Flake8: `npm run flake8` (or `flake8 --select=E9,F63,F7,F82 .`)

### Building
- Create distribution: `python setup.py bdist_wheel`
- Create source and wheel: `python setup.py sdist bdist_wheel --universal`
- Check distribution: `twine check dist/*`

### Formatting
- Format ARXML files: `arxml-format <input.arxml> <output.arxml>`

## Key CLI Tools

- `arxml-dump`: Dump all ARXML data to screen
- `arxml-format`: Format ARXML files
- `arxml-swc`: List all SWComponentType in the autosar model
- `connector2xlsx`: Export all SwConnector to Excel file
- `connector-update`: Update SwConnector from Excel file
- `armodel-component`: List SW-Components in specific path
- `armodel-system-signal`: List system signals
- `armodel-memory-section`: Memory section operations
- `armodel-file-list`: File listing
- `armodel-uuid-checker`: UUID validation
- `format-xml`: XML formatting

## Core Concepts

- **AUTOSAR Singleton**: The `AUTOSAR.getInstance()` pattern provides a singleton instance for managing the entire AUTOSAR model
- **M2 Structure**: Models follow the AUTOSAR M2 schema structure (M2/MSR/..., M2/AUTOSARTemplates/...)
- **ARPackage**: The primary container for organizing AUTOSAR elements hierarchically
- **Parser/Writer**: Separate modules for reading and writing ARXML files
- **Referrable/Identifiable**: Core base classes implementing AUTOSAR object identification and referencing

## Testing Structure

Tests are located in `src/armodel/tests` and cover various AUTOSAR model components. Test files in `test_files/` directory contain sample ARXML files for validation.

## Code Organization

- Data models are organized according to AUTOSAR specification structure
- Parser and writer follow separation of concerns
- CLI tools provide specific functionality access points
- Test files use sample ARXML files from the test_files directory