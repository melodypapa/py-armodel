"""
Tests for writing the DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS element —
DiagnosticRequestEmissionRelatedDTCClass, Table 4.136 (p.154, R23-11).

DiagnosticRequestEmissionRelatedDTCClass (Base most-derived
DiagnosticServiceClass) defines no own attributes; the writer emits the
IDENTIFIABLE wrapper only, and the dispatch entry is writeARPackageElementRest →
writeDiagnosticRequestEmissionRelatedDTCClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_emission_related_dtc_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestEmissionRelatedDTCClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestEmissionRelatedDTCClass:
    """Tests for writeDiagnosticRequestEmissionRelatedDTCClass — own element field values (Table 4.136)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0307Classes")
        package.createDiagnosticRequestEmissionRelatedDTCClass("Red1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTCClass(parent, package.getReferrableElement("Red1", DiagnosticRequestEmissionRelatedDTCClass))

        child = parent.find("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Red1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0307Classes")
        package.createDiagnosticRequestEmissionRelatedDTCClass("Red1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Red1", DiagnosticRequestEmissionRelatedDTCClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest(
            "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"), reloaded_package
        )
        reloaded = reloaded_package.getReferrableElement("Red1", DiagnosticRequestEmissionRelatedDTCClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Red1"
