"""
Tests for parsing COUPLING-ELEMENT elements (CouplingElement, Table 3.52, p.108).

Round-trip counterpart: tests/test_armodel/writer/test_coupling_element.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    SwitchAsynchronousTrafficShaperGroupEntry,
    SwitchFlowMeteringEntry,
    SwitchStreamFilterActionDestPortModification,
    SwitchStreamFilterEntry,
    SwitchStreamFilterRule,
    SwitchStreamGateEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElement,
    CouplingElementAbstractDetails,
    CouplingElementEnum,
    CouplingElementSwitchDetails,
    CouplingPort,
    SwitchStreamIdentification,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _make_coupling_element() -> CouplingElement:
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createCouplingElement("Switch")


class TestReadCouplingElement:
    """Test readCouplingElement (CouplingElement, Table 3.52)."""

    def test_read_all_members(self, parser):
        """Every COUPLING-ELEMENT group element populates its model field."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COMMUNICATION-CLUSTER-REF DEST="ETHERNET-CLUSTER">/AUTOSAR/EthernetClusters/Cluster</COMMUNICATION-CLUSTER-REF>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
                <COUPLING-PORTS>
                    <COUPLING-PORT>
                        <SHORT-NAME>Cport1</SHORT-NAME>
                    </COUPLING-PORT>
                    <COUPLING-PORT>
                        <SHORT-NAME>Cport2</SHORT-NAME>
                    </COUPLING-PORT>
                </COUPLING-PORTS>
                <COUPLING-TYPE>SWITCH</COUPLING-TYPE>
                <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/Ecus/Ecu1</ECU-INSTANCE-REF>
                <FIREWALL-RULE-REFS>
                    <FIREWALL-RULE-REF DEST="STATE-DEPENDENT-FIREWALL">/AUTOSAR/Firewalls/Rule1</FIREWALL-RULE-REF>
                    <FIREWALL-RULE-REF DEST="STATE-DEPENDENT-FIREWALL">/AUTOSAR/Firewalls/Rule2</FIREWALL-RULE-REF>
                </FIREWALL-RULE-REFS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        assert coupling_element.getShortName() == "Switch"
        assert coupling_element.getCommunicationClusterRef() is not None
        assert coupling_element.getCommunicationClusterRef().getDest() == "ETHERNET-CLUSTER"
        assert coupling_element.getCommunicationClusterRef().getValue() == "/AUTOSAR/EthernetClusters/Cluster"

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert isinstance(details, CouplingElementAbstractDetails)
        assert details.getShortName() == "SwitchDetails"

        ports = coupling_element.getCouplingPorts()
        assert len(ports) == 2
        assert isinstance(ports[0], CouplingPort)
        assert ports[0].getShortName() == "Cport1"
        assert ports[1].getShortName() == "Cport2"

        assert coupling_element.getCouplingType() is not None
        assert coupling_element.getCouplingType().getValue() == CouplingElementEnum.SWITCH

        assert coupling_element.getEcuInstanceRef() is not None
        assert coupling_element.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert coupling_element.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecus/Ecu1"

        firewall_rule_refs = coupling_element.getFirewallRuleRefs()
        assert len(firewall_rule_refs) == 2
        assert firewall_rule_refs[0].getDest() == "STATE-DEPENDENT-FIREWALL"
        assert firewall_rule_refs[0].getValue() == "/AUTOSAR/Firewalls/Rule1"
        assert firewall_rule_refs[1].getValue() == "/AUTOSAR/Firewalls/Rule2"

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty-wrapper case)."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        assert coupling_element.getCommunicationClusterRef() is None
        assert coupling_element.getCouplingElementDetails() is None
        assert coupling_element.getCouplingPorts() == []
        assert coupling_element.getCouplingType() is None
        assert coupling_element.getEcuInstanceRef() is None
        assert coupling_element.getFirewallRuleRefs() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a COUPLING-ELEMENT."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <COUPLING-ELEMENT>
                    <SHORT-NAME>Router</SHORT-NAME>
                    <COMMUNICATION-CLUSTER-REF DEST="ETHERNET-CLUSTER">/AUTOSAR/Cluster</COMMUNICATION-CLUSTER-REF>
                    <COUPLING-TYPE>ROUTER</COUPLING-TYPE>
                    <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/Ecu1</ECU-INSTANCE-REF>
                </COUPLING-ELEMENT>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            coupling_elements = [e for e in pkg.getReferrableElements() if isinstance(e, CouplingElement)]
            assert len(coupling_elements) == 1
            assert coupling_elements[0].getShortName() == "Router"
            assert coupling_elements[0].getCommunicationClusterRef().getValue() == "/AUTOSAR/Cluster"
            assert coupling_elements[0].getCouplingType().getValue() == CouplingElementEnum.ROUTER
            assert coupling_elements[0].getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
            assert coupling_elements[0].getFirewallRuleRefs() == []
        finally:
            os.remove(file_path)


