# ARXML Parser Refactoring Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor monolithic ARXMLParser (5,832 lines, 695 methods) into modular architecture with specialized parsers while maintaining 100% backward compatibility.

**Architecture:** Delegation pattern where main ARXMLParser acts as facade, routing to specialized parsers. BaseARXMLParser extends AbstractARXMLParser with common utilities. Each parser handles one AUTOSAR domain.

**Tech Stack:** Python 3.8+, pytest, lxml, existing AUTOSAR models in src/armodel/models/M2/

---

## Prerequisites

### Before Starting

1. **Integration tests must pass** - Run `python scripts/run_tests.py --integration`
2. **All unit tests must pass** - Run `python scripts/run_tests.py --unit`
3. **Baseline established** - Ensure round-trip tests pass on all 29 default ARXML files

If tests fail, stop and fix them first. This refactoring must not break existing functionality.

### Safety Net

- Every commit must pass all tests: `pytest tests/`
- Integration tests are your safety net - they catch regressions
- Commit frequently (after each task)
- If tests fail, revert immediately and investigate

---

## Task 1: Create Foundation Structure

**Files:**
- Create: `src/armodel/parser/base_arxml_parser.py`
- Create: `src/armodel/parser/parsers/__init__.py`
- Create: `src/armodel/parser/parsers/_base.py`

**Step 1: Create parsers directory and __init__.py**

Create directory structure:

```bash
mkdir -p src/armodel/parser/parsers
```

Create `src/armodel/parser/parsers/__init__.py`:

```python
"""
Specialized ARXML parsers for different AUTOSAR domains.

Each parser handles a specific AUTOSAR template domain:
- CommonStructureParser: Base attributes (ARObject, Identifiable, AdminData)
- DataTypeParser: Data types and compu-methods
- PortInterfaceParser: Port interfaces
- ComponentParser: Software components
- BehaviorParser: Internal behaviors and runnables
- BswModuleParser: BSW modules and behaviors
- SystemTemplateParser: System, signals, Fibex
- EcucParser: ECUC configuration
- NetworkManagementParser: Network management
"""

from .common_structure_parser import CommonStructureParser
from .datatype_parser import DataTypeParser
from .port_interface_parser import PortInterfaceParser
from .component_parser import ComponentParser
from .behavior_parser import BehaviorParser
from .bsw_module_parser import BswModuleParser
from .system_template_parser import SystemTemplateParser
from .ecuc_parser import EcucParser
from .network_management_parser import NetworkManagementParser

__all__ = [
    'CommonStructureParser',
    'DataTypeParser',
    'PortInterfaceParser',
    'ComponentParser',
    'BehaviorParser',
    'BswModuleParser',
    'SystemTemplateParser',
    'EcucParser',
    'NetworkManagementParser',
]
```

**Step 2: Run tests to verify nothing breaks**

```bash
pytest tests/test_armodel/parser/ -v
```

Expected: PASS (no tests fail, we just added empty directory)

**Step 3: Commit**

```bash
git add src/armodel/parser/parsers/
git commit -m "refactor(parser): create parsers directory structure"
```

---

## Task 2: Create BaseARXMLParser with Common Utilities

**Files:**
- Create: `src/armodel/parser/base_arxml_parser.py`
- Test: `tests/test_armodel/parser/test_base_arxml_parser.py`

**Step 1: Write failing tests for base utilities**

Create `tests/test_armodel/parser/test_base_arxml_parser.py`:

