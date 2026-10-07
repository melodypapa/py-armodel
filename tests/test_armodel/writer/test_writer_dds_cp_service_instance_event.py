"""
Writer tests for DDS-CP-SERVICE-INSTANCE-EVENT elements — DdsCpServiceInstanceEvent, Table 6.155 (p.475, R23-11).

writeDdsCpServiceInstanceEvent emits <DDS-CP-SERVICE-INSTANCE-EVENT> with the group members
in XSD sequenceOffset order (DDS-EVENT-QOS-PROFILE-REF, DDS-EVENT-REF, DDS-EVENT-TOPIC-REF,
VARIATION-POINT last) plus the AR-OBJECT S/T attributes (AUTOSAR_00052.xsd l.29224).

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_service_instance_event.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpServiceInstanceEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_event() -> DdsCpServiceInstanceEvent:
    event = DdsCpServiceInstanceEvent()
    event.setDdsEventRef(RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/DdsEvent"))
    event.setDdsEventQosProfileRef(RefType().setDest("DDS-CP-QOS-PROFILE").setValue("/DdsCpConfig/QosProfiles/Profile1"))
    event.setDdsEventTopicRef(RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Domains/Domain1/Topics/Topic1"))
    event.setChecksum(String().setValue("77"))
    event.setTimestamp(DateTime().setValue("2025-03-03T00:00:00Z"))
    return event


class TestWriteDdsCpServiceInstanceEvent:
    def test_write_emits_element_and_refs(self):
        """Test that the writer emits the element with all three refs in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceEvent(parent, _new_event())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-EVENT")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["DDS-EVENT-QOS-PROFILE-REF", "DDS-EVENT-REF", "DDS-EVENT-TOPIC-REF"]
        topic_ref = node.find("DDS-EVENT-TOPIC-REF")
        assert topic_ref.attrib["DEST"] == "DDS-CP-TOPIC"
        assert topic_ref.text == "/DdsCpConfig/Domains/Domain1/Topics/Topic1"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceEvent(parent, _new_event())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-EVENT")
        assert node.attrib["S"] == "77"
        assert node.attrib["T"] == "2025-03-03T00:00:00Z"

    def test_write_empty_omits_refs(self):
        """Test that an empty event emits no ref elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceEvent(parent, DdsCpServiceInstanceEvent())
        node = parent.find("DDS-CP-SERVICE-INSTANCE-EVENT")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceEvent(parent, _new_event())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsCpServiceInstanceEvent()
        ARXMLParser().readDdsCpServiceInstanceEvent(root.find("{%s}DDS-CP-SERVICE-INSTANCE-EVENT" % NS), reloaded)
        assert reloaded.getDdsEventRef().getValue() == "/Fibex/Ecu1/PduTriggerings/DdsEvent"
        assert reloaded.getDdsEventRef().getDest() == "PDU-TRIGGERING"
        assert reloaded.getDdsEventQosProfileRef().getValue() == "/DdsCpConfig/QosProfiles/Profile1"
        assert reloaded.getDdsEventQosProfileRef().getDest() == "DDS-CP-QOS-PROFILE"
        assert reloaded.getDdsEventTopicRef().getValue() == "/DdsCpConfig/Domains/Domain1/Topics/Topic1"
        assert reloaded.getChecksum().getValue() == "77"
        assert reloaded.getTimestamp().getValue() == "2025-03-03T00:00:00Z"

    def test_round_trip_variation_point(self):
        """Test that a set variation point round-trips through the VP mixin."""
        event = _new_event()
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vpEvent"))
        event.setVariationPoint(variation_point)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpServiceInstanceEvent(parent, event)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        node = root.find("{%s}DDS-CP-SERVICE-INSTANCE-EVENT" % NS)
        assert node.find("{%s}VARIATION-POINT" % NS) is not None

        reloaded = DdsCpServiceInstanceEvent()
        ARXMLParser().readDdsCpServiceInstanceEvent(node, reloaded)
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vpEvent"
