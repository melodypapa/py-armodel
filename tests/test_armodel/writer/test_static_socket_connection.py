"""Writer/reader round-trip tests for StaticSocketConnection (Table 6.201, p.544).

StaticSocketConnection is an Identifiable value type aggregated by
SocketAddress.staticSocketConnection. The iPduIdentifier/remoteAddress refs are
serialized through the XSD-only atpVariation conditional wrappers.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import StaticSocketConnection
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


def _new_connection(short_name="Conn1"):
    connection = StaticSocketConnection(MockParent(), short_name)
    ref_1 = RefType()
    ref_1.setValue("/Ecu/SoCon/IPdu1")
    ref_2 = RefType()
    ref_2.setValue("/Ecu/SoCon/IPdu2")
    remote_ref = RefType()
    remote_ref.setValue("/Ecu/SoAd/SocketAddress/Remote")
    timeout = TimeValue().setValue(30)
    role = ARLiteral().setValue("connect")
    connection.addIPduIdentifierRef(ref_1)
    connection.addIPduIdentifierRef(ref_2)
    connection.setRemoteAddressRef(remote_ref)
    connection.setTcpConnectTimeout(timeout)
    connection.setTcpRole(role)
    return connection


class TestWriteStaticSocketConnection:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setStaticSocketConnection(parent, _new_connection())
        node = parent.find("STATIC-SOCKET-CONNECTION")
        assert node is not None
        ipdu_refs = node.findall("I-PDU-IDENTIFIERS/SO-CON-I-PDU-IDENTIFIER-REF-CONDITIONAL/SO-CON-I-PDU-IDENTIFIER-REF")
        assert len(ipdu_refs) == 2
        assert ipdu_refs[0].text == "/Ecu/SoCon/IPdu1"
        assert ipdu_refs[1].text == "/Ecu/SoCon/IPdu2"
        remote_ref = node.find("REMOTE-ADDRESSS/SOCKET-ADDRESS-REF-CONDITIONAL/SOCKET-ADDRESS-REF")
        assert remote_ref is not None
        assert remote_ref.text == "/Ecu/SoAd/SocketAddress/Remote"
        assert node.find("TCP-CONNECT-TIMEOUT").text == "30.0"
        assert node.find("TCP-ROLE").text == "connect"

    def test_write_empty_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setStaticSocketConnection(parent, StaticSocketConnection(MockParent(), "Empty"))
        node = parent.find("STATIC-SOCKET-CONNECTION")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("I-PDU-IDENTIFIERS") is None
        assert node.find("REMOTE-ADDRESSS") is None
        assert node.find("TCP-CONNECT-TIMEOUT") is None
        assert node.find("TCP-ROLE") is None


class TestStaticSocketConnectionRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setStaticSocketConnection(parent, _new_connection())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getStaticSocketConnection(root[0][0])
        assert isinstance(parsed, StaticSocketConnection)
        assert parsed.getShortName() == "Conn1"
        ipdu_refs = parsed.getIPduIdentifierRefs()
        assert len(ipdu_refs) == 2
        assert ipdu_refs[0].getValue() == "/Ecu/SoCon/IPdu1"
        assert ipdu_refs[1].getValue() == "/Ecu/SoCon/IPdu2"
        assert parsed.getRemoteAddressRef().getValue() == "/Ecu/SoAd/SocketAddress/Remote"
        assert parsed.getTcpConnectTimeout().getValue() == 30
        assert parsed.getTcpRole().getValue() == "connect"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<STATIC-SOCKET-CONNECTION xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></STATIC-SOCKET-CONNECTION>" % NS)
        parsed = parser.getStaticSocketConnection(element)
        assert isinstance(parsed, StaticSocketConnection)
        assert parsed.getShortName() == "Empty"
        assert parsed.getIPduIdentifierRefs() == []
        assert parsed.getRemoteAddressRef() is None
        assert parsed.getTcpConnectTimeout() is None
        assert parsed.getTcpRole() is None
