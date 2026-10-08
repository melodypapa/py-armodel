"""
Tests for reading DDS-CP-DOMAIN elements — DdsCpDomain, Table 6.176 (p.526, R23-11).

The class is a nested Identifiable element (aggregated by DdsCpConfig.ddsDomain, Table 6.175),
so the reusable helper readDdsCpDomain is exercised directly on a standalone XML subtree
(XSD complexType DDS-CP-DOMAIN, AUTOSAR_00052.xsd l.28746: group sequence AR-OBJECT,
REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE, DDS-CP-DOMAIN — the helper calls
readIdentifiable once for the inherited levels and reads its own group members
DDS-PARTITIONS, DDS-TOPICS, DOMAIN-ID in xml.sequenceOffset order).

ddsTopic children are read via the synced readDdsCpTopic (real coverage). ddsPartition
children are still identity-only (DdsCpPartition queued Table 6.178) — the reader constructs
the child from its SHORT-NAME; its own sync replaces the placeholder.

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_domain.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpDomain, DdsCpPartition, DdsCpTopic

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-DOMAIN xmlns='{NS}'>{inner}</DDS-CP-DOMAIN>")


class TestReadDdsCpDomain:
    """Tests for readDdsCpDomain — own group field values (Table 6.176)."""

    def _read(self, parser, inner):
        domain = DdsCpDomain(AUTOSAR.getInstance(), "Domain1")
        parser.readDdsCpDomain(_snip(inner), domain)
        return domain

    def test_read_sets_all_fields(self, parser):
        """Test that partitions, topics and the domain id are read with their values."""
        instance = self._read(
            parser,
            "<DDS-PARTITIONS>"
            "<DDS-CP-PARTITION><SHORT-NAME>Partition1</SHORT-NAME></DDS-CP-PARTITION>"
            "</DDS-PARTITIONS>"
            "<DDS-TOPICS>"
            "<DDS-CP-TOPIC><SHORT-NAME>Topic1</SHORT-NAME><TOPIC-NAME>MyDdsTopic</TOPIC-NAME></DDS-CP-TOPIC>"
            "</DDS-TOPICS>"
            "<DOMAIN-ID>1</DOMAIN-ID>",
        )
        partitions = instance.getDdsPartitions()
        assert len(partitions) == 1
        assert isinstance(partitions[0], DdsCpPartition)
        assert partitions[0].getShortName() == "Partition1"
        topics = instance.getDdsTopics()
        assert len(topics) == 1
        assert isinstance(topics[0], DdsCpTopic)
        assert topics[0].getShortName() == "Topic1"
        assert topics[0].getTopicName().getValue() == "MyDdsTopic"
        assert instance.getDomainId() is not None
        assert instance.getDomainId().getValue() == 1

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None/empty."""
        instance = self._read(parser, "")
        assert instance.getDdsPartitions() == []
        assert instance.getDdsTopics() == []
        assert instance.getDomainId() is None

    def test_read_inherited_identifiable_level(self, parser):
        """Test that the IDENTIFIABLE level (SHORT-NAME) is read via the base helper (Rule 0025)."""
        instance = self._read(parser, "<SHORT-NAME>Domain1</SHORT-NAME>")
        assert instance.getShortName() == "Domain1"
