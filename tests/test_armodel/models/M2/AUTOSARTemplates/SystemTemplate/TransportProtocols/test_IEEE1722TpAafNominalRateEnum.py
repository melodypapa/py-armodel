import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafNominalRateEnum,
)


class TestIEEE1722TpAafNominalRateEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.281, p.644 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAafNominalRateEnum.__doc__) == "Definition of the AAF nominal sample / frame rate. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.281; values = exact XSD enumeration facets (IEEE-1722-TP-AAF-NOMINAL-RATE-ENUM--SIMPLE)
        assert IEEE1722TpAafNominalRateEnum.ENUM_16KHZ == "16-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_176_4KHZ == "176-4-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_192KHZ == "192-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_24KHZ == "24-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_32KHZ == "32-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_44_1KHZ == "44-1-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_48KHZ == "48-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_88_2KHZ == "88-2-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_8KHZ == "8-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_96KHZ == "96-KHZ"
        assert IEEE1722TpAafNominalRateEnum.ENUM_USER == "USER"

    def test_member_count_matches_spec(self):
        # 11 Literal rows in Table 6.281 (10 rates + user)
        members = [name for name in dir(IEEE1722TpAafNominalRateEnum) if name.startswith("ENUM_")]
        assert len(members) == 11

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpAafNominalRateEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpAafNominalRateEnum.ENUM_44_1KHZ)
        assert enum.getValue() == IEEE1722TpAafNominalRateEnum.ENUM_44_1KHZ

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-AAF-NOMINAL-RATE-ENUM--SIMPLE)
        enum = IEEE1722TpAafNominalRateEnum()
        assert list(enum.getEnumValues()) == [
            "16-KHZ",
            "176-4-KHZ",
            "192-KHZ",
            "24-KHZ",
            "32-KHZ",
            "44-1-KHZ",
            "48-KHZ",
            "8-KHZ",
            "88-2-KHZ",
            "96-KHZ",
            "USER",
        ]
        assert typing.get_type_hints(IEEE1722TpAafNominalRateEnum.__init__) is not None
