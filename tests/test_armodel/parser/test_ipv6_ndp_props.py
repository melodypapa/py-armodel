"""
Tests for parsing NDP-PROPS elements (Ipv6NdpProps, Table 3.108, p.151).

The instance element is <NDP-PROPS> (XSD type AR:IPV-6-NDP-PROPS; IPV-6-NDP-PROPS
group contents) — the type name is the XSD group/complexType name only, the instance
tag under IPV-6-PROPS stays NDP-PROPS.
Round-trip counterpart: tests/test_armodel/writer/test_ipv6_ndp_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6NdpProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadIpv6NdpProps:
    """Test readIpv6NdpProps (Ipv6NdpProps, Table 3.108)."""

    def test_read_all_members(self, parser):
        """Every IPV-6-NDP-PROPS group element populates its model field with its value."""
        props = Ipv6NdpProps()
        element = ET.fromstring(
            f"""<NDP-PROPS xmlns='{NS}'>
                <TCP-IP-NDP-DEFAULT-REACHABLE-TIME>1.5</TCP-IP-NDP-DEFAULT-REACHABLE-TIME>
                <TCP-IP-NDP-DEFAULT-RETRANS-TIMER>1.5</TCP-IP-NDP-DEFAULT-RETRANS-TIMER>
                <TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE>4</TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE>
                <TCP-IP-NDP-DEFENSIVE-PROCESSING>true</TCP-IP-NDP-DEFENSIVE-PROCESSING>
                <TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE>1.5</TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE>
                <TCP-IP-NDP-DESTINATION-CACHE-SIZE>4</TCP-IP-NDP-DESTINATION-CACHE-SIZE>
                <TCP-IP-NDP-DYNAMIC-HOP-LIMIT-ENABLED>true</TCP-IP-NDP-DYNAMIC-HOP-LIMIT-ENABLED>
                <TCP-IP-NDP-DYNAMIC-MTU-ENABLED>true</TCP-IP-NDP-DYNAMIC-MTU-ENABLED>
                <TCP-IP-NDP-DYNAMIC-REACHABLE-TIME-ENABLED>true</TCP-IP-NDP-DYNAMIC-REACHABLE-TIME-ENABLED>
                <TCP-IP-NDP-DYNAMIC-RETRANS-TIME-ENABLED>true</TCP-IP-NDP-DYNAMIC-RETRANS-TIME-ENABLED>
                <TCP-IP-NDP-MAX-RANDOM-FACTOR>4</TCP-IP-NDP-MAX-RANDOM-FACTOR>
                <TCP-IP-NDP-MAX-RTR-SOLICITATION-DELAY>1.5</TCP-IP-NDP-MAX-RTR-SOLICITATION-DELAY>
                <TCP-IP-NDP-MAX-RTR-SOLICITATIONS>4</TCP-IP-NDP-MAX-RTR-SOLICITATIONS>
                <TCP-IP-NDP-MIN-RANDOM-FACTOR>4</TCP-IP-NDP-MIN-RANDOM-FACTOR>
                <TCP-IP-NDP-NEIGHBOR-UNREACHABILITY-DETECTION-ENABLED>true</TCP-IP-NDP-NEIGHBOR-UNREACHABILITY-DETECTION-ENABLED>
                <TCP-IP-NDP-NUM-MULTICAST-SOLICITATIONS>4</TCP-IP-NDP-NUM-MULTICAST-SOLICITATIONS>
                <TCP-IP-NDP-NUM-UNICAST-SOLICITATIONS>4</TCP-IP-NDP-NUM-UNICAST-SOLICITATIONS>
                <TCP-IP-NDP-PACKET-QUEUE-ENABLED>true</TCP-IP-NDP-PACKET-QUEUE-ENABLED>
                <TCP-IP-NDP-PREFIX-LIST-SIZE>4</TCP-IP-NDP-PREFIX-LIST-SIZE>
                <TCP-IP-NDP-RANDOM-REACHABLE-TIME-ENABLED>true</TCP-IP-NDP-RANDOM-REACHABLE-TIME-ENABLED>
                <TCP-IP-NDP-RND-RTR-SOLICITATION-DELAY-ENABLED>true</TCP-IP-NDP-RND-RTR-SOLICITATION-DELAY-ENABLED>
                <TCP-IP-NDP-RTR-SOLICITATION-INTERVAL>1.5</TCP-IP-NDP-RTR-SOLICITATION-INTERVAL>
                <TCP-IP-NDP-SLAAC-DAD-NUMBER-OF-TRANSMISSIONS>4</TCP-IP-NDP-SLAAC-DAD-NUMBER-OF-TRANSMISSIONS>
                <TCP-IP-NDP-SLAAC-DAD-RETRANSMISSION-DELAY>1.5</TCP-IP-NDP-SLAAC-DAD-RETRANSMISSION-DELAY>
                <TCP-IP-NDP-SLAAC-DELAY-ENABLED>true</TCP-IP-NDP-SLAAC-DELAY-ENABLED>
                <TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED>true</TCP-IP-NDP-SLAAC-OPTIMISTIC-DAD-ENABLED>
            </NDP-PROPS>"""
        )

        parser.readIpv6NdpProps(element, props)

        assert props.getTcpIpNdpDefaultReachableTime().getValue() == 1.5
        assert props.getTcpIpNdpDefaultRetransTimer().getValue() == 1.5
        assert props.getTcpIpNdpDefaultRouterListSize().getValue() == 4
        assert props.getTcpIpNdpDefensiveProcessing().getValue() is True
        assert props.getTcpIpNdpDelayFirstProbeTimeValue().getValue() == 1.5
        assert props.getTcpIpNdpDestinationCacheSize().getValue() == 4
        assert props.getTcpIpNdpDynamicHopLimitEnabled().getValue() is True
        assert props.getTcpIpNdpDynamicMtuEnabled().getValue() is True
        assert props.getTcpIpNdpDynamicReachableTimeEnabled().getValue() is True
        assert props.getTcpIpNdpDynamicRetransTimeEnabled().getValue() is True
        assert props.getTcpIpNdpMaxRandomFactor().getValue() == 4
        assert props.getTcpIpNdpMaxRtrSolicitationDelay().getValue() == 1.5
        assert props.getTcpIpNdpMaxRtrSolicitations().getValue() == 4
        assert props.getTcpIpNdpMinRandomFactor().getValue() == 4
        assert props.getTcpIpNdpNeighborUnreachabilityDetectionEnabled().getValue() is True
        assert props.getTcpIpNdpNumMulticastSolicitations().getValue() == 4
        assert props.getTcpIpNdpNumUnicastSolicitations().getValue() == 4
        assert props.getTcpIpNdpPacketQueueEnabled().getValue() is True
        assert props.getTcpIpNdpPrefixListSize().getValue() == 4
        assert props.getTcpIpNdpRandomReachableTimeEnabled().getValue() is True
        assert props.getTcpIpNdpRndRtrSolicitationDelayEnabled().getValue() is True
        assert props.getTcpIpNdpRtrSolicitationInterval().getValue() == 1.5
        assert props.getTcpIpNdpSlaacDadNumberOfTransmissions().getValue() == 4
        assert props.getTcpIpNdpSlaacDadRetransmissionDelay().getValue() == 1.5
        assert props.getTcpIpNdpSlaacDelayEnabled().getValue() is True
        assert props.getTcpIpNdpSlaacOptimisticDadEnabled().getValue() is True

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Ipv6NdpProps()
        element = ET.fromstring(
            f"""<NDP-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <TCP-IP-NDP-DEFENSIVE-PROCESSING>true</TCP-IP-NDP-DEFENSIVE-PROCESSING>
            </NDP-PROPS>"""
        )

        parser.readIpv6NdpProps(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "123"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpNdpDefensiveProcessing().getValue() is True

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Ipv6NdpProps()
        element = ET.fromstring(f"""<NDP-PROPS xmlns='{NS}'/>""")

        parser.readIpv6NdpProps(element, props)

        assert props.getTcpIpNdpDefaultReachableTime() is None
        assert props.getTcpIpNdpDefaultRetransTimer() is None
        assert props.getTcpIpNdpDefaultRouterListSize() is None
        assert props.getTcpIpNdpDefensiveProcessing() is None
        assert props.getTcpIpNdpDelayFirstProbeTimeValue() is None
        assert props.getTcpIpNdpDestinationCacheSize() is None
        assert props.getTcpIpNdpDynamicHopLimitEnabled() is None
        assert props.getTcpIpNdpDynamicMtuEnabled() is None
        assert props.getTcpIpNdpDynamicReachableTimeEnabled() is None
        assert props.getTcpIpNdpDynamicRetransTimeEnabled() is None
        assert props.getTcpIpNdpMaxRandomFactor() is None
        assert props.getTcpIpNdpMaxRtrSolicitationDelay() is None
        assert props.getTcpIpNdpMaxRtrSolicitations() is None
        assert props.getTcpIpNdpMinRandomFactor() is None
        assert props.getTcpIpNdpNeighborUnreachabilityDetectionEnabled() is None
        assert props.getTcpIpNdpNumMulticastSolicitations() is None
        assert props.getTcpIpNdpNumUnicastSolicitations() is None
        assert props.getTcpIpNdpPacketQueueEnabled() is None
        assert props.getTcpIpNdpPrefixListSize() is None
        assert props.getTcpIpNdpRandomReachableTimeEnabled() is None
        assert props.getTcpIpNdpRndRtrSolicitationDelayEnabled() is None
        assert props.getTcpIpNdpRtrSolicitationInterval() is None
        assert props.getTcpIpNdpSlaacDadNumberOfTransmissions() is None
        assert props.getTcpIpNdpSlaacDadRetransmissionDelay() is None
        assert props.getTcpIpNdpSlaacDelayEnabled() is None
        assert props.getTcpIpNdpSlaacOptimisticDadEnabled() is None
