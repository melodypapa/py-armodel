"""
Tests for writing DIAGNOSTIC-EVENT-PORT-MAPPING elements —
DiagnosticEventPortMapping, Table 5.24 (p.249, R23-11).

DiagnosticEventPortMapping (Base most-derived DiagnosticSwMapping) owns 4 0..1 references
(bswServiceDependencyRef, diagnosticEventRef, swcFlatServiceDependencyRef, swcServiceDependencyInSystemIRef), AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-PORT-MAPPING
l.36577.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_event_port_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventPortMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventPortMapping:
    """Tests for writeDiagnosticEventPortMapping — own element field values (Table 5.24)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventPortMapping without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventPortMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventPortMapping(parent, package.getReferrableElement("M1", DiagnosticEventPortMapping))

        child = parent.find("DIAGNOSTIC-EVENT-PORT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs_in_xsd_order(self):
        """Test that all references are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventPortMapping("M1")
        mapping.setBswServiceDependencyRef(RefType().setValue("/AUTOSAR/BswServiceDependency1"))
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        mapping.setSwcFlatServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcFlatServiceDependency1"))
        mapping.setSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/SwcServiceDependencyInSystem1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventPortMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-PORT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "BSW-SERVICE-DEPENDENCY-REF", "DIAGNOSTIC-EVENT-REF", "SWC-FLAT-SERVICE-DEPENDENCY-REF", "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF"]
        assert child.find("BSW-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/BswServiceDependency1"
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("SWC-FLAT-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/SwcFlatServiceDependency1"
        assert child.find("SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF").text == "/AUTOSAR/SwcServiceDependencyInSystem1"
