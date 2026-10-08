"""Tests for the writeEthTpConnection handler (R23-11 EthTpConnection, Table 6.263, p.618)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import EthTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "IDENT",
    "TP-SDU-REFS",
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


def _fill_connection(connection: EthTpConnection) -> EthTpConnection:
    connection.createTpConnectionIdent("EthConnIdent")
    connection.addTpSduRef(_ref("/PduTriggerings/Tp1", "PDU-TRIGGERING"))
    connection.addTpSduRef(_ref("/PduTriggerings/Tp2", "PDU-TRIGGERING"))
    return connection


class TestWriteEthTpConnection:
    """Tests for writeEthTpConnection handler (R23-11 EthTpConnection, Table 6.263, p.618)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(EthTpConnection())

        parent = _parent()
        writer.writeEthTpConnection(parent, connection)
        child = parent.find("ETH-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(EthTpConnection())

        parent = _parent()
        writer.writeEthTpConnection(parent, connection)
        child = parent.find("ETH-TP-CONNECTION")
        assert child.find("IDENT/SHORT-NAME").text == "EthConnIdent"
        tp_sdu_refs = child.findall("TP-SDU-REFS/TP-SDU-REF")
        assert len(tp_sdu_refs) == 2
        assert tp_sdu_refs[0].text == "/PduTriggerings/Tp1"
        assert tp_sdu_refs[0].get("DEST") == "PDU-TRIGGERING"
        assert tp_sdu_refs[1].text == "/PduTriggerings/Tp2"

    def test_empty_connection_writes_no_own_elements(self, writer):
        connection = EthTpConnection()

        parent = _parent()
        writer.writeEthTpConnection(parent, connection)
        child = parent.find("ETH-TP-CONNECTION")
        assert child is not None
        assert len(list(child)) == 0

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(EthTpConnection())

        parent = _parent()
        writer.writeEthTpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = EthTpConnection()
        parser.readEthTpConnection(element, reloaded)
        assert reloaded.getIdent() is not None
        assert reloaded.getIdent().getShortName() == "EthConnIdent"
        tp_sdu_refs = reloaded.getTpSduRefs()
        assert len(tp_sdu_refs) == 2
        assert tp_sdu_refs[0].getValue() == "/PduTriggerings/Tp1"
        assert tp_sdu_refs[0].getDest() == "PDU-TRIGGERING"
        assert tp_sdu_refs[1].getValue() == "/PduTriggerings/Tp2"
