"""Writer round-trip tests for LinTpConnection (Table 6.261, p.616).

Element order per XSD group LIN-TP-CONNECTION (AUTOSAR_00052.xsd l.78089):
DATA-PDU-REF, FLOW-CONTROL-REF, LIN-TP-N-SDU-REF, MULTICAST-REF,
RECEIVER-REFS, TIMEOUT-AS, TIMEOUT-CR, TIMEOUT-CS, TRANSMITTER-REF, then
VARIATION-POINT (sequenceOffset 10000). The atp.Status="removed" elements
(DROP-NOT-REQUESTED-NAD, MAX-NUMBER-OF-RESP-PENDING-FRAMES, P-2-MAX,
P-2-TIMING) are not emitted (Rule 0015).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import LinTpConfig, LinTpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

REMOVED_TAGS = [
    "DROP-NOT-REQUESTED-NAD",
    "MAX-NUMBER-OF-RESP-PENDING-FRAMES",
    "P-2-MAX",
    "P-2-TIMING",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _new_connection():
    connection = LinTpConnection()
    connection.createTpConnectionIdent("LinIdent")
    connection.setDataPduRef(_ref("/Pdus/Data", "N-PDU"))
    connection.setFlowControlRef(_ref("/Pdus/FlowControl", "N-PDU"))
    connection.setLinTpNSduRef(_ref("/Pdus/NSdu", "I-PDU"))
    connection.setMulticastRef(_ref("/TpConfigs/Addr", "TP-ADDRESS"))
    connection.addReceiverRef(_ref("/Nodes/Rx1", "LIN-TP-NODE"))
    connection.addReceiverRef(_ref("/Nodes/Rx2", "LIN-TP-NODE"))
    connection.setTimeoutAs(_time("0.1"))
    connection.setTimeoutCr(_time("1.5"))
    connection.setTimeoutCs(_time("0.05"))
    connection.setTransmitterRef(_ref("/Nodes/Tx", "LIN-TP-NODE"))
    return connection


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteLinTpConnection:
    def test_none(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConnection(parent, None)
        assert len(parent) == 0

    def test_empty(self):
        connection = LinTpConnection()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConnection(parent, connection)

        node = parent.find("LIN-TP-CONNECTION")
        assert node is not None
        assert node.find("DATA-PDU-REF") is None
        assert node.find("MULTICAST-REF") is None
        assert node.find("RECEIVER-REFS") is None
        for tag in REMOVED_TAGS:
            assert node.find(tag) is None

    def test_full_element_order_and_values(self):
        connection = _new_connection()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConnection(parent, connection)

        node = parent.find("LIN-TP-CONNECTION")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags == [
            "IDENT",
            "DATA-PDU-REF",
            "FLOW-CONTROL-REF",
            "LIN-TP-N-SDU-REF",
            "MULTICAST-REF",
            "RECEIVER-REFS",
            "TIMEOUT-AS",
            "TIMEOUT-CR",
            "TIMEOUT-CS",
            "TRANSMITTER-REF",
        ]

        assert node.find("IDENT/SHORT-NAME").text == "LinIdent"
        assert node.find("DATA-PDU-REF").text == "/Pdus/Data"
        assert node.find("DATA-PDU-REF").attrib["DEST"] == "N-PDU"
        assert node.find("FLOW-CONTROL-REF").text == "/Pdus/FlowControl"
        assert node.find("LIN-TP-N-SDU-REF").text == "/Pdus/NSdu"
        assert node.find("MULTICAST-REF").text == "/TpConfigs/Addr"
        assert node.find("MULTICAST-REF").attrib["DEST"] == "TP-ADDRESS"
        receiver_refs = node.findall("RECEIVER-REFS/RECEIVER-REF")
        assert [r.text for r in receiver_refs] == ["/Nodes/Rx1", "/Nodes/Rx2"]
        assert node.find("TIMEOUT-AS").text == "0.1"
        assert node.find("TIMEOUT-CR").text == "1.5"
        assert node.find("TIMEOUT-CS").text == "0.05"
        assert node.find("TRANSMITTER-REF").text == "/Nodes/Tx"
        for tag in REMOVED_TAGS:
            assert node.find(tag) is None

    def test_round_trip(self):
        connection = _new_connection()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConnection(parent, connection)

        reloaded = LinTpConnection()
        ARXMLParser().readLinTpConnection(_with_ns(parent)[0], reloaded)

        assert reloaded.getIdent().getShortName() == "LinIdent"
        assert reloaded.getDataPduRef().getValue() == "/Pdus/Data"
        assert reloaded.getFlowControlRef().getValue() == "/Pdus/FlowControl"
        assert reloaded.getLinTpNSduRef().getValue() == "/Pdus/NSdu"
        assert reloaded.getMulticastRef().getValue() == "/TpConfigs/Addr"
        assert [r.getValue() for r in reloaded.getReceiverRefs()] == ["/Nodes/Rx1", "/Nodes/Rx2"]
        assert reloaded.getTimeoutAs().getValue() == 0.1
        assert reloaded.getTimeoutCr().getValue() == 1.5
        assert reloaded.getTimeoutCs().getValue() == 0.05
        assert reloaded.getTransmitterRef().getValue() == "/Nodes/Tx"


class TestWriteLinTpConfigTpConnectionsRoundTrip:
    def test_full_round_trip(self):
        config = LinTpConfig(MockParent(), "LinTp")
        config.addTpConnection(_new_connection())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConfigTpConnections(parent, config)

        wrapper = parent.find("TP-CONNECTIONS")
        assert wrapper is not None
        nodes = wrapper.findall("LIN-TP-CONNECTION")
        assert len(nodes) == 1
        assert nodes[0].find("MULTICAST-REF").text == "/TpConfigs/Addr"

        reloaded = LinTpConfig(MockParent(), "LinTp")
        ARXMLParser().readLinTpConfigTpConnections(_with_ns(parent), reloaded)
        connections = reloaded.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getMulticastRef().getValue() == "/TpConfigs/Addr"
        assert [r.getValue() for r in connections[0].getReceiverRefs()] == ["/Nodes/Rx1", "/Nodes/Rx2"]
        assert connections[0].getTimeoutCs().getValue() == 0.05
