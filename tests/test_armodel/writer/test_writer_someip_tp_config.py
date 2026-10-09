"""Tests for the writeSomeipTpConfig handler (R23-11 SomeipTpConfig, Table 6.264, p.619)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpConfig, SomeipTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "TP-CHANNELS",
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


def _fill_config(config: SomeipTpConfig) -> SomeipTpConfig:
    channel = config.createSomeipTpChannel("Channel1")
    assert channel is not None
    connection = SomeipTpConnection()
    config.addTpConnection(connection)
    return config


class TestWriteSomeipTpConfig:
    """Tests for writeSomeipTpConfig handler (R23-11 SomeipTpConfig, Table 6.264, p.619)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(SomeipTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "SomeipTpConfig1"))

        parent = _parent()
        writer.writeSomeipTpConfig(parent, config)
        child = parent.find("SOMEIP-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        channels = child.findall("TP-CHANNELS/SOMEIP-TP-CHANNEL")
        assert len(channels) == 1
        assert channels[0].find("SHORT-NAME").text == "Channel1"

    def test_empty_config_writes_no_wrappers(self, writer):
        config = SomeipTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "SomeipTpConfig1")

        parent = _parent()
        writer.writeSomeipTpConfig(parent, config)
        child = parent.find("SOMEIP-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip(self, writer, parser):
        config = _fill_config(SomeipTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "SomeipTpConfig1"))

        parent = _parent()
        writer.writeSomeipTpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = SomeipTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "SomeipTpConfig1")
        parser.readSomeipTpConfig(element, reloaded)
        assert len(reloaded.getTpChannels()) == 1
        assert reloaded.getTpChannels()[0].getShortName() == "Channel1"
        assert len(reloaded.getTpConnections()) == 1
