"""
Test suite for Dhcpv6Props (CP_TPS_SystemTemplate Table 3.107, p.149, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Dhcpv6Props model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Dhcpv6Props

CLASS_NOTE = "This meta-class specifies the configuration options for DHCPv6."

MEMBER_ORDER = [
    "tcpIpDhcpV6CnfDelayMax",
    "tcpIpDhcpV6CnfDelayMin",
    "tcpIpDhcpV6InfDelayMax",
    "tcpIpDhcpV6InfDelayMin",
    "tcpIpDhcpV6SolDelayMax",
    "tcpIpDhcpV6SolDelayMin",
]

CNF_DELAY_MAX_NOTE = (
    "Maximum delay in seconds before sending the first Confirm message. If this value is bigger than the previous minimum delay value " "a random delay will be chosen from the interval."
)
CNF_DELAY_MIN_NOTE = "Minimum delay in seconds before the first Confirm message will be sent."
INF_DELAY_MAX_NOTE = (
    "Maximum delay in seconds before sending the first Information Request message. If this value is bigger than the previous minimum " "delay value a random delay will be chosen from the interval."
)
INF_DELAY_MIN_NOTE = "Minimum delay (s) before the first Information Request message will be sent."
SOL_DELAY_MAX_NOTE = (
    "Maximum delay in seconds before sending the first Solicit message. If this value is bigger than the previous minimum delay value " "a random delay will be chosen from the interval."
)
SOL_DELAY_MIN_NOTE = "Minimum delay (s) before the first Solicit message will be sent."


class TestDhcpv6Props:
    def test_inheritance(self):
        assert issubclass(Dhcpv6Props, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Dhcpv6Props.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Dhcpv6Props()

        assert obj.getTcpIpDhcpV6CnfDelayMax() is None
        assert obj.getTcpIpDhcpV6CnfDelayMin() is None
        assert obj.getTcpIpDhcpV6InfDelayMax() is None
        assert obj.getTcpIpDhcpV6InfDelayMin() is None
        assert obj.getTcpIpDhcpV6SolDelayMax() is None
        assert obj.getTcpIpDhcpV6SolDelayMin() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Dhcpv6Props")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        for member in MEMBER_ORDER:
            assert annotations[member] == "Optional[TimeValue]"

        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6CnfDelayMax).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6CnfDelayMax).get("return") is Dhcpv6Props
        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6CnfDelayMin).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6CnfDelayMin).get("return") is Dhcpv6Props
        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6InfDelayMax).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6InfDelayMax).get("return") is Dhcpv6Props
        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6InfDelayMin).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6InfDelayMin).get("return") is Dhcpv6Props
        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6SolDelayMax).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6SolDelayMax).get("return") is Dhcpv6Props
        assert typing.get_type_hints(Dhcpv6Props.getTcpIpDhcpV6SolDelayMin).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Dhcpv6Props.setTcpIpDhcpV6SolDelayMin).get("return") is Dhcpv6Props

    def test_member_order(self):
        obj = Dhcpv6Props()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_dhcp_v6_cnf_delay_max(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(100.0)

        result = obj.setTcpIpDhcpV6CnfDelayMax(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6CnfDelayMax() is value

        obj.setTcpIpDhcpV6CnfDelayMax(None)
        assert obj.getTcpIpDhcpV6CnfDelayMax() is value

    def test_get_set_tcp_ip_dhcp_v6_cnf_delay_min(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpDhcpV6CnfDelayMin(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6CnfDelayMin() is value

        obj.setTcpIpDhcpV6CnfDelayMin(None)
        assert obj.getTcpIpDhcpV6CnfDelayMin() is value

    def test_get_set_tcp_ip_dhcp_v6_inf_delay_max(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(120.0)

        result = obj.setTcpIpDhcpV6InfDelayMax(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6InfDelayMax() is value

        obj.setTcpIpDhcpV6InfDelayMax(None)
        assert obj.getTcpIpDhcpV6InfDelayMax() is value

    def test_get_set_tcp_ip_dhcp_v6_inf_delay_min(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpDhcpV6InfDelayMin(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6InfDelayMin() is value

        obj.setTcpIpDhcpV6InfDelayMin(None)
        assert obj.getTcpIpDhcpV6InfDelayMin() is value

    def test_get_set_tcp_ip_dhcp_v6_sol_delay_max(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(120.0)

        result = obj.setTcpIpDhcpV6SolDelayMax(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6SolDelayMax() is value

        obj.setTcpIpDhcpV6SolDelayMax(None)
        assert obj.getTcpIpDhcpV6SolDelayMax() is value

    def test_get_set_tcp_ip_dhcp_v6_sol_delay_min(self):
        obj = Dhcpv6Props()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpDhcpV6SolDelayMin(value)
        assert result is obj
        assert obj.getTcpIpDhcpV6SolDelayMin() is value

        obj.setTcpIpDhcpV6SolDelayMin(None)
        assert obj.getTcpIpDhcpV6SolDelayMin() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6CnfDelayMax.__doc__) == CNF_DELAY_MAX_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6CnfDelayMax.__doc__) == (CNF_DELAY_MAX_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6CnfDelayMax.")
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6CnfDelayMin.__doc__) == CNF_DELAY_MIN_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6CnfDelayMin.__doc__) == (CNF_DELAY_MIN_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6CnfDelayMin.")
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6InfDelayMax.__doc__) == INF_DELAY_MAX_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6InfDelayMax.__doc__) == (INF_DELAY_MAX_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6InfDelayMax.")
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6InfDelayMin.__doc__) == INF_DELAY_MIN_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6InfDelayMin.__doc__) == (INF_DELAY_MIN_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6InfDelayMin.")
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6SolDelayMax.__doc__) == SOL_DELAY_MAX_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6SolDelayMax.__doc__) == (SOL_DELAY_MAX_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6SolDelayMax.")
        assert inspect.cleandoc(Dhcpv6Props.getTcpIpDhcpV6SolDelayMin.__doc__) == SOL_DELAY_MIN_NOTE
        assert inspect.cleandoc(Dhcpv6Props.setTcpIpDhcpV6SolDelayMin.__doc__) == (SOL_DELAY_MIN_NOTE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpDhcpV6SolDelayMin.")
