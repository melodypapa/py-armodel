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
synced Table 6.181, DdsDurabilityService, synced Table 6.183, DdsDeadline, synced
Table 6.185, DdsLatencyBudget, synced Table 6.186, DdsOwnership, synced Table 6.187,
DdsOwnershipStrength, synced Table 6.189, and DdsLiveliness, synced Table 6.190) are still
unsynced stubs — the reader serializes them identity-only (Rule 0001.7 debt).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_qos_profile.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DdsDeadline,
    DdsDurability,
    DdsDurabilityService,
    DdsHistory,
    DdsLatencyBudget,
    DdsLiveliness,
    DdsOwnership,
    DdsOwnershipStrength,
    DdsReliability,
    DdsTopicData,
)
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
            "<DESTINATION-ORDER/><HISTORY><HISTORY-KIND>KEEP-LAST</HISTORY-KIND></HISTORY>",
        )
        assert profile.getDestinationOrder() is not None
        assert isinstance(profile.getHistory(), DdsHistory)
        assert profile.getTransportPriority() is None

    def test_read_sets_reliability_with_values(self, parser):
        """Test that the synced DdsReliability child is read with its field values."""
        profile = self._read(
            parser,
            "<RELIABILITY><RELIABILITY-KIND>RELIABLE</RELIABILITY-KIND><RELIABILITY-MAX-BLOCKING-TIME>0.5</RELIABILITY-MAX-BLOCKING-TIME></RELIABILITY>",
        )
        assert isinstance(profile.getReliability(), DdsReliability)
        assert profile.getReliability().getReliabilityKind() is not None
        assert profile.getReliability().getReliabilityKind().getValue() == "RELIABLE"
        assert profile.getReliability().getReliabilityMaxBlockingTime() is not None
        assert profile.getReliability().getReliabilityMaxBlockingTime().getValue() == 0.5

    def test_read_sets_durability_with_values(self, parser):
        """Test that the synced DdsDurability child is read with its field values."""
        profile = self._read(parser, "<DURABILITY><DURABILITY-KIND>TRANSIENT-LOCAL</DURABILITY-KIND></DURABILITY>")
        assert isinstance(profile.getDurability(), DdsDurability)
        assert profile.getDurability().getDurabilityKind() is not None
        assert profile.getDurability().getDurabilityKind().getValue() == "TRANSIENT-LOCAL"

    def test_read_sets_deadline_with_values(self, parser):
        """Test that the synced DdsDeadline child is read with its field values."""
        profile = self._read(parser, "<DEADLINE><DEADLINE-PERIOD>0.5</DEADLINE-PERIOD></DEADLINE>")
        assert isinstance(profile.getDeadline(), DdsDeadline)
        assert profile.getDeadline().getDeadlinePeriod() is not None
        assert profile.getDeadline().getDeadlinePeriod().getValue() == 0.5

    def test_read_sets_liveliness_with_values(self, parser):
        """Test that the synced DdsLiveliness child is read with its field values."""
        profile = self._read(parser, "<LIVELINESS><LIVELINESS-LEASE-DURATION>10.0</LIVELINESS-LEASE-DURATION><LIVENESS-KIND>MANUAL-BY-TOPIC</LIVENESS-KIND></LIVELINESS>")
        assert isinstance(profile.getLiveliness(), DdsLiveliness)
        assert profile.getLiveliness().getLivelinessLeaseDuration().getValue() == 10.0
        assert profile.getLiveliness().getLivenessKind().getValue() == "MANUAL-BY-TOPIC"

    def test_read_sets_ownership_strength_with_values(self, parser):
        """Test that the synced DdsOwnershipStrength child is read with its field values."""
        profile = self._read(parser, "<OWNERSHIP-STRENGTH><OWNERSHIP-STRENGTH>5</OWNERSHIP-STRENGTH></OWNERSHIP-STRENGTH>")
        assert isinstance(profile.getOwnershipStrength(), DdsOwnershipStrength)
        assert profile.getOwnershipStrength().getOwnershipStrength() is not None
        assert profile.getOwnershipStrength().getOwnershipStrength().getValue() == 5

    def test_read_sets_ownership_with_values(self, parser):
        """Test that the synced DdsOwnership child is read with its field values."""
        profile = self._read(parser, "<OWNERSHIP><OWNERSHIP-KIND>EXCLUSIVE</OWNERSHIP-KIND></OWNERSHIP>")
        assert isinstance(profile.getOwnership(), DdsOwnership)
        assert profile.getOwnership().getOwnershipKind() is not None
        assert profile.getOwnership().getOwnershipKind().getValue() == "EXCLUSIVE"

    def test_read_sets_latency_budget_with_values(self, parser):
        """Test that the synced DdsLatencyBudget child is read with its field values."""
        profile = self._read(parser, "<LATENCY-BUDGET><LATENCY-BUDGET-DURATION>0.1</LATENCY-BUDGET-DURATION></LATENCY-BUDGET>")
        assert isinstance(profile.getLatencyBudget(), DdsLatencyBudget)
        assert profile.getLatencyBudget().getLatencyBudgetDuration() is not None
        assert profile.getLatencyBudget().getLatencyBudgetDuration().getValue() == 0.1

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
