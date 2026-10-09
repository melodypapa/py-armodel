"""Tests for the readIEEE1722TpIidcConnection handler (R23-11 IEEE1722TpIidcConnection, Table 6.284, p.648)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpIidcConnection,
)
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


class TestReadIEEE1722TpIidcConnection:
    """Tests for readIEEE1722TpIidcConnection handler (R23-11 IEEE1722TpIidcConnection, Table 6.284, p.648)."""

    def test_read_ieee_1722_tp_iidc_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>IidcStream</SHORT-NAME>
                <MAX-TRANSIT-TIME>0.002</MAX-TRANSIT-TIME>
                <SDU-REFS>
                    <SDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</SDU-REF>
                </SDU-REFS>
                <IIDC-CHANNEL>1</IIDC-CHANNEL>
                <IIDC-DATA-BLOCK-SIZE>128</IIDC-DATA-BLOCK-SIZE>
                <IIDC-FRACTION-NUMBER>2</IIDC-FRACTION-NUMBER>
                <IIDC-SOURCE-PACKET-HEADER>true</IIDC-SOURCE-PACKET-HEADER>
                <IIDC-STREAM-FORMAT>0</IIDC-STREAM-FORMAT>
                <IIDC-SY>255</IIDC-SY>
                <IIDC-T-CODE>16</IIDC-T-CODE>
                <IIDC-TAG>8</IIDC-TAG>
            """,
            root_tag="IEEE-1722-TP-IIDC-CONNECTION",
        )
        connection = IEEE1722TpIidcConnection(None, "IidcStream")
        parser.readIEEE1722TpIidcConnection(element, connection)
        assert connection.getShortName() == "IidcStream"
        assert connection.getMaxTransitTime().getValue() == 0.002
        assert len(connection.getSduRefs()) == 1
        assert connection.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert connection.getIidcChannel().getValue() == 1
        assert connection.getIidcDataBlockSize().getValue() == 128
        assert connection.getIidcFractionNumber().getValue() == 2
        assert connection.getIidcSourcePacketHeader().getValue() is True
        assert connection.getIidcStreamFormat().getValue() == 0
        assert connection.getIidcSy().getValue() == 255
        assert connection.getIidcTCode().getValue() == 16
        assert connection.getIidcTag().getValue() == 8

    def test_read_ieee_1722_tp_iidc_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-IIDC-CONNECTION")
        connection = IEEE1722TpIidcConnection(None, "IidcStream")
        parser.readIEEE1722TpIidcConnection(element, connection)
        assert connection.getIidcChannel() is None
        assert connection.getIidcDataBlockSize() is None
        assert connection.getIidcFractionNumber() is None
        assert connection.getIidcSourcePacketHeader() is None
        assert connection.getIidcStreamFormat() is None
        assert connection.getIidcSy() is None
        assert connection.getIidcTag() is None
        assert connection.getIidcTCode() is None

    def test_ar_package_dispatch(self, parser):
        element = _snip(
            """
                    <SHORT-NAME>Pkg</SHORT-NAME>
                    <ELEMENTS>
                        <IEEE-1722-TP-IIDC-CONNECTION>
                            <SHORT-NAME>IidcConn</SHORT-NAME>
                            <IIDC-CHANNEL>3</IIDC-CHANNEL>
                        </IEEE-1722-TP-IIDC-CONNECTION>
                    </ELEMENTS>
            """,
            root_tag="AR-PACKAGE",
        )
        pkg = AUTOSAR.getInstance().createARPackage("TpConfigs")
        parser.readARPackage(element, pkg)
        connections = [e for e in pkg.getReferrableElements() if e.getShortName() == "IidcConn"]
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, IEEE1722TpIidcConnection)
        assert connection.getIidcChannel().getValue() == 3
