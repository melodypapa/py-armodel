"""Reader tests for SomeipSdServerServiceInstanceConfig (R23-11 CP_TPS_SystemTemplate, Table 6.169, p.514).

XSD group SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG (AUTOSAR_00052.xsd l.110751) element order:
INITIAL-OFFER-BEHAVIOR, OFFER-CYCLIC-DELAY, PRIORITY, REQUEST-RESPONSE-DELAY,
SERVICE-OFFER-TIME-TO-LIVE. Aggregated by ARPackage.element - the ARPackage ELEMENTS
choice instantiates the ARElement subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    InitialSdDelayConfig,
    RequestResponseDelay,
    SomeipSdServerServiceInstanceConfig,
)
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


ALL_ATTRS = (
    "<SHORT-NAME>sd_server_config</SHORT-NAME>"
    "<INITIAL-OFFER-BEHAVIOR>"
    "<INITIAL-DELAY-MAX-VALUE>0.1</INITIAL-DELAY-MAX-VALUE>"
    "<INITIAL-REPETITIONS-MAX>3</INITIAL-REPETITIONS-MAX>"
    "</INITIAL-OFFER-BEHAVIOR>"
    "<OFFER-CYCLIC-DELAY>2.0</OFFER-CYCLIC-DELAY>"
    "<PRIORITY>6</PRIORITY>"
    "<REQUEST-RESPONSE-DELAY>"
    "<MAX-VALUE>0.5</MAX-VALUE>"
    "<MIN-VALUE>0.05</MIN-VALUE>"
    "</REQUEST-RESPONSE-DELAY>"
    "<SERVICE-OFFER-TIME-TO-LIVE>30</SERVICE-OFFER-TIME-TO-LIVE>"
)


def test_read_someip_sd_server_service_instance_config_all_attrs(parser):
    config = SomeipSdServerServiceInstanceConfig(parser, "sd_server_config")
    element = ET.fromstring(f"<SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG xmlns='{NS}'>{ALL_ATTRS}</SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG>")
    parser.readSomeipSdServerServiceInstanceConfig(element, config)

    assert config.getShortName() == "sd_server_config"
    behavior = config.getInitialOfferBehavior()
    assert isinstance(behavior, InitialSdDelayConfig)
    assert behavior.getInitialDelayMaxValue().getValue() == 0.1
    assert behavior.getInitialRepetitionsMax().getValue() == 3
    assert config.getOfferCyclicDelay().getValue() == 2.0
    assert config.getPriority().getValue() == 6
    delay = config.getRequestResponseDelay()
    assert isinstance(delay, RequestResponseDelay)
    assert delay.getMaxValue().getValue() == 0.5
    assert delay.getMinValue().getValue() == 0.05
    assert config.getServiceOfferTimeToLive().getValue() == 30


def test_read_empty_element_leaves_defaults(parser):
    config = SomeipSdServerServiceInstanceConfig(parser, "sd_server_config")
    element = ET.fromstring(f"<SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG xmlns='{NS}'><SHORT-NAME>sd_server_config</SHORT-NAME></SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG>")
    parser.readSomeipSdServerServiceInstanceConfig(element, config)

    assert config.getInitialOfferBehavior() is None
    assert config.getOfferCyclicDelay() is None
    assert config.getPriority() is None
    assert config.getRequestResponseDelay() is None
    assert config.getServiceOfferTimeToLive() is None


def test_arpackage_elements_dispatch_instantiates_class(parser):
    root = _snip(
        "<ELEMENTS>" "<SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG>" "<SHORT-NAME>ServerConfig</SHORT-NAME>" "<PRIORITY>4</PRIORITY>" "</SOME-IP-SD-SERVER-SERVICE-INSTANCE-CONFIG>" "</ELEMENTS>"
    )
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    parser.readARPackageElements(root, package)

    config = package.getReferrableElement("ServerConfig", SomeipSdServerServiceInstanceConfig)
    assert isinstance(config, SomeipSdServerServiceInstanceConfig)
    assert config.getPriority().getValue() == 4
