"""
Writer tests for DDS-RELIABILITY elements — DdsReliability, Table 6.192 (p.535, R23-11).

writeDdsReliability emits <RELIABILITY> (the object element, per the DdsCpQosProfile.reliability
aggregation) with the AR-OBJECT S/T attributes and the two group members in XSD sequenceOffset
order (XSD group DDS-RELIABILITY, AUTOSAR_00052.xsd l.29986; facet spelling per
DDS-RELIABILITY-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_reliability.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsReliability
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsReliabilityKindEnum, Float, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_reliability() -> DdsReliability:
    reliability = DdsReliability()
    reliability.setReliabilityKind(DdsReliabilityKindEnum().setValue(DdsReliabilityKindEnum.RELIABLE))
    reliability.setReliabilityMaxBlockingTime(Float().setValue("0.5"))
    reliability.setChecksum(String().setValue("5"))
    reliability.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return reliability


class TestWriteDdsReliability:
    def test_write_emits_element_and_members_in_xsd_order(self):
        """Test that the writer emits the object element with both members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsReliability(parent, _new_reliability())
        node = parent.find("RELIABILITY")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == ["RELIABILITY-KIND", "RELIABILITY-MAX-BLOCKING-TIME"]
        assert node.find("RELIABILITY-KIND").text == "RELIABLE"
        assert node.find("RELIABILITY-MAX-BLOCKING-TIME").text == "0.5"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsReliability(parent, _new_reliability())
        node = parent.find("RELIABILITY")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsReliability(parent, DdsReliability())
        node = parent.find("RELIABILITY")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsReliability(parent, _new_reliability())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsReliability()
        ARXMLParser().readDdsReliability(root.find("{%s}RELIABILITY" % NS), reloaded)
        assert reloaded.getReliabilityKind().getValue() == DdsReliabilityKindEnum.RELIABLE
        assert reloaded.getReliabilityMaxBlockingTime().getValue() == 0.5
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
