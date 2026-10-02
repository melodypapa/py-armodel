"""
Tests for writing DIAGNOSTIC-PARAMETER-IDENTIFIER elements —
DiagnosticParameterIdentifier, Table 4.127 (p.147, R23-11).

DiagnosticParameterIdentifier (Base most-derived ARElement) owns the * aggregation
dataElement (DATA-ELEMENTS wrapper, unbounded DIAGNOSTIC-PARAMETER items), the 0..1
attrs id and pidSize, and the 0..1 aggr supportInfoByte, AUTOSAR_00052.xsd group
DIAGNOSTIC-PARAMETER-IDENTIFIER l.40783.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_parameter_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter, DiagnosticSupportInfoByte
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticParameterIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_parameter_identifier() -> DiagnosticParameterIdentifier:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticParameterIdentifiers")
    parameter_identifier = package.createDiagnosticParameterIdentifier("Pid1")
    data_element = DiagnosticParameter()
    data_element.createIdent("Param1")
    parameter_identifier.addDataElement(data_element)
    parameter_identifier.setId(PositiveInteger().setValue("4"))
    parameter_identifier.setPidSize(PositiveInteger().setValue("6"))
    parameter_identifier.setSupportInfoByte(DiagnosticSupportInfoByte())
    return parameter_identifier


class TestWriteDiagnosticParameterIdentifier:
    """Tests for writeDiagnosticParameterIdentifier — own element field values (Table 4.127)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticParameterIdentifier without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticParameterIdentifiers")
        package.createDiagnosticParameterIdentifier("Pid1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdentifier(parent, package.getReferrableElement("Pid1", DiagnosticParameterIdentifier))

        child = parent.find("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Pid1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_empty_data_elements_emit_no_wrapper(self):
        """Test that an empty dataElements list emits no DATA-ELEMENTS wrapper element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticParameterIdentifiers")
        parameter_identifier = package.createDiagnosticParameterIdentifier("Pid1")
        parameter_identifier.setId(PositiveInteger().setValue("4"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdentifier(parent, parameter_identifier)

        child = parent.find("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        assert [c.tag for c in child] == ["SHORT-NAME", "ID"]
        assert child.find("DATA-ELEMENTS") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        parameter_identifier = _make_full_parameter_identifier()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdentifier(parent, parameter_identifier)

        child = parent.find("DIAGNOSTIC-PARAMETER-IDENTIFIER")
        assert [c.tag for c in child] == ["SHORT-NAME", "DATA-ELEMENTS", "ID", "PID-SIZE", "SUPPORT-INFO-BYTE"]
        data_elements = child.find("DATA-ELEMENTS")
        assert [c.tag for c in data_elements] == ["DIAGNOSTIC-PARAMETER"]
        assert data_elements.find("DIAGNOSTIC-PARAMETER/IDENT/SHORT-NAME").text == "Param1"
        assert child.find("ID").text == "4"
        assert child.find("PID-SIZE").text == "6"
        assert child.find("SUPPORT-INFO-BYTE") is not None

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        parameter_identifier = _make_full_parameter_identifier()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticParameterIdentifier(parent, parameter_identifier)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticParameterIdentifier(AUTOSAR.getInstance(), "Pid1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-PARAMETER-IDENTIFIER")
        ARXMLParser().readDiagnosticParameterIdentifier(element, reloaded)
        data_elements = reloaded.getDataElements()
        assert len(data_elements) == 1
        assert data_elements[0].getIdent() is not None
        assert data_elements[0].getIdent().getShortName() == "Param1"
        assert reloaded.getId() is not None
        assert reloaded.getId().getValue() == 4
        assert reloaded.getPidSize() is not None
        assert reloaded.getPidSize().getValue() == 6
        assert reloaded.getSupportInfoByte() is not None
