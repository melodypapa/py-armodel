"""
Tests for reading DDS-DESTINATION-ORDER elements — DdsDestinationOrder, Table 6.196 (p.536, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.destinationOrder as the
<DESTINATION-ORDER> element), so the reusable helper readDdsDestinationOrder is exercised directly
on a standalone XML subtree (XSD group DDS-DESTINATION-ORDER, AUTOSAR_00052.xsd l.29377: AR-OBJECT
group + attributeGroup — S/T round-trip; group member DESTINATION-ORDER-KIND typed
AR:DDS-DESTINATION-ORDER-KIND-ENUM, facets BY-RECEPTION-TIMESTAMP/BY-SOURCE-TIMESTAMP per the
--SIMPLE simpleType — the markdown literal cells render "byReception Timestamp"/"bySource Timestamp"
with an embedded space, a line-wrap artefact).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_destination_order.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDestinationOrder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsDestinationOrderKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DESTINATION-ORDER xmlns='{NS}'>{inner}</DESTINATION-ORDER>")


class TestReadDdsDestinationOrder:
    """Tests for readDdsDestinationOrder — own group field values (Table 6.196)."""

    def _read(self, parser, inner):
        destination_order = DdsDestinationOrder()
        parser.readDdsDestinationOrder(_snip(inner), destination_order)
        return destination_order

    def test_read_sets_member(self, parser):
        """Test that the group member is read with its value."""
        destination_order = self._read(parser, "<DESTINATION-ORDER-KIND>BY-SOURCE-TIMESTAMP</DESTINATION-ORDER-KIND>")
        assert isinstance(destination_order.getDestinationOrderKind(), DdsDestinationOrderKindEnum)
        assert destination_order.getDestinationOrderKind().getValue() == DdsDestinationOrderKindEnum.BY_SOURCE_TIMESTAMP

    def test_read_empty(self, parser):
        """Test that the absent member leaves the field None."""
        destination_order = self._read(parser, "")
        assert destination_order.getDestinationOrderKind() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DESTINATION-ORDER xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><DESTINATION-ORDER-KIND>BY-RECEPTION-TIMESTAMP</DESTINATION-ORDER-KIND></DESTINATION-ORDER>" % NS)
        destination_order = DdsDestinationOrder()
        parser.readDdsDestinationOrder(element, destination_order)
        assert destination_order.getChecksum() is not None
        assert destination_order.getChecksum().getValue() == "5"
        assert destination_order.getTimestamp() is not None
        assert destination_order.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert destination_order.getDestinationOrderKind().getValue() == DdsDestinationOrderKindEnum.BY_RECEPTION_TIMESTAMP
