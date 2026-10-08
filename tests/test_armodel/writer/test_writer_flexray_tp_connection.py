"""Tests for the writeFlexrayTpConnection handler (R23-11 FlexrayTpConnection, Table 6.241, p.594)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "IDENT",
    "BANDWIDTH-LIMITATION",
    "DIRECT-TP-SDU-REF",
    "MULTICAST-REF",
    "RECEIVER-REFS",
    "REVERSED-TP-SDU-REF",
    "RX-PDU-POOL-REF",
    "TP-CONNECTION-CONTROL-REF",
    "TRANSMITTER-REF",
    "TX-PDU-POOL-REF",
    "VARIATION-POINT",
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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _fill_connection(connection: FlexrayTpConnection) -> FlexrayTpConnection:
    connection.createTpConnectionIdent("ConnIdent")
    connection.setBandwidthLimitation(Boolean().setValue("true"))
    connection.setDirectTpSduRef(_ref("/Pdus/DirectSdu", "I-PDU"))
    connection.setMulticastRef(_ref("/TpAddresses/Mcast", "TP-ADDRESS"))
    connection.addReceiverRef(_ref("/TpNodes/Rx1", "FLEXRAY-TP-NODE"))
    connection.addReceiverRef(_ref("/TpNodes/Rx2", "FLEXRAY-TP-NODE"))
    connection.setReversedTpSduRef(_ref("/Pdus/ReversedSdu", "I-PDU"))
    connection.setRxPduPoolRef(_ref("/PduPools/RxPool", "FLEXRAY-TP-PDU-POOL"))
    connection.setTpConnectionControlRef(_ref("/Controls/Ctrl1", "FLEXRAY-TP-CONNECTION-CONTROL"))
    connection.setTransmitterRef(_ref("/TpNodes/Tx1", "FLEXRAY-TP-NODE"))
    connection.setTxPduPoolRef(_ref("/PduPools/TxPool", "FLEXRAY-TP-PDU-POOL"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vp1"))
    connection.setVariationPoint(variation_point)
    return connection


class TestWriteFlexrayTpConnection:
    """Tests for writeFlexrayTpConnection handler (R23-11 FlexrayTpConnection, Table 6.241, p.594)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(FlexrayTpConnection())

        parent = _parent()
        writer.writeFlexrayTpConnection(parent, connection)
        child = parent.find("FLEXRAY-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(FlexrayTpConnection())

        parent = _parent()
        writer.writeFlexrayTpConnection(parent, connection)
        child = parent.find("FLEXRAY-TP-CONNECTION")
        assert child.find("IDENT/SHORT-NAME").text == "ConnIdent"
        assert child.find("BANDWIDTH-LIMITATION").text == "true"
        direct_ref = child.find("DIRECT-TP-SDU-REF")
        assert direct_ref.text == "/Pdus/DirectSdu"
        assert direct_ref.get("DEST") == "I-PDU"
        assert child.find("MULTICAST-REF").text == "/TpAddresses/Mcast"
        assert child.find("MULTICAST-REF").get("DEST") == "TP-ADDRESS"
        receivers = child.findall("RECEIVER-REFS/RECEIVER-REF")
        assert len(receivers) == 2
        assert receivers[0].text == "/TpNodes/Rx1"
        assert receivers[0].get("DEST") == "FLEXRAY-TP-NODE"
        assert receivers[1].text == "/TpNodes/Rx2"
        assert child.find("REVERSED-TP-SDU-REF").text == "/Pdus/ReversedSdu"
        assert child.find("RX-PDU-POOL-REF").text == "/PduPools/RxPool"
        assert child.find("TP-CONNECTION-CONTROL-REF").text == "/Controls/Ctrl1"
        assert child.find("TRANSMITTER-REF").text == "/TpNodes/Tx1"
        assert child.find("TX-PDU-POOL-REF").text == "/PduPools/TxPool"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "vp1"

    def test_empty_connection_writes_no_own_elements(self, writer):
        connection = FlexrayTpConnection()

        parent = _parent()
        writer.writeFlexrayTpConnection(parent, connection)
        child = parent.find("FLEXRAY-TP-CONNECTION")
        assert child is not None
        assert len(list(child)) == 0

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(FlexrayTpConnection())

        parent = _parent()
        writer.writeFlexrayTpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = FlexrayTpConnection()
        parser.readFlexrayTpConnection(element, reloaded)
        assert reloaded.getIdent() is not None
        assert reloaded.getIdent().getShortName() == "ConnIdent"
        assert reloaded.getBandwidthLimitation().getValue() is True
        assert reloaded.getDirectTpSduRef().getValue() == "/Pdus/DirectSdu"
        assert reloaded.getDirectTpSduRef().getDest() == "I-PDU"
        assert reloaded.getMulticastRef().getValue() == "/TpAddresses/Mcast"
        assert len(reloaded.getReceiverRefs()) == 2
        assert reloaded.getReceiverRefs()[0].getValue() == "/TpNodes/Rx1"
        assert reloaded.getReceiverRefs()[1].getValue() == "/TpNodes/Rx2"
        assert reloaded.getReversedTpSduRef().getValue() == "/Pdus/ReversedSdu"
        assert reloaded.getRxPduPoolRef().getValue() == "/PduPools/RxPool"
        assert reloaded.getTpConnectionControlRef().getValue() == "/Controls/Ctrl1"
        assert reloaded.getTransmitterRef().getValue() == "/TpNodes/Tx1"
        assert reloaded.getTxPduPoolRef().getValue() == "/PduPools/TxPool"
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"
