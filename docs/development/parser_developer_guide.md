# ARXML Parser Developer Guide

## Quick Start

### Understanding the Parser Structure

The ARXML parser is organized as a **facade pattern** with specialized parsers:

```
ARXMLParser (main entry point)
    └── delegates to → Specialized Parsers (9 total)
```

### When to Add Code

**Adding a new AUTOSAR element type:**

1. Identify which parser should handle it
2. Add the parsing method to that parser
3. Update the parser registry if needed
4. Write tests

**Example: Adding a new data type**

```python
# In src/armodel/parser/parsers/datatype_parser.py

class DataTypeParser(BaseARXMLParser):
    # ... existing methods ...

    def readMyNewDataType(self, element: ET.Element, data_type: MyNewDataType):
        """Parse MyNewDataType element."""
        self.readIdentifiable(element, data_type)

        # Read specific attributes
        data_type.setSpecialAttribute(
            self.getChildElementOptionalLiteral(element, "SPECIAL-ATTRIBUTE")
        )

        # Read child elements
        for child in self.findall(element, "SUPPORTED-VALUES/*"):
            tag_name = self.getTagName(child)
            if tag_name == "SUPPORTED-VALUE":
                value = self.getChildElementLiteral(child, "VALUE")
                data_type.addSupportedValue(value)
            else:
                self.notImplemented(f"Unsupported element: {tag_name}")
```

## Parser Responsibilities

### CommonStructureParser
**When to use:** Base AUTOSAR attributes, documentation, admin data

**Common methods:**
- `readARObject()` - Basic ARObject attributes (UUID, timestamp)
- `readReferrable()` - Short name
- `readIdentifiable()` - Short name + category + admin data
- `readARElement()` - All Identifiable + ARElement attributes
- `getAdminData()` - AdminData documentation

**Example:**
```python
def readMyElement(self, element: ET.Element, obj: MyElement):
    """Always start with base attributes."""
    self.readIdentifiable(element, obj)  # Sets short-name, category
    # Then add specific behavior
    obj.setMySpecificAttr(...)
```

### DataTypeParser
**When to use:** Data types, compu-methods, units, constraints

**Key methods:**
- `readApplicationPrimitiveDataType()`
- `readImplementationDataType()`
- `readCompuMethod()`
- `readUnit()`
- `readDataConstr()`

**Pattern:**
```python
def readMyDataType(self, element, data_type):
    self.readAutosarDataType(element, data_type)  # Base class setup
    # Add type-specific logic
    data_type.setMyTypeAttribute(...)
```

### PortInterfaceParser
**When to use:** Port interfaces, port prototypes, communication specs

**Key methods:**
- `readSenderReceiverInterface()`
- `readClientServerInterface()`
- `readModeSwitchInterface()`
- `readPPortPrototype()`, `readRPortPrototype()`
- `readNonqueuedSenderComSpec()`, `readNonqueuedReceiverComSpec()`

### ComponentParser
**When to use:** Component types, connectors, component prototypes

**Key methods:**
- `readApplicationSwComponentType()`
- `readAtomicSwComponentType()`
- `readCompositionSwComponentType()`
- `readAssemblySwConnector()`
- `readSwComponentPrototype()`

### BehaviorParser
**When to use:** Internal behaviors, runnables, events, service dependencies

**Key methods:**
- `readSwcInternalBehavior()`
- `readBswInternalBehavior()`
- `readRunnableEntity()`
- RTE Event readers: `readTimingEvent()`, `readDataReceivedEvent()`, etc.
- Service needs: `readNvBlockNeeds()`, `readDiagnosticEventNeeds()`, etc.

### BswModuleParser
**When to use:** BSW module descriptions, entries, behaviors

**Key methods:**
- `readBswModuleDescription()`
- `readBswModuleEntry()`
- `readBswCalledEntity()`, `readBswSchedulableEntity()`
- BSW event readers

### SystemTemplateParser
**When to use:** System, signals, ECU instances, Fibex protocols

**Key methods:**
- `readSystem()`
- `readSystemSignal()`
- `readEcuInstance()`
- Fibex methods: `readCanCluster()`, `readEthernetCluster()`, etc.

### EcucParser
**When to use:** ECUC configuration values and definitions

**Key methods:**
- `readEcucValueCollection()`
- `readEcucContainerValue()`
- `readEcucNumericalParamValue()`, `readEcucTextualParamValue()`
- `readEcucContainerDef()`, `readEcucParamDef()`

### NetworkManagementParser
**When to use:** Network management, transport protocols

**Key methods:**
- `readNmConfig()`, `readNmCluster()`, `readNmNode()`
- `readCanTpConfig()`, `readLinTpConfig()`
- `readEndToEndProtectionSet()`

## Common Patterns

### Reading Collections

