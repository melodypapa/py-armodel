"""Parser tests for TransportProtocolConfiguration (Table 6.125, p.459) dispatch:
the TP-CONFIGURATION choice instantiates the abstract class's concrete subclasses.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import GenericTp, TransportProtocolConfiguration
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


def test_read_generic_tp_configuration(parser):
    root = _snip("<TP-CONFIGURATION>" '<GENERIC-TP S="1234" T="2024-01-01T00:00:00Z">' "<TP-ADDRESS>30490</TP-ADDRESS>" "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>" "</GENERIC-TP>" "</TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, GenericTp)
    assert isinstance(configuration, TransportProtocolConfiguration)
    assert configuration.getTpAddress().getValue() == "30490"
    assert configuration.getTpTechnology().getValue() == "UDP"
    assert configuration.getChecksum().getValue() == "1234"
    assert configuration.getTimestamp().getValue() == "2024-01-01T00:00:00Z"


def test_read_tp_configuration_empty(parser):
    root = _snip("<TP-CONFIGURATION></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert configuration is None
