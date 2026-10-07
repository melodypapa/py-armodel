"""
Tests for reading DDS-CP-QOS-PROFILE elements — DdsCpQosProfile, Table 6.179 (p.529, R23-11).

The class is a nested non-top-level Identifiable (aggregated by the still-unsynced
DdsCpConfig.ddsQosProfile), so the reusable helper readDdsCpQosProfile is exercised directly
on a standalone XML subtree (XSD complexType DDS-CP-QOS-PROFILE, AUTOSAR_00052.xsd l.29057:
AR-OBJECT + REFERRABLE + MULTILANGUAGE-REFERRABLE + IDENTIFIABLE groups/attributeGroups —
read via readIdentifiable; group members DEADLINE, DESTINATION-ORDER, DURABILITY,
DURABILITY-SERVICE, HISTORY, LATENCY-BUDGET, LIFESPAN, LIVELINESS, OWNERSHIP,
OWNERSHIP-STRENGTH, RELIABILITY, RESOURCE-LIMITS, TOPIC-DATA, TRANSPORT-PRIORITY).

The Dds* QoS policy child classes (except DdsTopicData, synced Table 6.180, DdsDurability,
synced Table 6.181, and DdsDurabilityService, synced Table 6.183) are still unsynced stubs —
the reader serializes them identity-only (Rule 0001.7 debt).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_qos_profile.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurability, DdsDurabilityService, DdsHistory, DdsTopicData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpQosProfile

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-QOS-PROFILE xmlns='{NS}'>{inner}</DDS-CP-QOS-PROFILE>")


class TestReadDdsCpQosProfile:
    """Tests for readDdsCpQosProfile — own group field values (Table 6.179)."""

    def _read(self, parser, inner):
        profile = DdsCpQosProfile(AUTOSAR.getInstance(), "Profile1")
        parser.readDdsCpQosProfile(_snip(inner), profile)
        return profile

    def test_read_sets_stub_children_identity_only(self, parser):
        """Test that unsynced Dds* QoS policy children are constructed identity-only (presence round-trips)."""
        profile = self._read(
            parser,
            "<DEADLINE><DURATION>1.0</DURATION></DEADLINE><HISTORY><HISTORY-KIND>KEEP-LAST</HISTORY-KIND></HISTORY>",
        )
        assert profile.getDeadline() is not None
        assert isinstance(profile.getHistory(), DdsHistory)
        assert profile.getDestinationOrder() is None

    def test_read_sets_durability_with_values(self, parser):
        """Test that the synced DdsDurability child is read with its field values."""
        profile = self._read(parser, "<DURABILITY><DURABILITY-KIND>TRANSIENT-LOCAL</DURABILITY-KIND></DURABILITY>")
        assert isinstance(profile.getDurability(), DdsDurability)
        assert profile.getDurability().getDurabilityKind() is not None
        assert profile.getDurability().getDurabilityKind().getValue() == "TRANSIENT-LOCAL"

    def test_read_sets_durability_service_with_values(self, parser):
        """Test that the synced DdsDurabilityService child is read with its field values."""
        profile = self._read(
            parser,
            "<DURABILITY-SERVICE>"
            "<DURABILITY-SERVICE-CLEANUP-DELAY>2.5</DURABILITY-SERVICE-CLEANUP-DELAY>"
            "<DURABILITY-SERVICE-HISTORY-KIND>KEEP-LAST</DURABILITY-SERVICE-HISTORY-KIND>"
            "<DURABILITY-SERVICE-MAX-SAMPLES>16</DURABILITY-SERVICE-MAX-SAMPLES>"
            "</DURABILITY-SERVICE>",
        )
        assert isinstance(profile.getDurabilityService(), DdsDurabilityService)
        assert profile.getDurabilityService().getDurabilityServiceCleanupDelay().getValue() == 2.5
        assert profile.getDurabilityService().getDurabilityServiceHistoryKind().getValue() == "KEEP-LAST"
        assert profile.getDurabilityService().getDurabilityServiceMaxSamples().getValue() == 16

    def test_read_sets_topic_data_with_values(self, parser):
        """Test that the synced DdsTopicData child is read with its field values (TOPIC-DATA nested same-name shape)."""
        profile = self._read(parser, "<TOPIC-DATA><TOPIC-DATA>raw payload</TOPIC-DATA></TOPIC-DATA>")
        assert isinstance(profile.getTopicData(), DdsTopicData)
        assert profile.getTopicData().getTopicData().getValue() == "raw payload"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        profile = self._read(parser, "")
        assert profile.getDeadline() is None
        assert profile.getTopicData() is None
        assert profile.getTransportPriority() is None

    def test_read_identifiable_level(self, parser):
        """Test that the IDENTIFIABLE attributeGroup (UUID attribute) is read via the base helper."""
        element = ET.fromstring("<DDS-CP-QOS-PROFILE xmlns='%s' UUID='abcd-efgh'/>" % NS)
        profile = DdsCpQosProfile(AUTOSAR.getInstance(), "Profile1")
        parser.readDdsCpQosProfile(element, profile)
        assert profile.getUuid() is not None
        assert profile.getUuid().getValue() == "abcd-efgh"
