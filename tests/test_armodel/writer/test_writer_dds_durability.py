"""
Writer tests for DDS-DURABILITY elements — DdsDurability, Table 6.181 (p.530, R23-11).

writeDdsDurability emits <DURABILITY> (the object element, per the DdsCpQosProfile.durability
aggregation) with the AR-OBJECT S/T attributes and the DURABILITY-KIND member (XSD complexType
DDS-DURABILITY, AUTOSAR_00052.xsd l.29461; facet spelling per DDS-DURABILITY-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_durability.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurability
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsDurabilityKindEnum, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_durability() -> DdsDurability:
    durability = DdsDurability()
    durability.setDurabilityKind(DdsDurabilityKindEnum().setValue(DdsDurabilityKindEnum.TRANSIENT_LOCAL))
    durability.setChecksum(String().setValue("5"))
    durability.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return durability


class TestWriteDdsDurability:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the DURABILITY-KIND facet."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurability(parent, _new_durability())
        node = parent.find("DURABILITY")
        assert node is not None
        assert node.find("DURABILITY-KIND").text == "TRANSIENT-LOCAL"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurability(parent, _new_durability())
        node = parent.find("DURABILITY")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurability(parent, DdsDurability())
        node = parent.find("DURABILITY")
        assert node is not None
        assert node.find("DURABILITY-KIND") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurability(parent, _new_durability())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsDurability()
        ARXMLParser().readDdsDurability(root.find("{%s}DURABILITY" % NS), reloaded)
        assert reloaded.getDurabilityKind() is not None
        assert reloaded.getDurabilityKind().getValue() == DdsDurabilityKindEnum.TRANSIENT_LOCAL
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
