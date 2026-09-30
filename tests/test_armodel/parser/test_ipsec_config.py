"""Parser tests for IPSecConfig (Table 6.221, p.571) readIPSecConfig and the
NetworkEndpoint.ipSecConfig aggregation wiring (XSD group NETWORK-ENDPOINT:
FULLY-QUALIFIED-DOMAIN-NAME -> INFRASTRUCTURE-SERVICES -> IP-SEC-CONFIG ->
NETWORK-ENDPOINT-ADDRESSES)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import IPSecConfig, NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecRule
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


def test_read_ip_sec_config(parser):
    root = _snip(
        "<IP-SEC-CONFIG>"
        "<IP-SEC-CONFIG-PROPS-REF DEST='IP-SEC-CONFIG-PROPS'>/pkg/GlobalProps</IP-SEC-CONFIG-PROPS-REF>"
        "<IP-SEC-RULES>"
        "<IP-SEC-RULE>"
        "<SHORT-NAME>RuleA</SHORT-NAME>"
        "<DIRECTION>IN</DIRECTION>"
        "<LOCAL-ID>hostA</LOCAL-ID>"
        "</IP-SEC-RULE>"
        "<IP-SEC-RULE>"
        "<SHORT-NAME>RuleB</SHORT-NAME>"
        "<POLICY>IPSEC</POLICY>"
        "<PRIORITY>7</PRIORITY>"
        "</IP-SEC-RULE>"
        "</IP-SEC-RULES>"
        "</IP-SEC-CONFIG>"
    )
    config = IPSecConfig()
    parser.readIPSecConfig(parser.find(root, "IP-SEC-CONFIG"), config)

    assert config.getIpSecConfigPropsRef().getValue() == "/pkg/GlobalProps"
    assert config.getIpSecConfigPropsRef().getDest() == "IP-SEC-CONFIG-PROPS"
    rules = config.getIPSecRules()
    assert len(rules) == 2
    assert isinstance(rules[0], IPSecRule)
    assert rules[0].getShortName() == "RuleA"
    assert rules[0].getDirection().getValue() == "IN"
    assert rules[0].getLocalId().getValue() == "hostA"
    assert rules[1].getShortName() == "RuleB"
    assert rules[1].getPolicy().getValue() == "IPSEC"
    assert rules[1].getPriority().getValue() == 7


def test_read_ip_sec_config_absent_members(parser):
    root = _snip("<IP-SEC-CONFIG></IP-SEC-CONFIG>")
    config = IPSecConfig()
    parser.readIPSecConfig(parser.find(root, "IP-SEC-CONFIG"), config)

    assert config.getIpSecConfigPropsRef() is None
    assert config.getIPSecRules() == []


def test_read_network_endpoint_ip_sec_config_wiring(parser):
    root = _snip(
        "<NETWORK-ENDPOINT>"
        "<SHORT-NAME>Ep1</SHORT-NAME>"
        "<INFRASTRUCTURE-SERVICES></INFRASTRUCTURE-SERVICES>"
        "<IP-SEC-CONFIG>"
        "<IP-SEC-CONFIG-PROPS-REF DEST='IP-SEC-CONFIG-PROPS'>/pkg/Props</IP-SEC-CONFIG-PROPS-REF>"
        "<IP-SEC-RULES>"
        "<IP-SEC-RULE>"
        "<SHORT-NAME>RuleA</SHORT-NAME>"
        "<MODE>TUNNEL</MODE>"
        "</IP-SEC-RULE>"
        "</IP-SEC-RULES>"
        "</IP-SEC-CONFIG>"
        "<NETWORK-ENDPOINT-ADDRESSES></NETWORK-ENDPOINT-ADDRESSES>"
        "</NETWORK-ENDPOINT>"
    )
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    parser.readNetworkEndPoint(parser.find(root, "NETWORK-ENDPOINT"), endpoint)

    config = endpoint.getIpSecConfig()
    assert isinstance(config, IPSecConfig)
    assert config.getIpSecConfigPropsRef().getValue() == "/pkg/Props"
    rules = config.getIPSecRules()
    assert len(rules) == 1
    assert rules[0].getShortName() == "RuleA"
    assert rules[0].getMode().getValue() == "TUNNEL"


def test_read_network_endpoint_without_ip_sec_config(parser):
    root = _snip("<NETWORK-ENDPOINT>" "<SHORT-NAME>Ep1</SHORT-NAME>" "<NETWORK-ENDPOINT-ADDRESSES></NETWORK-ENDPOINT-ADDRESSES>" "</NETWORK-ENDPOINT>")
    endpoint = NetworkEndpoint(parent=AUTOSAR.getInstance(), short_name="Ep1")
    parser.readNetworkEndPoint(parser.find(root, "NETWORK-ENDPOINT"), endpoint)

    assert endpoint.getIpSecConfig() is None
