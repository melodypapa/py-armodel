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
    Identifier,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
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
        identifier.setPduRef(_ref("/Pdu/Pdu1"))
        identifier.setPduTriggeringRef(_ref("/IT/FrTrigger"))
        identifier.setRoutingGroupRefs([_ref("/Pkg/SoAdRoutingGroup1")])
        bundle.setPdus([identifier])
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

        pdus = re_bundle.getPdus()
        assert len(pdus) == 1
        re_identifier = pdus[0]
        assert isinstance(re_identifier, SocketConnectionIpduIdentifier)
        assert int(re_identifier.getHeaderId().getValue()) == 4660
        assert float(re_identifier.getPduCollectionPduTimeout().getValue()) == 10.0
        assert re_identifier.getPduCollectionSemantics().getValue() == "queued"
        assert re_identifier.getPduCollectionTrigger().getValue() == "always"
        assert re_identifier.getPduRef().getValue() == "/Pdu/Pdu1"
        assert re_identifier.getPduTriggeringRef().getValue() == "/IT/FrTrigger"
        refs = re_identifier.getRoutingGroupRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Pkg/SoAdRoutingGroup1"
