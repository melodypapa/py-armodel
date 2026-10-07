"""
Test suite for Ipv6Props (CP_TPS_SystemTemplate Table 3.105, p.148, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv6Props model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, Dhcpv6Props, Ipv6FragmentationProps, Ipv6NdpProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6Props

CLASS_NOTE = "This meta-class specifies the configuration options for IPv6."


class TestIpv6Props:
    def test_inheritance(self):
        assert issubclass(Ipv6Props, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6Props.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv6Props()

        assert obj.getDhcpProps() is None
        assert obj.getFragmentationProps() is None
        assert obj.getNdpProps() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv6Props")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["dhcpProps"] == "Optional[Dhcpv6Props]"
        assert annotations["fragmentationProps"] == "Optional[Ipv6FragmentationProps]"
        assert annotations["ndpProps"] == "Optional[Ipv6NdpProps]"

        assert typing.get_type_hints(Ipv6Props.getDhcpProps).get("return") == typing.Optional[Dhcpv6Props]
        assert typing.get_type_hints(Ipv6Props.setDhcpProps).get("return") is Ipv6Props
        assert typing.get_type_hints(Ipv6Props.getFragmentationProps).get("return") == typing.Optional[Ipv6FragmentationProps]
        assert typing.get_type_hints(Ipv6Props.setFragmentationProps).get("return") is Ipv6Props
        assert typing.get_type_hints(Ipv6Props.getNdpProps).get("return") == typing.Optional[Ipv6NdpProps]
        assert typing.get_type_hints(Ipv6Props.setNdpProps).get("return") is Ipv6Props

    def test_member_order(self):
        obj = Ipv6Props()

        members = [k for k in vars(obj) if k in {"dhcpProps", "fragmentationProps", "ndpProps"}]
        assert members == ["dhcpProps", "fragmentationProps", "ndpProps"]

    def test_get_set_dhcp_props(self):
        obj = Ipv6Props()
        value = Dhcpv6Props()

        result = obj.setDhcpProps(value)
        assert result is obj
        assert obj.getDhcpProps() is value

        obj.setDhcpProps(None)
        assert obj.getDhcpProps() is value

    def test_get_set_fragmentation_props(self):
        obj = Ipv6Props()
        value = Ipv6FragmentationProps()

        result = obj.setFragmentationProps(value)
        assert result is obj
        assert obj.getFragmentationProps() is value

        obj.setFragmentationProps(None)
        assert obj.getFragmentationProps() is value

    def test_get_set_ndp_props(self):
        obj = Ipv6Props()
        value = Ipv6NdpProps()

        result = obj.setNdpProps(value)
        assert result is obj
        assert obj.getNdpProps() is value

        obj.setNdpProps(None)
        assert obj.getNdpProps() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv6Props.getDhcpProps.__doc__) == "Configuration properties for DHCPv6."
        assert inspect.cleandoc(Ipv6Props.setDhcpProps.__doc__) == ("Configuration properties for DHCPv6.\n\nA None value is a no-op and does not overwrite an existing dhcpProps.")
        assert inspect.cleandoc(Ipv6Props.getFragmentationProps.__doc__) == "Configuration properties for IPv6 packet fragmentation/reassembly."
        assert inspect.cleandoc(Ipv6Props.setFragmentationProps.__doc__) == (
            "Configuration properties for IPv6 packet fragmentation/reassembly.\n\nA None value is a no-op and does not overwrite an existing fragmentationProps."
        )
        assert inspect.cleandoc(Ipv6Props.getNdpProps.__doc__) == "Configuration properties for the Neighbor Discovery Protocol for IPv6."
        assert inspect.cleandoc(Ipv6Props.setNdpProps.__doc__) == (
            "Configuration properties for the Neighbor Discovery Protocol for IPv6.\n\nA None value is a no-op and does not overwrite an existing ndpProps."
        )
