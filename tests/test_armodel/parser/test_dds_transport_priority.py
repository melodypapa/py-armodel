"""
Tests for reading DDS-TRANSPORT-PRIORITY elements — DdsTransportPriority, Table 6.194 (p.535, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.transportPriority as the
<TRANSPORT-PRIORITY> element), so the reusable helper readDdsTransportPriority is exercised directly
on a standalone XML subtree (XSD group DDS-TRANSPORT-PRIORITY, AUTOSAR_00052.xsd l.30704: AR-OBJECT
group + attributeGroup — S/T round-trip; group member TRANSPORT-PRIORITY typed AR:POSITIVE-INTEGER).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_transport_priority.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsTransportPriority

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<TRANSPORT-PRIORITY xmlns='{NS}'>{inner}</TRANSPORT-PRIORITY>")


class TestReadDdsTransportPriority:
    """Tests for readDdsTransportPriority — own group field values (Table 6.194)."""

    def _read(self, parser, inner):
        transport_priority = DdsTransportPriority()
        parser.readDdsTransportPriority(_snip(inner), transport_priority)
        return transport_priority

    def test_read_sets_member(self, parser):
        """Test that the group member is read with its value."""
        transport_priority = self._read(parser, "<TRANSPORT-PRIORITY>4</TRANSPORT-PRIORITY>")
        assert transport_priority.getTransportPriority() is not None
        assert transport_priority.getTransportPriority().getValue() == 4

    def test_read_empty(self, parser):
        """Test that the absent member leaves the field None."""
        transport_priority = self._read(parser, "")
        assert transport_priority.getTransportPriority() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<TRANSPORT-PRIORITY xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><TRANSPORT-PRIORITY>7</TRANSPORT-PRIORITY></TRANSPORT-PRIORITY>" % NS)
        transport_priority = DdsTransportPriority()
        parser.readDdsTransportPriority(element, transport_priority)
        assert transport_priority.getChecksum() is not None
        assert transport_priority.getChecksum().getValue() == "5"
        assert transport_priority.getTimestamp() is not None
        assert transport_priority.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert transport_priority.getTransportPriority().getValue() == 7