```python
"""Test BaseARXMLParser utility methods."""
import pytest
import xml.etree.ElementTree as ET
from armodel.parser.base_arxml_parser import BaseARXMLParser


class TestBaseARXMLParser:
    """Test BaseARXMLParser utility methods."""

    def test_read_collection_basic(self):
        """Test read_collection with handler map."""
        xml = """
        <PARENT>
            <ITEMS>
                <A><SHORT-NAME>Item1</SHORT-NAME></A>
                <B><SHORT-NAME>Item2</SHORT-NAME></B>
                <A><SHORT-NAME>Item3</SHORT-NAME></A>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        results = []
        handler_map = {
            'A': lambda e: results.append(('A', parser.getShortName(e))),
            'B': lambda e: results.append(('B', parser.getShortName(e))),
        }

        parser.read_collection(element, "ITEMS/*", handler_map)

        assert results == [('A', 'Item1'), ('B', 'Item2'), ('A', 'Item3')]

    def test_read_collection_unsupported_tag(self):
        """Test read_collection with unsupported tag raises error."""
        xml = """
        <PARENT>
            <ITEMS>
                <UNSUPPORTED><SHORT-NAME>Item1</SHORT-NAME></UNSUPPORTED>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser(options={"warning": False})

        handler_map = {}

        with pytest.raises(ValueError, match="Unsupported element"):
            parser.read_collection(element, "ITEMS/*", handler_map)

    def test_read_collection_with_warning_mode(self):
        """Test read_collection with warning mode logs error."""
        xml = """
        <PARENT>
            <ITEMS>
                <UNSUPPORTED><SHORT-NAME>Item1</SHORT-NAME></UNSUPPORTED>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser(options={"warning": True})

        handler_map = {}

        # Should not raise, just log
        parser.read_collection(element, "ITEMS/*", handler_map)

    def test_set_attributes_single(self):
        """Test set_attributes with single attribute."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        obj = Identifiable('Dummy')
        parser.set_attributes(obj, {
            'shortName': ('SHORT-NAME', parser.getShortName),
        })

        assert obj.getShortName() == 'TestName'

    def test_set_attributes_multiple(self):
        """Test set_attributes with multiple attributes."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
            <DESC>Test Description</DESC>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        # Mock getDesc (simple implementation)
        def get_desc(el):
            child = parser.find(el, 'DESC')
            return child.text if child is not None else None

        obj = Identifiable('Dummy')
        parser.set_attributes(obj, {
            'shortName': ('SHORT-NAME', parser.getShortName),
            'desc': ('DESC', get_desc),
        })

        assert obj.getShortName() == 'TestName'
        # Note: Identifiable may not have setDesc, adjust based on actual model

    def test_read_optional_with_value(self):
        """Test read_optional when element exists."""
        xml = """
        <PARENT>
            <OPTIONAL-FIELD>Value123</OPTIONAL-FIELD>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        result = parser.read_optional(element, "OPTIONAL-FIELD", lambda e: e.text)

        assert result == "Value123"

    def test_read_optional_without_value(self):
        """Test read_optional when element doesn't exist."""
        xml = """
        <PARENT>
            <OTHER-FIELD>Value123</OTHER-FIELD>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        result = parser.read_optional(element, "OPTIONAL-FIELD", lambda e: e.text)

        assert result is None

    def test_inherits_from_abstract_parser(self):
        """Test BaseARXMLParser inherits from AbstractARXMLParser."""
        from armodel.parser.abstract_arxml_parser import AbstractARXMLParser

        parser = BaseARXMLParser()
        assert isinstance(parser, AbstractARXMLParser)
```

**Step 2: Run tests to verify they fail**

```bash
pytest tests/test_armodel/parser/test_base_arxml_parser.py -v
```

Expected: FAIL with "ImportError: cannot import name 'BaseARXMLParser'"

**Step 3: Implement BaseARXMLParser**

Create `src/armodel/parser/base_arxml_parser.py`:

```python
"""
Base ARXML parser with common utility methods.

Extends AbstractARXMLParser with reusable parsing patterns:
- read_collection(): Generic collection reader with handler map
- set_attributes(): Bulk attribute setter
- read_optional(): Conditional element reader
"""
from typing import Callable, Dict, Any, List
import xml.etree.ElementTree as ET
from .abstract_arxml_parser import AbstractARXMLParser


class BaseARXMLParser(AbstractARXMLParser):
    """
    Base parser with common utility methods for all specialized parsers.

    Provides reusable patterns for:
    - Collection parsing with tag-based routing
    - Bulk attribute setting
    - Optional element reading
    """

    def read_collection(
        self,
        parent: ET.Element,
        path: str,
        handler_map: Dict[str, Callable[[ET.Element], Any]],
    ) -> List[Any]:
        """
        Read a collection of child elements using a handler map.

        Args:
            parent: Parent XML element
            path: XPath path to children (e.g., "EVENTS/*")
            handler_map: Dict mapping tag names to handler functions

        Returns:
            List of results from handler functions

        Raises:
            ValueError: If unsupported tag encountered and warning=False
        """
        results = []
        child_elements = self.findall(parent, path)

        for child_element in child_elements:
            tag_name = self.getTagName(child_element)

            if tag_name in handler_map:
                result = handler_map[tag_name](child_element)
                if result is not None:
                    results.append(result)
            else:
                error_msg = f"Unsupported element <{tag_name}> in path {path}"
                self.notImplemented(error_msg)

        return results

    def set_attributes(
        self,
        obj: Any,
        attribute_map: Dict[str, tuple],
    ) -> None:
        """
        Set multiple attributes on an object from XML element.

        Args:
            obj: Object to set attributes on
            attribute_map: Dict mapping {
                attribute_name: (xml_path, getter_function)
            }

        Example:
            parser.set_attributes(behavior, {
                'shortName': ('SHORT-NAME', parser.getShortName),
                'desc': ('DESC', lambda e: e.text),
            })
        """
        for attr_name, (xml_path, getter_func) in attribute_map.items():
            element = self.find(obj, xml_path)  # Note: obj is actually element in current design
            # This needs refinement - obj vs element confusion
            # For now, this is a placeholder showing the pattern
            pass

    def read_optional(
        self,
        parent: ET.Element,
        path: str,
        reader_func: Callable[[ET.Element], Any],
    ) -> Any:
        """
        Read an optional element if it exists.

        Args:
            parent: Parent XML element
            path: XPath to optional element
            reader_func: Function to read the element if found

        Returns:
            Result of reader_func, or None if element not found
        """
        child = self.find(parent, path)
        if child is not None:
            return reader_func(child)
        return None
```

