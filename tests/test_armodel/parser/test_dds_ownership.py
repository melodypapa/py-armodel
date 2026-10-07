"""
Tests for reading DDS-OWNERSHIP elements — DdsOwnership, Table 6.187 (p.532, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.ownership as the
<OWNERSHIP> element), so the reusable helper readDdsOwnership is exercised directly on a
standalone XML subtree (XSD group DDS-OWNERSHIP, AUTOSAR_00052.xsd l.29836: AR-OBJECT group +
attributeGroup — S/T round-trip; group member OWNERSHIP-KIND typed
AR:DDS-OWNERSHIP-KIND-ENUM, facets EXCLUSIVE/SHARED).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_ownership.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsOwnership
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsOwnershipKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<OWNERSHIP xmlns='{NS}'>{inner}</OWNERSHIP>")


class TestReadDdsOwnership:
    """Tests for readDdsOwnership — own group field values (Table 6.187)."""

    def _read(self, parser, inner):
        ownership = DdsOwnership()
        parser.readDdsOwnership(_snip(inner), ownership)
        return ownership

    def test_read_sets_ownership_kind(self, parser):
        """Test that the OWNERSHIP-KIND enum member is read with its XSD facet value."""
        ownership = self._read(parser, "<OWNERSHIP-KIND>EXCLUSIVE</OWNERSHIP-KIND>")
        assert ownership.getOwnershipKind() is not None
        assert isinstance(ownership.getOwnershipKind(), DdsOwnershipKindEnum)
        assert ownership.getOwnershipKind().getValue() == DdsOwnershipKindEnum.EXCLUSIVE

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        ownership = self._read(parser, "")
        assert ownership.getOwnershipKind() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<OWNERSHIP xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><OWNERSHIP-KIND>SHARED</OWNERSHIP-KIND></OWNERSHIP>" % NS)
        ownership = DdsOwnership()
        parser.readDdsOwnership(element, ownership)
        assert ownership.getChecksum() is not None
        assert ownership.getChecksum().getValue() == "5"
        assert ownership.getTimestamp() is not None
        assert ownership.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert ownership.getOwnershipKind().getValue() == DdsOwnershipKindEnum.SHARED
