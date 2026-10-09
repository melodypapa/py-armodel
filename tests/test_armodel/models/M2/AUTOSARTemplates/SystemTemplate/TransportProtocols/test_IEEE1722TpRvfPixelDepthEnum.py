import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfPixelDepthEnum,
)


class TestIEEE1722TpRvfPixelDepthEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.286, p.650 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpRvfPixelDepthEnum.__doc__) == "Definition of the RVF Pixel Depth. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.286; values = exact XSD enumeration facets (IEEE-1722-TP-RVF-PIXEL-DEPTH-ENUM--SIMPLE)
        assert IEEE1722TpRvfPixelDepthEnum.ENUM_10 == "10"
        assert IEEE1722TpRvfPixelDepthEnum.ENUM_12 == "12"
        assert IEEE1722TpRvfPixelDepthEnum.ENUM_16 == "16"
        assert IEEE1722TpRvfPixelDepthEnum.ENUM_8 == "8"
        assert IEEE1722TpRvfPixelDepthEnum.ENUM_USER == "USER"

    def test_member_count_matches_spec(self):
        # 5 Literal rows in Table 6.286
        members = [name for name in dir(IEEE1722TpRvfPixelDepthEnum) if name.startswith("ENUM_")]
        assert len(members) == 5

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpRvfPixelDepthEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpRvfPixelDepthEnum.ENUM_10)
        assert enum.getValue() == IEEE1722TpRvfPixelDepthEnum.ENUM_10

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-RVF-PIXEL-DEPTH-ENUM--SIMPLE)
        enum = IEEE1722TpRvfPixelDepthEnum()
        assert list(enum.getEnumValues()) == ["10", "12", "16", "8", "USER"]
        assert typing.get_type_hints(IEEE1722TpRvfPixelDepthEnum.__init__) is not None
