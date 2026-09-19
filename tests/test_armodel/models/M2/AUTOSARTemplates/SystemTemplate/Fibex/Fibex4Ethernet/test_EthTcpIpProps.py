"""Tests for the TcpProps class (R23-11 SystemTemplate Table 3.111)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthTcpIpProps, TcpProps, UdpProps


class TestTcpProps:
    """
    Test class for TcpProps functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.111, p.155 (R23-11)
    """

    MEMBERS = [
        "tcpCongestionAvoidanceEnabled",
        "tcpDelayedAckTimeout",
        "tcpFastRecoveryEnabled",
        "tcpFastRetransmitEnabled",
        "tcpFinWait2Timeout",
        "tcpKeepAliveEnabled",
        "tcpKeepAliveInterval",
        "tcpKeepAliveProbesMax",
        "tcpKeepAliveTime",
        "tcpMaxRtx",
        "tcpMsl",
        "tcpNagleEnabled",
        "tcpReceiveWindowMax",
        "tcpRetransmissionTimeout",
        "tcpSlowStartEnabled",
        "tcpSynMaxRtx",
        "tcpSynReceivedTimeout",
        "tcpTtl",
    ]

    def test_inheritance(self):
        assert issubclass(TcpProps, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class specifies the configuration options for TCP (Transmission Control Protocol)."
            "\n\n"
            "[constr_5119] Value range of TcpProps.tcpTtl: If defined, the value of TcpProps.tcpTtl shall be in the range of 1..255."
            "\n\n"
            "[constr_5120] Value range of TcpProps.tcpDelayedAckTimeout: If defined, the value of TcpProps.tcpDelayedAckTimeout shall be in the range of 0..0.5."
            "\n\n"
            "[constr_5121] Value range of TcpProps.tcpSynMaxRtx: If defined, the value of TcpProps.tcpSynMaxRtx shall be in the range of 0..255."
        )
        assert inspect.cleandoc(TcpProps.__doc__) == expected

    def test_initialization_defaults(self):
        obj = TcpProps()
        for member in self.MEMBERS:
            assert getattr(obj, member) is None

    def test_member_order(self):
        obj = TcpProps()
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_tcp_ttl(self):
        obj = TcpProps()
        value = PositiveInteger().setValue(64)
        result = obj.setTcpTtl(value)
        assert result is obj
        assert obj.getTcpTtl() == value
        obj.setTcpTtl(None)
        assert obj.getTcpTtl() == value

    def test_get_set_tcp_delayed_ack_timeout(self):
        obj = TcpProps()
        value = TimeValue().setValue(0.1)
        result = obj.setTcpDelayedAckTimeout(value)
        assert result is obj
        assert obj.getTcpDelayedAckTimeout() == value
        obj.setTcpDelayedAckTimeout(None)
        assert obj.getTcpDelayedAckTimeout() == value

    def test_get_set_tcp_nagle_enabled(self):
        obj = TcpProps()
        value = Boolean().setValue(True)
        result = obj.setTcpNagleEnabled(value)
        assert result is obj
        assert obj.getTcpNagleEnabled() == value
        obj.setTcpNagleEnabled(None)
        assert obj.getTcpNagleEnabled() == value


class TestUdpProps:
    """
    Test class for UdpProps functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.110, p.154 (R23-11)
    """

    def test_inheritance(self):
        assert issubclass(UdpProps, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class specifies the configuration options for UDP (User Datagram Protocol)."
            "\n\n"
            "[constr_5118] Value range of UdpProps.udpTtl: If defined, the value of UdpProps.udpTtl shall be in the range of 1..255."
        )
        assert inspect.cleandoc(UdpProps.__doc__) == expected

    def test_initialization_defaults(self):
        obj = UdpProps()
        assert obj.udpTtl is None

    def test_get_set_udp_ttl(self):
        obj = UdpProps()
        value = PositiveInteger().setValue(64)
        result = obj.setUdpTtl(value)
        assert result is obj
        assert obj.getUdpTtl() == value
        obj.setUdpTtl(None)
        assert obj.getUdpTtl() == value


class TestEthTcpIpProps:
    """
    Test class for EthTcpIpProps functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.109, p.153 (R23-11)
    """

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        assert issubclass(EthTcpIpProps, ARElement)

    def test_class_docstring_note(self):
        expected = "This meta-class is used to configure the EcuInstance specific TcpIp Stack attributes." " Tags: atp.recommendedPackage=EthTcpIpProps"
        assert inspect.cleandoc(EthTcpIpProps.__doc__) == expected

    def test_initialization_defaults(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpPropsPkg")
        obj = EthTcpIpProps(pkg, "TcpIpProps1")
        assert obj.getTcpProps() is None
        assert obj.getUdpProps() is None

    def test_get_set_tcp_props(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpPropsPkg")
        obj = EthTcpIpProps(pkg, "TcpIpProps1")
        tcp = TcpProps()
        result = obj.setTcpProps(tcp)
        assert result is obj
        assert obj.getTcpProps() is tcp
        obj.setTcpProps(None)
        assert obj.getTcpProps() is tcp

    def test_get_set_udp_props(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpPropsPkg")
        obj = EthTcpIpProps(pkg, "TcpIpProps1")
        udp = UdpProps()
        obj.setUdpProps(udp)
        assert obj.getUdpProps() is udp

    def test_arpackage_factory(self):
        pkg = AUTOSAR.getInstance().createARPackage("EthTcpIpPropsPkg2")
        props = pkg.createEthTcpIpProps("Props1")
        assert isinstance(props, EthTcpIpProps)
        again = pkg.createEthTcpIpProps("Props1")
        assert again is props
