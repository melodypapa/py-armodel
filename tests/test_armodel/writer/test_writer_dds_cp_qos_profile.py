"""
Writer tests for DDS-CP-QOS-PROFILE elements — DdsCpQosProfile, Table 6.179 (p.529, R23-11).

writeDdsCpQosProfile emits <DDS-CP-QOS-PROFILE> with the IDENTIFIABLE level
(writeIdentifiable) and the 14 QoS policy children in XSD sequenceOffset order
(AUTOSAR_00052.xsd l.29057). Unsynced Dds* children serialize identity-only (empty
elements, Rule 0001.7 debt); the synced DdsTopicData child serializes fully.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_qos_profile.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurability, DdsTopicData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpQosProfile
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_profile() -> DdsCpQosProfile:
    profile = DdsCpQosProfile(AUTOSAR.getInstance(), "Profile1")
    profile.setDurability(DdsDurability())
    topic_data = DdsTopicData()
    topic_data.setTopicData(String().setValue("raw payload"))
    profile.setTopicData(topic_data)
    return profile


class TestWriteDdsCpQosProfile:
    def test_write_emits_children_in_xsd_order(self):
        """Test that the writer emits the children in XSD sequenceOffset order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        assert node is not None
        children = [child.tag for child in node if child.tag != "SHORT-NAME"]
        # DURABILITY before TOPIC-DATA per sequenceOffset
        assert children.index("DURABILITY") < children.index("TOPIC-DATA")

    def test_write_emits_stub_child_identity_only(self):
        """Test that an unsynced child serializes as an empty element (identity-only debt)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        durability_node = node.find("DURABILITY")
        assert durability_node is not None
        assert len(list(durability_node)) == 0

    def test_write_emits_topic_data_fully(self):
        """Test that the synced DdsTopicData child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        topic_data_node = node.find("TOPIC-DATA")
        assert topic_data_node is not None
        assert topic_data_node.find("TOPIC-DATA").text == "raw payload"

    def test_write_empty_omits_children(self):
        """Test that an empty profile emits only the SHORT-NAME."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, DdsCpQosProfile(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("DDS-CP-QOS-PROFILE")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("DEADLINE") is None
        assert node.find("TOPIC-DATA") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values (DdsTopicData child one level down)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsCpQosProfile(AUTOSAR.getInstance(), "Profile1")
        ARXMLParser().readDdsCpQosProfile(root.find("{%s}DDS-CP-QOS-PROFILE" % NS), reloaded)
        assert isinstance(reloaded.getDurability(), DdsDurability)
        assert reloaded.getTopicData() is not None
        assert reloaded.getTopicData().getTopicData().getValue() == "raw payload"
