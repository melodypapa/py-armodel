# ARXML Parser & Writer 100% Test Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Increase test coverage of `src/armodel/parser/arxml_parser.py` (88.76% → 100%) and `src/armodel/writer/arxml_writer.py` (51.93% → 100%), closing ~2976 uncovered lines across ~868 gap groups.

**Architecture:** Phase M (parser) adds 11 test files extending existing patterns (inline XML snippets + `ARXMLParser.readXxx` invocation). Phase N (writer) adds 19 test files using two strategies: (a) direct `ARXMLWriter.writeXxx` invocation on built model objects, (b) round-trip integration tests (parse → write → re-parse). Each task targets a coherent AUTOSAR category.

**Tech Stack:** Python 3.8+, pytest, coverage.py, xml.etree.ElementTree, py-armodel (AUTOSAR R4.0.0 / R23-11)

## Global Constraints

- Python >= 3.8 required
- AUTOSAR release MUST be set before parse/write: `AUTOSAR.getInstance().setARRelease('R23-11')`
- Use `AUTOSAR.getInstance().new()` to reset singleton between tests
- Max line length: 79 (CI warns at 127)
- Classes: PascalCase, Methods: camelCase (AUTOSAR standard)
- Do NOT add comments unless asked
- Method chaining: setters return `self`
- Boolean values in XML must not contain spaces
- Parser options: `ARXMLParser(options={"warning": True})` for warning mode
- Writer options: `ARXMLWriter(options={'warning': True})` for warning mode
- Exclude build/ from lint (generated code)
- Each task ends with green tests + commit
- Run `python scripts/run_tests.py --coverage` for coverage reports

## Baseline Coverage

| File | Current | Missing Lines | Gap Groups |
|------|---------|---------------|------------|
| `src/armodel/parser/arxml_parser.py` | 88.76% | 505 | 228 |
| `src/armodel/writer/arxml_writer.py` | 51.93% | 2471 | 640 |
| **Total** | — | **2976** | **868** |

## Test Pattern Reference (Established)

**Parser test pattern** (from `test_arxml_parser_ecuc_handlers.py`):
```python
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

**Writer test pattern** (from `test_arxml_writer.py`):
```python
@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()

@pytest.fixture
def writer():
    return ARXMLWriter()

def _build_element(tag: str = "ROOT") -> ET.Element:
    return ET.Element(tag, xmlns="http://autosar.org/schema/r4.0")
```

---

# Phase M: Parser Remaining Coverage (505 lines)

Each task creates a new test file under `tests/test_armodel/parser/` following the established pattern. Target: 88.76% → 100% (close all 505 missing lines).

---

### Task M1: SwcInternalBehavior ServiceNeeds & Events

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:725-786, 1602-1653`

**Interfaces:**
- Consumes: `ARXMLParser`, `AUTOSAR`, `SwcInternalBehavior`, `ServiceNeeds` subtypes
- Produces: Test file covering `readSwcServiceDependencyServiceNeeds` (L732-757), `getIncludedDataTypeSets` (L779-786), `readSwcInternalBehaviorEvents` (L1618-1636), `getSwPointerTargetProps` (L1638-1645), `readSwPointerTargetProps` (L1647-1653)

**Handler methods to cover:**
- `readSwcServiceDependencyServiceNeeds` - branches for DiagnosticCommunicationManagerNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds, DiagnosticEventNeeds, DiagnosticEventInfoNeeds, CryptoServiceNeeds, EcuStateMgrUserNeeds, DtcStatusChangeNotificationNeeds, DltUserNeeds + warning branch
- `getIncludedDataTypeSets` (L778-786) - entire getter untested
- `readSwcInternalBehaviorEvents` - branches: INTERNAL-TRIGGER-OCCURRED-EVENT, INIT-EVENT, ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT, MODE-SWITCHED-ACK-EVENT, BACKGROUND-EVENT, DATA-SEND-COMPLETED-EVENT + warning branch
- `getSwPointerTargetProps` / `readSwPointerTargetProps` (L1638-1653) - entirely untested

- [ ] **Step 1: Create test file with fixtures**

```python
"""Tests for SwcInternalBehavior ServiceNeeds and Events handlers."""
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
    return ET.fromstring(
        f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>"
    )


def _autosar_root():
    return AUTOSAR.getInstance()
```

- [ ] **Step 2: Add ServiceNeeds branch tests**

```python
class TestSwcServiceDependencyServiceNeeds:
    """Tests for readSwcServiceDependencyServiceNeeds branches."""

    @pytest.mark.parametrize("tag,cls_name", [
        ("DIAG-COMMUNICATION-MANAGER-NEEDS",
         "DiagnosticCommunicationManagerNeeds"),
        ("DIAG-ROUTINE-NEEDS", "DiagnosticRoutineNeeds"),
        ("DIAG-VALUE-NEEDS", "DiagnosticValueNeeds"),
        ("DIAG-EVENT-NEEDS", "DiagnosticEventNeeds"),
        ("DIAG-EVENT-INFO-NEEDS", "DiagnosticEventInfoNeeds"),
        ("CRYPTO-SERVICE-NEEDS", "CryptoServiceNeeds"),
        ("ECU-STATE-MGR-USER-NEEDS", "EcuStateMgrUserNeeds"),
        ("DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
         "DtcStatusChangeNotificationNeeds"),
        ("DLT-USER-NEEDS", "DltUserNeeds"),
    ])
    def test_service_needs_branches(self, parser, tag, cls_name):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import (
            SwcServiceDependency,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = SwcServiceDependency(_autosar_root(), "Dep")
        element = _snip(
            f"""
            <SERVICE-NEEDS>
                <{tag}>
                    <SHORT-NAME>{cls_name}</SHORT-NAME>
                </{tag}>
            </SERVICE-NEEDS>
            """,
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        parser.readSwcServiceDependencyServiceNeeds(element, dep)
        needs = dep.getServiceNeeds()
        assert len(needs) == 1
        assert needs[0].getShortName() == cls_name

    def test_unknown_service_needs_warning(self, warning_parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import (
            SwcServiceDependency,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = SwcServiceDependency(_autosar_root(), "Dep")
        element = _snip(
            """
            <SERVICE-NEEDS>
                <UNKNOWN-NEEDS>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-NEEDS>
            </SERVICE-NEEDS>
            """,
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        warning_parser.readSwcServiceDependencyServiceNeeds(element, dep)
        assert len(dep.getServiceNeeds()) == 0
```

- [ ] **Step 3: Add getIncludedDataTypeSets tests**

```python
class TestIncludedDataTypeSets:
    """Tests for getIncludedDataTypeSets (L778-786)."""

    def test_get_included_data_type_sets_with_data(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <INCLUDED-DATA-TYPE-SETS>
                <INCLUDED-DATA-TYPE-SET>
                    <DATA-TYPES>
                        <DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/dt/Type1</DATA-TYPE-REF>
                    </DATA-TYPES>
                </INCLUDED-DATA-TYPE-SET>
            </INCLUDED-DATA-TYPE-SETS>
            """,
        )
        result = parser.getIncludedDataTypeSets(element)
        assert result is not None
        assert len(result) == 1

    def test_get_included_data_type_sets_empty(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getIncludedDataTypeSets(element)
        assert result is None or len(result) == 0
```

- [ ] **Step 4: Add SwcInternalBehaviorEvents branch tests**

```python
class TestSwcInternalBehaviorEvents:
    """Tests for readSwcInternalBehaviorEvents branches."""

    @pytest.mark.parametrize("tag", [
        "INTERNAL-TRIGGER-OCCURRED-EVENT",
        "INIT-EVENT",
        "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT",
        "MODE-SWITCHED-ACK-EVENT",
        "BACKGROUND-EVENT",
        "DATA-SEND-COMPLETED-EVENT",
    ])
    def test_event_branches(self, parser, tag):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
            SwcInternalBehavior,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = SwcInternalBehavior(_autosar_root(), "Behavior")
        element = _snip(
            f"""
            <EVENTS>
                <{tag}>
                    <SHORT-NAME>{tag.title()}</SHORT-NAME>
                </{tag}>
            </EVENTS>
            """,
        )
        parser.readSwcInternalBehaviorEvents(element, behavior)
        events = behavior.getEvents()
        assert len(events) == 1

    def test_unknown_event_warning(self, warning_parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
            SwcInternalBehavior,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = SwcInternalBehavior(_autosar_root(), "Behavior")
        element = _snip(
            """
            <EVENTS>
                <UNKNOWN-EVENT>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-EVENT>
            </EVENTS>
            """,
        )
        warning_parser.readSwcInternalBehaviorEvents(element, behavior)
        assert len(behavior.getEvents()) == 0
```

