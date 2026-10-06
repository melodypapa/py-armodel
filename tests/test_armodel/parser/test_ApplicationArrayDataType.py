"""Reader tests for ApplicationArrayDataType (Swc TPS Table 5.8, p.252).

readApplicationArrayDataType populates the model via the mutators. Element order
per the XSD group APPLICATION-ARRAY-DATA-TYPE (AUTOSAR_00052.xsd):
DYNAMIC-ARRAY-SIZE-PROFILE, then ELEMENT.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestApplicationArrayDataTypeReader:
    def test_read_field_values(self, parser):
        data_type = ApplicationArrayDataType(_autosar_root(), "ArrayType")
        element = _snip(
            """
            <SHORT-NAME>ArrayType</SHORT-NAME>
            <DYNAMIC-ARRAY-SIZE-PROFILE>VARIABLE-LENGTH</DYNAMIC-ARRAY-SIZE-PROFILE>
            <ELEMENT>
                <SHORT-NAME>Elem</SHORT-NAME>
                <TYPE-TREF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/DataTypes/uint8</TYPE-TREF>
                <ARRAY-SIZE-HANDLING>ALL-INDICES-DIFFERENT-ARRAY-SIZE</ARRAY-SIZE-HANDLING>
                <MAX-NUMBER-OF-ELEMENTS>4</MAX-NUMBER-OF-ELEMENTS>
            </ELEMENT>
            """,
            root_tag="APPLICATION-ARRAY-DATA-TYPE",
        )

        parser.readApplicationArrayDataType(element, data_type)

        assert data_type.getDynamicArraySizeProfile().getValue() == "VARIABLE-LENGTH"

        array_element = data_type.getApplicationArrayElement()
        assert array_element is not None
        assert array_element.short_name == "Elem"
        assert array_element.parent is data_type
        assert array_element.getTypeTRef().getValue() == "/DataTypes/uint8"
        assert array_element.getTypeTRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
        assert array_element.getMaxNumberOfElements().getValue() == 4

    def test_read_empty_wrapper_yields_unset_fields(self, parser):
        data_type = ApplicationArrayDataType(_autosar_root(), "ArrayType")
        element = _snip(
            "<SHORT-NAME>ArrayType</SHORT-NAME>",
            root_tag="APPLICATION-ARRAY-DATA-TYPE",
        )

        parser.readApplicationArrayDataType(element, data_type)

        assert data_type.getDynamicArraySizeProfile() is None
        assert data_type.getApplicationArrayElement() is None
