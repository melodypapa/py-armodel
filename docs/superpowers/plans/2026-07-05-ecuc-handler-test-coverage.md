# ECUC Handler Test Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add ~30 focused tests for ECUC parsing handlers to improve arxml_parser.py coverage from 86.47% to ~90%+.

**Architecture:** Create a dedicated test file `test_arxml_parser_ecuc_handlers.py` with 3 test classes covering the main ECUC handler gaps. Follow the established Phase G/H/I test file patterns with inline XML snippets via `_snip()` helper.

**Tech Stack:** pytest, ElementTree, AUTOSAR singleton pattern, armodel.models ECUC classes.

## Global Constraints

- AUTOSAR version must be set via `AUTOSAR.setARRelease('R23-11')` before parsing
- Use `AUTOSAR.getInstance().new()` to reset singleton between tests
- Follow existing test patterns from Phase G/H/I files
- Use inline XML snippets (no external test files)
- Import ECUC model classes: `EcucParamConfContainerDef`, `EcucBooleanParamDef`, etc.
- Namespace: `NS = "http://autosar.org/schema/r4.0"`

---

### Task 1: Create Test File with Fixtures

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Produces: `_snip()` helper, `parser` fixture, `reset_autosar` fixture

- [ ] **Step 1: Write the test file header and fixtures**

```python
"""Tests for ECUC (ECU Configuration) parsing handlers."""

import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()
```

- [ ] **Step 2: Run tests to verify file loads**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py -v --collect-only`
Expected: Shows test collection (no tests yet, but file loads)

- [ ] **Step 3: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC handler test file with fixtures"
```

---

### Task 2: TestEcucContainerDefParameters Class - Boolean and String

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucParamConfContainerDef` model class
- Produces: Tests covering `readEcucBooleanParamDef`, `readEcucStringParamDef` (lines 4578-4583)

- [ ] **Step 1: Write TestEcucContainerDefParameters class header and boolean tests**

Add to the test file:

```python
class TestEcucContainerDefParameters:
    """Tests for readEcucContainerDefParameters handler."""

    def test_readEcucBooleanParamDef_with_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>EnableFeature</SHORT-NAME>
                    <DEFAULT-VALUE>true</DEFAULT-VALUE>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EnableFeature"
        assert params[0].getDefaultValue() is not None
        assert params[0].getDefaultValue().getValue() == True

    def test_readEcucBooleanParamDef_without_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>EnableFeature</SHORT-NAME>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EnableFeature"
        assert params[0].getDefaultValue() is None
```

- [ ] **Step 2: Write String parameter tests**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucStringParamDef_with_default(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>ConfigString</SHORT-NAME>
                    <DEFAULT-VALUE>default_value</DEFAULT-VALUE>
                    <MAX-LENGTH>100</MAX-LENGTH>
                    <MIN-LENGTH>1</MIN-LENGTH>
                </ECUC-STRING-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "ConfigString"
        assert params[0].getDefaultValue() is not None
        assert params[0].getMaxLength().getValue() == 100
        assert params[0].getMinLength().getValue() == 1

    def test_readEcucStringParamDef_without_default(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>ConfigString</SHORT-NAME>
                </ECUC-STRING-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "ConfigString"
        assert params[0].getDefaultValue() is None
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucContainerDefParameters -v`
Expected: 4 tests pass

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC Boolean and String parameter tests"
```

---

### Task 3: TestEcucContainerDefParameters Class - Integer and Float

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucParamConfContainerDef` model class
- Produces: Tests covering `readEcucIntegerParamDef`, `readEcucFloatParamDef` (lines 4584-4589)

- [ ] **Step 1: Write Integer parameter tests**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucIntegerParamDef_with_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>MaxRetries</SHORT-NAME>
                    <DEFAULT-VALUE>10</DEFAULT-VALUE>
                    <MAX>100</MAX>
                    <MIN>0</MIN>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "MaxRetries"
        assert params[0].getDefaultValue().getValue() == 10
        assert params[0].getMax().getValue() == 100
        assert params[0].getMin().getValue() == 0

    def test_readEcucIntegerParamDef_without_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>Counter</SHORT-NAME>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Counter"
        assert params[0].getDefaultValue() is None
        assert params[0].getMax() is None
        assert params[0].getMin() is None
