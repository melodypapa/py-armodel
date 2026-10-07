"""
Writer tests for DDS-CP-DOMAIN elements — DdsCpDomain, Table 6.176 (p.526, R23-11).

writeDdsCpDomain creates the DDS-CP-DOMAIN element, emits the IDENTIFIABLE level
(SHORT-NAME, UUID — writeIdentifiable, called exactly once, Rule 0013.1/0025), then its own
group members in XSD sequenceOffset order (group DDS-CP-DOMAIN, AUTOSAR_00052.xsd l.28712):
DDS-PARTITIONS, DDS-TOPICS, DOMAIN-ID. Wrapper elements are emitted only when non-empty.

ddsTopic children are written via the synced writeDdsCpTopic (real coverage). ddsPartition
children are still identity-only (DdsCpPartition queued Table 6.178) — the writer emits the
empty DDS-CP-PARTITION item element; its own sync replaces the placeholder.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_domain.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpDomain
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_domain() -> DdsCpDomain:
    domain = DdsCpDomain(AUTOSAR.getInstance(), "Domain1")
    domain.createDdsPartition("Partition1")
    topic = domain.createDdsTopic("Topic1")
    topic.setTopicName(String().setValue("MyDdsTopic"))
    domain.setDomainId(PositiveInteger().setValue("1"))
    return domain


class TestWriteDdsCpDomain:
    def test_write_emits_members_in_xsd_order(self):
        """Test that the writer emits SHORT-NAME and its own members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpDomain(parent, _new_domain())

        child = parent.find("DDS-CP-DOMAIN")
        assert child is not None
        children = [c.tag for c in child]
        assert children[0] == "SHORT-NAME"
        assert child.find("SHORT-NAME").text == "Domain1"
        assert children.index("DDS-PARTITIONS") < children.index("DDS-TOPICS")
        assert children.index("DDS-TOPICS") < children.index("DOMAIN-ID")

        assert child.find("DDS-PARTITIONS/DDS-CP-PARTITION/SHORT-NAME").text == "Partition1"
        assert child.find("DDS-TOPICS/DDS-CP-TOPIC/SHORT-NAME").text == "Topic1"
        assert child.find("DDS-TOPICS/DDS-CP-TOPIC/TOPIC-NAME").text == "MyDdsTopic"
        assert child.find("DOMAIN-ID").text == "1"

    def test_write_empty_omits_members(self):
        """Test that an empty domain emits only the SHORT-NAME (wrapper lists omitted when empty)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpDomain(parent, DdsCpDomain(AUTOSAR.getInstance(), "Empty"))
        child = parent.find("DDS-CP-DOMAIN")
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_via_file(self, tmp_path):
        """Element-level round-trip: write, reload, read back via readDdsCpDomain, assert field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpDomain(parent, _new_domain())
        inner = ET.tostring(parent[0]).decode("utf-8")

        out_file = str(tmp_path / "dds_cp_domain.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_domain = DdsCpDomain(re_document, "Domain1")
        parser.readDdsCpDomain(ET.parse(out_file).getroot()[0], re_domain)

        assert re_domain.getShortName() == "Domain1"
        partitions = re_domain.getDdsPartitions()
        assert len(partitions) == 1
        assert partitions[0].getShortName() == "Partition1"
        topics = re_domain.getDdsTopics()
        assert len(topics) == 1
        assert topics[0].getShortName() == "Topic1"
        assert topics[0].getTopicName().getValue() == "MyDdsTopic"
        assert re_domain.getDomainId().getValue() == 1
