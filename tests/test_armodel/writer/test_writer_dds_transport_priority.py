"""
Writer tests for DDS-TRANSPORT-PRIORITY elements — DdsTransportPriority, Table 6.194 (p.535, R23-11).

writeDdsTransportPriority emits <TRANSPORT-PRIORITY> (the object element, per the
DdsCpQosProfile.transportPriority aggregation) with the AR-OBJECT S/T attributes and the single
group member (XSD group DDS-TRANSPORT-PRIORITY, AUTOSAR_00052.xsd l.30704).

Round-trip counterpart: tests/test_armodel/parser/test_dds_transport_priority.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsTransportPriority
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_transport_priority() -> DdsTransportPriority:
    transport_priority = DdsTransportPriority()
    transport_priority.setTransportPriority(PositiveInteger().setValue("4"))
    transport_priority.setChecksum(String().setValue("5"))
    transport_priority.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return transport_priority


class TestWriteDdsTransportPriority:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the group member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTransportPriority(parent, _new_transport_priority())
        node = parent.find("TRANSPORT-PRIORITY")
        assert node is not None
        assert node.find("TRANSPORT-PRIORITY").text == "4"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTransportPriority(parent, _new_transport_priority())
        node = parent.find("TRANSPORT-PRIORITY")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTransportPriority(parent, DdsTransportPriority())
        node = parent.find("TRANSPORT-PRIORITY")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTransportPriority(parent, _new_transport_priority())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsTransportPriority()
        ARXMLParser().readDdsTransportPriority(root.find("{%s}TRANSPORT-PRIORITY" % NS), reloaded)
        assert reloaded.getTransportPriority().getValue() == 4
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
