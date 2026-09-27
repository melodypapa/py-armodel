"""Tests for the readDoIpTpConnection handler (R23-11 DoIpTpConnection, Table 6.206, p.555)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpTpConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDoIpTpConnection:
    """Tests for readDoIpTpConnection handler (R23-11 DoIpTpConnection, Table 6.206, p.555)."""

    def test_read_doip_tp_connection_full(self, parser):
        element = _snip(
            """
                <IDENT>
                    <SHORT-NAME>Connection1</SHORT-NAME>
                </IDENT>
                <DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1</DO-IP-SOURCE-ADDRESS-REF>
                <DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2</DO-IP-TARGET-ADDRESS-REF>
                <TP-SDU-REF DEST="PDU-TRIGGERING">/SoAd/PduTriggering1</TP-SDU-REF>
            """,
            root_tag="DO-IP-TP-CONNECTION",
        )
        connection = DoIpTpConnection()
        parser.readDoIpTpConnection(element, connection)
        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "Connection1"
        assert connection.getDoIpSourceAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert connection.getDoIpSourceAddressRef().getDest() == "DO-IP-LOGIC-ADDRESS"
        assert connection.getDoIpTargetAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert connection.getDoIpTargetAddressRef().getDest() == "DO-IP-LOGIC-ADDRESS"
        assert connection.getTpSduRef().getValue() == "/SoAd/PduTriggering1"
        assert connection.getTpSduRef().getDest() == "PDU-TRIGGERING"

    def test_read_doip_tp_connection_empty(self, parser):
        element = _snip("", root_tag="DO-IP-TP-CONNECTION")
        connection = DoIpTpConnection()
        parser.readDoIpTpConnection(element, connection)
        assert connection.getIdent() is None
        assert connection.getDoIpSourceAddressRef() is None
        assert connection.getDoIpTargetAddressRef() is None
        assert connection.getTpSduRef() is None
