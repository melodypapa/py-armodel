from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import MirroringProtocolEnum


class Test_MirroringProtocolEnum:
    def test_members(self):
        # spec literals per Table 6.326, p.697 (none idx1, version1 idx0); values = XSD
        # MIRRORING-PROTOCOL-ENUM--SIMPLE facets (hyphenated VERSION-1 token)
        assert MirroringProtocolEnum.NONE == "NONE"
        assert MirroringProtocolEnum.VERSION1 == "VERSION-1"

    def test_literal_order(self):
        # XSD facet order (= markdown displayed order; EnumerationLiteralIndex 1/0 differs)
        e = MirroringProtocolEnum()
        assert e.getEnumValues() == [
            MirroringProtocolEnum.NONE,
            MirroringProtocolEnum.VERSION1,
        ]

    def test_instantiation_and_set_value(self):
        e = MirroringProtocolEnum()
        assert e.setValue(MirroringProtocolEnum.VERSION1) is e
        assert e.getValue() == MirroringProtocolEnum.VERSION1
        e.setValue(MirroringProtocolEnum.NONE)
        assert e.getValue() == MirroringProtocolEnum.NONE

    def test_docstring_is_spec_note_verbatim(self):
        note = "Eunumeration that defines the supported bus mirroring protocol options) with two literals."
        assert MirroringProtocolEnum.__doc__.strip() == note
