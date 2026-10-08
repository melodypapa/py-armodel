"""Tests for the readJ1939TpConnection handler (R23-11 J1939TpConnection, Table 6.268, p.625).

XSD element order (J-1939-TP-CONNECTION group, AUTOSAR_00052.xsd l.75713): BROADCAST,
BUFFER-RATIO, CANCELLATION, DATA-PDU-REF, DYNAMIC-BS, FLOW-CONTROL-PDU-REFS, MAX-BS,
MAX-EXP-BS, RECEIVER-REFS, RETRY, TP-PGS, TRANSMITTER-REF, then VARIATION-POINT
(sequenceOffset 10000, last).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

CONNECTION_XML = (
    "<J-1939-TP-CONNECTION>"
    "<IDENT><SHORT-NAME>J1939Ident</SHORT-NAME></IDENT>"
    "<BROADCAST>true</BROADCAST>"
    "<BUFFER-RATIO>75</BUFFER-RATIO>"
    "<CANCELLATION>true</CANCELLATION>"
    '<DATA-PDU-REF DEST="N-PDU">/Pdus/Data</DATA-PDU-REF>'
    "<DYNAMIC-BS>true</DYNAMIC-BS>"
    "<FLOW-CONTROL-PDU-REFS>"
    '<FLOW-CONTROL-PDU-REF DEST="N-PDU">/Pdus/FlowControl1</FLOW-CONTROL-PDU-REF>'
    '<FLOW-CONTROL-PDU-REF DEST="N-PDU">/Pdus/FlowControl2</FLOW-CONTROL-PDU-REF>'
    "</FLOW-CONTROL-PDU-REFS>"
    "<MAX-BS>8</MAX-BS>"
    "<MAX-EXP-BS>16</MAX-EXP-BS>"
    "<RECEIVER-REFS>"
    '<RECEIVER-REF DEST="J-1939-TP-NODE">/TpConfigs/Config1/Rx1</RECEIVER-REF>'
    '<RECEIVER-REF DEST="J-1939-TP-NODE">/TpConfigs/Config1/Rx2</RECEIVER-REF>'
    "</RECEIVER-REFS>"
    "<RETRY>true</RETRY>"
    "<TP-PGS>"
    "<J-1939-TP-PG />"
    "</TP-PGS>"
    '<TRANSMITTER-REF DEST="J-1939-TP-NODE">/TpConfigs/Config1/Tx</TRANSMITTER-REF>'
    "<VARIATION-POINT />"
    "</J-1939-TP-CONNECTION>"
)

EMPTY_CONNECTION_XML = "<J-1939-TP-CONNECTION />"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadJ1939TpConnection:
    def test_read_full(self):
        connection = J1939TpConnection()
        root = _snip(CONNECTION_XML)
        ARXMLParser().readJ1939TpConnection(root[0], connection)

        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "J1939Ident"

        assert connection.getBroadcast() is not None
        assert connection.getBroadcast().getValue() is True

        assert connection.getBufferRatio() is not None
        assert connection.getBufferRatio().getValue() == 75

        assert connection.getCancellation() is not None
        assert connection.getCancellation().getValue() is True

        data_pdu_ref = connection.getDataPduRef()
        assert data_pdu_ref.getValue() == "/Pdus/Data"
        assert data_pdu_ref.getDest() == "N-PDU"

        assert connection.getDynamicBs() is not None
        assert connection.getDynamicBs().getValue() is True

        flow_control_pdu_refs = connection.getFlowControlPduRefs()
        assert len(flow_control_pdu_refs) == 2
        assert flow_control_pdu_refs[0].getValue() == "/Pdus/FlowControl1"
        assert flow_control_pdu_refs[0].getDest() == "N-PDU"
        assert flow_control_pdu_refs[1].getValue() == "/Pdus/FlowControl2"

        assert connection.getMaxBs() is not None
        assert connection.getMaxBs().getValue() == 8

        assert connection.getMaxExpBs() is not None
        assert connection.getMaxExpBs().getValue() == 16

        receiver_refs = connection.getReceiverRefs()
        assert len(receiver_refs) == 2
        assert receiver_refs[0].getValue() == "/TpConfigs/Config1/Rx1"
        assert receiver_refs[0].getDest() == "J-1939-TP-NODE"
        assert receiver_refs[1].getValue() == "/TpConfigs/Config1/Rx2"

        assert connection.getRetry() is not None
        assert connection.getRetry().getValue() is True

        assert len(connection.getTpPgs()) == 1

        transmitter_ref = connection.getTransmitterRef()
        assert transmitter_ref.getValue() == "/TpConfigs/Config1/Tx"
        assert transmitter_ref.getDest() == "J-1939-TP-NODE"

        assert connection.getVariationPoint() is not None

    def test_read_empty(self):
        connection = J1939TpConnection()
        root = _snip(EMPTY_CONNECTION_XML)
        ARXMLParser().readJ1939TpConnection(root[0], connection)

        assert connection.getIdent() is None
        assert connection.getBroadcast() is None
        assert connection.getBufferRatio() is None
        assert connection.getCancellation() is None
        assert connection.getDataPduRef() is None
        assert connection.getDynamicBs() is None
        assert connection.getFlowControlPduRefs() == []
        assert connection.getMaxBs() is None
        assert connection.getMaxExpBs() is None
        assert connection.getReceiverRefs() == []
        assert connection.getRetry() is None
        assert connection.getTpPgs() == []
        assert connection.getTransmitterRef() is None
        assert connection.getVariationPoint() is None
