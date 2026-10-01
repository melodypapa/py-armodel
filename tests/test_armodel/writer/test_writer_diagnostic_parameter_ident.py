"""
Tests for writing DIAGNOSTIC-PARAMETER-IDENT elements — DiagnosticParameterIdent, Table 4.7 (p.37, R23-11).

DiagnosticParameterIdent (Base = IdentCaption) carries the top-level SUB-ELEMENTS
aggregation (XSD group DIAGNOSTIC-PARAMETER-IDENT, AUTOSAR_00052.xsd l.40735 —
choice of DIAGNOSTIC-PARAMETER-ELEMENT). The writer reads the model via the
getSubElements getter; DIAGNOSTIC-PARAMETER-IDENT is emitted through the
DiagnosticParameter IDENT dispatch, which replaces the former identity-only
SHORT-NAME write.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_parameter_ident.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticParameterIdent:
    """Tests for writeDiagnosticParameterIdent — own element field values (Table 4.7)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that SUB-ELEMENTS is emitted after the identity elements with their content."""
        ident = DiagnosticParameterIdent(AUTOSAR.getInstance(), "Pid1")
        sub_element = ident.createSubElement("Sub1")
        array_size = PositiveInteger()
        array_size.setValue("4")
        sub_element.setArraySize(array_size)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdent(parent, ident)

        child = parent.find("IDENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Pid1"
        sub_elements = child.find("SUB-ELEMENTS")
        assert sub_elements is not None
        items = list(sub_elements)
        assert [item.tag for item in items] == ["DIAGNOSTIC-PARAMETER-ELEMENT"]
        assert items[0].find("SHORT-NAME").text == "Sub1"
        assert items[0].find("ARRAY-SIZE").text == "4"
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "SUB-ELEMENTS"]

    def test_write_empty_aggregation_omits_wrapper(self):
        """Test that an empty SUB-ELEMENTS aggregation emits no wrapper tag."""
        ident = DiagnosticParameterIdent(AUTOSAR.getInstance(), "Pid1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterIdent(parent, ident)

        child = parent.find("IDENT")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("SUB-ELEMENTS") is None

    def test_ident_dispatch_writes_sub_elements(self):
        """Test that writeDiagnosticParameter emits IDENT/SUB-ELEMENTS with their content."""
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        parameter = DiagnosticParameter()
        ident = parameter.createIdent("Pid1")
        ident.createSubElement("Sub1")
        did.addDataElement(parameter)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifier(parent, did)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER")
        ident_element = child.find("DATA-ELEMENTS/DIAGNOSTIC-PARAMETER/IDENT")
        assert ident_element is not None
        assert ident_element.find("SHORT-NAME").text == "Pid1"
        sub_elements = ident_element.find("SUB-ELEMENTS")
        assert sub_elements is not None
        assert [item.tag for item in sub_elements] == ["DIAGNOSTIC-PARAMETER-ELEMENT"]
        assert sub_elements[0].find("SHORT-NAME").text == "Sub1"


class TestDiagnosticParameterIdentRoundTrip:
    """Full set → save → reload → assert cycle through the document tree."""

    def test_round_trip(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        parameter = DiagnosticParameter()
        ident = parameter.createIdent("Pid1")
        sub_element = ident.createSubElement("Sub1")
        array_size = PositiveInteger()
        array_size.setValue("4")
        sub_element.setArraySize(array_size)
        nested = sub_element.createSubElement("Leaf")
        nested_array_size = PositiveInteger()
        nested_array_size.setValue("8")
        nested.setArraySize(nested_array_size)
        did.addDataElement(parameter)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getElement("Di", DiagnosticDataIdentifier)
            assert did_2 is not None
            parameter_2 = did_2.getDataElements()[0]
            ident_2 = parameter_2.getIdent()
            assert ident_2 is not None
            assert ident_2.getShortName() == "Pid1"
            assert len(ident_2.getSubElements()) == 1
            sub_element_2 = ident_2.getSubElements()[0]
            assert isinstance(sub_element_2, DiagnosticParameterElement)
            assert sub_element_2.getShortName() == "Sub1"
            assert sub_element_2.getArraySize() is not None
            assert sub_element_2.getArraySize().getValue() == 4
            assert len(sub_element_2.getSubElements()) == 1
            leaf_2 = sub_element_2.getSubElements()[0]
            assert leaf_2.getShortName() == "Leaf"
            assert leaf_2.getArraySize() is not None
            assert leaf_2.getArraySize().getValue() == 8
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
