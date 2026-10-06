from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecPolicyEnum


class Test_IPsecPolicyEnum:
    def test_members(self):
        # spec literals per Table 6.225, p.574 (ipsec idx1, passthrough idx2, drop idx3, reject idx4)
        assert IPsecPolicyEnum.DROP == "DROP"
        assert IPsecPolicyEnum.IPSEC == "IPSEC"
        assert IPsecPolicyEnum.PASSTHROUGH == "PASSTHROUGH"
        assert IPsecPolicyEnum.REJECT == "REJECT"

    def test_literal_order(self):
        # displayed markdown order: drop, ipsec, passthrough, reject
        e = IPsecPolicyEnum()
        assert e.getEnumValues() == [
            IPsecPolicyEnum.DROP,
            IPsecPolicyEnum.IPSEC,
            IPsecPolicyEnum.PASSTHROUGH,
            IPsecPolicyEnum.REJECT,
        ]

    def test_instantiation_and_set_value(self):
        e = IPsecPolicyEnum()
        assert e.setValue(IPsecPolicyEnum.IPSEC) is e
        assert e.getValue() == IPsecPolicyEnum.IPSEC
        e.setValue(IPsecPolicyEnum.REJECT)
        assert e.getValue() == IPsecPolicyEnum.REJECT

    def test_docstring_is_spec_note_verbatim(self):
        note = "Defines the filter actions that are supported by IPsec."
        assert IPsecPolicyEnum.__doc__.strip() == note