```python
# Pattern 1: Using read_collection (from BaseARXMLParser)
def readMyCollection(self, element, parent):
    handler_map = {
        'ITEM-TYPE-A': lambda e: self.readItemTypeA(e, parent.createItemTypeA(...)),
        'ITEM-TYPE-B': lambda e: self.readItemTypeB(e, parent.createItemTypeB(...)),
    }
    self.read_collection(element, "MY-COLLECTION/*", handler_map)

# Pattern 2: Manual iteration
def readMyCollection(self, element, parent):
    for child in self.findall(element, "MY-COLLECTION/*"):
        tag_name = self.getTagName(child)
        if tag_name == "ITEM-TYPE-A":
            item = parent.createItemTypeA(self.getShortName(child))
            self.readItemTypeA(child, item)
        elif tag_name == "ITEM-TYPE-B":
            # ... handle ITEM-TYPE-B
        else:
            self.notImplemented(f"Unsupported element: {tag_name}")
```

### Reading Optional Elements

```python
# Pattern 1: Using read_optional (from BaseARXMLParser)
value = self.read_optional(element, "OPTIONAL-ELEMENT", lambda e: e.text)

# Pattern 2: Manual check
child = self.find(element, "OPTIONAL-ELEMENT")
if child is not None:
    value = self.getChildElementLiteral(child, "VALUE")
    obj.setValue(value)
```

### Reading References

```python
# Optional reference
ref = self.getChildElementOptionalRefType(element, "MY-REF")
obj.setMyRef(ref)

# Required reference
ref = self.getChildElementRefType(obj.getShortName(), element, "MY-REF")
obj.setMyRef(ref)

# Reference list
for ref in self.getChildElementRefTypeList(element, "MY-REFS/MY-REF"):
    obj.addMyRef(ref)
```

### Reading Values

```python
# Different value types
text_value = self.getChildElementOptionalLiteral(element, "TEXT-VALUE")
int_value = self.getChildElementOptionalIntegerValue(element, "INT-VALUE")
float_value = self.getChildElementOptionalFloatValue(element, "FLOAT-VALUE")
bool_value = self.getChildElementOptionalBooleanValue(element, "BOOL-VALUE")
numerical_value = self.getChildElementOptionalNumericalValue(element, "NUMERICAL-VALUE")
```

## Cross-Parser Dependencies

### Calling Other Parsers

Specialized parsers can call other parsers via `_main_parser`:

```python
class BehaviorParser(BaseARXMLParser):
    def __init__(self, options=None, main_parser=None):
        super().__init__(options)
        self._main_parser = main_parser

    def readSwcInternalBehaviorPortAPIOptions(self, element, behavior):
        """Delegate to PortInterfaceParser."""
        for child_element in self.findall(element, "PORT-API-OPTIONS/PORT-API-OPTION"):
            # Access PortInterfaceParser through main parser
            option = self._main_parser._port_interface_parser.readPortAPIOption(...)
            behavior.addPortAPIOption(option)
```

### When to Use _main_parser

✅ **Use when:**
- Accessing methods from another specialized parser
- The method doesn't exist in your parser
- Clear separation of concerns

❌ **Don't use when:**
- The method exists in BaseARXMLParser (use `self.method()` instead)
- Creating circular dependencies
- The functionality belongs in your parser

## Testing Guidelines

### Unit Test Structure

```python
# In tests/test_armodel/parser/parsers/test_my_parser.py

import pytest
import xml.etree.ElementTree as ET
from armodel.parser.parsers.my_parser import MyParser
from armodel.models.M2.AUTOSARTemplates... import MyElementType

class TestMyParser:
    """Test MyParser functionality."""

    def test_read_my_element_basic(self):
        """Test basic MyElement parsing."""
        xml = """
        <MY-ELEMENT>
            <SHORT-NAME>TestElement</SHORT-NAME>
            <CATEGORY>MyCategory</CATEGORY>
        </MY-ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = MyParser()

        obj = MyElementType('Dummy')
        parser.readMyElement(element, obj)

        assert obj.getShortName() == 'TestElement'
        assert obj.getCategory() == 'MyCategory'

    def test_read_my_element_with_optional_child(self):
        """Test MyElement with optional child."""
        # ... test implementation
```

### Integration Test Structure

```python
def test_my_arxml_loading_and_saving(self):
    """Test full round-trip of MY-type ARXML."""
    # Load original file
    parser = ARXMLParser()
    document = AUTOSAR.getInstance()
    document.clear()
    parser.load(get_test_file_path('MyTest.arxml'), document)

    # Save to temp file
    writer = ARXMLWriter()
    writer.write_to_file(document, '/tmp/test_output.arxml')

    # Compare files
    self.compare_xml_files(
        get_test_file_path('MyTest.arxml'),
        '/tmp/test_output.arxml'
    )
```

## Debugging Tips

### Enable Warnings

```python
parser = ARXMLParser(options={"warning": True})
# This will log warnings instead of raising exceptions
# Useful for understanding what's being skipped
```

### Enable Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

