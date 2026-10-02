"""
Tests for writing DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING elements —
DiagnosticEventToSecurityEventMapping, Table 5.30 (p.257, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_event_to_security_event_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToSecurityEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToSecurityEventMapping:
    """Tests for writeDiagnosticEventToSecurityEventMapping — own element field values (Table 5.30)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToSecurityEventMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToSecurityEventMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToSecurityEventMapping(parent, package.getReferrableElement("M1", DiagnosticEventToSecurityEventMapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToSecurityEventMapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        mapping.setSecurityEventPropsRef(RefType().setValue("/AUTOSAR/SecurityEventProps1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToSecurityEventMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "SECURITY-EVENT-PROPS-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("SECURITY-EVENT-PROPS-REF").text == "/AUTOSAR/SecurityEventProps1"
