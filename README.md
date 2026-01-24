# 1. py-armodel

## 1.1. Purpose

To support AUTOSAR model with python 

## 1.2. Reference Documents
1. AUTOSAR_TPS_XMLSchemaProductionRules.pdf
2. AUTOSAR_TPS_ARXMLSerializationRules.pdf

|Version|Documentation|Travis CI|Coverage Status|Pypi|
|--|--|--|--|--|
|[![GitHub version](https://badge.fury.io/gh/melodypapa%2Fpy-armodel.svg)](https://badge.fury.io/gh/melodypapa%2Fpy-armodel)|[![Documentation Status](https://readthedocs.org/projects/py-armodel/badge/?version=latest)](https://py-armodel.readthedocs.io/en/latest)|[![](https://www.travis-ci.com/melodypapa/py-armodel.svg?branch=main)](https://www.travis-ci.com/melodypapa/py-armodel)|[![Coverage Status](https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main)](https://coveralls.io/github/melodypapa/py-armodel?branch=main)|[![PyPI version](https://badge.fury.io/py/armodel.svg)](https://badge.fury.io/py/armodel)|

## 1.3. How to create the distribution and upload to pypi
1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

## 1.4. How to perform Tests

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

* Run `pip install pytest pytest-cov` to install pytest
* Run `pytest --cov=armodel --cov-report term-missing` to verify all the functionality
* Run `pytest tests/test_armodel/` to run only unit tests
* Run `pytest tests/integration_tests/ -s` to run integration tests with progress output

## 1.5. Integration Tests

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

## 1.6. Usage Guidelines

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

* Run `python setup.py sdist bdist_wheel --universal`

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

## 1.10. CLI usages

### 1.10.1. arxml-dump

**Dump all the arxml data to screen**


`arxml-dump --arxml arg -h`

--arxml arg     The file name of arxml data
-h              show the help information

#### 1.10.1.1. arxml-dump usage

**Dump the arxml data from test1.arxml and test2.arxml**

```
$arxml-dump --arxml test1.arxml --arxml test2.arxml
```

### 1.10.2. arxml-swc

**List all the SwComponentType in the autosar model**

usage: swc-list [-h] [-v] [-f FORMAT] [--filter FILTER] Input [Input ...]

-h, --help          show the help message and exit
-v, --verbose       Print debug information
-f FORMAT, --format FORMAT
                    Specify the short or long name of Sw-C. 
                      *short* : only print the short name of SWComponentType
                      *long*  : print the SWComponentType with ARPackage names
--filter FILTER     Set the filter condition. 
                      *CompositionSwComponent* : Print the CompositionSwComponent only.


#### 1.10.2.1. List all the SW-Components in the specific path

```
$arxml-swc <arxml_folder>
```

#### 1.10.2.2. List all the CompositionSwComponent with the long name

```
$arxml-swc --format long --filter CompositionSwComponent <arxml_folder> 
```

### 1.10.3. connector2xlsx

**Export all the SwConnector (AssemblySwConnector, DelegationSwConnector) to excel file**

```
$connector2xlsx src/armodel/tests/test_files/SoftwareComponents.arxml data/SoftwareComponents.xlsx
```

### 1.10.4. connector-update

**Update all the SwConnector (AssemblySwConnector, DelegationSwConnector) from excel file**

```
$connector-update src/armodel/tests/test_files/SoftwareComponents.arxml data/SoftwareComponents.xlsx data/Test.arxml
```


## 1.11. API

### 1.11.1. Constructor

```
  ARXMLParser(options={"warning": True})
```

## 1.12. Change notes:

**Version 1.9.0**

1. **Testing Infrastructure**
   * Add comprehensive integration test suite with round-trip validation
   * Add test runner script (`scripts/run_tests.py`) with colored output
   * Add pytest configuration (`pytest.ini`) with custom markers
   * Support 2205+ unit tests and 29 integration test files
   * Add coverage reporting (HTML and terminal)

2. **Integration Tests**
   * Round-trip testing: Parse → Write → Re-parse → Compare
   * Tests all 29 ARXML files in `test_files/` directory
   * Auto-detects AUTOSAR version from XSD schema (4.0.3 to R24-11)
   * Verbose progress tracking with step-by-step feedback
   * Extensible configuration via YAML for additional test directories

3. **Documentation**
   * Add integration test design document
   * Add integration test README with usage examples
   * Update CLAUDE.md with test runner documentation

4. **Developer Experience**
   * Unified test runner for both unit and integration tests
   * Colored console output (success/failure/warning)
   * Test summary with pass/fail/skip statistics
   * Support for category-based test selection

**Version 0.1.1**

Add the ARRAY category support for ImplementationDataType

**Version 0.1.2**

Add the AsynchronousServerCallPoint support for ARXML

**Version 0.1.3**

Fix the attribute intervalType of **Limit** is empty issue.

**Version 1.0.0**

1. Add the logging support
2. Add the <warning> option to disable exception raised.
3. Add the BswMD support

**Version 1.1.0**

1. Add the InitEvent support. (Issue #5)
2. Add the DataReceiveEvent support. (Issue #5)
3. Add the SwcModeSwitchEvent support. (Issue #5)

**Version 1.2.0**

1. Add the SwcImplementation support (Issue #9)
2. Add the integer value for memory section alignment (Issue #9)
3. Remove the required attributes for the Implementation according to the AUTOSAR standard 23R-11. (Issue #9)
4. Change the START-ON-EVENT-REF to optional according to the AUTOSAR standard 23R-11. (Issue #9)
5. Change the HANDLE-OUT-OF-RANGE to optional according to the AUTOSAR standard 23R-11. (Issue #9)
6. Add the SensorActuatorSwComponentType support (Issue #9)
7. Change the CATEGORY of COMPU-METHOD to optional.
8. Change the CAN-BE-INVOKED-CONCURRENTLY to optional.

**Version 1.3.0**

1. List all the SwComponentType (Issue #11)
2. Support to parse the DelegationSwConnector (Issue #12)
3. Correct the class definitions of PPortInCompositionInstanceRef and RPortInCompositionInstanceRef. (Issue #12)

**Version 1.4.0**

1. Support to write the AUTOSAR model to arxml file (Issue #17)
   * ARPackage
   * CompositionSwComponent
   * CompuMethod
   * DataConstr
   * Unit
2. Support to read the AUTOSAR model from arxml file (Issue #17)
   * ConstantSpecification
   * DataConstr
   * Unit

**Version 1.4.1**

1. Support to read the AUTOSAR model from arxml file (Issue #19)
   * ServerComSpec
   * PerInstanceMemory
   * PortDefinedArgumentValue
   * DataWriteAccesses
   * NvBlockNeeds
   * CompositeNetworkRepresentation
   * PortGroup
2. Support to write the AUTOSAR model to arxml file (Issue #19)
   * ServerComSpec
   * PerInstanceMemory
   * ServerCallPoint
   * ReadLocalVariable
   * WrittenLocalVariable
   * PortDefinedArgumentValue
   * RVariableInAtomicSwcInstanceRef
   * DataWriteAccesses
   * NvBlockNeeds
   * RecordValueSpecification
   * CompositeNetworkRepresentation
   * PortGroup
3. Move the ARPackage from the Elements.

**Version 1.4.2**

1. Support to read the AUTOSAR model from arxml file (Issue #23)
   * EndToEndProtectionSet
   * EndToEndProtection
   * EndToEndProtectionVariablePrototype
   * EndToEndDescription
   * ApplicationArrayDataType
   * SwRecordLayout
   * SwCalprmAxisSet
   * SwCalprmAxis
   * ApplicationArrayElement
   * ApplicationArrayDataType
   * SwRecordLayoutGroup
   * SwRecordLayoutGroupContent
2. Support to write the AUTOSAR model to arxml file (Issue #23)
   * EndToEndProtectionSet
   * EndToEndProtection
   * EndToEndProtectionVariablePrototype
   * EndToEndDescription
   * ApplicationArrayDataType
   * SwRecordLayout
   * SwCalprmAxisSet
   * SwCalprmAxis
   * ApplicationArrayElement
   * ApplicationArrayDataType
   * SwRecordLayoutGroup
   * SwRecordLayoutGroupContent
   * ImplementationDataType

**Version 1.4.3**

1. Support to write the AUTOSAR model to arxml file (Issue #25)
   * BswCalledEntity
   * BswSchedulableEntity
   * BswImplementation
   * ServiceSwComponentType
   * DataTypeMappingSet
   * ModeRequestTypeMap
   * PortInterface
   * ModeInterface
2. Support ot read the AUTOSAR model to arxml file (Issue #25)
   * ServiceSwComponentType
   * ModeRequestTypeMap
   * PortInterface
   * ModeInterface
3. Refactor the Base ARType
   * ARFloat
   * ARNumerical
   * ARLiteral
4. Fix Issue #22 - raise wrong Exception: Invalid ResourceConsumption of Implementation

**Version 1.5.0**

1. Fix the old ARElement (Issue #27)
   * InitEvent
   * SwcTiming
   * ConstantMemory
   * ModeSwitchReceiverComSpec
   * MODE-ACCESS-POINTS
2. Add the timestamp to following ARElement (Issue #27)
   * AUTOSAR-VARIABLE-IREF
   * MODE-REQUEST-TYPE-MAP
3. Timing Extension  (Issue #27)
   * TIMING-REQUIREMENTS
   * EXECUTION-ORDER-CONSTRAINT
   * EOC-EXECUTABLE-ENTITY-REF
4. Communication (Issue #27)
   * LIN-CLUSTER
   * NM-PDU
   * LIN-UNCONDITIONAL-FRAME
   * CAN-FRAME
   * GATEWAY
   * I-SIGNAL

**Version 1.6.0**

1. Add the annotation support for the Identifiable class. (Issue #29)
2. Ecuc (Issue #29)
   * EcucValueCollection
   * EcucModuleConfigurationValues
   * EcucContainerValue
   * EcucParameterValue
   * EcucAbstractReferenceValue
3. To support the following AR Element:
   * I-SIGNAL-GROUP
   * I-SIGNAL-I-PDU-GROUP
   * NM-CONFIG
   * NM-NODE
   * NM-CLUSTER
   * CAN-NM-MODE
   * NM-ECU
   * SECURED-I-PDU
   * MODE-SWITCH-POINTS
 4. Create the CLI (armodel-system-signal) to list all the system signals

**Version 1.6.1**

1. Organize the armodel package.
2. Add the Get/Set method for several class.

**Version 1.6.2**

1. Change the AUTOSAR.clear() to AUTOSAR.new().
2. Fix the several refactor methods issue.

**Version 1.6.3**

1. Change the Package structure according to AUTOSAR standard.

**Version 1.6.4**

1. Refactor the Implementation.
2. Fix the Binary value
3. Refactor the SwComponentType.

**Version 1.7.0**

1. To support the following AR Element:
   * SWC-TO-ECU-MAPPING
   * SW-MAPPINGS
   * ROOT-SOFTWARE-COMPOSITIONS
   * SPEED
   * ECU-INSTANCE
   * COMM-CONTROLLERS
   * CAN-COMMUNICATION-CONNECTOR
   * I-PDU-TIMING
   * DATA-FILTER
   * EVENT-CONTROLLED-TIMING

**Version 1.7.1**

1. To support the following AR Element:
   * INTRODUCTION
   * LIST
   * SW-INTENDED-RESOLUTION
   * REFERENCE-BASE
  
**Version 1.7.2**

1. Fix the invalidationPolicy of SenderReceiverInterface cannot be written in ARXML
2. To support the following AR Element:
   * SW-ADDR-METHOD
   * DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS
   * DIAGNOSTIC-ROUTINE-NEEDS
   * DIAGNOSTIC-VALUE-NEEDS
   * DIAGNOSTIC-EVENT-NEEDS
   * CRYPTO-SERVICE-NEEDS
   * DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL
   * ROLE-BASED-DATA-TYPE-ASSIGNMENT
   * ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT
   * PR-PORT-PROTOTYPE

**Version 1.7.3**

1. To support the following AR Element:
   * MEM-CLASS-SYMBOL
   * ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS
   * STEP-SIZE
   * BSW-INTERRUPT-ENTITY
   * FLAT-MAP
   * VARIABLE-AND-PARAMETER-INTERFACE-MAPPING
   * PORT-INTERFACE-MAPPING-SET
   * DATA-MAPPINGS
   * ECU-STATE-MGR-USER-NEEDS
   * STACK-USAGES
   * ROUGH-ESTIMATE-STACK-USAGE
2. To improve the following AR Element:
   * PARAMETER-INTERFACE

**Version 1.7.4**

1. To support the following AR Element:
   * DIAGNOSTIC-EVENT-INFO-NEEDS
   * AR-TYPED-PER-INSTANCE-MEMORYS
   * USED-DATA-ELEMENT
   * ETHERNET-COMMUNICATION-CONTROLLER
   * ETHERNET-COMMUNICATION-CONNECTOR
   * ETHERNET-PHYSICAL-CHANNEL
   * PHYSICAL-PROPS
   * SO-AD-CONFIG
2. To improve the following AR Element:
   * MODE-SWITCH-RECEIVER-COM-SPEC
   * APPLICATION-ARRAY-DATA-TYPE

**Version 1.7.5**

1. To support the following AR Element:
   * DIAGNOSTIC-CONNECTION
   * DIAGNOSTIC-SERVICE-TABLE
   * LIN-MASTER
   * LIN-COMMUNICATION-CONNECTOR
   * UDP-NM-CLUSTER
   * UDP-NM-NODE
   * MULTIPLEXED-I-PDU
   * USER-DEFINED-I-PDU
   * USER-DEFINED-PDU
   * GENERAL-PURPOSE-I-PDU
   * GENERAL-PURPOSE-PDU
   * SECURE-COMMUNICATION-PROPS-SET
   * SO-AD-ROUTING-GROUP
   * BUS-OFF-RECOVERY
   * SCHEDULE-TABLES
   * INFRASTRUCTURE-SERVICES
   * GENERIC-TP
   * TCP-TP
   * UDP-TP
   * CONSUMED-SERVICE-INSTANCES
2. Fix the following AR Element
   * SW-RECORD-LAYOUT-V-AXIS
   * SW-RECORD-LAYOUT-GROUP-AXIS
3. Improve the following AR Element
   * SOCKET-CONNECTION
   * SOCKET-ADDRESS

**Version 1.7.6**

1. To support the following AR Element:
   * PROVIDED-SERVICE-INSTANCE
   * MAC-MULTICAST-GROUP
   * ASSOCIATED-COM-I-PDU-GROUP-REF
   * CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS
   * CAN-CONTROLLER-FD-REQUIREMENTS
2. Improve the following AR Element
   * AR-PACKAGE
   * LIN-TP-CONFIG
   * DIAGNOSTIC-SERVICE-TABLE
   * LIN-MASTER
   * IMPLEMENTATION-DATA-TYPE
   * ETHERNET-COMMUNICATION-CONTROLLER
   * I-SIGNAL-PORT
   * SYMBOL-PROPS
   * I-PDU-PORT
3. Fix the following AR Element
   * I-PDU-MAPPING

**Version 1.7.7**

1. To support the following AR Element:
   * UDP-NM-CLUSTER
   * UDP-NM-CLUSTER-COUPLING
   * NM-IF-ECUS
   * UDP-NM-ECU
   * TRANSMISSION-MODE-FALSE-TIMING
   * SECURED-I-PDU
   * MULTIPLEXED-I-PDU
   * NM-PDU
   * SECURE-COMMUNICATION-PROPS-SET
   * SO-AD-ROUTING-GROUP
   * ECU-RESOURCE-MAPPINGS
   * SW-IMPL-MAPPINGS
   * CAN-TP-CONFIG
   * DO-IP-TP-CONFIG
   * LIN-TP-CONFIG
   * BSW-BACKGROUND-EVENT
   * BSW-DATA-RECEIVED-EVENT
   * BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT
   * MODE-SWITCHED-ACK-EVENT
   * BACKGROUND-EVENT
2. Improve the following AR Element
   * ETHERNET-COMMUNICATION-CONNECTOR
   * ECU-INSTANCE
   * CAN-NM-NODE
   * NM-NODE
   * SDG
   * DATA-FILTER
   * USER-DEFINED-PDU
   * APPLICATION-ARRAY-DATA-TYPE
   * MODE-SWITCH-SENDER-COM-SPEC

3. Access the RootSwCompositionPrototype directly from AUTOSAR instance 
4. Create the mapping for Implementation and InternalBehavior
   * AUTOSAR::getBehavior()
   * AUTOSAR::getImplementation()
5. Improve the Identifiable::setCategory with Raw String

**Version 1.7.8**

1. To support the following AR Element:
   * STATIC-MEMORYS
   * RECEPTION-POLICYS
   * VENDOR-API-INFIX
   * INCLUDED-MODE-DECLARATION-GROUP-SET
   * HW-ELEMENT
   * FLEXRAY-FRAME
   * TYPE-MAPPING
   * DATA-TRANSFORMATION-SET
   * FLEXRAY-COMMUNICATION-CONTROLLER
   * FLEXRAY-COMMUNICATION-CONNECTOR
   * FLEXRAY-PHYSICAL-CHANNEL
   * FLEXRAY-CLUSTER
   * BSW-OPERATION-INVOKED-EVENT
2. Improve the following AR Element
   * SW-DATA-DEF-PROPS
   * SW-RECORD-LAYOUT-GROUP
   * BSW-MODULE-DESCRIPTION
   * BSW-CALLED-ENTITY
   * BSW-SCHEDULABLE-ENTITY
   * SW-SERVICE-ARG
   * RUNNABLE-ENTITY
   * I-SIGNAL-GROUP
   * END-TO-END-PROTECTION
   * BSW-INTERNAL-TRIGGER-OCCURRED-EVENT
3. Fix the following AR Element
   * PROVIDED-MODE-GROUPS
   * MANAGED-MODE-GROUPS 
4. Enable the Flake8 
   * Fix the Flake8 issues
5. Add the CompositionSwComponentType in the AUTOSAR root model.
   * AbstractAUTOSAR::getCompositionSwComponentTypes
   * AbstractAUTOSAR::getCompositionSwComponentType
   * AbstractAUTOSAR::addCompositionSwComponentType
6. Add the duplicate UUID check

**Version 1.7.9**

1. To improve the following AR Element
   * BSW-MODULE-DESCRIPTION
   * BSW-INTERNAL-BEHAVIOR
   * LIFE-CYCLE-INFO-SET
   * PHYSICAL-DIMENSION
2. To support the following AR Element:
   * ACTIVATION-POINTS
   * CALL-POINTS
   * LIFE-CYCLE-INFO
   * COLLECTION
   * KEYWORD-SET
   * FIGURE
   * CLIENT-SERVER-INTERFACE-MAPPING
   * DTC-STATUS-CHANGE-NOTIFICATION-NEEDS
3. Add the test case for
   * AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
4. Add the API to set the autosar release version and correct schema will be set.
   * AUTOSAR::setARRelease()
5. Fix the conversion for float number in scientific notation.

**Version 1.8.0**

1. To support the following AR Element:
   * DLT-USER-NEEDS
2. Improve the UUID check
3. Improve the find method of class AbstractAUTOSAR to support the validation of dest
4. Add the findXXX method of class AbstractAUTOSAR
   * findAtomicSwComponentType
   * findSystemSignal
   * findSystemSignalGroup
   * findPort
   * findVariableDataPrototype
   * findImplementationDataType

**Version 1.8.1**

1. To support the following AR Element:
   * MODE-DECLARATION-MAPPING-SET
   * MODE-INTERFACE-MAPPING
   * ECUC-MODULE-DEF
   * DOC-REVISION
   * ECUC-PARAM-CONF-CONTAINER-DEF
   * ECUC-BOOLEAN-PARAM-DEF
   * ECUC-STRING-PARAM-DEF
   * ECUC-INTEGER-PARAM-DEF
   * ECUC-FLOAT-PARAM-DEF
   * ECUC-ENUMERATION-PARAM-DEF
2. Same short name with different type can be added and located.

**Version 1.8.2**

1. Fix the AUTOSAR XML schema issue

**Version 1.8.3**

1. To support the SHORT-LABEL for VALUE
2. To Support the following AR Element:
   * MAX-DELTA-COUNTER-INIT
   * MAX-NO-NEW-OR-REPEATED-DATA
   * USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS
   * MASK

**Version 1.8.4**

1. To Support the following AR Element:
   * BSW-SYNCHRONOUS-SERVER-CALL-POINT
   * RETURN-TYPE
2. Add the armodel-uuid-checker cli.
3. Remove the space in the boolean type.

**Version 1.8.5**

1. Reorganize the SwConnector class.
2. Raise the error if the short name of rootSwCompositionPrototype.
3. To support the following AR Element:
   * NvProvideComSpec
4. Fix the duplicate short name of ARPackage and Other ARElements. 

**Version 1.8.6**

1. To support the following AR Element:
   * NvProvideComSpec
   * NvRequireComSpec
2. To improve the following AR Element:
   * ParameterAccess

**Version 1.8.7**

1. Correct the base class of the BswEvent.
2. Export the RunnableEntity class.
3. Add the more class support for getDestType