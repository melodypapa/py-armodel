"""
Tests for writing DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING elements —
DiagnosticEnableConditionPortMapping, Table 5.26 (p.252, R23-11).

DiagnosticEnableConditionPortMapping (Base most-derived DiagnosticSwMapping) owns 3 0..1 references
(enableConditionRef, swcFlatServiceDependencyRef, swcServiceDependencyInSystemIRef), AUTOSAR_00052.xsd group DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING
l.35627.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_enable_condition_port_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionPortMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEnableConditionPortMapping:
    """Tests for writeDiagnosticEnableConditionPortMapping — own element field values (Table 5.26)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEnableConditionPortMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEnableConditionPortMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableConditionPortMapping(parent, package.getElement("M1", DiagnosticEnableConditionPortMapping))

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEnableConditionPortMapping("M1")
        mapping.setEnableConditionRef(RefType().setValue("/AUTOSAR/EnableCondition1"))
        mapping.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        mapping.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnableConditionPortMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "ENABLE-CONDITION-REF", "SWC-FLAT-SERVICE-DEPENDENCY-REF", "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF"]
        assert child.find("ENABLE-CONDITION-REF").text == "/AUTOSAR/EnableCondition1"
        assert child.find("SWC-FLAT-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/SwcFlatServiceDependency1"
        assert child.find("SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF").text == "/AUTOSAR/SwcServiceDependencyInSystem1"
