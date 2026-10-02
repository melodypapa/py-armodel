"""
Tests for writing DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING elements —
DiagnosticSecurityEventReportingModeMapping, Table 5.18 (p.243, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_security_event_reporting_mode_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSecurityEventReportingModeMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticSecurityEventReportingModeMapping:
    """Tests for writeDiagnosticSecurityEventReportingModeMapping — own element field values (Table 5.18)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticSecurityEventReportingModeMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticSecurityEventReportingModeMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityEventReportingModeMapping(parent, package.getElement("M1", DiagnosticSecurityEventReportingModeMapping))

        child = parent.find("DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticSecurityEventReportingModeMapping("M1")
        mapping.setDataElementRef(RefType().setValue("/AUTOSAR/DataElement1"))
        mapping.setSecurityEventRef(RefType().setValue("/AUTOSAR/SecurityEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSecurityEventReportingModeMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DATA-ELEMENT-REF", "SECURITY-EVENT-REF"]
        assert child.find("DATA-ELEMENT-REF").text == "/AUTOSAR/DataElement1"
        assert child.find("SECURITY-EVENT-REF").text == "/AUTOSAR/SecurityEvent1"
