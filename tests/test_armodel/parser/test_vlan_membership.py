"""Parser tests for VlanMembership (Table 3.59, p.112).

XML element order per XSD group VLAN-MEMBERSHIP: DEFAULT-PRIORITY,
DHCP-ADDRESS-ASSIGNMENT, SEND-ACTIVITY, VLAN-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import VlanMembership
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


def test_read_vlan_membership_all_fields(parser):
    xml = """
      <VLAN-MEMBERSHIP>
        <DEFAULT-PRIORITY>5</DEFAULT-PRIORITY>
        <DHCP-ADDRESS-ASSIGNMENT>
          <IPV-4-DHCP-SERVER-CONFIGURATION>
            <DEFAULT-GATEWAY>192.168.0.1</DEFAULT-GATEWAY>
          </IPV-4-DHCP-SERVER-CONFIGURATION>
        </DHCP-ADDRESS-ASSIGNMENT>
        <SEND-ACTIVITY>SENT-TAGGED</SEND-ACTIVITY>
        <VLAN-REF DEST="ETHERNET-PHYSICAL-CHANNEL">/Clusters/Ch1</VLAN-REF>
      </VLAN-MEMBERSHIP>
    """
    root = _snip(xml)
    element = parser.find(root, "VLAN-MEMBERSHIP")
    membership = VlanMembership()
    parser.readVlanMembership(element, membership)

    assert membership.getDefaultPriority() is not None
    assert membership.getDefaultPriority().getValue() == 5

    config = membership.getDhcpAddressAssignment()
    assert config is not None
    ipv4 = config.getIpv4DhcpServerConfiguration()
    assert ipv4 is not None
    assert ipv4.getDefaultGateway().getValue() == "192.168.0.1"

    assert membership.getSendActivity() is not None
    assert membership.getSendActivity().getValue() == "SENT-TAGGED"

    assert membership.getVlanRef() is not None
    assert membership.getVlanRef().getValue() == "/Clusters/Ch1"
    assert membership.getVlanRef().getDest() == "ETHERNET-PHYSICAL-CHANNEL"


def test_read_vlan_membership_empty(parser):
    root = _snip("<VLAN-MEMBERSHIP></VLAN-MEMBERSHIP>")
    element = parser.find(root, "VLAN-MEMBERSHIP")
    membership = VlanMembership()
    parser.readVlanMembership(element, membership)

    assert membership.getDefaultPriority() is None
    assert membership.getDhcpAddressAssignment() is None
    assert membership.getSendActivity() is None
    assert membership.getVlanRef() is None
