"""Writer/reader round-trip tests for SoAdConfig (Table 6.117, p.452).

SoAdConfig aggregates connection (obsolete), connectionBundle (obsolete) and
socketAddress. SocketConnection is modeled per R4.3.1 Table 6.120, p.319
(runtimePortConfiguration: RuntimeAddressConfigurationEnum, shortLabel: Identifier).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    RuntimeAddressConfigurationEnum,
    SocketConnection,
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
