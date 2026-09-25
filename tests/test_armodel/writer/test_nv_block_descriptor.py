"""
Tests for writing NV-BLOCK-DESCRIPTOR elements — NvBlockDescriptor, Table 11.6 (p.670, R23-11).

NvBlockDescriptor (Base = AtpStructureElement) emits its twelve members in the XSD
group order (AUTOSAR_00052.xsd group NV-BLOCK-DESCRIPTOR): CLIENT-SERVER-PORTS →
CONSTANT-VALUE-MAPPING-REFS → DATA-TYPE-MAPPING-REFS → INSTANTIATION-DATA-DEF-PROPSS →
MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS → NV-BLOCK-DATA-MAPPINGS → NV-BLOCK-NEEDS →
RAM-BLOCK → ROM-BLOCK → SUPPORT-DIRTY-FLAG → TIMING-EVENT-REF → WRITING-STRATEGYS.
Wrappers are emitted only when non-empty; getters feed every emission.

Round-trip counterpart: tests/test_armodel/parser/test_nv_block_descriptor.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "CLIENT-SERVER-PORTS",
    "CONSTANT-VALUE-MAPPING-REFS",
    "DATA-TYPE-MAPPING-REFS",
    "INSTANTIATION-DATA-DEF-PROPSS",
    "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS",
    "NV-BLOCK-DATA-MAPPINGS",
    "NV-BLOCK-NEEDS",
    "RAM-BLOCK",
    "ROM-BLOCK",
    "SUPPORT-DIRTY-FLAG",
    "TIMING-EVENT-REF",
    "WRITING-STRATEGYS",
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
    return ARXMLWriter()


def _timing_event_ref():
    ref = RefType()
    ref.setValue("/TimingEvent")
    ref.setDest("TIMING-EVENT")
    return ref


class TestWriteNvBlockDescriptor:
    """Tests for writeNvBlockDescriptor — element order and values (Table 11.6)."""

    def test_scalar_members_emitted_in_xsd_order(self, writer):
        """Test that the scalar members are emitted after the aggregate wrappers, in XSD order."""
        descriptor = NvBlockDescriptor(None, "Desc")
        descriptor.createNvBlockNeeds("Needs")
        descriptor.createRamBlock("Ram")
        descriptor.createRomBlock("Rom")
        descriptor.setSupportDirtyFlag(Boolean().setValue(True))
        descriptor.setTimingEventRef(_timing_event_ref())

        root = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(root, descriptor)

        emitted = [child.tag for child in root.find("NV-BLOCK-DESCRIPTOR")]
        expected = ["SHORT-NAME"] + [tag for tag in XSD_ELEMENT_ORDER if tag in emitted]
        assert emitted == expected

    def test_scalar_member_values(self, writer):
        """Test that SUPPORT-DIRTY-FLAG and TIMING-EVENT-REF carry their values."""
        descriptor = NvBlockDescriptor(None, "Desc")
        descriptor.setSupportDirtyFlag(Boolean().setValue(True))
        descriptor.setTimingEventRef(_timing_event_ref())

        root = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(root, descriptor)

        node = root.find("NV-BLOCK-DESCRIPTOR")
        assert node.find("SUPPORT-DIRTY-FLAG").text == "true"
        ref = node.find("TIMING-EVENT-REF")
        assert ref.text == "/TimingEvent"
        assert ref.get("DEST") == "TIMING-EVENT"

    def test_wrappers_absent_when_empty(self, writer):
        """Test that an empty descriptor emits only the SHORT-NAME."""
        descriptor = NvBlockDescriptor(None, "Desc")

        root = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(root, descriptor)

        node = root.find("NV-BLOCK-DESCRIPTOR")
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_write_read_round_trip(self, writer):
        """Test that a written descriptor re-reads with the same field values (lossless round-trip)."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        descriptor.createNvBlockNeeds("Needs")
        descriptor.setSupportDirtyFlag(Boolean().setValue(True))
        descriptor.setTimingEventRef(_timing_event_ref())

        parent = ET.Element("PARENT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        element = parent.find("NV-BLOCK-DESCRIPTOR")
        assert element is not None
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-BLOCK-DESCRIPTOR", "NV-BLOCK-DESCRIPTOR xmlns='%s'" % NS, 1))

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        again = NvBlockDescriptor(root2, "OtherName")
        ARXMLParser().readNvBlockDescriptor(reloaded_element, again)

        assert again.getSupportDirtyFlag().getValue() is True
        assert again.getTimingEventRef().getValue() == "/TimingEvent"
        assert again.getTimingEventRef().getDest() == "TIMING-EVENT"
        assert again.getNvBlockNeeds().getShortName() == "Needs"
