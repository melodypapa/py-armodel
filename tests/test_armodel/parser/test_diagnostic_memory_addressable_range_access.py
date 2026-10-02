"""
Tests for reading the MEMORY-RANGE-REFS wrapper —
DiagnosticMemoryAddressableRangeAccess, Table 4.111 (p.140, R23-11).

DiagnosticMemoryAddressableRangeAccess is an abstract base (Base most-derived
DiagnosticMemoryByAddress): its XML group DIAGNOSTIC-MEMORY-ADDRESSABLE-RANGE-ACCESS
(AUTOSAR_00052.xsd l.39420) carries the single optional MEMORY-RANGE-REFS wrapper
holding unbounded MEMORY-RANGE-REF elements (DEST
DIAGNOSTIC-MEMORY-IDENTIFIER--SUBTYPES-ENUM). The reusable
readDiagnosticMemoryAddressableRangeAccess helper is exercised through the test
stub subclass _MemoryAddressableRangeAccessStub.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_memory_addressable_range_access.py
"""

from unittest.mock import MagicMock

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryAddressableRangeAccess
from tests.test_armodel.parser._helpers import _snip


class _MemoryAddressableRangeAccessStub(DiagnosticMemoryAddressableRangeAccess):
    """Concrete test stub for the abstract DiagnosticMemoryAddressableRangeAccess."""

    pass


class TestReadDiagnosticMemoryAddressableRangeAccess:
    """Tests for readDiagnosticMemoryAddressableRangeAccess — own element field values (Table 4.111)."""

    def _read(self, parser, inner):
        range_access = _MemoryAddressableRangeAccessStub(parent=MagicMock(), short_name="RangeAccess")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-DOWNLOAD")
        parser.readDiagnosticMemoryAddressableRangeAccess(element, range_access)
        return range_access

    def test_read_memory_range_refs(self, parser):
        """Test that MEMORY-RANGE-REFS wrapper children are read with their DEST attributes."""
        range_access = self._read(
            parser,
            """
            <MEMORY-RANGE-REFS>
                <MEMORY-RANGE-REF DEST="DIAGNOSTIC-MEMORY-IDENTIFIER">/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1</MEMORY-RANGE-REF>
                <MEMORY-RANGE-REF DEST="DIAGNOSTIC-MEMORY-IDENTIFIER">/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2</MEMORY-RANGE-REF>
            </MEMORY-RANGE-REFS>
            """,
        )
        ranges = range_access.getMemoryRanges()
        assert len(ranges) == 2
        assert ranges[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert ranges[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert ranges[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"

    def test_read_absent_wrapper(self, parser):
        """Test that an absent MEMORY-RANGE-REFS wrapper leaves memoryRanges empty."""
        range_access = self._read(parser, "<SHORT-NAME>RangeAccess</SHORT-NAME>")
        assert range_access.getMemoryRanges() == []

    def test_read_empty_wrapper(self, parser):
        """Test that an empty MEMORY-RANGE-REFS wrapper parses leaving memoryRanges empty."""
        range_access = self._read(parser, "<MEMORY-RANGE-REFS></MEMORY-RANGE-REFS>")
        assert range_access.getMemoryRanges() == []
