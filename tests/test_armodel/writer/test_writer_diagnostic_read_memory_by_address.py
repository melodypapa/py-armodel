"""
Tests for writing DIAGNOSTIC-READ-MEMORY-BY-ADDRESS elements —
DiagnosticReadMemoryByAddress, Table 4.115 (p.142, R23-11).

DiagnosticReadMemoryByAddress (Base most-derived DiagnosticMemoryAddressableRangeAccess)
inherits the 0..* memoryRange refs (MEMORY-RANGE-REFS wrapper) and owns one 0..1
reference readClass (READ-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-MEMORY-BY-ADDRESS l.41433: MEMORY-RANGE-REFS, READ-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_memory_by_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadMemoryByAddress
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


def _make_full_read_memory() -> DiagnosticReadMemoryByAddress:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticReadMemoryByAddressServices")
    read_memory = package.createDiagnosticReadMemoryByAddress("ReadMem1")
    range_ref1 = RefType().setDest("DIAGNOSTIC-MEMORY-IDENTIFIER").setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1")
    range_ref2 = RefType().setDest("DIAGNOSTIC-MEMORY-IDENTIFIER").setValue("/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2")
    read_memory.addMemoryRange(range_ref1)
    read_memory.addMemoryRange(range_ref2)
    read_memory.setReadClassRef(RefType().setDest("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS").setValue("/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"))
    return read_memory


class TestWriteDiagnosticReadMemoryByAddress:
    """Tests for writeDiagnosticReadMemoryByAddress — own element field values (Table 4.115)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticReadMemoryByAddress without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadMemoryByAddressServices")
        package.createDiagnosticReadMemoryByAddress("ReadMem1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadMemoryByAddress(parent, package.getReferrableElement("ReadMem1", DiagnosticReadMemoryByAddress))

        child = parent.find("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadMem1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        read_memory = _make_full_read_memory()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadMemoryByAddress(parent, read_memory)

        child = parent.find("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS")
        assert [c.tag for c in child] == ["SHORT-NAME", "MEMORY-RANGE-REFS", "READ-CLASS-REF"]
        range_refs = child.find("MEMORY-RANGE-REFS")
        assert [c.tag for c in range_refs] == ["MEMORY-RANGE-REF", "MEMORY-RANGE-REF"]
        assert range_refs[0].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert range_refs[0].get("DEST") == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert range_refs[1].text == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert child.find("READ-CLASS-REF").text == "/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"
        assert child.find("READ-CLASS-REF").get("DEST") == "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"

    def test_write_empty_memory_ranges_emits_no_wrapper(self):
        """Test that empty memoryRanges emit no MEMORY-RANGE-REFS wrapper tag."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadMemoryByAddressServices")
        read_memory = package.createDiagnosticReadMemoryByAddress("ReadMem1")
        read_memory.setReadClassRef(RefType().setDest("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS").setValue("/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadMemoryByAddress(parent, read_memory)

        child = parent.find("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS")
        assert child.find("MEMORY-RANGE-REFS") is None
        assert [c.tag for c in child] == ["SHORT-NAME", "READ-CLASS-REF"]

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        read_memory = _make_full_read_memory()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticReadMemoryByAddress(parent, read_memory)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticReadMemoryByAddress(AUTOSAR.getInstance(), "ReadMem1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-READ-MEMORY-BY-ADDRESS")
        ARXMLParser().readDiagnosticReadMemoryByAddress(element, reloaded)
        assert len(reloaded.getMemoryRanges()) == 2
        assert reloaded.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert reloaded.getMemoryRanges()[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert reloaded.getMemoryRanges()[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert reloaded.getReadClassRef() is not None
        assert reloaded.getReadClassRef().getValue() == "/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"
        assert reloaded.getReadClassRef().getDest() == "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"
