"""Tests for the writeFlexrayArTpChannel handler (R23-11 FlexrayArTpChannel, Table 6.246, p.602)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    FrArTpAckType,
    Integer,
    MaximumMessageLengthType,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpChannel, FlexrayArTpConfig, FlexrayArTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "ACK-TYPE",
    "CANCELLATION",
    "EXTENDED-ADDRESSING",
    "MAX-AR",
    "MAX-AS",
    "MAX-BS",
    "MAX-FC-WAIT",
    "MAXIMUM-MESSAGE-LENGTH",
    "MAX-RETRIES",
    "MINIMUM-MULTICAST-SEPERATION-TIME",
    "MINIMUM-SEPARATION-TIME",
    "MULTICAST-SEGMENTATION",
    "N-PDU-REFS",
    "TIME-BR",
    "TIME-CS",
    "TIMEOUT-AR",
    "TIMEOUT-AS",
    "TIMEOUT-BS",
    "TIMEOUT-CR",
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


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _fill_channel(channel: FlexrayArTpChannel) -> FlexrayArTpChannel:
    channel.setAckType(FrArTpAckType().setValue(FrArTpAckType.ENUM_ACK_WITH_RT))
    channel.setCancellation(_boolean(True))
    channel.setExtendedAddressing(_boolean(True))
    channel.setMaxAr(_integer(3))
    channel.setMaxAs(_integer(4))
    channel.setMaxBs(_integer(8))
    channel.setMaxFcWait(_positive_integer(2))
    channel.setMaximumMessageLength(MaximumMessageLengthType().setValue(MaximumMessageLengthType.ENUM_ISO))
    channel.setMaxRetries(_integer(1))
    channel.setMinimumMulticastSeperationTime(_time(0.0002))
    channel.setMinimumSeparationTime(_time(0.0001))
    channel.setMulticastSegmentation(_boolean(False))
    channel.addNPduRef(_ref("/NPdus/N1", "N-PDU"))
    channel.setTimeBr(_time(0.01))
    channel.setTimeCs(_time(0.02))
    channel.setTimeoutAr(_time(0.03))
    channel.setTimeoutAs(_time(0.04))
    channel.setTimeoutBs(_time(0.05))
    channel.setTimeoutCr(_time(0.06))
    connection = FlexrayArTpConnection()
    connection.setConnectionPrioPdus(_integer(16))
    connection.setSourceRef(_ref("/Nodes/Src", "FLEXRAY-AR-TP-NODE"))
    connection.addTargetRef(_ref("/Nodes/Tgt", "FLEXRAY-AR-TP-NODE"))
    channel.addTpConnection(connection)
    return channel


class TestWriteFlexrayArTpChannel:
    """Tests for writeFlexrayArTpChannel (R23-11 FlexrayArTpChannel, Table 6.246, p.602)."""

    def test_children_in_xsd_order(self, writer):
        channel = _fill_channel(FlexrayArTpChannel())
        parent = _parent()
        writer.writeFlexrayArTpChannel(parent, channel)
        child = parent.find("FLEXRAY-AR-TP-CHANNEL")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("ACK-TYPE").text == "ACK-WITH-RT"
        assert child.find("MAXIMUM-MESSAGE-LENGTH").text == "ISO"
        assert child.find("MINIMUM-MULTICAST-SEPERATION-TIME").text == "0.0002"
        refs = child.findall("N-PDU-REFS/N-PDU-REF")
        assert len(refs) == 1
        assert refs[0].text == "/NPdus/N1"
        connections = child.findall("TP-CONNECTIONS/FLEXRAY-AR-TP-CONNECTION")
        assert len(connections) == 1
        assert connections[0].find("CONNECTION-PRIO-PDUS").text == "16"
        assert connections[0].find("SOURCE-REF").text == "/Nodes/Src"
        targets = connections[0].findall("TARGET-REFS/TARGET-REF")
        assert len(targets) == 1
        assert targets[0].text == "/Nodes/Tgt"

    def test_empty_channel_writes_no_attributes(self, writer):
        channel = FlexrayArTpChannel()
        parent = _parent()
        writer.writeFlexrayArTpChannel(parent, channel)
        child = parent.find("FLEXRAY-AR-TP-CHANNEL")
        assert child is not None
        assert len(child) == 0

    def test_round_trip_via_config(self, writer, parser):
        config = FlexrayArTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        config.addTpChannel(_fill_channel(FlexrayArTpChannel()))

        parent = _parent()
        writer.writeFlexrayArTpConfig(parent, config)
        xml_text = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        assert "FLEXRAY-AR-TP-CHANNEL" in xml_text

        reparsed = ET.fromstring(xml_text)[0]
        config2 = FlexrayArTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        parser.readFlexrayArTpConfig(reparsed, config2)
        channels = config2.getTpChannels()
        assert len(channels) == 1
        loaded = channels[0]
        assert loaded.getAckType() is not None
        assert loaded.getAckType().getValue() == FrArTpAckType.ENUM_ACK_WITH_RT
        assert loaded.getCancellation().getValue() is True
        assert loaded.getExtendedAddressing().getValue() is True
        assert loaded.getMaxAr().getValue() == 3
        assert loaded.getMaxAs().getValue() == 4
        assert loaded.getMaxBs().getValue() == 8
        assert loaded.getMaxFcWait().getValue() == 2
        assert loaded.getMaximumMessageLength().getValue() == MaximumMessageLengthType.ENUM_ISO
        assert loaded.getMaxRetries().getValue() == 1
        assert loaded.getMinimumMulticastSeperationTime().getValue() == 0.0002
        assert loaded.getMinimumSeparationTime().getValue() == 0.0001
        assert loaded.getMulticastSegmentation().getValue() is False
        refs = loaded.getNPduRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/NPdus/N1"
        assert refs[0].getDest() == "N-PDU"
        assert loaded.getTimeBr().getValue() == 0.01
        assert loaded.getTimeCs().getValue() == 0.02
        assert loaded.getTimeoutAr().getValue() == 0.03
        assert loaded.getTimeoutAs().getValue() == 0.04
        assert loaded.getTimeoutBs().getValue() == 0.05
        assert loaded.getTimeoutCr().getValue() == 0.06
        connections = loaded.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getConnectionPrioPdus().getValue() == 16
        assert connections[0].getSourceRef().getValue() == "/Nodes/Src"
        targets = connections[0].getTargetRefs()
        assert len(targets) == 1
        assert targets[0].getValue() == "/Nodes/Tgt"
