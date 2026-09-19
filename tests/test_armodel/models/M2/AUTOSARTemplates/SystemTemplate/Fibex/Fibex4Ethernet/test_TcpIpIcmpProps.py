"""Tests for the TcpIpIcmpv4Props class (R23-11 SystemTemplate Table 3.113)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TcpIpIcmpv4Props


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
