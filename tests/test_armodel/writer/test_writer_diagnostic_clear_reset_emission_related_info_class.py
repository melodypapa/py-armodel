"""
Tests for writing the DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS element —
DiagnosticClearResetEmissionRelatedInfoClass, Table 4.138 (p.155, R23-11).

DiagnosticClearResetEmissionRelatedInfoClass (Base most-derived
DiagnosticServiceClass) defines no own attributes; the writer emits the
IDENTIFIABLE wrapper only, and the dispatch entry is writeARPackageElementRest →
writeDiagnosticClearResetEmissionRelatedInfoClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_clear_reset_emission_related_info_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearResetEmissionRelatedInfoClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticClearResetEmissionRelatedInfoClass:
    """Tests for writeDiagnosticClearResetEmissionRelatedInfoClass — own element field values (Table 4.138)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode04Classes")
        package.createDiagnosticClearResetEmissionRelatedInfoClass("Cre1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticClearResetEmissionRelatedInfoClass(parent, package.getReferrableElement("Cre1", DiagnosticClearResetEmissionRelatedInfoClass))

        child = parent.find("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Cre1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode04Classes")
        package.createDiagnosticClearResetEmissionRelatedInfoClass("Cre1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Cre1", DiagnosticClearResetEmissionRelatedInfoClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest(
            "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"), reloaded_package
        )
        reloaded = reloaded_package.getReferrableElement("Cre1", DiagnosticClearResetEmissionRelatedInfoClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Cre1"
