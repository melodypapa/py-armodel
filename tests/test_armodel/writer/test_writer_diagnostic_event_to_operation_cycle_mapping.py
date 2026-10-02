"""
Tests for writing DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING elements —
DiagnosticEventToOperationCycleMapping, Table 5.20 (p.245, R23-11).

DiagnosticEventToOperationCycleMapping (Base most-derived DiagnosticMapping) owns 2 0..1 references
(diagnosticEventRef, operationCycleRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING
l.36841.

Round-trip counterpart: tests/test_armodel/parser/test_diagnosticeventtooperationcyclemapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToOperationCycleMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToOperationCycleMapping:
    """Tests for writeDiagnosticEventToOperationCycleMapping — own element field values (Table 5.20)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToOperationCycleMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToOperationCycleMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToOperationCycleMapping(parent, package.getReferrableElement("M1", DiagnosticEventToOperationCycleMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToOperationCycleMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1").setDest("DEST"))
        mapping.setOperationCycleRef(RefType().setValue("/AUTOSAR/OperationCycle1").setDest("DEST"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToOperationCycleMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "OPERATION-CYCLE-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("OPERATION-CYCLE-REF").text == "/AUTOSAR/OperationCycle1"
