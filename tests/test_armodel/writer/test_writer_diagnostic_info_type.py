"""
Tests for writing DIAGNOSTIC-INFO-TYPE elements — DiagnosticInfoType, Table 4.146
(p.160, R23-11).

DiagnosticInfoType (Base most-derived ARElement) owns the * aggregation
dataElement (DATA-ELEMENTS wrapper, unbounded DIAGNOSTIC-PARAMETER items) and the
0..1 attr id (ID), AUTOSAR_00052.xsd group DIAGNOSTIC-INFO-TYPE l.38300.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_info_type.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticInfoType
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


def _make_full_info_type() -> DiagnosticInfoType:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticInfoTypes")
    info_type = package.createDiagnosticInfoType("InfoType1")
    data_element = DiagnosticParameter()
    data_element.createIdent("Param1")
    info_type.addDataElement(data_element)
    info_type.setId(PositiveInteger().setValue("6"))
    return info_type


class TestWriteDiagnosticInfoType:
    """Tests for writeDiagnosticInfoType — own element field values (Table 4.146)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticInfoType without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticInfoTypes")
        package.createDiagnosticInfoType("InfoType1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticInfoType(parent, package.getReferrableElement("InfoType1", DiagnosticInfoType))

        child = parent.find("DIAGNOSTIC-INFO-TYPE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "InfoType1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_empty_data_elements_emit_no_wrapper(self):
        """Test that an empty dataElements list emits no DATA-ELEMENTS wrapper element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticInfoTypes")
        info_type = package.createDiagnosticInfoType("InfoType1")
        info_type.setId(PositiveInteger().setValue("6"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticInfoType(parent, info_type)

        child = parent.find("DIAGNOSTIC-INFO-TYPE")
        assert [c.tag for c in child] == ["SHORT-NAME", "ID"]
        assert child.find("DATA-ELEMENTS") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        info_type = _make_full_info_type()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticInfoType(parent, info_type)

        child = parent.find("DIAGNOSTIC-INFO-TYPE")
        assert [c.tag for c in child] == ["SHORT-NAME", "DATA-ELEMENTS", "ID"]
        data_elements = child.find("DATA-ELEMENTS")
        assert [c.tag for c in data_elements] == ["DIAGNOSTIC-PARAMETER"]
        assert data_elements.find("DIAGNOSTIC-PARAMETER/IDENT/SHORT-NAME").text == "Param1"
        assert child.find("ID").text == "6"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        info_type = _make_full_info_type()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticInfoType(parent, info_type)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticInfoType(AUTOSAR.getInstance(), "InfoType1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-INFO-TYPE")
        ARXMLParser().readDiagnosticInfoType(element, reloaded)
        data_elements = reloaded.getDataElements()
        assert len(data_elements) == 1
        assert data_elements[0].getIdent() is not None
        assert data_elements[0].getIdent().getShortName() == "Param1"
        assert reloaded.getId() is not None
        assert reloaded.getId().getValue() == 6
