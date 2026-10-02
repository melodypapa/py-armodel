"""
Tests for writing the MEMORY-RANGE-REFS wrapper —
DiagnosticMemoryAddressableRangeAccess, Table 4.111 (p.140, R23-11).

DiagnosticMemoryAddressableRangeAccess is an abstract base (Base most-derived
DiagnosticMemoryByAddress): its XML group DIAGNOSTIC-MEMORY-ADDRESSABLE-RANGE-ACCESS
(AUTOSAR_00052.xsd l.39420) carries the single optional MEMORY-RANGE-REFS wrapper
holding unbounded MEMORY-RANGE-REF elements (DEST
DIAGNOSTIC-MEMORY-IDENTIFIER--SUBTYPES-ENUM). The reusable
writeDiagnosticMemoryAddressableRangeAccess helper is exercised through the test
stub subclass _MemoryAddressableRangeAccessStub; it emits the wrapper into a
caller-provided element (no own SubElement — the concrete element tag belongs
to the subclass writer).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_memory_addressable_range_access.py
"""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryAddressableRangeAccess
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class _MemoryAddressableRangeAccessStub(DiagnosticMemoryAddressableRangeAccess):
    """Concrete test stub for the abstract DiagnosticMemoryAddressableRangeAccess."""

    pass


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticMemoryAddressableRangeAccess:
    """Tests for writeDiagnosticMemoryAddressableRangeAccess — own element field values (Table 4.111)."""

    def test_write_memory_range_refs(self):
        """Test that the MEMORY-RANGE-REFS wrapper is emitted with its children's DEST attributes."""
        obj = _MemoryAddressableRangeAccessStub(parent=MagicMock(), short_name="RangeAccess")
        obj.addMemoryRange(_ref("DIAGNOSTIC-MEMORY-IDENTIFIER", "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"))
        obj.addMemoryRange(_ref("DIAGNOSTIC-MEMORY-IDENTIFIER", "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"))

        parent = ET.Element("DIAGNOSTIC-REQUEST-DOWNLOAD")
        ARXMLWriter().writeDiagnosticMemoryAddressableRangeAccess(parent, obj)

        wrapper = parent.find("MEMORY-RANGE-REFS")
        assert wrapper is not None
        refs = wrapper.findall("MEMORY-RANGE-REF")
        assert len(refs) == 2
        assert refs[0].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert refs[0].get("DEST") == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert refs[1].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"

    def test_write_unset_ranges_omit_wrapper(self):
        """Test that empty memoryRanges emits no MEMORY-RANGE-REFS wrapper."""
        obj = _MemoryAddressableRangeAccessStub(parent=MagicMock(), short_name="RangeAccess")

        parent = ET.Element("DIAGNOSTIC-REQUEST-DOWNLOAD")
        ARXMLWriter().writeDiagnosticMemoryAddressableRangeAccess(parent, obj)

        assert parent.find("MEMORY-RANGE-REFS") is None
        assert len(list(parent)) == 0

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        obj = _MemoryAddressableRangeAccessStub(parent=MagicMock(), short_name="RangeAccess")
        obj.addMemoryRange(_ref("DIAGNOSTIC-MEMORY-IDENTIFIER", "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"))
        obj.addMemoryRange(_ref("DIAGNOSTIC-MEMORY-IDENTIFIER", "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"))

        parent = ET.Element("DIAGNOSTIC-REQUEST-DOWNLOAD", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticMemoryAddressableRangeAccess(parent, obj)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = _MemoryAddressableRangeAccessStub(parent=MagicMock(), short_name="RangeAccess")
        ARXMLParser().readDiagnosticMemoryAddressableRangeAccess(ET.fromstring(xml_text), reloaded)
        ranges = reloaded.getMemoryRanges()
        assert len(ranges) == 2
        assert ranges[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert ranges[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert ranges[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