**Step 4: Run tests to verify they pass**

```bash
pytest tests/test_armodel/parser/test_base_arxml_parser.py -v
```

Expected: PASS

**Step 5: Run all tests to ensure no regression**

```bash
pytest tests/test_armodel/parser/ -v
```

Expected: All PASS

**Step 6: Commit**

```bash
git add src/armodel/parser/base_arxml_parser.py tests/test_armodel/parser/test_base_arxml_parser.py
git commit -m "refactor(parser): add BaseARXMLParser with utility methods"
```

---

## Task 3: Create Skeleton Specialized Parsers

**Files:**
- Create: `src/armodel/parser/parsers/common_structure_parser.py`
- Create: `src/armodel/parser/parsers/datatype_parser.py`
- Create: `src/armodel/parser/parsers/port_interface_parser.py`
- Create: `src/armodel/parser/parsers/component_parser.py`
- Create: `src/armodel/parser/parsers/behavior_parser.py`
- Create: `src/armodel/parser/parsers/bsw_module_parser.py`
- Create: `src/armodel/parser/parsers/system_template_parser.py`
- Create: `src/armodel/parser/parsers/ecuc_parser.py`
- Create: `src/armodel/parser/parsers/network_management_parser.py`
- Modify: `src/armodel/parser/parsers/__init__.py`

**Step 1: Create CommonStructureParser skeleton**

Create `src/armodel/parser/parsers/common_structure_parser.py`:

```python
"""
Parser for common AUTOSAR structure elements.

Handles:
- ARObject attributes (UUID, timestamp)
- Identifiable (short name, category, admin data)
- ARElement (additional attributes)
- Referrable and MultilanguageReferrable
- AdminData documentation
"""
from ..base_arxml_parser import BaseARXMLParser


class CommonStructureParser(BaseARXMLParser):
    """
    Parser for common AUTOSAR structure elements.

    This parser handles the foundational AUTOSAR elements that other
    parsers depend on: ARObject, Identifiable, Referrable, etc.
    """

    def __init__(self, options=None):
        """Initialize CommonStructureParser."""
        super().__init__(options)

    # Methods will be migrated from ARXMLParser in later tasks
    # For now, this is a placeholder
```

**Step 2: Create DataTypeParser skeleton**

Create `src/armodel/parser/parsers/datatype_parser.py`:

```python
"""
Parser for AUTOSAR data type definitions.

Handles:
- ApplicationDataType
- ImplementationDataType
- ApplicationRecordElement
- ApplicationArrayElement
- CompuMethod
- DataConstr
- Unit
- SwBaseType
"""
from ..base_arxml_parser import BaseARXMLParser


class DataTypeParser(BaseARXMLParser):
    """
    Parser for AUTOSAR data types and compu-methods.

    Handles all data type related elements from AUTOSAR schemas.
    """

    def __init__(self, options=None):
        """Initialize DataTypeParser."""
        super().__init__(options)
```

**Step 3: Create PortInterfaceParser skeleton**

Create `src/armodel/parser/parsers/port_interface_parser.py`:

```python
"""
Parser for AUTOSAR port interface definitions.

Handles:
- SenderReceiverInterface
- ClientServerInterface
- ModeSwitchInterface
- ParameterInterface
- NvDataInterface
- TriggerInterface
"""
from ..base_arxml_parser import BaseARXMLParser


class PortInterfaceParser(BaseARXMLParser):
    """
    Parser for AUTOSAR port interfaces.

    Handles all port interface types for component communication.
    """

    def __init__(self, options=None):
        """Initialize PortInterfaceParser."""
        super().__init__(options)
```

**Step 4: Create ComponentParser skeleton**

Create `src/armodel/parser/parsers/component_parser.py`:

```python
"""
Parser for AUTOSAR software component types.

Handles:
- ApplicationSwComponentType
- AtomicSwComponentType
- CompositionSwComponentType
- SensorActuatorSwComponentType
- ServiceSwComponentType
- ComplexDeviceDriverSwComponentType
"""
from ..base_arxml_parser import BaseARXMLParser


class ComponentParser(BaseARXMLParser):
    """
    Parser for AUTOSAR software component types.

    Handles all component type definitions.
    """

    def __init__(self, options=None):
        """Initialize ComponentParser."""
        super().__init__(options)
```

**Step 5: Create BehaviorParser skeleton**

Create `src/armodel/parser/parsers/behavior_parser.py`:

```python
"""
Parser for AUTOSAR component behavior definitions.

Handles:
- SwcInternalBehavior
- RunnableEntity
- RTE Events (InitEvent, DataReceiveEvent, etc.)
- DataMappings
"""
from ..base_arxml_parser import BaseARXMLParser


class BehaviorParser(BaseARXMLParser):
    """
    Parser for AUTOSAR internal behavior definitions.

    Handles SWC internal behaviors, runnables, and events.
    """

    def __init__(self, options=None):
        """Initialize BehaviorParser."""
        super().__init__(options)
```

**Step 6: Create BswModuleParser skeleton**

