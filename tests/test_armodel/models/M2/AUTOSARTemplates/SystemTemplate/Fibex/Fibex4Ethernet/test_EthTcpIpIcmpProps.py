"""Tests for the EthTcpIpIcmpProps class (R23-11 SystemTemplate Table 3.112)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthTcpIpIcmpProps,
    TcpIpIcmpv4Props,
    TcpIpIcmpv6Props,
)


class TestEthTcpIpIcmpProps:
    """
    Test class for EthTcpIpIcmpProps functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.112, p.156 (R23-11)
    """

    MEMBERS = [
        "icmpV4Props",
        "icmpV6Props",
    ]

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        assert issubclass(EthTcpIpIcmpProps, ARElement)

    def test_class_docstring_note(self):
        expected = "This meta-class is used to configure the EcuInstance specific ICMP (Internet Control Message Protocol) attributes" " Tags: atp.recommendedPackage=EthTcpIcmpProps"
        assert inspect.cleandoc(EthTcpIpIcmpProps.__doc__) == expected

    def test_initialization_defaults(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpIcmpPropsPkg")
        obj = EthTcpIpIcmpProps(pkg, "IcmpProps1")
        assert obj.getIcmpV4Props() is None
        assert obj.getIcmpV6Props() is None

    def test_member_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpIcmpPropsPkg")
        obj = EthTcpIpIcmpProps(pkg, "IcmpProps1")
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_icmp_v4_props(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpIcmpPropsPkg")
        obj = EthTcpIpIcmpProps(pkg, "IcmpProps1")
        v4 = TcpIpIcmpv4Props()
        result = obj.setIcmpV4Props(v4)
        assert result is obj
        assert obj.getIcmpV4Props() is v4
        obj.setIcmpV4Props(None)
        assert obj.getIcmpV4Props() is v4

    def test_get_set_icmp_v6_props(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpIcmpPropsPkg")
        obj = EthTcpIpIcmpProps(pkg, "IcmpProps1")
        v6 = TcpIpIcmpv6Props()
        result = obj.setIcmpV6Props(v6)
        assert result is obj
        assert obj.getIcmpV6Props() is v6
        obj.setIcmpV6Props(None)
        assert obj.getIcmpV6Props() is v6

    def test_arpackage_factory(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpIcmpPropsPkg2")
        props = pkg.createEthTcpIpIcmpProps("IcmpProps1")
        assert isinstance(props, EthTcpIpIcmpProps)
        again = pkg.createEthTcpIpIcmpProps("IcmpProps1")
        assert again is props
