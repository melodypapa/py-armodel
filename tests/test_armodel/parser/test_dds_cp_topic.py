"""
Tests for reading DDS-CP-TOPIC elements — DdsCpTopic, Table 6.177 (p.527, R23-11).

The class is a nested non-top-level Identifiable (aggregated by the still-unsynced
DdsCpDomain.ddsTopic), so the reusable helper readDdsCpTopic is exercised directly on a
standalone XML subtree (XSD complexType DDS-CP-TOPIC, AUTOSAR_00052.xsd l.29324:
AR-OBJECT + REFERRABLE + MULTILANGUAGE-REFERRABLE + IDENTIFIABLE groups and
attributeGroups — read via readIdentifiable; group members DDS-PARTITION-REF,
TOPIC-NAME).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_topic.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpTopic

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-TOPIC xmlns='{NS}'>{inner}</DDS-CP-TOPIC>")


class TestReadDdsCpTopic:
    """Tests for readDdsCpTopic — own group field values (Table 6.177)."""

    def _read(self, parser, inner):
        topic = DdsCpTopic(AUTOSAR.getInstance(), "Topic1")
        parser.readDdsCpTopic(_snip(inner), topic)
        return topic

    def test_read_sets_all_fields(self, parser):
        """Test that the partition ref and topic name are read with their values."""
        topic = self._read(
            parser,
            "<SHORT-NAME>Topic1</SHORT-NAME>" '<DDS-PARTITION-REF DEST="DDS-CP-PARTITION">/DdsCpConfig/Domains/Domain1/Partitions/Partition1</DDS-PARTITION-REF>' "<TOPIC-NAME>MyDdsTopic</TOPIC-NAME>",
        )
        assert topic.getShortName() == "Topic1"
        assert topic.getDdsPartitionRef() is not None
        assert topic.getDdsPartitionRef().getDest() == "DDS-CP-PARTITION"
        assert topic.getDdsPartitionRef().getValue() == "/DdsCpConfig/Domains/Domain1/Partitions/Partition1"
        assert topic.getTopicName() is not None
        assert topic.getTopicName().getValue() == "MyDdsTopic"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        topic = self._read(parser, "")
        assert topic.getDdsPartitionRef() is None
        assert topic.getTopicName() is None

    def test_read_identifiable_level(self, parser):
        """Test that the IDENTIFIABLE attributeGroup (UUID attribute) is read via the base helper (SHORT-NAME is consumed by the aggregator that constructs the object)."""
        element = ET.fromstring("<DDS-CP-TOPIC xmlns='%s' UUID='1234-5678'/>" % NS)
        topic = DdsCpTopic(AUTOSAR.getInstance(), "Topic1")
        parser.readDdsCpTopic(element, topic)
        assert topic.getUuid() is not None
        assert topic.getUuid().getValue() == "1234-5678"
