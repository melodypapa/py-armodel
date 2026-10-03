"""
Tests for writing DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO elements —
DiagnosticClearResetEmissionRelatedInfo, Table 4.137 (p.155, R23-11).

DiagnosticClearResetEmissionRelatedInfo (Base most-derived
DiagnosticServiceInstance) owns one 0..1 reference
clearResetEmissionRelatedDiagnosticInfoClass
(CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO l.32432.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_clear_reset_emission_related_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticClearResetEmissionRelatedInfo
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


def _make_full_mode04() -> DiagnosticClearResetEmissionRelatedInfo:
    package = AUTOSAR.getInstance().createARPackage("OBDMode04Services")
    mode04 = package.createDiagnosticClearResetEmissionRelatedInfo("Mode04")
    mode04.setClearResetEmissionRelatedDiagnosticInfoClassRef(
        RefType().setDest("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS").setValue("/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1")
    )
    return mode04


class TestWriteDiagnosticClearResetEmissionRelatedInfo:
    """Tests for writeDiagnosticClearResetEmissionRelatedInfo — own element field values (Table 4.137)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticClearResetEmissionRelatedInfo without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode04Services")
        package.createDiagnosticClearResetEmissionRelatedInfo("Mode04")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticClearResetEmissionRelatedInfo(parent, package.getReferrableElement("Mode04", DiagnosticClearResetEmissionRelatedInfo))

        child = parent.find("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode04"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode04 = _make_full_mode04()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticClearResetEmissionRelatedInfo(parent, mode04)

        child = parent.find("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO")
        assert [c.tag for c in child] == ["SHORT-NAME", "CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF"]
        assert child.find("CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF").text == "/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1"
        assert child.find("CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF").get("DEST") == "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode04 = _make_full_mode04()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticClearResetEmissionRelatedInfo(parent, mode04)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticClearResetEmissionRelatedInfo(AUTOSAR.getInstance(), "Mode04")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO")
        ARXMLParser().readDiagnosticClearResetEmissionRelatedInfo(element, reloaded)
        assert reloaded.getClearResetEmissionRelatedDiagnosticInfoClassRef() is not None
        assert reloaded.getClearResetEmissionRelatedDiagnosticInfoClassRef().getValue() == "/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1"
        assert reloaded.getClearResetEmissionRelatedDiagnosticInfoClassRef().getDest() == "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"
