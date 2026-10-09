import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCanMessageTypeEnum,
)


class TestIEEE1722TpAcfCanMessageTypeEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.295, p.662 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfCanMessageTypeEnum.__doc__) == "Definition of the ACF CAN stream message type. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.295; values = exact XSD enumeration facets (IEEE-1722-TP-ACF-CAN-MESSAGE-TYPE-ENUM--SIMPLE)
        assert IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN == "CAN"
        assert IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN_BRIEF == "CAN-BRIEF"

    def test_member_count_matches_spec(self):
        # 2 Literal rows in Table 6.295
        members = [name for name in dir(IEEE1722TpAcfCanMessageTypeEnum) if name.startswith("ENUM_")]
        assert len(members) == 2

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpAcfCanMessageTypeEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN_BRIEF)
        assert enum.getValue() == IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN_BRIEF

    def test_xsd_facet_order(self):
        # __init__ passes the values in XSD facet order (restriction order of IEEE-1722-TP-ACF-CAN-MESSAGE-TYPE-ENUM--SIMPLE)
        enum = IEEE1722TpAcfCanMessageTypeEnum()
        assert list(enum.getEnumValues()) == ["CAN", "CAN-BRIEF"]
        assert typing.get_type_hints(IEEE1722TpAcfCanMessageTypeEnum.__init__) is not None
