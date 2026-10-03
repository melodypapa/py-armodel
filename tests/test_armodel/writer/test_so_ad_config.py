"""Writer/reader round-trip tests for SoAdConfig (Table 6.117, p.452).

SoAdConfig aggregates connection (obsolete), connectionBundle (obsolete) and
socketAddress. SocketConnection is modeled per R4.3.1 Table 6.120, p.319
(runtimePortConfiguration: RuntimeAddressConfigurationEnum, shortLabel: Identifier).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    DateTime,
    Identifier,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection
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


def _connection():
    connection = SocketConnection()
    connection.setRuntimePortConfiguration(RuntimeAddressConfigurationEnum().setValue("sd"))
    connection.setShortLabel(Identifier().setValue("label"))
    return connection


def _literal(value):
    literal = ARLiteral()
    literal.setValue(value)
    return literal


def _positive(value):
    positive = PositiveInteger()
    positive.setValue(value)
    return positive


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _identifier(header_id):
    identifier = SocketConnectionIpduIdentifier()
    identifier.setHeaderId(_positive(header_id))
    return identifier


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
        assert connection.getRuntimePortConfiguration().getValue() == "sd"
        assert connection.getShortLabel().getValue() == "label"

    def test_write_all_fields(self, writer):
        parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
        config = SoAdConfig()
        config.addConnection(_connection())
        config.createSocketConnectionBundle("Bundle1")
        config.createSocketAddress("SA1")
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)

        node = parent.find("SO-AD-CONFIG")
        assert node.find("CONNECTIONS/SOCKET-CONNECTION") is not None
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/RUNTIME-PORT-CONFIGURATION").text == "sd"
        assert node.find("CONNECTIONS/SOCKET-CONNECTION/SHORT-LABEL").text == "label"
        assert node.find("CONNECTION-BUNDLES/SOCKET-CONNECTION-BUNDLE/SHORT-NAME").text == "Bundle1"
        assert node.find("SOCKET-ADDRESSS/SOCKET-ADDRESS/SHORT-NAME").text == "SA1"

    def test_round_trip_connection_members(self, writer, parser):
        config = SoAdConfig()
        connection = SocketConnection()
        connection.setAllowedIPv6ExtHeadersRef(_ref("/Pkgs/IPv6List"))
        connection.setAllowedTcpOptionsRef(_ref("/Pkgs/TcpList"))
        connection.setClientIpAddrFromConnectionRequest(_boolean(True))
        connection.setClientPortFromConnectionRequest(_boolean(False))
        connection.setClientPortRef(_ref("/Sock/SA1"))
        connection.addPdu(_identifier(4660))
        connection.setPduCollectionMaxBufferSize(_positive(1024))
        timeout = TimeValue()
        timeout.setValue(0.5)
        connection.setPduCollectionTimeout(timeout)
        connection.setRuntimeIpAddressConfiguration(RuntimeAddressConfigurationEnum().setValue("none"))
        connection.setRuntimePortConfiguration(RuntimeAddressConfigurationEnum().setValue("sd"))
        connection.setShortLabel(Identifier().setValue("Conn1"))
        config.addConnection(connection)

        parsed = _write_and_parse(writer, parser, config)

        connections = parsed.getConnections()
        assert len(connections) == 1
        re_connection = connections[0]
        assert isinstance(re_connection, SocketConnection)
        assert re_connection.getAllowedIPv6ExtHeadersRef().getValue() == "/Pkgs/IPv6List"
        assert re_connection.getAllowedTcpOptionsRef().getValue() == "/Pkgs/TcpList"
        assert re_connection.getClientIpAddrFromConnectionRequest().getValue() is True
        assert re_connection.getClientPortFromConnectionRequest().getValue() is False
        assert re_connection.getClientPortRef().getValue() == "/Sock/SA1"
        pdus = re_connection.getPdus()
        assert len(pdus) == 1
        assert int(pdus[0].getHeaderId().getValue()) == 4660
        assert int(re_connection.getPduCollectionMaxBufferSize().getValue()) == 1024
        assert float(re_connection.getPduCollectionTimeout().getValue()) == 0.5
        assert re_connection.getRuntimeIpAddressConfiguration().getValue() == "none"
        assert re_connection.getRuntimePortConfiguration().getValue() == "sd"
        assert re_connection.getShortLabel().getValue() == "Conn1"

    def test_round_trip_bundle_and_pdus(self, writer, parser):
        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("Bundle1")
        bundle.setDifferentiatedServiceField(_positive(48))
        bundle.setFlowLabel(_positive(100))
        bundle.setPathMtuDiscoveryEnabled(_boolean(True))
        bundle.setUdpChecksumHandling(_literal("randomize"))
        bundle.setServerPortRef(_ref("/Sock/SA1"))

        identifier = SocketConnectionIpduIdentifier()
        identifier.setHeaderId(_positive(4660))
        timeout = TimeValue()
        timeout.setValue(10.0)
        identifier.setPduCollectionPduTimeout(timeout)
        identifier.setPduCollectionSemantics(_literal("queued"))
        identifier.setPduCollectionTrigger(_literal("always"))
        identifier.setPduTriggeringRef(_ref("/IT/FrTrigger"))
        identifier.addRoutingGroupRef(_ref("/Pkg/SoAdRoutingGroup1"))
        identifier.addRoutingGroupRef(_ref("/Pkg/SoAdRoutingGroup2"))
        bundle.addPdu(identifier)
        bundle.addBundledConnection(_connection())

        parsed = _write_and_parse(writer, parser, config)

        bundles = parsed.getConnectionBundles()
        assert len(bundles) == 1
        re_bundle = bundles[0]
        assert int(re_bundle.getDifferentiatedServiceField().getValue()) == 48
        assert int(re_bundle.getFlowLabel().getValue()) == 100
        assert re_bundle.getPathMtuDiscoveryEnabled().getValue() is True
        assert re_bundle.getUdpChecksumHandling().getValue() == "randomize"
        assert re_bundle.getServerPortRef().getValue() == "/Sock/SA1"

        bundled = re_bundle.getBundledConnections()
        assert len(bundled) == 1
        re_connection = bundled[0]
        assert isinstance(re_connection, SocketConnection)
        assert re_connection.getRuntimePortConfiguration().getValue() == "sd"
        assert re_connection.getShortLabel().getValue() == "label"

        pdus = re_bundle.getPdus()
        assert len(pdus) == 1
        re_identifier = pdus[0]
        assert isinstance(re_identifier, SocketConnectionIpduIdentifier)
        assert int(re_identifier.getHeaderId().getValue()) == 4660
        assert float(re_identifier.getPduCollectionPduTimeout().getValue()) == 10.0
        assert re_identifier.getPduCollectionSemantics().getValue() == "queued"
        assert re_identifier.getPduCollectionTrigger().getValue() == "always"
        assert re_identifier.getPduTriggeringRef().getValue() == "/IT/FrTrigger"
        refs = re_identifier.getRoutingGroupRefs()
        assert [ref.getValue() for ref in refs] == ["/Pkg/SoAdRoutingGroup1", "/Pkg/SoAdRoutingGroup2"]

    def test_round_trip_bundle_preserves_arobject_checksum_and_timestamp(self, writer, parser):
        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("Bundle1")
        bundle.setChecksum(String().setValue("CHK123"))
        bundle.setTimestamp(DateTime().setValue("2026-10-03T00:00:00Z"))

        parsed = _write_and_parse(writer, parser, config)

        re_bundle = parsed.getConnectionBundles()[0]
        assert re_bundle.getChecksum().getValue() == "CHK123"
        assert re_bundle.getTimestamp().getValue() == "2026-10-03T00:00:00Z"

    def test_round_trip_bundle_empty_optional_and_no_children(self, writer, parser):
        config = SoAdConfig()
        config.createSocketConnectionBundle("Bundle1")

        parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)
        node = parent.find("SO-AD-CONFIG/CONNECTION-BUNDLES/SOCKET-CONNECTION-BUNDLE")
        assert node.find("BUNDLED-CONNECTIONS") is None
        assert node.find("PDUS") is None
        assert node.find("DIFFERENTIATED-SERVICE-FIELD") is None
        assert node.find("FLOW-LABEL") is None
        assert node.find("PATH-MTU-DISCOVERY-ENABLED") is None
        assert node.find("SERVER-PORT-REF") is None
        assert node.find("UDP-CHECKSUM-HANDLING") is None

        parsed = _write_and_parse(writer, parser, config)
        re_bundle = parsed.getConnectionBundles()[0]
        assert re_bundle.getBundledConnections() == []
        assert re_bundle.getPdus() == []
        assert re_bundle.getDifferentiatedServiceField() is None
        assert re_bundle.getFlowLabel() is None
        assert re_bundle.getPathMtuDiscoveryEnabled() is None
        assert re_bundle.getServerPortRef() is None
        assert re_bundle.getUdpChecksumHandling() is None

    def test_round_trip_pdu_without_routing_groups(self, writer, parser):
        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("Bundle1")
        identifier = SocketConnectionIpduIdentifier()
        identifier.setHeaderId(_positive(1))
        bundle.addPdu(identifier)

        parsed = _write_and_parse(writer, parser, config)

        re_identifier = parsed.getConnectionBundles()[0].getPdus()[0]
        assert re_identifier.getRoutingGroupRefs() == []
        parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)
        assert parent.find("SO-AD-CONFIG/CONNECTION-BUNDLES/SOCKET-CONNECTION-BUNDLE/PDUS/SOCKET-CONNECTION-IPDU-IDENTIFIER/ROUTING-GROUP-REFS") is None

    def test_round_trip_variation_point_is_last_element(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("Bundle1")
        point = VariationPoint()
        label = Identifier()
        label.setValue("vp1")
        point.setShortLabel(label)
        bundle.setVariationPoint(point)

        parsed = _write_and_parse(writer, parser, config)
        re_bundle = parsed.getConnectionBundles()[0]
        assert re_bundle.getVariationPoint() is not None
        assert re_bundle.getVariationPoint().getShortLabel().getValue() == "vp1"

        parent = ET.Element("ETHERNET-PHYSICAL-CHANNEL")
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", config)
        bundle_element = parent.find("SO-AD-CONFIG/CONNECTION-BUNDLES/SOCKET-CONNECTION-BUNDLE")
        assert bundle_element[-1].tag == "VARIATION-POINT"
