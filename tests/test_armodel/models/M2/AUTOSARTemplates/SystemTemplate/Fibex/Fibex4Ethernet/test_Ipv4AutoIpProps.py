"""
Test suite for Ipv4AutoIpProps (CP_TPS_SystemTemplate Table 3.103, p.147, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv4AutoIpProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4AutoIpProps

CLASS_NOTE = "Specifies the configuration options for Auto-IP (automatic private IP addressing)."

MEMBER_ORDER = [
    "tcpIpAutoIpInitTimeout",
]

INIT_TIMEOUT_NOTE = (
    "This attribute specifies the time in seconds Auto-IP waits at startup, before beginning with ARP probing. "
    "This delay is used to give DHCP time to acquire a lease in case a DHCP server is present."
)


class TestIpv4AutoIpProps:
    def test_inheritance(self):
        assert issubclass(Ipv4AutoIpProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4AutoIpProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv4AutoIpProps()

        assert obj.getTcpIpAutoIpInitTimeout() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv4AutoIpProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["tcpIpAutoIpInitTimeout"] == "Optional[TimeValue]"

        assert typing.get_type_hints(Ipv4AutoIpProps.getTcpIpAutoIpInitTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv4AutoIpProps.setTcpIpAutoIpInitTimeout).get("return") is Ipv4AutoIpProps

    def test_member_order(self):
        obj = Ipv4AutoIpProps()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_auto_ip_init_timeout(self):
        obj = Ipv4AutoIpProps()
        value = TimeValue().setValue(3.0)

        result = obj.setTcpIpAutoIpInitTimeout(value)
        assert result is obj
        assert obj.getTcpIpAutoIpInitTimeout() is value

        obj.setTcpIpAutoIpInitTimeout(None)
        assert obj.getTcpIpAutoIpInitTimeout() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv4AutoIpProps.getTcpIpAutoIpInitTimeout.__doc__) == INIT_TIMEOUT_NOTE
        assert inspect.cleandoc(Ipv4AutoIpProps.setTcpIpAutoIpInitTimeout.__doc__) == (INIT_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpAutoIpInitTimeout.")
