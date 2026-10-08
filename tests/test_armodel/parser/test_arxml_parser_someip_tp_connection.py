"""Tests for the readSomeipTpConnection handler (R23-11 SomeipTpConnection, Table 6.265, p.620)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpConnection
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


class TestReadSomeipTpConnection:
    """Tests for readSomeipTpConnection handler (R23-11 SomeipTpConnection, Table 6.265, p.620)."""

    def test_read_someip_tp_connection_full(self, parser):
        element = _snip(
            """
                <TP-CHANNEL-REF DEST="SOMEIP-TP-CHANNEL">/TpConfigs/Config/Chan</TP-CHANNEL-REF>
                <TP-SDU-REF DEST="PDU-TRIGGERING">/PduTriggerings/TpSdu</TP-SDU-REF>
                <TRANSPORT-PDU-REF DEST="PDU-TRIGGERING">/PduTriggerings/TransportPdu</TRANSPORT-PDU-REF>
            """,
            root_tag="SOMEIP-TP-CONNECTION",
        )
        connection = SomeipTpConnection()
        parser.readSomeipTpConnection(element, connection)
        assert connection.getTpChannelRef() is not None
        assert connection.getTpChannelRef().getValue() == "/TpConfigs/Config/Chan"
        assert connection.getTpChannelRef().getDest() == "SOMEIP-TP-CHANNEL"
        assert connection.getTpSduRef() is not None
        assert connection.getTpSduRef().getValue() == "/PduTriggerings/TpSdu"
        assert connection.getTpSduRef().getDest() == "PDU-TRIGGERING"
        assert connection.getTransportPduRef() is not None
        assert connection.getTransportPduRef().getValue() == "/PduTriggerings/TransportPdu"
        assert connection.getTransportPduRef().getDest() == "PDU-TRIGGERING"

    def test_read_someip_tp_connection_partial(self, parser):
        element = _snip(
            """
                <TP-SDU-REF DEST="PDU-TRIGGERING">/PduTriggerings/TpSdu</TP-SDU-REF>
            """,
            root_tag="SOMEIP-TP-CONNECTION",
        )
        connection = SomeipTpConnection()
        parser.readSomeipTpConnection(element, connection)
        assert connection.getTpChannelRef() is None
        assert connection.getTpSduRef().getValue() == "/PduTriggerings/TpSdu"
        assert connection.getTransportPduRef() is None

    def test_read_someip_tp_connection_empty(self, parser):
        element = _snip("", root_tag="SOMEIP-TP-CONNECTION")
        connection = SomeipTpConnection()
        parser.readSomeipTpConnection(element, connection)
        assert connection.getTpChannelRef() is None
        assert connection.getTpSduRef() is None
        assert connection.getTransportPduRef() is None
