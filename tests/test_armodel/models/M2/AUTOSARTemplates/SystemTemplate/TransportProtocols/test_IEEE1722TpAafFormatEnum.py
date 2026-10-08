import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafFormatEnum,
)


class TestIEEE1722TpAafFormatEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.282, p.644 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAafFormatEnum.__doc__) == "Definition of the AAF stream format. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.282; values = exact XSD enumeration facets (IEEE-1722-TP-AAF-FORMAT-ENUM--SIMPLE)
        assert IEEE1722TpAafFormatEnum.AES3_32BIT == "AES-3-32-BIT"
        assert IEEE1722TpAafFormatEnum.FLOAT_32BIT == "FLOAT-32-BIT"
        assert IEEE1722TpAafFormatEnum.INT_16BIT == "INT-16-BIT"
        assert IEEE1722TpAafFormatEnum.INT_24BIT == "INT-24-BIT"
        assert IEEE1722TpAafFormatEnum.INT_32BIT == "INT-32-BIT"
        assert IEEE1722TpAafFormatEnum.USER == "USER"

    def test_member_count_matches_spec(self):
        # 6 Literal rows in Table 6.282
        members = [name for name in dir(IEEE1722TpAafFormatEnum) if name.isupper() and not name.startswith("_")]
        assert len(members) == 6

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpAafFormatEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpAafFormatEnum.AES3_32BIT)
        assert enum.getValue() == IEEE1722TpAafFormatEnum.AES3_32BIT

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-AAF-FORMAT-ENUM--SIMPLE)
        enum = IEEE1722TpAafFormatEnum()
        assert list(enum.getEnumValues()) == [
            "AES-3-32-BIT",
            "FLOAT-32-BIT",
            "INT-16-BIT",
            "INT-24-BIT",
            "INT-32-BIT",
            "USER",
        ]
        assert typing.get_type_hints(IEEE1722TpAafFormatEnum.__init__) is not None
