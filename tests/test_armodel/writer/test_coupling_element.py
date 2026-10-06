"""
Writer/reader round-trip tests for CouplingElement (Table 3.52, p.108).

XML element order per XSD COUPLING-ELEMENT group: COMMUNICATION-CLUSTER-REF,
COUPLING-ELEMENT-DETAILS, COUPLING-PORTS, COUPLING-TYPE, ECU-INSTANCE-REF,
FIREWALL-RULE-REFS. The wrappers COUPLING-ELEMENT-DETAILS/COUPLING-PORTS/
FIREWALL-RULE-REFS are emitted only when non-empty. writeCouplingElement calls
writeIdentifiable on the COUPLING-ELEMENT element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElement,
    CouplingElementEnum,
    EthernetConnectionNegotiationEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "COMMUNICATION-CLUSTER-REF",
    "COUPLING-ELEMENT-DETAILS",
    "COUPLING-PORTS",
    "COUPLING-TYPE",
    "ECU-INSTANCE-REF",
    "FIREWALL-RULE-REFS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _pkg():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_coupling_element():
    coupling_element = CouplingElement(_pkg(), "Switch")
    coupling_element.setCommunicationClusterRef(_ref("/Pkg/EthernetClusters/Cluster", "ETHERNET-CLUSTER"))
    coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
    port = coupling_element.createCouplingPort("Cport1")
    port.setConnectionNegotiationBehavior(EthernetConnectionNegotiationEnum().setValue(EthernetConnectionNegotiationEnum.AUTO))
    coupling_element.setCouplingType(CouplingElementEnum().setValue(CouplingElementEnum.SWITCH))
    coupling_element.setEcuInstanceRef(_ref("/Pkg/Ecus/Ecu1", "ECU-INSTANCE"))
    coupling_element.addFirewallRuleRef(_ref("/Pkg/Firewalls/Rule1", "STATE-DEPENDENT-FIREWALL"))
    coupling_element.addFirewallRuleRef(_ref("/Pkg/Firewalls/Rule2", "STATE-DEPENDENT-FIREWALL"))
    return coupling_element


def _write_coupling_element(coupling_element):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeCouplingElement(parent, coupling_element)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteCouplingElement:
    def test_entry_point_emits_short_name_and_group_in_xsd_order(self):
        parent = _write_coupling_element(_full_coupling_element())
        coupling_element = parent.find("COUPLING-ELEMENT")

        assert coupling_element.find("SHORT-NAME").text == "Switch"
        children = [child.tag for child in coupling_element]
        assert children == ["SHORT-NAME"] + XSD_ORDER

    def test_entry_point_writes_field_values(self):
        parent = _write_coupling_element(_full_coupling_element())
        coupling_element = parent.find("COUPLING-ELEMENT")

        cluster_ref = coupling_element.find("COMMUNICATION-CLUSTER-REF")
        assert cluster_ref.text == "/Pkg/EthernetClusters/Cluster"
        assert cluster_ref.attrib["DEST"] == "ETHERNET-CLUSTER"
        assert coupling_element.find("COUPLING-ELEMENT-DETAILS/COUPLING-ELEMENT-SWITCH-DETAILS/SHORT-NAME").text == "SwitchDetails"
        ports = coupling_element.findall("COUPLING-PORTS/COUPLING-PORT")
        assert len(ports) == 1
        assert ports[0].find("SHORT-NAME").text == "Cport1"
        assert coupling_element.find("COUPLING-TYPE").text == "SWITCH"
        ecu_ref = coupling_element.find("ECU-INSTANCE-REF")
        assert ecu_ref.text == "/Pkg/Ecus/Ecu1"
        assert ecu_ref.attrib["DEST"] == "ECU-INSTANCE"
        firewall_refs = coupling_element.findall("FIREWALL-RULE-REFS/FIREWALL-RULE-REF")
        assert len(firewall_refs) == 2
        assert firewall_refs[0].text == "/Pkg/Firewalls/Rule1"
        assert firewall_refs[0].attrib["DEST"] == "STATE-DEPENDENT-FIREWALL"
        assert firewall_refs[1].text == "/Pkg/Firewalls/Rule2"

    def test_bare_coupling_element_emits_no_wrappers(self):
        parent = _write_coupling_element(CouplingElement(_pkg(), "Switch"))
        coupling_element = parent.find("COUPLING-ELEMENT")

        assert coupling_element.find("SHORT-NAME").text == "Switch"
        for tag in XSD_ORDER:
            assert coupling_element.find(tag) is None, tag


class TestCouplingElementRoundTrip:
    def test_round_trip_full_through_coupling_element(self):
        parent = _write_coupling_element(_full_coupling_element())
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Switch"
        assert reloaded.getCommunicationClusterRef().getValue() == "/Pkg/EthernetClusters/Cluster"
        assert reloaded.getCommunicationClusterRef().getDest() == "ETHERNET-CLUSTER"
        assert reloaded.getCouplingElementDetails().getShortName() == "SwitchDetails"
        ports = reloaded.getCouplingPorts()
        assert len(ports) == 1
        assert ports[0].getShortName() == "Cport1"
        assert ports[0].getConnectionNegotiationBehavior().getValue() == EthernetConnectionNegotiationEnum.AUTO
        assert reloaded.getCouplingType().getValue() == CouplingElementEnum.SWITCH
        assert reloaded.getEcuInstanceRef().getValue() == "/Pkg/Ecus/Ecu1"
        assert reloaded.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        firewall_refs = reloaded.getFirewallRuleRefs()
        assert len(firewall_refs) == 2
        assert firewall_refs[0].getValue() == "/Pkg/Firewalls/Rule1"
        assert firewall_refs[0].getDest() == "STATE-DEPENDENT-FIREWALL"
        assert firewall_refs[1].getValue() == "/Pkg/Firewalls/Rule2"

    def test_round_trip_empty_through_coupling_element(self):
        parent = _write_coupling_element(CouplingElement(_pkg(), "Switch"))
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Switch"
        assert reloaded.getCommunicationClusterRef() is None
        assert reloaded.getCouplingElementDetails() is None
        assert reloaded.getCouplingPorts() == []
        assert reloaded.getCouplingType() is None
        assert reloaded.getEcuInstanceRef() is None
        assert reloaded.getFirewallRuleRefs() == []

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        coupling_element = pkg.createCouplingElement("Switch")
        coupling_element.setCommunicationClusterRef(_ref("/Pkg/EthernetClusters/Cluster", "ETHERNET-CLUSTER"))
        coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        coupling_element.createCouplingPort("Cport1")
        coupling_element.setCouplingType(CouplingElementEnum().setValue(CouplingElementEnum.SWITCH))
        coupling_element.setEcuInstanceRef(_ref("/Pkg/Ecus/Ecu1", "ECU-INSTANCE"))
        coupling_element.addFirewallRuleRef(_ref("/Pkg/Firewalls/Rule1", "STATE-DEPENDENT-FIREWALL"))

        out_file = str(tmp_path / "coupling_element.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance().new()
        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded = [e for e in reloaded_pkg.getReferrableElements() if isinstance(e, CouplingElement)]
        assert len(reloaded) == 1
        reloaded = reloaded[0]
        assert reloaded.getShortName() == "Switch"
        assert reloaded.getCommunicationClusterRef().getValue() == "/Pkg/EthernetClusters/Cluster"
        assert reloaded.getCouplingElementDetails().getShortName() == "SwitchDetails"
        assert reloaded.getCouplingPorts()[0].getShortName() == "Cport1"
        assert reloaded.getCouplingType().getValue() == CouplingElementEnum.SWITCH
        assert reloaded.getEcuInstanceRef().getValue() == "/Pkg/Ecus/Ecu1"
        assert reloaded.getFirewallRuleRefs()[0].getValue() == "/Pkg/Firewalls/Rule1"
