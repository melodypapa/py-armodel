"""
Tests for reading DDS-DURABILITY-SERVICE elements — DdsDurabilityService, Table 6.183 (p.531, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.durabilityService as
the <DURABILITY-SERVICE> element), so the reusable helper readDdsDurabilityService is exercised
directly on a standalone XML subtree (XSD group DDS-DURABILITY-SERVICE, AUTOSAR_00052.xsd
l.29474: AR-OBJECT group + attributeGroup — S/T round-trip; group members
DURABILITY-SERVICE-CLEANUP-DELAY (FLOAT), DURABILITY-SERVICE-HISTORY-DEPTH (POSITIVE-INTEGER),
DURABILITY-SERVICE-HISTORY-KIND (ENUM, facets KEEP-ALL/KEEP-LAST), DURABILITY-SERVICE-MAX-INSTANCES,
DURABILITY-SERVICE-MAX-SAMPLES, DURABILITY-SERVICE-MAX-SAMPLES-PER-INSTANCE).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_durability_service.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurabilityService
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsDurabilityServiceHistoryKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DURABILITY-SERVICE xmlns='{NS}'>{inner}</DURABILITY-SERVICE>")


class TestReadDdsDurabilityService:
    """Tests for readDdsDurabilityService — own group field values (Table 6.183)."""

    def _read(self, parser, inner):
        durability_service = DdsDurabilityService()
        parser.readDdsDurabilityService(_snip(inner), durability_service)
        return durability_service

    def test_read_sets_all_members(self, parser):
        """Test that all six group members are read with their values."""
        durability_service = self._read(
            parser,
            "<DURABILITY-SERVICE-CLEANUP-DELAY>2.5</DURABILITY-SERVICE-CLEANUP-DELAY>"
            "<DURABILITY-SERVICE-HISTORY-DEPTH>4</DURABILITY-SERVICE-HISTORY-DEPTH>"
            "<DURABILITY-SERVICE-HISTORY-KIND>KEEP-LAST</DURABILITY-SERVICE-HISTORY-KIND>"
            "<DURABILITY-SERVICE-MAX-INSTANCES>8</DURABILITY-SERVICE-MAX-INSTANCES>"
            "<DURABILITY-SERVICE-MAX-SAMPLES>16</DURABILITY-SERVICE-MAX-SAMPLES>"
            "<DURABILITY-SERVICE-MAX-SAMPLES-PER-INSTANCE>32</DURABILITY-SERVICE-MAX-SAMPLES-PER-INSTANCE>",
        )
        assert durability_service.getDurabilityServiceCleanupDelay() is not None
        assert durability_service.getDurabilityServiceCleanupDelay().getValue() == 2.5
        assert durability_service.getDurabilityServiceHistoryDepth() is not None
        assert durability_service.getDurabilityServiceHistoryDepth().getValue() == 4
        assert isinstance(durability_service.getDurabilityServiceHistoryKind(), DdsDurabilityServiceHistoryKindEnum)
        assert durability_service.getDurabilityServiceHistoryKind().getValue() == DdsDurabilityServiceHistoryKindEnum.KEEP_LAST
        assert durability_service.getDurabilityServiceMaxInstances() is not None
        assert durability_service.getDurabilityServiceMaxInstances().getValue() == 8
        assert durability_service.getDurabilityServiceMaxSamples() is not None
        assert durability_service.getDurabilityServiceMaxSamples().getValue() == 16
        assert durability_service.getDurabilityServiceMaxSamplesPerInstance() is not None
        assert durability_service.getDurabilityServiceMaxSamplesPerInstance().getValue() == 32

    def test_read_empty(self, parser):
        """Test that absent members leave the fields None."""
        durability_service = self._read(parser, "")
        assert durability_service.getDurabilityServiceCleanupDelay() is None
        assert durability_service.getDurabilityServiceHistoryDepth() is None
        assert durability_service.getDurabilityServiceHistoryKind() is None
        assert durability_service.getDurabilityServiceMaxInstances() is None
        assert durability_service.getDurabilityServiceMaxSamples() is None
        assert durability_service.getDurabilityServiceMaxSamplesPerInstance() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DURABILITY-SERVICE xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><DURABILITY-SERVICE-HISTORY-KIND>KEEP-ALL</DURABILITY-SERVICE-HISTORY-KIND></DURABILITY-SERVICE>" % NS)
        durability_service = DdsDurabilityService()
        parser.readDdsDurabilityService(element, durability_service)
        assert durability_service.getChecksum() is not None
        assert durability_service.getChecksum().getValue() == "5"
        assert durability_service.getTimestamp() is not None
        assert durability_service.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert durability_service.getDurabilityServiceHistoryKind().getValue() == DdsDurabilityServiceHistoryKindEnum.KEEP_ALL
