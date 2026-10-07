"""
Tests for reading DDS-CP-SERVICE-INSTANCE-EVENT elements — DdsCpServiceInstanceEvent, Table 6.155 (p.475, R23-11).

The class is a nested non-top-level element (aggregated by the still-unsynced
DdsCpConsumedServiceInstance.consumedDdsServiceEvent / DdsCpProvidedServiceInstance.providedDdsServiceInstanceEvent),
so the reusable helper readDdsCpServiceInstanceEvent is exercised directly on a
standalone XML subtree (XSD complexType DDS-CP-SERVICE-INSTANCE-EVENT, AUTOSAR_00052.xsd
l.29224: AR-OBJECT group + attributeGroup — S/T round-trip; group members in
xml.sequenceOffset order DDS-EVENT-QOS-PROFILE-REF, DDS-EVENT-REF, DDS-EVENT-TOPIC-REF,
VARIATION-POINT last).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_service_instance_event.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpServiceInstanceEvent

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-SERVICE-INSTANCE-EVENT xmlns='{NS}'>{inner}</DDS-CP-SERVICE-INSTANCE-EVENT>")


class TestReadDdsCpServiceInstanceEvent:
    """Tests for readDdsCpServiceInstanceEvent — own group field values (Table 6.155)."""

    def _read(self, parser, inner):
        event = DdsCpServiceInstanceEvent()
        parser.readDdsCpServiceInstanceEvent(_snip(inner), event)
        return event

    def test_read_sets_all_refs(self, parser):
        """Test that all three refs are read with their DEST and value (XSD sequenceOffset order)."""
        event = self._read(
            parser,
            '<DDS-EVENT-QOS-PROFILE-REF DEST="DDS-CP-QOS-PROFILE">/DdsCpConfig/QosProfiles/Profile1</DDS-EVENT-QOS-PROFILE-REF>'
            '<DDS-EVENT-REF DEST="PDU-TRIGGERING">/Fibex/Ecu1/PduTriggerings/DdsEvent</DDS-EVENT-REF>'
            '<DDS-EVENT-TOPIC-REF DEST="DDS-CP-TOPIC">/DdsCpConfig/Domains/Domain1/Topics/Topic1</DDS-EVENT-TOPIC-REF>',
        )
        assert event.getDdsEventQosProfileRef() is not None
        assert event.getDdsEventQosProfileRef().getDest() == "DDS-CP-QOS-PROFILE"
        assert event.getDdsEventQosProfileRef().getValue() == "/DdsCpConfig/QosProfiles/Profile1"
        assert event.getDdsEventRef() is not None
        assert event.getDdsEventRef().getDest() == "PDU-TRIGGERING"
        assert event.getDdsEventRef().getValue() == "/Fibex/Ecu1/PduTriggerings/DdsEvent"
        assert event.getDdsEventTopicRef() is not None
        assert event.getDdsEventTopicRef().getDest() == "DDS-CP-TOPIC"
        assert event.getDdsEventTopicRef().getValue() == "/DdsCpConfig/Domains/Domain1/Topics/Topic1"

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        event = self._read(parser, "")
        assert event.getDdsEventRef() is None
        assert event.getDdsEventQosProfileRef() is None
        assert event.getDdsEventTopicRef() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DDS-CP-SERVICE-INSTANCE-EVENT xmlns='%s' S='77' T='2025-03-03T00:00:00Z'/>" % NS)
        event = DdsCpServiceInstanceEvent()
        parser.readDdsCpServiceInstanceEvent(element, event)
        assert event.getChecksum() is not None
        assert event.getChecksum().getValue() == "77"
        assert event.getTimestamp() is not None
        assert event.getTimestamp().getValue() == "2025-03-03T00:00:00Z"

    def test_read_variation_point(self, parser):
        """Test that a trailing VARIATION-POINT (sequenceOffset=10000) is read via the VP mixin."""
        event = self._read(parser, "<VARIATION-POINT><SHORT-LABEL>vpEvent</SHORT-LABEL></VARIATION-POINT>")
        assert event.getVariationPoint() is not None
        assert event.getVariationPoint().getShortLabel() is not None
        assert event.getVariationPoint().getShortLabel().getValue() == "vpEvent"
