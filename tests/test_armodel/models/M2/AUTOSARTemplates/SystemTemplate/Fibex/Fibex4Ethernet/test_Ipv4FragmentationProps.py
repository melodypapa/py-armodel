"""
Test suite for Ipv4FragmentationProps (CP_TPS_SystemTemplate Table 3.104, p.147, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv4FragmentationProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4FragmentationProps

CLASS_NOTE = "Specifies the configuration options for IPv4 packet fragmentation/reassembly."

MEMBER_ORDER = [
    "tcpIpIpFragmentationRxEnabled",
    "tcpIpIpNumFragments",
    "tcpIpIpNumReassDgrams",
    "tcpIpIpReassTimeout",
]

FRAGMENTATION_RX_ENABLED_NOTE = (
    "Enables (TRUE) or disables (FALSE) support for reassembling of incoming datagrams that are " "fragmented according to IETF RFC 815 (IP Datagram Reassembly Algorithms)."
)
NUM_FRAGMENTS_NOTE = "Specifies the maximum number of IP fragments per datagram."
NUM_REASS_DGRAMS_NOTE = "Specifies the maximum number of fragmented IP datagrams that can be reassembled in parallel."
REASS_TIMEOUT_NOTE = "Specifies the timeout in [s] after which an incomplete datagram gets discarded."


class TestIpv4FragmentationProps:
    def test_inheritance(self):
        assert issubclass(Ipv4FragmentationProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4FragmentationProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv4FragmentationProps()

        assert obj.getTcpIpIpFragmentationRxEnabled() is None
        assert obj.getTcpIpIpNumFragments() is None
        assert obj.getTcpIpIpNumReassDgrams() is None
        assert obj.getTcpIpIpReassTimeout() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv4FragmentationProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["tcpIpIpFragmentationRxEnabled"] == "Optional[Boolean]"
        assert annotations["tcpIpIpNumFragments"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpNumReassDgrams"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpReassTimeout"] == "Optional[TimeValue]"

        assert typing.get_type_hints(Ipv4FragmentationProps.getTcpIpIpFragmentationRxEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv4FragmentationProps.setTcpIpIpFragmentationRxEnabled).get("return") is Ipv4FragmentationProps
        assert typing.get_type_hints(Ipv4FragmentationProps.getTcpIpIpNumFragments).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv4FragmentationProps.setTcpIpIpNumFragments).get("return") is Ipv4FragmentationProps
        assert typing.get_type_hints(Ipv4FragmentationProps.getTcpIpIpNumReassDgrams).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv4FragmentationProps.setTcpIpIpNumReassDgrams).get("return") is Ipv4FragmentationProps
        assert typing.get_type_hints(Ipv4FragmentationProps.getTcpIpIpReassTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv4FragmentationProps.setTcpIpIpReassTimeout).get("return") is Ipv4FragmentationProps

    def test_member_order(self):
        obj = Ipv4FragmentationProps()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_ip_fragmentation_rx_enabled(self):
        obj = Ipv4FragmentationProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpIpFragmentationRxEnabled(value)
        assert result is obj
        assert obj.getTcpIpIpFragmentationRxEnabled() is value

        obj.setTcpIpIpFragmentationRxEnabled(None)
        assert obj.getTcpIpIpFragmentationRxEnabled() is value

    def test_get_set_tcp_ip_ip_num_fragments(self):
        obj = Ipv4FragmentationProps()
        value = PositiveInteger().setValue(8)

        result = obj.setTcpIpIpNumFragments(value)
        assert result is obj
        assert obj.getTcpIpIpNumFragments() is value

        obj.setTcpIpIpNumFragments(None)
        assert obj.getTcpIpIpNumFragments() is value

    def test_get_set_tcp_ip_ip_num_reass_dgrams(self):
        obj = Ipv4FragmentationProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpIpNumReassDgrams(value)
        assert result is obj
        assert obj.getTcpIpIpNumReassDgrams() is value

        obj.setTcpIpIpNumReassDgrams(None)
        assert obj.getTcpIpIpNumReassDgrams() is value

    def test_get_set_tcp_ip_ip_reass_timeout(self):
        obj = Ipv4FragmentationProps()
        value = TimeValue().setValue(15.0)

        result = obj.setTcpIpIpReassTimeout(value)
        assert result is obj
        assert obj.getTcpIpIpReassTimeout() is value

        obj.setTcpIpIpReassTimeout(None)
        assert obj.getTcpIpIpReassTimeout() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv4FragmentationProps.getTcpIpIpFragmentationRxEnabled.__doc__) == FRAGMENTATION_RX_ENABLED_NOTE
        assert inspect.cleandoc(Ipv4FragmentationProps.setTcpIpIpFragmentationRxEnabled.__doc__) == (
            FRAGMENTATION_RX_ENABLED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpFragmentationRxEnabled."
        )
        assert inspect.cleandoc(Ipv4FragmentationProps.getTcpIpIpNumFragments.__doc__) == NUM_FRAGMENTS_NOTE
        assert inspect.cleandoc(Ipv4FragmentationProps.setTcpIpIpNumFragments.__doc__) == (NUM_FRAGMENTS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpNumFragments.")
        assert inspect.cleandoc(Ipv4FragmentationProps.getTcpIpIpNumReassDgrams.__doc__) == NUM_REASS_DGRAMS_NOTE
        assert inspect.cleandoc(Ipv4FragmentationProps.setTcpIpIpNumReassDgrams.__doc__) == (
            NUM_REASS_DGRAMS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpNumReassDgrams."
        )
        assert inspect.cleandoc(Ipv4FragmentationProps.getTcpIpIpReassTimeout.__doc__) == REASS_TIMEOUT_NOTE
        assert inspect.cleandoc(Ipv4FragmentationProps.setTcpIpIpReassTimeout.__doc__) == (REASS_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpReassTimeout.")
