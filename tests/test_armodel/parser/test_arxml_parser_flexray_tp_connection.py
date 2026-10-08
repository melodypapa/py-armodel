"""Tests for the readFlexrayTpConnection handler (R23-11 FlexrayTpConnection, Table 6.241, p.594)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _connection() -> FlexrayTpConnection:
    return FlexrayTpConnection()


class TestReadFlexrayTpConnection:
    """Tests for readFlexrayTpConnection handler (R23-11 FlexrayTpConnection, Table 6.241, p.594)."""

    def test_read_flexray_tp_connection_full(self, parser):
        element = _snip(
            """
                <IDENT>
                    <SHORT-NAME>ConnIdent</SHORT-NAME>
                </IDENT>
                <BANDWIDTH-LIMITATION>true</BANDWIDTH-LIMITATION>
                <DIRECT-TP-SDU-REF DEST="I-PDU">/Pdus/DirectSdu</DIRECT-TP-SDU-REF>
                <MULTICAST-REF DEST="TP-ADDRESS">/TpAddresses/Mcast</MULTICAST-REF>
                <RECEIVER-REFS>
                    <RECEIVER-REF DEST="FLEXRAY-TP-NODE">/TpNodes/Rx1</RECEIVER-REF>
                    <RECEIVER-REF DEST="FLEXRAY-TP-NODE">/TpNodes/Rx2</RECEIVER-REF>
                </RECEIVER-REFS>
                <REVERSED-TP-SDU-REF DEST="I-PDU">/Pdus/ReversedSdu</REVERSED-TP-SDU-REF>
                <RX-PDU-POOL-REF DEST="FLEXRAY-TP-PDU-POOL">/PduPools/RxPool</RX-PDU-POOL-REF>
                <TP-CONNECTION-CONTROL-REF DEST="FLEXRAY-TP-CONNECTION-CONTROL">/Controls/Ctrl1</TP-CONNECTION-CONTROL-REF>
                <TRANSMITTER-REF DEST="FLEXRAY-TP-NODE">/TpNodes/Tx1</TRANSMITTER-REF>
                <TX-PDU-POOL-REF DEST="FLEXRAY-TP-PDU-POOL">/PduPools/TxPool</TX-PDU-POOL-REF>
                <VARIATION-POINT>
                    <SHORT-LABEL>vp1</SHORT-LABEL>
                </VARIATION-POINT>
            """,
            root_tag="FLEXRAY-TP-CONNECTION",
        )
        connection = _connection()
        parser.readFlexrayTpConnection(element, connection)
        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "ConnIdent"
        assert connection.getBandwidthLimitation().getValue() is True
        assert connection.getDirectTpSduRef().getValue() == "/Pdus/DirectSdu"
        assert connection.getDirectTpSduRef().getDest() == "I-PDU"
        assert connection.getMulticastRef().getValue() == "/TpAddresses/Mcast"
        assert connection.getMulticastRef().getDest() == "TP-ADDRESS"
        receivers = connection.getReceiverRefs()
        assert len(receivers) == 2
        assert receivers[0].getValue() == "/TpNodes/Rx1"
        assert receivers[0].getDest() == "FLEXRAY-TP-NODE"
        assert receivers[1].getValue() == "/TpNodes/Rx2"
        assert connection.getReversedTpSduRef().getValue() == "/Pdus/ReversedSdu"
        assert connection.getRxPduPoolRef().getValue() == "/PduPools/RxPool"
        assert connection.getRxPduPoolRef().getDest() == "FLEXRAY-TP-PDU-POOL"
        assert connection.getTpConnectionControlRef().getValue() == "/Controls/Ctrl1"
        assert connection.getTransmitterRef().getValue() == "/TpNodes/Tx1"
        assert connection.getTxPduPoolRef().getValue() == "/PduPools/TxPool"
        assert connection.getVariationPoint() is not None
        assert connection.getVariationPoint().getShortLabel().getValue() == "vp1"

    def test_read_flexray_tp_connection_empty(self, parser):
        element = _snip("", root_tag="FLEXRAY-TP-CONNECTION")
        connection = _connection()
        parser.readFlexrayTpConnection(element, connection)
        assert connection.getIdent() is None
        assert connection.getBandwidthLimitation() is None
        assert connection.getDirectTpSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getReversedTpSduRef() is None
        assert connection.getRxPduPoolRef() is None
        assert connection.getTpConnectionControlRef() is None
        assert connection.getTransmitterRef() is None
        assert connection.getTxPduPoolRef() is None
        assert connection.getVariationPoint() is None
