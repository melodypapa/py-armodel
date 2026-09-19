"""Tests for the TcpIpIcmpv4Props / TcpIpIcmpv6Props classes (R23-11 SystemTemplate Tables 3.113/3.114)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TcpIpIcmpv4Props, TcpIpIcmpv6Props


class TestTcpIpIcmpv4Props:
    """
    Test class for TcpIpIcmpv4Props functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.113, p.156 (R23-11)
    """

    MEMBERS = [
        "tcpIpIcmpV4EchoReplyEnabled",
        "tcpIpIcmpV4Ttl",
    ]

    def test_inheritance(self):
        assert issubclass(TcpIpIcmpv4Props, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class specifies the configuration options for ICMPv4 (Internet Control Message Protocol)."
            "\n\n"
            "[constr_5125] Value range of TcpIpIcmpv4Props.tcpIpIcmpV4Ttl: If defined, the value of TcpIpIcmpv4Props.tcpIpIcmpV4Ttl shall be in the range of 1..255."
        )
        assert inspect.cleandoc(TcpIpIcmpv4Props.__doc__) == expected

    def test_initialization_defaults(self):
        obj = TcpIpIcmpv4Props()
        for member in self.MEMBERS:
            assert getattr(obj, member) is None

    def test_member_order(self):
        obj = TcpIpIcmpv4Props()
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_tcp_ip_icmpv4_echo_reply_enabled(self):
        obj = TcpIpIcmpv4Props()
        value = Boolean().setValue(True)
        result = obj.setTcpIpIcmpV4EchoReplyEnabled(value)
        assert result is obj
        assert obj.getTcpIpIcmpV4EchoReplyEnabled() == value
        obj.setTcpIpIcmpV4EchoReplyEnabled(None)
        assert obj.getTcpIpIcmpV4EchoReplyEnabled() == value

    def test_get_set_tcp_ip_icmpv4_ttl(self):
        obj = TcpIpIcmpv4Props()
        value = PositiveInteger().setValue(64)
        result = obj.setTcpIpIcmpV4Ttl(value)
        assert result is obj
        assert obj.getTcpIpIcmpV4Ttl() == value
        obj.setTcpIpIcmpV4Ttl(None)
        assert obj.getTcpIpIcmpV4Ttl() == value


class TestTcpIpIcmpv6Props:
    """
    Test class for TcpIpIcmpv6Props functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.114, p.157 (R23-11)
    """

    MEMBERS = [
        "tcpIpIcmpV6EchoReplyAvoidFragmentation",
        "tcpIpIcmpV6EchoReplyEnabled",
        "tcpIpIcmpV6HopLimit",
        "tcpIpIcmpV6MsgDestinationUnreachableEnabled",
        "tcpIpIcmpV6MsgParameterProblemEnabled",
    ]

    def test_inheritance(self):
        assert issubclass(TcpIpIcmpv6Props, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class specifies the configuration options for ICMPv6 (Internet Control Message Protocol)."
            "\n\n"
            "[constr_5154] Value range of TcpIpIcmpv6Props.tcpIpIcmpV6HopLimit: If defined, the value of TcpIpIcmpv6Props.tcpIpIcmpV6HopLimit shall be in the range of 1..255."
        )
        assert inspect.cleandoc(TcpIpIcmpv6Props.__doc__) == expected

    def test_initialization_defaults(self):
        obj = TcpIpIcmpv6Props()
        for member in self.MEMBERS:
            assert getattr(obj, member) is None

    def test_member_order(self):
        obj = TcpIpIcmpv6Props()
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_tcp_ip_icmpv6_echo_reply_avoid_fragmentation(self):
        obj = TcpIpIcmpv6Props()
        value = Boolean().setValue(True)
        result = obj.setTcpIpIcmpV6EchoReplyAvoidFragmentation(value)
        assert result is obj
        assert obj.getTcpIpIcmpV6EchoReplyAvoidFragmentation() == value
        obj.setTcpIpIcmpV6EchoReplyAvoidFragmentation(None)
        assert obj.getTcpIpIcmpV6EchoReplyAvoidFragmentation() == value

    def test_get_set_tcp_ip_icmpv6_echo_reply_enabled(self):
        obj = TcpIpIcmpv6Props()
        value = Boolean().setValue(False)
        result = obj.setTcpIpIcmpV6EchoReplyEnabled(value)
        assert result is obj
        assert obj.getTcpIpIcmpV6EchoReplyEnabled() == value
        obj.setTcpIpIcmpV6EchoReplyEnabled(None)
        assert obj.getTcpIpIcmpV6EchoReplyEnabled() == value

    def test_get_set_tcp_ip_icmpv6_hop_limit(self):
        obj = TcpIpIcmpv6Props()
        value = PositiveInteger().setValue(64)
        result = obj.setTcpIpIcmpV6HopLimit(value)
        assert result is obj
        assert obj.getTcpIpIcmpV6HopLimit() == value
        obj.setTcpIpIcmpV6HopLimit(None)
        assert obj.getTcpIpIcmpV6HopLimit() == value

    def test_get_set_tcp_ip_icmpv6_msg_destination_unreachable_enabled(self):
        obj = TcpIpIcmpv6Props()
        value = Boolean().setValue(True)
        result = obj.setTcpIpIcmpV6MsgDestinationUnreachableEnabled(value)
        assert result is obj
        assert obj.getTcpIpIcmpV6MsgDestinationUnreachableEnabled() == value
        obj.setTcpIpIcmpV6MsgDestinationUnreachableEnabled(None)
        assert obj.getTcpIpIcmpV6MsgDestinationUnreachableEnabled() == value

    def test_get_set_tcp_ip_icmpv6_msg_parameter_problem_enabled(self):
        obj = TcpIpIcmpv6Props()
        value = Boolean().setValue(True)
        result = obj.setTcpIpIcmpV6MsgParameterProblemEnabled(value)
        assert result is obj
        assert obj.getTcpIpIcmpV6MsgParameterProblemEnabled() == value
        obj.setTcpIpIcmpV6MsgParameterProblemEnabled(None)
        assert obj.getTcpIpIcmpV6MsgParameterProblemEnabled() == value
