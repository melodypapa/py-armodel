"""Tests for the writeEthTpConfig handler (R23-11 EthTpConfig, Table 6.262, p.617)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import EthTpConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import EthTpConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "TP-CONNECTIONS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _fill_config(config: EthTpConfig) -> EthTpConfig:
    connection = EthTpConnection()
    config.addTpConnection(connection)
    return config


class TestWriteEthTpConfig:
    """Tests for writeEthTpConfig handler (R23-11 EthTpConfig, Table 6.262, p.617)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(EthTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "EthTpConfig1"))

        parent = _parent()
        writer.writeEthTpConfig(parent, config)
        child = parent.find("ETH-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        connections = child.findall("TP-CONNECTIONS/ETH-TP-CONNECTION")
        assert len(connections) == 1

    def test_empty_config_writes_no_wrappers(self, writer):
        config = EthTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "EthTpConfig1")

        parent = _parent()
        writer.writeEthTpConfig(parent, config)
        child = parent.find("ETH-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip(self, writer, parser):
        config = _fill_config(EthTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "EthTpConfig1"))

        parent = _parent()
        writer.writeEthTpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = EthTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "EthTpConfig1")
        parser.readEthTpConfig(element, reloaded)
        assert len(reloaded.getTpConnections()) == 1
