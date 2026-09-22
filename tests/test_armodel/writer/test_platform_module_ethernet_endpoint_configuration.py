"""Writer round-trip tests for PlatformModuleEthernetEndpointConfiguration (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.19, p.65).

Element order per XSD group PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION
(AUTOSAR_00052.xsd l.91421): COMMUNICATION-CONNECTOR-REF,
IPV-4-MULTICAST-IP-ADDRESS, IPV-6-MULTICAST-IP-ADDRESS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModuleImplementation import (
    PlatformModuleEthernetEndpointConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_configuration() -> PlatformModuleEthernetEndpointConfiguration:
    package = AUTOSAR.getInstance().createARPackage("EndpointConfigs")
    config = PlatformModuleEthernetEndpointConfiguration(package, "Cfg1")
    ref = RefType()
    ref.setDest("ETHERNET-COMMUNICATION-CONNECTOR")
    ref.setValue("/Ecu/Conn")
    config.setCommunicationConnectorRef(ref)
    config.setIpv4MulticastIpAddress(Ip4AddressString().setValue("239.255.0.1"))
    config.setIpv6MulticastIpAddress(Ip6AddressString().setValue("ff02::1"))
    return config


def test_write_platform_module_ethernet_endpoint_configuration_order():
    parent = ET.Element("ROOT")
    ARXMLWriter().writePlatformModuleEthernetEndpointConfiguration(parent, _new_configuration())

    node = parent.find("PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION")
    assert node is not None
    assert [child.tag for child in node] == [
        "SHORT-NAME",
        "COMMUNICATION-CONNECTOR-REF",
        "IPV-4-MULTICAST-IP-ADDRESS",
        "IPV-6-MULTICAST-IP-ADDRESS",
    ]
    ref = node.find("COMMUNICATION-CONNECTOR-REF")
    assert ref.text == "/Ecu/Conn"
    assert ref.attrib["DEST"] == "ETHERNET-COMMUNICATION-CONNECTOR"
    assert node.find("IPV-4-MULTICAST-IP-ADDRESS").text == "239.255.0.1"
    assert node.find("IPV-6-MULTICAST-IP-ADDRESS").text == "ff02::1"


def test_write_platform_module_ethernet_endpoint_configuration_empty_omits_optional_tags():
    package = AUTOSAR.getInstance().createARPackage("EndpointConfigs")
    config = PlatformModuleEthernetEndpointConfiguration(package, "EmptyCfg")
    parent = ET.Element("ROOT")
    ARXMLWriter().writePlatformModuleEthernetEndpointConfiguration(parent, config)

    node = parent.find("PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION")
    assert node is not None
    assert [child.tag for child in node] == ["SHORT-NAME"]


def test_round_trip_preserves_all_values():
    parent = ET.Element("ROOT")
    ARXMLWriter().writePlatformModuleEthernetEndpointConfiguration(parent, _new_configuration())
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    package = AUTOSAR.getInstance().createARPackage("EndpointConfigs")
    parsed = PlatformModuleEthernetEndpointConfiguration(package, "Cfg1")
    ARXMLParser().readPlatformModuleEthernetEndpointConfiguration(root[0], parsed)

    assert parsed.getShortName() == "Cfg1"
    assert parsed.getCommunicationConnectorRef().getValue() == "/Ecu/Conn"
    assert parsed.getCommunicationConnectorRef().getDest() == "ETHERNET-COMMUNICATION-CONNECTOR"
    assert parsed.getIpv4MulticastIpAddress().getValue() == "239.255.0.1"
    assert parsed.getIpv6MulticastIpAddress().getValue() == "ff02::1"
