"""
Tests for writing IMPLEMENTATION-DATA-TYPE-ELEMENT elements — Table 5.17 (p.270, R23-11).

ImplementationDataTypeElement (Base = AbstractImplementationDataTypeElement) carries its own
elements ARRAY-IMPL-POLICY, ARRAY-SIZE, ARRAY-SIZE-HANDLING, ARRAY-SIZE-SEMANTICS,
IS-OPTIONAL (0..1 each), the SUB-ELEMENTS wrapper (recursive IMPLEMENTATION-DATA-TYPE-ELEMENT)
and SW-DATA-DEF-PROPS. Writer element order must follow the XSD sequenceOffset
(AUTOSAR_00052.xsd group IMPLEMENTATION-DATA-TYPE-ELEMENT).

Round-trip counterpart: tests/test_armodel/parser/test_implementation_data_type_element.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
    ImplementationDataType,
    ImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ArraySizeHandlingEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _build_element(with_fields=True):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    element = ImplementationDataTypeElement(pkg, "Elem")
    if with_fields:
        element.setArrayImplPolicy(ArrayImplPolicyEnum().setValue(ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY))
        element.setArraySize(PositiveInteger().setValue("4"))
        element.setArraySizeHandling(ArraySizeHandlingEnum().setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE))
        element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
        element.setIsOptional(Boolean().setValue(True))
        element.setSwDataDefProps(SwDataDefProps())
        element.createImplementationDataTypeElement("Sub")
    return element


def _save_and_reload():
    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        ARXMLWriter().save(tmp_path, AUTOSAR.getInstance())
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        ARXMLParser().load(tmp_path, AUTOSAR.getInstance())
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


class TestWriteImplementationDataTypeElement:
    """
    Test writeImplementationDataTypeElement — own element field values (Table 5.17).
    """

    def test_write_array_impl_policy_and_is_optional_field_values(self, writer):
        """
        Test that ARRAY-IMPL-POLICY and IS-OPTIONAL are emitted with the field values.
        """
        element = _build_element()
        element.setArraySize(None)
        element.setArraySizeHandling(None)
        element.setArraySizeSemantics(None)
        element.setSwDataDefProps(None)
        element.subElements.clear()
        parent = ET.Element("ELEMENTS")

        writer.writeImplementationDataTypeElement(parent, element)

        child = parent.find("IMPLEMENTATION-DATA-TYPE-ELEMENT")
        assert child is not None
        policy = child.find("ARRAY-IMPL-POLICY")
        assert policy is not None
        assert policy.text == "payloadAsPointerToArray"
        optional = child.find("IS-OPTIONAL")
        assert optional is not None
        assert optional.text == "true"

    def test_write_element_order_matches_xsd(self, writer):
        """
        Test that the emitted own elements follow the XSD group order.
        """
        element = _build_element()
        parent = ET.Element("ELEMENTS")

        writer.writeImplementationDataTypeElement(parent, element)

        child = parent.find("IMPLEMENTATION-DATA-TYPE-ELEMENT")
        tags = [c.tag for c in child]
        expected = ["ARRAY-IMPL-POLICY", "ARRAY-SIZE", "ARRAY-SIZE-HANDLING", "ARRAY-SIZE-SEMANTICS", "IS-OPTIONAL", "SUB-ELEMENTS", "SW-DATA-DEF-PROPS"]
        indexes = [tags.index(tag) for tag in expected]
        assert indexes == sorted(indexes)
        assert child.find("ARRAY-SIZE").text == "4"

    def test_write_unset_fields_emit_no_optional_elements(self, writer):
        """
        Test that unset fields emit no own elements (empty-wrapper analog for SUB-ELEMENTS).
        """
        element = _build_element(with_fields=False)
        parent = ET.Element("ELEMENTS")

        writer.writeImplementationDataTypeElement(parent, element)

        child = parent.find("IMPLEMENTATION-DATA-TYPE-ELEMENT")
        assert child is not None
        assert child.find("ARRAY-IMPL-POLICY") is None
        assert child.find("ARRAY-SIZE") is None
        assert child.find("ARRAY-SIZE-HANDLING") is None
        assert child.find("ARRAY-SIZE-SEMANTICS") is None
        assert child.find("IS-OPTIONAL") is None
        assert child.find("SUB-ELEMENTS") is None
        assert child.find("SW-DATA-DEF-PROPS") is None

    def test_full_document_round_trip_field_values(self):
        """
        Test save → reload asserts the ImplementationDataTypeElement field values end-to-end.
        """
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        element = data_type.createImplementationDataTypeElement("Elem")
        element.setArrayImplPolicy(ArrayImplPolicyEnum().setValue(ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY))
        element.setArraySize(PositiveInteger().setValue("4"))
        element.setArraySizeHandling(ArraySizeHandlingEnum().setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE))
        element.setArraySizeSemantics(ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE))
        element.setIsOptional(Boolean().setValue(True))
        sub_element = element.createImplementationDataTypeElement("Sub")
        sub_element.setArrayImplPolicy(ArrayImplPolicyEnum().setValue(ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY))

        _save_and_reload()

        pkg = AUTOSAR.getInstance().getARPackages()[0]
        data_type = pkg.getElement("ImplType", ImplementationDataType)
        assert data_type is not None
        element = data_type.getSubElements()[0]
        assert element.getArrayImplPolicy() is not None
        assert element.getArrayImplPolicy().getValue() == "payloadAsPointerToArray"
        assert element.getArraySize() is not None
        assert element.getArraySize().getValue() == 4
        assert element.getArraySizeHandling() is not None
        assert element.getArraySizeHandling().getValue() == "allIndicesSameArraySize"
        assert element.getArraySizeSemantics() is not None
        assert element.getArraySizeSemantics().getValue() == "fixedSize"
        assert element.getIsOptional() is not None
        assert element.getIsOptional().getValue() is True
        sub_element = element.getSubElements()[0]
        assert sub_element.getShortName() == "Sub"
        assert sub_element.getArrayImplPolicy() is not None
        assert sub_element.getArrayImplPolicy().getValue() == "payloadAsArray"
