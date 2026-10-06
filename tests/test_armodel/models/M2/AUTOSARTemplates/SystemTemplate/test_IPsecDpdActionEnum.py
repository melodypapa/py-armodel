from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecDpdActionEnum


class Test_IPsecDpdActionEnum:
    def test_members(self):
        # spec literals per Table 6.228, p.577 (clear idx0, trap idx1, restart idx2)
        assert IPsecDpdActionEnum.CLEAR == "CLEAR"
        assert IPsecDpdActionEnum.RESTART == "RESTART"
        assert IPsecDpdActionEnum.TRAP == "TRAP"

    def test_literal_order(self):
        # displayed markdown order: clear, restart, trap
        e = IPsecDpdActionEnum()
        assert e.getEnumValues() == [
            IPsecDpdActionEnum.CLEAR,
            IPsecDpdActionEnum.RESTART,
            IPsecDpdActionEnum.TRAP,
        ]

    def test_instantiation_and_set_value(self):
        e = IPsecDpdActionEnum()
        assert e.setValue(IPsecDpdActionEnum.RESTART) is e
        assert e.getValue() == IPsecDpdActionEnum.RESTART
        e.setValue(IPsecDpdActionEnum.TRAP)
        assert e.getValue() == IPsecDpdActionEnum.TRAP

    def test_docstring_is_spec_note_verbatim(self):
        note = "Potential Dead Peer Detection (Dpd) Actions"
        assert IPsecDpdActionEnum.__doc__.strip() == note
