"""
Tests for reading DIAGNOSTIC-PARAMETER-ELEMENT elements — DiagnosticParameterElement, Table 4.6 (p.36, R23-11).

DiagnosticParameterElement (Base = DiagnosticAbstractParameter + Identifiable)
carries the ARRAY-SIZE attribute and the recursive SUB-ELEMENTS aggregation
(XSD group DIAGNOSTIC-PARAMETER-ELEMENT, AUTOSAR_00052.xsd l.40629). The reader
populates the model via the setArraySize/createSubElement mutators; the helper is
called directly until the DiagnosticParameterIdent SUB-ELEMENTS dispatch lands
with the Table 4.7 sync.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_parameter_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DIAGNOSTIC-PARAMETER-ELEMENT xmlns='{NS}'>{inner}</DIAGNOSTIC-PARAMETER-ELEMENT>")


class TestReadDiagnosticParameterElement:
    """Tests for readDiagnosticParameterElement — own element field values (Table 4.6)."""

    def _read(self, parser, inner):
        parent = AUTOSAR.getInstance()
        parameter_element = DiagnosticParameterElement(parent, "Elem1")
        parser.readDiagnosticParameterElement(_snip(inner), parameter_element)
        return parameter_element

    def test_read_sets_all_fields(self, parser):
        """Test that ARRAY-SIZE and nested SUB-ELEMENTS are read with their field values."""
        parameter_element = self._read(
            parser,
            "<SHORT-NAME>Elem1</SHORT-NAME>"
            "<ARRAY-SIZE>8</ARRAY-SIZE>"
            "<SUB-ELEMENTS>"
            "<DIAGNOSTIC-PARAMETER-ELEMENT><SHORT-NAME>Sub1</SHORT-NAME><ARRAY-SIZE>16</ARRAY-SIZE></DIAGNOSTIC-PARAMETER-ELEMENT>"
            "</SUB-ELEMENTS>",
        )
        assert parameter_element.getArraySize() is not None
        assert parameter_element.getArraySize().getValue() == 8
        assert len(parameter_element.getSubElements()) == 1
        sub_element = parameter_element.getSubElements()[0]
        assert sub_element.getShortName() == "Sub1"
        assert sub_element.getArraySize() is not None
        assert sub_element.getArraySize().getValue() == 16

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields at their defaults."""
        parameter_element = self._read(parser, "<SHORT-NAME>Elem1</SHORT-NAME>")
        assert parameter_element.getArraySize() is None
        assert parameter_element.getSubElements() == []

    def test_read_nested_two_levels(self, parser):
        """Test that the SUB-ELEMENTS recursion descends two levels."""
        parameter_element = self._read(
            parser,
            "<SHORT-NAME>Elem1</SHORT-NAME>"
            "<SUB-ELEMENTS>"
            "<DIAGNOSTIC-PARAMETER-ELEMENT><SHORT-NAME>Sub1</SHORT-NAME>"
            "<SUB-ELEMENTS><DIAGNOSTIC-PARAMETER-ELEMENT><SHORT-NAME>Leaf</SHORT-NAME></DIAGNOSTIC-PARAMETER-ELEMENT></SUB-ELEMENTS>"
            "</DIAGNOSTIC-PARAMETER-ELEMENT>"
            "</SUB-ELEMENTS>",
        )
        leaf = parameter_element.getSubElements()[0].getSubElements()[0]
        assert leaf.getShortName() == "Leaf"


def test_write_read_round_trip_via_element(parser):
    """Test the write → serialize → parse → read cycle over the element tree (no document dispatch yet)."""
    parent = AUTOSAR.getInstance()
    parameter_element = DiagnosticParameterElement(parent, "Elem1")
    array_size = PositiveInteger()
    array_size.setValue("8")
    parameter_element.setArraySize(array_size)
    sub_element = parameter_element.createSubElement("Sub1")
    sub_array_size = PositiveInteger()
    sub_array_size.setValue("16")
    sub_element.setArraySize(sub_array_size)

    parent_element = ET.Element("PARENT")
    ARXMLWriter().writeDiagnosticParameterElement(parent_element, parameter_element)
    serialized = ET.tostring(parent_element, encoding="unicode")

    reparsed = DiagnosticParameterElement(AUTOSAR.getInstance(), "Elem1")
    wrapped = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, serialized))
    ARXMLParser().readDiagnosticParameterElement(wrapped[0][0], reparsed)

    assert reparsed.getArraySize() is not None
    assert reparsed.getArraySize().getValue() == 8
    assert len(reparsed.getSubElements()) == 1
    assert reparsed.getSubElements()[0].getShortName() == "Sub1"
    assert reparsed.getSubElements()[0].getArraySize() is not None
    assert reparsed.getSubElements()[0].getArraySize().getValue() == 16
