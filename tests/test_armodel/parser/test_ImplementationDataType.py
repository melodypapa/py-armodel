"""Reader tests for ImplementationDataType (Swc TPS Table 5.15, p.268).

readImplementationDataType populates the model via the mutators. Child element
set per the XSD group IMPLEMENTATION-DATA-TYPE (AUTOSAR_00052.xsd):
DYNAMIC-ARRAY-SIZE-PROFILE, IS-STRUCT-WITH-OPTIONAL-ELEMENT, SUB-ELEMENTS,
SYMBOL-PROPS, TYPE-EMITTER.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestImplementationDataTypeReader:
    def test_read_field_values(self, parser):
        data_type = ImplementationDataType(_autosar_root(), "StructType")
        element = _snip(
            """
            <SHORT-NAME>StructType</SHORT-NAME>
            <DYNAMIC-ARRAY-SIZE-PROFILE>VARIABLE-LENGTH</DYNAMIC-ARRAY-SIZE-PROFILE>
            <IS-STRUCT-WITH-OPTIONAL-ELEMENT>true</IS-STRUCT-WITH-OPTIONAL-ELEMENT>
            <SUB-ELEMENTS>
                <IMPLEMENTATION-DATA-TYPE-ELEMENT>
                    <SHORT-NAME>Size</SHORT-NAME>
                    <ARRAY-SIZE>8</ARRAY-SIZE>
                    <ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>
                </IMPLEMENTATION-DATA-TYPE-ELEMENT>
                <IMPLEMENTATION-DATA-TYPE-ELEMENT>
                    <SHORT-NAME>Payload</SHORT-NAME>
                    <IS-OPTIONAL>true</IS-OPTIONAL>
                </IMPLEMENTATION-DATA-TYPE-ELEMENT>
            </SUB-ELEMENTS>
            <SYMBOL-PROPS>
                <SHORT-NAME>Sym</SHORT-NAME>
                <SYMBOL>REASON_SYM</SYMBOL>
            </SYMBOL-PROPS>
            <TYPE-EMITTER>RTE</TYPE-EMITTER>
            """,
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )

        parser.readImplementationDataType(element, data_type)

        assert data_type.getDynamicArraySizeProfile().getValue() == "VARIABLE-LENGTH"
        assert data_type.getIsStructWithOptionalElement().getValue() is True

        sub_elements = data_type.getSubElements()
        assert len(sub_elements) == 2
        assert sub_elements[0].short_name == "Size"
        assert sub_elements[0].parent is data_type
        assert sub_elements[0].getArraySize().getValue() == 8
        assert sub_elements[0].getArraySizeSemantics().getValue() == "fixedSize"
        assert sub_elements[1].short_name == "Payload"
        assert sub_elements[1].getIsOptional().getValue() is True

        symbol_props = data_type.getSymbolProps()
        assert symbol_props is not None
        assert symbol_props.short_name == "Sym"
        assert symbol_props.parent is data_type
        assert symbol_props.getSymbol().getValue() == "REASON_SYM"

        assert data_type.getTypeEmitter().getValue() == "RTE"

    def test_read_empty_wrapper_yields_unset_fields(self, parser):
        data_type = ImplementationDataType(_autosar_root(), "PlainType")
        element = _snip(
            "<SHORT-NAME>PlainType</SHORT-NAME>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )

        parser.readImplementationDataType(element, data_type)

        assert data_type.getDynamicArraySizeProfile() is None
        assert data_type.getIsStructWithOptionalElement() is None
        assert data_type.getSubElements() == []
        assert data_type.getSymbolProps() is None
        assert data_type.getTypeEmitter() is None
