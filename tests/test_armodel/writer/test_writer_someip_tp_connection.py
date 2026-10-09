"""Tests for the writeSomeipTpConnection handler (R23-11 SomeipTpConnection, Table 6.265, p.620)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "TP-CHANNEL-REF",
    "TP-SDU-REF",
    "TRANSPORT-PDU-REF",
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


def _fill_connection(connection: SomeipTpConnection) -> SomeipTpConnection:
    connection.setTpChannelRef(_ref("/TpConfigs/Config/Chan", "SOMEIP-TP-CHANNEL"))
    connection.setTpSduRef(_ref("/PduTriggerings/TpSdu", "PDU-TRIGGERING"))
    connection.setTransportPduRef(_ref("/PduTriggerings/TransportPdu", "PDU-TRIGGERING"))
    return connection


class TestWriteSomeipTpConnection:
    """Tests for writeSomeipTpConnection handler (R23-11 SomeipTpConnection, Table 6.265, p.620)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(SomeipTpConnection())

        parent = _parent()
        writer.writeSomeipTpConnection(parent, connection)
        child = parent.find("SOMEIP-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(SomeipTpConnection())

        parent = _parent()
        writer.writeSomeipTpConnection(parent, connection)
        child = parent.find("SOMEIP-TP-CONNECTION")
        tp_channel_ref = child.find("TP-CHANNEL-REF")
        assert tp_channel_ref.text == "/TpConfigs/Config/Chan"
        assert tp_channel_ref.get("DEST") == "SOMEIP-TP-CHANNEL"
        tp_sdu_ref = child.find("TP-SDU-REF")
        assert tp_sdu_ref.text == "/PduTriggerings/TpSdu"
        assert tp_sdu_ref.get("DEST") == "PDU-TRIGGERING"
        transport_pdu_ref = child.find("TRANSPORT-PDU-REF")
        assert transport_pdu_ref.text == "/PduTriggerings/TransportPdu"
        assert transport_pdu_ref.get("DEST") == "PDU-TRIGGERING"

    def test_empty_connection_writes_no_own_elements(self, writer):
        connection = SomeipTpConnection()

        parent = _parent()
        writer.writeSomeipTpConnection(parent, connection)
        child = parent.find("SOMEIP-TP-CONNECTION")
        assert child is not None
        assert len(list(child)) == 0

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(SomeipTpConnection())

        parent = _parent()
        writer.writeSomeipTpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = SomeipTpConnection()
        parser.readSomeipTpConnection(element, reloaded)
        assert reloaded.getTpChannelRef() is not None
        assert reloaded.getTpChannelRef().getValue() == "/TpConfigs/Config/Chan"
        assert reloaded.getTpChannelRef().getDest() == "SOMEIP-TP-CHANNEL"
        assert reloaded.getTpSduRef() is not None
        assert reloaded.getTpSduRef().getValue() == "/PduTriggerings/TpSdu"
        assert reloaded.getTpSduRef().getDest() == "PDU-TRIGGERING"
        assert reloaded.getTransportPduRef() is not None
        assert reloaded.getTransportPduRef().getValue() == "/PduTriggerings/TransportPdu"
        assert reloaded.getTransportPduRef().getDest() == "PDU-TRIGGERING"
