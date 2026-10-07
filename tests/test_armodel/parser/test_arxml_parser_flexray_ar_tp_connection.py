"""Tests for the readFlexrayArTpConnection handler (R23-11 FlexrayArTpConnection, Table 6.248, p.603)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConnection
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


def _connection() -> FlexrayArTpConnection:
    return FlexrayArTpConnection()


class TestReadFlexrayArTpConnection:
    """Tests for readFlexrayArTpConnection handler (R23-11 FlexrayArTpConnection, Table 6.248, p.603)."""

    def test_read_flexray_ar_tp_connection_full(self, parser):
        element = _snip(
            """
                <IDENT>
                    <SHORT-NAME>FrArConnIdent</SHORT-NAME>
                </IDENT>
                <CONNECTION-PRIO-PDUS>8</CONNECTION-PRIO-PDUS>
                <DIRECT-TP-SDU-REF DEST="I-PDU">/Pdus/DirectSdu</DIRECT-TP-SDU-REF>
                <MULTICAST-REF DEST="TP-ADDRESS">/TpAddresses/Mcast</MULTICAST-REF>
                <REVERSED-TP-SDU-REF DEST="I-PDU">/Pdus/ReversedSdu</REVERSED-TP-SDU-REF>
                <SOURCE-REF DEST="FLEXRAY-AR-TP-NODE">/TpNodes/Src</SOURCE-REF>
                <TARGET-REFS>
                    <TARGET-REF DEST="FLEXRAY-AR-TP-NODE">/TpNodes/Tgt1</TARGET-REF>
                    <TARGET-REF DEST="FLEXRAY-AR-TP-NODE">/TpNodes/Tgt2</TARGET-REF>
                </TARGET-REFS>
            """,
            root_tag="FLEXRAY-AR-TP-CONNECTION",
        )
        connection = _connection()
        parser.readFlexrayArTpConnection(element, connection)
        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "FrArConnIdent"
        assert connection.getConnectionPrioPdus().getValue() == 8
        assert connection.getDirectTpSduRef().getValue() == "/Pdus/DirectSdu"
        assert connection.getDirectTpSduRef().getDest() == "I-PDU"
        assert connection.getMulticastRef().getValue() == "/TpAddresses/Mcast"
        assert connection.getMulticastRef().getDest() == "TP-ADDRESS"
        assert connection.getReversedTpSduRef().getValue() == "/Pdus/ReversedSdu"
        assert connection.getSourceRef().getValue() == "/TpNodes/Src"
        assert connection.getSourceRef().getDest() == "FLEXRAY-AR-TP-NODE"
        targets = connection.getTargetRefs()
        assert len(targets) == 2
        assert targets[0].getValue() == "/TpNodes/Tgt1"
        assert targets[0].getDest() == "FLEXRAY-AR-TP-NODE"
        assert targets[1].getValue() == "/TpNodes/Tgt2"

    def test_read_flexray_ar_tp_connection_empty(self, parser):
        element = _snip("", root_tag="FLEXRAY-AR-TP-CONNECTION")
        connection = _connection()
        parser.readFlexrayArTpConnection(element, connection)
        assert connection.getIdent() is None
        assert connection.getConnectionPrioPdus() is None
        assert connection.getDirectTpSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReversedTpSduRef() is None
        assert connection.getSourceRef() is None
        assert connection.getTargetRefs() == []
