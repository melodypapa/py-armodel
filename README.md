# py-armodel

**A Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files**

[![PyPI version](https://badge.fury.io/py/armodel.svg)](https://badge.fury.io/py/armodel)
[![Documentation Status](https://readthedocs.org/projects/py-armodel/badge/?version=latest)](https://py-armodel.readthedocs.io/en/latest)
[![GitHub Actions](https://github.com/melodypapa/py-armodel/actions/workflows/python-package.yml/badge.svg)](https://github.com/melodypapa/py-armodel/actions)
[![Coverage Status](https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main)](https://coveralls.io/github/melodypapa/py-armodel?branch=main)
[![Python Versions](https://img.shields.io/pypi/pyversions/armodel.svg)](https://pypi.org/project/armodel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

py-armodel is a Python library that implements the AUTOSAR meta-model for working with AUTOSAR XML (ARXML) files. It follows the AUTOSAR standard specifications and supports versions from 4.0.3 to R24-11, with particular focus on CP R23-11 standard compliance.

**Current Version**: 1.9.1
**Python Requirements**: >= 3.5 (CI tests on 3.8-3.12)
**License**: MIT
**Repository**: http://github.com/melodypapa/py-armodel

## Key Features

- **Complete AUTOSAR M2 Meta-model**: Implements the AUTOSAR meta-model structure
- **ARXML Parser & Writer**: Read and write ARXML files with version detection
- **Component Support**: Software components, port interfaces, data types, behavior, implementation
- **Communication Support**: CAN, LIN, FlexRay, Ethernet, Network Management, End-to-End Protection
- **BSW Modules**: Basic Software module descriptions, behavior, implementation, interfaces
- **ECUC Configuration**: ECUC configuration values and parameter definitions
- **Command-Line Tools**: 10+ CLI utilities for common ARXML operations
- **Type Safety**: Full type annotations with Python 3.10+ union syntax
- **Comprehensive Testing**: 2200+ unit tests, 29 integration tests with round-trip validation

## Reference Documents

1. AUTOSAR_TPS_XMLSchemaProductionRules.pdf
2. AUTOSAR_TPS_ARXMLSerializationRules.pdf

## Installation

### Install from PyPI

```bash
pip install armodel
```

### Install for Development

```bash
# Clone the repository
git clone https://github.com/melodypapa/py-armodel.git
cd py-armodel

# Install in editable mode
pip install -e .

# Install development dependencies
pip install pytest pytest-cov flake8
```

### Dependencies

**Runtime:**
- colorama
- openpyxl
- lxml

**Development:**
- pytest
- pytest-cov
- flake8
- sphinx (for documentation)

## Building and Publishing

### Creating Distribution

```bash
# Build both source and wheel distributions
python -m build

# Build only source distribution
python -m build --sdist

# Build only wheel distribution
python -m build --wheel
```

### Uploading to PyPI

```bash
# Check the distribution
twine check dist/*

# Upload to PyPI
twine upload dist/*

# Verify at https://pypi.org/project/armodel/
```

For more details, see https://packaging.python.org/  

## Testing

### Quick Start (Recommended)

Use the test runner script for colored output and comprehensive testing:

```bash
# Run all tests (unit + integration)
python scripts/run_tests.py

# Run only unit tests
python scripts/run_tests.py --unit

# Run only integration tests
python scripts/run_tests.py --integration

# Run with coverage reports
python scripts/run_tests.py --coverage

# Verbose output
python scripts/run_tests.py --verbose
```

### Using pytest Directly

```bash
# Install pytest
pip install pytest pytest-cov

# Run all tests with coverage
pytest --cov=armodel --cov-report term-missing

# Run only unit tests
pytest tests/test_armodel/

# Run integration tests with progress output
pytest tests/integration_tests/ -s

# Run specific test file
pytest tests/test_armodel/parser/test_arxml_parser.py

# Run specific test method
pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method

# Verbose output
pytest -v

# Show print output
pytest -s
```

## Integration Tests

The project includes a comprehensive integration test suite that validates round-trip parsing and writing of ARXML files.

### Purpose

Integration tests verify the complete parse → write → re-parse → compare cycle to ensure data integrity through the full workflow.

### Test Coverage

- **29 ARXML files** tested from `test_files/` directory
- **Round-trip validation**: Parse → Write → Re-parse → Compare
- **AUTOSAR version detection**: Auto-detects from 4.0.3 to R24-11
- **Extensible**: Add custom directories via `config.yaml`

### Running Integration Tests

```bash
# Using the test runner (recommended)
python scripts/run_tests.py --integration

# Using pytest directly with progress output
pytest tests/integration_tests/ -s

# Run specific file categories
pytest tests/integration_tests/ -k "datatypes"
pytest tests/integration_tests/ -k "bsw"
pytest tests/integration_tests/ -k "production"
```

### Adding Custom Test Files

Edit `tests/integration_tests/config.yaml`:

```yaml
additional_directories:
  - path: "/path/to/your/project/arxml"
    category: "production"
    recursive: true

exclude_patterns:
  - "*/temp/*.arxml"
  - "*/backup/*.arxml"
```

For more details, see [tests/integration_tests/README.md](tests/integration_tests/README.md).

## Usage

### Basic Usage

```python
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

# Set AUTOSAR version before parsing/writing
AUTOSAR.setARRelease("R23-11")

# Parse ARXML file
parser = ARXMLParser()
document = AUTOSAR.getInstance()
document.clear()
parser.load("input.arxml", document)

# Access the model
packages = document.getARPackages()
for pkg in packages:
    print(f"Package: {pkg.getShortName()}")

# Write to ARXML file
writer = ARXMLWriter()
writer.save("output.arxml", document)
```

### Best Practices

1. **Always set AUTOSAR version** before parsing or writing:
   ```python
   AUTOSAR.setARRelease("R23-11")  # Required
   ```

2. **Reset singleton** between operations:
   ```python
   AUTOSAR.getInstance().clear()  # or AUTOSAR.new()
   ```

3. **Use warning mode** for development:
   ```python
   parser = ARXMLParser(options={"warning": True})
   ```

4. **Find elements by short name**:
   ```python
   component = autosar.findAtomicSwComponentType("MyComponent")
   if component is not None:
       behavior = autosar.getBehavior(component)
   ```

### Common Workflows

#### Load and Inspect ARXML

```python
AUTOSAR.setARRelease("R23-11")
parser = ARXMLParser()
doc = AUTOSAR.getInstance()
doc.clear()
parser.load("file.arxml", doc)

# List all software components
components = doc.getAtomicSwComponentTypes()
for comp in components:
    print(f"{comp.getShortName()}: {comp.__class__.__name__}")
```

#### Modify and Save ARXML

```python
# Load existing file
parser.load("input.arxml", doc)

# Find and modify a component
comp = doc.findAtomicSwComponentType("MyComponent")
if comp:
    comp.setShortName("NewComponentName")

# Save changes
writer.save("output.arxml", doc)
```

## 1.7. How to create a distribution and wheel

* Run `python -m build` to build both source and wheel distributions
* Run `python -m build --sdist` to build only source distribution
* Run `python -m build --wheel` to build only wheel distribution

## 1.8. How to create the document

1. Run `pip install sphinx` to install the necessary document

## 1.9. Heritage 

```
- ARObject
  - Referrable
    - MultilanguageReferrable
      - Identifiable
        - PackageableElement
          - ARElement
            - AtpType
              - AutosarDataType
              - PortInterface
                - DataInterface
                  - NvDataInterface
                  - ParameterInterface
                  - SenderReceiverInterface
            - BswModuleEntry
            - EndToEndProtectionSet
          - Implementation
            - BswImplementation
        - AtpFeature
          - AtpPrototype
            - AtpPrototype
              - DataPrototype
                - AutosarDataPrototype
                  - VariableDataPrototype
                - ApplicationCompositeElementDataPrototype
                  - ApplicationArrayElement
                  - ApplicationRecordElement
          - AtpStructureElement
            - BswModuleDescription
        - ExecutableEntity
        - SwcBswMapping
        - PortPrototype
          - AbstractProvidedPortPrototype
            - PPortPrototype
          - AbstractRequiredPortPrototype
            - RPortPrototype
  - ValueSpecification
    - ConstantReference
```

## CLI Tools

The library provides 10+ command-line tools for common ARXML operations:

### arxml-dump

Dump all ARXML data to screen.

```bash
arxml-dump --arxml file1.arxml --arxml file2.arxml
arxml-dump --arxml input.arxml -h  # Show help
```

### arxml-format

Format ARXML files.

```bash
arxml-format input.arxml output.arxml
```

### armodel-component

List all SwComponentType in the AUTOSAR model.

```bash
# List all components (short name format)
armodel-component <arxml_folder>

# List all components with long format (includes package names)
armodel-component --format long <arxml_folder>

# List only CompositionSwComponent
armodel-component --format long --filter CompositionSwComponent <arxml_folder>
```

### armodel-system-signal

List all system signals.

```bash
armodel-system-signal <arxml_folder>
```

### armodel-memory-section

Memory section operations.

```bash
armodel-memory-section <command> [options]
```

### armodel-file-list

List files.

```bash
armodel-file-list <arxml_folder>
```

### armodel-uuid-checker

Validate UUIDs in ARXML files.

```bash
armodel-uuid-checker <arxml_folder>
```

### connector2xlsx

Export all SwConnector (AssemblySwConnector, DelegationSwConnector) to Excel file.

```bash
connector2xlsx input.arxml output.xlsx
```

### connector-update

Update all SwConnector (AssemblySwConnector, DelegationSwConnector) from Excel file.

```bash
connector-update input.arxml data.xlsx output.arxml
```

### format-xml

Format XML files.

```bash
format-xml input.xml output.xml
```


## API Reference

### AUTOSAR Singleton

```python
from armodel.models import AUTOSAR

# Get or create singleton instance
document = AUTOSAR.getInstance()

# Clear and create fresh instance
document = AUTOSAR.new()

# MUST set AUTOSAR version before parsing/writing
AUTOSAR.setARRelease('R23-11')  # or '4.0.3', 'R24-11', etc.
```

### ARXMLParser Constructor

```python
from armodel.parser.arxml_parser import ARXMLParser

# Create parser with warning mode for development
parser = ARXMLParser(options={"warning": True})

# Create parser in strict mode (raises exceptions)
parser = ARXMLParser()
```

### Key AUTOSAR Methods

```python
# Find elements by short name (returns None if not found)
component = autosar.findAtomicSwComponentType("MyComponent")
signal = autosar.findSystemSignal("MySignal")
port = autosar.findPort("MyPort")
data_type = autosar.findImplementationDataType("MyDataType")

# Get behavior and implementation
behavior = autosar.getBehavior(component)
implementation = autosar.getImplementation(component)

# Get collections
components = autosar.getAtomicSwComponentTypes()
compositions = autosar.getCompositionSwComponentTypes()
signals = autosar.getSystemSignals()
```

## Documentation

### Building Documentation

```bash
# Install sphinx
pip install sphinx

# Build with Sphinx
cd docs && make html

# Or build with MkDocs
mkdocs build
mkdocs serve
```

### Additional Documentation

- [CLAUDE.md](CLAUDE.md) - Project guidance for Claude Code
- [AGENTS.md](AGENTS.md) - Agent guidelines
- [IFLOW.md](iflow.md) - Chinese language project guide
- [docs/](docs/) - Comprehensive documentation

## Changelog

### Version 1.9.1 (Latest)

1. **Package Structure Refactoring**
   - Fixed case-sensitivity issues with Components/ vs Components directories
   - Reorganized ECUC module imports to resolve ImportError
   - Improved AnyInstanceRef and CompositionSwComponentType package structure
   - Enhanced deviation tracking and documentation

2. **Test Coverage Enhancement**
   - Ongoing effort to increase test coverage across all modules
   - Focus on M2 models, parser, writer, and library functions
   - Added tests for SwcInternalBehavior and NetworkManagement
   - Using test-driven development for new features

3. **Documentation Improvements**
   - Added comprehensive deviation documentation
   - Enhanced class hierarchy documentation
   - Improved coding rules documentation
   - Added SpeckKit integration for feature specification

### Version 1.9.0

1. **Testing Infrastructure**
   - Add comprehensive integration test suite with round-trip validation
   - Add test runner script (`scripts/run_tests.py`) with colored output
   - Add pytest configuration (`pytest.ini`) with custom markers
   - Support 2205+ unit tests and 29 integration test files
   - Add coverage reporting (HTML and terminal)

2. **Integration Tests**
   - Round-trip testing: Parse → Write → Re-parse → Compare
   - Tests all 29 ARXML files in `test_files/` directory
   - Auto-detects AUTOSAR version from XSD schema (4.0.3 to R24-11)
   - Verbose progress tracking with step-by-step feedback
   - Extensible configuration via YAML for additional test directories

3. **Documentation**
   - Add integration test design document
   - Add integration test README with usage examples
   - Update CLAUDE.md with test runner documentation

4. **Developer Experience**
   - Unified test runner for both unit and integration tests
   - Colored console output (success/failure/warning)
   - Test summary with pass/fail/skip statistics
   - Support for category-based test selection

### Version 1.8.7

1. Correct the base class of the BswEvent
2. Export the RunnableEntity class
3. Add the more class support for getDestType

### Version 1.8.6

1. To support the following AR Element:
   - NvProvideComSpec
   - NvRequireComSpec
2. To improve the following AR Element:
   - ParameterAccess

### Version 1.8.5

1. Reorganize the SwConnector class
2. Raise the error if the short name of rootSwCompositionPrototype
3. To support NvProvideComSpec
4. Fix the duplicate short name of ARPackage and Other ARElements

### Version 1.8.4

1. To Support the following AR Element:
   - BSW-SYNCHRONOUS-SERVER-CALL-POINT
   - RETURN-TYPE
2. Add the armodel-uuid-checker cli
3. Remove the space in the boolean type

### Version 1.8.3

1. To support the SHORT-LABEL for VALUE
2. To Support the following AR Element:
   - MAX-DELTA-COUNTER-INIT
   - MAX-NO-NEW-OR-REPEATED-DATA
   - USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS
   - MASK

### Version 1.8.2

1. Fix the AUTOSAR XML schema issue

### Version 1.8.1

1. To support the following AR Element:
   - MODE-DECLARATION-MAPPING-SET
   - MODE-INTERFACE-MAPPING
   - ECUC-MODULE-DEF
   - DOC-REVISION
   - ECUC-PARAM-CONF-CONTAINER-DEF
   - ECUC-BOOLEAN-PARAM-DEF
   - ECUC-STRING-PARAM-DEF
   - ECUC-INTEGER-PARAM-DEF
   - ECUC-FLOAT-PARAM-DEF
   - ECUC-ENUMERATION-PARAM-DEF
2. Same short name with different type can be added and located

### Version 1.8.0

1. To support the following AR Element:
   - DLT-USER-NEEDS
2. Improve the UUID check
3. Improve the find method of class AbstractAUTOSAR to support the validation of dest
4. Add the findXXX method of class AbstractAUTOSAR
   - findAtomicSwComponentType
   - findSystemSignal
   - findSystemSignalGroup
   - findPort
   - findVariableDataPrototype
   - findImplementationDataType

### Version 1.7.9

1. To improve the following AR Element
   - BSW-MODULE-DESCRIPTION
   - BSW-INTERNAL-BEHAVIOR
   - LIFE-CYCLE-INFO-SET
   - PHYSICAL-DIMENSION
2. To support the following AR Element:
   - ACTIVATION-POINTS
   - CALL-POINTS
   - LIFE-CYCLE-INFO
   - COLLECTION
   - KEYWORD-SET
   - FIGURE
   - CLIENT-SERVER-INTERFACE-MAPPING
   - DTC-STATUS-CHANGE-NOTIFICATION-NEEDS
3. Add the test case for AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
4. Add the API to set the autosar release version and correct schema will be set (AUTOSAR::setARRelease())
5. Fix the conversion for float number in scientific notation

### Version 1.7.8

1. To support the following AR Element:
   - STATIC-MEMORYS
   - RECEPTION-POLICYS
   - VENDOR-API-INFIX
   - INCLUDED-MODE-DECLARATION-GROUP-SET
   - HW-ELEMENT
   - FLEXRAY-FRAME
   - TYPE-MAPPING
   - DATA-TRANSFORMATION-SET
   - FLEXRAY-COMMUNICATION-CONTROLLER
   - FLEXRAY-COMMUNICATION-CONNECTOR
   - FLEXRAY-PHYSICAL-CHANNEL
   - FLEXRAY-CLUSTER
   - BSW-OPERATION-INVOKED-EVENT
2. Improve the following AR Element
   - SW-DATA-DEF-PROPS
   - SW-RECORD-LAYOUT-GROUP
   - BSW-MODULE-DESCRIPTION
   - BSW-CALLED-ENTITY
   - BSW-SCHEDULABLE-ENTITY
   - SW-SERVICE-ARG
   - RUNNABLE-ENTITY
   - I-SIGNAL-GROUP
   - END-TO-END-PROTECTION
   - BSW-INTERNAL-TRIGGER-OCCURRED-EVENT
3. Fix the following AR Element
   - PROVIDED-MODE-GROUPS
   - MANAGED-MODE-GROUPS
4. Enable the Flake8 - Fix the Flake8 issues
5. Add the CompositionSwComponentType in the AUTOSAR root model
6. Add the duplicate UUID check

### Version 1.7.7

1. To support the following AR Element:
   - UDP-NM-CLUSTER
   - UDP-NM-CLUSTER-COUPLING
   - NM-IF-ECUS
   - UDP-NM-ECU
   - TRANSMISSION-MODE-FALSE-TIMING
   - SECURED-I-PDU
   - MULTIPLEXED-I-PDU
   - NM-PDU
   - SECURE-COMMUNICATION-PROPS-SET
   - SO-AD-ROUTING-GROUP
   - ECU-RESOURCE-MAPPINGS
   - SW-IMPL-MAPPINGS
   - CAN-TP-CONFIG
   - DO-IP-TP-CONFIG
   - LIN-TP-CONFIG
   - BSW-BACKGROUND-EVENT
   - BSW-DATA-RECEIVED-EVENT
   - BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT
   - MODE-SWITCHED-ACK-EVENT
   - BACKGROUND-EVENT
2. Improve the following AR Element
   - ETHERNET-COMMUNICATION-CONNECTOR
   - ECU-INSTANCE
   - CAN-NM-NODE
   - NM-NODE
   - SDG
   - DATA-FILTER
   - USER-DEFINED-PDU
   - APPLICATION-ARRAY-DATA-TYPE
   - MODE-SWITCH-SENDER-COM-SPEC
3. Access the RootSwCompositionPrototype directly from AUTOSAR instance
4. Create the mapping for Implementation and InternalBehavior
5. Improve the Identifiable::setCategory with Raw String

### Version 1.7.6

1. To support the following AR Element:
   - PROVIDED-SERVICE-INSTANCE
   - MAC-MULTICAST-GROUP
   - ASSOCIATED-COM-I-PDU-GROUP-REF
   - CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS
   - CAN-CONTROLLER-FD-REQUIREMENTS
2. Improve the following AR Element
   - AR-PACKAGE
   - LIN-TP-CONFIG
   - DIAGNOSTIC-SERVICE-TABLE
   - LIN-MASTER
   - IMPLEMENTATION-DATA-TYPE
   - ETHERNET-COMMUNICATION-CONTROLLER
   - I-SIGNAL-PORT
   - SYMBOL-PROPS
   - I-PDU-PORT
3. Fix the following AR Element
   - I-PDU-MAPPING

### Version 1.7.5

1. To support the following AR Element:
   - DIAGNOSTIC-CONNECTION
   - DIAGNOSTIC-SERVICE-TABLE
   - LIN-MASTER
   - LIN-COMMUNICATION-CONNECTOR
   - UDP-NM-CLUSTER
   - UDP-NM-NODE
   - MULTIPLEXED-I-PDU
   - USER-DEFINED-I-PDU
   - USER-DEFINED-PDU
   - GENERAL-PURPOSE-I-PDU
   - GENERAL-PURPOSE-PDU
   - SECURE-COMMUNICATION-PROPS-SET
   - SO-AD-ROUTING-GROUP
   - BUS-OFF-RECOVERY
   - SCHEDULE-TABLES
   - INFRASTRUCTURE-SERVICES
   - GENERIC-TP
   - TCP-TP
   - UDP-TP
   - CONSUMED-SERVICE-INSTANCES
2. Fix the following AR Element
   - SW-RECORD-LAYOUT-V-AXIS
   - SW-RECORD-LAYOUT-GROUP-AXIS
3. Improve the following AR Element
   - SOCKET-CONNECTION
   - SOCKET-ADDRESS

### Version 1.7.4

1. To support the following AR Element:
   - DIAGNOSTIC-EVENT-INFO-NEEDS
   - AR-TYPED-PER-INSTANCE-MEMORYS
   - USED-DATA-ELEMENT
   - ETHERNET-COMMUNICATION-CONTROLLER
   - ETHERNET-COMMUNICATION-CONNECTOR
   - ETHERNET-PHYSICAL-CHANNEL
   - PHYSICAL-PROPS
   - SO-AD-CONFIG
2. To improve the following AR Element:
   - MODE-SWITCH-RECEIVER-COM-SPEC
   - APPLICATION-ARRAY-DATA-TYPE

### Version 1.7.3

1. To support the following AR Element:
   - MEM-CLASS-SYMBOL
   - ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS
   - STEP-SIZE
   - BSW-INTERRUPT-ENTITY
   - FLAT-MAP
   - VARIABLE-AND-PARAMETER-INTERFACE-MAPPING
   - PORT-INTERFACE-MAPPING-SET
   - DATA-MAPPINGS
   - ECU-STATE-MGR-USER-NEEDS
   - STACK-USAGES
   - ROUGH-ESTIMATE-STACK-USAGE
2. To improve the following AR Element:
   - PARAMETER-INTERFACE

### Version 1.7.2

1. Fix the invalidationPolicy of SenderReceiverInterface cannot be written in ARXML
2. To support the following AR Element:
   - SW-ADDR-METHOD
   - DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS
   - DIAGNOSTIC-ROUTINE-NEEDS
   - DIAGNOSTIC-VALUE-NEEDS
   - DIAGNOSTIC-EVENT-NEEDS
   - CRYPTO-SERVICE-NEEDS
   - DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL
   - ROLE-BASED-DATA-TYPE-ASSIGNMENT
   - ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT
   - PR-PORT-PROTOTYPE

### Version 1.7.1

1. To support the following AR Element:
   - INTRODUCTION
   - LIST
   - SW-INTENDED-RESOLUTION
   - REFERENCE-BASE

### Version 1.7.0

1. To support the following AR Element:
   - SWC-TO-ECU-MAPPING
   - SW-MAPPINGS
   - ROOT-SOFTWARE-COMPOSITIONS
   - SPEED
   - ECU-INSTANCE
   - COMM-CONTROLLERS
   - CAN-COMMUNICATION-CONNECTOR
   - I-PDU-TIMING
   - DATA-FILTER
   - EVENT-CONTROLLED-TIMING

### Version 1.6.4

1. Refactor the Implementation
2. Fix the Binary value
3. Refactor the SwComponentType

### Version 1.6.3

1. Change the Package structure according to AUTOSAR standard

### Version 1.6.2

1. Change the AUTOSAR.clear() to AUTOSAR.new()
2. Fix the several refactor methods issue

### Version 1.6.1

1. Organize the armodel package
2. Add the Get/Set method for several class

### Version 1.6.0

1. Add the annotation support for the Identifiable class
2. Ecuc:
   - EcucValueCollection
   - EcucModuleConfigurationValues
   - EcucContainerValue
   - EcucParameterValue
   - EcucAbstractReferenceValue
3. To support the following AR Element:
   - I-SIGNAL-GROUP
   - I-SIGNAL-I-PDU-GROUP
   - NM-CONFIG
   - NM-NODE
   - NM-CLUSTER
   - CAN-NM-MODE
   - NM-ECU
   - SECURED-I-PDU
   - MODE-SWITCH-POINTS
4. Create the CLI (armodel-system-signal) to list all the system signals

### Version 1.5.0

1. Fix the old ARElement
   - InitEvent
   - SwcTiming
   - ConstantMemory
   - ModeSwitchReceiverComSpec
   - MODE-ACCESS-POINTS
2. Add the timestamp to following ARElement
   - AUTOSAR-VARIABLE-IREF
   - MODE-REQUEST-TYPE-MAP
3. Timing Extension
   - TIMING-REQUIREMENTS
   - EXECUTION-ORDER-CONSTRAINT
   - EOC-EXECUTABLE-ENTITY-REF
4. Communication
   - LIN-CLUSTER
   - NM-PDU
   - LIN-UNCONDITIONAL-FRAME
   - CAN-FRAME
   - GATEWAY
   - I-SIGNAL

### Version 1.4.3

1. Support to write the AUTOSAR model to arxml file
   - BswCalledEntity
   - BswSchedulableEntity
   - BswImplementation
   - ServiceSwComponentType
   - DataTypeMappingSet
   - ModeRequestTypeMap
   - PortInterface
   - ModeInterface
2. Support ot read the AUTOSAR model to arxml file
   - ServiceSwComponentType
   - ModeRequestTypeMap
   - PortInterface
   - ModeInterface
3. Refactor the Base ARType
   - ARFloat
   - ARNumerical
   - ARLiteral
4. Fix Issue #22 - raise wrong Exception: Invalid ResourceConsumption of Implementation

### Version 1.4.2

1. Support to read the AUTOSAR model from arxml file
   - EndToEndProtectionSet
   - EndToEndProtection
   - EndToEndProtectionVariablePrototype
   - EndToEndDescription
   - ApplicationArrayDataType
   - SwRecordLayout
   - SwCalprmAxisSet
   - SwCalprmAxis
   - ApplicationArrayElement
   - ApplicationRecordElement
   - SwRecordLayoutGroup
   - SwRecordLayoutGroupContent
2. Support to write the AUTOSAR model to arxml file
   - EndToEndProtectionSet
   - EndToEndProtection
   - EndToEndProtectionVariablePrototype
   - EndToEndDescription
   - ApplicationArrayDataType
   - SwRecordLayout
   - SwCalprmAxisSet
   - SwCalprmAxis
   - ApplicationArrayElement
   - ApplicationRecordElement
   - SwRecordLayoutGroup
   - SwRecordLayoutGroupContent
   - ImplementationDataType

### Version 1.4.1

1. Support to read the AUTOSAR model from arxml file
   - ServerComSpec
   - PerInstanceMemory
   - PortDefinedArgumentValue
   - DataWriteAccesses
   - NvBlockNeeds
   - CompositeNetworkRepresentation
   - PortGroup
2. Support to write the AUTOSAR model to arxml file
   - ServerComSpec
   - PerInstanceMemory
   - ServerCallPoint
   - ReadLocalVariable
   - WrittenLocalVariable
   - PortDefinedArgumentValue
   - RVariableInAtomicSwcInstanceRef
   - DataWriteAccesses
   - NvBlockNeeds
   - RecordValueSpecification
   - CompositeNetworkRepresentation
   - PortGroup
3. Move the ARPackage from the Elements

### Version 1.4.0

1. Support to write the AUTOSAR model to arxml file
   - ARPackage
   - CompositionSwComponent
   - CompuMethod
   - DataConstr
   - Unit
2. Support to read the AUTOSAR model from arxml file
   - ConstantSpecification
   - DataConstr
   - Unit

### Version 1.3.0

1. List all the SwComponentType
2. Support to parse the DelegationSwConnector
3. Correct the class definitions of PPortInCompositionInstanceRef and RPortInCompositionInstanceRef

### Version 1.2.0

1. Add the SwcImplementation support
2. Add the integer value for memory section alignment
3. Remove the required attributes for the Implementation according to the AUTOSAR standard 23R-11
4. Change the START-ON-EVENT-REF to optional according to the AUTOSAR standard 23R-11
5. Change the HANDLE-OUT-OF-RANGE to optional according to the AUTOSAR standard 23R-11
6. Add the SensorActuatorSwComponentType support
7. Change the CATEGORY of COMPU-METHOD to optional
8. Change the CAN-BE-INVOKED-CONCURRENTLY to optional

### Version 1.1.0

1. Add the InitEvent support
2. Add the DataReceiveEvent support
3. Add the SwcModeSwitchEvent support

### Version 1.0.0

1. Add the logging support
2. Add the <warning> option to disable exception raised
3. Add the BswMD support

### Version 0.1.3

Fix the attribute intervalType of Limit is empty issue

### Version 0.1.2

Add the AsynchronousServerCallPoint support for ARXML

### Version 0.1.1

Add the ARRAY category support for ImplementationDataType

## Project Structure

### AUTOSAR M2 Meta-model

```
- ARObject
  - Referrable
    - MultilanguageReferrable
      - Identifiable
        - PackageableElement
          - ARElement
            - AtpType
              - AutosarDataType
              - PortInterface
                - DataInterface
                  - NvDataInterface
                  - ParameterInterface
                  - SenderReceiverInterface
            - BswModuleEntry
            - EndToEndProtectionSet
          - Implementation
            - BswImplementation
        - AtpFeature
          - AtpPrototype
            - AtpPrototype
              - DataPrototype
                - AutosarDataPrototype
                  - VariableDataPrototype
                - ApplicationCompositeElementDataPrototype
                  - ApplicationArrayElement
                  - ApplicationRecordElement
          - AtpStructureElement
            - BswModuleDescription
        - ExecutableEntity
        - SwcBswMapping
        - PortPrototype
          - AbstractProvidedPortPrototype
            - PPortPrototype
          - AbstractRequiredPortPrototype
            - RPortPrototype
  - ValueSpecification
    - ConstantReference
```

### Package Organization

```
src/armodel/
├── models/M2/                 # AUTOSAR M2 meta-model
│   ├── MSR/                   # Meta-model semantic rules
│   └── AUTOSARTemplates/      # AUTOSAR template models
│       ├── AutosarTopLevelStructure
│       ├── CommonStructure
│       ├── SWComponentTemplate
│       ├── SystemTemplate
│       ├── BswModuleTemplate
│       ├── ECUCDescriptionTemplate
│       └── ...
├── parser/                    # ARXML parsing
├── writer/                    # ARXML writing
├── cli/                       # Command-line tools
├── lib/                       # Library utilities
└── transformer/               # Data transformation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Links

- **AUTOSAR**: https://www.autosar.org/
- **GitHub**: http://github.com/melodypapa/py-armodel
- **PyPI**: https://pypi.org/project/armodel/
- **Docs**: https://py-armodel.readthedocs.io/