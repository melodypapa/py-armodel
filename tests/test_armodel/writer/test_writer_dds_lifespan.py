"""
Writer tests for DDS-LIFESPAN elements — DdsLifespan, Table 6.195 (p.536, R23-11).

writeDdsLifespan emits <LIFESPAN> (the object element, per the DdsCpQosProfile.lifespan
aggregation) with the AR-OBJECT S/T attributes and the single group member (XSD group
DDS-LIFESPAN, AUTOSAR_00052.xsd l.29768).

Round-trip counterpart: tests/test_armodel/parser/test_dds_lifespan.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLifespan
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Float, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_lifespan() -> DdsLifespan:
    lifespan = DdsLifespan()
    lifespan.setLifespanDuration(Float().setValue("10.0"))
    lifespan.setChecksum(String().setValue("5"))
    lifespan.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return lifespan


class TestWriteDdsLifespan:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the group member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLifespan(parent, _new_lifespan())
        node = parent.find("LIFESPAN")
        assert node is not None
        assert node.find("LIFESPAN-DURATION").text == "10.0"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLifespan(parent, _new_lifespan())
        node = parent.find("LIFESPAN")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLifespan(parent, DdsLifespan())
        node = parent.find("LIFESPAN")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLifespan(parent, _new_lifespan())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsLifespan()
        ARXMLParser().readDdsLifespan(root.find("{%s}LIFESPAN" % NS), reloaded)
        assert reloaded.getLifespanDuration().getValue() == 10.0
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
