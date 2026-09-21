"""Parser tests for NetworkEndpointAddress (Table 6.135, p.464) dispatch:
the NETWORK-ENDPOINT-ADDRESSES choice instantiates the abstract class's
concrete subclasses (IPV-4-CONFIGURATION, IPV-6-CONFIGURATION, MAC-MULTICAST-CONFIGURATION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4Configuration, NetworkEndpoint, NetworkEndpointAddress
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def test_read_ipv4_configuration_address(parser):
    root = _snip(
        "<NETWORK-ENDPOINT-ADDRESSES>"
        "<IPV-4-CONFIGURATION>"
        "<ASSIGNMENT-PRIORITY>1</ASSIGNMENT-PRIORITY>"
        "<DEFAULT-GATEWAY>192.168.0.1</DEFAULT-GATEWAY>"
        "<DNS-SERVER-ADDRESSES>"
        "<DNS-SERVER-ADDRESS>8.8.8.8</DNS-SERVER-ADDRESS>"
        "<DNS-SERVER-ADDRESS>8.8.4.4</DNS-SERVER-ADDRESS>"
        "</DNS-SERVER-ADDRESSES>"
        "<IP-ADDRESS-KEEP-BEHAVIOR>KEEP</IP-ADDRESS-KEEP-BEHAVIOR>"
        "<IPV-4-ADDRESS>192.168.0.10</IPV-4-ADDRESS>"
        "<NETWORK-MASK>255.255.255.0</NETWORK-MASK>"
        "<TTL>64</TTL>"
        "</IPV-4-CONFIGURATION>"
        "</NETWORK-ENDPOINT-ADDRESSES>"
    )
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    parser.readNetworkEndPointNetworkEndPointAddress(root, endpoint)

    addresses = endpoint.getNetworkEndpointAddresses()
    assert len(addresses) == 1
    address = addresses[0]
    assert isinstance(address, Ipv4Configuration)
    assert isinstance(address, NetworkEndpointAddress)
    assert address.getIpv4Address().getValue() == "192.168.0.10"
    assert address.getNetworkMask().getValue() == "255.255.255.0"
    assert address.getDefaultGateway().getValue() == "192.168.0.1"
    assert address.getAssignmentPriority().getValue() == 1
    assert address.getTtl().getValue() == 64
    dns = address.getDnsServerAddresses()
    assert len(dns) == 2
    assert dns[0].getValue() == "8.8.8.8"
    assert dns[1].getValue() == "8.8.4.4"
    assert address.getIpAddressKeepBehavior().getValue() == "KEEP"
