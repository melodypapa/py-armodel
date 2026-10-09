import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfPixelFormatEnum,
)


class TestIEEE1722TpRvfPixelFormatEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.287, p.651 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpRvfPixelFormatEnum.__doc__) == "Definition of the RVF Pixel Format. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.287; values = exact XSD enumeration facets (IEEE-1722-TP-RVF-PIXEL-FORMAT-ENUM--SIMPLE)
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_1_1 == "4-1-1"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_0 == "4-2-0"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_2 == "4-2-2"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_2_4 == "4-2-2-4"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_4_4 == "4-4-4"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_4_4_4_4 == "4-4-4-4"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_BAYER_BGGR == "BAYER-BGGR"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_BAYER_GBRG == "BAYER-GBRG"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_BAYER_GRBG == "BAYER-GRBG"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_BAYER_RGGB == "BAYER-RGGB"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_MONOCHROME == "MONOCHROME"
        assert IEEE1722TpRvfPixelFormatEnum.ENUM_USER == "USER"

    def test_member_count_matches_spec(self):
        # 12 Literal rows in Table 6.287 (6 numeric + 4 bayer + monochrome + user)
        members = [name for name in dir(IEEE1722TpRvfPixelFormatEnum) if name.startswith("ENUM_")]
        assert len(members) == 12

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpRvfPixelFormatEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_2)
        assert enum.getValue() == IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_2

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-RVF-PIXEL-FORMAT-ENUM--SIMPLE)
        enum = IEEE1722TpRvfPixelFormatEnum()
        assert list(enum.getEnumValues()) == [
            "4-1-1",
            "4-2-0",
            "4-2-2",
            "4-2-2-4",
            "4-4-4",
            "4-4-4-4",
            "BAYER-BGGR",
            "BAYER-GBRG",
            "BAYER-GRBG",
            "BAYER-RGGB",
            "MONOCHROME",
            "USER",
        ]
        assert typing.get_type_hints(IEEE1722TpRvfPixelFormatEnum.__init__) is not None
