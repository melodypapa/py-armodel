"""Writer/reader round-trip tests for Ipv6Configuration (Table 6.139, p.466).

Ipv6Configuration is a NetworkEndpointAddress value type aggregated by
NetworkEndpoint.networkEndpointAddress.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv6AddressSourceEnum,
    Ipv6Configuration,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _new_configuration():
    configuration = Ipv6Configuration()
    configuration.setAssignmentPriority(PositiveInteger().setValue(1))
    configuration.setDefaultRouter(Ip6AddressString().setValue("fe80::1"))
    configuration.addDnsServerAddress(Ip6AddressString().setValue("2001:db8::53"))
    configuration.setEnableAnycast(Boolean().setValue("true"))
    configuration.setHopCount(PositiveInteger().setValue(64))
    configuration.setIpAddressKeepBehavior(IpAddressKeepEnum().setValue(IpAddressKeepEnum.STORE_PERSISTENTLY))
    configuration.setIpAddressPrefixLength(PositiveInteger().setValue(48))
    configuration.setIpv6Address(Ip6AddressString().setValue("2001:db8::1"))
    configuration.setIpv6AddressSource(Ipv6AddressSourceEnum().setValue(Ipv6AddressSourceEnum.DHCPV6))
    return configuration


class TestWriteIpv6Configuration:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setIpv6Configuration(parent, _new_configuration())
        node = parent.find("IPV-6-CONFIGURATION")
        assert node is not None
        assert node.find("ASSIGNMENT-PRIORITY").text == "1"
        assert node.find("DEFAULT-ROUTER").text == "fe80::1"
        dns_addresses = node.findall("DNS-SERVER-ADDRESSES/DNS-SERVER-ADDRESS")
        assert len(dns_addresses) == 1
        assert dns_addresses[0].text == "2001:db8::53"
        assert node.find("ENABLE-ANYCAST").text == "true"
        assert node.find("HOP-COUNT").text == "64"
        assert node.find("IP-ADDRESS-KEEP-BEHAVIOR").text == "storePersistently"
        assert node.find("IP-ADDRESS-PREFIX-LENGTH").text == "48"
        assert node.find("IPV-6-ADDRESS").text == "2001:db8::1"
        assert node.find("IPV-6-ADDRESS-SOURCE").text == "dhcpv6"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.setIpv6Configuration(parent, Ipv6Configuration())
        node = parent.find("IPV-6-CONFIGURATION")
        assert node is not None
        assert len(list(node)) == 0


class TestIpv6ConfigurationRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setIpv6Configuration(parent, _new_configuration())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getIpv6Configuration(root[0][0])
        assert isinstance(parsed, Ipv6Configuration)
        assert parsed.getAssignmentPriority().getValue() == 1
        assert parsed.getDefaultRouter().getValue() == "fe80::1"
        dns_addresses = parsed.getDnsServerAddresses()
        assert len(dns_addresses) == 1
        assert dns_addresses[0].getValue() == "2001:db8::53"
        assert parsed.getEnableAnycast().getValue() is True
        assert parsed.getHopCount().getValue() == 64
        assert parsed.getIpAddressKeepBehavior().getValue() == "storePersistently"
        assert isinstance(parsed.getIpAddressKeepBehavior(), IpAddressKeepEnum)
        assert parsed.getIpAddressPrefixLength().getValue() == 48
        assert parsed.getIpv6Address().getValue() == "2001:db8::1"
        assert parsed.getIpv6AddressSource().getValue() == "dhcpv6"
        assert isinstance(parsed.getIpv6AddressSource(), Ipv6AddressSourceEnum)

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<IPV-6-CONFIGURATION xmlns='%s'></IPV-6-CONFIGURATION>" % NS)
        parsed = parser.getIpv6Configuration(element)
        assert isinstance(parsed, Ipv6Configuration)
        assert parsed.getDnsServerAddresses() == []
        assert parsed.getIpAddressKeepBehavior() is None
