"""Tests for the readEthTpConnection handler (R23-11 EthTpConnection, Table 6.263, p.618)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import EthTpConnection
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


class TestReadEthTpConnection:
    """Tests for readEthTpConnection handler (R23-11 EthTpConnection, Table 6.263, p.618)."""

    def test_read_eth_tp_connection_full(self, parser):
        element = _snip(
            """
                <IDENT>
                    <SHORT-NAME>EthConnIdent</SHORT-NAME>
                </IDENT>
                <TP-SDU-REFS>
                    <TP-SDU-REF DEST="PDU-TRIGGERING">/PduTriggerings/Tp1</TP-SDU-REF>
                    <TP-SDU-REF DEST="PDU-TRIGGERING">/PduTriggerings/Tp2</TP-SDU-REF>
                </TP-SDU-REFS>
            """,
            root_tag="ETH-TP-CONNECTION",
        )
        connection = EthTpConnection()
        parser.readEthTpConnection(element, connection)
        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "EthConnIdent"
        tp_sdu_refs = connection.getTpSduRefs()
        assert len(tp_sdu_refs) == 2
        assert tp_sdu_refs[0].getValue() == "/PduTriggerings/Tp1"
        assert tp_sdu_refs[0].getDest() == "PDU-TRIGGERING"
        assert tp_sdu_refs[1].getValue() == "/PduTriggerings/Tp2"

    def test_read_eth_tp_connection_empty(self, parser):
        element = _snip("", root_tag="ETH-TP-CONNECTION")
        connection = EthTpConnection()
        parser.readEthTpConnection(element, connection)
        assert connection.getIdent() is None
        assert connection.getTpSduRefs() == []
