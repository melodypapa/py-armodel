"""
Tests for reading DDS-RELIABILITY elements — DdsReliability, Table 6.192 (p.535, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.reliability as the
<RELIABILITY> element), so the reusable helper readDdsReliability is exercised directly on a
standalone XML subtree (XSD group DDS-RELIABILITY, AUTOSAR_00052.xsd l.29986: AR-OBJECT group +
attributeGroup — S/T round-trip; group members RELIABILITY-KIND typed
AR:DDS-RELIABILITY-KIND-ENUM, facets BEST-EFFORT/RELIABLE, and RELIABILITY-MAX-BLOCKING-TIME
typed AR:FLOAT).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_reliability.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsReliability
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsReliabilityKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<RELIABILITY xmlns='{NS}'>{inner}</RELIABILITY>")


class TestReadDdsReliability:
    """Tests for readDdsReliability — own group field values (Table 6.192)."""

    def _read(self, parser, inner):
        reliability = DdsReliability()
        parser.readDdsReliability(_snip(inner), reliability)
        return reliability

    def test_read_sets_all_members(self, parser):
        """Test that both group members are read with their values."""
        reliability = self._read(
            parser,
            "<RELIABILITY-KIND>RELIABLE</RELIABILITY-KIND><RELIABILITY-MAX-BLOCKING-TIME>0.5</RELIABILITY-MAX-BLOCKING-TIME>",
        )
        assert isinstance(reliability.getReliabilityKind(), DdsReliabilityKindEnum)
        assert reliability.getReliabilityKind().getValue() == DdsReliabilityKindEnum.RELIABLE
        assert reliability.getReliabilityMaxBlockingTime() is not None
        assert reliability.getReliabilityMaxBlockingTime().getValue() == 0.5

    def test_read_empty(self, parser):
        """Test that absent members leave the fields None."""
        reliability = self._read(parser, "")
        assert reliability.getReliabilityKind() is None
        assert reliability.getReliabilityMaxBlockingTime() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<RELIABILITY xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><RELIABILITY-KIND>BEST-EFFORT</RELIABILITY-KIND></RELIABILITY>" % NS)
        reliability = DdsReliability()
        parser.readDdsReliability(element, reliability)
        assert reliability.getChecksum() is not None
        assert reliability.getChecksum().getValue() == "5"
        assert reliability.getTimestamp() is not None
        assert reliability.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert reliability.getReliabilityKind().getValue() == DdsReliabilityKindEnum.BEST_EFFORT
