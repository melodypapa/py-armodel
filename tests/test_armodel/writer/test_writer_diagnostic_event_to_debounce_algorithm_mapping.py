"""
Tests for writing DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING elements —
DiagnosticEventToDebounceAlgorithmMapping, Table 5.21 (p.246, R23-11).

DiagnosticEventToDebounceAlgorithmMapping (Base most-derived DiagnosticMapping) owns 2 0..1 references
(debounceAlgorithmRef, diagnosticEventRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING
l.36725.

Round-trip counterpart: tests/test_armodel/parser/test_diagnosticeventtodebouncealgorithmmapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToDebounceAlgorithmMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToDebounceAlgorithmMapping:
    """Tests for writeDiagnosticEventToDebounceAlgorithmMapping — own element field values (Table 5.21)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToDebounceAlgorithmMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToDebounceAlgorithmMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToDebounceAlgorithmMapping(parent, package.getElement("M1", DiagnosticEventToDebounceAlgorithmMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToDebounceAlgorithmMapping("M1")
        mapping.setDebounceAlgorithmRef(RefType().setValue("/AUTOSAR/DebounceAlgorithm1").setDest("DEST"))
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToDebounceAlgorithmMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DEBOUNCE-ALGORITHM-REF", "DIAGNOSTIC-EVENT-REF"]
        assert child.find("DEBOUNCE-ALGORITHM-REF").text == "/AUTOSAR/DebounceAlgorithm1"
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
