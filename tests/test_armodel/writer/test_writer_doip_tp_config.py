"""Tests for the writeDoIpTpConfig handler (R23-11 DoIpTpConfig, Table 6.205, p.555)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpTpConfig, DoIpTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "DO-IP-LOGIC-ADDRESSS",
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


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _fill_config(config: DoIpTpConfig) -> DoIpTpConfig:
    address1 = config.createDoIpLogicAddress("LogicAddress1")
    address1.setAddress(_positive_integer("2048"))
    address2 = config.createDoIpLogicAddress("LogicAddress2")
    address2.setAddress(_positive_integer("4096"))
    connection = DoIpTpConnection()
    connection.setDoIpSourceAddressRef(_ref("/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1", "DO-IP-LOGIC-ADDRESS"))
    connection.setDoIpTargetAddressRef(_ref("/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2", "DO-IP-LOGIC-ADDRESS"))
    connection.setTpSduRef(_ref("/SoAd/PduTriggering1", "PDU-TRIGGERING"))
    config.addTpConnection(connection)
    return config


class TestWriteDoIpTpConfig:
    """Tests for writeDoIpTpConfig handler (R23-11 DoIpTpConfig, Table 6.205, p.555)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(DoIpTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "DoIpTpConfig1"))

        parent = _parent()
        writer.writeDoIpTpConfig(parent, config)
        child = parent.find("DO-IP-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        addresses = child.findall("DO-IP-LOGIC-ADDRESSS/DO-IP-LOGIC-ADDRESS")
        assert len(addresses) == 2
        assert addresses[0].find("SHORT-NAME").text == "LogicAddress1"
        assert addresses[0].find("ADDRESS").text == "2048"
        assert addresses[1].find("SHORT-NAME").text == "LogicAddress2"
        assert addresses[1].find("ADDRESS").text == "4096"
        connections = child.findall("TP-CONNECTIONS/DO-IP-TP-CONNECTION")
        assert len(connections) == 1
        source_ref = connections[0].find("DO-IP-SOURCE-ADDRESS-REF")
        assert source_ref.text == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert source_ref.get("DEST") == "DO-IP-LOGIC-ADDRESS"
        assert connections[0].find("DO-IP-TARGET-ADDRESS-REF").text == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert connections[0].find("TP-SDU-REF").text == "/SoAd/PduTriggering1"

    def test_empty_children_omitted(self, writer):
        config = DoIpTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "DoIpTpConfig1")
        parent = _parent()
        writer.writeDoIpTpConfig(parent, config)
        child = parent.find("DO-IP-TP-CONFIG")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_round_trip(self, writer, parser):
        config = _fill_config(DoIpTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "DoIpTpConfig1"))

        parent = _parent()
        writer.writeDoIpTpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        package = AUTOSAR.getInstance().createARPackage("TpConfigs2")
        reparsed = DoIpTpConfig(package, "DoIpTpConfig1")
        parser.readDoIpTpConfig(parser.find(element, "DO-IP-TP-CONFIG"), reparsed)
        addresses = reparsed.getDoIpLogicAddresses()
        assert len(addresses) == 2
        assert addresses[0].getShortName() == "LogicAddress1"
        assert addresses[0].getAddress().getValue() == 2048
        assert addresses[1].getAddress().getValue() == 4096
        connections = reparsed.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getDoIpSourceAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert connections[0].getDoIpTargetAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert connections[0].getTpSduRef().getValue() == "/SoAd/PduTriggering1"
