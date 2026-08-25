"""Writer/reader round-trip tests for DhcpServerConfiguration (Table 3.79, p.131).

DhcpServerConfiguration is an inline Describable value type consumed by
VlanMembership.dhcpAddressAssignment (serialized as DHCP-ADDRESS-ASSIGNMENT) and
InfrastructureServices.dhcpServerConfiguration (serialized as DHCP-SERVER-CONFIGURATION).
It aggregates IPV-4-DHCP-SERVER-CONFIGURATION and IPV-6-DHCP-SERVER-CONFIGURATION.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DhcpServerConfiguration,
    Ipv4DhcpServerConfiguration,
    Ipv6DhcpServerConfiguration,
    VlanMembership,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _new_config(ipv4=True, ipv6=True):
    config = DhcpServerConfiguration()
    if ipv4:
        config.setIpv4DhcpServerConfiguration(Ipv4DhcpServerConfiguration())
    if ipv6:
        config.setIpv6DhcpServerConfiguration(Ipv6DhcpServerConfiguration())
    return config


class TestWriteDhcpServerConfiguration:
    def test_write_all_fields(self, writer):
        membership = VlanMembership()
        membership.setDhcpAddressAssignment(_new_config())
        parent = ET.Element("PARENT")
        writer.writeVlanMembership(parent, membership)
        vm = parent.find("VLAN-MEMBERSHIP")
        assert vm is not None
        dhcp = vm.find("DHCP-ADDRESS-ASSIGNMENT")
        assert dhcp is not None
        assert dhcp.find("IPV-4-DHCP-SERVER-CONFIGURATION") is not None
        assert dhcp.find("IPV-6-DHCP-SERVER-CONFIGURATION") is not None

    def test_write_empty_omits_element(self, writer):
        membership = VlanMembership()
        parent = ET.Element("PARENT")
        writer.writeVlanMembership(parent, membership)
        vm = parent.find("VLAN-MEMBERSHIP")
        assert vm is not None
        assert vm.find("DHCP-ADDRESS-ASSIGNMENT") is None


class TestDhcpServerConfigurationRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        membership = VlanMembership()
        membership.setDhcpAddressAssignment(_new_config())
        parent = ET.Element("PARENT")
        writer.writeVlanMembership(parent, membership)
        vm_element = _serialize_and_wrap(parent)
        parsed = VlanMembership()
        parser.readVlanMembership(vm_element, parsed)
        config = parsed.getDhcpAddressAssignment()
        assert isinstance(config, DhcpServerConfiguration)
        assert isinstance(config.getIpv4DhcpServerConfiguration(), Ipv4DhcpServerConfiguration)
        assert isinstance(config.getIpv6DhcpServerConfiguration(), Ipv6DhcpServerConfiguration)

    def test_reader_empty_fields(self, writer, parser):
        element = ET.fromstring("<VLAN-MEMBERSHIP xmlns='%s'></VLAN-MEMBERSHIP>" % NS)
        parsed = VlanMembership()
        parser.readVlanMembership(element, parsed)
        assert parsed.getDhcpAddressAssignment() is None


def _new_ipv4_config():
    config = Ipv4DhcpServerConfiguration()
    config.setAddressRangeLowerBound(Ip4AddressString().setValue("192.168.0.100"))
    config.setAddressRangeUpperBound(Ip4AddressString().setValue("192.168.0.200"))
    config.setDefaultGateway(Ip4AddressString().setValue("192.168.0.1"))
    config.setDefaultLeaseTime(TimeValue().setValue(3600))
    config.addDnsServerAddress(Ip4AddressString().setValue("8.8.8.8"))
    config.addDnsServerAddress(Ip4AddressString().setValue("8.8.4.4"))
    config.setNetworkMask(Ip4AddressString().setValue("255.255.255.0"))
    return config


class TestIpv4DhcpServerConfigurationWrite:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION", _new_ipv4_config())
        node = parent.find("IPV-4-DHCP-SERVER-CONFIGURATION")
        assert node is not None
        assert node.find("ADDRESS-RANGE-LOWER-BOUND").text == "192.168.0.100"
        assert node.find("ADDRESS-RANGE-UPPER-BOUND").text == "192.168.0.200"
        assert node.find("DEFAULT-GATEWAY").text == "192.168.0.1"
        assert node.find("DEFAULT-LEASE-TIME").text == "3600.0"
        dns_addresses = node.findall("DNS-SERVER-ADDRESSES/DNS-SERVER-ADDRESS")
        assert len(dns_addresses) == 2
        assert dns_addresses[0].text == "8.8.8.8"
        assert dns_addresses[1].text == "8.8.4.4"
        assert node.find("NETWORK-MASK").text == "255.255.255.0"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.setIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION", Ipv4DhcpServerConfiguration())
        node = parent.find("IPV-4-DHCP-SERVER-CONFIGURATION")
        assert node is not None
        assert len(list(node)) == 0

    def test_write_none_omits_element(self, writer):
        parent = ET.Element("PARENT")
        writer.setIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION", None)
        assert parent.find("IPV-4-DHCP-SERVER-CONFIGURATION") is None


class TestIpv4DhcpServerConfigurationRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION", _new_ipv4_config())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getIpv4DhcpServerConfiguration(root[0], "IPV-4-DHCP-SERVER-CONFIGURATION")
        assert isinstance(parsed, Ipv4DhcpServerConfiguration)
        assert parsed.getAddressRangeLowerBound().getValue() == "192.168.0.100"
        assert parsed.getAddressRangeUpperBound().getValue() == "192.168.0.200"
        assert parsed.getDefaultGateway().getValue() == "192.168.0.1"
        assert parsed.getDefaultLeaseTime().getValue() == 3600
        dns_addresses = parsed.getDnsServerAddresses()
        assert len(dns_addresses) == 2
        assert dns_addresses[0].getValue() == "8.8.8.8"
        assert dns_addresses[1].getValue() == "8.8.4.4"
        assert parsed.getNetworkMask().getValue() == "255.255.255.0"

    def test_reader_missing_element_returns_none(self, parser):
        parent = ET.fromstring("<PARENT xmlns='%s'></PARENT>" % NS)
        assert parser.getIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION") is None

    def test_reader_empty_fields(self, parser):
        parent = ET.fromstring("<PARENT xmlns='%s'><IPV-4-DHCP-SERVER-CONFIGURATION/></PARENT>" % NS)
        parsed = parser.getIpv4DhcpServerConfiguration(parent, "IPV-4-DHCP-SERVER-CONFIGURATION")
        assert isinstance(parsed, Ipv4DhcpServerConfiguration)
        assert parsed.getAddressRangeLowerBound() is None
        assert parsed.getAddressRangeUpperBound() is None
        assert parsed.getDefaultGateway() is None
        assert parsed.getDefaultLeaseTime() is None
        assert parsed.getDnsServerAddresses() == []
        assert parsed.getNetworkMask() is None
