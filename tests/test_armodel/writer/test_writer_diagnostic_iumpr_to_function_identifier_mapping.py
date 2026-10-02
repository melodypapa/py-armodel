"""
Tests for writing DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING elements —
DiagnosticIumprToFunctionIdentifierMapping, Table 5.39 (p.265, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_iumpr_to_function_identifier_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprToFunctionIdentifierMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticIumprToFunctionIdentifierMapping:
    """Tests for writeDiagnosticIumprToFunctionIdentifierMapping — own element field values (Table 5.39)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticIumprToFunctionIdentifierMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticIumprToFunctionIdentifierMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIumprToFunctionIdentifierMapping(parent, package.getElement("M1", DiagnosticIumprToFunctionIdentifierMapping))

        child = parent.find("DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticIumprToFunctionIdentifierMapping("M1")
        mapping.setFunctionIdentifierRef(RefType().setValue("/AUTOSAR/FunctionIdentifier1"))
        mapping.setIumprRef(RefType().setValue("/AUTOSAR/Iumpr1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIumprToFunctionIdentifierMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "FUNCTION-IDENTIFIER-REF", "IUMPR-REF"]
        assert child.find("FUNCTION-IDENTIFIER-REF").text == "/AUTOSAR/FunctionIdentifier1"
        assert child.find("IUMPR-REF").text == "/AUTOSAR/Iumpr1"
