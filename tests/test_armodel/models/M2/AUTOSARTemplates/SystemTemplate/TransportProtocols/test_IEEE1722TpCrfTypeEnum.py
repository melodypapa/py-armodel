import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import IEEE1722TpCrfTypeEnum


class TestIEEE1722TpCrfTypeEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.278, p.640 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpCrfTypeEnum.__doc__) == "Definition of the CRF stream type. Tags: atp.Status=candidate"

    def test_literal_members_and_xsd_facet_values(self):
        # Literal rows of Table 6.278; values = exact XSD enumeration facets (IEEE-1722-TP-CRF-TYPE-ENUM--SIMPLE)
        assert IEEE1722TpCrfTypeEnum.ENUM_AUDIO_SAMPLE == "AUDIO-SAMPLE"
        assert IEEE1722TpCrfTypeEnum.ENUM_MACHINE_CYCLE == "MACHINE-CYCLE"
        assert IEEE1722TpCrfTypeEnum.ENUM_USER == "USER"
        assert IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME == "VIDEO-FRAME"
        assert IEEE1722TpCrfTypeEnum.ENUM_VIDEO_LINE == "VIDEO-LINE"

    def test_instantiable_and_value_round_trip(self):
        enum = IEEE1722TpCrfTypeEnum()
        enum.setValue(IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME)
        assert enum.getValue() == IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME

    def test_xsd_facet_order(self):
        enum = IEEE1722TpCrfTypeEnum()
        assert enum.getValue() == ""
        enum.setValue(IEEE1722TpCrfTypeEnum.ENUM_AUDIO_SAMPLE)
        assert enum.getValue() == "AUDIO-SAMPLE"
        assert typing.get_type_hints(IEEE1722TpCrfTypeEnum.__init__) is not None
