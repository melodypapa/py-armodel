"""
Tests for writing DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING elements —
DiagnosticStorageConditionPortMapping, Table 5.27 (p.253, R23-11).

DiagnosticStorageConditionPortMapping (Base most-derived DiagnosticSwMapping) owns 3 0..1 references
(diagnosticStorageConditionRef, swcFlatServiceDependencyRef, swcServiceDependencyInSystemIRef), AUTOSAR_00052.xsd group DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING
l.45750.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_storage_condition_port_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageConditionPortMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticStorageConditionPortMapping:
    """Tests for writeDiagnosticStorageConditionPortMapping — own element field values (Table 5.27)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticStorageConditionPortMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticStorageConditionPortMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageConditionPortMapping(parent, package.getReferrableElement("M1", DiagnosticStorageConditionPortMapping))

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticStorageConditionPortMapping("M1")
        mapping.setDiagnosticStorageConditionRef(RefType().setValue("/AUTOSAR/DiagnosticStorageCondition1"))
        mapping.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        mapping.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticStorageConditionPortMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-STORAGE-CONDITION-REF", "SWC-FLAT-SERVICE-DEPENDENCY-REF", "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF"]
        assert child.find("DIAGNOSTIC-STORAGE-CONDITION-REF").text == "/AUTOSAR/DiagnosticStorageCondition1"
        assert child.find("SWC-FLAT-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/SwcFlatServiceDependency1"
        assert child.find("SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF").text == "/AUTOSAR/SwcServiceDependencyInSystem1"
