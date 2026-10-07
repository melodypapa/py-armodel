"""
Test suite for Ipv6FragmentationProps (CP_TPS_SystemTemplate Table 3.106, p.148, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv6FragmentationProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6FragmentationProps

CLASS_NOTE = "This meta-class specifies the configuration options for IPv6 packet fragmentation/reassembly."

MEMBER_ORDER = [
    "tcpIpIpReassemblyBufferCount",
    "tcpIpIpReassemblyBufferSize",
    "tcpIpIpReassemblySegmentCount",
    "tcpIpIpReassemblyTimeout",
    "tcpIpIpTxFragmentBufferCount",
    "tcpIpIpTxFragmentBufferSize",
]

REASSEMBLY_BUFFER_COUNT_NOTE = (
    "Number of buffers that can be used for fragment reassembly. In case of a reassembly error or if not all fragments are received in "
    'time this buffer will be blocked until the specified "Fragment Reassembly Timeout" has been exceeded. A value of 0 disables fragment reassembly.'
)
REASSEMBLY_BUFFER_SIZE_NOTE = "Size of each fragment tx buffer in bytes."
REASSEMBLY_SEGMENT_COUNT_NOTE = (
    "Specifies the maximum number of consecutive data segments that can be managed in each reassembly buffer. If all fragments are received "
    "in order, only one segment will be needed. To deal with fragments received out of order this value should be configured bigger than 1."
)
REASSEMBLY_TIMEOUT_NOTE = "Specifies the timeout in seconds after which an incomplete datagram gets discarded."
TX_FRAGMENT_BUFFER_COUNT_NOTE = (
    "These buffers will be used if the IpV6 receives packets from the upper layer that do not fit into the MTU and thus must be fragmented. " "A value of 0 disables tx fragmentation."
)
TX_FRAGMENT_BUFFER_SIZE_NOTE = "Size of each fragment tx buffer in bytes."


class TestIpv6FragmentationProps:
    def test_inheritance(self):
        assert issubclass(Ipv6FragmentationProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6FragmentationProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv6FragmentationProps()

        assert obj.getTcpIpIpReassemblyBufferCount() is None
        assert obj.getTcpIpIpReassemblyBufferSize() is None
        assert obj.getTcpIpIpReassemblySegmentCount() is None
        assert obj.getTcpIpIpReassemblyTimeout() is None
        assert obj.getTcpIpIpTxFragmentBufferCount() is None
        assert obj.getTcpIpIpTxFragmentBufferSize() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv6FragmentationProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["tcpIpIpReassemblyBufferCount"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpReassemblyBufferSize"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpReassemblySegmentCount"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpReassemblyTimeout"] == "Optional[TimeValue]"
        assert annotations["tcpIpIpTxFragmentBufferCount"] == "Optional[PositiveInteger]"
        assert annotations["tcpIpIpTxFragmentBufferSize"] == "Optional[PositiveInteger]"

        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpReassemblyBufferCount).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpReassemblyBufferCount).get("return") is Ipv6FragmentationProps
        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpReassemblyBufferSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpReassemblyBufferSize).get("return") is Ipv6FragmentationProps
        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpReassemblySegmentCount).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpReassemblySegmentCount).get("return") is Ipv6FragmentationProps
        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpReassemblyTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpReassemblyTimeout).get("return") is Ipv6FragmentationProps
        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpTxFragmentBufferCount).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpTxFragmentBufferCount).get("return") is Ipv6FragmentationProps
        assert typing.get_type_hints(Ipv6FragmentationProps.getTcpIpIpTxFragmentBufferSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6FragmentationProps.setTcpIpIpTxFragmentBufferSize).get("return") is Ipv6FragmentationProps

    def test_member_order(self):
        obj = Ipv6FragmentationProps()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_ip_reassembly_buffer_count(self):
        obj = Ipv6FragmentationProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpIpReassemblyBufferCount(value)
        assert result is obj
        assert obj.getTcpIpIpReassemblyBufferCount() is value

        obj.setTcpIpIpReassemblyBufferCount(None)
        assert obj.getTcpIpIpReassemblyBufferCount() is value

    def test_get_set_tcp_ip_ip_reassembly_buffer_size(self):
        obj = Ipv6FragmentationProps()
        value = PositiveInteger().setValue(1500)

        result = obj.setTcpIpIpReassemblyBufferSize(value)
        assert result is obj
        assert obj.getTcpIpIpReassemblyBufferSize() is value

        obj.setTcpIpIpReassemblyBufferSize(None)
        assert obj.getTcpIpIpReassemblyBufferSize() is value

    def test_get_set_tcp_ip_ip_reassembly_segment_count(self):
        obj = Ipv6FragmentationProps()
        value = PositiveInteger().setValue(2)

        result = obj.setTcpIpIpReassemblySegmentCount(value)
        assert result is obj
        assert obj.getTcpIpIpReassemblySegmentCount() is value

        obj.setTcpIpIpReassemblySegmentCount(None)
        assert obj.getTcpIpIpReassemblySegmentCount() is value

    def test_get_set_tcp_ip_ip_reassembly_timeout(self):
        obj = Ipv6FragmentationProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpIpReassemblyTimeout(value)
        assert result is obj
        assert obj.getTcpIpIpReassemblyTimeout() is value

        obj.setTcpIpIpReassemblyTimeout(None)
        assert obj.getTcpIpIpReassemblyTimeout() is value

    def test_get_set_tcp_ip_ip_tx_fragment_buffer_count(self):
        obj = Ipv6FragmentationProps()
        value = PositiveInteger().setValue(5)

        result = obj.setTcpIpIpTxFragmentBufferCount(value)
        assert result is obj
        assert obj.getTcpIpIpTxFragmentBufferCount() is value

        obj.setTcpIpIpTxFragmentBufferCount(None)
        assert obj.getTcpIpIpTxFragmentBufferCount() is value

    def test_get_set_tcp_ip_ip_tx_fragment_buffer_size(self):
        obj = Ipv6FragmentationProps()
        value = PositiveInteger().setValue(1500)

        result = obj.setTcpIpIpTxFragmentBufferSize(value)
        assert result is obj
        assert obj.getTcpIpIpTxFragmentBufferSize() is value

        obj.setTcpIpIpTxFragmentBufferSize(None)
        assert obj.getTcpIpIpTxFragmentBufferSize() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpReassemblyBufferCount.__doc__) == REASSEMBLY_BUFFER_COUNT_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpReassemblyBufferCount.__doc__) == (
            REASSEMBLY_BUFFER_COUNT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpReassemblyBufferCount."
        )
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpReassemblyBufferSize.__doc__) == REASSEMBLY_BUFFER_SIZE_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpReassemblyBufferSize.__doc__) == (
            REASSEMBLY_BUFFER_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpReassemblyBufferSize."
        )
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpReassemblySegmentCount.__doc__) == REASSEMBLY_SEGMENT_COUNT_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpReassemblySegmentCount.__doc__) == (
            REASSEMBLY_SEGMENT_COUNT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpReassemblySegmentCount."
        )
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpReassemblyTimeout.__doc__) == REASSEMBLY_TIMEOUT_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpReassemblyTimeout.__doc__) == (
            REASSEMBLY_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpReassemblyTimeout."
        )
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpTxFragmentBufferCount.__doc__) == TX_FRAGMENT_BUFFER_COUNT_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpTxFragmentBufferCount.__doc__) == (
            TX_FRAGMENT_BUFFER_COUNT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpTxFragmentBufferCount."
        )
        assert inspect.cleandoc(Ipv6FragmentationProps.getTcpIpIpTxFragmentBufferSize.__doc__) == TX_FRAGMENT_BUFFER_SIZE_NOTE
        assert inspect.cleandoc(Ipv6FragmentationProps.setTcpIpIpTxFragmentBufferSize.__doc__) == (
            TX_FRAGMENT_BUFFER_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpIpTxFragmentBufferSize."
        )
