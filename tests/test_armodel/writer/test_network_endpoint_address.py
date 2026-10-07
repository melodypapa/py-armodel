"""Writer round-trip tests for NetworkEndpointAddress (Table 6.135, p.464) dispatch:
the NETWORK-ENDPOINT-ADDRESSES choice serializes the abstract class's
concrete subclasses in XSD order (IPV-4-CONFIGURATION, IPV-6-CONFIGURATION, MAC-MULTICAST-CONFIGURATION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Ip4AddressString, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv4AddressSourceEnum,
    Ipv4Configuration,
    MacMulticastConfiguration,
    NetworkEndpoint,
    NetworkEndpointAddress,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ipv4_address(text):
    value = Ip4AddressString()
    value.setValue(text)
    return value


def _ipv4_source(text):
    value = Ipv4AddressSourceEnum()
    value.setValue(text)
    return value


def _keep_behavior(text):
    value = IpAddressKeepEnum()
    value.setValue(text)
    return value


def _new_endpoint():
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    config = Ipv4Configuration()
    priority = PositiveInteger()
    priority.setValue(1)
    config.setAssignmentPriority(priority)
    config.setDefaultGateway(_ipv4_address("192.168.0.1"))
    config.addDnsServerAddress(_ipv4_address("8.8.8.8"))
    config.setIpAddressKeepBehavior(_keep_behavior("STORE-PERSISTENTLY"))
    config.setIpv4Address(_ipv4_address("192.168.0.10"))
    config.setIpv4AddressSource(_ipv4_source("FIXED"))
    config.setNetworkMask(_ipv4_address("255.255.255.0"))
    ttl = PositiveInteger()
    ttl.setValue(64)
    config.setTtl(ttl)
    endpoint.addNetworkEndpointAddress(config)
    return endpoint


class TestWriteNetworkEndpointAddress:
    def test_write_ipv4_configuration(self):
        endpoint = _new_endpoint()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        wrapper = parent.find("NETWORK-ENDPOINT-ADDRESSES")
        assert wrapper is not None
        node = wrapper.find("IPV-4-CONFIGURATION")
        assert node is not None
        assert node.find("ASSIGNMENT-PRIORITY").text == "1"
        assert node.find("DEFAULT-GATEWAY").text == "192.168.0.1"
        dns = node.findall("DNS-SERVER-ADDRESSES/DNS-SERVER-ADDRESS")
        assert len(dns) == 1
        assert dns[0].text == "8.8.8.8"
        assert node.find("IP-ADDRESS-KEEP-BEHAVIOR").text == "STORE-PERSISTENTLY"
        assert node.find("IPV-4-ADDRESS").text == "192.168.0.10"
        assert node.find("IPV-4-ADDRESS-SOURCE").text == "FIXED"
        assert node.find("NETWORK-MASK").text == "255.255.255.0"
        assert node.find("TTL").text == "64"
        children = [child.tag for child in node]
        assert children == ["ASSIGNMENT-PRIORITY", "DEFAULT-GATEWAY", "DNS-SERVER-ADDRESSES", "IP-ADDRESS-KEEP-BEHAVIOR", "IPV-4-ADDRESS", "IPV-4-ADDRESS-SOURCE", "NETWORK-MASK", "TTL"]

    def test_write_ipv4_configuration_empty_wrapper(self):
        endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        config = Ipv4Configuration()
        config.addDnsServerAddress(None)
        endpoint.addNetworkEndpointAddress(config)
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        node = parent.find("NETWORK-ENDPOINT-ADDRESSES/IPV-4-CONFIGURATION")
        assert node is not None
        assert node.find("DNS-SERVER-ADDRESSES") is None
        assert [child.tag for child in node] == []

        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        reloaded = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        ARXMLParser().readNetworkEndPointNetworkEndPointAddress(root, reloaded)
        assert reloaded.getNetworkEndpointAddresses()[0].getDnsServerAddresses() == []

    def test_round_trip_preserves_values(self):
        endpoint = _new_endpoint()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        ARXMLParser().readNetworkEndPointNetworkEndPointAddress(root, reloaded)

        addresses = reloaded.getNetworkEndpointAddresses()
        assert len(addresses) == 1
        address = addresses[0]
        assert isinstance(address, NetworkEndpointAddress)
        assert address.getIpv4Address().getValue() == "192.168.0.10"
        assert address.getNetworkMask().getValue() == "255.255.255.0"
        assert address.getDefaultGateway().getValue() == "192.168.0.1"
        assert address.getDnsServerAddresses()[0].getValue() == "8.8.8.8"
        assert address.getIpAddressKeepBehavior().getValue() == IpAddressKeepEnum.STORE_PERSISTENTLY
        assert address.getIpv4AddressSource().getValue() == "FIXED"
        assert address.getTtl().getValue() == 64
        assert isinstance(address.getIpv4AddressSource(), Ipv4AddressSourceEnum)


def _new_mac_multicast_configuration():
    config = MacMulticastConfiguration()
    config.setChecksum(String().setValue("77"))
    config.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    ref = RefType()
    ref.setValue("/EthernetCluster/McastGroup")
    ref.setDest("MAC-MULTICAST-GROUP")
    config.setMacMulticastGroupRef(ref)
    return config


class TestWriteMacMulticastConfiguration:
    def test_write_mac_multicast_configuration(self):
        endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        endpoint.addNetworkEndpointAddress(_new_mac_multicast_configuration())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        node = parent.find("NETWORK-ENDPOINT-ADDRESSES/MAC-MULTICAST-CONFIGURATION")
        assert node is not None
        ref_node = node.find("MAC-MULTICAST-GROUP-REF")
        assert ref_node is not None
        assert ref_node.text == "/EthernetCluster/McastGroup"
        assert ref_node.get("DEST") == "MAC-MULTICAST-GROUP"

    def test_write_mac_multicast_configuration_empty_omits_ref(self):
        endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        endpoint.addNetworkEndpointAddress(MacMulticastConfiguration())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        node = parent.find("NETWORK-ENDPOINT-ADDRESSES/MAC-MULTICAST-CONFIGURATION")
        assert node is not None
        assert node.find("MAC-MULTICAST-GROUP-REF") is None

    def test_round_trip_mac_multicast_configuration_preserves_values(self):
        endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        endpoint.addNetworkEndpointAddress(_new_mac_multicast_configuration())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNetworkEndPointNetworkEndPointAddresses(parent, endpoint.getNetworkEndpointAddresses())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
        ARXMLParser().readNetworkEndPointNetworkEndPointAddress(root, reloaded)

        addresses = reloaded.getNetworkEndpointAddresses()
        assert len(addresses) == 1
        address = addresses[0]
        assert isinstance(address, MacMulticastConfiguration)
        ref = address.getMacMulticastGroupRef()
        assert ref is not None
        assert ref.getValue() == "/EthernetCluster/McastGroup"
        assert ref.getDest() == "MAC-MULTICAST-GROUP"
        assert address.getChecksum().getValue() == "77"
        assert address.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