class TestReadCouplingElementAbstractDetails:
    """Test the CouplingElementAbstractDetails abstract level inside COUPLING-ELEMENT-DETAILS
    (CouplingElementAbstractDetails, Table 3.82, p.133): the identifiable levels plus the
    VARIATION-POINT group child of COUPLING-ELEMENT-ABSTRACT-DETAILS."""

    def test_read_identifiable_levels_and_variation_point(self, parser):
        """Identity levels and the abstract-level VARIATION-POINT populate the details object."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS UUID="DCE:2fac1234-31f8-11b4-a222-08002b34c003">
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                        <CATEGORY>myCategory</CATEGORY>
                        <VARIATION-POINT>
                            <SHORT-LABEL>vpLabel</SHORT-LABEL>
                        </VARIATION-POINT>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert isinstance(details, CouplingElementAbstractDetails)
        assert details.getShortName() == "SwitchDetails"
        assert details.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert details.getCategory().getValue() == "myCategory"
        assert details.getVariationPoint() is not None
        assert details.getVariationPoint().getShortLabel().getValue() == "vpLabel"

    def test_read_details_without_variation_point(self, parser):
        """A details item without a VARIATION-POINT child leaves the variation point unset (empty-wrapper case)."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert details.getShortName() == "SwitchDetails"
        assert details.getVariationPoint() is None


