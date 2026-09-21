"""Writer round-trip tests for VlanMembership (Table 3.59, p.112).

XML element order per XSD group VLAN-MEMBERSHIP: DEFAULT-PRIORITY,
DHCP-ADDRESS-ASSIGNMENT, SEND-ACTIVITY, VLAN-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import DhcpServerConfiguration, Ipv4DhcpServerConfiguration, VlanMembership
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_membership():
    membership = VlanMembership()

    priority = PositiveInteger()
    priority.setValue(5)
    membership.setDefaultPriority(priority)

    ipv4 = Ipv4DhcpServerConfiguration()
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

    gateway = String()
    gateway.setValue("192.168.0.1")
    ipv4.setDefaultGateway(gateway)
    config = DhcpServerConfiguration()
    config.setIpv4DhcpServerConfiguration(ipv4)
    membership.setDhcpAddressAssignment(config)

    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetSwitchVlanEgressTaggingEnum

    activity = EthernetSwitchVlanEgressTaggingEnum()
    activity.setValue("SENT-TAGGED")
    membership.setSendActivity(activity)

    ref = RefType()
    ref.setDest("ETHERNET-PHYSICAL-CHANNEL")
    ref.setValue("/Clusters/Ch1")
    membership.setVlanRef(ref)
    return membership


class TestWriteVlanMembership:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVlanMembership(parent, _new_membership())
        node = parent.find("VLAN-MEMBERSHIP")
        assert node is not None
        assert node.find("DEFAULT-PRIORITY").text == "5"
        gateway = node.find("DHCP-ADDRESS-ASSIGNMENT/IPV-4-DHCP-SERVER-CONFIGURATION/DEFAULT-GATEWAY")
        assert gateway is not None
        assert gateway.text == "192.168.0.1"
        assert node.find("SEND-ACTIVITY").text == "SENT-TAGGED"
        vlan_ref = node.find("VLAN-REF")
        assert vlan_ref.text == "/Clusters/Ch1"
        assert vlan_ref.attrib["DEST"] == "ETHERNET-PHYSICAL-CHANNEL"
        children = [child.tag for child in node]
        assert children == ["DEFAULT-PRIORITY", "DHCP-ADDRESS-ASSIGNMENT", "SEND-ACTIVITY", "VLAN-REF"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVlanMembership(parent, VlanMembership())
        node = parent.find("VLAN-MEMBERSHIP")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_all_values(self):
        membership = _new_membership()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeVlanMembership(parent, membership)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = VlanMembership()
        ARXMLParser().readVlanMembership(root[0][0], parsed)

        assert parsed.getDefaultPriority().getValue() == 5
        assert parsed.getDhcpAddressAssignment().getIpv4DhcpServerConfiguration().getDefaultGateway().getValue() == "192.168.0.1"
        assert parsed.getSendActivity().getValue() == "SENT-TAGGED"
        assert parsed.getVlanRef().getValue() == "/Clusters/Ch1"
        assert parsed.getVlanRef().getDest() == "ETHERNET-PHYSICAL-CHANNEL"
