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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CategoryString, Identifier, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElement,
    CouplingElementAbstractDetails,
    CouplingElementEnum,
    CouplingElementSwitchDetails,
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


class TestCouplingElementAbstractDetailsRoundTrip:
    """CouplingElementAbstractDetails (Table 3.82, p.133) — the COUPLING-ELEMENT-SWITCH-DETAILS
    item round-trips its identity levels and the abstract-level VARIATION-POINT group child
    (XSD group COUPLING-ELEMENT-ABSTRACT-DETAILS, sequenceOffset=10000 → last)."""

    def _coupling_element_with_details(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        return coupling_element, details

    def test_details_writes_identity_levels_and_variation_point(self):
        coupling_element, details = self._coupling_element_with_details()
        details.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
        details.setCategory(CategoryString().setValue("myCategory"))
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vpLabel"))
        details.setVariationPoint(variation_point)

        parent = _write_coupling_element(coupling_element)
        details_element = parent.find("COUPLING-ELEMENT/COUPLING-ELEMENT-DETAILS/COUPLING-ELEMENT-SWITCH-DETAILS")

        assert details_element is not None
        assert details_element.find("SHORT-NAME").text == "SwitchDetails"
        assert details_element.attrib["UUID"] == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert details_element.find("CATEGORY").text == "myCategory"
        children = [child.tag for child in details_element]
        assert children[-1] == "VARIATION-POINT"
        assert details_element.find("VARIATION-POINT/SHORT-LABEL").text == "vpLabel"

    def test_details_without_variation_point_writes_no_vp_element(self):
        coupling_element, _ = self._coupling_element_with_details()

        parent = _write_coupling_element(coupling_element)
        details_element = parent.find("COUPLING-ELEMENT/COUPLING-ELEMENT-DETAILS/COUPLING-ELEMENT-SWITCH-DETAILS")

        assert details_element.find("SHORT-NAME").text == "SwitchDetails"
        assert details_element.find("VARIATION-POINT") is None

    def test_round_trip_details_field_values(self):
        coupling_element, details = self._coupling_element_with_details()
        details.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
        details.setCategory(CategoryString().setValue("myCategory"))
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vpLabel"))
        details.setVariationPoint(variation_point)

        parent = _write_coupling_element(coupling_element)
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        reloaded_details = reloaded.getCouplingElementDetails()
        assert isinstance(reloaded_details, CouplingElementAbstractDetails)
        assert reloaded_details.getShortName() == "SwitchDetails"
        assert reloaded_details.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert reloaded_details.getCategory().getValue() == "myCategory"
        assert reloaded_details.getVariationPoint() is not None
        assert reloaded_details.getVariationPoint().getShortLabel().getValue() == "vpLabel"


class TestCouplingElementSwitchDetailsRoundTrip:
    """CouplingElementSwitchDetails (Table 3.83, p.133) — the five switch-level wrapper groups
    of COUPLING-ELEMENT-SWITCH-DETAILS (XSD group COUPLING-ELEMENT-SWITCH-DETAILS) round-trip
    after the abstract level. XML child order per XSD sequence: the identifiable levels,
    VARIATION-POINT (abstract level), then FLOW-METERINGS, STREAM-FILTERS, STREAM-GATES,
    SWITCH-STREAM-IDENTIFICATIONS, TRAFFIC-SHAPER-GROUPS. Wrappers are emitted only when
    non-empty."""

    SWITCH_XSD_ORDER = [
        "FLOW-METERINGS",
        "STREAM-FILTERS",
        "STREAM-GATES",
        "SWITCH-STREAM-IDENTIFICATIONS",
        "TRAFFIC-SHAPER-GROUPS",
    ]

    def _coupling_element_with_full_switch_details(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        details.createFlowMetering("Metering1")
        details.createFlowMetering("Metering2")
        details.createStreamFilter("Filter1")
        details.createStreamGate("Gate1")
        details.createSwitchStreamIdentification("Stream1")
        details.createSwitchStreamIdentification("Stream2")
        details.createTrafficShaperGroup("Group1")
        return coupling_element, details

    def _switch_details_element(self, coupling_element):
        parent = _write_coupling_element(coupling_element)
        return parent.find("COUPLING-ELEMENT/COUPLING-ELEMENT-DETAILS/COUPLING-ELEMENT-SWITCH-DETAILS")

    def test_writes_five_wrappers_in_xsd_order(self):
        coupling_element, details = self._coupling_element_with_full_switch_details()
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vpLabel"))
        details.setVariationPoint(variation_point)

        details_element = self._switch_details_element(coupling_element)

        children = [child.tag for child in details_element]
        assert children == ["SHORT-NAME", "VARIATION-POINT"] + self.SWITCH_XSD_ORDER

    def test_writes_field_values(self):
        coupling_element, _ = self._coupling_element_with_full_switch_details()

        details_element = self._switch_details_element(coupling_element)

        assert details_element.find("SHORT-NAME").text == "SwitchDetails"
        flow_meterings = details_element.findall("FLOW-METERINGS/SWITCH-FLOW-METERING-ENTRY")
        assert len(flow_meterings) == 2
        assert flow_meterings[0].find("SHORT-NAME").text == "Metering1"
        assert flow_meterings[1].find("SHORT-NAME").text == "Metering2"
        stream_filters = details_element.findall("STREAM-FILTERS/SWITCH-STREAM-FILTER-ENTRY")
        assert len(stream_filters) == 1
        assert stream_filters[0].find("SHORT-NAME").text == "Filter1"
        stream_gates = details_element.findall("STREAM-GATES/SWITCH-STREAM-GATE-ENTRY")
        assert len(stream_gates) == 1
        assert stream_gates[0].find("SHORT-NAME").text == "Gate1"
        stream_identifications = details_element.findall("SWITCH-STREAM-IDENTIFICATIONS/SWITCH-STREAM-IDENTIFICATION")
        assert len(stream_identifications) == 2
        assert stream_identifications[0].find("SHORT-NAME").text == "Stream1"
        assert stream_identifications[1].find("SHORT-NAME").text == "Stream2"
        traffic_shaper_groups = details_element.findall("TRAFFIC-SHAPER-GROUPS/SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY")
        assert len(traffic_shaper_groups) == 1
        assert traffic_shaper_groups[0].find("SHORT-NAME").text == "Group1"

    def test_bare_details_emits_no_wrappers(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        coupling_element.createCouplingElementSwitchDetails("SwitchDetails")

        details_element = self._switch_details_element(coupling_element)

        assert details_element.find("SHORT-NAME").text == "SwitchDetails"
        for tag in self.SWITCH_XSD_ORDER:
            assert details_element.find(tag) is None, tag

    def test_round_trip_field_values(self):
        coupling_element, _ = self._coupling_element_with_full_switch_details()

        parent = _write_coupling_element(coupling_element)
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        reloaded_details = reloaded.getCouplingElementDetails()
        assert isinstance(reloaded_details, CouplingElementSwitchDetails)
        assert reloaded_details.getShortName() == "SwitchDetails"
        assert [e.getShortName() for e in reloaded_details.getFlowMeterings()] == ["Metering1", "Metering2"]
        assert [e.getShortName() for e in reloaded_details.getStreamFilters()] == ["Filter1"]
        assert [e.getShortName() for e in reloaded_details.getStreamGates()] == ["Gate1"]
        assert [e.getShortName() for e in reloaded_details.getSwitchStreamIdentifications()] == ["Stream1", "Stream2"]
        assert [e.getShortName() for e in reloaded_details.getTrafficShaperGroups()] == ["Group1"]

    def test_round_trip_empty_details(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        coupling_element.createCouplingElementSwitchDetails("SwitchDetails")

        parent = _write_coupling_element(coupling_element)
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        reloaded_details = reloaded.getCouplingElementDetails()
        assert isinstance(reloaded_details, CouplingElementSwitchDetails)
        assert reloaded_details.getShortName() == "SwitchDetails"
        assert reloaded_details.getFlowMeterings() == []
        assert reloaded_details.getStreamFilters() == []
        assert reloaded_details.getStreamGates() == []
        assert reloaded_details.getSwitchStreamIdentifications() == []
        assert reloaded_details.getTrafficShaperGroups() == []


class TestSwitchStreamIdentificationRoundTrip:
    """SwitchStreamIdentification (Table 3.84, p.135) — the SWITCH-STREAM-IDENTIFICATION item of
    COUPLING-ELEMENT-SWITCH-DETAILS round-trips its seven XSD group children after the identifiable
    levels (XSD group SWITCH-STREAM-IDENTIFICATION). XML child order per XSD sequence: SHORT-NAME
    (identifiable levels), then EGRESS-PORT-REFS, FILTER-ACTION-BLOCK-SOURCE,
    FILTER-ACTION-DEST-PORT-MODIFICATION, FILTER-ACTION-DROP-FRAME,
    FILTER-ACTION-VLAN-MODIFICATION, INGRESS-PORT-REFS, STREAM-FILTER-RULE. The ref wrappers
    EGRESS-PORT-REFS/INGRESS-PORT-REFS are emitted only when non-empty."""

    STREAM_XSD_ORDER = [
        "EGRESS-PORT-REFS",
        "FILTER-ACTION-BLOCK-SOURCE",
        "FILTER-ACTION-DEST-PORT-MODIFICATION",
        "FILTER-ACTION-DROP-FRAME",
        "FILTER-ACTION-VLAN-MODIFICATION",
        "INGRESS-PORT-REFS",
        "STREAM-FILTER-RULE",
    ]

    def _coupling_element_with_full_stream_identification(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        stream_identification = details.createSwitchStreamIdentification("Stream1")
        stream_identification.addEgressPortRef(_ref("/Pkg/Switch/Cport2", "COUPLING-PORT"))
        stream_identification.addEgressPortRef(_ref("/Pkg/Switch/Cport3", "COUPLING-PORT"))
        stream_identification.setFilterActionBlockSource(Boolean().setValue(True))
        stream_identification.createFilterActionDestPortModification("DestMod")
        stream_identification.setFilterActionDropFrame(Boolean().setValue(False))
        stream_identification.setFilterActionVlanModification(PositiveInteger().setValue("10"))
        stream_identification.addIngressPortRef(_ref("/Pkg/Switch/Cport1", "COUPLING-PORT"))
        stream_identification.createStreamFilterRule("Rule1")
        return coupling_element, details, stream_identification

    def _switch_details_element(self, coupling_element):
        parent = _write_coupling_element(coupling_element)
        return parent.find("COUPLING-ELEMENT/COUPLING-ELEMENT-DETAILS/COUPLING-ELEMENT-SWITCH-DETAILS")

    def test_writes_children_in_xsd_order(self):
        coupling_element, _, _ = self._coupling_element_with_full_stream_identification()

        stream_element = self._switch_details_element(coupling_element).find("SWITCH-STREAM-IDENTIFICATIONS/SWITCH-STREAM-IDENTIFICATION")

        children = [child.tag for child in stream_element]
        assert children == ["SHORT-NAME"] + self.STREAM_XSD_ORDER

    def test_writes_field_values(self):
        coupling_element, _, _ = self._coupling_element_with_full_stream_identification()

        stream_element = self._switch_details_element(coupling_element).find("SWITCH-STREAM-IDENTIFICATIONS/SWITCH-STREAM-IDENTIFICATION")

        assert stream_element.find("SHORT-NAME").text == "Stream1"
        egress_port_refs = stream_element.findall("EGRESS-PORT-REFS/EGRESS-PORT-REF")
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0].text == "/Pkg/Switch/Cport2"
        assert egress_port_refs[0].attrib["DEST"] == "COUPLING-PORT"
        assert egress_port_refs[1].text == "/Pkg/Switch/Cport3"
        assert stream_element.find("FILTER-ACTION-BLOCK-SOURCE").text == "true"
        modification_element = stream_element.find("FILTER-ACTION-DEST-PORT-MODIFICATION")
        assert modification_element is not None
        assert modification_element.find("SHORT-NAME").text == "DestMod"
        assert stream_element.find("FILTER-ACTION-DROP-FRAME").text == "false"
        assert stream_element.find("FILTER-ACTION-VLAN-MODIFICATION").text == "10"
        ingress_port_refs = stream_element.findall("INGRESS-PORT-REFS/INGRESS-PORT-REF")
        assert len(ingress_port_refs) == 1
        assert ingress_port_refs[0].text == "/Pkg/Switch/Cport1"
        assert ingress_port_refs[0].attrib["DEST"] == "COUPLING-PORT"
        rule_element = stream_element.find("STREAM-FILTER-RULE")
        assert rule_element is not None
        assert rule_element.find("SHORT-NAME").text == "Rule1"

    def test_bare_stream_identification_emits_no_children(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        details.createSwitchStreamIdentification("Stream1")

        stream_element = self._switch_details_element(coupling_element).find("SWITCH-STREAM-IDENTIFICATIONS/SWITCH-STREAM-IDENTIFICATION")

        assert stream_element.find("SHORT-NAME").text == "Stream1"
        for tag in self.STREAM_XSD_ORDER:
            assert stream_element.find(tag) is None, tag

    def test_round_trip_field_values(self):
        coupling_element, _, _ = self._coupling_element_with_full_stream_identification()

        parent = _write_coupling_element(coupling_element)
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        reloaded_stream = reloaded.getCouplingElementDetails().getSwitchStreamIdentifications()[0]
        assert reloaded_stream.getShortName() == "Stream1"
        egress_port_refs = reloaded_stream.getEgressPortRefs()
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0].getValue() == "/Pkg/Switch/Cport2"
        assert egress_port_refs[0].getDest() == "COUPLING-PORT"
        assert egress_port_refs[1].getValue() == "/Pkg/Switch/Cport3"
        assert reloaded_stream.getFilterActionBlockSource().getValue() is True
        assert reloaded_stream.getFilterActionDestPortModification().getShortName() == "DestMod"
        assert reloaded_stream.getFilterActionDropFrame().getValue() is False
        assert reloaded_stream.getFilterActionVlanModification().getValue() == 10
        ingress_port_refs = reloaded_stream.getIngressPortRefs()
        assert len(ingress_port_refs) == 1
        assert ingress_port_refs[0].getValue() == "/Pkg/Switch/Cport1"
        assert reloaded_stream.getStreamFilterRule().getShortName() == "Rule1"

    def test_round_trip_bare_stream_identification(self):
        coupling_element = CouplingElement(_pkg(), "Switch")
        details = coupling_element.createCouplingElementSwitchDetails("SwitchDetails")
        details.createSwitchStreamIdentification("Stream1")

        parent = _write_coupling_element(coupling_element)
        reloaded = CouplingElement(_pkg(), "Switch")
        ARXMLParser().readCouplingElement(_namespaced_first_child(parent), reloaded)

        reloaded_stream = reloaded.getCouplingElementDetails().getSwitchStreamIdentifications()[0]
        assert reloaded_stream.getShortName() == "Stream1"
        assert reloaded_stream.getEgressPortRefs() == []
        assert reloaded_stream.getFilterActionBlockSource() is None
        assert reloaded_stream.getFilterActionDestPortModification() is None
        assert reloaded_stream.getFilterActionDropFrame() is None
        assert reloaded_stream.getFilterActionVlanModification() is None
        assert reloaded_stream.getIngressPortRefs() == []
        assert reloaded_stream.getStreamFilterRule() is None
