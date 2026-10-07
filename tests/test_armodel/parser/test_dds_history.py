"""
Tests for reading DDS-HISTORY elements — DdsHistory, Table 6.198 (p.537, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.history as the
<HISTORY> element), so the reusable helper readDdsHistory is exercised directly on a standalone
XML subtree (XSD group DDS-HISTORY, AUTOSAR_00052.xsd l.29702: AR-OBJECT group + attributeGroup —
S/T round-trip; group members HISTORY-KIND typed AR:DDS-HISTORY-KIND-ENUM, facets KEEP-ALL/
KEEP-LAST, and HISTORY-ORDER-DEPTH typed AR:POSITIVE-INTEGER).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_history.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsHistory
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DdsHistoryKindEnum

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<HISTORY xmlns='{NS}'>{inner}</HISTORY>")


class TestReadDdsHistory:
    """Tests for readDdsHistory — own group field values (Table 6.198)."""

    def _read(self, parser, inner):
        history = DdsHistory()
        parser.readDdsHistory(_snip(inner), history)
        return history

    def test_read_sets_all_members(self, parser):
        """Test that both group members are read with their values."""
        history = self._read(parser, "<HISTORY-KIND>KEEP-LAST</HISTORY-KIND><HISTORY-ORDER-DEPTH>4</HISTORY-ORDER-DEPTH>")
        assert isinstance(history.getHistoryKind(), DdsHistoryKindEnum)
        assert history.getHistoryKind().getValue() == DdsHistoryKindEnum.KEEP_LAST
        assert history.getHistoryOrderDepth() is not None
        assert history.getHistoryOrderDepth().getValue() == 4

    def test_read_empty(self, parser):
        """Test that absent members leave the fields None."""
        history = self._read(parser, "")
        assert history.getHistoryKind() is None
        assert history.getHistoryOrderDepth() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<HISTORY xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><HISTORY-KIND>KEEP-ALL</HISTORY-KIND></HISTORY>" % NS)
        history = DdsHistory()
        parser.readDdsHistory(element, history)
        assert history.getChecksum() is not None
        assert history.getChecksum().getValue() == "5"
        assert history.getTimestamp() is not None
        assert history.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert history.getHistoryKind().getValue() == DdsHistoryKindEnum.KEEP_ALL
