"""
Test suite for CouplingElement (CP_TPS_SystemTemplate Table 3.52, p.108, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, factory
semantics (duplicate short name returns the existing element) and the verbatim
class-level spec Note of the CouplingElement model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElement,
    CouplingElementAbstractDetails,
    CouplingElementEnum,
    CouplingElementSwitchDetails,
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

CLASS_NOTE = (
    "A CouplingElement is used to connect EcuInstances to the VLAN of an EthernetCluster. "
    "Coupling Elements can reach from a simple hub to a complex managed switch or even devices "
    "with functionalities in higher layers. A CouplingElement that is not related to an "
    "EcuInstance occurs as a dedicated single device. Tags: atp.recommendedPackage=CouplingElements"
)


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    ref.setDest("ETHERNET-CLUSTER-REF")
    return ref


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestCouplingElement:
    def test_inheritance(self):
        assert issubclass(CouplingElement, FibexElement)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CouplingElement.__doc__) == CLASS_NOTE

    def test_initialization(self):
        coupling_element = CouplingElement(MockParent(), "CE1")

        assert coupling_element.getShortName() == "CE1"
        assert coupling_element.getCommunicationClusterRef() is None
        assert coupling_element.getCouplingElementDetails() is None
        assert coupling_element.getCouplingPorts() == []
        assert coupling_element.getCouplingType() is None
        assert coupling_element.getEcuInstanceRef() is None
        assert coupling_element.getFirewallRuleRefs() == []

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "CouplingElement")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        assert annotations["communicationClusterRef"] == "Optional[RefType]"
        assert annotations["couplingElementDetails"] == "Optional[CouplingElementAbstractDetails]"
        assert annotations["couplingPorts"] == "List[CouplingPort]"
        assert annotations["couplingType"] == "Optional[CouplingElementEnum]"
        assert annotations["ecuInstanceRef"] == "Optional[RefType]"
        assert annotations["firewallRuleRefs"] == "List[RefType]"

        assert typing.get_type_hints(CouplingElement.createCouplingElementSwitchDetails).get("return") is CouplingElementSwitchDetails
        assert typing.get_type_hints(CouplingElement.getCouplingElementDetails).get("return") == typing.Optional[CouplingElementAbstractDetails]
        assert typing.get_type_hints(CouplingElement.createCouplingPort).get("return") is CouplingPort
        assert typing.get_type_hints(CouplingElement.getCouplingPorts).get("return") == typing.List[CouplingPort]
        assert typing.get_type_hints(CouplingElement.getCouplingType).get("return") == typing.Optional[CouplingElementEnum]
        assert typing.get_type_hints(CouplingElement.getFirewallRuleRefs).get("return") == typing.List[RefType]

    def test_get_set_communication_cluster_ref(self):
        coupling_element = CouplingElement(MockParent(), "CE1")
        ref = _ref("/Pkg/EthernetClusters/Cluster")

        result = coupling_element.setCommunicationClusterRef(ref)
        assert result == coupling_element
        assert coupling_element.getCommunicationClusterRef() is ref

        coupling_element.setCommunicationClusterRef(None)
        assert coupling_element.getCommunicationClusterRef() is ref

    def test_create_coupling_element_switch_details(self):
        coupling_element = CouplingElement(MockParent(), "CE1")

        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        assert isinstance(details, CouplingElementSwitchDetails)
        assert details.getShortName() == "SwitchDetails"
        assert coupling_element.getCouplingElementDetails() is details

        duplicate = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        assert duplicate is details
        assert coupling_element.getCouplingElementDetails() is details

    def test_create_coupling_port(self):
        coupling_element = CouplingElement(MockParent(), "CE1")

        port = coupling_element.createCouplingPort("Cport1")
        assert isinstance(port, CouplingPort)
        assert port.getShortName() == "Cport1"
        assert coupling_element.getCouplingPorts() == [port]

        duplicate = coupling_element.createCouplingPort("Cport1")
        assert duplicate is port
        assert len(coupling_element.getCouplingPorts()) == 1

        second = coupling_element.createCouplingPort("Cport2")
        assert coupling_element.getCouplingPorts() == [port, second]

    def test_get_set_coupling_type(self):
        coupling_element = CouplingElement(MockParent(), "CE1")
        coupling_type = CouplingElementEnum().setValue(CouplingElementEnum.SWITCH)

        result = coupling_element.setCouplingType(coupling_type)
        assert result == coupling_element
        assert coupling_element.getCouplingType() is coupling_type
        assert coupling_element.getCouplingType().getValue() == CouplingElementEnum.SWITCH

        coupling_element.setCouplingType(None)
        assert coupling_element.getCouplingType() is coupling_type

    def test_get_set_ecu_instance_ref(self):
        coupling_element = CouplingElement(MockParent(), "CE1")
        ref = RefType()
        ref.setValue("/Pkg/Ecus/Ecu1")
        ref.setDest("ECU-INSTANCE-REF")

        result = coupling_element.setEcuInstanceRef(ref)
        assert result == coupling_element
        assert coupling_element.getEcuInstanceRef() is ref

        coupling_element.setEcuInstanceRef(None)
        assert coupling_element.getEcuInstanceRef() is ref

    def test_add_firewall_rule_ref(self):
        coupling_element = CouplingElement(MockParent(), "CE1")
        ref = RefType()
        ref.setValue("/Pkg/Firewalls/Rule1")
        ref.setDest("STATE-DEPENDENT-FIREWALL-REF")

        result = coupling_element.addFirewallRuleRef(ref)
        assert result == coupling_element
        assert coupling_element.getFirewallRuleRefs() == [ref]

        coupling_element.addFirewallRuleRef(None)
        assert coupling_element.getFirewallRuleRefs() == [ref]

        second = RefType()
        second.setValue("/Pkg/Firewalls/Rule2")
        second.setDest("STATE-DEPENDENT-FIREWALL-REF")
        coupling_element.addFirewallRuleRef(second)
        assert coupling_element.getFirewallRuleRefs() == [ref, second]