parser = ARXMLParser()
# Debug logs will show which elements are being parsed
```

### Check Parser Registry

```python
parser = ARXMLParser()
print(parser._parser_registry.keys())
# Shows all registered tag names → parser mappings
```

## Common Mistakes to Avoid

### 1. Forgetting to Call Base Methods

❌ **Wrong:**
```python
def readMyElement(self, element, obj):
    obj.setSpecificAttr(...)
    # Missing: self.readIdentifiable(element, obj)
```

✅ **Correct:**
```python
def readMyElement(self, element, obj):
    self.readIdentifiable(element, obj)  # Sets short-name, category
    obj.setSpecificAttr(...)
```

### 2. Not Handling Collections

❌ **Wrong:**
```python
def readMyElement(self, element, obj):
    # Only reads first child
    child = self.find(element, "MY-ITEM")
    if child is not None:
        item = obj.createMyItem(self.getShortName(child))
```

✅ **Correct:**
```python
def readMyElement(self, element, obj):
    # Reads ALL children
    for child in self.findall(element, "MY-ITEMS/MY-ITEM"):
        item = obj.createMyItem(self.getShortName(child))
        self.readMyItem(child, item)
```

### 3. Ignoring Namespace Prefixes

❌ **Wrong:**
```python
# Don't hardcode namespaces
ns = {'ar': 'http://autosar.org/schema/r4.0'}
element.find('ar:MY-ELEMENT', ns)
```

✅ **Correct:**
```python
# The parser handles namespaces automatically
self.find(element, "MY-ELEMENT")
```

### 4. Creating Circular Dependencies

❌ **Wrong:**
```python
# ComponentParser calling BehaviorParser directly
from ..parsers.behavior_parser import BehaviorParser

class ComponentParser(BaseARXMLParser):
    def __init__(self):
        self._behavior_parser = BehaviorParser()  # Creates circular import
```

✅ **Correct:**
```python
# Access through _main_parser
class ComponentParser(BaseARXMLParser):
    def __init__(self, options=None, main_parser=None):
        super().__init__(options)
        self._main_parser = main_parser

    def readSomething(self, element, obj):
        # Access BehaviorParser through main
        self._main_parser._behavior_parser.readBehavior(...)
```

## Performance Tips

### 1. Use Collection Methods

```python
# Good: Single pass with handler map
self.read_collection(element, "ITEMS/*", handler_map)

# Avoid: Multiple iterations
for child in self.findall(element, "ITEMS/*"):
    if child.tag == "TYPE-A":
        # ...
    elif child.tag == "TYPE-B":
        # ...
```

### 2. Cache Expensive Operations

```python
def readMyExpensiveMethod(self, element, obj):
    # Cache computed values
    if not hasattr(self, '_cached_value'):
        self._cached_value = self.expensiveOperation()
```

### 3. Avoid Unnecessary Object Creation

```python
# Good: Reuse parser
parser = ARXMLParser()
for file in files:
    parser.parse_from_file(file)  # Reuses same parser

# Avoid: Creating new parser each time
for file in files:
    parser = ARXMLParser()  # Creates new parser unnecessarily
    parser.parse_from_file(file)
```

## Adding New Specialized Parsers

If you need to add a completely new specialized parser:

### 1. Create Parser File

```bash
# In src/armodel/parser/parsers/
touch my_new_parser.py
```

### 2. Implement Parser

```python
"""
Parser for MY-DOMAIN elements.

Handles:
- MyElement1
- MyElement2
- MyElement3
"""
from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.MyDomain import (
    MyElement1, MyElement2, MyElement3
)

class MyNewParser(BaseARXMLParser):
    """
    Parser for MY-DOMAIN elements.

    Handles all MY-DOMAIN related functionality.
    """

    def __init__(self, options=None, main_parser=None):
        """Initialize MyNewParser."""
        super().__init__(options)
        self._main_parser = main_parser

    def readMyElement1(self, element: ET.Element, obj: MyElement1):
        """Parse MyElement1."""
        self.readIdentifiable(element, obj)
        # Implementation

    # ... more methods
```

### 3. Register Parser

In `src/armodel/parser/parsers/__init__.py`:

```python
from .my_new_parser import MyNewParser

__all__ = [
    # ... existing parsers
    'MyNewParser',
]
```

### 4. Initialize in ARXMLParser

In `src/armodel/parser/arxml_parser.py`:

```python
from .parsers.my_new_parser import MyNewParser

class ARXMLParser(AbstractARXMLParser):
    def __init__(self, options=None):
        super().__init__(options)
        # ... existing parsers
        self._my_new_parser = MyNewParser(options, self)

        self._parser_registry = {
            # ... existing mappings
            'MY-ELEMENT-1': self._my_new_parser,
        }
```

## Checklist for New Features

Before committing new parser features:

- [ ] Method added to correct specialized parser
- [ ] Parser registry updated (if applicable)
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Code follows PEP 8 standards
- [ ] No flake8 errors
- [ ] All existing tests still pass

## Resources

- Architecture: `docs/development/parser_architecture.md`
- Coding rules: `docs/development/coding_rules.md`
- Project overview: `CLAUDE.md`
- AUTOSAR specifications: https://www.autosar.org/
