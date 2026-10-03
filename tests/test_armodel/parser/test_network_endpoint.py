"""Reader round-trip tests for NetworkEndpoint (Table 6.134, p.463)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
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


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _endpoint():
    from armodel.models import EthernetCluster, EthernetPhysicalChannel, NetworkEndpoint

    cluster = EthernetCluster(parent=AUTOSAR.getInstance(), short_name="eth")
    channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
    return NetworkEndpoint(parent=channel, short_name="ne")


class TestNetworkEndpointReader:
    def test_read_fully_qualified_domain_name_value(self, parser):
        endpoint = _endpoint()
        element = _snip("<SHORT-NAME>ne</SHORT-NAME><FULLY-QUALIFIED-DOMAIN-NAME>some.example.host</FULLY-QUALIFIED-DOMAIN-NAME>", root_tag="NETWORK-ENDPOINT")
        parser.readNetworkEndPoint(element, endpoint)
        assert endpoint.getFullyQualifiedDomainName() is not None
        assert endpoint.getFullyQualifiedDomainName().getValue() == "some.example.host"

    def test_read_all_attributes(self, parser):
        endpoint = _endpoint()
        element = _snip(
            "<SHORT-NAME>ne</SHORT-NAME>"
            "<FULLY-QUALIFIED-DOMAIN-NAME>host.example.com</FULLY-QUALIFIED-DOMAIN-NAME>"
            "<INFRASTRUCTURE-SERVICES><DO-IP-ENTITY><DO-IP-ENTITY-ROLE>server</DO-IP-ENTITY-ROLE></DO-IP-ENTITY></INFRASTRUCTURE-SERVICES>"
            "<NETWORK-ENDPOINT-ADDRESSES><IPV-6-CONFIGURATION><IPV-6-ADDRESS>fe80::1</IPV-6-ADDRESS></IPV-6-CONFIGURATION></NETWORK-ENDPOINT-ADDRESSES>"
            "<PRIORITY>3</PRIORITY>",
            root_tag="NETWORK-ENDPOINT",
        )
        parser.readNetworkEndPoint(element, endpoint)
        assert endpoint.getFullyQualifiedDomainName().getValue() == "host.example.com"
        assert endpoint.getInfrastructureServices() is not None
        assert len(endpoint.getNetworkEndpointAddresses()) == 1
        assert endpoint.getPriority().getValue() == 3

    def test_read_absent_attributes_are_none_and_empty(self, parser):
        endpoint = _endpoint()
        element = _snip("<SHORT-NAME>ne</SHORT-NAME>", root_tag="NETWORK-ENDPOINT")
        parser.readNetworkEndPoint(element, endpoint)
        assert endpoint.getFullyQualifiedDomainName() is None
        assert endpoint.getInfrastructureServices() is None
        assert endpoint.getIpSecConfig() is None
        assert endpoint.getNetworkEndpointAddresses() == []
        assert endpoint.getPriority() is None
