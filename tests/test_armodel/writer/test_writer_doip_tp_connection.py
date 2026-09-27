"""Tests for the writeDoIpTpConnection handler (R23-11 DoIpTpConnection, Table 6.206, p.555)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _filled_connection() -> DoIpTpConnection:
    connection = DoIpTpConnection()
    connection.createTpConnectionIdent("Connection1")
    connection.setDoIpSourceAddressRef(_ref("/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1", "DO-IP-LOGIC-ADDRESS"))
    connection.setDoIpTargetAddressRef(_ref("/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2", "DO-IP-LOGIC-ADDRESS"))
    connection.setTpSduRef(_ref("/SoAd/PduTriggering1", "PDU-TRIGGERING"))
    return connection


class TestWriteDoIpTpConnection:
    """Tests for the writeDoIpTpConnection handler (R23-11 DoIpTpConnection, Table 6.206, p.555)."""

    def test_write_full_in_xsd_order(self, writer):
        connection = _filled_connection()

        parent = _parent()
        writer.writeDoIpTpConnection(parent, connection)
        child = parent.find("DO-IP-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == ["IDENT", "DO-IP-SOURCE-ADDRESS-REF", "DO-IP-TARGET-ADDRESS-REF", "TP-SDU-REF"]
        assert child.find("IDENT/SHORT-NAME").text == "Connection1"
        source_ref = child.find("DO-IP-SOURCE-ADDRESS-REF")
        assert source_ref.text == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert source_ref.get("DEST") == "DO-IP-LOGIC-ADDRESS"
        target_ref = child.find("DO-IP-TARGET-ADDRESS-REF")
        assert target_ref.text == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert target_ref.get("DEST") == "DO-IP-LOGIC-ADDRESS"
        tp_sdu_ref = child.find("TP-SDU-REF")
        assert tp_sdu_ref.text == "/SoAd/PduTriggering1"
        assert tp_sdu_ref.get("DEST") == "PDU-TRIGGERING"

    def test_write_empty_connection_omits_refs(self, writer):
        connection = DoIpTpConnection()

        parent = _parent()
        writer.writeDoIpTpConnection(parent, connection)
        child = parent.find("DO-IP-TP-CONNECTION")
        assert child is not None
        assert child.find("IDENT") is None
        assert child.find("DO-IP-SOURCE-ADDRESS-REF") is None
        assert child.find("DO-IP-TARGET-ADDRESS-REF") is None
        assert child.find("TP-SDU-REF") is None

    def test_round_trip(self, writer, parser):
        connection = _filled_connection()

        parent = _parent()
        writer.writeDoIpTpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reparsed = DoIpTpConnection()
        parser.readDoIpTpConnection(parser.find(element, "DO-IP-TP-CONNECTION"), reparsed)
        assert reparsed.getIdent() is not None
        assert reparsed.getIdent().getShortName() == "Connection1"
        assert reparsed.getDoIpSourceAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert reparsed.getDoIpSourceAddressRef().getDest() == "DO-IP-LOGIC-ADDRESS"
        assert reparsed.getDoIpTargetAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert reparsed.getTpSduRef().getValue() == "/SoAd/PduTriggering1"
        assert reparsed.getTpSduRef().getDest() == "PDU-TRIGGERING"