- [ ] **Step 5: Add SwPointerTargetProps tests**

```python
class TestSwPointerTargetProps:
    """Tests for getSwPointerTargetProps and readSwPointerTargetProps."""

    def test_get_sw_pointer_target_props_with_data(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <SW-POINTER-TARGET-PROPS>
                <TARGET-VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Target</TARGET-VARIABLE-REF>
            </SW-POINTER-TARGET-PROPS>
            """,
        )
        result = parser.getSwPointerTargetProps(element)
        assert result is not None

    def test_get_sw_pointer_target_props_empty(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getSwPointerTargetProps(element)
        assert result is None
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py -v`
Expected: All tests PASS (the handlers exist; tests exercise them)

- [ ] **Step 7: Verify coverage improvement**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py --cov=armodel.parser.arxml_parser --cov-report=term-missing -q`
Expected: Lines 725-786, 1602-1653 show as covered

- [ ] **Step 8: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py
git commit -m "test: add SwcInternalBehavior ServiceNeeds and Events gap tests"
```

---

### Task M2: InstanceRefs & ModeGroup Handlers

**Files:**
- Extend: `tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:1278-1283, 1386-1392`

**Handler methods to cover:**
- `getParameterInAtomicSWCTypeInstanceRef` (L1278-1283) - main path body never entered
- `getModeGroupIRef` (L1386-1392) - branches for P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF and R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF + warning branch

- [ ] **Step 1: Add ParameterInAtomicSWCTypeInstanceRef tests**

```python
class TestParameterInAtomicSWCTypeInstanceRef:
    """Tests for getParameterInAtomicSWCTypeInstanceRef (L1278-1283)."""

    def test_with_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
                <PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/p/Param</PARAMETER-REF>
            </PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
            """,
        )
        result = parser.getParameterInAtomicSWCTypeInstanceRef(element)
        assert result is not None

    def test_without_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getParameterInAtomicSWCTypeInstanceRef(element)
        assert result is None
```

- [ ] **Step 2: Add ModeGroupIRef tests**

```python
class TestModeGroupIRef:
    """Tests for getModeGroupIRef (L1386-1392)."""

    def test_p_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/pp/Port</CONTEXT-P-PORT-REF>
                <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
            </P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            """,
        )
        result = parser.getModeGroupIRef(element)
        assert result is not None

    def test_r_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/rp/Port</CONTEXT-R-PORT-REF>
                <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
            </R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            """,
        )
        result = parser.getModeGroupIRef(element)
        assert result is not None

    def test_unknown_mode_group_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <UNKNOWN-MODE-GROUP-REF>
                <SHORT-NAME>Unknown</SHORT-NAME>
            </UNKNOWN-MODE-GROUP-REF>
            """,
        )
        result = warning_parser.getModeGroupIRef(element)
        assert result is None
```

- [ ] **Step 3: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py -v`
Expected: All PASS

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_swc_behavior_gaps.py
git commit -m "test: add InstanceRefs and ModeGroup handler gap tests"
```

---

