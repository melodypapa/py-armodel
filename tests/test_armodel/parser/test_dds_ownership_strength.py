"""
Tests for reading DDS-OWNERSHIP-STRENGTH elements — DdsOwnershipStrength, Table 6.189 (p.533, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.ownershipStrength as
the <OWNERSHIP-STRENGTH> element), so the reusable helper readDdsOwnershipStrength is exercised
directly on a standalone XML subtree (XSD group DDS-OWNERSHIP-STRENGTH, AUTOSAR_00052.xsd
l.29865: AR-OBJECT group + attributeGroup — S/T round-trip; group member OWNERSHIP-STRENGTH
typed AR:POSITIVE-INTEGER; nested same-name shape: the object element carries the member of
the same name inside).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_ownership_strength.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsOwnershipStrength

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<OWNERSHIP-STRENGTH xmlns='{NS}'>{inner}</OWNERSHIP-STRENGTH>")


class TestReadDdsOwnershipStrength:
    """Tests for readDdsOwnershipStrength — own group field values (Table 6.189)."""

    def _read(self, parser, inner):
        ownership_strength = DdsOwnershipStrength()
        parser.readDdsOwnershipStrength(_snip(inner), ownership_strength)
        return ownership_strength

    def test_read_sets_ownership_strength(self, parser):
        """Test that the OWNERSHIP-STRENGTH positive-integer member is read with its value."""
        ownership_strength = self._read(parser, "<OWNERSHIP-STRENGTH>5</OWNERSHIP-STRENGTH>")
        assert ownership_strength.getOwnershipStrength() is not None
        assert ownership_strength.getOwnershipStrength().getValue() == 5

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        ownership_strength = self._read(parser, "")
        assert ownership_strength.getOwnershipStrength() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<OWNERSHIP-STRENGTH xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><OWNERSHIP-STRENGTH>10</OWNERSHIP-STRENGTH></OWNERSHIP-STRENGTH>" % NS)
        ownership_strength = DdsOwnershipStrength()
        parser.readDdsOwnershipStrength(element, ownership_strength)
        assert ownership_strength.getChecksum() is not None
        assert ownership_strength.getChecksum().getValue() == "5"
        assert ownership_strength.getTimestamp() is not None
        assert ownership_strength.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert ownership_strength.getOwnershipStrength().getValue() == 10
