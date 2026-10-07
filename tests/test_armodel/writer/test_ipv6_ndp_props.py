"""
Writer/reader round-trip tests for Ipv6NdpProps (Table 3.108, p.151).

XML element order per XSD IPV-6-NDP-PROPS group (emitted as the NDP-PROPS element —
the instance tag under IPV-6-PROPS; the XSD type is AR:IPV-6-NDP-PROPS):
TCP-IP-NDP-DEFAULT-REACHABLE-TIME ... TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED
(unwrapped direct children; the removed TCP-IP-NDP-DELAY-FIRST-PROBE-TIME element is
not modeled — atp.Status="removed").
writeIpv6Props dispatches NDP-PROPS to writeIpv6NdpProps since the Ipv6NdpProps sync
(Table 3.108) — the child is fully serialized, no longer identity-only.
writeIpv6NdpProps calls writeARObject on the NDP-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6NdpProps, Ipv6Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-NDP-DEFAULT-REACHABLE-TIME",
    "TCP-IP-NDP-DEFAULT-RETRANS-TIMER",
    "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE",
    "TCP-IP-NDP-DEFENSIVE-PROCESSING",
    "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE",
    "TCP-IP-NDP-DESTINATION-CACHE-SIZE",
    "TCP-IP-NDP-DYNAMIC-HOP-LIMIT-ENABLED",
    "TCP-IP-NDP-DYNAMIC-MTU-ENABLED",
    "TCP-IP-NDP-DYNAMIC-REACHABLE-TIME-ENABLED",
    "TCP-IP-NDP-DYNAMIC-RETRANS-TIME-ENABLED",
    "TCP-IP-NDP-MAX-RANDOM-FACTOR",
    "TCP-IP-NDP-MAX-RTR-SOLICITATION-DELAY",
    "TCP-IP-NDP-MAX-RTR-SOLICITATIONS",
    "TCP-IP-NDP-MIN-RANDOM-FACTOR",
    "TCP-IP-NDP-NEIGHBOR-UNREACHABILITY-DETECTION-ENABLED",
    "TCP-IP-NDP-NUM-MULTICAST-SOLICITATIONS",
    "TCP-IP-NDP-NUM-UNICAST-SOLICITATIONS",
    "TCP-IP-NDP-PACKET-QUEUE-ENABLED",
    "TCP-IP-NDP-PREFIX-LIST-SIZE",
    "TCP-IP-NDP-RANDOM-REACHABLE-TIME-ENABLED",
    "TCP-IP-NDP-RND-RTR-SOLICITATION-DELAY-ENABLED",
    "TCP-IP-NDP-RTR-SOLICITATION-INTERVAL",
    "TCP-IP-NDP-SLAAC-DAD-NUMBER-OF-TRANSMISSIONS",
    "TCP-IP-NDP-SLAAC-DAD-RETRANSMISSION-DELAY",
    "TCP-IP-NDP-SLAAC-DELAY-ENABLED",
    "TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv6_ndp_props():
    props = Ipv6NdpProps()
    props.setTcpIpNdpDefaultReachableTime(TimeValue().setValue(1.5))
    props.setTcpIpNdpDefaultRetransTimer(TimeValue().setValue(1.5))
    props.setTcpIpNdpDefaultRouterListSize(PositiveInteger().setValue(4))
    props.setTcpIpNdpDefensiveProcessing(Boolean().setValue(True))
    props.setTcpIpNdpDelayFirstProbeTimeValue(TimeValue().setValue(1.5))
    props.setTcpIpNdpDestinationCacheSize(PositiveInteger().setValue(4))
    props.setTcpIpNdpDynamicHopLimitEnabled(Boolean().setValue(True))
    props.setTcpIpNdpDynamicMtuEnabled(Boolean().setValue(True))
    props.setTcpIpNdpDynamicReachableTimeEnabled(Boolean().setValue(True))
    props.setTcpIpNdpDynamicRetransTimeEnabled(Boolean().setValue(True))
    props.setTcpIpNdpMaxRandomFactor(PositiveInteger().setValue(4))
    props.setTcpIpNdpMaxRtrSolicitationDelay(TimeValue().setValue(1.5))
    props.setTcpIpNdpMaxRtrSolicitations(PositiveInteger().setValue(4))
    props.setTcpIpNdpMinRandomFactor(PositiveInteger().setValue(4))
    props.setTcpIpNdpNeighborUnreachabilityDetectionEnabled(Boolean().setValue(True))
    props.setTcpIpNdpNumMulticastSolicitations(PositiveInteger().setValue(4))
    props.setTcpIpNdpNumUnicastSolicitations(PositiveInteger().setValue(4))
    props.setTcpIpNdpPacketQueueEnabled(Boolean().setValue(True))
    props.setTcpIpNdpPrefixListSize(PositiveInteger().setValue(4))
    props.setTcpIpNdpRandomReachableTimeEnabled(Boolean().setValue(True))
    props.setTcpIpNdpRndRtrSolicitationDelayEnabled(Boolean().setValue(True))
    props.setTcpIpNdpRtrSolicitationInterval(TimeValue().setValue(1.5))
    props.setTcpIpNdpSlaacDadNumberOfTransmissions(PositiveInteger().setValue(4))
    props.setTcpIpNdpSlaacDadRetransmissionDelay(TimeValue().setValue(1.5))
    props.setTcpIpNdpSlaacDelayEnabled(Boolean().setValue(True))
    props.setTcpIpNdpSlaacOptimisticDadEnabled(Boolean().setValue(True))
    return props


def _write_ipv6_ndp_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv6NdpProps(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv6NdpProps:
    def test_members_in_xsd_order(self):
        parent = _write_ipv6_ndp_props(_full_ipv6_ndp_props())
        ndp_props = parent.find("NDP-PROPS")

        children = [child.tag for child in ndp_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_ipv6_ndp_props(_full_ipv6_ndp_props())
        ndp_props = parent.find("NDP-PROPS")

        assert ndp_props.find("TCP-IP-NDP-DEFAULT-REACHABLE-TIME").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-DEFAULT-RETRANS-TIMER").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE").text == "4"
        assert ndp_props.find("TCP-IP-NDP-DEFENSIVE-PROCESSING").text == "true"
        assert ndp_props.find("TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-DESTINATION-CACHE-SIZE").text == "4"
        assert ndp_props.find("TCP-IP-NDP-DYNAMIC-HOP-LIMIT-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-DYNAMIC-MTU-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-DYNAMIC-REACHABLE-TIME-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-DYNAMIC-RETRANS-TIME-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-MAX-RANDOM-FACTOR").text == "4"
        assert ndp_props.find("TCP-IP-NDP-MAX-RTR-SOLICITATION-DELAY").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-MAX-RTR-SOLICITATIONS").text == "4"
        assert ndp_props.find("TCP-IP-NDP-MIN-RANDOM-FACTOR").text == "4"
        assert ndp_props.find("TCP-IP-NDP-NEIGHBOR-UNREACHABILITY-DETECTION-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-NUM-MULTICAST-SOLICITATIONS").text == "4"
        assert ndp_props.find("TCP-IP-NDP-NUM-UNICAST-SOLICITATIONS").text == "4"
        assert ndp_props.find("TCP-IP-NDP-PACKET-QUEUE-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-PREFIX-LIST-SIZE").text == "4"
        assert ndp_props.find("TCP-IP-NDP-RANDOM-REACHABLE-TIME-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-RND-RTR-SOLICITATION-DELAY-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-RTR-SOLICITATION-INTERVAL").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-SLAAC-DAD-NUMBER-OF-TRANSMISSIONS").text == "4"
        assert ndp_props.find("TCP-IP-NDP-SLAAC-DAD-RETRANSMISSION-DELAY").text == "1.5"
        assert ndp_props.find("TCP-IP-NDP-SLAAC-DELAY-ENABLED").text == "true"
        assert ndp_props.find("TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED").text == "true"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_ipv6_ndp_props(Ipv6NdpProps())
        ndp_props = parent.find("NDP-PROPS")

        assert len(list(ndp_props)) == 0

    def test_checksum_emitted(self):
        props = Ipv6NdpProps()
        checksum = String()
        checksum.setValue("789")
        props.setChecksum(checksum)
        parent = _write_ipv6_ndp_props(props)

        assert parent.find("NDP-PROPS").attrib.get("S") == "789"


class TestIpv6NdpPropsRoundTrip:
    def test_round_trip_full_through_ndp_props(self):
        parent = _write_ipv6_ndp_props(_full_ipv6_ndp_props())
        reloaded = Ipv6NdpProps()
        ARXMLParser().readIpv6NdpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpNdpDefaultReachableTime().getValue() == 1.5
        assert reloaded.getTcpIpNdpDefaultRetransTimer().getValue() == 1.5
        assert reloaded.getTcpIpNdpDefaultRouterListSize().getValue() == 4
        assert reloaded.getTcpIpNdpDefensiveProcessing().getValue() is True
        assert reloaded.getTcpIpNdpDelayFirstProbeTimeValue().getValue() == 1.5
        assert reloaded.getTcpIpNdpDestinationCacheSize().getValue() == 4
        assert reloaded.getTcpIpNdpDynamicHopLimitEnabled().getValue() is True
        assert reloaded.getTcpIpNdpDynamicMtuEnabled().getValue() is True
        assert reloaded.getTcpIpNdpDynamicReachableTimeEnabled().getValue() is True
        assert reloaded.getTcpIpNdpDynamicRetransTimeEnabled().getValue() is True
        assert reloaded.getTcpIpNdpMaxRandomFactor().getValue() == 4
        assert reloaded.getTcpIpNdpMaxRtrSolicitationDelay().getValue() == 1.5
        assert reloaded.getTcpIpNdpMaxRtrSolicitations().getValue() == 4
        assert reloaded.getTcpIpNdpMinRandomFactor().getValue() == 4
        assert reloaded.getTcpIpNdpNeighborUnreachabilityDetectionEnabled().getValue() is True
        assert reloaded.getTcpIpNdpNumMulticastSolicitations().getValue() == 4
        assert reloaded.getTcpIpNdpNumUnicastSolicitations().getValue() == 4
        assert reloaded.getTcpIpNdpPacketQueueEnabled().getValue() is True
        assert reloaded.getTcpIpNdpPrefixListSize().getValue() == 4
        assert reloaded.getTcpIpNdpRandomReachableTimeEnabled().getValue() is True
        assert reloaded.getTcpIpNdpRndRtrSolicitationDelayEnabled().getValue() is True
        assert reloaded.getTcpIpNdpRtrSolicitationInterval().getValue() == 1.5
        assert reloaded.getTcpIpNdpSlaacDadNumberOfTransmissions().getValue() == 4
        assert reloaded.getTcpIpNdpSlaacDadRetransmissionDelay().getValue() == 1.5
        assert reloaded.getTcpIpNdpSlaacDelayEnabled().getValue() is True
        assert reloaded.getTcpIpNdpSlaacOptimisticDadEnabled().getValue() is True

    def test_round_trip_empty_through_ndp_props(self):
        parent = _write_ipv6_ndp_props(Ipv6NdpProps())
        reloaded = Ipv6NdpProps()
        ARXMLParser().readIpv6NdpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpNdpDefaultReachableTime() is None
        assert reloaded.getTcpIpNdpDefaultRetransTimer() is None
        assert reloaded.getTcpIpNdpDefaultRouterListSize() is None
        assert reloaded.getTcpIpNdpDefensiveProcessing() is None
        assert reloaded.getTcpIpNdpDelayFirstProbeTimeValue() is None
        assert reloaded.getTcpIpNdpDestinationCacheSize() is None
        assert reloaded.getTcpIpNdpDynamicHopLimitEnabled() is None
        assert reloaded.getTcpIpNdpDynamicMtuEnabled() is None
        assert reloaded.getTcpIpNdpDynamicReachableTimeEnabled() is None
        assert reloaded.getTcpIpNdpDynamicRetransTimeEnabled() is None
        assert reloaded.getTcpIpNdpMaxRandomFactor() is None
        assert reloaded.getTcpIpNdpMaxRtrSolicitationDelay() is None
        assert reloaded.getTcpIpNdpMaxRtrSolicitations() is None
        assert reloaded.getTcpIpNdpMinRandomFactor() is None
        assert reloaded.getTcpIpNdpNeighborUnreachabilityDetectionEnabled() is None
        assert reloaded.getTcpIpNdpNumMulticastSolicitations() is None
        assert reloaded.getTcpIpNdpNumUnicastSolicitations() is None
        assert reloaded.getTcpIpNdpPacketQueueEnabled() is None
        assert reloaded.getTcpIpNdpPrefixListSize() is None
        assert reloaded.getTcpIpNdpRandomReachableTimeEnabled() is None
        assert reloaded.getTcpIpNdpRndRtrSolicitationDelayEnabled() is None
        assert reloaded.getTcpIpNdpRtrSolicitationInterval() is None
        assert reloaded.getTcpIpNdpSlaacDadNumberOfTransmissions() is None
        assert reloaded.getTcpIpNdpSlaacDadRetransmissionDelay() is None
        assert reloaded.getTcpIpNdpSlaacDelayEnabled() is None
        assert reloaded.getTcpIpNdpSlaacOptimisticDadEnabled() is None

    def test_round_trip_full_through_ipv6_props_dispatch(self):
        """The upgraded Ipv6Props dispatch fully round-trips the NDP-PROPS child."""
        ipv6_props = Ipv6Props()
        ipv6_props.setNdpProps(_full_ipv6_ndp_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv6Props(parent, ipv6_props)

        ndp_props_element = parent.find("IPV-6-PROPS/NDP-PROPS")
        xml_text = ET.tostring(parent.find("IPV-6-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-6-PROPS", "IPV-6-PROPS xmlns='%s'" % NS, 1))

        assert ndp_props_element.find("TCP-IP-NDP-DEFAULT-REACHABLE-TIME").text == "1.5"
        assert ndp_props_element.find("TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED").text == "true"

        reloaded = Ipv6Props()
        ARXMLParser().readIpv6Props(namespaced, reloaded)
        reloaded_ndp = reloaded.getNdpProps()
        assert isinstance(reloaded_ndp, Ipv6NdpProps)
        assert reloaded_ndp.getTcpIpNdpDefaultReachableTime().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpDefensiveProcessing().getValue() is True
        assert reloaded_ndp.getTcpIpNdpMaxRtrSolicitations().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpRtrSolicitationInterval().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpSlaacOptimisticDadEnabled().getValue() is True

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv6_props = Ipv6Props()
        ipv6_props.setNdpProps(_full_ipv6_ndp_props())
        eth_ip_props.setIpv6Props(ipv6_props)

        out_file = str(tmp_path / "ipv6_ndp_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_ndp = reloaded_eth_ip_props.getIpv6Props().getNdpProps()
        assert isinstance(reloaded_ndp, Ipv6NdpProps)
        assert reloaded_ndp.getTcpIpNdpDefaultReachableTime().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpDefaultRetransTimer().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpDefaultRouterListSize().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpDefensiveProcessing().getValue() is True
        assert reloaded_ndp.getTcpIpNdpDelayFirstProbeTimeValue().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpDestinationCacheSize().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpDynamicHopLimitEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpDynamicMtuEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpDynamicReachableTimeEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpDynamicRetransTimeEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpMaxRandomFactor().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpMaxRtrSolicitationDelay().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpMaxRtrSolicitations().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpMinRandomFactor().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpNeighborUnreachabilityDetectionEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpNumMulticastSolicitations().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpNumUnicastSolicitations().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpPacketQueueEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpPrefixListSize().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpRandomReachableTimeEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpRndRtrSolicitationDelayEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpRtrSolicitationInterval().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpSlaacDadNumberOfTransmissions().getValue() == 4
        assert reloaded_ndp.getTcpIpNdpSlaacDadRetransmissionDelay().getValue() == 1.5
        assert reloaded_ndp.getTcpIpNdpSlaacDelayEnabled().getValue() is True
        assert reloaded_ndp.getTcpIpNdpSlaacOptimisticDadEnabled().getValue() is True