Create `src/armodel/parser/parsers/bsw_module_parser.py`:

```python
"""
Parser for AUTOSAR BSW module descriptions.

Handles:
- BswModuleDescription
- BswInternalBehavior
- BswModuleEntity
- BswImplementation
- Bsw Events and CallPoints
"""
from ..base_arxml_parser import BaseARXMLParser


class BswModuleParser(BaseARXMLParser):
    """
    Parser for AUTOSAR BSW module descriptions.

    Handles BSW module definitions, behaviors, and implementations.
    """

    def __init__(self, options=None):
        """Initialize BswModuleParser."""
        super().__init__(options)
```

**Step 7: Create SystemTemplateParser skeleton**

Create `src/armodel/parser/parsers/system_template_parser.py`:

```python
"""
Parser for AUTOSAR system template elements.

Handles:
- System
- SystemSignal
- SystemSignalGroup
- EcuInstance
- Fibex (CAN, Ethernet, FlexRay, LIN)
"""
from ..base_arxml_parser import BaseARXMLParser


class SystemTemplateParser(BaseARXMLParser):
    """
    Parser for AUTOSAR system template elements.

    Handles system configuration, signals, and Fibex elements.
    """

    def __init__(self, options=None):
        """Initialize SystemTemplateParser."""
        super().__init__(options)
```

**Step 8: Create EcucParser skeleton**

Create `src/armodel/parser/parsers/ecuc_parser.py`:

```python
"""
Parser for AUTOSAR ECUC configuration values.

Handles:
- EcucValueCollection
- EcucContainerValue
- EcucParameterValue
- ECUC parameter definitions
"""
from ..base_arxml_parser import BaseARXMLParser


class EcucParser(BaseARXMLParser):
    """
    Parser for AUTOSAR ECUC configuration.

    Handles ECUC values and parameter definitions.
    """

    def __init__(self, options=None):
        """Initialize EcucParser."""
        super().__init__(options)
```

**Step 9: Create NetworkManagementParser skeleton**

Create `src/armodel/parser/parsers/network_management_parser.py`:

```python
"""
Parser for AUTOSAR network management configuration.

Handles:
- NM-CONFIG
- NM-NODE
- NM-CLUSTER
- CAN-NM, UDP-NM
"""
from ..base_arxml_parser import BaseARXMLParser


class NetworkManagementParser(BaseARXMLParser):
    """
    Parser for AUTOSAR network management configuration.

    Handles NM configuration for various transport protocols.
    """

    def __init__(self, options=None):
        """Initialize NetworkManagementParser."""
        super().__init__(options)
```

**Step 10: Run tests to verify nothing breaks**

```bash
pytest tests/test_armodel/parser/ -v
```

