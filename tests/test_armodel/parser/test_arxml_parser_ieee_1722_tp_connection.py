"""Tests for the readIEEE1722TpConnection handler (R23-11 IEEE1722TpConnection, Table 6.275, p.637)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _Conn(IEEE1722TpConnection):
    pass


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


class TestReadIEEE1722TpConnection:
    """Tests for readIEEE1722TpConnection handler (R23-11 IEEE1722TpConnection, Table 6.275, p.637)."""

    def test_read_ieee_1722_tp_connection_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>StreamConn</SHORT-NAME>
                <DESTINATION-MAC-ADDRESS>02:00:00:00:00:01</DESTINATION-MAC-ADDRESS>
                <MAC-ADDRESS-STREAM-ID>91:E0:F0:00:FE:00</MAC-ADDRESS-STREAM-ID>
                <PDU-REF DEST="PDU-TRIGGERING">/Pkgs/Pt1</PDU-REF>
                <UNIQUE-STREAM-ID>42</UNIQUE-STREAM-ID>
                <VERSION>2</VERSION>
                <VLAN-PRIORITY>5</VLAN-PRIORITY>
            """,
            root_tag="IEEE-1722-TP-CONNECTION",
        )
        connection = _Conn(None, "StreamConn")
        parser.readIEEE1722TpConnection(element, connection)
        assert connection.getShortName() == "StreamConn"
        assert connection.getDestinationMacAddress().getValue() == "02:00:00:00:00:01"
        assert connection.getMacAddressStreamId().getValue() == "91:E0:F0:00:FE:00"
        assert connection.getPduRef().getValue() == "/Pkgs/Pt1"
        assert connection.getPduRef().getDest() == "PDU-TRIGGERING"
        assert connection.getUniqueStreamId().getValue() == 42
        assert connection.getVersion().getValue() == 2
        assert connection.getVlanPriority().getValue() == 5

    def test_read_ieee_1722_tp_connection_empty(self, parser):
        element = _snip("", root_tag="IEEE-1722-TP-CONNECTION")
        connection = _Conn(None, "StreamConn")
        parser.readIEEE1722TpConnection(element, connection)
        assert connection.getDestinationMacAddress() is None
        assert connection.getMacAddressStreamId() is None
        assert connection.getPduRef() is None
        assert connection.getUniqueStreamId() is None
        assert connection.getVersion() is None
        assert connection.getVlanPriority() is None