### Task M3: Port Communication Specifications (ComSpec)

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_comspec_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:2006-2068, 2143-2204`

**Handler methods to cover:**
- `getClientComSpec` (L2005)
- `getParameterRequireComSpec` (L2011-2016)
- `getQueuedReceiverComSpec` (L2019-2023)
- `getModeSwitchReceiverComSpec` (L2032-2038) - top gap
- `getNonqueuedReceiverComSpec` (L2040-2050)
- `readRequiredComSpec` (L2061-2066) - branches: MODE-SWITCH-RECEIVER-COM-SPEC, PARAMETER-REQUIRE-COM-SPEC, NV-REQUIRE-COM-SPEC + error path
- `getQueuedSenderComSpec` (L2162-2165)
- `getModeSwitchedAckRequest` (L2167-2173) - top gap
- `getModeSwitchSenderComSpec` (L2175-2180)
- `getNvProvideComSpec` (L2182-2188) - top gap
- `readProvidedComSpec` (L2197-2202) - branches: QUEUED-SENDER-COM-SPEC, MODE-SWITCH-SENDER-COM-SPEC, NV-PROVIDE-COM-SPEC + error path

- [ ] **Step 1: Create test file with fixtures** (same fixture pattern as M1)

- [ ] **Step 2: Add ComSpec getter tests**

```python
class TestComSpecGetters:
    """Tests for ComSpec getter methods."""

    def test_get_mode_switch_receiver_com_spec(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-SWITCH-RECEIVER-COM-SPEC>
                <OPERATION>
                    <DISABLED-MODE-REF DEST="MODE-DECLARATION">/md/Disabled</DISABLED-MODE-REF>
                </OPERATION>
            </MODE-SWITCH-RECEIVER-COM-SPEC>
            """,
        )
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None

    def test_get_mode_switched_ack_request(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-SWITCHED-ACK-REQUEST>
                <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/pp/Port</CONTEXT-P-PORT-REF>
            </MODE-SWITCHED-ACK-REQUEST>
            """,
        )
        result = parser.getModeSwitchedAckRequest(element)
        assert result is not None

    def test_get_nv_provide_com_spec(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <NV-PROVIDE-COM-SPEC>
                <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</DATA-ELEMENT-REF>
            </NV-PROVIDE-COM-SPEC>
            """,
        )
        result = parser.getNvProvideComSpec(element)
        assert result is not None
```

- [ ] **Step 3: Add readRequiredComSpec and readProvidedComSpec branch tests**

```python
class TestRequiredProvidedComSpec:
    """Tests for readRequiredComSpec and readProvidedComSpec branches."""

    @pytest.mark.parametrize("tag", [
        "MODE-SWITCH-RECEIVER-COM-SPEC",
        "PARAMETER-REQUIRE-COM-SPEC",
        "NV-REQUIRE-COM-SPEC",
    ])
    def test_required_com_spec_branches(self, parser, tag):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import (
            RPortPrototype,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        port = RPortPrototype(_autosar_root(), "RPort")
        element = _snip(
            f"""
            <REQUIRED-COM-SPECS>
                <{tag}>
                    <SHORT-NAME>{tag.title()}</SHORT-NAME>
                </{tag}>
            </REQUIRED-COM-SPECS>
            """,
        )
        parser.readRequiredComSpec(element, port)

    def test_required_com_spec_unknown_raises(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import (
            RPortPrototype,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        port = RPortPrototype(_autosar_root(), "RPort")
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <UNKNOWN-COM-SPEC>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """,
        )
        with pytest.raises(ValueError):
            parser.readRequiredComSpec(element, port)

    @pytest.mark.parametrize("tag", [
        "QUEUED-SENDER-COM-SPEC",
        "MODE-SWITCH-SENDER-COM-SPEC",
        "NV-PROVIDE-COM-SPEC",
    ])
    def test_provided_com_spec_branches(self, parser, tag):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.components import (
            PPortPrototype,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        port = PPortPrototype(_autosar_root(), "PPort")
        element = _snip(
            f"""
            <PROVIDED-COM-SPECS>
                <{tag}>
                    <SHORT-NAME>{tag.title()}</SHORT-NAME>
                </{tag}>
            </PROVIDED-COM-SPECS>
            """,
        )
        parser.readProvidedComSpec(element, port)
```

- [ ] **Step 4: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_comspec_gaps.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_comspec_gaps.py
git commit -m "test: add ComSpec handler gap tests"
```

---

### Task M4: End-to-End Protection

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_e2e_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:2815-2831`

**Handler methods to cover:**
- `readEndToEndProtectionEndToEndProtectionISignalIPdus` (L2815-2820) - main branch + warning
- `readEndToEndProtection` (L2825-2831) - entire handler untested

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add E2E protection tests**

```python
class TestEndToEndProtection:
    """Tests for EndToEndProtection handlers."""

    def test_read_e2e_protection_isignal_ipdus(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
            EndToEndProtection,
        )
        e2e = EndToEndProtection(_autosar_root(), "E2E")
        element = _snip(
            """
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
                <END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
                    <I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/pdu/Signal</I-SIGNAL-I-PDU-REF>
                </END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
            </END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
            """,
        )
        parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(
            element, e2e
        )

    def test_read_e2e_protection(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
            EndToEndProtectionSet,
        )
        e2e_set = EndToEndProtectionSet(_autosar_root(), "E2ESet")
        element = _snip(
            """
            <END-TO-END-PROTECTIONS>
                <END-TO-END-PROTECTION>
                    <SHORT-NAME>E2EProtection</SHORT-NAME>
                    <END-TO-END-PROFILE>
                        <PROFILE-NAME>Profile1</PROFILE-NAME>
                    </END-TO-END-PROFILE>
                </END-TO-END-PROTECTION>
            </END-TO-END-PROTECTIONS>
            """,
        )
        parser.readEndToEndProtection(element, e2e_set)
```

- [ ] **Step 3: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_e2e_gaps.py -v`
Expected: All PASS

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_e2e_gaps.py
git commit -m "test: add EndToEndProtection handler gap tests"
```

---

### Task M5: Multiplexed IPdu & Dynamic/Static Parts

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_multiplexed_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:3632-3782`

**Handler methods to cover (L3632-3782):**
- `readMultiplexedPartSegmentPositions` (L3632-3637)
- `readMultiplexedPart` (L3641-3642)
- `readDynamicPartAlternative` (L3644-3647)
- `readDynamicPartDynamicPartAlternatives` (L3649-3657)
- `readDynamicPart` (L3659-3661)
- `readMultiplexedIPduDynamicParts` (L3663-3671)
- `readStaticPart` (L3673-3675)
- `readMultiplexedIPduStaticParts` (L3677-3685)
- `readMultiplexedIPdu` (L3687-3696)
- `readUserDefinedIPdu`, `readUserDefinedPdu`, `readGeneralPurposePdu`, `readGeneralPurposeIPdu` (L3698-3714)
- `readSecureCommunicationAuthenticationProps` (L3716-3719)
- `readSecureCommunicationPropsSetAuthenticationProps` (L3721-3728)
- `readSecureCommunicationFreshnessProps` (L3730-3733)
- `readSecureCommunicationPropsSetFreshnessProps` (L3735-3742)
- `readSecureCommunicationPropsSet` (L3744-3748)
- `readSoAdRoutingGroup` (L3750-3753)
- `readDoIpLogicAddress` (L3755-3757)
- `readDoIpTpConfigDoIpLogicAddresses` (L3759-3766)
- `readDoIpTpConnection` (L3768-3772)
- `readDoIpTpConfigTpConnections` (L3774-3782)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add MultiplexedIPdu tests** (provide tests for each handler listed above, following the established inline XML pattern. Use `IPdu` or `MultiplexedIPdu` model objects as targets.)

- [ ] **Step 3: Add SecureCommunication tests** (provide tests for `readSecureCommunicationAuthenticationProps`, `readSecureCommunicationPropsSetAuthenticationProps`, `readSecureCommunicationFreshnessProps`, `readSecureCommunicationPropsSetFreshnessProps`, `readSecureCommunicationPropsSet`)

- [ ] **Step 4: Add DoIp tests** (provide tests for `readDoIpLogicAddress`, `readDoIpTpConfigDoIpLogicAddresses`, `readDoIpTpConnection`, `readDoIpTpConfigTpConnections`)

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_multiplexed_gaps.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_multiplexed_gaps.py
git commit -m "test: add MultiplexedIPdu and SecureCommunication handler gap tests"
```

---

### Task M6: Network Management & LIN TP

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_nm_tp_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:4039-4049, 4220-4243`

**Handler methods to cover:**
- `readUdpNmEcu` (L4038-4039)
- `readBusDependentNmEcus` (L4041-4049) - main branch + warning
- `readLinTpConfigTpConnections` (L4218-4226)
- `readLinTpNode` (L4228-4234)
- `readLinTpConfigTpNodes` (L4236-4243)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add UdpNm and BusDependentNm tests**

```python
class TestNmEcuHandlers:
    def test_read_udp_nm_ecu(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <UDP-NM-ECU>
                <SHORT-NAME>UdpNmEcu</SHORT-NAME>
            </UDP-NM-ECU>
            """,
        )
        parser.readUdpNmEcu(element, _autosar_root())

    def test_read_bus_dependent_nm_ecus(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <BUS-DEPENDENT-NM-ECUS>
                <UDP-NM-ECU>
                    <SHORT-Name>NmEcu</SHORT-NAME>
                </UDP-NM-ECU>
            </BUS-DEPENDENT-NM-ECUS>
            """,
        )
        parser.readBusDependentNmEcus(element, _autosar_root())
```

- [ ] **Step 3: Add LinTp tests** (follow same pattern for `readLinTpConfigTpConnections`, `readLinTpNode`, `readLinTpConfigTpNodes`)

- [ ] **Step 4: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_nm_tp_gaps.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_nm_tp_gaps.py
git commit -m "test: add NM and LIN TP handler gap tests"
```

---

### Task M7: CAN Controller FD & Coupling Port

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_can_eth_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:4744-4873`

**Handler methods to cover:**
- `getCanControllerFdConfiguration` (L4743-4749) - note: has TODO/incomplete impl, test lightly
- `getCanControllerFdConfigurationRequirements` (L4751-4765)
- `readAbstractCanCommunicationControllerCanControllerAttributes` (L4780-4788)
- `readCouplingPortDetailsCouplingPortStructuralElements` (L4811-4821) - top gap
- `readCouplingPortDetailsEthernetPriorityRegenerations` (L4827-4834)
- `getCouplingPortDetails` (L4836-4844)
- `readVlanMembership` / `readCouplingPortVlanMemberships` (L4846-4857)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add CAN FD tests** (test `getCanControllerFdConfiguration` and `getCanControllerFdConfigurationRequirements` with child elements present)

- [ ] **Step 3: Add CouplingPort tests** (test `readCouplingPortDetailsCouplingPortStructuralElements` with COUPLING-PORT-FIFO and COUPLING-PORT-SCHEDULER branches, `readCouplingPortDetailsEthernetPriorityRegenerations`, `getCouplingPortDetails`, `readVlanMembership`, `readCouplingPortVlanMemberships`)

- [ ] **Step 4: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_can_eth_gaps.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_can_eth_gaps.py
git commit -m "test: add CAN FD and CouplingPort handler gap tests"
```

---

### Task M8: ECUC Module Configuration Values

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_ecuc_values_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:5128-5229`

**Handler methods to cover:**
- `getEcucInstanceReferenceValue` (L5127-5131)
- `readEcucContainerValueReferenceValues` (L5133-5141) - branches + warning
- `readEcucContainerValue` (L5143-5145)
- `readEcucContainerValueEcucContainerValue` (L5147-5148)
- `readEcucContainerValueSubContainers` (L5150-5162)
- `readEcucModuleConfigurationValuesEcucContainerValue` (L5164-5170)
- `readEcucModuleConfigurationValuesContainers` (L5172-5184)
- `readEcucModuleConfigurationValues` (L5164-5184)
- `readPhysicalDimension` (L5186-5196)
- `readISignalGroup*` family (L5197-5229)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add ECUC container value tests** (test each readEcuc*Value handler with inline XML)

- [ ] **Step 3: Add PhysicalDimension tests**

- [ ] **Step 4: Add ISignalGroup tests** (test `readISignalGroupTransformationISignalProps` with END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS branch + warning)

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_ecuc_values_gaps.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_ecuc_values_gaps.py
git commit -m "test: add ECUC module configuration values gap tests"
```

---

### Task M9: System Mapping & Type Mapping

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_system_mapping_gaps.py`
- Target: `src/armodel/parser/arxml_parser.py:5374-5419`

**Handler methods to cover:**
- `readSenderRecRecordElementMapping` (L5373-5377)
- `readSenderRecArrayTypeMappingRecordElementMapping` (L5379-5387) - branch + warning
- `readSenderRecRecordTypeMapping` (L5389-5391)
- `readSenderReceiverToSignalGroupMappingTypeMapping` (L5393-5402) - top gap
- `readSystemMappingDataMappings` (L5409-5421) - branches + warning

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add SystemMapping tests** (test each handler with inline XML for SENDER-RECEIVER-TO-SIGNAL-MAPPING and SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING branches)

- [ ] **Step 3: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_system_mapping_gaps.py -v`
Expected: All PASS

- [ ] **Step 4: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_system_mapping_gaps.py
git commit -m "test: add SystemMapping and TypeMapping handler gap tests"
```

---

### Task M10: Parser Remaining Small Gaps Sweep

**Files:**
- Create: `tests/test_armodel/parser/test_arxml_parser_remaining_gaps.py`
- Target: All remaining uncovered lines in `arxml_parser.py` not covered by M1-M9

**Handler methods to cover (remaining small gaps):**
- L305, L603-623, L687-692 (various helpers)
- L732-757 (remaining ServiceNeeds branches if any)
- L813, L840-848 (helpers)
- L1025, L1166, L1179-1180, L1209
- L1370-1429 (various)
- L1618-1653 (remaining)
- L1827, L1943
- L2122-2149 (small ComSpec gaps)
- L2231, L2345, L2370
- L2423-2455
- L2685-2697, L2784
- L2835-2839
- L2982-3121
- L3148-3277
- L3363-3505
- L3607-3717
- L3808-3981
- L4039-4049 (if any remaining)
- L4072-4311
- L4461-4802
- L4873-5034
- L5081-5601

- [ ] **Step 1: Run coverage report to identify exact remaining gaps**

Run: `pytest tests/test_armodel/parser/ --cov=armodel.parser.arxml_parser --cov-report=term-missing -q > remaining_gaps.txt`
Expected: List of remaining uncovered lines

- [ ] **Step 2: Create test file and add tests for each remaining gap** (use the inline XML pattern, group by handler method)

- [ ] **Step 3: Run tests and verify coverage**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_remaining_gaps.py -v`
Expected: All PASS

- [ ] **Step 4: Verify parser coverage reaches ~99%+**

Run: `pytest tests/test_armodel/parser/ --cov=armodel.parser.arxml_parser --cov-report=term-missing -q`
Expected: Coverage >= 99% (some lines may be unreachable defensive code)

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/test_arxml_parser_remaining_gaps.py
git commit -m "test: add parser remaining gap sweep tests"
```

---

### Task M11: Verify Parser 100% Coverage

- [ ] **Step 1: Run full parser coverage report**

Run: `python scripts/run_tests.py --coverage`
Expected: `arxml_parser.py` coverage >= 99% (target 100%)

- [ ] **Step 2: Identify any remaining uncovered lines**

If 100%: Task complete, proceed to Phase N
If <100%: Examine remaining lines, add targeted tests

- [ ] **Step 3: Add final targeted tests for any remaining lines**

- [ ] **Step 4: Re-run coverage and verify 100%**

Run: `python scripts/run_tests.py --coverage`
Expected: `arxml_parser.py` coverage = 100% (or as close as possible, noting any genuinely unreachable code)

- [ ] **Step 5: Commit final parser coverage tests**

```bash
git add tests/test_armodel/parser/
git commit -m "test: achieve 100% parser coverage"
```

---

# Phase N: Writer Coverage (2471 lines)

Each task creates a new test file under `tests/test_armodel/writer/`. Target: 51.93% → 100% (close all 2471 missing lines).

**Writer test strategies:**
1. **Direct method test**: Build model object → call `writer.writeXxx(elem, obj)` → assert XML structure
2. **Round-trip test**: Parse ARXML → write back → re-parse → compare (use existing `tests/integration_tests/` pattern)
3. **Warning branch test**: Use `ARXMLWriter(options={'warning': True})` + unsupported types

---

### Task N1: Writer Common Structure & Documentation

**Files:**
- Create: `tests/test_armodel/writer/test_writer_common_structure.py`
- Target: `src/armodel/writer/arxml_writer.py:240-918, 4065-4158, 5812-5837`

**Handler methods to cover:**
- `setShortName`, `writeSds`, `writeSdgCaption`, `writeSdgSdxRefs`, `setSdg` (L240-282)
- `writeAdminDataSdgs` (L282)
- `writeReferrable` (L297)
- `setLanguageSpecific`, `setLLongName`, `setMultiLongName` (L301-318)
- `writeMultilanguageReferrable` (L328)
- `writeModification`, `writeDocRevision*`, `writeAdminDataDocRevisions`, `setAdminData` (L343-390)
- `writeIdentifiable`, `writeARElement` (L390-398)
- `writeLParagraphs`, `setMultiLanguageParagraphs`, `setListElement`, `setGraphic`, `writeMlFigure*`, `setMlFigures` (L845-898)
- `writeDocumentationBlock` (L898)
- `writeGeneralAnnotation`, `setAnnotations` (L907-918)
- `writeCollection*` (L4065-4087)
- `writeKeyword*` (L4088-4118)
- `writePortPrototypeBlueprint` (L4120)
- `writeModeDeclarationMapping*` (L4127-4157)
- `writeDescribable` (L5812)

- [ ] **Step 1: Create test file with fixtures** (writer fixture pattern)

- [ ] **Step 2: Add Sdg/AdminData tests** (build Sdg/Sd/AdminData/DocRevision/Modification objects, call writers, assert XML)

- [ ] **Step 3: Add Documentation tests** (build LLongName/MultilanguageLongName/Annotation objects, call writers)

- [ ] **Step 4: Add Collection/Keyword/Blueprint tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_common_structure.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_common_structure.py
git commit -m "test: add writer common structure and documentation tests"
```

---

### Task N2: Writer SW Component & Communication

**Files:**
- Create: `tests/test_armodel/writer/test_writer_sw_component.py`
- Target: `src/armodel/writer/arxml_writer.py:401-841`

**Handler methods to cover:**
- `writeTransmissionAcknowledgementRequest` (L401)
- `writeSenderComSpec`, `writeNonqueuedSenderComSpec`, `writeQueuedSenderComSpec` (L408-452)
- `writeTransformationComSpecProps`, `writeUserDefinedTransformationComSpecProps`, `writeServerComSpec*` (L426-445)
- `setModeSwitchedAckRequest`, `writeModeSwitchSenderComSpec` (L457-463)
- `writeNvProvideComSpec`, `writePPortComSpec` (L470-478)
- `writeCompositeNetworkRepresentation` (L499)
- `writeReceiverComSpec`, `writeNonqueuedReceiverComSpec`, `writeQueuedReceiverComSpec` (L506-614)
- `writeClientComSpec`, `writeParameterRequireComSpec`, `writeNvRequireComSpec` (L620-633)
- `setModeSwitchReceiverComSpec`, `writeRPortComSpec` (L640-648)
- `writePPortPrototype`, `writeRPortPrototype`, `writePRPortPrototype` (L664-693)
- `writeSwComponentTypePorts`, `writePortGroup*`, `writeSwComponentTypePortGroups`, `writeSwComponentType` (L701-749)
- `writeSwComponentPrototype` (L754)
- `writeCompositionSwComponentType*` family (L759-841)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add ComSpec writer tests** (build ComSpec objects, call writers, assert XML elements)

- [ ] **Step 3: Add PortPrototype writer tests**

- [ ] **Step 4: Add SwComponentType and Composition tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_sw_component.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_sw_component.py
git commit -m "test: add writer SW component and communication tests"
```

---

### Task N3: Writer DataDefProps, DataTypes & CompuMethod

**Files:**
- Create: `tests/test_armodel/writer/test_writer_data_types.py`
- Target: `src/armodel/writer/arxml_writer.py:919-1201`

**Handler methods to cover:**
- `setSwAxisIndividual`, `setSwAxisGrouped`, `setSwCalprmAxis`, `setSwCalprmAxisSet`, `setSwPointerTargetProps`, `setSwDataDefProps` (L919-982)
- `writeApplicationPrimitiveDataType`, `writeDataPrototype`, `writeApplicationRecordElement`, `writeApplicationRecordDataType*` (L983-1033)
- `setBaseTypeDirectDefinition`, `writeSwBaseType` (L1034-1041)
- `writeCompuScale*`, `setCompuConstContent`, `setCompuScales`, `setCompuConst`, `setCompu`, `writeCompuMethod` (L1046-1115)
- `writeApplicationValueSpecification`, `writeRecordValueSpecification`, `writeConstantSpecification` (L1123-1151)
- `setInternalConstrs`, `setPhysConstrs`, `writeDataConstrRules`, `writeDataConstr` (L1158-1188)
- `writeUnit` (L1193)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add SwDataDefProps and SwAxis tests**

- [ ] **Step 3: Add DataType writer tests**

- [ ] **Step 4: Add CompuMethod and ValueSpecification tests**

- [ ] **Step 5: Add DataConstr and Unit tests**

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_data_types.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_data_types.py
git commit -m "test: add writer data types and compu method tests"
```

---

### Task N4: Writer SWC Internal Behavior

**Files:**
- Create: `tests/test_armodel/writer/test_writer_swc_behavior.py`
- Target: `src/armodel/writer/arxml_writer.py:1202-1923`

**Handler methods to cover:**
- Event writers: `writeTimingEvent`, `writeOperationInvokedEvent`, `writeSwcModeSwitchEvent`, `writeDataReceivedEvent`, `writeInternalTriggerOccurredEvent`, `writeInitEvent`, `writeAsynchronousServerCallReturnsEvent`, `writeModeSwitchedAckEvent`, `writeBackgroundEvent`, `writeDataSendCompletedEvent` (L1226-1287)
- `writeSwcInternalBehaviorEvents` (L1293) - dispatch
- `writeExclusiveAreas`, `writeDataTypeMappingRefs`, `writeInternalBehaviorStaticMemories`, `writeInternalBehavior` (L1322-1345)
- `setVariableInAtomicSWCTypeInstanceRef`, `setAutosarVariableRef`, `writeVariableAccess` (L1352-1374)
- `setParameterInAtomicSWCTypeInstanceRef`, `setAutosarParameterRef`, `writeParameterAccess` (L1379-1394)
- `writeRunnableEntity*` family (L1399-1590)
- `writeSwcInternalBehaviorRunnables`, `writeSwcInternalBehaviorArTypedPerInstanceMemories`, `writeSwcInternalBehaviorExplicitInterRunnableVariables`, `writeSwcInternalBehaviorPerInstanceMemories` (L1591-1621)
- `writeParameterDataPrototype`, `writeSwcInternalBehaviorParameterDataPrototypes`, `writePortDefinedArgumentValues`, `writeSwcInternalBehaviorPortAPIOptions` (L1633-1653)
- `writeServiceDependency*` family (L1665-1716)
- `writeServiceNeeds`, `writeNvBlockNeeds` (L1717-1742)
- Diagnostic ServiceNeeds writers (L1744-1815)
- `writeSwcServiceDependencyServiceNeeds` (L1820) - dispatch
- `writeSwcInternalBehavior` (L1897) - hub

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add event writer tests** (test each event type writer)

- [ ] **Step 3: Add VariableAccess and ParameterAccess tests**

- [ ] **Step 4: Add RunnableEntity tests**

- [ ] **Step 5: Add ServiceNeeds and ServiceDependency tests**

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_swc_behavior.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_swc_behavior.py
git commit -m "test: add writer SWC internal behavior tests"
```

---

### Task N5: Writer Implementation, E2E & PortInterfaces

**Files:**
- Create: `tests/test_armodel/writer/test_writer_impl_e2e_ports.py`
- Target: `src/armodel/writer/arxml_writer.py:1923-2179`

**Handler methods to cover:**
- `writeArtifactDescriptors`, `writeCode`, `writeCodeDescriptors` (L1933-1959)
- `setMemorySectionOptions`, `writeMemorySections` (L1960-1980)
- `setStackUsage`, `setRoughEstimateStackUsage`, `writeStackUsages`, `setResourceConsumption`, `writeImplementation`, `writeSwcImplementation` (L1981-2022)
- `writeEndToEndDescriptionDataIds`, `setEndToEndDescription` (L2023-2041)
- `writeEndToEndProtection*` family (L2042-2105)
- `writeAutosarDataPrototype`, `writeVariableDataPrototype` (L2111-2115)
- `writeSenderReceiverInterface*` (L2115-2140)
- `writeModeDeclarationGroupPrototype` (L2156)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add Implementation and ResourceConsumption tests**

- [ ] **Step 3: Add EndToEndProtection tests**

- [ ] **Step 4: Add PortInterface tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_impl_e2e_ports.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_impl_e2e_ports.py
git commit -m "test: add writer implementation, E2E, and port interface tests"
```

---

### Task N6: Writer BSW Module Template

**Files:**
- Create: `tests/test_armodel/writer/test_writer_bsw_module.py`
- Target: `src/armodel/writer/arxml_writer.py:2148-2571`

**Handler methods to cover:**
- `writeBswModuleDescriptionImplementedEntryRefs` (L2148)
- `writeBswModuleDescriptionProvidedModeGroups`, `writeBswModuleDescriptionRequiredModeGroups` (L2161-2179)
- `writeCanEnterExclusiveAreaRefs`, `writeExecutableEntity` (L2181-2193)
- `writeBswModuleEntity*` family (L2194-2243)
- `writeBswModuleCallPoint`, `writeBswAsynchronousServerCallPoint`, `writeBswSynchronousServerCallPoint`, `writeBswModuleEntityCallPoints` (L2244-2268)
- `writeBswModuleEntity`, `writeBswCalledEntity`, `writeBswSchedulableEntity`, `setBswInterruptEntity` (L2269-2295)
- `writeBswInternalBehaviorEntities` (L2296) - dispatch
- `writeBswEvent*` family (L2310-2353)
- `writeBswInternalBehaviorEvents` (L2354) - dispatch
- `setBswModeSenderPolicy`, `writeBswInternalBehaviorModeSenderPolicy`, `writeBswInternalBehaviorIncludedModeDeclarationGroupSets` (L2374-2395)
- `writeBswApiOptions`, `writeBswDataReceptionPolicy`, `writeBswQueuedDataReceptionPolicy`, `writeBswInternalBehaviorReceptionPolicies` (L2396-2418)
- `writeBswInternalTriggeringPoint`, `writeBswInternalBehaviorInternalTriggeringPoints`, `writeBswInternalBehavior`, `writeBswModuleDescriptionInternalBehaviors` (L2419-2452)
- `writeTrigger`, `writeBswModuleDescriptionReleasedTriggers`, `writeBswModuleDescriptionRequiredTriggers`, `writeBswModuleDescriptionProvidedDatas`, `writeBswModuleDescriptionRequiredDatas` (L2453-2496)
- `writeBswModuleClientServerEntry`, `writeBswModuleDescriptionProvidedClientServerEntries`, `writeBswModuleDescriptionRequiredClientServerEntries`, `writeBswModuleDescription` (L2497-2524)
- `setSwServiceArg`, `writeBswModuleEntryArguments`, `writeBswModuleEntryReturnType`, `writeBswModuleEntry` (L2540-2571)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add BswModuleDescription and BswInternalBehavior tests**

- [ ] **Step 3: Add BswModuleEntity and BswEvent tests**

- [ ] **Step 4: Add BswModuleEntry tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_bsw_module.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_bsw_module.py
git commit -m "test: add writer BSW module template tests"
```

---

### Task N7: Writer ImplementationTypes, PortInterfaces & Mappings

**Files:**
- Create: `tests/test_armodel/writer/test_writer_impl_types_ports.py`
- Target: `src/armodel/writer/arxml_writer.py:2573-2966`

**Handler methods to cover:**
- `setSwcBswRunnableMapping`, `writeSwcBswRunnableMappings`, `writeSwcBswMapping` (L2573-2588)
- `writeEngineeringObject`, `writeAutosarEngineeringObject`, `writeArtifactDescriptor`, `writeBswImplementation*`, `writeBswImplementation` (L2596-2624)
- `writeAbstractImplementationDataTypeElement`, `writeImplementationDataTypeElement*`, `writeImplementationDataTypeSubElements`, `writeImplementationProps`, `writeSymbolProps`, `writeImplementationDataTypeSymbolProps`, `writeImplementationDataType` (L2633-2678)
- `writeArgumentDataPrototype`, `writeClientServerOperation*`, `writeClientServerInterfaceOperations` (L2687-2726)
- `writeApplicationError`, `writePossibleErrors`, `writePortInterface`, `writeDataInterface`, `writeParameterInterface`, `writeNvDataInterface*`, `writeClientServerInterface` (L2727-2773)
- `writeApplicationSwComponentType`, `writeEcuAbstractionSwComponentType`, `setApplicationArrayElement`, `writeApplicationArrayDataType` (L2780-2798)
- `setSwRecordLayoutV`, `writeSwRecordLayoutGroup*`, `setSwRecordLayoutGroup`, `writeSwRecordLayout`, `writeSwAddrMethod`, `writeTriggerInterface`, `writeServiceSwComponentType` (L2805-2855)
- `writeDataTypeMaps`, `writeModeRequestTypeMaps`, `writeDataTypeMappingSet` (L2860-2880)
- `setModeDeclaration`, `writeModeDeclarationGroup*`, `writeModeSwitchInterface*` (L2887-2915)
- `setEOCExecutableEntityRefSuccessorRefs`, `writeEOCExecutableEntityRef`, `writeExecutionOrderConstraint*`, `writeTimingRequirements`, `writeTimingExtension`, `writeSwcTiming` (L2921-2961)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add SwcBswMapping and BswImplementation tests**

- [ ] **Step 3: Add ImplementationDataType and PortInterface tests**

- [ ] **Step 4: Add DataTypeMapping and ModeDeclaration tests**

- [ ] **Step 5: Add Timing tests**

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_impl_types_ports.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_impl_types_ports.py
git commit -m "test: add writer implementation types and port interface tests"
```

---

### Task N8: Writer Network Management

**Files:**
- Create: `tests/test_armodel/writer/test_writer_nm.py`
- Target: `src/armodel/writer/arxml_writer.py:2967-3171`

**Handler methods to cover:**
- `writePduToFrameMappings`, `writeFrame`, `writeLinUnconditionalFrame` (L2967-2983)
- `writeNmNode` (L2988), `writeCanNmNode` (L3007), `writeUdpNmNode` (L3016)
- `writeNmClusterNmNodes` (L3022) - dispatch
- `writeCanNmClusterCoupling`, `writeUdpNmClusterCoupling`, `writeNmConfigNmClusterCouplings` (L3034-3053)
- `writeNmCluster` (L3066), `writeCanNmCluster` (L3075) - large body, ~19 attrs
- `writeUdpNmCluster` (L3095) - large body, ~13 attrs
- `writeNmConfigNmClusters` (L3112) - dispatch
- `writeUdpNmEcu`, `writeBusDependentNmEcus`, `writeNmEcu` (L3124-3139)
- `writeNmConfigNmIfEcus`, `writeNmConfig` (L3154-3164)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add NmNode tests** (build NmNode/CanNmNode/UdpNmNode, call writers, assert XML)

- [ ] **Step 3: Add NmCluster tests** (build CanNmCluster/UdpNmCluster with all optional attrs set, call writers)

- [ ] **Step 4: Add NmConfig tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_nm.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_nm.py
git commit -m "test: add writer network management tests"
```

---

### Task N9: Writer PDUs & Transport Protocol

**Files:**
- Create: `tests/test_armodel/writer/test_writer_pdu_tp.py`
- Target: `src/armodel/writer/arxml_writer.py:3172-3428`

**Handler methods to cover:**
- `writeISignalToIPduMapping`, `writeNmPduISignalToIPduMappings`, `writeNmPdu`, `writeNPdu`, `writeDcmIPdu` (L3172-3203)
- `setSecureCommunicationProps`, `writeSecuredIPdu` (L3209-3222)
- `writeTpConfig`, `writeCanTpAddress`, `writeCanTpConfigTpAddresses`, `writeCanTpChannel`, `writeCanTpConfigTpChannels` (L3232-3260)
- `writeTpConnection`, `writeTpConnectionReceiverRefs` (L3270-3277)
- `writeCanTpConnection` (L3284) - large body, ~19 attrs
- `writeCanTpConfigTpConnections` (L3305) - dispatch
- `writeCanTpEcu`, `writeCanTpConfigTpEcus`, `writeCanTpNode`, `writeCanTpConfigTpNodes`, `writeCanTpConfig` (L3315-3352)
- `writeTpAddress`, `writeLinTpConfigTpAddresses`, `writeLinTpConnection`, `writeLinTpConfigTpConnections`, `writeLinTpNode`, `writeLinTpConfigTpNodes`, `writeLinTpConfig` (L3362-3421)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add PDU writer tests** (NmPdu, NPdu, DcmIPdu, SecuredIPdu)

- [ ] **Step 3: Add CanTp tests** (CanTpConnection with all attrs, CanTpConfig)

- [ ] **Step 4: Add LinTp tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_pdu_tp.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_pdu_tp.py
git commit -m "test: add writer PDU and transport protocol tests"
```

---

### Task N10: Writer Frame Triggering & Physical Channel

**Files:**
- Create: `tests/test_armodel/writer/test_writer_frame_channel.py`
- Target: `src/armodel/writer/arxml_writer.py:3429-4021, 4022-4063`

**Handler methods to cover:**
- `writeFrameTriggering`, `writeCanFrameTriggering`, `writeLinFrameTriggering` (L3429-3456)
- `writeCommunicationCycle`, `writeCycleRepetition` (L3463-3466)
- `writeFlexrayAbsolutelyScheduledTiming*`, `writeFlexrayFrameTriggering*` (L3473-3499)
- `writeISignalTriggering`, `writePduTriggering` (L3508-3538)
- `writePhysicalChannel*`, `writeCanPhysicalChannel` (L3538-3588)
- `writeScheduleTableEntry`, `writeLinScheduleTable*`, `writeLinPhysicalChannel*` (L3593-3630)
- `writeNetworkEndPoint*`, `writeEthernetPhysicalChannelNetworkEndPoints` (L3647-3710)
- `writeSocketConnectionBundle*`, `writeSoAdConfigConnectionBundles` (L3711-3728)
- `writeUdpTp`, `writeTcpTp`, `writeGenericTp`, `writeTransportProtocolConfiguration` (L3744-3762)
- `writeConsumedEventGroup*`, `writeConsumedServiceInstance*` (L3776-3818)
- `writeSocketAddressApplicationEndpointConsumedServiceInstances` (L3826) - dispatch
- `writeEventHandler*`, `writeProvidedServiceInstance*`, `writeSocketAddress*`, `writeSoAdConfig*` (L3854-3940)
- `writeEthernetPhysicalChannel*`, `writeFlexrayPhysicalChannel`, `writeCommunicationCluster*` (L3946-3983)
- `writeAbstractCanCluster`, `writeLinCluster`, `writeCanCluster` (L3996-4011)
- `writeFlexrayCluster` (L4022-4063) - very large body, ~32 attrs

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add FrameTriggering tests**

- [ ] **Step 3: Add PhysicalChannel tests** (Can, Lin, Ethernet, Flexray)

- [ ] **Step 4: Add SoAd tests**

- [ ] **Step 5: Add CommunicationCluster tests** (Can, Lin, Flexray - set all optional attrs)

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_frame_channel.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_frame_channel.py
git commit -m "test: add writer frame triggering and physical channel tests"
```

---

### Task N11: Writer ECUC Parameter Definition Template

**Files:**
- Create: `tests/test_armodel/writer/test_writer_ecuc_def.py`
- Target: `src/armodel/writer/arxml_writer.py:4159-4398`

**Handler methods to cover:**
- `writeEcucDefinitionElement`, `writeEcucModuleDefSupportedConfigVariants` (L4159-4165)
- `writeEcucAbstractConfigurationClass`, `writeEcucMultiplicityConfigurationClass`, `writeEcucValueConfigurationClass`, `writeEcucCommonAttributes`, `writeEcucParameterDef` (L4172-4214)
- `writeEcucBooleanParamDef`, `writeEcucAbstractStringParamDef`, `writeEcucStringParamDef`, `writeEcucIntegerParamDef`, `writeEcucFloatParamDef`, `writeEcucEnumerationLiteralDef`, `writeEcucEnumerationParamDefLiterals`, `writeEcucEnumerationParamDef`, `writeEcucFunctionNameDef` (L4220-4274)
- `writeEcucContainerDefParameters`, `writeEcucContainerDef`, `writeEcucAbstractReferenceDef`, `writeEcucAbstractInternalReferenceDef`, `writeEcucSymbolicNameReferenceDef`, `writeEcucReferenceDef`, `writeEcucContainerDefReferences`, `writeEcucContainerDefSubContainers`, `writeEcucParamConfContainerDef`, `writeEcucChoiceContainerDefChoices`, `writeEcucChoiceContainerDef`, `writeEcucModuleDefContainers`, `writeEcucModuleDef` (L4285-4391)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add EcucParamDef writer tests** (Boolean, String, Integer, Float, Enumeration, FunctionName)

- [ ] **Step 3: Add EcucContainerDef and EcucModuleDef tests**

- [ ] **Step 4: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_ecuc_def.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/writer/test_writer_ecuc_def.py
git commit -m "test: add writer ECUC parameter definition tests"
```

---

### Task N12: Writer Ethernet/CAN Controllers & EcuInstance

**Files:**
- Create: `tests/test_armodel/writer/test_writer_controllers_ecu.py`
- Target: `src/armodel/writer/arxml_writer.py:4400-4704`

**Handler methods to cover:**
- `writeMacMulticastGroup`, `writeEthernetClusterMacMulticastGroups`, `writeEthernetCluster` (L4400-4420)
- `writeCanFrame` (L4426)
- `writeCommConnectorPort`, `writeFramePort`, `writeIPduPort`, `writeISignalPort` (L4431-4446)
- `writeCommunicationConnectorEcuCommPortInstances` (L4451) - dispatch
- `writeCommunicationController` (L4466)
- `setCanControllerFdConfiguration`, `setCanControllerFdConfigurationRequirements`, `writeAbstractCanCommunicationControllerAttributes`, `writeCanControllerConfigurationRequirements`, `writeAbstractCanCommunicationControllerCanControllerAttributes`, `writeAbstractCanCommunicationController`, `writeCanCommunicationController` (L4469-4516)
- `writeCouplingPort*` (L4524-4548)
- `writeEthernetPriorityRegeneration`, `writeCouplingPortDetailsEthernetPriorityRegenerations`, `setCouplingPortDetails` (L4550-4573)
- `writeVlanMembership`, `writeCouplingPortVlanMemberships`, `writeCouplingPort`, `writeEthernetCommunicationControllerCouplingPorts`, `writeEthernetCommunicationController` (L4574-4606)
- `writeEcuInstanceCommControllers` (L4616) - dispatch
- `writeCommunicationConnector*`, `writeCanCommunicationConnector`, `writeEthernetCommunicationConnector*`, `writeLinCommunicationConnector`, `writeFlexrayCommunicationConnector` (L4632-4661)
- `writeEcuInstanceConnectors` (L4663) - dispatch
- `writeEcuInstanceAssociatedComIPduGroupRefs`, `writeEcuInstance` (L4683-4704)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add EthernetCluster and CAN controller tests**

- [ ] **Step 3: Add CouplingPort tests**

- [ ] **Step 4: Add EcuInstance tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_controllers_ecu.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_controllers_ecu.py
git commit -m "test: add writer controllers and EcuInstance tests"
```

---

### Task N13: Writer System, Mapping, PhysicalDimension & FlatMap

**Files:**
- Create: `tests/test_armodel/writer/test_writer_system_mapping.py`
- Target: `src/armodel/writer/arxml_writer.py:4705-5029`

**Handler methods to cover:**
- `writeSystemSignalGroup` (L4705)
- `writeSenderReceiverToSignalMapping*`, `writeSenderRecCompositeTypeMapping`, `writeSenderRecRecordElementMapping`, `writeSenderRecArrayTypeMappingRecordElementMapping`, `writeSenderRecRecordTypeMapping`, `writeSenderReceiverToSignalGroupMappingTypeMapping`, `writeSenderReceiverToSignalGroupMapping` (L4715-4761)
- `writeSystemMappingDataMappings` (L4763) - dispatch
- `setSwcToEcuMapping`, `writeSystemMappingSwMappings`, `writeEcuMapping`, `writeSystemMappingEcuResourceMappings`, `writeSwcToImplMapping`, `writeSystemMappingSwImplMappings` (L4775-4833)
- `writeSystemMapping`, `writeSystemMappings`, `writeRootSwCompositionPrototype`, `writeSystemFibexElementRefs`, `writeSystem` (L4834-4879)
- `writePhysicalDimension` (L4881)
- `setFlatInstanceDescriptor`, `writeFlatMapInstances`, `writeFlatMap` (L4893-4910)
- `setDataPrototypeMapping`, `setDataPrototypeMappings`, `writeVariableAndParameterInterfaceMapping`, `writeClientServerOperationMapping`, `writeClientServerInterfaceMappingOperationMappings`, `writeClientServerInterfaceMapping`, `writeModeInterfaceMappingModeMapping`, `writeModeInterfaceMapping`, `writePortInterfaceMappings`, `writePortInterfaceMappingSet` (L4916-4988)
- `setISignalMappings`, `setTargetIPduRef`, `setIPduMappings`, `writeGateway`, `writeISignal` (L4990-5029)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add SystemMapping tests**

- [ ] **Step 3: Add PhysicalDimension and FlatMap tests**

- [ ] **Step 4: Add PortInterfaceMappingSet tests**

- [ ] **Step 5: Add Gateway and ISignal tests**

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_system_mapping.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_system_mapping.py
git commit -m "test: add writer system mapping and flat map tests"
```

---

### Task N14: Writer ECUC Values & Variant Handling

**Files:**
- Create: `tests/test_armodel/writer/test_writer_ecuc_values_variant.py`
- Target: `src/armodel/writer/arxml_writer.py:5030-5228`

**Handler methods to cover:**
- `writeEcucValueCollectionEcucValues`, `writeEcucValueCollection` (L5030-5038)
- `writeEcucContainerValueSubContainers` (L5045)
- `writeEcucParameterValue`, `writeEcucContainerValueParameterValues`, `writeEcucAbstractReferenceValue`, `writeEcucContainerValueReferenceValues`, `writeEcucContainValue`, `writeEcucModuleConfigurationValuesContainers`, `writeEcucModuleConfigurationValues` (L5055-5139)
- `writeSwSystemconst`, `writeSwSystemconstValue`, `writeSwSystemconstantValueSetSwSystemconstantValues`, `writeSwSystemconstantValueSet` (L5148-5167)
- `writePredefinedVariantIncludedVariantRefs`, `writePredefinedVariantPostBuildVariantCriterionValueSetRefs`, `writePredefinedVariantSwSystemconstantValueSetRefs`, `writePredefinedVariant` (L5173-5218)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add EcucValueCollection tests**

- [ ] **Step 3: Add EcucContainerValue and ParameterValue tests**

- [ ] **Step 4: Add SwSystemconst and PredefinedVariant tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_ecuc_values_variant.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_ecuc_values_variant.py
git commit -m "test: add writer ECUC values and variant handling tests"
```

---

### Task N15: Writer ISignalGroup, SystemSignal & Diagnostic

**Files:**
- Create: `tests/test_armodel/writer/test_writer_signals_diagnostic.py`
- Target: `src/armodel/writer/arxml_writer.py:5230-5383`

**Handler methods to cover:**
- `writeISignalGroupISignalRef`, `writeISignalGroupComBasedSignalGroupTransformation`, `writeTransformationISignalProps`, `writeEndToEndTransformationISignalPropsDataIds`, `writeEndToEndTransformationISignalProps`, `writeISignalGroupTransformationISignalProps`, `writeISignalGroup`, `writeISignalIPduGroup`, `writeSystemSignal`, `writeGenericEthernetFrame` (L5230-5311)
- `setLifeCyclePeriod`, `writeLifeCycleInfoUseInsteadRefs`, `writeLifeCycleInfo`, `writeLifeCycleInfoSetLifeCycleInfos`, `writeLifeCycleInfoSet` (L5313-5345)
- `writeDiagnosticConnectionFunctionalRequestRefs`, `writeDiagnosticConnection`, `writeDiagnosticServiceTableDiagnosticConnectionRefs`, `writeDiagnosticServiceTable` (L5355-5378)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add ISignalGroup and SystemSignal tests**

- [ ] **Step 3: Add LifeCycle tests**

- [ ] **Step 4: Add Diagnostic tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_signals_diagnostic.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_signals_diagnostic.py
git commit -m "test: add writer signals and diagnostic tests"
```

---

### Task N16: Writer PDUs (Extended), SecureComm, SoAd & DoIp

**Files:**
- Create: `tests/test_armodel/writer/test_writer_pdu_secure_soad.py`
- Target: `src/armodel/writer/arxml_writer.py:5385-5576`

**Handler methods to cover:**
- `writePdu`, `writeIPdu` (L5385-5392)
- `writeSegmentPosition`, `writeMultiplexedPartSegmentPositions`, `writeMultiplexedPart` (L5393-5411)
- `writeDynamicPartAlternative`, `writeDynamicPartDynamicPartAlternatives`, `writeDynamicPart`, `writeMultiplexedIPduDynamicParts`, `writeStaticPart`, `writeMultiplexedIPduStaticParts`, `writeMultiplexedIPdu` (L5413-5468)
- `writeUserDefinedIPdu`, `writeUserDefinedPdu`, `writeGeneralPurposePdu`, `writeGeneralPurposeIPdu` (L5470-5490)
- `writeSecureCommunicationAuthenticationProps`, `writeSecureCommunicationPropsSetAuthenticationProps`, `writeSecureCommunicationFreshnessProps`, `writeSecureCommunicationPropsSetFreshnessProps`, `writeSecureCommunicationPropsSet` (L5492-5524)
- `writeSoAdRoutingGroup`, `writeDoIpLogicAddress`, `writeDoIpTpConfigDoIpLogicAddresses`, `writeDoIpTpConnection`, `writeDoIpTpConfigTpConnections`, `writeDoIpTpConfig` (L5531-5571)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add MultiplexedIPdu and extended PDU tests**

- [ ] **Step 3: Add SecureCommunication tests**

- [ ] **Step 4: Add SoAd and DoIp tests**

- [ ] **Step 5: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_pdu_secure_soad.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_armodel/writer/test_writer_pdu_secure_soad.py
git commit -m "test: add writer PDU, secure comm, and SoAd tests"
```

---

### Task N17: Writer HW Element, LinMaster, Flexray & DataTransformation

**Files:**
- Create: `tests/test_armodel/writer/test_writer_hw_lin_flexray_transform.py`
- Target: `src/armodel/writer/arxml_writer.py:5578-5864`

**Handler methods to cover:**
- `writeHwDescriptionEntityHwCategoryRefs`, `writeHwDescriptionEntity`, `writeHwPinGroup`, `writeHwElementHwPinGroups`, `writeHwElement`, `writeHwAttributeDef`, `writeHwCategoryHwAttributeDef`, `writeHwCategory`, `writeHwType` (L5578-5633)
- `writeLinCommunicationController`, `writeLinMaster` (L5638-5651)
- `writeISignalToPduMappings` (L5652)
- `setDataFilter`, `setTransmissionModeConditions`, `setTimeRangeType`, `setEventControlledTiming`, `setCyclicTiming`, `setTransmissionModeTiming`, `setTransmissionModeDeclaration`, `setISignalIPduIPduTimingSpecification` (L5666-5717)
- `writeISignalIPdu` (L5719)
- `writeFlexrayFrame` (L5728)
- `writeFlexrayCommunicationController` (L5734-5764) - large body, ~23 attrs
- `writeDataTransformationTransformerChainRefs`, `writeDataTransformation`, `writeDataTransformationSetDataTransformations`, `writeDataTransformationSetTransformationTechnologies` (L5766-5798)
- `writeBufferPropertiesBufferComputation`, `setBufferProperties`, `writeDescribable`, `writeTransformationDescription`, `writeEndToEndTransformationDescription` (L5800-5837) - large body
- `writeTransformationTechnologyTransformationDescriptions`, `writeTransformationTechnology`, `writeDataTransformationSet` (L5839-5864)

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add HwElement and HwCategory tests**

- [ ] **Step 3: Add LinMaster and ISignalIPdu tests**

- [ ] **Step 4: Add FlexrayFrame and FlexrayCommunicationController tests** (set all optional attrs)

- [ ] **Step 5: Add DataTransformation tests**

- [ ] **Step 6: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_hw_lin_flexray_transform.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/test_armodel/writer/test_writer_hw_lin_flexray_transform.py
git commit -m "test: add writer HW, Lin, Flexray, and transformation tests"
```

---

### Task N18: Writer ARPackage Dispatch & Top-Level

**Files:**
- Create: `tests/test_armodel/writer/test_writer_arpackage_dispatch.py`
- Target: `src/armodel/writer/arxml_writer.py:5866-6085`

**Handler methods to cover:**
- `writeARPackageElement` (L5866) - huge dispatch router, ~60 isinstance branches
- `writeReferenceBases` (L6034)
- `writeARPackage` (L6046)
- `writeARPackageElements` (L6055)
- `writeARPackages` (L6063)
- `save` (L6072) - entry point

- [ ] **Step 1: Create test file with fixtures**

- [ ] **Step 2: Add ARPackageElement dispatch tests** (build each ARElement subtype, call writeARPackageElement, assert XML created)

```python
class TestARPackageElementDispatch:
    """Tests for writeARPackageElement dispatch router."""

    @pytest.mark.parametrize("element_type,element_class", [
        ("APPLICATION_PRIMITIVE_DATA_TYPE", "ApplicationPrimitiveDataType"),
        ("SW-BASE-TYPE", "SwBaseType"),
        ("COMPU-METHOD", "CompuMethod"),
        # ... add all ~60 element types
    ])
    def test_dispatch(self, writer, element_type, element_class):
        # Build element, call writeARPackageElement, assert XML
        pass

    def test_unknown_element_warning(self):
        writer = ARXMLWriter(options={'warning': True})
        # Build unsupported element type, call writeARPackageElement
        # assert notImplemented is called (no exception in warning mode)
        pass
```

- [ ] **Step 3: Add top-level save/write tests**

- [ ] **Step 4: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_arpackage_dispatch.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/writer/test_writer_arpackage_dispatch.py
git commit -m "test: add writer ARPackage dispatch and top-level tests"
```

---

### Task N19: Writer Remaining Gaps Sweep

**Files:**
- Create: `tests/test_armodel/writer/test_writer_remaining_gaps.py`
- Target: All remaining uncovered lines in `arxml_writer.py` not covered by N1-N18

- [ ] **Step 1: Run coverage report to identify exact remaining gaps**

Run: `pytest tests/test_armodel/writer/ --cov=armodel.writer.arxml_writer --cov-report=term-missing -q > writer_remaining_gaps.txt`
Expected: List of remaining uncovered lines

- [ ] **Step 2: Create test file and add tests for each remaining gap** (use the direct method test pattern, group by handler method)

- [ ] **Step 3: Run tests and verify coverage**

Run: `pytest tests/test_armodel/writer/test_writer_remaining_gaps.py -v`
Expected: All PASS

- [ ] **Step 4: Verify writer coverage reaches ~99%+**

Run: `pytest tests/test_armodel/writer/ --cov=armodel.writer.arxml_writer --cov-report=term-missing -q`
Expected: Coverage >= 99%

- [ ] **Step 5: Commit**

```bash
git add tests/test_armodel/writer/test_writer_remaining_gaps.py
git commit -m "test: add writer remaining gap sweep tests"
```

---

### Task N20: Verify Writer 100% Coverage

- [ ] **Step 1: Run full writer coverage report**

Run: `python scripts/run_tests.py --coverage`
Expected: `arxml_writer.py` coverage >= 99% (target 100%)

- [ ] **Step 2: Identify any remaining uncovered lines**

If 100%: Task complete
If <100%: Examine remaining lines, add targeted tests

- [ ] **Step 3: Add final targeted tests for any remaining lines**

- [ ] **Step 4: Re-run coverage and verify 100%**

Run: `python scripts/run_tests.py --coverage`
Expected: `arxml_writer.py` coverage = 100% (or as close as possible)

- [ ] **Step 5: Commit final writer coverage tests**

```bash
git add tests/test_armodel/writer/
git commit -m "test: achieve 100% writer coverage"
```

---

### Task F1: Final Verification & Cleanup

- [ ] **Step 1: Run full test suite with coverage**

Run: `python scripts/run_tests.py --coverage`
Expected: Both `arxml_parser.py` and `arxml_writer.py` at ~100% coverage

- [ ] **Step 2: Run lint check**

Run: `npm run flake8`
Expected: No errors (warnings OK for line length)

- [ ] **Step 3: Verify no test regressions**

Run: `python scripts/run_tests.py`
Expected: All tests pass

- [ ] **Step 4: Clean up temporary files**

Remove any `coverage.json`, `coverage.xml`, temporary gap analysis files created during planning.

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "chore: final coverage verification and cleanup"
```

---

## Summary

| Phase | Tasks | Target | Coverage Gain |
|-------|-------|--------|---------------|
| M (Parser) | 11 tasks | 88.76% → 100% | +505 lines |
| N (Writer) | 20 tasks | 51.93% → 100% | +2471 lines |
| F (Final) | 1 task | Verify & cleanup | — |
| **Total** | **32 tasks** | — | **+2976 lines** |

## Notes

1. **Unreachable code:** Some lines may be genuinely unreachable (defensive code, dead branches). The plan targets 100% but accepts 99%+ if specific lines are proven unreachable.

2. **Incomplete implementation:** `getCanControllerFdConfiguration` (parser L4743-4749) has a TODO. Test lightly - the object is created but not populated.

3. **`raiseError` vs `notImplemented`:** Two parser paths use `raiseError` (strict): `readRequiredComSpec` (L2068) and `readProvidedComSpec` (L2204). Tests must use `pytest.raises(ValueError)`.

4. **Writer dispatch router:** `writeARPackageElement` (L5866) is the largest single method (~166 lines, ~60 branches). Task N18 is dedicated to it.

5. **Network category:** The writer's network handlers (Flexray, CanTp, CanNm, etc.) have the largest attribute-heavy bodies. Tasks N8-N10 and N12 are the highest-effort tasks.
