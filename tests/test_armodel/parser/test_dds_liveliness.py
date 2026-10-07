"""
Tests for reading DDS-LIVELINESS elements — DdsLiveliness, Table 6.190 (p.534, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.liveliness as the
<LIVELINESS> element), so the reusable helper readDdsLiveliness is exercised directly on a
standalone XML subtree (XSD group DDS-LIVELINESS, AUTOSAR_00052.xsd l.29799: AR-OBJECT group +
attributeGroup — S/T round-trip; group members LIVELINESS-LEASE-DURATION typed AR:FLOAT and
LIVENESS-KIND typed AR:DDS-LIVENESS-KIND-ENUM, facets AUTOMATIC/MANUAL-BY-PARTICIPANT/
MANUAL-BY-TOPIC).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_liveliness.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLiveliness
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsLivenessKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<LIVELINESS xmlns='{NS}'>{inner}</LIVELINESS>")


class TestReadDdsLiveliness:
    """Tests for readDdsLiveliness — own group field values (Table 6.190)."""

    def _read(self, parser, inner):
        liveliness = DdsLiveliness()
        parser.readDdsLiveliness(_snip(inner), liveliness)
        return liveliness

    def test_read_sets_all_members(self, parser):
        """Test that both group members are read with their values."""
        liveliness = self._read(
            parser,
            "<LIVELINESS-LEASE-DURATION>10.0</LIVELINESS-LEASE-DURATION><LIVENESS-KIND>MANUAL-BY-TOPIC</LIVENESS-KIND>",
        )
        assert liveliness.getLivelinessLeaseDuration() is not None
        assert liveliness.getLivelinessLeaseDuration().getValue() == 10.0
        assert isinstance(liveliness.getLivenessKind(), DdsLivenessKindEnum)
        assert liveliness.getLivenessKind().getValue() == DdsLivenessKindEnum.MANUAL_BY_TOPIC

    def test_read_empty(self, parser):
        """Test that absent members leave the fields None."""
        liveliness = self._read(parser, "")
        assert liveliness.getLivelinessLeaseDuration() is None
        assert liveliness.getLivenessKind() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<LIVELINESS xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><LIVENESS-KIND>AUTOMATIC</LIVENESS-KIND></LIVELINESS>" % NS)
        liveliness = DdsLiveliness()
        parser.readDdsLiveliness(element, liveliness)
        assert liveliness.getChecksum() is not None
        assert liveliness.getChecksum().getValue() == "5"
        assert liveliness.getTimestamp() is not None
        assert liveliness.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert liveliness.getLivenessKind().getValue() == DdsLivenessKindEnum.AUTOMATIC
