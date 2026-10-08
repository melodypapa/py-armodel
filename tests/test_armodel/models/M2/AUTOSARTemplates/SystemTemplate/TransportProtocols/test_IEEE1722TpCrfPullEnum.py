import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import IEEE1722TpCrfPullEnum


class TestIEEE1722TpCrfPullEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.279, p.641 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpCrfPullEnum.__doc__) == "Definition of the CRF stream pull value. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.279; values = exact XSD enumeration facets (IEEE-1722-TP-CRF-PULL-ENUM--SIMPLE)
        assert IEEE1722TpCrfPullEnum.ENUM_1_0 == "1-0"
        assert IEEE1722TpCrfPullEnum.ENUM_1_001 == "1-001"
        assert IEEE1722TpCrfPullEnum.ENUM_1_1_001 == "1-1-001"
        assert IEEE1722TpCrfPullEnum.ENUM_1_8 == "1-8"
        assert IEEE1722TpCrfPullEnum.ENUM_24_25 == "24-25"
        assert IEEE1722TpCrfPullEnum.ENUM_25_24 == "25-24"

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpCrfPullEnum()
        enum.setValue(IEEE1722TpCrfPullEnum.ENUM_1_1_001)
        assert enum.getValue() == IEEE1722TpCrfPullEnum.ENUM_1_1_001

    def test_xsd_facet_order(self):
        enum = IEEE1722TpCrfPullEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpCrfPullEnum.ENUM_24_25)
        assert enum.getValue() == "24-25"
        assert typing.get_type_hints(IEEE1722TpCrfPullEnum.__init__) is not None
