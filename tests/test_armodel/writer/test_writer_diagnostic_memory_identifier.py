"""
Tests for writing DIAGNOSTIC-MEMORY-IDENTIFIER elements —
DiagnosticMemoryIdentifier, Table 4.112 (p.140, R23-11).

DiagnosticMemoryIdentifier (Base most-derived ARElement) owns one 0..1 reference
(accessPermission) and five 0..1 value attributes (id, memoryHighAddress,
memoryHighAddressLabel, memoryLowAddress, memoryLowAddressLabel), AUTOSAR_00052.xsd
group DIAGNOSTIC-MEMORY-IDENTIFIER l.39770: ACCESS-PERMISSION-REF, ID,
MEMORY-HIGH-ADDRESS, MEMORY-HIGH-ADDRESS-LABEL, MEMORY-LOW-ADDRESS,
MEMORY-LOW-ADDRESS-LABEL.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_memory_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_identifier() -> DiagnosticMemoryIdentifier:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryIdentifiers")
    identifier = package.createDiagnosticMemoryIdentifier("Segment1")
    identifier.setAccessPermissionRef(RefType().setDest("DIAGNOSTIC-ACCESS-PERMISSION").setValue("/AUTOSAR/DiagnosticAccessPermissions/Permission1"))
    identifier.setId(PositiveInteger().setValue("1"))
    identifier.setMemoryHighAddress(PositiveInteger().setValue("4096"))
    identifier.setMemoryHighAddressLabel(String().setValue("0x1000"))
    identifier.setMemoryLowAddress(PositiveInteger().setValue("0"))
    identifier.setMemoryLowAddressLabel(String().setValue("0x0"))
    return identifier


class TestWriteDiagnosticMemoryIdentifier:
    """Tests for writeDiagnosticMemoryIdentifier — own element field values (Table 4.112)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticMemoryIdentifier without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryIdentifiers")
        package.createDiagnosticMemoryIdentifier("Segment1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMemoryIdentifier(parent, package.getReferrableElement("Segment1", DiagnosticMemoryIdentifier))

        child = parent.find("DIAGNOSTIC-MEMORY-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Segment1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        identifier = _make_full_identifier()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMemoryIdentifier(parent, identifier)

        child = parent.find("DIAGNOSTIC-MEMORY-IDENTIFIER")
        assert [c.tag for c in child] == ["SHORT-NAME", "ACCESS-PERMISSION-REF", "ID", "MEMORY-HIGH-ADDRESS", "MEMORY-HIGH-ADDRESS-LABEL", "MEMORY-LOW-ADDRESS", "MEMORY-LOW-ADDRESS-LABEL"]
        assert child.find("ACCESS-PERMISSION-REF").text == "/AUTOSAR/DiagnosticAccessPermissions/Permission1"
        assert child.find("ACCESS-PERMISSION-REF").get("DEST") == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert child.find("ID").text == "1"
        assert child.find("MEMORY-HIGH-ADDRESS").text == "4096"
        assert child.find("MEMORY-HIGH-ADDRESS-LABEL").text == "0x1000"
        assert child.find("MEMORY-LOW-ADDRESS").text == "0"
        assert child.find("MEMORY-LOW-ADDRESS-LABEL").text == "0x0"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        identifier = _make_full_identifier()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticMemoryIdentifier(parent, identifier)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticMemoryIdentifier(AUTOSAR.getInstance(), "Segment1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-MEMORY-IDENTIFIER")
        ARXMLParser().readDiagnosticMemoryIdentifier(element, reloaded)
        assert reloaded.getAccessPermissionRef() is not None
        assert reloaded.getAccessPermissionRef().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Permission1"
        assert reloaded.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert reloaded.getId().getValue() == 1
        assert reloaded.getMemoryHighAddress().getValue() == 4096
        assert reloaded.getMemoryHighAddressLabel().getValue() == "0x1000"
        assert reloaded.getMemoryLowAddress().getValue() == 0
        assert reloaded.getMemoryLowAddressLabel().getValue() == "0x0"