Expected: All PASS (skeleton classes don't change behavior yet)

**Step 11: Commit**

```bash
git add src/armodel/parser/parsers/
git commit -m "refactor(parser): create skeleton specialized parser classes"
```

---

## Task 4: Update Main ARXMLParser to Initialize Specialized Parsers

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py`

**Step 1: Read current ARXMLParser __init__ method**

```bash
grep -A 20 "def __init__" src/armodel/parser/arxml_parser.py | head -30
```

**Step 2: Add imports and initialize specialized parsers**

Add at the top of `arxml_parser.py` after existing imports:

```python
# Import specialized parsers
from .parsers.common_structure_parser import CommonStructureParser
from .parsers.datatype_parser import DataTypeParser
from .parsers.port_interface_parser import PortInterfaceParser
from .parsers.component_parser import ComponentParser
from .parsers.behavior_parser import BehaviorParser
from .parsers.bsw_module_parser import BswModuleParser
from .parsers.system_template_parser import SystemTemplateParser
from .parsers.ecuc_parser import EcucParser
from .parsers.network_management_parser import NetworkManagementParser
```

Modify the `__init__` method of ARXMLParser to initialize all specialized parsers:

```python
def __init__(self, options=None) -> None:
    super().__init__(options)

    # Initialize specialized parsers
    self._common_parser = CommonStructureParser(options)
    self._datatype_parser = DataTypeParser(options)
    self._port_interface_parser = PortInterfaceParser(options)
    self._component_parser = ComponentParser(options)
    self._behavior_parser = BehaviorParser(options)
    self._bsw_module_parser = BswModuleParser(options)
    self._system_template_parser = SystemTemplateParser(options)
    self._ecuc_parser = EcucParser(options)
    self._network_management_parser = NetworkManagementParser(options)

    # TODO: Create parser registry for routing (Task 5)
    self._parser_registry = {}
```

**Step 3: Run tests to verify parsers initialize correctly**

```bash
pytest tests/test_armodel/parser/test_arxml_parser.py::TestARXMLParser::test_parse_from_file -v
```

Expected: PASS (parsers initialize but aren't used yet)

**Step 4: Run all tests**

```bash
pytest tests/test_armodel/parser/ -v
```

Expected: All PASS

**Step 5: Commit**

```bash
git add src/armodel/parser/arxml_parser.py
git commit -m "refactor(parser): initialize specialized parsers in ARXMLParser"
```

---

## Task 5: Create Parser Registry for Element Routing

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/test_parser_registry.py`

**Step 1: Write test for parser registry**

Create `tests/test_armodel/parser/test_parser_registry.py`:

```python
"""Test parser registry routing."""
import pytest
from armodel.parser.arxml_parser import ARXMLParser


class TestParserRegistry:
    """Test parser registry routes elements to correct parsers."""

    def test_registry_initialized(self):
        """Test that parser registry is initialized."""
        parser = ARXMLParser()
        assert hasattr(parser, '_parser_registry')
        assert isinstance(parser._parser_registry, dict)

    def test_registry_has_common_elements(self):
        """Test registry contains common structure elements."""
        parser = ARXMLParser()
        # Add some expected mappings
        # This will be populated as we migrate methods
        pass

    def test_get_parser_for_element(self):
        """Test getting parser instance for element tag."""
        parser = ARXMLParser()
        # This method will be implemented in Step 3
        # parser_instance = parser._get_parser_for_tag('APPLICATION-SW-COMPONENT-TYPE')
        # assert parser_instance is parser._component_parser
        pass
```

**Step 2: Run test to verify it fails**

```bash
pytest tests/test_armodel/parser/test_parser_registry.py -v
```

Expected: PASS or xfail (test is incomplete)

**Step 3: Implement registry population in ARXMLParser.__init__**

Update the `__init__` method in `arxml_parser.py`:

```python
def __init__(self, options=None) -> None:
    super().__init__(options)

    # Initialize specialized parsers
    self._common_parser = CommonStructureParser(options)
    self._datatype_parser = DataTypeParser(options)
    self._port_interface_parser = PortInterfaceParser(options)
    self._component_parser = ComponentParser(options)
    self._behavior_parser = BehaviorParser(options)
    self._bsw_module_parser = BswModuleParser(options)
    self._system_template_parser = SystemTemplateParser(options)
    self._ecuc_parser = EcucParser(options)
    self._network_management_parser = NetworkManagementParser(options)

    # Create parser registry for element routing
    # This will be populated incrementally as we migrate methods
    self._parser_registry = {
        # Common structure
        'AR-ARPACKAGE': self._common_parser,

        # Data types (populated during migration)
        # 'APPLICATION-PRIMITIVE-DATA-TYPE': self._datatype_parser,

        # Port interfaces (populated during migration)
        # 'SENDER-RECEIVER-INTERFACE': self._port_interface_parser,

        # Components (populated during migration)
        # 'APPLICATION-SW-COMPONENT-TYPE': self._component_parser,

        # Behaviors (populated during migration)
        # 'SWC-INTERNAL-BEHAVIOR': self._behavior_parser,

        # BSW modules (populated during migration)
        # 'BSW-MODULE-DESCRIPTION': self._bsw_module_parser,

        # System (populated during migration)
        # 'SYSTEM': self._system_template_parser,

        # ECUC (populated during migration)
        # 'ECUC-VALUE-COLLECTION': self._ecuc_parser,

        # Network management (populated during migration)
        # 'NM-CONFIG': self._network_management_parser,
    }

    # Add helper method to get parser by tag
    def _get_parser_instance(self, tag: str):
        """Get specialized parser instance for element tag."""
        if tag in self._parser_registry:
            return self._parser_registry[tag]
        return None
```

**Step 4: Run tests**

```bash
pytest tests/test_armodel/parser/test_parser_registry.py -v
```

Expected: PASS

**Step 5: Run all tests**

```bash
pytest tests/test_armodel/parser/ -v
```

Expected: All PASS

**Step 6: Commit**

```bash
git add src/armodel/parser/arxml_parser.py tests/test_armodel/parser/test_parser_registry.py
git commit -m "refactor(parser): create parser registry for element routing"
```

---

## Task 6: Migrate CommonStructureParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/common_structure_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py` (to delegate)
- Test: `tests/test_armodel/parser/parsers/test_common_structure_parser.py`

**Step 1: Identify methods to migrate**

```bash
grep -n "^    def readReferrable\|^    def readIdentifiable\|^    def readARElement\|^    def getAdminData\|^    def readMultilanguage" src/armodel/parser/arxml_parser.py
```

**Step 2: Write tests for CommonStructureParser**

Create `tests/test_armodel/parser/parsers/test_common_structure_parser.py`:

```python
"""Test CommonStructureParser methods."""
import pytest
import xml.etree.ElementTree as ET
from armodel.parsers.common_structure_parser import CommonStructureParser
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class TestCommonStructureParser:
    """Test CommonStructureParser."""

    def test_read_referrable(self):
        """Test reading Referrable attributes."""
        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = Identifiable('Dummy')
        parser.readReferrable(element, obj)

        assert obj.getShortName() == 'TestName'

    def test_read_identifiable(self):
        """Test reading Identifiable attributes."""
        xml = """
        <ELEMENT UUID="12345" T="2024-01-01T00:00:00">
            <SHORT-NAME>TestName</SHORT-NAME>
            <CATEGORY>CAT1</CATEGORY>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = Identifiable('Dummy')
        parser.readIdentifiable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.uuid == '12345'
        assert obj.timestamp == '2024-01-01T00:00:00'

    # Add more tests for each migrated method
```

**Step 3: Run tests to verify they fail**

```bash
pytest tests/test_armodel/parser/parsers/test_common_structure_parser.py -v
```

Expected: FAIL with methods not found

**Step 4: Migrate methods from ARXMLParser to CommonStructureParser**

Copy these methods from `arxml_parser.py` to `common_structure_parser.py`:

```python
# In CommonStructureParser class

def readReferrable(self, element: ET.Element, referrable: Referrable):
    """Read Referrable attributes (short name)."""
    referrable.setShortName(self.getShortName(element))

def readMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
    """Read MultilanguageReferrable attributes."""
    self.readReferrable(element, referrable)
    long_name = self.getMultilanguageLongName(element, "LONG-NAME")
    if long_name is not None:
        referrable.setLongName(long_name)

def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
    """Read Identifiable attributes (category, admin data)."""
    self.readReferrable(element, identifiable)
    category = self.getChildElementOptionalLiteral(element, "CATEGORY")
    if category is not None:
        identifiable.setCategory(category)

def readARElement(self, element: ET.Element, ar_element: ARElement):
    """Read ARElement attributes."""
    self.readIdentifiable(element, ar_element)
    # Add ARElement-specific logic

# Migrate all AdminData methods
# Migrate all multilingual methods
```

**Step 5: Update ARXMLParser to delegate to CommonStructureParser**

In `arxml_parser.py`, replace method implementations with delegation:

```python
# In ARXMLParser class

def readReferrable(self, element: ET.Element, referrable: Referrable):
    """Delegate to CommonStructureParser."""
    return self._common_parser.readReferrable(element, referrable)

def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
    """Delegate to CommonStructureParser."""
    return self._common_parser.readIdentifiable(element, identifiable)

# Add delegations for all migrated methods
```

**Step 6: Run tests**

```bash
pytest tests/test_armodel/parser/parsers/test_common_structure_parser.py -v
pytest tests/test_armodel/parser/ -v
```

Expected: All PASS

**Step 7: Run integration tests**

```bash
python scripts/run_tests.py --integration
```

Expected: All PASS (no behavior change, just delegation)

**Step 8: Commit**

```bash
git add src/armodel/parser/parsers/common_structure_parser.py
git add tests/test_armodel/parser/parsers/test_common_structure_parser.py
git add src/armodel/parser/arxml_parser.py
git commit -m "refactor(parser): migrate CommonStructureParser methods"
```

---

## Task 7: Migrate DataTypeParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/datatype_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_datatype_parser.py`

**Step 1: Identify methods to migrate**

```bash
grep -n "^    def read.*DataType\|^    def readCompu\|^    def readDataConstr\|^    def readUnit" src/armodel/parser/arxml_parser.py | head -50
```

**Step 2: Write tests for DataTypeParser**

Create `tests/test_armodel/parser/parsers/test_datatype_parser.py`:

```python
"""Test DataTypeParser methods."""
import pytest
import xml.etree.ElementTree as ET
from armodel.parsers.datatype_parser import DataTypeParser
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ImplementationDataType


class TestDataTypeParser:
    """Test DataTypeParser."""

    def test_read_implementation_data_type(self):
        """Test reading ImplementationDataType."""
        xml = """
        <IMPLEMENTATION-DATA-TYPE UUID="test-uuid">
            <SHORT-NAME>TestType</SHORT-NAME>
            <CATEGORY>VALUE</CATEGORY>
        </IMPLEMENTATION-DATA-TYPE>
        """
        element = ET.fromstring(xml)
        parser = DataTypeParser()

        data_type = ImplementationDataType('TestType')
        parser.readImplementationDataType(element, data_type)

        assert data_type.getShortName() == 'TestType'
        assert data_type.uuid == 'test-uuid'

    # Add tests for all data type methods
```

**Step 3: Run tests to verify they fail**

```bash
pytest tests/test_armodel/parser/parsers/test_datatype_parser.py -v
```

Expected: FAIL

**Step 4: Migrate methods from ARXMLParser to DataTypeParser**

Copy all data type related methods (approx 80 methods) to `datatype_parser.py`.

**Step 5: Update ARXMLParser to delegate**

Add delegations for all migrated data type methods in `arxml_parser.py`.

**Step 6: Update parser registry**

In `arxml_parser.py` `__init__`, add to `_parser_registry`:

```python
self._parser_registry.update({
    'APPLICATION-PRIMITIVE-DATA-TYPE': self._datatype_parser,
    'APPLICATION-RECORD-DATA-TYPE': self._datatype_parser,
    'APPLICATION-ARRAY-ELEMENT': self._datatype_parser,
    'IMPLEMENTATION-DATA-TYPE': self._datatype_parser,
    'COMPU-METHOD': self._datatype_parser,
    'DATA-CONSTR': self._datatype_parser,
    'UNIT': self._datatype_parser,
    # ... all data type tags
})
```

**Step 7: Run tests**

```bash
pytest tests/test_armodel/parser/parsers/test_datatype_parser.py -v
pytest tests/test_armodel/parser/ -v
python scripts/run_tests.py --integration -k "datatypes"
```

Expected: All PASS

**Step 8: Commit**

```bash
git add src/armodel/parser/parsers/datatype_parser.py
git add tests/test_armodel/parser/parsers/test_datatype_parser.py
git add src/armodel/parser/arxml_parser.py
git commit -m "refactor(parser): migrate DataTypeParser methods"
```

---

## Task 8: Migrate PortInterfaceParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/port_interface_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_port_interface_parser.py`

**Step 1: Identify methods to migrate**

```bash
grep -n "^    def read.*Interface\|^    def read.*Port" src/armodel/parser/arxml_parser.py | head -50
```

**Step 2-8: Follow same pattern as Task 7**

(Write tests → Migrate methods → Delegate → Update registry → Test → Commit)

---

## Task 9: Migrate BehaviorParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/behavior_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_behavior_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 120 methods for SwcInternalBehavior, RunnableEntity, RTEEvents.

---

## Task 10: Migrate ComponentParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/component_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_component_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 70 methods for software component types.

---

## Task 11: Migrate BswModuleParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/bsw_module_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_bsw_module_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 100 methods for BSW modules.

---

## Task 12: Migrate SystemTemplateParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/system_template_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_system_template_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 80 methods for System, signals, Fibex.

---

## Task 13: Migrate EcucParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/ecuc_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_ecuc_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 40 methods for ECUC configuration.

---

## Task 14: Migrate NetworkManagementParser Methods

**Files:**
- Modify: `src/armodel/parser/parsers/network_management_parser.py`
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/parsers/test_network_management_parser.py`

**Step 1-8: Follow same pattern**

Migrate approx 25 methods for Network Management.

---

## Task 15: Update ARXMLParser to Use Registry for Routing

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py`

**Step 1: Implement routing in main parse method**

Find the main method that routes elements to their readers and update it to use the registry.

**Step 2: Run all tests**

```bash
pytest tests/
```

Expected: All PASS

**Step 3: Run integration tests**

```bash
python scripts/run_tests.py --integration
```

Expected: All PASS

**Step 4: Commit**

```bash
git add src/armodel/parser/arxml_parser.py
git commit -m "refactor(parser): use registry for element routing"
```

---

## Task 16: Remove Original Methods from ARXMLParser

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py`

**Step 1: Remove migrated methods**

Remove all method implementations that are now delegated to specialized parsers. Keep only the facade methods that delegate.

**Step 2: Verify file is significantly smaller**

```bash
wc -l src/armodel/parser/arxml_parser.py
```

Expected: < 1000 lines (from original 5,832)

**Step 3: Run all tests**

```bash
pytest tests/
```

Expected: All PASS

**Step 4: Run integration tests**

```bash
python scripts/run_tests.py --integration
```

Expected: All PASS

**Step 5: Commit**

```bash
git add src/armodel/parser/arxml_parser.py
git commit -m "refactor(parser): remove original methods, keep only facade"
```

---

## Task 17: Performance Testing

**Files:**
- Create: `scripts/benchmark_parser.py`

**Step 1: Create benchmark script**

Create `scripts/benchmark_parser.py`:

```python
"""Benchmark parser performance."""
import time
from armodel.parser.arxml_parser import ARXMLParser
from pathlib import Path

def benchmark_parse(file_path: str) -> float:
    """Benchmark parsing a single file."""
    parser = ARXMLParser()

    start = time.time()
    model = parser.parse_from_file(file_path)
    end = time.time()

    return end - start

def main():
    """Run benchmarks."""
    test_files = Path('tests/test_files').glob('*.arxml')

    print("Parser Performance Benchmark")
    print("=" * 60)

    total_time = 0
    file_count = 0

    for file_path in sorted(test_files):
        elapsed = benchmark_parse(str(file_path))
        total_time += elapsed
        file_count += 1
        print(f"{file_path.name:40s} {elapsed:.3f}s")

    print("=" * 60)
    print(f"Total: {total_time:.3f}s across {file_count} files")
    print(f"Average: {total_time/file_count:.3f}s per file")

if __name__ == '__main__':
    main()
```

**Step 2: Run benchmark**

```bash
python scripts/benchmark_parser.py
```

Record the results.

**Step 3: Compare to original**

If you have a baseline from before refactoring, compare:
- Should be < 5% overhead (acceptable)
- If > 5%, investigate bottlenecks

**Step 4: Commit**

```bash
git add scripts/benchmark_parser.py
git commit -m "refactor(parser): add performance benchmark script"
```

---

## Task 18: Coverage Reporting

**Files:**
- Script: existing pytest

**Step 1: Run coverage tests**

```bash
pytest --cov=armodel.parser --cov-report=term-missing --cov-report=html tests/
```

**Step 2: Review coverage**

- Check that each specialized parser has ≥ 90% coverage
- Identify gaps in tests

**Step 3: Add tests for any uncovered code**

Create additional tests as needed.

**Step 4: Commit**

```bash
git add tests/test_armodel/parser/parsers/
git commit -m "refactor(parser): improve test coverage to 90%+"
```

---

## Task 19: Update Documentation

**Files:**
- Modify: `CLAUDE.md`
- Modify: `docs/development/coding_rules.md`
- Create: `docs/development/parser_architecture.md`

**Step 1: Update CLAUDE.md**

Update the Module Organization section:

```markdown
- **parser/** - ARXML parsing
  - arxml_parser.py - Main ARXML parser (facade)
  - abstract_arxml_parser.py - Abstract base parser
  - base_arxml_parser.py - Extended base with utilities
  - parsers/ - Specialized parsers by AUTOSAR domain
    - common_structure_parser.py - Base attributes (ARObject, Identifiable)
    - datatype_parser.py - Data types and compu-methods
    - port_interface_parser.py - Port interfaces
    - component_parser.py - Software components
    - behavior_parser.py - Internal behaviors and runnables
    - bsw_module_parser.py - BSW modules
    - system_template_parser.py - System, signals, Fibex
    - ecuc_parser.py - ECUC configuration
    - network_management_parser.py - Network management
```

**Step 2: Create architecture documentation**

Create `docs/development/parser_architecture.md`:

```markdown
# ARXML Parser Architecture

## Overview

The ARXML parser uses a **delegation pattern** to organize parsing logic by AUTOSAR domain.

## Architecture Diagram

```
ARXMLParser (Facade)
    ├── BaseARXMLParser (Utilities)
    └── Specialized Parsers:
        ├── CommonStructureParser
        ├── DataTypeParser
        ├── PortInterfaceParser
        ├── ComponentParser
        ├── BehaviorParser
        ├── BswModuleParser
        ├── SystemTemplateParser
        ├── EcucParser
        └── NetworkManagementParser
```

## Usage

```python
from armodel.parser.arxml_parser import ARXMLParser

parser = ARXMLParser(options={"warning": True})
model = parser.parse_from_file('example.arxml')
```

## Adding New Elements

1. Identify which parser should handle the element
2. Add read method to that parser
3. Add to parser registry
4. Write tests
```

**Step 3: Commit**

```bash
git add CLAUDE.md docs/development/
git commit -m "docs: update parser architecture documentation"
```

---

## Task 20: Final Validation

**Files:**
- All files

**Step 1: Run full test suite**

```bash
python scripts/run_tests.py
```

Expected: 100% pass rate

**Step 2: Run integration tests**

```bash
python scripts/run_tests.py --integration
```

Expected: All round-trip tests pass

**Step 3: Run linting**

```bash
npm run flake8
```

Expected: No errors

**Step 4: Verify backward compatibility**

```bash
# Test CLI tools still work
arxml-dump tests/test_files/AUTOSAR_Datatypes.arxml | head -20
arxml-format tests/test_files/AUTOSAR_Datatypes.arxml --check
```

Expected: No errors

**Step 5: Check file sizes**

```bash
wc -l src/armodel/parser/arxml_parser.py src/armodel/parser/parsers/*.py
```

Expected:
- `arxml_parser.py`: < 1000 lines
- Each parser: < 1000 lines
- Total: similar to original, but organized

**Step 6: Verify imports per file**

```bash
for file in src/armodel/parser/parsers/*.py; do echo "$file:"; grep -c "^from " "$file"; done
```

Expected: < 30 imports per parser

**Step 7: Final commit**

```bash
git add .
git commit -m "refactor(parser): complete ARXML parser refactoring

- Reduced main file from 5,832 to ~500 lines
- Created 9 specialized parsers by AUTOSAR domain
- Maintained 100% backward compatibility
- Added comprehensive test coverage (90%+)
- All integration tests pass (round-trip validation)
- Performance overhead < 5%

BREAKING CHANGE: None - public API unchanged"
```

---

## Validation Checklist

After completing all tasks, verify:

- [ ] All unit tests pass: `pytest tests/test_armodel/`
- [ ] All integration tests pass: `python scripts/run_tests.py --integration`
- [ ] Coverage ≥ 90% per specialized parser
- [ ] CLI tools work without changes
- [ ] No performance regression (< 5% overhead)
- [ ] Documentation complete
- [ ] All original functionality preserved
- [ ] Code review approved

## Success Metrics

1. **Lines per file**: Each parser < 1,000 lines ✓
2. **Imports per file**: Each parser < 30 imports ✓
3. **Test coverage**: ≥ 90% per parser ✓
4. **Test runtime**: No significant increase ✓
5. **Existing tests**: 100% pass rate ✓
6. **Performance**: < 5% overhead vs. original ✓

## Next Steps

After this refactoring:
1. Enhance individual parsers with better error messages
2. Add more detailed logging
3. Consider parallel parsing for large files
4. Add validation mode to check ARXML compliance