```

- [ ] **Step 2: Write Float parameter tests**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucFloatParamDef_with_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FLOAT-PARAM-DEF>
                    <SHORT-NAME>Tolerance</SHORT-NAME>
                    <DEFAULT-VALUE>0.5</DEFAULT-VALUE>
                    <MAX>
                        <VALUE>10.0</VALUE>
                        <INTERVAL-TYPE>CLOSED</INTERVAL-TYPE>
                    </MAX>
                    <MIN>
                        <VALUE>0.0</VALUE>
                        <INTERVAL-TYPE>CLOSED</INTERVAL-TYPE>
                    </MIN>
                </ECUC-FLOAT-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Tolerance"
        assert params[0].getDefaultValue() is not None

    def test_readEcucFloatParamDef_without_limits(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FLOAT-PARAM-DEF>
                    <SHORT-NAME>Ratio</SHORT-NAME>
                </ECUC-FLOAT-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Ratio"
        assert params[0].getDefaultValue() is None
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucContainerDefParameters -v`
Expected: 8 tests pass (4 from Task 2 + 4 new)

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC Integer and Float parameter tests"
```

---

### Task 4: TestEcucContainerDefParameters Class - Enumeration and FunctionName

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucParamConfContainerDef`, `EcucEnumerationParamDef` model classes
- Produces: Tests covering `readEcucEnumerationParamDef`, `readEcucFunctionNameDef` (lines 4590-4595)

