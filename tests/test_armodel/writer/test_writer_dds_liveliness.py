"""
Writer tests for DDS-LIVELINESS elements — DdsLiveliness, Table 6.190 (p.534, R23-11).

writeDdsLiveliness emits <LIVELINESS> (the object element, per the DdsCpQosProfile.liveliness
aggregation) with the AR-OBJECT S/T attributes and the two group members in XSD sequenceOffset
order (XSD group DDS-LIVELINESS, AUTOSAR_00052.xsd l.29799; facet spelling per
DDS-LIVENESS-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_liveliness.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLiveliness
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsLivenessKindEnum, Float, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_liveliness() -> DdsLiveliness:
    liveliness = DdsLiveliness()
    liveliness.setLivelinessLeaseDuration(Float().setValue("10.0"))
    liveliness.setLivenessKind(DdsLivenessKindEnum().setValue(DdsLivenessKindEnum.MANUAL_BY_TOPIC))
    liveliness.setChecksum(String().setValue("5"))
    liveliness.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return liveliness


class TestWriteDdsLiveliness:
    def test_write_emits_element_and_members_in_xsd_order(self):
        """Test that the writer emits the object element with both members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLiveliness(parent, _new_liveliness())
        node = parent.find("LIVELINESS")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == ["LIVELINESS-LEASE-DURATION", "LIVENESS-KIND"]
        assert node.find("LIVELINESS-LEASE-DURATION").text == "10.0"
        assert node.find("LIVENESS-KIND").text == "MANUAL-BY-TOPIC"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLiveliness(parent, _new_liveliness())
        node = parent.find("LIVELINESS")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLiveliness(parent, DdsLiveliness())
        node = parent.find("LIVELINESS")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLiveliness(parent, _new_liveliness())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsLiveliness()
        ARXMLParser().readDdsLiveliness(root.find("{%s}LIVELINESS" % NS), reloaded)
        assert reloaded.getLivelinessLeaseDuration().getValue() == 10.0
        assert reloaded.getLivenessKind().getValue() == DdsLivenessKindEnum.MANUAL_BY_TOPIC
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
