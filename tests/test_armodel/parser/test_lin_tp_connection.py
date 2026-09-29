"""Parser tests for LinTpConnection (Table 6.261, p.616).

TpConnection concrete subclass serialized through LIN-TP-CONNECTION
(XSD group LIN-TP-CONNECTION, AUTOSAR_00052.xsd l.78089): DATA-PDU-REF,
FLOW-CONTROL-REF, LIN-TP-N-SDU-REF, MULTICAST-REF, RECEIVER-REFS,
TIMEOUT-AS, TIMEOUT-CR, TIMEOUT-CS, TRANSMITTER-REF, then VARIATION-POINT
(sequenceOffset 10000). The XSD's DROP-NOT-REQUESTED-NAD /
MAX-NUMBER-OF-RESP-PENDING-FRAMES / P-2-MAX / P-2-TIMING carry
atp.Status="removed" and are not modeled (Rule 0015).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import LinTpConfig, LinTpConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


CONNECTION_XML = (
    "<LIN-TP-CONNECTION>"
    "<IDENT><SHORT-NAME>LinIdent</SHORT-NAME></IDENT>"
    '<DATA-PDU-REF DEST="N-PDU">/Pdus/Data</DATA-PDU-REF>'
    '<FLOW-CONTROL-REF DEST="N-PDU">/Pdus/FlowControl</FLOW-CONTROL-REF>'
    '<LIN-TP-N-SDU-REF DEST="I-PDU">/Pdus/NSdu</LIN-TP-N-SDU-REF>'
    '<MULTICAST-REF DEST="TP-ADDRESS">/TpConfigs/Addr</MULTICAST-REF>'
    "<RECEIVER-REFS>"
    '<RECEIVER-REF DEST="LIN-TP-NODE">/Nodes/Rx1</RECEIVER-REF>'
    '<RECEIVER-REF DEST="LIN-TP-NODE">/Nodes/Rx2</RECEIVER-REF>'
    "</RECEIVER-REFS>"
    "<TIMEOUT-AS>0.1</TIMEOUT-AS>"
    "<TIMEOUT-CR>1.5</TIMEOUT-CR>"
    "<TIMEOUT-CS>0.05</TIMEOUT-CS>"
    '<TRANSMITTER-REF DEST="LIN-TP-NODE">/Nodes/Tx</TRANSMITTER-REF>'
    "<VARIATION-POINT />"
    "</LIN-TP-CONNECTION>"
)


class TestReadLinTpConnection:
    def test_read_full(self):
        connection = LinTpConnection()
        root = _snip(CONNECTION_XML)
        ARXMLParser().readLinTpConnection(root[0], connection)

        assert connection.getIdent() is not None
        assert connection.getIdent().getShortName() == "LinIdent"

        data_pdu_ref = connection.getDataPduRef()
        assert data_pdu_ref.getValue() == "/Pdus/Data"
        assert data_pdu_ref.getDest() == "N-PDU"

        flow_control_ref = connection.getFlowControlRef()
        assert flow_control_ref.getValue() == "/Pdus/FlowControl"
        assert flow_control_ref.getDest() == "N-PDU"

        lin_tp_n_sdu_ref = connection.getLinTpNSduRef()
        assert lin_tp_n_sdu_ref.getValue() == "/Pdus/NSdu"
        assert lin_tp_n_sdu_ref.getDest() == "I-PDU"

        multicast_ref = connection.getMulticastRef()
        assert multicast_ref is not None
        assert multicast_ref.getValue() == "/TpConfigs/Addr"
        assert multicast_ref.getDest() == "TP-ADDRESS"

        receiver_refs = connection.getReceiverRefs()
        assert [r.getValue() for r in receiver_refs] == ["/Nodes/Rx1", "/Nodes/Rx2"]
        assert all(r.getDest() == "LIN-TP-NODE" for r in receiver_refs)

        assert connection.getTimeoutAs().getValue() == 0.1
        assert connection.getTimeoutCr().getValue() == 1.5
        assert connection.getTimeoutCs().getValue() == 0.05

        transmitter_ref = connection.getTransmitterRef()
        assert transmitter_ref.getValue() == "/Nodes/Tx"
        assert transmitter_ref.getDest() == "LIN-TP-NODE"

        assert connection.getVariationPoint() is not None

    def test_read_empty(self):
        connection = LinTpConnection()
        root = _snip("<LIN-TP-CONNECTION />")
        ARXMLParser().readLinTpConnection(root[0], connection)

        assert connection.getIdent() is None
        assert connection.getDataPduRef() is None
        assert connection.getFlowControlRef() is None
        assert connection.getLinTpNSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getTimeoutAs() is None
        assert connection.getTimeoutCr() is None
        assert connection.getTimeoutCs() is None
        assert connection.getTransmitterRef() is None
        assert connection.getVariationPoint() is None


class TestReadLinTpConfigTpConnections:
    def test_dispatch_and_round_trip(self):
        config = LinTpConfig(MockParent(), "LinTp")
        root = _snip("<LIN-TP-CONFIG>" "<SHORT-NAME>LinTp</SHORT-NAME>" "<TP-CONNECTIONS>%s</TP-CONNECTIONS>" "</LIN-TP-CONFIG>" % CONNECTION_XML)
        ARXMLParser().readLinTpConfigTpConnections(root[0], config)

        connections = config.getTpConnections()
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, LinTpConnection)
        assert connection.getDataPduRef().getValue() == "/Pdus/Data"
        assert connection.getMulticastRef().getValue() == "/TpConfigs/Addr"
        assert [r.getValue() for r in connection.getReceiverRefs()] == ["/Nodes/Rx1", "/Nodes/Rx2"]
        assert connection.getTimeoutCs().getValue() == 0.05
