"""
Tests for writing DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS elements —
DiagnosticWriteMemoryByAddress, Table 4.113 (p.141, R23-11).

DiagnosticWriteMemoryByAddress (Base most-derived DiagnosticMemoryAddressableRangeAccess)
inherits the 0..* memoryRange refs (MEMORY-RANGE-REFS wrapper) and owns one 0..1
reference writeClass (WRITE-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS l.47258: MEMORY-RANGE-REFS, WRITE-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_write_memory_by_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticWriteMemoryByAddress
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


def _make_full_write_memory() -> DiagnosticWriteMemoryByAddress:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressServices")
    write_memory = package.createDiagnosticWriteMemoryByAddress("WriteMem1")
    range_ref1 = RefType().setDest("DIAGNOSTIC-MEMORY-IDENTIFIER").setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1")
    range_ref2 = RefType().setDest("DIAGNOSTIC-MEMORY-IDENTIFIER").setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2")
    write_memory.addMemoryRange(range_ref1)
    write_memory.addMemoryRange(range_ref2)
    write_memory.setWriteClassRef(RefType().setDest("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS").setValue("/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"))
    return write_memory


class TestWriteDiagnosticWriteMemoryByAddress:
    """Tests for writeDiagnosticWriteMemoryByAddress — own element field values (Table 4.113)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticWriteMemoryByAddress without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressServices")
        package.createDiagnosticWriteMemoryByAddress("WriteMem1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteMemoryByAddress(parent, package.getReferrableElement("WriteMem1", DiagnosticWriteMemoryByAddress))

        child = parent.find("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "WriteMem1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        write_memory = _make_full_write_memory()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteMemoryByAddress(parent, write_memory)

        child = parent.find("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS")
        assert [c.tag for c in child] == ["SHORT-NAME", "MEMORY-RANGE-REFS", "WRITE-CLASS-REF"]
        range_refs = child.find("MEMORY-RANGE-REFS")
        assert [c.tag for c in range_refs] == ["MEMORY-RANGE-REF", "MEMORY-RANGE-REF"]
        assert range_refs[0].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert range_refs[0].get("DEST") == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert range_refs[1].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert child.find("WRITE-CLASS-REF").text == "/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"
        assert child.find("WRITE-CLASS-REF").get("DEST") == "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"

    def test_write_empty_memory_ranges_emits_no_wrapper(self):
        """Test that empty memoryRanges emit no MEMORY-RANGE-REFS wrapper tag."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressServices")
        write_memory = package.createDiagnosticWriteMemoryByAddress("WriteMem1")
        write_memory.setWriteClassRef(RefType().setDest("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS").setValue("/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteMemoryByAddress(parent, write_memory)

        child = parent.find("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS")
        assert child.find("MEMORY-RANGE-REFS") is None
        assert [c.tag for c in child] == ["SHORT-NAME", "WRITE-CLASS-REF"]

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        write_memory = _make_full_write_memory()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticWriteMemoryByAddress(parent, write_memory)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticWriteMemoryByAddress(AUTOSAR.getInstance(), "WriteMem1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS")
        ARXMLParser().readDiagnosticWriteMemoryByAddress(element, reloaded)
        assert len(reloaded.getMemoryRanges()) == 2
        assert reloaded.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert reloaded.getMemoryRanges()[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert reloaded.getMemoryRanges()[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert reloaded.getWriteClassRef() is not None
        assert reloaded.getWriteClassRef().getValue() == "/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"
        assert reloaded.getWriteClassRef().getDest() == "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"
