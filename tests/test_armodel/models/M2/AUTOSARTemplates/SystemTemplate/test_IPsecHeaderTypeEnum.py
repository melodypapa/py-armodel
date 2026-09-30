from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecHeaderTypeEnum


class Test_IPsecHeaderTypeEnum:
    def test_members(self):
        # spec literals per Table 6.227, p.576 (ah idx0, esp idx1, none idx2)
        assert IPsecHeaderTypeEnum.AH == "ah"
        assert IPsecHeaderTypeEnum.ESP == "esp"
        assert IPsecHeaderTypeEnum.NONE == "none"

    def test_literal_order(self):
        # displayed markdown order: ah, esp, none
        e = IPsecHeaderTypeEnum()
        assert e.getEnumValues() == [
            IPsecHeaderTypeEnum.AH,
            IPsecHeaderTypeEnum.ESP,
            IPsecHeaderTypeEnum.NONE,
        ]

    def test_instantiation_and_set_value(self):
        e = IPsecHeaderTypeEnum()
        assert e.setValue(IPsecHeaderTypeEnum.ESP) is e
        assert e.getValue() == "esp"
        e.setValue(IPsecHeaderTypeEnum.AH)
        assert e.getValue() == "ah"

    def test_docstring_is_spec_note_verbatim(self):
        note = "IPsec Header Type options"
        assert IPsecHeaderTypeEnum.__doc__.strip() == note
