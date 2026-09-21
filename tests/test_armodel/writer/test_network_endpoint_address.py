"""Writer round-trip tests for NetworkEndpointAddress (Table 6.135, p.464) dispatch:
the NETWORK-ENDPOINT-ADDRESSES choice serializes the abstract class's
concrete subclasses in XSD order (IPV-4-CONFIGURATION, IPV-6-CONFIGURATION, MAC-MULTICAST-CONFIGURATION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4Configuration, NetworkEndpoint, NetworkEndpointAddress
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


def _new_endpoint():
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    config = Ipv4Configuration()
    priority = PositiveInteger()
    priority.setValue(1)
    config.setAssignmentPriority(priority)
    config.setDefaultGateway(_ipv4_address("192.168.0.1"))
    config.addDnsServerAddress(_ipv4_address("8.8.8.8"))
    config.setIpv4Address(_ipv4_address("192.168.0.10"))
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
        assert node.find("IPV-4-ADDRESS").text == "192.168.0.10"
        assert node.find("NETWORK-MASK").text == "255.255.255.0"
        assert node.find("TTL").text == "64"
        children = [child.tag for child in node]
        assert children == ["ASSIGNMENT-PRIORITY", "DEFAULT-GATEWAY", "DNS-SERVER-ADDRESSES", "IPV-4-ADDRESS", "NETWORK-MASK", "TTL"]

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
        assert address.getTtl().getValue() == 64
