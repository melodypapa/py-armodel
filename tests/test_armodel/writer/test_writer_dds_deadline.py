"""
Writer tests for DDS-DEADLINE elements — DdsDeadline, Table 6.185 (p.532, R23-11).

writeDdsDeadline emits <DEADLINE> (the object element, per the DdsCpQosProfile.deadline
aggregation) with the AR-OBJECT S/T attributes and the DEADLINE-PERIOD member (XSD group
DDS-DEADLINE, AUTOSAR_00052.xsd l.29346).

Round-trip counterpart: tests/test_armodel/parser/test_dds_deadline.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDeadline
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


def _new_deadline() -> DdsDeadline:
    deadline = DdsDeadline()
    deadline.setDeadlinePeriod(Float().setValue("0.5"))
    deadline.setChecksum(String().setValue("5"))
    deadline.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return deadline


class TestWriteDdsDeadline:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the DEADLINE-PERIOD member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDeadline(parent, _new_deadline())
        node = parent.find("DEADLINE")
        assert node is not None
        assert node.find("DEADLINE-PERIOD").text == "0.5"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDeadline(parent, _new_deadline())
        node = parent.find("DEADLINE")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDeadline(parent, DdsDeadline())
        node = parent.find("DEADLINE")
        assert node is not None
        assert node.find("DEADLINE-PERIOD") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDeadline(parent, _new_deadline())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsDeadline()
        ARXMLParser().readDdsDeadline(root.find("{%s}DEADLINE" % NS), reloaded)
        assert reloaded.getDeadlinePeriod().getValue() == 0.5
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
