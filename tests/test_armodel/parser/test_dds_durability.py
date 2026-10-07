"""
Tests for reading DDS-DURABILITY elements — DdsDurability, Table 6.181 (p.530, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.durability as the
<DURABILITY> element), so the reusable helper readDdsDurability is exercised directly on a
standalone XML subtree (XSD complexType DDS-DURABILITY, AUTOSAR_00052.xsd l.29461:
AR-OBJECT group + attributeGroup — S/T round-trip; group member DURABILITY-KIND typed
AR:DDS-DURABILITY-KIND-ENUM, facets PERSISTENT/TRANSIENT/TRANSIENT-LOCAL/VOLATILE).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_durability.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDurability
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsDurabilityKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DURABILITY xmlns='{NS}'>{inner}</DURABILITY>")


class TestReadDdsDurability:
    """Tests for readDdsDurability — own group field values (Table 6.181)."""

    def _read(self, parser, inner):
        durability = DdsDurability()
        parser.readDdsDurability(_snip(inner), durability)
        return durability

    def test_read_sets_durability_kind(self, parser):
        """Test that the DURABILITY-KIND enum member is read with its XSD facet value."""
        durability = self._read(parser, "<DURABILITY-KIND>TRANSIENT-LOCAL</DURABILITY-KIND>")
        assert durability.getDurabilityKind() is not None
        assert isinstance(durability.getDurabilityKind(), DdsDurabilityKindEnum)
        assert durability.getDurabilityKind().getValue() == DdsDurabilityKindEnum.TRANSIENT_LOCAL

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        durability = self._read(parser, "")
        assert durability.getDurabilityKind() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DURABILITY xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><DURABILITY-KIND>PERSISTENT</DURABILITY-KIND></DURABILITY>" % NS)
        durability = DdsDurability()
        parser.readDdsDurability(element, durability)
        assert durability.getChecksum() is not None
        assert durability.getChecksum().getValue() == "5"
        assert durability.getTimestamp() is not None
        assert durability.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert durability.getDurabilityKind().getValue() == DdsDurabilityKindEnum.PERSISTENT
