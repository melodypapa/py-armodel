"""
Tests for writing DIAGNOSTIC-DATA-ELEMENT elements — DiagnosticDataElement, Table 4.9 (p.41, R23-11).

DiagnosticDataElement (Base = Identifiable, VP-capable per Rule 0020) owns the
ARRAY-SIZE-SEMANTICS / MAX-NUMBER-OF-ELEMENTS / SCALING-INFO-SIZE /
SW-DATA-DEF-PROPS / VARIATION-POINT group (XSD group DIAGNOSTIC-DATA-ELEMENT,
AUTOSAR_00052.xsd l.34124 — VARIATION-POINT last, sequenceOffset=10000). The
writer reads the model via the get accessors; DIAGNOSTIC-DATA-ELEMENT items are
emitted through the DiagnosticAbstractParameter DATA-ELEMENTS dispatch, which
replaces the former identity-only SHORT-NAME write.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_element.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
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


def _make_data_element(short_name: str) -> DiagnosticDataElement:
    data_element = DiagnosticDataElement(AUTOSAR.getInstance(), short_name)
    data_element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
    max_number_of_elements = PositiveInteger()
    max_number_of_elements.setValue("4")
    data_element.setMaxNumberOfElements(max_number_of_elements)
    scaling_info_size = PositiveInteger()
    scaling_info_size.setValue("8")
    data_element.setScalingInfoSize(scaling_info_size)
    sw_data_def_props = SwDataDefProps()
    base_type_ref = RefType()
    base_type_ref.setValue("/Base/uint8")
    base_type_ref.setDest("SW-BASE-TYPE-REF")
    sw_data_def_props.setBaseTypeRef(base_type_ref)
    data_element.setSwDataDefProps(sw_data_def_props)
    data_element.setVariationPoint(VariationPoint())
    return data_element


class TestWriteDiagnosticDataElement:
    """Tests for writeDiagnosticDataElement — own element field values (Table 4.9)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that all attributes are emitted in XSD group order with VARIATION-POINT last."""
        data_element = _make_data_element("De1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataElement(parent, data_element)

        child = parent.find("DIAGNOSTIC-DATA-ELEMENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "De1"
        assert child.find("ARRAY-SIZE-SEMANTICS").text == "FIXED-SIZE"
        assert child.find("MAX-NUMBER-OF-ELEMENTS").text == "4"
        assert child.find("SCALING-INFO-SIZE").text == "8"
        assert child.find("SW-DATA-DEF-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF").text == "/Base/uint8"
        assert child.find("VARIATION-POINT") is not None
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "ARRAY-SIZE-SEMANTICS", "MAX-NUMBER-OF-ELEMENTS", "SCALING-INFO-SIZE", "SW-DATA-DEF-PROPS", "VARIATION-POINT"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset attributes and the variation point emit no elements."""
        data_element = DiagnosticDataElement(AUTOSAR.getInstance(), "De1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataElement(parent, data_element)

        child = parent.find("DIAGNOSTIC-DATA-ELEMENT")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_data_elements_dispatch_writes_diagnostic_data_element(self):
        """Test that writeDiagnosticAbstractParameter emits DATA-ELEMENTS with full child content."""
        parameter = DiagnosticParameter()
        parameter.createDataElement("De1").setMaxNumberOfElements(PositiveInteger().setValue("4"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAbstractParameter(parent, parameter)

        data_elements = parent.find("DATA-ELEMENTS")
        assert data_elements is not None
        items = list(data_elements)
        assert [item.tag for item in items] == ["DIAGNOSTIC-DATA-ELEMENT"]
        assert items[0].find("SHORT-NAME").text == "De1"
        assert items[0].find("MAX-NUMBER-OF-ELEMENTS").text == "4"


class TestDiagnosticDataElementRoundTrip:
    """Full set → save → reload → assert cycle through the document tree."""

    def test_round_trip(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Dids")
        did = package.createDiagnosticDataIdentifier("Di")
        parameter = DiagnosticParameter()
        parameter.createDataElement("De1")
        data_element = parameter.getDataElement()
        data_element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue("fixedSize"))
        max_number_of_elements = PositiveInteger()
        max_number_of_elements.setValue("4")
        data_element.setMaxNumberOfElements(max_number_of_elements)
        scaling_info_size = PositiveInteger()
        scaling_info_size.setValue("8")
        data_element.setScalingInfoSize(scaling_info_size)
        sw_data_def_props = SwDataDefProps()
        base_type_ref = RefType()
        base_type_ref.setValue("/Base/uint8")
        base_type_ref.setDest("SW-BASE-TYPE")
        sw_data_def_props.setBaseTypeRef(base_type_ref)
        data_element.setSwDataDefProps(sw_data_def_props)
        data_element.setVariationPoint(VariationPoint())
        did.addDataElement(parameter)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            did_2 = package_2.getReferrableElement("Di", DiagnosticDataIdentifier)
            assert did_2 is not None
            parameter_2 = did_2.getDataElements()[0]
            data_element_2 = parameter_2.getDataElement()
            assert isinstance(data_element_2, DiagnosticDataElement)
            assert data_element_2.getShortName() == "De1"
            assert data_element_2.getArraySizeSemantics() is not None
            assert data_element_2.getMaxNumberOfElements() is not None
            assert data_element_2.getMaxNumberOfElements().getValue() == 4
            assert data_element_2.getScalingInfoSize() is not None
            assert data_element_2.getScalingInfoSize().getValue() == 8
            assert data_element_2.getSwDataDefProps() is not None
            assert data_element_2.getSwDataDefProps().getBaseTypeRef().getValue() == "/Base/uint8"
            assert data_element_2.getVariationPoint() is not None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
