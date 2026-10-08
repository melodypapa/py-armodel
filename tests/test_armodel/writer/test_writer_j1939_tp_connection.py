"""Tests for the writeJ1939TpConnection handler (R23-11 J1939TpConnection, Table 6.268, p.625)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpConnection, J1939TpPg
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "IDENT",
    "BROADCAST",
    "BUFFER-RATIO",
    "CANCELLATION",
    "DATA-PDU-REF",
    "DYNAMIC-BS",
    "FLOW-CONTROL-PDU-REFS",
    "MAX-BS",
    "MAX-EXP-BS",
    "RECEIVER-REFS",
    "RETRY",
    "TP-PGS",
    "TRANSMITTER-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _positive(value):
    integer = PositiveInteger()
    integer.setValue(str(value))
    return integer


def _int(value):
    integer = Integer()
    integer.setValue(str(value))
    return integer


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _fill_connection(connection: J1939TpConnection) -> J1939TpConnection:
    connection.createTpConnectionIdent("J1939Ident")
    connection.setBroadcast(_bool(True))
    connection.setBufferRatio(_positive(75))
    connection.setCancellation(_bool(True))
    connection.setDataPduRef(_ref("/Pdus/Data"))
    connection.setDynamicBs(_bool(True))
    connection.addFlowControlPduRef(_ref("/Pdus/FlowControl1"))
    connection.addFlowControlPduRef(_ref("/Pdus/FlowControl2"))
    connection.setMaxBs(_positive(8))
    connection.setMaxExpBs(_positive(16))
    connection.addReceiverRef(_ref("/TpConfigs/Config1/Rx1"))
    connection.addReceiverRef(_ref("/TpConfigs/Config1/Rx2"))
    connection.setRetry(_bool(True))
    tp_pg = J1939TpPg()
    tp_pg.setPgn(_int(61444))
    connection.addTpPg(tp_pg)
    connection.setTransmitterRef(_ref("/TpConfigs/Config1/Tx"))
    return connection


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteJ1939TpConnection:
    def test_children_in_xsd_order(self):
        connection = _fill_connection(J1939TpConnection())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpConnection(parent, connection)

        child = parent.find("J-1939-TP-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert len(child.findall("FLOW-CONTROL-PDU-REFS/FLOW-CONTROL-PDU-REF")) == 2
        assert len(child.findall("RECEIVER-REFS/RECEIVER-REF")) == 2
        assert len(child.findall("TP-PGS/J-1939-TP-PG")) == 1

    def test_empty_connection_writes_no_wrappers(self):
        connection = J1939TpConnection()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpConnection(parent, connection)

        child = parent.find("J-1939-TP-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == []

    def test_round_trip(self):
        connection = _fill_connection(J1939TpConnection())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpConnection(parent, connection)

        reloaded = J1939TpConnection()
        ARXMLParser().readJ1939TpConnection(_with_ns(parent)[0], reloaded)

        assert reloaded.getIdent() is not None
        assert reloaded.getIdent().getShortName() == "J1939Ident"
        assert reloaded.getBroadcast().getValue() is True
        assert reloaded.getBufferRatio().getValue() == 75
        assert reloaded.getCancellation().getValue() is True
        assert reloaded.getDataPduRef().getValue() == "/Pdus/Data"
        assert reloaded.getDynamicBs().getValue() is True
        flow_control_pdu_refs = reloaded.getFlowControlPduRefs()
        assert len(flow_control_pdu_refs) == 2
        assert flow_control_pdu_refs[0].getValue() == "/Pdus/FlowControl1"
        assert flow_control_pdu_refs[1].getValue() == "/Pdus/FlowControl2"
        assert reloaded.getMaxBs().getValue() == 8
        assert reloaded.getMaxExpBs().getValue() == 16
        receiver_refs = reloaded.getReceiverRefs()
        assert len(receiver_refs) == 2
        assert receiver_refs[0].getValue() == "/TpConfigs/Config1/Rx1"
        assert receiver_refs[1].getValue() == "/TpConfigs/Config1/Rx2"
        assert reloaded.getRetry().getValue() is True
        assert len(reloaded.getTpPgs()) == 1
        assert reloaded.getTpPgs()[0].getPgn() is not None
        assert reloaded.getTpPgs()[0].getPgn().getValue() == 61444
        assert reloaded.getTransmitterRef().getValue() == "/TpConfigs/Config1/Tx"

    def test_round_trip_empty(self):
        connection = J1939TpConnection()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpConnection(parent, connection)

        reloaded = J1939TpConnection()
        ARXMLParser().readJ1939TpConnection(_with_ns(parent)[0], reloaded)

        assert reloaded.getFlowControlPduRefs() == []
        assert reloaded.getReceiverRefs() == []
        assert reloaded.getTpPgs() == []
        assert reloaded.getTransmitterRef() is None
