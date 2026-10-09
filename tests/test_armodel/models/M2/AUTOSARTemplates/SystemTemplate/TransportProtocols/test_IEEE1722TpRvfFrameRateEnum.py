import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfFrameRateEnum,
)


class TestIEEE1722TpRvfFrameRateEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.289, p.654 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpRvfFrameRateEnum.__doc__) == "Definition of the RVF stream frame_rate. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.289; values = exact XSD enumeration facets (IEEE-1722-TP-RVF-FRAME-RATE-ENUM--SIMPLE)
        assert IEEE1722TpRvfFrameRateEnum.ENUM_1 == "1"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_10 == "10"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_100 == "100"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_120 == "120"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_15 == "15"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_150 == "150"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_2 == "2"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_20 == "20"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_200 == "200"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_24 == "24"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_240 == "240"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_25 == "25"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_30 == "30"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_300 == "300"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_48 == "48"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_5 == "5"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_50 == "50"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_60 == "60"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_72 == "72"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_85 == "85"
        assert IEEE1722TpRvfFrameRateEnum.ENUM_USER == "USER"

    def test_member_count_matches_spec(self):
        # 21 Literal rows in Table 6.289 (20 frame rates + user)
        members = [name for name in dir(IEEE1722TpRvfFrameRateEnum) if name.startswith("ENUM_")]
        assert len(members) == 21

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpRvfFrameRateEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpRvfFrameRateEnum.ENUM_25)
        assert enum.getValue() == IEEE1722TpRvfFrameRateEnum.ENUM_25

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-RVF-FRAME-RATE-ENUM--SIMPLE)
        enum = IEEE1722TpRvfFrameRateEnum()
        assert list(enum.getEnumValues()) == [
            "1",
            "10",
            "100",
            "120",
            "15",
            "150",
            "2",
            "20",
            "200",
            "24",
            "240",
            "25",
            "30",
            "300",
            "48",
            "5",
            "50",
            "60",
            "72",
            "85",
            "USER",
        ]
        assert typing.get_type_hints(IEEE1722TpRvfFrameRateEnum.__init__) is not None
