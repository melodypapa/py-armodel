"""Reader tests for SwTextProps (Swc TPS Table 5.7, p.250).

getSwTextProps populates the model via the four mutators. Element order per the
XSD group SW-TEXT-PROPS (AUTOSAR_00052.xsd): ARRAY-SIZE-SEMANTICS,
SW-MAX-TEXT-SIZE (sequenceOffset 20), BASE-TYPE-REF (30), SW-FILL-CHARACTER (40).
"""

from tests.test_armodel.parser._helpers import _snip


class TestSwTextPropsReader:
    def test_read_full_field_values(self, parser):
        element = _snip(
            """
            <SW-TEXT-PROPS>
                <ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>
                <SW-MAX-TEXT-SIZE>200</SW-MAX-TEXT-SIZE>
                <BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/BaseTypes/uint8</BASE-TYPE-REF>
                <SW-FILL-CHARACTER>48</SW-FILL-CHARACTER>
            </SW-TEXT-PROPS>
            """,
            root_tag="SW-DATA-DEF-PROPS-CONDITIONAL",
        )
        props = parser.getSwTextProps(element, "SW-TEXT-PROPS")
        assert props is not None
        assert props.getArraySizeSemantics().getValue() == "fixedSize"
        assert props.getSwMaxTextSize().getValue() == 200
        assert props.getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
        assert props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert props.getSwFillCharacter().getValue() == 48

    def test_read_empty_wrapper_yields_unset_fields(self, parser):
        element = _snip(
            "<SW-TEXT-PROPS/>",
            root_tag="SW-DATA-DEF-PROPS-CONDITIONAL",
        )
        props = parser.getSwTextProps(element, "SW-TEXT-PROPS")
        assert props is not None
        assert props.getArraySizeSemantics() is None
        assert props.getSwMaxTextSize() is None
        assert props.getBaseTypeRef() is None
        assert props.getSwFillCharacter() is None

    def test_read_absent_wrapper_returns_none(self, parser):
        element = _snip(
            "",
            root_tag="SW-DATA-DEF-PROPS-CONDITIONAL",
        )
        assert parser.getSwTextProps(element, "SW-TEXT-PROPS") is None
