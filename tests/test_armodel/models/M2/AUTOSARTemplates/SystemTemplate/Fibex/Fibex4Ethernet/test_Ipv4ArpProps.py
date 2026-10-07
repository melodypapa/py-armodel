"""
Test suite for Ipv4ArpProps (CP_TPS_SystemTemplate Table 3.102, p.146, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv4ArpProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps

CLASS_NOTE = "Specifies the configuration options for the ARP (Address Resolution Protocol)."

MEMBER_ORDER = [
    "tcpIpArpNumGratuitousArpOnStartup",
    "tcpIpArpPacketQueueEnabled",
    "tcpIpArpRequestTimeout",
    "tcpIpArpTableEntryTimeout",
]

NUM_GRATUITOUS_ARP_ON_STARTUP_NOTE = "This attribute specifies the number of gratuitous ARP replies which shall be sent on assignment of a new IP address."
PACKET_QUEUE_ENABLED_NOTE = "This attribute enables (TRUE) or disables (FALSE) support of the ARP Packet Queue according to IETF RFC 1122, section 2.3.2.2."
REQUEST_TIMEOUT_NOTE = (
    "This attribute specifies a timeout in seconds for the validity of ARP requests. "
    "After the transmission of an ARP request the TcpIp shall skip the transmission of any further ARP requests "
    "to the same destination within a duration of tcpIpArpRequestTimeout seconds. (IETF RFC 1122, section 2.3.2.1)."
)
TABLE_ENTRY_TIMEOUT_NOTE = "This attribute specifies the timeout in seconds after which an unused ARP entry is removed."


class TestIpv4ArpProps:
    def test_inheritance(self):
        assert issubclass(Ipv4ArpProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4ArpProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv4ArpProps()

        assert obj.getTcpIpArpNumGratuitousArpOnStartup() is None
        assert obj.getTcpIpArpPacketQueueEnabled() is None
        assert obj.getTcpIpArpRequestTimeout() is None
        assert obj.getTcpIpArpTableEntryTimeout() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv4ArpProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["tcpIpArpNumGratuitousArpOnStartup"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpArpPacketQueueEnabled"] == "Optional[Boolean]"
        assert annotations["tcpIpArpRequestTimeout"] == "Optional[TimeValue]"
        assert annotations["tcpIpArpTableEntryTimeout"] == "Optional[TimeValue]"

        assert typing.get_type_hints(Ipv4ArpProps.getTcpIpArpNumGratuitousArpOnStartup).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv4ArpProps.setTcpIpArpNumGratuitousArpOnStartup).get("return") is Ipv4ArpProps
        assert typing.get_type_hints(Ipv4ArpProps.getTcpIpArpPacketQueueEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv4ArpProps.setTcpIpArpPacketQueueEnabled).get("return") is Ipv4ArpProps
        assert typing.get_type_hints(Ipv4ArpProps.getTcpIpArpRequestTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv4ArpProps.setTcpIpArpRequestTimeout).get("return") is Ipv4ArpProps
        assert typing.get_type_hints(Ipv4ArpProps.getTcpIpArpTableEntryTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv4ArpProps.setTcpIpArpTableEntryTimeout).get("return") is Ipv4ArpProps

    def test_member_order(self):
        obj = Ipv4ArpProps()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_arp_num_gratuitous_arp_on_startup(self):
        obj = Ipv4ArpProps()
        value = PositiveInteger().setValue(3)

        result = obj.setTcpIpArpNumGratuitousArpOnStartup(value)
        assert result is obj
        assert obj.getTcpIpArpNumGratuitousArpOnStartup() is value

        obj.setTcpIpArpNumGratuitousArpOnStartup(None)
        assert obj.getTcpIpArpNumGratuitousArpOnStartup() is value

    def test_get_set_tcp_ip_arp_packet_queue_enabled(self):
        obj = Ipv4ArpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpArpPacketQueueEnabled(value)
        assert result is obj
        assert obj.getTcpIpArpPacketQueueEnabled() is value

        obj.setTcpIpArpPacketQueueEnabled(None)
        assert obj.getTcpIpArpPacketQueueEnabled() is value

    def test_get_set_tcp_ip_arp_request_timeout(self):
        obj = Ipv4ArpProps()
        value = TimeValue().setValue(1.5)

        result = obj.setTcpIpArpRequestTimeout(value)
        assert result is obj
        assert obj.getTcpIpArpRequestTimeout() is value

        obj.setTcpIpArpRequestTimeout(None)
        assert obj.getTcpIpArpRequestTimeout() is value

    def test_get_set_tcp_ip_arp_table_entry_timeout(self):
        obj = Ipv4ArpProps()
        value = TimeValue().setValue(2.0)

        result = obj.setTcpIpArpTableEntryTimeout(value)
        assert result is obj
        assert obj.getTcpIpArpTableEntryTimeout() is value

        obj.setTcpIpArpTableEntryTimeout(None)
        assert obj.getTcpIpArpTableEntryTimeout() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv4ArpProps.getTcpIpArpNumGratuitousArpOnStartup.__doc__) == NUM_GRATUITOUS_ARP_ON_STARTUP_NOTE
        assert inspect.cleandoc(Ipv4ArpProps.setTcpIpArpNumGratuitousArpOnStartup.__doc__) == (
            NUM_GRATUITOUS_ARP_ON_STARTUP_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpArpNumGratuitousArpOnStartup."
        )
        assert inspect.cleandoc(Ipv4ArpProps.getTcpIpArpPacketQueueEnabled.__doc__) == PACKET_QUEUE_ENABLED_NOTE
        assert inspect.cleandoc(Ipv4ArpProps.setTcpIpArpPacketQueueEnabled.__doc__) == (
            PACKET_QUEUE_ENABLED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpArpPacketQueueEnabled."
        )
        assert inspect.cleandoc(Ipv4ArpProps.getTcpIpArpRequestTimeout.__doc__) == REQUEST_TIMEOUT_NOTE
        assert inspect.cleandoc(Ipv4ArpProps.setTcpIpArpRequestTimeout.__doc__) == (REQUEST_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpArpRequestTimeout.")
        assert inspect.cleandoc(Ipv4ArpProps.getTcpIpArpTableEntryTimeout.__doc__) == TABLE_ENTRY_TIMEOUT_NOTE
        assert inspect.cleandoc(Ipv4ArpProps.setTcpIpArpTableEntryTimeout.__doc__) == (
            TABLE_ENTRY_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpArpTableEntryTimeout."
        )
