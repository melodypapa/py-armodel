"""
Test suite for Ipv4Props (CP_TPS_SystemTemplate Table 3.101, p.146, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv4Props model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, Ipv4FragmentationProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps, Ipv4AutoIpProps, Ipv4Props

CLASS_NOTE = "This meta-class specifies the configuration options for IPv4."


class TestIpv4Props:
    def test_inheritance(self):
        assert issubclass(Ipv4Props, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv4Props.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv4Props()

        assert obj.getArpProps() is None
        assert obj.getAutoIpProps() is None
        assert obj.getFragmentationProps() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv4Props")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["arpProps"] == "Optional[Ipv4ArpProps]"
        assert annotations["autoIpProps"] == "Optional[Ipv4AutoIpProps]"
        assert annotations["fragmentationProps"] == "Optional[Ipv4FragmentationProps]"

        assert typing.get_type_hints(Ipv4Props.getArpProps).get("return") == typing.Optional[Ipv4ArpProps]
        assert typing.get_type_hints(Ipv4Props.setArpProps).get("return") is Ipv4Props
        assert typing.get_type_hints(Ipv4Props.getAutoIpProps).get("return") == typing.Optional[Ipv4AutoIpProps]
        assert typing.get_type_hints(Ipv4Props.setAutoIpProps).get("return") is Ipv4Props
        assert typing.get_type_hints(Ipv4Props.getFragmentationProps).get("return") == typing.Optional[Ipv4FragmentationProps]
        assert typing.get_type_hints(Ipv4Props.setFragmentationProps).get("return") is Ipv4Props

    def test_member_order(self):
        obj = Ipv4Props()

        members = [k for k in vars(obj) if k in {"arpProps", "autoIpProps", "fragmentationProps"}]
        assert members == ["arpProps", "autoIpProps", "fragmentationProps"]

    def test_get_set_arp_props(self):
        obj = Ipv4Props()
        value = Ipv4ArpProps()

        result = obj.setArpProps(value)
        assert result is obj
        assert obj.getArpProps() is value

        obj.setArpProps(None)
        assert obj.getArpProps() is value

    def test_get_set_auto_ip_props(self):
        obj = Ipv4Props()
        value = Ipv4AutoIpProps()

        result = obj.setAutoIpProps(value)
        assert result is obj
        assert obj.getAutoIpProps() is value

        obj.setAutoIpProps(None)
        assert obj.getAutoIpProps() is value

    def test_get_set_fragmentation_props(self):
        obj = Ipv4Props()
        value = Ipv4FragmentationProps()

        result = obj.setFragmentationProps(value)
        assert result is obj
        assert obj.getFragmentationProps() is value

        obj.setFragmentationProps(None)
        assert obj.getFragmentationProps() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv4Props.getArpProps.__doc__) == "Configuration properties for the ARP (Address Resolution Protocol)."
        assert inspect.cleandoc(Ipv4Props.setArpProps.__doc__) == (
            "Configuration properties for the ARP (Address Resolution Protocol).\n\nA None value is a no-op and does not overwrite an existing arpProps."
        )
        assert inspect.cleandoc(Ipv4Props.getAutoIpProps.__doc__) == "Configuration options for Auto-IP (automatic private IP addressing)."
        assert inspect.cleandoc(Ipv4Props.setAutoIpProps.__doc__) == (
            "Configuration options for Auto-IP (automatic private IP addressing).\n\nA None value is a no-op and does not overwrite an existing autoIpProps."
        )
        assert inspect.cleandoc(Ipv4Props.getFragmentationProps.__doc__) == "Configuration options for IPv4 packet fragmentation/reassembly."
        assert inspect.cleandoc(Ipv4Props.setFragmentationProps.__doc__) == (
            "Configuration options for IPv4 packet fragmentation/reassembly.\n\nA None value is a no-op and does not overwrite an existing fragmentationProps."
        )
