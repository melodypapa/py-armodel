"""Parser tests for PlatformModuleEthernetEndpointConfiguration (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.19, p.65).

The reader helper is exercised directly on a
PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION fragment and through the
ARPackage ELEMENTS dispatch; the PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION
group (AUTOSAR_00052.xsd l.91421) holds COMMUNICATION-CONNECTOR-REF,
IPV-4-MULTICAST-IP-ADDRESS, IPV-6-MULTICAST-IP-ADDRESS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModuleImplementation import (
    PlatformModuleEthernetEndpointConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_configuration() -> PlatformModuleEthernetEndpointConfiguration:
    package = AUTOSAR.getInstance().createARPackage("EndpointConfigs")
    return PlatformModuleEthernetEndpointConfiguration(package, "Cfg1")


def test_read_platform_module_ethernet_endpoint_configuration():
    element = ET.fromstring(
        "<PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION xmlns='%s'>"
        "<SHORT-NAME>Cfg1</SHORT-NAME>"
        "<COMMUNICATION-CONNECTOR-REF DEST='ETHERNET-COMMUNICATION-CONNECTOR'>/Ecu/Conn</COMMUNICATION-CONNECTOR-REF>"
        "<IPV-4-MULTICAST-IP-ADDRESS>239.255.0.1</IPV-4-MULTICAST-IP-ADDRESS>"
        "<IPV-6-MULTICAST-IP-ADDRESS>ff02::1</IPV-6-MULTICAST-IP-ADDRESS>"
        "</PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION>" % NS
    )
    config = _new_configuration()
    ARXMLParser().readPlatformModuleEthernetEndpointConfiguration(element, config)

    assert config.getShortName() == "Cfg1"
    assert config.getCommunicationConnectorRef().getValue() == "/Ecu/Conn"
    assert config.getCommunicationConnectorRef().getDest() == "ETHERNET-COMMUNICATION-CONNECTOR"
    assert config.getIpv4MulticastIpAddress().getValue() == "239.255.0.1"
    assert config.getIpv6MulticastIpAddress().getValue() == "ff02::1"


def test_read_platform_module_ethernet_endpoint_configuration_empty():
    element = ET.fromstring("<PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION xmlns='%s'><SHORT-NAME>Cfg1</SHORT-NAME></PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION>" % NS)
    config = _new_configuration()
    ARXMLParser().readPlatformModuleEthernetEndpointConfiguration(element, config)

    assert config.getCommunicationConnectorRef() is None
    assert config.getIpv4MulticastIpAddress() is None
    assert config.getIpv6MulticastIpAddress() is None


def test_arpackage_dispatch_reads_element():
    parser = ARXMLParser()
    package = AUTOSAR.getInstance().createARPackage("EndpointConfigs")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>EndpointConfigs</SHORT-NAME>"
        "<ELEMENTS>"
        "<PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION>"
        "<SHORT-NAME>Cfg1</SHORT-NAME>"
        "<COMMUNICATION-CONNECTOR-REF DEST='ETHERNET-COMMUNICATION-CONNECTOR'>/Ecu/Conn</COMMUNICATION-CONNECTOR-REF>"
        "</PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    config = package.getElement("Cfg1", PlatformModuleEthernetEndpointConfiguration)
    assert config is not None
    assert isinstance(config, PlatformModuleEthernetEndpointConfiguration)
    assert config.getCommunicationConnectorRef().getValue() == "/Ecu/Conn"
