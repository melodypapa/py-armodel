"""Tests for SwcInternalBehavior ServiceNeeds and Events handlers."""
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.models import ApplicationSwComponentType
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


def _make_dependency():
    app = ApplicationSwComponentType(
        parent=_autosar_root(), short_name="App"
    )
    behavior = app.createSwcInternalBehavior("Behavior")
    return behavior.createSwcServiceDependency("Dep")


def _make_behavior():
    app = ApplicationSwComponentType(
        parent=_autosar_root(), short_name="App"
    )
    return app.createSwcInternalBehavior("Behavior")


class TestSwcServiceDependencyServiceNeeds:
    """Tests for readSwcServiceDependencyServiceNeeds branches."""

    @pytest.mark.parametrize("tag", [
        "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS",
        "DIAGNOSTIC-ROUTINE-NEEDS",
        "DIAGNOSTIC-VALUE-NEEDS",
        "DIAGNOSTIC-EVENT-NEEDS",
        "DIAGNOSTIC-EVENT-INFO-NEEDS",
        "CRYPTO-SERVICE-NEEDS",
        "ECU-STATE-MGR-USER-NEEDS",
        "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
        "DLT-USER-NEEDS",
    ])
    def test_service_needs_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_dependency()
        element = _snip(
            f"""
            <SERVICE-NEEDS>
                <{tag}>
                    <SHORT-NAME>Need</SHORT-NAME>
                </{tag}>
            </SERVICE-NEEDS>
            """,
        )
        parser.readSwcServiceDependencyServiceNeeds(element, dep)
        needs = dep.getServiceNeeds()
        assert len(needs) == 1
        assert needs[0].getShortName() == "Need"

    def test_nv_block_needs_branch(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_dependency()
        element = _snip(
            """
            <SERVICE-NEEDS>
                <NV-BLOCK-NEEDS>
                    <SHORT-NAME>NvNeed</SHORT-NAME>
                </NV-BLOCK-NEEDS>
            </SERVICE-NEEDS>
            """,
        )
        parser.readSwcServiceDependencyServiceNeeds(element, dep)
        needs = dep.getServiceNeeds()
        assert len(needs) == 1
        assert needs[0].getShortName() == "NvNeed"

    def test_unknown_service_needs_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_dependency()
        element = _snip(
            """
            <SERVICE-NEEDS>
                <UNKNOWN-NEEDS>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-NEEDS>
            </SERVICE-NEEDS>
            """,
        )
        warning_parser.readSwcServiceDependencyServiceNeeds(
            element, dep
        )
        assert len(dep.getServiceNeeds()) == 0


class TestIncludedDataTypeSets:
    """Tests for getIncludedDataTypeSets (L778-786)."""

    def test_with_data_type_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <INCLUDED-DATA-TYPE-SETS>
                <INCLUDED-DATA-TYPE-SET>
                    <DATA-TYPE-REFS>
                        <DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/dt/Type1</DATA-TYPE-REF>
                    </DATA-TYPE-REFS>
                </INCLUDED-DATA-TYPE-SET>
            </INCLUDED-DATA-TYPE-SETS>
            """,
        )
        result = parser.getIncludedDataTypeSets(element)
        assert len(result) == 1
        assert len(result[0].getDataTypeRefs()) == 1

    def test_empty_returns_empty_list(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getIncludedDataTypeSets(element)
        assert result == []


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
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = _make_behavior()
        element = _snip(
            f"""
            <EVENTS>
                <{tag}>
                    <SHORT-NAME>Event</SHORT-NAME>
                </{tag}>
            </EVENTS>
            """,
        )
        parser.readSwcInternalBehaviorEvents(element, behavior)
        event = behavior.getEvent("Event")
        assert event is not None
        assert event.getShortName() == "Event"

    def test_unknown_event_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = _make_behavior()
        element = _snip(
            """
            <EVENTS>
                <UNKNOWN-EVENT>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-EVENT>
            </EVENTS>
            """,
        )
        warning_parser.readSwcInternalBehaviorEvents(
            element, behavior
        )


class TestSwPointerTargetProps:
    """Tests for getSwPointerTargetProps and readSwPointerTargetProps."""

    def test_get_sw_pointer_target_props_with_data(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <SW-POINTER-TARGET-PROPS>
                <TARGET-CATEGORY>VALUE</TARGET-CATEGORY>
            </SW-POINTER-TARGET-PROPS>
            """,
        )
        result = parser.getSwPointerTargetProps(
            element, "SW-POINTER-TARGET-PROPS"
        )
        assert result is not None
        assert result.getTargetCategory() is not None

    def test_get_sw_pointer_target_props_empty(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getSwPointerTargetProps(
            element, "SW-POINTER-TARGET-PROPS"
        )
        assert result is None

    def test_read_sw_pointer_target_props(self, parser):
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = SwDataDefProps()
        element = _snip(
            """
            <SW-POINTER-TARGET-PROPS>
                <TARGET-CATEGORY>VALUE</TARGET-CATEGORY>
            </SW-POINTER-TARGET-PROPS>
            """,
        )
        parser.readSwPointerTargetProps(element, parent)
        assert parent.swPointerTargetProps is not None
        assert parent.swPointerTargetProps.getTargetCategory() is not None

    def test_read_sw_pointer_target_props_empty(self, parser):
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = SwDataDefProps()
        element = _snip("")
        parser.readSwPointerTargetProps(element, parent)
        assert parent.swPointerTargetProps is None


class TestParameterInAtomicSWCTypeInstanceRef:
    """Tests for getParameterInAtomicSWCTypeInstanceRef (L1278-1283)."""

    def test_with_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
                <PORT-PROTOTYPE-REF DEST="P-PORT-PROTOTYPE">/pp/Port</PORT-PROTOTYPE-REF>
                <ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST="PARAMETER-DATA-PROTOTYPE">/pdp/Param</ROOT-PARAMETER-DATA-PROTOTYPE-REF>
            </PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
            """,
        )
        result = parser.getParameterInAtomicSWCTypeInstanceRef(
            element, "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"
        )
        assert result is not None
        assert result.getPortPrototypeRef() is not None

    def test_without_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getParameterInAtomicSWCTypeInstanceRef(
            element, "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"
        )
        assert result is None


class TestModeGroupIRef:
    """Tests for getModeGroupIRef (L1386-1392)."""

    def test_p_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                    <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/pp/Port</CONTEXT-P-PORT-REF>
                    <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
                </P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = parser.getModeGroupIRef(element, "MODE-GROUP-IREF")
        assert result is not None

    def test_r_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                    <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/rp/Port</CONTEXT-R-PORT-REF>
                    <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
                </R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = parser.getModeGroupIRef(element, "MODE-GROUP-IREF")
        assert result is not None

    def test_unknown_mode_group_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <UNKNOWN-MODE-GROUP-REF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-MODE-GROUP-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = warning_parser.getModeGroupIRef(
            element, "MODE-GROUP-IREF"
        )
        assert result is None
