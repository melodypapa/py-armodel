import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfColorSpaceEnum,
)


class TestIEEE1722TpRvfColorSpaceEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.288, p.652 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpRvfColorSpaceEnum.__doc__) == "Definition of the RVF stream colorspace. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.288; values = exact XSD enumeration facets (IEEE-1722-TP-RVF-COLOR-SPACE-ENUM--SIMPLE)
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_BT_REC_601 == "BT-REC-601"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_BT_REC_709 == "BT-REC-709"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_GRAYSCALE == "GRAYSCALE"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_ITU_BT_2020 == "ITU-BT-2020"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_SRGB == "SRGB"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_USER == "USER"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_XYZ == "XYZ"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_YCBCR == "YCBCR"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_YCGCO == "YCGCO"
        assert IEEE1722TpRvfColorSpaceEnum.ENUM_YCM == "YCM"

    def test_member_count_matches_spec(self):
        # 10 Literal rows in Table 6.288
        members = [name for name in dir(IEEE1722TpRvfColorSpaceEnum) if name.startswith("ENUM_")]
        assert len(members) == 10

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpRvfColorSpaceEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpRvfColorSpaceEnum.ENUM_YCBCR)
        assert enum.getValue() == IEEE1722TpRvfColorSpaceEnum.ENUM_YCBCR

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-RVF-COLOR-SPACE-ENUM--SIMPLE)
        enum = IEEE1722TpRvfColorSpaceEnum()
        assert list(enum.getEnumValues()) == [
            "BT-REC-601",
            "BT-REC-709",
            "GRAYSCALE",
            "ITU-BT-2020",
            "SRGB",
            "USER",
            "XYZ",
            "YCBCR",
            "YCGCO",
            "YCM",
        ]
        assert typing.get_type_hints(IEEE1722TpRvfColorSpaceEnum.__init__) is not None
