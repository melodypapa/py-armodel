"""
Tests for writing DIAGNOSTIC-ABSTRACT-PARAMETER group elements — DiagnosticAbstractParameter, Table 4.8 (p.37, R23-11).

DiagnosticAbstractParameter (abstract, Base = ARObject) owns the BIT-OFFSET /
DATA-ELEMENTS / PARAMETER-SIZE XML group (XSD group DIAGNOSTIC-ABSTRACT-PARAMETER,
AUTOSAR_00052.xsd l.31435 — group order BIT-OFFSET, DATA-ELEMENTS, PARAMETER-SIZE;
the DIAGNOSTIC-PARAMETER complexType l.40615 serializes the group before IDENT/
SUPPORT-INFO/VARIATION-POINT, the DIAGNOSTIC-PARAMETER-ELEMENT complexType
l.40656 between the identity groups and ARRAY-SIZE/SUB-ELEMENTS). The PDF
multiplicity of dataElement is 0..1 — the wrapper is emitted only when the field
is set, with a single DIAGNOSTIC-DATA-ELEMENT item dispatched to
writeDiagnosticDataElement since the Table 4.9 sync.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_abstract_parameter.py
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


class TestWriteDiagnosticAbstractParameter:
    """Tests for writeDiagnosticAbstractParameter — own group field values (Table 4.8)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that BIT-OFFSET, DATA-ELEMENTS and PARAMETER-SIZE are emitted in group order with their values."""
        parameter = DiagnosticParameter()
        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        parameter.setBitOffset(bit_offset)
        parameter.createDataElement("De1")
        parameter_size = PositiveInteger()
        parameter_size.setValue("16")
        parameter.setParameterSize(parameter_size)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAbstractParameter(parent, parameter)

        assert parent.find("BIT-OFFSET").text == "8"
        assert parent.find("DATA-ELEMENTS/DIAGNOSTIC-DATA-ELEMENT/SHORT-NAME").text == "De1"
        assert parent.find("PARAMETER-SIZE").text == "16"
        tags = [c.tag for c in parent]
        assert tags == ["BIT-OFFSET", "DATA-ELEMENTS", "PARAMETER-SIZE"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset base attributes emit no elements."""
        parameter = DiagnosticParameter()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAbstractParameter(parent, parameter)

        assert [c.tag for c in parent] == []

    def test_diagnostic_parameter_dispatch_orders_base_group_before_ident(self):
        """Test that writeDiagnosticParameter emits the base group before IDENT/SUPPORT-INFO/VARIATION-POINT."""
        parameter = DiagnosticParameter()
        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        parameter.setBitOffset(bit_offset)
        parameter.createIdent("Pid1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameter(parent, parameter)

        child = parent.find("DIAGNOSTIC-PARAMETER")
        assert [c.tag for c in child] == ["BIT-OFFSET", "IDENT"]

    def test_diagnostic_parameter_element_dispatch_orders_base_group_before_array_size(self):
        """Test that writeDiagnosticParameterElement emits the base group between the identity and own groups."""
        parameter_element = DiagnosticParameterElement(AUTOSAR.getInstance(), "Elem1")
        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        parameter_element.setBitOffset(bit_offset)
        parameter_size = PositiveInteger()
        parameter_size.setValue("16")
        parameter_element.setParameterSize(parameter_size)
        parameter_element.createSubElement("Sub1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterElement(parent, parameter_element)

        child = parent.find("DIAGNOSTIC-PARAMETER-ELEMENT")
        assert [c.tag for c in child] == ["SHORT-NAME", "BIT-OFFSET", "PARAMETER-SIZE", "SUB-ELEMENTS"]


class TestDiagnosticAbstractParameterRoundTrip:
    """Full set → save → reload → assert cycle through the document tree."""

    def test_round_trip_via_diagnostic_parameter(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        parameter = DiagnosticParameter()
        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        parameter.setBitOffset(bit_offset)
        parameter.createDataElement("De1")
        parameter_size = PositiveInteger()
        parameter_size.setValue("16")
        parameter.setParameterSize(parameter_size)
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
            assert parameter_2.getBitOffset() is not None
            assert parameter_2.getBitOffset().getValue() == 8
            assert parameter_2.getDataElement() is not None
            assert parameter_2.getDataElement().getShortName() == "De1"
            assert parameter_2.getParameterSize() is not None
            assert parameter_2.getParameterSize().getValue() == 16
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_via_diagnostic_parameter_element(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        parameter = DiagnosticParameter()
        ident = parameter.createIdent("Pid1")
        sub_element = ident.createSubElement("Sub1")
        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        sub_element.setBitOffset(bit_offset)
        parameter_size = PositiveInteger()
        parameter_size.setValue("16")
        sub_element.setParameterSize(parameter_size)
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
            sub_element_2 = parameter_2.getIdent().getSubElements()[0]
            assert isinstance(sub_element_2, DiagnosticParameterElement)
            assert sub_element_2.getBitOffset() is not None
            assert sub_element_2.getBitOffset().getValue() == 8
            assert sub_element_2.getParameterSize() is not None
            assert sub_element_2.getParameterSize().getValue() == 16
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
