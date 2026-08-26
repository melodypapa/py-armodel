"""Writer/reader round-trip tests for SocketAddress (Table 6.118, p.453)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SocketAddress, StaticSocketConnection, UdpChecksumCalculationEnum
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _full_address():
    address = SocketAddress(MockParent(), "SA1")
    address.setAllowedIPv6ExtHeadersRef(_ref("IPV6-EXT-HEADER-FILTER-LIST", "/Ether/TcpOptionFilterSets/IPv6List"))
    address.setAllowedTcpOptionsRef(_ref("TCP-OPTION-FILTER-LIST", "/Ether/TcpOptionFilterSets/TcpList"))

    end_point = address.createApplicationEndpoint("AEP1")
    end_point.setMaxNumberOfConnections(_pos_int("10"))

    address.setConnectorRef(_ref("ETHERNET-COMMUNICATION-CONNECTOR", "/Ether/Ecu1/Connector1"))
    address.setDifferentiatedServiceField(_pos_int("46"))
    address.setFlowLabel(_pos_int("12345"))
    address.addMulticastConnectorRef(_ref("ETHERNET-COMMUNICATION-CONNECTOR", "/Ether/Ecu2/Connector2"))
    address.addMulticastConnectorRef(_ref("ETHERNET-COMMUNICATION-CONNECTOR", "/Ether/Ecu3/Connector3"))
    address.setPathMtuDiscoveryEnabled(Boolean().setValue("true"))
    address.setPduCollectionMaxBufferSize(_pos_int("1024"))
    timeout = TimeValue()
    timeout.setValue("0.005")
    address.setPduCollectionTimeout(timeout)

    checksum = UdpChecksumCalculationEnum()
    checksum.setValue(UdpChecksumCalculationEnum.UDP_CHECKSUM_ENABLED)
    address.setUdpChecksumHandling(checksum)
    return address


class TestWriteSocketAddress:
    def test_write_all_fields(self, writer):
        parent = ET.Element("SO-AD-CONFIG")
        writer.writeSocketAddress(parent, _full_address())

        el = parent.find("SOCKET-ADDRESS")
        assert el is not None
        assert el.find("SHORT-NAME").text == "SA1"
        allowed_ipv6 = el.find("ALLOWED-I-PV-6-EXT-HEADERS-REF")
        assert allowed_ipv6 is not None
        assert allowed_ipv6.text == "/Ether/TcpOptionFilterSets/IPv6List"
        assert allowed_ipv6.get("DEST") == "IPV6-EXT-HEADER-FILTER-LIST"
        allowed_tcp = el.find("ALLOWED-TCP-OPTIONS-REF")
        assert allowed_tcp is not None
        assert allowed_tcp.text == "/Ether/TcpOptionFilterSets/TcpList"
        assert allowed_tcp.get("DEST") == "TCP-OPTION-FILTER-LIST"
        application_endpoint = el.find("APPLICATION-ENDPOINT")
        assert application_endpoint is not None
        assert application_endpoint.find("SHORT-NAME").text == "AEP1"
        assert el.find("CONNECTOR-REF").text == "/Ether/Ecu1/Connector1"
        assert el.find("DIFFERENTIATED-SERVICE-FIELD").text == "46"
        assert el.find("FLOW-LABEL").text == "12345"
        multicast_refs = el.findall("MULTICAST-CONNECTOR-REFS/MULTICAST-CONNECTOR-REF")
        assert len(multicast_refs) == 2
        assert multicast_refs[0].text == "/Ether/Ecu2/Connector2"
        assert multicast_refs[1].text == "/Ether/Ecu3/Connector3"
        assert el.find("PATH-MTU-DISCOVERY-ENABLED").text == "true"
        assert el.find("PDU-COLLECTION-MAX-BUFFER-SIZE").text == "1024"
        assert float(el.find("PDU-COLLECTION-TIMEOUT").text) == 0.005
        assert el.find("UDP-CHECKSUM-HANDLING").text == "udpChecksumEnabled"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        address = SocketAddress(MockParent(), "EmptyAddress")
        parent = ET.Element("SO-AD-CONFIG")
        writer.writeSocketAddress(parent, address)

        el = parent.find("SOCKET-ADDRESS")
        assert el is not None
        assert el.find("ALLOWED-I-PV-6-EXT-HEADERS-REF") is None
        assert el.find("ALLOWED-TCP-OPTIONS-REF") is None
        assert el.find("APPLICATION-ENDPOINT") is None
        assert el.find("CONNECTOR-REF") is None
        assert el.find("DIFFERENTIATED-SERVICE-FIELD") is None
        assert el.find("FLOW-LABEL") is None
        assert el.find("MULTICAST-CONNECTOR-REFS") is None
        assert el.find("PATH-MTU-DISCOVERY-ENABLED") is None
        assert el.find("PDU-COLLECTION-MAX-BUFFER-SIZE") is None
        assert el.find("PDU-COLLECTION-TIMEOUT") is None
        assert el.find("PORT-ADDRESS") is None
        assert el.find("STATIC-SOCKET-CONNECTIONS") is None
        assert el.find("UDP-CHECKSUM-HANDLING") is None


class TestSocketAddressRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        address = _full_address()

        parent = ET.Element("SO-AD-CONFIG")
        writer.writeSocketAddress(parent, address)

        out_file = str(tmp_path / "socket_address.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered_address = SocketAddress(MockParent(), "SA1")
        tree = ET.parse(out_file)
        parser.readSocketAddress(tree.getroot()[0][0], recovered_address)

        assert recovered_address.getShortName() == "SA1"
        assert recovered_address.getAllowedIPv6ExtHeadersRef().getValue() == "/Ether/TcpOptionFilterSets/IPv6List"
        assert recovered_address.getAllowedTcpOptionsRef().getValue() == "/Ether/TcpOptionFilterSets/TcpList"
        end_point = recovered_address.getApplicationEndpoint()
        assert end_point is not None
        assert end_point.getShortName() == "AEP1"
        assert end_point.getMaxNumberOfConnections().getValue() == 10
        assert recovered_address.getConnectorRef().getValue() == "/Ether/Ecu1/Connector1"
        assert recovered_address.getDifferentiatedServiceField().getValue() == 46
        assert recovered_address.getFlowLabel().getValue() == 12345
        refs = recovered_address.getMulticastConnectorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Ether/Ecu2/Connector2"
        assert refs[1].getValue() == "/Ether/Ecu3/Connector3"
        assert recovered_address.getPathMtuDiscoveryEnabled().getValue() is True
        assert recovered_address.getPduCollectionMaxBufferSize().getValue() == 1024
        assert recovered_address.getPduCollectionTimeout().getValue() == 0.005
        assert isinstance(recovered_address.getUdpChecksumHandling(), UdpChecksumCalculationEnum)
        assert recovered_address.getUdpChecksumHandling().getValue() == "udpChecksumEnabled"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<SOCKET-ADDRESS xmlns='{NS}'><SHORT-NAME>SA1</SHORT-NAME></SOCKET-ADDRESS>")

        recovered_address = SocketAddress(MockParent(), "SA1")
        parser.readSocketAddress(element, recovered_address)

        assert recovered_address.getShortName() == "SA1"
        assert recovered_address.getAllowedIPv6ExtHeadersRef() is None
        assert recovered_address.getAllowedTcpOptionsRef() is None
        assert recovered_address.getApplicationEndpoint() is None
        assert recovered_address.getConnectorRef() is None
        assert recovered_address.getDifferentiatedServiceField() is None
        assert recovered_address.getFlowLabel() is None
        assert recovered_address.getMulticastConnectorRefs() == []
        assert recovered_address.getPathMtuDiscoveryEnabled() is None
        assert recovered_address.getPduCollectionMaxBufferSize() is None
        assert recovered_address.getPduCollectionTimeout() is None
        assert recovered_address.getStaticSocketConnections() == []
        assert recovered_address.getUdpChecksumHandling() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _static_connection(short_name):
    connection = StaticSocketConnection(MockParent(), short_name)
    role = ARLiteral()
    role.setValue("listen")
    connection.setTcpRole(role)
    return connection


class TestSocketAddressStaticSocketConnections:
    def test_write_static_socket_connections(self, writer):
        parent = ET.Element("SO-AD-CONFIG")
        address = SocketAddress(MockParent(), "SA1")
        address.addStaticSocketConnection(_static_connection("SSC1"))
        address.addStaticSocketConnection(_static_connection("SSC2"))
        writer.writeSocketAddress(parent, address)

        el = parent.find("SOCKET-ADDRESS")
        wrapper = el.find("STATIC-SOCKET-CONNECTIONS")
        assert wrapper is not None
        entries = wrapper.findall("STATIC-SOCKET-CONNECTION")
        assert len(entries) == 2
        assert entries[0].find("SHORT-NAME").text == "SSC1"
        assert entries[0].find("TCP-ROLE").text == "listen"
        assert entries[1].find("SHORT-NAME").text == "SSC2"

    def test_round_trip_preserves_static_socket_connections(self, writer, parser, tmp_path):
        address = SocketAddress(MockParent(), "SA1")
        address.addStaticSocketConnection(_static_connection("SSC1"))
        address.addStaticSocketConnection(_static_connection("SSC2"))

        parent = ET.Element("SO-AD-CONFIG")
        writer.writeSocketAddress(parent, address)

        out_file = str(tmp_path / "socket_address_ssc.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered = SocketAddress(MockParent(), "SA1")
        tree = ET.parse(out_file)
        parser.readSocketAddress(tree.getroot()[0][0], recovered)

        connections = recovered.getStaticSocketConnections()
        assert len(connections) == 2
        assert isinstance(connections[0], StaticSocketConnection)
        assert connections[0].getShortName() == "SSC1"
        assert connections[0].getTcpRole().getValue() == "listen"
        assert connections[1].getShortName() == "SSC2"

    def test_reader_no_wrapper_leaves_list_empty(self, parser):
        element = ET.fromstring(f"<SOCKET-ADDRESS xmlns='{NS}'><SHORT-NAME>SA1</SHORT-NAME></SOCKET-ADDRESS>")
        recovered = SocketAddress(MockParent(), "SA1")
        parser.readSocketAddress(element, recovered)
        assert recovered.getStaticSocketConnections() == []
