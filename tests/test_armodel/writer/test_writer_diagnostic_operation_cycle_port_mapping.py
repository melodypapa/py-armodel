"""
Tests for writing DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING elements —
DiagnosticOperationCyclePortMapping, Table 5.25 (p.250, R23-11).

DiagnosticOperationCyclePortMapping (Base most-derived DiagnosticSwMapping) owns 3 0..1 references
(operationCycleRef, swcFlatServiceDependencyRef, swcServiceDependencyInSystemIRef), AUTOSAR_00052.xsd group DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING
l.40438.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_operation_cycle_port_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticOperationCyclePortMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticOperationCyclePortMapping:
    """Tests for writeDiagnosticOperationCyclePortMapping — own element field values (Table 5.25)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticOperationCyclePortMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticOperationCyclePortMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticOperationCyclePortMapping(parent, package.getElement("M1", DiagnosticOperationCyclePortMapping))

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticOperationCyclePortMapping("M1")
        mapping.setOperationCycleRef(RefType().setValue("/AUTOSAR/OperationCycle1"))
        mapping.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        mapping.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticOperationCyclePortMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "OPERATION-CYCLE-REF", "SWC-FLAT-SERVICE-DEPENDENCY-REF", "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF"]
        assert child.find("OPERATION-CYCLE-REF").text == "/AUTOSAR/OperationCycle1"
        assert child.find("SWC-FLAT-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/SwcFlatServiceDependency1"
        assert child.find("SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF").text == "/AUTOSAR/SwcServiceDependencyInSystem1"
