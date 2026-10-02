"""
Tests for writing DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING elements —
DiagnosticEventToTroubleCodeJ1939Mapping, Table 5.43 (p.269, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_event_to_trouble_code_j1939_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToTroubleCodeJ1939Mapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEventToTroubleCodeJ1939Mapping:
    """Tests for writeDiagnosticEventToTroubleCodeJ1939Mapping — own element field values (Table 5.43)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventToTroubleCodeJ1939Mapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticEventToTroubleCodeJ1939Mapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToTroubleCodeJ1939Mapping(parent, package.getReferrableElement("M1", DiagnosticEventToTroubleCodeJ1939Mapping))

        child = parent.find("DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticEventToTroubleCodeJ1939Mapping("M1")
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))
        mapping.setTroubleCodeJ1939Ref(RefType().setValue("/AUTOSAR/TroubleCodeJ19391"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventToTroubleCodeJ1939Mapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENT-REF", "TROUBLE-CODE-J-1939-REF"]
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
        assert child.find("TROUBLE-CODE-J-1939-REF").text == "/AUTOSAR/TroubleCodeJ19391"
