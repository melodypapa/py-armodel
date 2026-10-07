"""
Writer tests for DDS-OWNERSHIP-STRENGTH elements — DdsOwnershipStrength, Table 6.189 (p.533, R23-11).

writeDdsOwnershipStrength emits <OWNERSHIP-STRENGTH> (the object element, per the
DdsCpQosProfile.ownershipStrength aggregation) with the AR-OBJECT S/T attributes and the
OWNERSHIP-STRENGTH member (XSD group DDS-OWNERSHIP-STRENGTH, AUTOSAR_00052.xsd l.29865).

Round-trip counterpart: tests/test_armodel/parser/test_dds_ownership_strength.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsOwnershipStrength
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


def _new_ownership_strength() -> DdsOwnershipStrength:
    ownership_strength = DdsOwnershipStrength()
    ownership_strength.setOwnershipStrength(PositiveInteger().setValue("5"))
    ownership_strength.setChecksum(String().setValue("5"))
    ownership_strength.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return ownership_strength


class TestWriteDdsOwnershipStrength:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the OWNERSHIP-STRENGTH member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnershipStrength(parent, _new_ownership_strength())
        node = parent.find("OWNERSHIP-STRENGTH")
        assert node is not None
        assert node.find("OWNERSHIP-STRENGTH").text == "5"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnershipStrength(parent, _new_ownership_strength())
        node = parent.find("OWNERSHIP-STRENGTH")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnershipStrength(parent, DdsOwnershipStrength())
        node = parent.find("OWNERSHIP-STRENGTH")
        assert node is not None
        assert node.find("OWNERSHIP-STRENGTH") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsOwnershipStrength(parent, _new_ownership_strength())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsOwnershipStrength()
        ARXMLParser().readDdsOwnershipStrength(root.find("{%s}OWNERSHIP-STRENGTH" % NS), reloaded)
        assert reloaded.getOwnershipStrength().getValue() == 5
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
