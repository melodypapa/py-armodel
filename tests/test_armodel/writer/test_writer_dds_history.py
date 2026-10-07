"""
Writer tests for DDS-HISTORY elements — DdsHistory, Table 6.198 (p.537, R23-11).

writeDdsHistory emits <HISTORY> (the object element, per the DdsCpQosProfile.history aggregation)
with the AR-OBJECT S/T attributes and the two group members in XSD sequenceOffset order (XSD group
DDS-HISTORY, AUTOSAR_00052.xsd l.29702; facet spelling per DDS-HISTORY-KIND-ENUM--SIMPLE).

Round-trip counterpart: tests/test_armodel/parser/test_dds_history.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsHistory
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsHistoryKindEnum, PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_history() -> DdsHistory:
    history = DdsHistory()
    history.setHistoryKind(DdsHistoryKindEnum().setValue(DdsHistoryKindEnum.KEEP_LAST))
    history.setHistoryOrderDepth(PositiveInteger().setValue("4"))
    history.setChecksum(String().setValue("5"))
    history.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return history


class TestWriteDdsHistory:
    def test_write_emits_element_and_members_in_xsd_order(self):
        """Test that the writer emits the object element with both members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsHistory(parent, _new_history())
        node = parent.find("HISTORY")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == ["HISTORY-KIND", "HISTORY-ORDER-DEPTH"]
        assert node.find("HISTORY-KIND").text == "KEEP-LAST"
        assert node.find("HISTORY-ORDER-DEPTH").text == "4"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsHistory(parent, _new_history())
        node = parent.find("HISTORY")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsHistory(parent, DdsHistory())
        node = parent.find("HISTORY")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsHistory(parent, _new_history())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsHistory()
        ARXMLParser().readDdsHistory(root.find("{%s}HISTORY" % NS), reloaded)
        assert reloaded.getHistoryKind().getValue() == DdsHistoryKindEnum.KEEP_LAST
        assert reloaded.getHistoryOrderDepth().getValue() == 4
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