- [ ] **Step 1: Write Enumeration parameter tests**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucEnumerationParamDef_with_literals(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-ENUMERATION-PARAM-DEF>
                    <SHORT-NAME>Mode</SHORT-NAME>
                    <DEFAULT-VALUE>STANDARD</DEFAULT-VALUE>
                    <LITERALS>
                        <ECUC-ENUMERATION-LITERAL-DEF>
                            <SHORT-NAME>STANDARD</SHORT-NAME>
                        </ECUC-ENUMERATION-LITERAL-DEF>
                        <ECUC-ENUMERATION-LITERAL-DEF>
                            <SHORT-NAME>ADVANCED</SHORT-NAME>
                        </ECUC-ENUMERATION-LITERAL-DEF>
                    </LITERALS>
                </ECUC-ENUMERATION-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Mode"
        assert params[0].getDefaultValue() is not None
        literals = params[0].getLiterals()
        assert len(literals) == 2

    def test_readEcucEnumerationParamDef_without_literals(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-ENUMERATION-PARAM-DEF>
                    <SHORT-NAME>EmptyMode</SHORT-NAME>
                </ECUC-ENUMERATION-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "EmptyMode"
        assert params[0].getDefaultValue() is None
```

- [ ] **Step 2: Write FunctionName parameter tests**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucFunctionNameDef_with_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FUNCTION-NAME-DEF>
                    <SHORT-NAME>InitFunction</SHORT-NAME>
                    <ECUC-FUNCTION-NAME-DEF-VARIANTS>
                        <ECUC-FUNCTION-NAME-DEF-CONDITIONAL>
                            <DEFAULT-VALUE>Init_MyModule</DEFAULT-VALUE>
                            <MIN-LENGTH>1</MIN-LENGTH>
                            <MAX-LENGTH>50</MAX-LENGTH>
                        </ECUC-FUNCTION-NAME-DEF-CONDITIONAL>
                    </ECUC-FUNCTION-NAME-DEF-VARIANTS>
                </ECUC-FUNCTION-NAME-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "InitFunction"

    def test_readEcucFunctionNameDef_without_value(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-FUNCTION-NAME-DEF>
                    <SHORT-NAME>CallbackFunc</SHORT-NAME>
                </ECUC-FUNCTION-NAME-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "CallbackFunc"
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucContainerDefParameters -v`
Expected: 12 tests pass (8 from Tasks 2-3 + 4 new)

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC Enumeration and FunctionName parameter tests"
```

---

### Task 5: TestEcucContainerDefParameters Class - Multiple Parameters

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucParamConfContainerDef` model class
- Produces: Tests covering multiple parameter types in single container (line 4576 loop)

- [ ] **Step 1: Write test for multiple parameter types in one container**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucContainerDefParameters_multiple_types(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>Enable</SHORT-NAME>
                    <DEFAULT-VALUE>true</DEFAULT-VALUE>
                </ECUC-BOOLEAN-PARAM-DEF>
                <ECUC-STRING-PARAM-DEF>
                    <SHORT-NAME>Name</SHORT-NAME>
                    <DEFAULT-VALUE>default</DEFAULT-VALUE>
                </ECUC-STRING-PARAM-DEF>
                <ECUC-INTEGER-PARAM-DEF>
                    <SHORT-NAME>Count</SHORT-NAME>
                    <DEFAULT-VALUE>5</DEFAULT-VALUE>
                </ECUC-INTEGER-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 3
        assert params[0].getShortName() == "Enable"
        assert params[1].getShortName() == "Name"
        assert params[2].getShortName() == "Count"
```

- [ ] **Step 2: Write test for unsupported parameter type with warning parser**

Add to TestEcucContainerDefParameters class:

```python
    def test_readEcucContainerDefParameters_unsupported_type_warning(self, warning_parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <PARAMETERS>
                <ECUC-UNKNOWN-PARAM-DEF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-PARAM-DEF>
                <ECUC-BOOLEAN-PARAM-DEF>
                    <SHORT-NAME>Enable</SHORT-NAME>
                </ECUC-BOOLEAN-PARAM-DEF>
            </PARAMETERS>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        warning_parser.readEcucContainerDefParameters(element, container)
        params = container.getParameters()
        assert len(params) == 1
        assert params[0].getShortName() == "Enable"
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucContainerDefParameters -v`
Expected: 14 tests pass (12 from Tasks 2-4 + 2 new)

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC multiple parameters and unsupported type tests"
```

---

### Task 6: TestEcucCommonAttributes Class

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucCommonAttributes` model class
- Produces: Tests covering `readEcucCommonAttributes` (lines 4506-4515)

- [ ] **Step 1: Write TestEcucCommonAttributes class with basic tests**

Add to the test file:

```python
class TestEcucCommonAttributes:
    """Tests for readEcucCommonAttributes handler."""

    def test_readEcucCommonAttributes_with_multiplicity(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <SHORT-NAME>ContainerDef</SHORT-NAME>
            <LOWER-MULTIPLICITY>1</LOWER-MULTIPLICITY>
            <UPPER-MULTIPLICITY>10</UPPER-MULTIPLICITY>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucCommonAttributes(element, container)
        assert container.getLowerMultiplicity().getValue() == 1
        assert container.getUpperMultiplicity().getValue() == 10

    def test_readEcucCommonAttributes_with_origin(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <SHORT-NAME>ContainerDef</SHORT-NAME>
            <ORIGIN>MANUFACTURER</ORIGIN>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucCommonAttributes(element, container)
        assert container.getOrigin() is not None
```

- [ ] **Step 2: Write tests for multiplicity config classes**

Add to TestEcucCommonAttributes class:

```python
    def test_readEcucCommonAttributes_with_multiplicity_config_classes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <SHORT-NAME>ContainerDef</SHORT-NAME>
            <MULTIPLICITY-CONFIG-CLASSES>
                <ECUC-MULTIPLICITY-CONFIGURATION-CLASS>
                    <SHORT-NAME>ConfigClass1</SHORT-NAME>
                    <CONFIG-CLASS>PRE-COMMIT</CONFIG-CLASS>
                    <CONFIG-VARIANT>VARIANT-1</CONFIG-VARIANT>
                </ECUC-MULTIPLICITY-CONFIGURATION-CLASS>
            </MULTIPLICITY-CONFIG-CLASSES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucCommonAttributes(element, container)
        cfg_classes = container.getMultiplicityConfigClasses()
        assert len(cfg_classes) == 1
        assert cfg_classes[0].getShortName() == "ConfigClass1"
```

- [ ] **Step 3: Write tests for value config classes**

Add to TestEcucCommonAttributes class:

```python
    def test_readEcucCommonAttributes_with_value_config_classes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <SHORT-NAME>ContainerDef</SHORT-NAME>
            <VALUE-CONFIG-CLASSES>
                <ECUC-VALUE-CONFIGURATION-CLASS>
                    <SHORT-NAME>ValueClass1</SHORT-NAME>
                    <CONFIG-CLASS>POST-BUILD</CONFIG-CLASS>
                    <CONFIG-VARIANT>VARIANT-2</CONFIG-VARIANT>
                </ECUC-VALUE-CONFIGURATION-CLASS>
            </VALUE-CONFIG-CLASSES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucCommonAttributes(element, container)
        cfg_classes = container.getValueConfigClasses()
        assert len(cfg_classes) == 1
        assert cfg_classes[0].getShortName() == "ValueClass1"
```

- [ ] **Step 4: Write tests for post-build variants**

Add to TestEcucCommonAttributes class:

```python
    def test_readEcucCommonAttributes_with_post_build_variants(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <SHORT-NAME>ContainerDef</SHORT-NAME>
            <POST-BUILD-VARIANT-MULTIPLICITY>true</POST-BUILD-VARIANT-MULTIPLICITY>
            <POST-BUILD-VARIANT-VALUE>false</POST-BUILD-VARIANT-VALUE>
            <REQUIRES-INDEX>true</REQUIRES-INDEX>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucCommonAttributes(element, container)
        assert container.getPostBuildVariantMultiplicity() is not None
        assert container.getPostBuildVariantMultiplicity().getValue() == True
        assert container.getPostBuildVariantValue() is not None
        assert container.getPostBuildVariantValue().getValue() == False
        assert container.getRequiresIndex() is not None
        assert container.getRequiresIndex().getValue() == True
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucCommonAttributes -v`
Expected: 5 tests pass

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC common attributes tests"
```

---

### Task 7: TestEcucContainerDefReferences Class

**Files:**
- Modify: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: `_snip()` helper, `parser` fixture, `EcucParamConfContainerDef` model class
- Produces: Tests covering `readEcucContainerDefReferences` (lines 4614-4622)

- [ ] **Step 1: Write TestEcucContainerDefReferences class with symbolic name ref tests**

Add to the test file:

```python
class TestEcucContainerDefReferences:
    """Tests for readEcucContainerDefReferences handler."""

    def test_readEcucSymbolicNameReferenceDef_with_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>TargetRef</SHORT-NAME>
                    <DESTINATION-REF DESTINATION="SomeType">/Path/To/Target</DESTINATION-REF>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "TargetRef"
        assert refs[0].getDestinationRef() is not None

    def test_readEcucSymbolicNameReferenceDef_without_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>EmptyRef</SHORT-NAME>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "EmptyRef"
        assert refs[0].getDestinationRef() is None
```

- [ ] **Step 2: Write tests for ECUC-REFERENCE-DEF**

Add to TestEcucContainerDefReferences class:

```python
    def test_readEcucReferenceDef_with_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-REFERENCE-DEF>
                    <SHORT-NAME>ComponentRef</SHORT-NAME>
                    <DESTINATION-REF DESTINATION="SwComponentType">/Components/MyComponent</DESTINATION-REF>
                </ECUC-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "ComponentRef"

    def test_readEcucReferenceDef_without_destination(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-REFERENCE-DEF>
                    <SHORT-NAME>OptionalRef</SHORT-NAME>
                </ECUC-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "OptionalRef"
        assert refs[0].getDestinationRef() is None
```

- [ ] **Step 3: Write test for unsupported reference type with warning parser**

Add to TestEcucContainerDefReferences class:

```python
    def test_readEcucContainerDefReferences_unsupported_type_warning(self, warning_parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef

        AUTOSAR.setARRelease("R23-11")
        container = EcucParamConfContainerDef(_autosar_root(), "ContainerDef")
        element = _snip(
            """
            <REFERENCES>
                <ECUC-UNKNOWN-REF-DEF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </ECUC-UNKNOWN-REF-DEF>
                <ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
                    <SHORT-NAME>ValidRef</SHORT-NAME>
                </ECUC-SYMBOLIC-NAME-REFERENCE-DEF>
            </REFERENCES>
            """,
            root_tag="ECUC-PARAM-CONF-CONTAINER-DEF",
        )
        warning_parser.readEcucContainerDefReferences(element, container)
        refs = container.getReferences()
        assert len(refs) == 1
        assert refs[0].getShortName() == "ValidRef"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py::TestEcucContainerDefReferences -v`
Expected: 5 tests pass

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: add ECUC container reference tests"
```

---

### Task 8: Verification and Coverage Check

**Files:**
- Test: `tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py`

**Interfaces:**
- Consumes: All tests from Tasks 1-7
- Produces: Coverage report showing improved coverage

- [ ] **Step 1: Run all tests**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py -v`
Expected: ~24 tests pass (14 params + 5 common + 5 refs)

- [ ] **Step 2: Run coverage report**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py --cov=armodel.parser.arxml_parser --cov-report=term-missing -q`
Expected: Coverage shows improvement in lines 4506-4595 range

- [ ] **Step 3: Verify full parser test suite still passes**

Run: `pytest tests/test_armodel/parser/ -q`
Expected: All tests pass, no regressions

- [ ] **Step 4: Final commit if needed**

```bash
git status
git add tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
git commit -m "test: complete ECUC handler test coverage"
```

---

## Success Criteria

- All ~24 tests pass
- Coverage of `readEcucContainerDefParameters`, `readEcucCommonAttributes`, `readEcucContainerDefReferences` improved
- No regressions in existing tests
- Tests follow established patterns from Phase G/H/I files