class TestReadCouplingElementSwitchDetails:
    """Test readCouplingElementSwitchDetails (CouplingElementSwitchDetails, Table 3.83, p.133):
    the five XSD group children of COUPLING-ELEMENT-SWITCH-DETAILS after the abstract level —
    FLOW-METERINGS, STREAM-FILTERS, STREAM-GATES, SWITCH-STREAM-IDENTIFICATIONS,
    TRAFFIC-SHAPER-GROUPS (XSD group COUPLING-ELEMENT-SWITCH-DETAILS)."""

    def test_read_all_five_wrappers(self, parser):
        """Every wrapper populates its model list field, in document order."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                        <FLOW-METERINGS>
                            <SWITCH-FLOW-METERING-ENTRY>
                                <SHORT-NAME>Metering1</SHORT-NAME>
                            </SWITCH-FLOW-METERING-ENTRY>
                            <SWITCH-FLOW-METERING-ENTRY>
                                <SHORT-NAME>Metering2</SHORT-NAME>
                            </SWITCH-FLOW-METERING-ENTRY>
                        </FLOW-METERINGS>
                        <STREAM-FILTERS>
                            <SWITCH-STREAM-FILTER-ENTRY>
                                <SHORT-NAME>Filter1</SHORT-NAME>
                            </SWITCH-STREAM-FILTER-ENTRY>
                        </STREAM-FILTERS>
                        <STREAM-GATES>
                            <SWITCH-STREAM-GATE-ENTRY>
                                <SHORT-NAME>Gate1</SHORT-NAME>
                            </SWITCH-STREAM-GATE-ENTRY>
                        </STREAM-GATES>
                        <SWITCH-STREAM-IDENTIFICATIONS>
                            <SWITCH-STREAM-IDENTIFICATION>
                                <SHORT-NAME>Stream1</SHORT-NAME>
                            </SWITCH-STREAM-IDENTIFICATION>
                            <SWITCH-STREAM-IDENTIFICATION>
                                <SHORT-NAME>Stream2</SHORT-NAME>
                            </SWITCH-STREAM-IDENTIFICATION>
                        </SWITCH-STREAM-IDENTIFICATIONS>
                        <TRAFFIC-SHAPER-GROUPS>
                            <SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY>
                                <SHORT-NAME>Group1</SHORT-NAME>
                            </SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY>
                        </TRAFFIC-SHAPER-GROUPS>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)

        flow_meterings = details.getFlowMeterings()
        assert len(flow_meterings) == 2
        assert isinstance(flow_meterings[0], SwitchFlowMeteringEntry)
        assert flow_meterings[0].getShortName() == "Metering1"
        assert flow_meterings[1].getShortName() == "Metering2"

        stream_filters = details.getStreamFilters()
        assert len(stream_filters) == 1
        assert isinstance(stream_filters[0], SwitchStreamFilterEntry)
        assert stream_filters[0].getShortName() == "Filter1"

        stream_gates = details.getStreamGates()
        assert len(stream_gates) == 1
        assert isinstance(stream_gates[0], SwitchStreamGateEntry)
        assert stream_gates[0].getShortName() == "Gate1"

        stream_identifications = details.getSwitchStreamIdentifications()
        assert len(stream_identifications) == 2
        assert isinstance(stream_identifications[0], SwitchStreamIdentification)
        assert stream_identifications[0].getShortName() == "Stream1"
        assert stream_identifications[1].getShortName() == "Stream2"

        traffic_shaper_groups = details.getTrafficShaperGroups()
        assert len(traffic_shaper_groups) == 1
        assert isinstance(traffic_shaper_groups[0], SwitchAsynchronousTrafficShaperGroupEntry)
        assert traffic_shaper_groups[0].getShortName() == "Group1"

    def test_read_wrappers_with_variation_point_and_category(self, parser):
        """The abstract level (identity levels + VARIATION-POINT) and the switch-level wrappers
        populate the same details object."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                        <CATEGORY>myCategory</CATEGORY>
                        <VARIATION-POINT>
                            <SHORT-LABEL>vpLabel</SHORT-LABEL>
                        </VARIATION-POINT>
                        <SWITCH-STREAM-IDENTIFICATIONS>
                            <SWITCH-STREAM-IDENTIFICATION>
                                <SHORT-NAME>Stream1</SHORT-NAME>
                            </SWITCH-STREAM-IDENTIFICATION>
                        </SWITCH-STREAM-IDENTIFICATIONS>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert details.getCategory().getValue() == "myCategory"
        assert details.getVariationPoint() is not None
        assert details.getVariationPoint().getShortLabel().getValue() == "vpLabel"
        assert [e.getShortName() for e in details.getSwitchStreamIdentifications()] == ["Stream1"]
        assert details.getFlowMeterings() == []
        assert details.getStreamFilters() == []
        assert details.getStreamGates() == []
        assert details.getTrafficShaperGroups() == []

    def test_read_without_wrapper_children(self, parser):
        """A details item without any switch-level wrapper leaves all list fields empty (empty-wrapper case)."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert details.getFlowMeterings() == []
        assert details.getStreamFilters() == []
        assert details.getStreamGates() == []
        assert details.getSwitchStreamIdentifications() == []
        assert details.getTrafficShaperGroups() == []


class TestReadSwitchStreamIdentification:
    """Test readSwitchStreamIdentification (SwitchStreamIdentification, Table 3.84, p.135):
    the seven XSD group children of SWITCH-STREAM-IDENTIFICATION after the identifiable levels —
    EGRESS-PORT-REFS, FILTER-ACTION-BLOCK-SOURCE, FILTER-ACTION-DEST-PORT-MODIFICATION,
    FILTER-ACTION-DROP-FRAME, FILTER-ACTION-VLAN-MODIFICATION, INGRESS-PORT-REFS,
    STREAM-FILTER-RULE (XSD group SWITCH-STREAM-IDENTIFICATION). The reader dispatch of
    readCouplingElementSwitchDetails for the SWITCH-STREAM-IDENTIFICATION item calls this level."""

    def test_read_all_members(self, parser):
        """Every XSD group child populates its model field, in document order."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                        <SWITCH-STREAM-IDENTIFICATIONS>
                            <SWITCH-STREAM-IDENTIFICATION>
                                <SHORT-NAME>Stream1</SHORT-NAME>
                                <EGRESS-PORT-REFS>
                                    <EGRESS-PORT-REF DEST="COUPLING-PORT">/AUTOSAR/Switch/Cport2</EGRESS-PORT-REF>
                                    <EGRESS-PORT-REF DEST="COUPLING-PORT">/AUTOSAR/Switch/Cport3</EGRESS-PORT-REF>
                                </EGRESS-PORT-REFS>
                                <FILTER-ACTION-BLOCK-SOURCE>true</FILTER-ACTION-BLOCK-SOURCE>
                                <FILTER-ACTION-DEST-PORT-MODIFICATION>
                                    <SHORT-NAME>DestMod</SHORT-NAME>
                                </FILTER-ACTION-DEST-PORT-MODIFICATION>
                                <FILTER-ACTION-DROP-FRAME>false</FILTER-ACTION-DROP-FRAME>
                                <FILTER-ACTION-VLAN-MODIFICATION>10</FILTER-ACTION-VLAN-MODIFICATION>
                                <INGRESS-PORT-REFS>
                                    <INGRESS-PORT-REF DEST="COUPLING-PORT">/AUTOSAR/Switch/Cport1</INGRESS-PORT-REF>
                                </INGRESS-PORT-REFS>
                                <STREAM-FILTER-RULE>
                                    <SHORT-NAME>Rule1</SHORT-NAME>
                                </STREAM-FILTER-RULE>
                            </SWITCH-STREAM-IDENTIFICATION>
                        </SWITCH-STREAM-IDENTIFICATIONS>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        details = coupling_element.getCouplingElementDetails()
        stream_identifications = details.getSwitchStreamIdentifications()
        assert len(stream_identifications) == 1
        stream_identification = stream_identifications[0]
        assert isinstance(stream_identification, SwitchStreamIdentification)
        assert stream_identification.getShortName() == "Stream1"

        egress_port_refs = stream_identification.getEgressPortRefs()
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0].getValue() == "/AUTOSAR/Switch/Cport2"
        assert egress_port_refs[0].getDest() == "COUPLING-PORT"
        assert egress_port_refs[1].getValue() == "/AUTOSAR/Switch/Cport3"

        assert stream_identification.getFilterActionBlockSource() is not None
        assert stream_identification.getFilterActionBlockSource().getValue() is True

        modification = stream_identification.getFilterActionDestPortModification()
        assert isinstance(modification, SwitchStreamFilterActionDestPortModification)
        assert modification.getShortName() == "DestMod"

        assert stream_identification.getFilterActionDropFrame() is not None
        assert stream_identification.getFilterActionDropFrame().getValue() is False

        assert stream_identification.getFilterActionVlanModification() is not None
        assert stream_identification.getFilterActionVlanModification().getValue() == 10

        ingress_port_refs = stream_identification.getIngressPortRefs()
        assert len(ingress_port_refs) == 1
        assert ingress_port_refs[0].getValue() == "/AUTOSAR/Switch/Cport1"
        assert ingress_port_refs[0].getDest() == "COUPLING-PORT"

        rule = stream_identification.getStreamFilterRule()
        assert isinstance(rule, SwitchStreamFilterRule)
        assert rule.getShortName() == "Rule1"

    def test_read_absent_optional_members(self, parser):
        """A bare SWITCH-STREAM-IDENTIFICATION item leaves all fields unset (empty-wrapper case)."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                        <SWITCH-STREAM-IDENTIFICATIONS>
                            <SWITCH-STREAM-IDENTIFICATION>
                                <SHORT-NAME>Stream1</SHORT-NAME>
                            </SWITCH-STREAM-IDENTIFICATION>
                        </SWITCH-STREAM-IDENTIFICATIONS>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        stream_identification = coupling_element.getCouplingElementDetails().getSwitchStreamIdentifications()[0]
        assert stream_identification.getShortName() == "Stream1"
        assert stream_identification.getEgressPortRefs() == []
        assert stream_identification.getFilterActionBlockSource() is None
        assert stream_identification.getFilterActionDestPortModification() is None
        assert stream_identification.getFilterActionDropFrame() is None
        assert stream_identification.getFilterActionVlanModification() is None
        assert stream_identification.getIngressPortRefs() == []
        assert stream_identification.getStreamFilterRule() is None
