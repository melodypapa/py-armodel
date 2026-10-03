"""
Tests for writing DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC elements —
DiagnosticRequestEmissionRelatedDTC, Table 4.135 (p.154, R23-11).

DiagnosticRequestEmissionRelatedDTC (Base most-derived DiagnosticServiceInstance)
owns one 0..1 reference requestEmissionRelatedDtcClass
(REQUEST-EMISSION-RELATED-DTC-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC l.41879.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_emission_related_dtc.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestEmissionRelatedDTC
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


def _make_full_mode0307() -> DiagnosticRequestEmissionRelatedDTC:
    package = AUTOSAR.getInstance().createARPackage("OBDMode0307Services")
    mode0307 = package.createDiagnosticRequestEmissionRelatedDTC("Mode0307")
    mode0307.setRequestEmissionRelatedDtcClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS").setValue("/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1"))
    return mode0307


class TestWriteDiagnosticRequestEmissionRelatedDTC:
    """Tests for writeDiagnosticRequestEmissionRelatedDTC — own element field values (Table 4.135)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestEmissionRelatedDTC without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0307Services")
        package.createDiagnosticRequestEmissionRelatedDTC("Mode0307")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTC(parent, package.getReferrableElement("Mode0307", DiagnosticRequestEmissionRelatedDTC))

        child = parent.find("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode0307"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode0307 = _make_full_mode0307()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTC(parent, mode0307)

        child = parent.find("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-EMISSION-RELATED-DTC-CLASS-REF"]
        assert child.find("REQUEST-EMISSION-RELATED-DTC-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1"
        assert child.find("REQUEST-EMISSION-RELATED-DTC-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode0307 = _make_full_mode0307()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestEmissionRelatedDTC(parent, mode0307)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestEmissionRelatedDTC(AUTOSAR.getInstance(), "Mode0307")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC")
        ARXMLParser().readDiagnosticRequestEmissionRelatedDTC(element, reloaded)
        assert reloaded.getRequestEmissionRelatedDtcClassRef() is not None
        assert reloaded.getRequestEmissionRelatedDtcClassRef().getValue() == "/AUTOSAR/DiagnosticRequestEmissionRelatedDTCClasses/Class1"
        assert reloaded.getRequestEmissionRelatedDtcClassRef().getDest() == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"
