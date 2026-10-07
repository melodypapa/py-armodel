"""
Writer tests for DDS-DESTINATION-ORDER elements — DdsDestinationOrder, Table 6.196 (p.536, R23-11).

writeDdsDestinationOrder emits <DESTINATION-ORDER> (the object element, per the
DdsCpQosProfile.destinationOrder aggregation) with the AR-OBJECT S/T attributes and the single
group member (XSD group DDS-DESTINATION-ORDER, AUTOSAR_00052.xsd l.29377; facet spelling per
DDS-DESTINATION-ORDER-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_destination_order.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDestinationOrder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsDestinationOrderKindEnum, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_destination_order() -> DdsDestinationOrder:
    destination_order = DdsDestinationOrder()
    destination_order.setDestinationOrderKind(DdsDestinationOrderKindEnum().setValue(DdsDestinationOrderKindEnum.BY_SOURCE_TIMESTAMP))
    destination_order.setChecksum(String().setValue("5"))
    destination_order.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return destination_order


class TestWriteDdsDestinationOrder:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the group member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDestinationOrder(parent, _new_destination_order())
        node = parent.find("DESTINATION-ORDER")
        assert node is not None
        assert node.find("DESTINATION-ORDER-KIND").text == "BY-SOURCE-TIMESTAMP"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDestinationOrder(parent, _new_destination_order())
        node = parent.find("DESTINATION-ORDER")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDestinationOrder(parent, DdsDestinationOrder())
        node = parent.find("DESTINATION-ORDER")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDestinationOrder(parent, _new_destination_order())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsDestinationOrder()
        ARXMLParser().readDdsDestinationOrder(root.find("{%s}DESTINATION-ORDER" % NS), reloaded)
        assert reloaded.getDestinationOrderKind().getValue() == DdsDestinationOrderKindEnum.BY_SOURCE_TIMESTAMP
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
