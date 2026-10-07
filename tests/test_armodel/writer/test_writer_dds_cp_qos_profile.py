"""
Writer tests for DDS-CP-QOS-PROFILE elements — DdsCpQosProfile, Table 6.179 (p.529, R23-11).

writeDdsCpQosProfile emits <DDS-CP-QOS-PROFILE> with the IDENTIFIABLE level
(writeIdentifiable) and the 14 QoS policy children in XSD sequenceOffset order
(AUTOSAR_00052.xsd l.29057). Unsynced Dds* children serialize identity-only (empty
elements, Rule 0001.7 debt); the synced DdsTopicData/DdsDurability/DdsDurabilityService/
DdsDeadline/DdsLatencyBudget/DdsOwnership/DdsOwnershipStrength/DdsLiveliness children
serialize fully.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_qos_profile.py
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DdsDurabilityKindEnum,
    DdsDurabilityServiceHistoryKindEnum,
    DdsLivenessKindEnum,
    DdsOwnershipKindEnum,
    DdsReliabilityKindEnum,
    Float,
    PositiveInteger,
    String,
)
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
    deadline = DdsDeadline()
    deadline.setDeadlinePeriod(Float().setValue("0.5"))
    profile.setDeadline(deadline)
    latency_budget = DdsLatencyBudget()
    latency_budget.setLatencyBudgetDuration(Float().setValue("0.1"))
    profile.setLatencyBudget(latency_budget)
    ownership = DdsOwnership()
    ownership.setOwnershipKind(DdsOwnershipKindEnum().setValue(DdsOwnershipKindEnum.EXCLUSIVE))
    profile.setOwnership(ownership)
    ownership_strength = DdsOwnershipStrength()
    ownership_strength.setOwnershipStrength(PositiveInteger().setValue("5"))
    profile.setOwnershipStrength(ownership_strength)
    liveliness = DdsLiveliness()
    liveliness.setLivelinessLeaseDuration(Float().setValue("10.0"))
    liveliness.setLivenessKind(DdsLivenessKindEnum().setValue(DdsLivenessKindEnum.MANUAL_BY_TOPIC))
    profile.setLiveliness(liveliness)
    reliability = DdsReliability()
    reliability.setReliabilityKind(DdsReliabilityKindEnum().setValue(DdsReliabilityKindEnum.RELIABLE))
    reliability.setReliabilityMaxBlockingTime(Float().setValue("0.5"))
    profile.setReliability(reliability)
    durability = DdsDurability()
    durability.setDurabilityKind(DdsDurabilityKindEnum().setValue(DdsDurabilityKindEnum.TRANSIENT_LOCAL))
    profile.setDurability(durability)
    durability_service = DdsDurabilityService()
    durability_service.setDurabilityServiceCleanupDelay(Float().setValue("2.5"))
    durability_service.setDurabilityServiceHistoryKind(DdsDurabilityServiceHistoryKindEnum().setValue(DdsDurabilityServiceHistoryKindEnum.KEEP_LAST))
    durability_service.setDurabilityServiceMaxSamples(PositiveInteger().setValue("16"))
    profile.setDurabilityService(durability_service)
    profile.setHistory(DdsHistory())
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
        history_node = node.find("HISTORY")
        assert history_node is not None
        assert len(list(history_node)) == 0

    def test_write_emits_deadline_fully(self):
        """Test that the synced DdsDeadline child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        deadline_node = node.find("DEADLINE")
        assert deadline_node is not None
        assert deadline_node.find("DEADLINE-PERIOD").text == "0.5"

    def test_write_emits_liveliness_fully(self):
        """Test that the synced DdsLiveliness child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        liveliness_node = node.find("LIVELINESS")
        assert liveliness_node is not None
        assert liveliness_node.find("LIVELINESS-LEASE-DURATION").text == "10.0"
        assert liveliness_node.find("LIVENESS-KIND").text == "MANUAL-BY-TOPIC"

    def test_write_emits_reliability_fully(self):
        """Test that the synced DdsReliability child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        reliability_node = node.find("RELIABILITY")
        assert reliability_node is not None
        assert reliability_node.find("RELIABILITY-KIND").text == "RELIABLE"
        assert reliability_node.find("RELIABILITY-MAX-BLOCKING-TIME").text == "0.5"

    def test_write_emits_ownership_strength_fully(self):
        """Test that the synced DdsOwnershipStrength child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        ownership_strength_node = node.find("OWNERSHIP-STRENGTH")
        assert ownership_strength_node is not None
        assert ownership_strength_node.find("OWNERSHIP-STRENGTH").text == "5"

    def test_write_emits_ownership_fully(self):
        """Test that the synced DdsOwnership child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        ownership_node = node.find("OWNERSHIP")
        assert ownership_node is not None
        assert ownership_node.find("OWNERSHIP-KIND").text == "EXCLUSIVE"

    def test_write_emits_latency_budget_fully(self):
        """Test that the synced DdsLatencyBudget child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        latency_budget_node = node.find("LATENCY-BUDGET")
        assert latency_budget_node is not None
        assert latency_budget_node.find("LATENCY-BUDGET-DURATION").text == "0.1"

    def test_write_emits_durability_fully(self):
        """Test that the synced DdsDurability child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        durability_node = node.find("DURABILITY")
        assert durability_node is not None
        assert durability_node.find("DURABILITY-KIND").text == "TRANSIENT-LOCAL"

    def test_write_emits_durability_service_fully(self):
        """Test that the synced DdsDurabilityService child serializes with its values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpQosProfile(parent, _new_profile())
        node = parent.find("DDS-CP-QOS-PROFILE")
        durability_service_node = node.find("DURABILITY-SERVICE")
        assert durability_service_node is not None
        assert durability_service_node.find("DURABILITY-SERVICE-CLEANUP-DELAY").text == "2.5"
        assert durability_service_node.find("DURABILITY-SERVICE-HISTORY-KIND").text == "KEEP-LAST"
        assert durability_service_node.find("DURABILITY-SERVICE-MAX-SAMPLES").text == "16"

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
        assert reloaded.getDurability().getDurabilityKind() is not None
        assert reloaded.getDurability().getDurabilityKind().getValue() == "TRANSIENT-LOCAL"
        assert isinstance(reloaded.getDurabilityService(), DdsDurabilityService)
        assert reloaded.getDurabilityService().getDurabilityServiceCleanupDelay().getValue() == 2.5
        assert reloaded.getDurabilityService().getDurabilityServiceHistoryKind().getValue() == "KEEP-LAST"
        assert reloaded.getDurabilityService().getDurabilityServiceMaxSamples().getValue() == 16
        assert isinstance(reloaded.getDeadline(), DdsDeadline)
        assert reloaded.getDeadline().getDeadlinePeriod().getValue() == 0.5
        assert isinstance(reloaded.getLatencyBudget(), DdsLatencyBudget)
        assert reloaded.getLatencyBudget().getLatencyBudgetDuration().getValue() == 0.1
        assert isinstance(reloaded.getOwnership(), DdsOwnership)
        assert reloaded.getOwnership().getOwnershipKind().getValue() == "EXCLUSIVE"
        assert isinstance(reloaded.getOwnershipStrength(), DdsOwnershipStrength)
        assert reloaded.getOwnershipStrength().getOwnershipStrength().getValue() == 5
        assert isinstance(reloaded.getLiveliness(), DdsLiveliness)
        assert reloaded.getLiveliness().getLivelinessLeaseDuration().getValue() == 10.0
        assert reloaded.getLiveliness().getLivenessKind().getValue() == "MANUAL-BY-TOPIC"
        assert isinstance(reloaded.getReliability(), DdsReliability)
        assert reloaded.getReliability().getReliabilityKind().getValue() == "RELIABLE"
        assert reloaded.getReliability().getReliabilityMaxBlockingTime().getValue() == 0.5
        assert reloaded.getTopicData() is not None
        assert reloaded.getTopicData().getTopicData().getValue() == "raw payload"
