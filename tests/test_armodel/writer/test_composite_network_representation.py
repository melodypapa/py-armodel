"""
Tests for writing COMPOSITE-NETWORK-REPRESENTATION elements — CompositeNetworkRepresentation, Table 4.74 (p.181, R23-11).

Writer element order must follow the XSD sequenceOffset (AUTOSAR_00052.xsd group
COMPOSITE-NETWORK-REPRESENTATION: LEAF-ELEMENT-IREF → NETWORK-REPRESENTATION). The
LEAF-ELEMENT-IREF inner refs are written flat under the element (fixed-concrete iref).
The COMPOSITE-NETWORK-REPRESENTATIONS wrapper is emitted on the owning comspec only
when the list is non-empty. The comspec-level round-trip goes through
QueuedReceiverComSpec.

Round-trip counterpart: tests/test_armodel/parser/test_composite_network_representation.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import CompositeNetworkRepresentation, QueuedReceiverComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _make_representation():
    representation = CompositeNetworkRepresentation()
    iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
    iref.setRootDataPrototypeRef(_ref("/pkg/root"))
    iref.addContextDataPrototypeRef(_ref("/pkg/ctx1"))
    iref.addContextDataPrototypeRef(_ref("/pkg/ctx2"))
    iref.setTargetDataPrototypeRef(_ref("/pkg/leaf"))
    representation.setLeafElementIRef(iref)
    props = SwDataDefProps()
    props.setBaseTypeRef(_ref("/pkg/uint8"))
    representation.setNetworkRepresentation(props)
    return representation


class TestWriteCompositeNetworkRepresentation:
    """Tests for writeCompositeNetworkRepresentation — own element field values (Table 4.74)."""

    def test_write_field_values(self, writer):
        """Test that LEAF-ELEMENT-IREF inner refs and NETWORK-REPRESENTATION are emitted with the field values."""
        parent = ET.Element("PARENT")

        writer.writeCompositeNetworkRepresentation(parent, _make_representation())

        child = parent.find("COMPOSITE-NETWORK-REPRESENTATION")
        assert child is not None
        iref_element = child.find("LEAF-ELEMENT-IREF")
        assert iref_element is not None
        assert iref_element.find("ROOT-DATA-PROTOTYPE-REF").text == "/pkg/root"
        context_refs = iref_element.findall("CONTEXT-DATA-PROTOTYPE-REF")
        assert [ref.text for ref in context_refs] == ["/pkg/ctx1", "/pkg/ctx2"]
        assert iref_element.find("TARGET-DATA-PROTOTYPE-REF").text == "/pkg/leaf"
        network_element = child.find("NETWORK-REPRESENTATION")
        assert network_element is not None
        conditional = network_element.find("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        assert conditional is not None
        assert conditional.find("BASE-TYPE-REF").text == "/pkg/uint8"

    def test_write_element_order_matches_xsd(self, writer):
        """Test that the emitted own elements follow the XSD group order."""
        parent = ET.Element("PARENT")

        writer.writeCompositeNetworkRepresentation(parent, _make_representation())

        child = parent.find("COMPOSITE-NETWORK-REPRESENTATION")
        tags = [c.tag for c in child]
        assert tags == ["LEAF-ELEMENT-IREF", "NETWORK-REPRESENTATION"]

    def test_write_none_representation_emits_nothing(self, writer):
        """Test that a None representation emits no COMPOSITE-NETWORK-REPRESENTATION element."""
        parent = ET.Element("PARENT")

        writer.writeCompositeNetworkRepresentation(parent, None)

        assert len(parent) == 0

    def test_write_unset_fields_emits_empty_element(self, writer):
        """Test that a set-but-unfilled representation emits the element without child elements."""
        parent = ET.Element("PARENT")

        writer.writeCompositeNetworkRepresentation(parent, CompositeNetworkRepresentation())

        child = parent.find("COMPOSITE-NETWORK-REPRESENTATION")
        assert child is not None
        assert len(child) == 0


class TestCompositeNetworkRepresentationRoundTrip:
    """Round-trip through the QueuedReceiverComSpec aggregation (write → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that the representation field values survive a comspec-level write/read cycle."""
        com_spec = QueuedReceiverComSpec()
        com_spec.addCompositeNetworkRepresentation(_make_representation())

        parent = ET.Element("PARENT")
        writer.writeQueuedReceiverComSpec(parent, com_spec)
        com_spec_element = parent.find("QUEUED-RECEIVER-COM-SPEC")

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("QUEUED-RECEIVER-COM-SPEC", "QUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getQueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        representations = reloaded.getCompositeNetworkRepresentations()
        assert len(representations) == 1
        representation = representations[0]
        iref = representation.getLeafElementIRef()
        assert iref is not None
        assert iref.getRootDataPrototypeRef().getValue() == "/pkg/root"
        assert [ref.getValue() for ref in iref.getContextDataPrototypeRefs()] == ["/pkg/ctx1", "/pkg/ctx2"]
        assert iref.getTargetDataPrototypeRef().getValue() == "/pkg/leaf"
        assert representation.getNetworkRepresentation() is not None
        assert representation.getNetworkRepresentation().getBaseTypeRef().getValue() == "/pkg/uint8"

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

        representation = CompositeNetworkRepresentation()
        checksum = String()
        checksum.setValue("abc123")
        representation.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        representation.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeCompositeNetworkRepresentation(parent, representation)
        element = parent.find("COMPOSITE-NETWORK-REPRESENTATION")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("COMPOSITE-NETWORK-REPRESENTATION", "COMPOSITE-NETWORK-REPRESENTATION xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getCompositeNetworkRepresentation(reloaded_element)
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_absent_representations(self, writer):
        """Test that an empty list emits no COMPOSITE-NETWORK-REPRESENTATIONS wrapper and reloads as []."""
        com_spec = QueuedReceiverComSpec()

        parent = ET.Element("PARENT")
        writer.writeQueuedReceiverComSpec(parent, com_spec)
        com_spec_element = parent.find("QUEUED-RECEIVER-COM-SPEC")
        assert com_spec_element.find("COMPOSITE-NETWORK-REPRESENTATIONS") is None

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("QUEUED-RECEIVER-COM-SPEC", "QUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getQueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getCompositeNetworkRepresentations() == []
