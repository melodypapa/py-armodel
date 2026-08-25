"""Writer/reader round-trip tests for SoAdConfig (Table 6.117, p.452).

SoAdConfig aggregates connection (obsolete), connectionBundle (obsolete) and
socketAddress. SocketConnection itself is an obsolete XSD-only class
(Rel 4.4.0 documentation; attributes derived from the AUTOSAR_00052.xsd group).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SocketConnection,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SoAdConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _connection():
    connection = SocketConnection()
    connection.setAutosarConnector(ARLiteral().setValue("tcp"))
    do_ip_source_ref = RefType()
    do_ip_source_ref.setValue("/Ecu/DoIp/LogicAddress/Source")
    connection.setDoIpSourceAddressRef(do_ip_source_ref)
    ident = TpConnectionIdent(MockParent(), "Ident1")
    connection.setIdent(ident)
    n_pdu_ref = RefType()
    n_pdu_ref.setValue("/Ecu/Pdu/NmPdu1")
    connection.setNPduRef(n_pdu_ref)
    pdu = SocketConnectionIpduIdentifier()
    pdu_id = PositiveInteger().setValue(42)
    pdu.setHeaderId(pdu_id)
    connection.addPdu(pdu)
    timeout = TimeValue().setValue("0.01")
    connection.setPduCollectionTimeout(timeout)
    connection.setSocketProtocol(ARLiteral().setValue("udp"))
    return connection


def _write_and_parse(writer, parser, config):
    parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
    writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
    return parser.getSoAdConfig(root[0], "SO-AD-CONFIG")


class TestSoAdConfigRoundTrip:
    def test_round_trip_preserves_connections(self, writer, parser):
        config = SoAdConfig()
        config.addConnection(_connection())

        parsed = _write_and_parse(writer, parser, config)
        assert isinstance(parsed, SoAdConfig)

        connections = parsed.getConnections()
        assert len(connections) == 1
        connection = connections[0]
        assert isinstance(connection, SocketConnection)
        assert connection.getAutosarConnector().getValue() == "tcp"
        assert connection.getDoIpSourceAddressRef().getValue() == "/Ecu/DoIp/LogicAddress/Source"
        assert isinstance(connection.getIdent(), TpConnectionIdent)
        assert connection.getIdent().getShortName() == "Ident1"
        assert connection.getNPduRef().getValue() == "/Ecu/Pdu/NmPdu1"
        assert len(connection.getPdus()) == 1
        assert connection.getPdus()[0].getHeaderId().getValue() == 42
        assert connection.getPduCollectionTimeout().getValue() == 0.01
        assert connection.getSocketProtocol().getValue() == "udp"

    def test_write_all_fields(self, writer):
        parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
        config = SoAdConfig()
        config.addConnection(_connection())
        config.createSocketConnectionBundle("Bundle1")
        config.createSocketAddress("SA1")
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)

        node = parent.find("SO-AD-CONFIG")
        assert node.find("CONNECTIONS/SOCKET-CONNECTION") is not None
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/AUTOSAR-CONNECTOR").text == "tcp"
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/DO-IP-SOURCE-ADDRESS-REF").text == "/Ecu/DoIp/LogicAddress/Source"
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/IDENT/SHORT-NAME").text == "Ident1"
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/N-PDU-REF").text == "/Ecu/Pdu/NmPdu1"
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/PDUS/SOCKET-CONNECTION-IPDU-IDENTIFIER") is not None
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/SOCKET-PROTOCOL").text == "udp"
        assert node.find("CONNECTION-BUNDLES/SOCKET-CONNECTION-BUNDLE/SHORT-NAME").text == "Bundle1"
        assert node.find("SOCKET-ADDRESSS/SOCKET-ADDRESS/SHORT-NAME").text == "SA1"
