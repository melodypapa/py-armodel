"""Reader tests for ApplicationArrayElement (Swc TPS Table 5.9, p.252).

readApplicationArrayElement populates the model via the mutators. Element order
per the XSD group APPLICATION-ARRAY-ELEMENT (AUTOSAR_00052.xsd, L2846):
ARRAY-SIZE-HANDLING, ARRAY-SIZE-SEMANTICS, INDEX-DATA-TYPE-REF,
MAX-NUMBER-OF-ELEMENTS.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestApplicationArrayElementReader:
    def test_read_field_values(self, parser):
        data_type = ApplicationArrayDataType(_autosar_root(), "ArrayType")
        element = _snip(
            """
            <ELEMENT>
                <SHORT-NAME>Elem</SHORT-NAME>
                <TYPE-TREF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/DataTypes/uint8</TYPE-TREF>
                <ARRAY-SIZE-HANDLING>ALL-INDICES-SAME-ARRAY-SIZE</ARRAY-SIZE-HANDLING>
                <ARRAY-SIZE-SEMANTICS>VARIABLE-SIZE</ARRAY-SIZE-SEMANTICS>
                <INDEX-DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/DataTypes/IndexType</INDEX-DATA-TYPE-REF>
                <MAX-NUMBER-OF-ELEMENTS>4</MAX-NUMBER-OF-ELEMENTS>
            </ELEMENT>
            """,
            root_tag="APPLICATION-ARRAY-DATA-TYPE",
        )

        parser.readApplicationArrayElement(element, data_type)

        array_element = data_type.getApplicationArrayElement()
        assert array_element is not None
        assert array_element.short_name == "Elem"
        assert array_element.parent is data_type
        assert array_element.getTypeTRef().getValue() == "/DataTypes/uint8"
        assert array_element.getTypeTRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert array_element.getArraySizeHandling().getValue() == "ALL-INDICES-SAME-ARRAY-SIZE"
        assert array_element.getArraySizeSemantics().getValue() == "VARIABLE-SIZE"
        assert array_element.getIndexDataTypeRef().getValue() == "/DataTypes/IndexType"
        assert array_element.getIndexDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert isinstance(array_element.getMaxNumberOfElements(), PositiveInteger)
        assert array_element.getMaxNumberOfElements().getValue() == 4

    def test_read_empty_wrapper_yields_unset_fields(self, parser):
        data_type = ApplicationArrayDataType(_autosar_root(), "ArrayType")
        element = _snip(
            """
            <ELEMENT>
                <SHORT-NAME>Elem</SHORT-NAME>
            </ELEMENT>
            """,
            root_tag="APPLICATION-ARRAY-DATA-TYPE",
        )

        parser.readApplicationArrayElement(element, data_type)

        array_element = data_type.getApplicationArrayElement()
        assert array_element is not None
        assert array_element.short_name == "Elem"
        assert array_element.getTypeTRef() is None
        assert array_element.getArraySizeHandling() is None
        assert array_element.getArraySizeSemantics() is None
        assert array_element.getIndexDataTypeRef() is None
        assert array_element.getMaxNumberOfElements() is None

    def test_read_without_element_wrapper(self, parser):
        data_type = ApplicationArrayDataType(_autosar_root(), "ArrayType")
        element = _snip(
            "<SHORT-NAME>ArrayType</SHORT-NAME>",
            root_tag="APPLICATION-ARRAY-DATA-TYPE",
        )

        parser.readApplicationArrayElement(element, data_type)

        assert data_type.getApplicationArrayElement() is None
