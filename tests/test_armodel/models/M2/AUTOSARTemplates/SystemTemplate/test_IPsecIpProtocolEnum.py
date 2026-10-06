from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPsecIpProtocolEnum


class Test_IPsecIpProtocolEnum:
    def test_members(self):
        # spec literals per Table 6.224, p.574 (udp idx0, tcp idx1, icmp idx2, any idx3)
        assert IPsecIpProtocolEnum.ANY == "ANY"
        assert IPsecIpProtocolEnum.ICMP == "ICMP"
        assert IPsecIpProtocolEnum.TCP == "TCP"
        assert IPsecIpProtocolEnum.UDP == "UDP"

    def test_literal_order(self):
        # displayed markdown order: any, icmp, tcp, udp
        e = IPsecIpProtocolEnum()
        assert e.getEnumValues() == [
            IPsecIpProtocolEnum.ANY,
            IPsecIpProtocolEnum.ICMP,
            IPsecIpProtocolEnum.TCP,
            IPsecIpProtocolEnum.UDP,
        ]

    def test_instantiation_and_set_value(self):
        e = IPsecIpProtocolEnum()
        assert e.setValue(IPsecIpProtocolEnum.UDP) is e
        assert e.getValue() == IPsecIpProtocolEnum.UDP
        e.setValue(IPsecIpProtocolEnum.ANY)
        assert e.getValue() == "ANY"

    def test_docstring_is_spec_note_verbatim(self):
        note = "Definition of supported TcpIp protocols that are supported in Security Policy Database (SPD) entries in IPSec configurations."
        assert IPsecIpProtocolEnum.__doc__.strip() == note
