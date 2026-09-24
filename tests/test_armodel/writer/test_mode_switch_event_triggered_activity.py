"""
Tests for writing MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY elements — ModeSwitchEventTriggeredActivity, Table 11.7 (p.675, R23-11).

ModeSwitchEventTriggeredActivity (Base = ARObject) carries two own attributes whose
writer element order must follow the XSD sequence (AUTOSAR_00052.xsd group
MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY): ROLE → SWC-MODE-SWITCH-EVENT-REF. The
MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS wrapper is emitted only when non-empty. The
set-level round-trip goes through the NvBlockDescriptor aggregation
(writeNvBlockDescriptor dispatch → readNvBlockDescriptor dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_mode_switch_event_triggered_activity.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity, NvBlockDescriptor
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "ROLE",
    "SWC-MODE-SWITCH-EVENT-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _identifier(value):
    identifier = Identifier()
    identifier.setValue(value)
    return identifier


def _swc_mode_switch_event_ref():
    ref = RefType()
    ref.setValue("/SwcModeSwitchEvent")
    ref.setDest("SWC-MODE-SWITCH-EVENT")
    return ref


def _filled_activity():
    activity = ModeSwitchEventTriggeredActivity()
    activity.setRole(_identifier("WriteBlock"))
    activity.setSwcModeSwitchEventRef(_swc_mode_switch_event_ref())
    return activity


class TestWriteModeSwitchEventTriggeredActivity:
    """Tests for writeModeSwitchEventTriggeredActivity — own element field values (Table 11.7)."""

    def test_write_field_values(self, writer):
        """Test that both attribute elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.writeModeSwitchEventTriggeredActivity(parent, _filled_activity())

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert element is not None
        assert element.find("ROLE").text == "WriteBlock"
        ref_element = element.find("SWC-MODE-SWITCH-EVENT-REF")
        assert ref_element.text == "/SwcModeSwitchEvent"
        assert ref_element.attrib.get("DEST") == "SWC-MODE-SWITCH-EVENT"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order."""
        parent = ET.Element("PARENT")

        writer.writeModeSwitchEventTriggeredActivity(parent, _filled_activity())

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert [elem.tag for elem in element] == XSD_ELEMENT_ORDER

    def test_write_unset_activity_emits_no_children(self, writer):
        """Test that an activity without fields emits the element only, with no attribute children."""
        parent = ET.Element("PARENT")

        writer.writeModeSwitchEventTriggeredActivity(parent, ModeSwitchEventTriggeredActivity())

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert element is not None
        assert element.find("ROLE") is None
        assert element.find("SWC-MODE-SWITCH-EVENT-REF") is None

    def test_write_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        activity = ModeSwitchEventTriggeredActivity()
        checksum = String()
        checksum.setValue("abc123")
        activity.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        activity.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeModeSwitchEventTriggeredActivity(parent, activity)

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert element.attrib.get("S") == "abc123"
        assert element.attrib.get("T") is not None

    def test_round_trip_via_nv_block_descriptor(self, writer):
        """Test the writeNvBlockDescriptor → readNvBlockDescriptor aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        descriptor.addModeSwitchEventTriggeredActivity(_filled_activity())

        parent = ET.Element("PARENT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        element = parent.find("NV-BLOCK-DESCRIPTOR")
        assert element is not None
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-BLOCK-DESCRIPTOR", "NV-BLOCK-DESCRIPTOR xmlns='%s'" % NS, 1))

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = NvBlockDescriptor(root2, "OtherName")
        ARXMLParser().readNvBlockDescriptor(reloaded_element, reloaded)

        activities = reloaded.getModeSwitchEventTriggeredActivitys()
        assert len(activities) == 1
        assert activities[0].getRole().getValue() == "WriteBlock"
        assert activities[0].getSwcModeSwitchEventRef().getValue() == "/SwcModeSwitchEvent"
        assert activities[0].getSwcModeSwitchEventRef().getDest() == "SWC-MODE-SWITCH-EVENT"

    def test_round_trip_absent_activities_emit_no_wrapper(self, writer):
        """Test that a descriptor without activities emits no MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS wrapper."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")

        parent = ET.Element("PARENT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        element = parent.find("NV-BLOCK-DESCRIPTOR")
        assert element.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS") is None
