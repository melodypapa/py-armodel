"""
Writer tests for DDS-TOPIC-DATA elements — DdsTopicData, Table 6.180 (p.529, R23-11).

writeDdsTopicData emits <TOPIC-DATA> (the object element, per the DdsCpQosProfile.topicData
aggregation) with the AR-OBJECT S/T attributes and the nested string member <TOPIC-DATA>
(XSD complexType DDS-TOPIC-DATA, AUTOSAR_00052.xsd l.30691).

Round-trip counterpart: tests/test_armodel/parser/test_dds_topic_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsTopicData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_topic_data() -> DdsTopicData:
    topic_data = DdsTopicData()
    topic_data.setTopicData(String().setValue("raw topic payload"))
    topic_data.setChecksum(String().setValue("5"))
    topic_data.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return topic_data


class TestWriteDdsTopicData:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the nested string member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTopicData(parent, _new_topic_data())
        node = parent.find("TOPIC-DATA")
        assert node is not None
        assert node.find("TOPIC-DATA").text == "raw topic payload"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTopicData(parent, _new_topic_data())
        node = parent.find("TOPIC-DATA")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTopicData(parent, DdsTopicData())
        node = parent.find("TOPIC-DATA")
        assert node is not None
        assert node.find("TOPIC-DATA") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsTopicData(parent, _new_topic_data())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsTopicData()
        ARXMLParser().readDdsTopicData(root.find("{%s}TOPIC-DATA" % NS), reloaded)
        assert reloaded.getTopicData().getValue() == "raw topic payload"
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
