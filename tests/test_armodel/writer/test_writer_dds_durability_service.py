"""
Writer tests for DDS-DURABILITY-SERVICE elements — DdsDurabilityService, Table 6.183 (p.531, R23-11).

writeDdsDurabilityService emits <DURABILITY-SERVICE> (the object element, per the
DdsCpQosProfile.durabilityService aggregation) with the AR-OBJECT S/T attributes and the six
group members in XSD sequenceOffset order (XSD group DDS-DURABILITY-SERVICE,
AUTOSAR_00052.xsd l.29474).

Round-trip counterpart: tests/test_armodel/parser/test_dds_durability_service.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurabilityService
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, DdsDurabilityServiceHistoryKindEnum, Float, PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_durability_service() -> DdsDurabilityService:
    durability_service = DdsDurabilityService()
    durability_service.setDurabilityServiceCleanupDelay(Float().setValue("2.5"))
    durability_service.setDurabilityServiceHistoryDepth(PositiveInteger().setValue("4"))
    durability_service.setDurabilityServiceHistoryKind(DdsDurabilityServiceHistoryKindEnum().setValue(DdsDurabilityServiceHistoryKindEnum.KEEP_LAST))
    durability_service.setDurabilityServiceMaxInstances(PositiveInteger().setValue("8"))
    durability_service.setDurabilityServiceMaxSamples(PositiveInteger().setValue("16"))
    durability_service.setDurabilityServiceMaxSamplesPerInstance(PositiveInteger().setValue("32"))
    durability_service.setChecksum(String().setValue("5"))
    durability_service.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return durability_service


class TestWriteDdsDurabilityService:
    def test_write_emits_element_and_members_in_xsd_order(self):
        """Test that the writer emits the object element with the six members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurabilityService(parent, _new_durability_service())
        node = parent.find("DURABILITY-SERVICE")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == [
            "DURABILITY-SERVICE-CLEANUP-DELAY",
            "DURABILITY-SERVICE-HISTORY-DEPTH",
            "DURABILITY-SERVICE-HISTORY-KIND",
            "DURABILITY-SERVICE-MAX-INSTANCES",
            "DURABILITY-SERVICE-MAX-SAMPLES",
            "DURABILITY-SERVICE-MAX-SAMPLES-PER-INSTANCE",
        ]
        assert node.find("DURABILITY-SERVICE-CLEANUP-DELAY").text == "2.5"
        assert node.find("DURABILITY-SERVICE-HISTORY-KIND").text == "KEEP-LAST"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurabilityService(parent, _new_durability_service())
        node = parent.find("DURABILITY-SERVICE")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_members(self):
        """Test that an empty object emits no member elements."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurabilityService(parent, DdsDurabilityService())
        node = parent.find("DURABILITY-SERVICE")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsDurabilityService(parent, _new_durability_service())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsDurabilityService()
        ARXMLParser().readDdsDurabilityService(root.find("{%s}DURABILITY-SERVICE" % NS), reloaded)
        assert reloaded.getDurabilityServiceCleanupDelay().getValue() == 2.5
        assert reloaded.getDurabilityServiceHistoryDepth().getValue() == 4
        assert reloaded.getDurabilityServiceHistoryKind().getValue() == DdsDurabilityServiceHistoryKindEnum.KEEP_LAST
        assert reloaded.getDurabilityServiceMaxInstances().getValue() == 8
        assert reloaded.getDurabilityServiceMaxSamples().getValue() == 16
        assert reloaded.getDurabilityServiceMaxSamplesPerInstance().getValue() == 32
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
