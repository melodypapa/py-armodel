"""
Tests for writing DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER elements —
DiagnosticTestRoutineIdentifier, Table 4.143 (p.158, R23-11).

DiagnosticTestRoutineIdentifier (Base most-derived ARElement) owns three 0..1
attrs — id (ID), requestDataSize (REQUEST-DATA-SIZE), responseDataSize
(RESPONSE-DATA-SIZE), AUTOSAR_00052.xsd group DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER
l.46056.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_test_routine_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTestRoutineIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_routine_identifier() -> DiagnosticTestRoutineIdentifier:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticTestRoutineIdentifiers")
    routine_identifier = package.createDiagnosticTestRoutineIdentifier("Routine1")
    routine_identifier.setId(PositiveInteger().setValue("1"))
    routine_identifier.setRequestDataSize(PositiveInteger().setValue("8"))
    routine_identifier.setResponseDataSize(PositiveInteger().setValue("16"))
    return routine_identifier


class TestWriteDiagnosticTestRoutineIdentifier:
    """Tests for writeDiagnosticTestRoutineIdentifier — own element field values (Table 4.143)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticTestRoutineIdentifier without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestRoutineIdentifiers")
        package.createDiagnosticTestRoutineIdentifier("Routine1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTestRoutineIdentifier(parent, package.getReferrableElement("Routine1", DiagnosticTestRoutineIdentifier))

        child = parent.find("DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Routine1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        routine_identifier = _make_full_routine_identifier()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTestRoutineIdentifier(parent, routine_identifier)

        child = parent.find("DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER")
        assert [c.tag for c in child] == ["SHORT-NAME", "ID", "REQUEST-DATA-SIZE", "RESPONSE-DATA-SIZE"]
        assert child.find("ID").text == "1"
        assert child.find("REQUEST-DATA-SIZE").text == "8"
        assert child.find("RESPONSE-DATA-SIZE").text == "16"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        routine_identifier = _make_full_routine_identifier()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticTestRoutineIdentifier(parent, routine_identifier)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticTestRoutineIdentifier(AUTOSAR.getInstance(), "Routine1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER")
        ARXMLParser().readDiagnosticTestRoutineIdentifier(element, reloaded)
        assert reloaded.getId() is not None
        assert reloaded.getId().getValue() == 1
        assert reloaded.getRequestDataSize() is not None
        assert reloaded.getRequestDataSize().getValue() == 8
        assert reloaded.getResponseDataSize() is not None
        assert reloaded.getResponseDataSize().getValue() == 16
