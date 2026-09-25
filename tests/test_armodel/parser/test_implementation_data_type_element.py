"""
Tests for parsing IMPLEMENTATION-DATA-TYPE-ELEMENT elements — Table 5.17 (p.270, R23-11).

ImplementationDataTypeElement (Base = AbstractImplementationDataTypeElement) carries its own
elements ARRAY-IMPL-POLICY, ARRAY-SIZE, ARRAY-SIZE-HANDLING, ARRAY-SIZE-SEMANTICS,
IS-OPTIONAL (0..1 each), the SUB-ELEMENTS wrapper (recursive IMPLEMENTATION-DATA-TYPE-ELEMENT)
and SW-DATA-DEF-PROPS (read via readAutosarDataType). XSD element order (AUTOSAR_00052.xsd
group IMPLEMENTATION-DATA-TYPE-ELEMENT): ARRAY-IMPL-POLICY, ARRAY-SIZE, ARRAY-SIZE-HANDLING,
ARRAY-SIZE-SEMANTICS, IS-OPTIONAL, SUB-ELEMENTS, SW-DATA-DEF-PROPS, VARIATION-POINT.

Round-trip counterpart: tests/test_armodel/writer/test_implementation_data_type_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataTypeElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _impl_element():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return ImplementationDataTypeElement(pkg, "Elem")


class TestReadImplementationDataTypeElement:
    """
    Test readImplementationDataTypeElement — own element field values (Table 5.17).
    """

    def test_read_array_impl_policy_field_value(self, parser):
        """
        Test that the ARRAY-IMPL-POLICY value is populated into the arrayImplPolicy field.
        """
        impl_element = _impl_element()
        element = ET.fromstring(f"""<IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Elem</SHORT-NAME>
                <ARRAY-IMPL-POLICY>payloadAsPointerToArray</ARRAY-IMPL-POLICY>
            </IMPLEMENTATION-DATA-TYPE-ELEMENT>""")

        parser.readImplementationDataTypeElement(element, impl_element)

        assert impl_element.getArrayImplPolicy() is not None
        assert impl_element.getArrayImplPolicy().getValue() == "payloadAsPointerToArray"

    def test_read_is_optional_field_value(self, parser):
        """
        Test that the IS-OPTIONAL value is populated into the isOptional field.
        """
        impl_element = _impl_element()
        element = ET.fromstring(f"""<IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Elem</SHORT-NAME>
                <IS-OPTIONAL>true</IS-OPTIONAL>
            </IMPLEMENTATION-DATA-TYPE-ELEMENT>""")

        parser.readImplementationDataTypeElement(element, impl_element)

        assert impl_element.getIsOptional() is not None
        assert isinstance(impl_element.getIsOptional(), Boolean)
        assert impl_element.getIsOptional().getValue() is True

    def test_read_array_size_handling_semantics_field_values(self, parser):
        """
        Test that ARRAY-SIZE, ARRAY-SIZE-HANDLING and ARRAY-SIZE-SEMANTICS populate their fields.
        """
        impl_element = _impl_element()
        element = ET.fromstring(f"""<IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Elem</SHORT-NAME>
                <ARRAY-SIZE>8</ARRAY-SIZE>
                <ARRAY-SIZE-HANDLING>allIndicesSameArraySize</ARRAY-SIZE-HANDLING>
                <ARRAY-SIZE-SEMANTICS>fixedSize</ARRAY-SIZE-SEMANTICS>
            </IMPLEMENTATION-DATA-TYPE-ELEMENT>""")

        parser.readImplementationDataTypeElement(element, impl_element)

        assert isinstance(impl_element.getArraySize(), PositiveInteger)
        assert impl_element.getArraySize().getValue() == 8
        assert impl_element.getArraySizeHandling() is not None
        assert impl_element.getArraySizeHandling().getValue() == "allIndicesSameArraySize"
        assert impl_element.getArraySizeSemantics() is not None
        assert impl_element.getArraySizeSemantics().getValue() == "fixedSize"

    def test_read_nested_sub_element_field_values(self, parser):
        """
        Test that nested IMPLEMENTATION-DATA-TYPE-ELEMENT items are populated recursively.
        """
        impl_element = _impl_element()
        element = ET.fromstring(f"""<IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Elem</SHORT-NAME>
                <SUB-ELEMENTS>
                    <IMPLEMENTATION-DATA-TYPE-ELEMENT>
                        <SHORT-NAME>Sub</SHORT-NAME>
                        <ARRAY-IMPL-POLICY>payloadAsArray</ARRAY-IMPL-POLICY>
                    </IMPLEMENTATION-DATA-TYPE-ELEMENT>
                </SUB-ELEMENTS>
            </IMPLEMENTATION-DATA-TYPE-ELEMENT>""")

        parser.readImplementationDataTypeElement(element, impl_element)

        subs = impl_element.getSubElements()
        assert len(subs) == 1
        assert subs[0].getShortName() == "Sub"
        assert subs[0].getArrayImplPolicy() is not None
        assert subs[0].getArrayImplPolicy().getValue() == "payloadAsArray"

    def test_read_without_optional_elements_leaves_fields_none(self, parser):
        """
        Test that an element without own elements leaves all fields None (empty-wrapper analog).
        """
        impl_element = _impl_element()
        element = ET.fromstring(f"<IMPLEMENTATION-DATA-TYPE-ELEMENT xmlns='{NS}'><SHORT-NAME>Elem</SHORT-NAME></IMPLEMENTATION-DATA-TYPE-ELEMENT>")

        parser.readImplementationDataTypeElement(element, impl_element)

        assert impl_element.getArrayImplPolicy() is None
        assert impl_element.getArraySize() is None
        assert impl_element.getArraySizeHandling() is None
        assert impl_element.getArraySizeSemantics() is None
        assert impl_element.getIsOptional() is None
        assert impl_element.getSubElements() == []
        assert impl_element.getSwDataDefProps() is None
