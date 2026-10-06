"""
Test suite for EthIpProps (CP_TPS_SystemTemplate Table 3.100, p.146, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, factory
semantics (duplicate short name returns the existing element) and the verbatim
class-level spec Note of the EthIpProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, Ipv4Props, Ipv6Props
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthIpProps

CLASS_NOTE = "This meta-class is used to configure the EcuInstance specific IP attributes. Tags: atp.recommendedPackage=EthIpProps"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestEthIpProps:
    def test_inheritance(self):
        assert issubclass(EthIpProps, ARElement)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthIpProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = EthIpProps(MockParent(), "IpProps1")

        assert obj.getShortName() == "IpProps1"
        assert obj.getIpv4Props() is None
        assert obj.getIpv6Props() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "EthIpProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["ipv4Props"] == "Optional[Ipv4Props]"
        assert annotations["ipv6Props"] == "Optional[Ipv6Props]"

        assert typing.get_type_hints(EthIpProps.getIpv4Props).get("return") == typing.Optional[Ipv4Props]
        assert typing.get_type_hints(EthIpProps.setIpv4Props).get("return") is EthIpProps
        assert typing.get_type_hints(EthIpProps.getIpv6Props).get("return") == typing.Optional[Ipv6Props]
        assert typing.get_type_hints(EthIpProps.setIpv6Props).get("return") is EthIpProps

    def test_member_order(self):
        obj = EthIpProps(MockParent(), "IpProps1")

        members = [k for k in vars(obj) if k in {"ipv4Props", "ipv6Props"}]
        assert members == ["ipv4Props", "ipv6Props"]

    def test_get_set_ipv4_props(self):
        obj = EthIpProps(MockParent(), "IpProps1")
        value = Ipv4Props()

        result = obj.setIpv4Props(value)
        assert result is obj
        assert obj.getIpv4Props() is value

        obj.setIpv4Props(None)
        assert obj.getIpv4Props() is value

    def test_get_set_ipv6_props(self):
        obj = EthIpProps(MockParent(), "IpProps1")
        value = Ipv6Props()

        result = obj.setIpv6Props(value)
        assert result is obj
        assert obj.getIpv6Props() is value

        obj.setIpv6Props(None)
        assert obj.getIpv6Props() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(EthIpProps.getIpv4Props.__doc__) == "Configuration options for IPv4."
        assert inspect.cleandoc(EthIpProps.setIpv4Props.__doc__) == ("Configuration options for IPv4.\n\nA None value is a no-op and does not overwrite an existing ipv4Props.")
        assert inspect.cleandoc(EthIpProps.getIpv6Props.__doc__) == "Configuration options for IPv6."
        assert inspect.cleandoc(EthIpProps.setIpv6Props.__doc__) == ("Configuration options for IPv6.\n\nA None value is a no-op and does not overwrite an existing ipv6Props.")

    def test_arpackage_factory(self):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("EthIpPropsPkg")

        props = pkg.createEthIpProps("Props1")
        assert isinstance(props, EthIpProps)
        assert props.getShortName() == "Props1"

        again = pkg.createEthIpProps("Props1")
        assert again is props
