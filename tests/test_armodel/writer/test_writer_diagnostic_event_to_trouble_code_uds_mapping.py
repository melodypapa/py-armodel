"""
Tests for writing DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING elements —
DiagnosticEventToTroubleCodeUdsMapping, Table 5.19 (p.245, R23-11).

DiagnosticEventToTroubleCodeUdsMapping (Base most-derived DiagnosticMapping) owns 2 0..1 references
(diagnosticEventRef, troubleCodeUdsRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING
l.37073.

Round-trip counterpart: tests/test_armodel/parser/test_diagnosticeventtotroublecodeudsmapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToTroubleCodeUdsMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToTroubleCodeUdsMapping:
    """Tests for writeDiagnosticEventToTroubleCodeUdsMapping — own element field values (Table 5.19)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToTroubleCodeUdsMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToTroubleCodeUdsMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToTroubleCodeUdsMapping(parent, package.getElement("M1", DiagnosticEventToTroubleCodeUdsMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToTroubleCodeUdsMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        mapping.setTroubleCodeUdsRef(RefType().setValue("/AUTOSAR/TroubleCodeUds1").setDest("DEST"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToTroubleCodeUdsMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "TROUBLE-CODE-UDS-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("TROUBLE-CODE-UDS-REF").text == "/AUTOSAR/TroubleCodeUds1"
