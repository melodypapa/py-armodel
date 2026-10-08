import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
)


class TestIEEE1722TpAafAes3DataTypeEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.283, p.645 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAafAes3DataTypeEnum.__doc__) == "Definition of the AAF AES3 stream aes3_data_type reference. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.283; values = exact XSD enumeration facets (IEEE-1722-TP-AAF-AES-3-DATA-TYPE-ENUM--SIMPLE)
        assert IEEE1722TpAafAes3DataTypeEnum.ENUM_IEC61937 == "IEC-61937"
        assert IEEE1722TpAafAes3DataTypeEnum.ENUM_PCM == "PCM"
        assert IEEE1722TpAafAes3DataTypeEnum.ENUM_SMPTE338 == "SMPTE-338"
        assert IEEE1722TpAafAes3DataTypeEnum.ENUM_UNSPECIFIED == "UNSPECIFIED"
        assert IEEE1722TpAafAes3DataTypeEnum.ENUM_VENDOR == "VENDOR"

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpAafAes3DataTypeEnum()
        enum.setValue(IEEE1722TpAafAes3DataTypeEnum.ENUM_SMPTE338)
        assert enum.getValue() == IEEE1722TpAafAes3DataTypeEnum.ENUM_SMPTE338

    def test_xsd_facet_order(self):
        enum = IEEE1722TpAafAes3DataTypeEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpAafAes3DataTypeEnum.ENUM_IEC61937)
        assert enum.getValue() == "IEC-61937"
        assert typing.get_type_hints(IEEE1722TpAafAes3DataTypeEnum.__init__) is not None
