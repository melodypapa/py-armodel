"""Tests for the writeFlexrayTpConfig handler (R23-11 FlexrayTpConfig, Table 6.239, p.592)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpConnection, FlexrayTpEcu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "PDU-POOLS",
    "TP-ADDRESSS",
    "TP-CONNECTIONS",
    "TP-CONNECTION-CONTROLS",
    "TP-ECUS",
    "TP-NODES",
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


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _fill_config(config: FlexrayTpConfig) -> FlexrayTpConfig:
    pool = config.createFlexrayTpPduPool("Pool1")
    assert pool is not None
    address = config.createTpAddress("Address1")
    address.setTpAddress(_integer(2048))
    connection = FlexrayTpConnection()
    config.addTpConnection(connection)
    control = config.createFlexrayTpConnectionControl("Control1")
    assert control is not None
    ecu = FlexrayTpEcu()
    config.addTpEcu(ecu)
    node = config.createFlexrayTpNode("Node1")
    assert node is not None
    return config


class TestWriteFlexrayTpConfig:
    """Tests for writeFlexrayTpConfig handler (R23-11 FlexrayTpConfig, Table 6.239, p.592)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "FlexrayTpConfig1"))

        parent = _parent()
        writer.writeFlexrayTpConfig(parent, config)
        child = parent.find("FLEXRAY-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        addresses = child.findall("TP-ADDRESSS/TP-ADDRESS")
        assert len(addresses) == 1
        assert addresses[0].find("SHORT-NAME").text == "Address1"
        assert addresses[0].find("TP-ADDRESS").text == "2048"

    def test_empty_config_writes_no_wrappers(self, writer):
        config = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "FlexrayTpConfig1")

        parent = _parent()
        writer.writeFlexrayTpConfig(parent, config)
        child = parent.find("FLEXRAY-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip(self, writer, parser):
        config = _fill_config(FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "FlexrayTpConfig1"))

        parent = _parent()
        writer.writeFlexrayTpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "FlexrayTpConfig1")
        parser.readFlexrayTpConfig(element, reloaded)
        assert len(reloaded.getPduPools()) == 1
        assert reloaded.getPduPools()[0].getShortName() == "Pool1"
        assert len(reloaded.getTpAddresses()) == 1
        assert reloaded.getTpAddresses()[0].getTpAddress().getValue() == 2048
        assert len(reloaded.getTpConnections()) == 1
        assert len(reloaded.getTpConnectionControls()) == 1
        assert reloaded.getTpConnectionControls()[0].getShortName() == "Control1"
        assert len(reloaded.getTpEcus()) == 1
        assert len(reloaded.getTpNodes()) == 1
        assert reloaded.getTpNodes()[0].getShortName() == "Node1"
