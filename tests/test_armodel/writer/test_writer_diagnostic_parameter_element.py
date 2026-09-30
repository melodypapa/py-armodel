"""
Tests for writing DIAGNOSTIC-PARAMETER-ELEMENT elements — DiagnosticParameterElement, Table 4.6 (p.36, R23-11).

DiagnosticParameterElement (Base = DiagnosticAbstractParameter + Identifiable)
carries the ARRAY-SIZE attribute and the recursive SUB-ELEMENTS aggregation
(XSD group DIAGNOSTIC-PARAMETER-ELEMENT, AUTOSAR_00052.xsd l.40629 — ARRAY-SIZE
before SUB-ELEMENTS). The writer reads the model via the
getArraySize/getSubElements getters; the document-level dispatch through
DiagnosticParameterIdent SUB-ELEMENTS lands with the Table 4.7 sync.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_parameter_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticParameterElement:
    """Tests for writeDiagnosticParameterElement — own element field values (Table 4.6)."""

    def _make_element(self) -> DiagnosticParameterElement:
        return DiagnosticParameterElement(AUTOSAR.getInstance(), "Elem1")

    def test_write_field_values_in_xsd_order(self):
        """Test that ARRAY-SIZE and SUB-ELEMENTS are emitted in XSD order with their values."""
        parameter_element = self._make_element()
        array_size = PositiveInteger()
        array_size.setValue("8")
        parameter_element.setArraySize(array_size)
        parameter_element.createSubElement("Sub1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterElement(parent, parameter_element)

        child = parent.find("DIAGNOSTIC-PARAMETER-ELEMENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Elem1"
        assert child.find("ARRAY-SIZE").text == "8"
        sub_elements = child.find("SUB-ELEMENTS")
        assert sub_elements is not None
        items = list(sub_elements)
        assert [item.tag for item in items] == ["DIAGNOSTIC-PARAMETER-ELEMENT"]
        assert items[0].find("SHORT-NAME").text == "Sub1"
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "ARRAY-SIZE", "SUB-ELEMENTS"]

    def test_write_unset_fields_omits_tags(self):
        """Test that an empty aggregation emits no wrapper and unset attribute emits no element."""
        parameter_element = self._make_element()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterElement(parent, parameter_element)

        child = parent.find("DIAGNOSTIC-PARAMETER-ELEMENT")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("SUB-ELEMENTS") is None

    def test_write_nested_two_levels(self):
        """Test that nested sub elements are emitted recursively."""
        parameter_element = self._make_element()
        parameter_element.createSubElement("Sub1").createSubElement("Leaf")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticParameterElement(parent, parameter_element)

        child = parent.find("DIAGNOSTIC-PARAMETER-ELEMENT")
        sub1 = child.find("SUB-ELEMENTS/DIAGNOSTIC-PARAMETER-ELEMENT")
        assert sub1 is not None
        assert sub1.find("SHORT-NAME").text == "Sub1"
        leaf = sub1.find("SUB-ELEMENTS/DIAGNOSTIC-PARAMETER-ELEMENT")
        assert leaf is not None
        assert leaf.find("SHORT-NAME").text == "Leaf"
