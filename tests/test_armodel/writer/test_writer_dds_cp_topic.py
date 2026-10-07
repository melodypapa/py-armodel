"""
Writer tests for DDS-CP-TOPIC elements — DdsCpTopic, Table 6.177 (p.527, R23-11).

writeDdsCpTopic emits <DDS-CP-TOPIC> with the IDENTIFIABLE level (SHORT-NAME, UUID —
writeIdentifiable) and the group members DDS-PARTITION-REF, TOPIC-NAME in XSD
sequenceOffset order (AUTOSAR_00052.xsd l.29324).

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_topic.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpTopic
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_topic() -> DdsCpTopic:
    topic = DdsCpTopic(AUTOSAR.getInstance(), "Topic1")
    topic.setDdsPartitionRef(RefType().setDest("DDS-CP-PARTITION").setValue("/DdsCpConfig/Domains/Domain1/Partitions/Partition1"))
    topic.setTopicName(String().setValue("MyDdsTopic"))
    return topic


class TestWriteDdsCpTopic:
    def test_write_emits_element_short_name_and_members(self):
        """Test that the writer emits the element with SHORT-NAME and both members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpTopic(parent, _new_topic())
        node = parent.find("DDS-CP-TOPIC")
        assert node is not None
        children = [child.tag for child in node]
        assert children[0] == "SHORT-NAME"
        assert node.find("SHORT-NAME").text == "Topic1"
        assert children.index("DDS-PARTITION-REF") < children.index("TOPIC-NAME")
        partition_ref = node.find("DDS-PARTITION-REF")
        assert partition_ref.attrib["DEST"] == "DDS-CP-PARTITION"
        assert partition_ref.text == "/DdsCpConfig/Domains/Domain1/Partitions/Partition1"
        assert node.find("TOPIC-NAME").text == "MyDdsTopic"

    def test_write_empty_omits_members(self):
        """Test that an empty topic emits only the SHORT-NAME (Identifiable level)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpTopic(parent, DdsCpTopic(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("DDS-CP-TOPIC")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("DDS-PARTITION-REF") is None
        assert node.find("TOPIC-NAME") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpTopic(parent, _new_topic())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsCpTopic(AUTOSAR.getInstance(), "Topic1")
        ARXMLParser().readDdsCpTopic(root.find("{%s}DDS-CP-TOPIC" % NS), reloaded)
        assert reloaded.getShortName() == "Topic1"
        assert reloaded.getDdsPartitionRef().getValue() == "/DdsCpConfig/Domains/Domain1/Partitions/Partition1"
        assert reloaded.getDdsPartitionRef().getDest() == "DDS-CP-PARTITION"
        assert reloaded.getTopicName().getValue() == "MyDdsTopic"
