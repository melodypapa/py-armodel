from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecModeEnum


class Test_IPsecModeEnum:
    def test_members(self):
        # spec literals per Table 6.226, p.575 (tunnel idx0, transport idx1)
        assert IPsecModeEnum.TRANSPORT == "transport"
        assert IPsecModeEnum.TUNNEL == "tunnel"

    def test_literal_order(self):
        # displayed markdown order: transport, tunnel
        e = IPsecModeEnum()
        assert e.getEnumValues() == [
            IPsecModeEnum.TRANSPORT,
            IPsecModeEnum.TUNNEL,
        ]

    def test_instantiation_and_set_value(self):
        e = IPsecModeEnum()
        assert e.setValue(IPsecModeEnum.TRANSPORT) is e
        assert e.getValue() == "transport"
        e.setValue(IPsecModeEnum.TUNNEL)
        assert e.getValue() == "tunnel"

    def test_docstring_is_spec_note_verbatim(self):
        note = "This enumeration describes the supported IPSec modes."
        assert IPsecModeEnum.__doc__.strip() == note
