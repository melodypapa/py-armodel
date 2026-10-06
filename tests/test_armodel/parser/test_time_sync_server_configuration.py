"""Parser tests for TimeSynchronization (Table 6.145, p.469) and its TimeSyncServerConfiguration child (Table 6.147, p.470).

XSD group TIME-SYNCHRONIZATION order: TIME-SYNC-CLIENT, TIME-SYNC-SERVER.
XSD group TIME-SYNC-SERVER-CONFIGURATION order:
PRIORITY, SYNC-INTERVAL, TIME-SYNC-SERVER-IDENTIFIER, TIME-SYNC-TECHNOLOGY.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _root(server_inner: str):
    xml = "<PARENT xmlns='%s'>" "<TIME-SYNCHRONIZATION>" "<TIME-SYNC-SERVER>" "<SHORT-NAME>Server</SHORT-NAME>" "%s" "</TIME-SYNC-SERVER>" "</TIME-SYNCHRONIZATION>" "</PARENT>" % (NS, server_inner)
    return ET.fromstring(xml)


def _client_root(client_inner: str):
    xml = "<PARENT xmlns='%s'>" "<TIME-SYNCHRONIZATION>" "<TIME-SYNC-CLIENT>" "%s" "</TIME-SYNC-CLIENT>" "</TIME-SYNCHRONIZATION>" "</PARENT>" % (NS, client_inner)
    return ET.fromstring(xml)


class TestReadTimeSyncServerConfiguration:
    def test_read_all_attribute_values(self):
        root = _root(
            "<PRIORITY>7</PRIORITY>" "<SYNC-INTERVAL>1.0</SYNC-INTERVAL>" "<TIME-SYNC-SERVER-IDENTIFIER>srv-1</TIME-SYNC-SERVER-IDENTIFIER>" "<TIME-SYNC-TECHNOLOGY>NTP--RFC-958</TIME-SYNC-TECHNOLOGY>"
        )
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        server = sync.getTimeSyncServer()
        assert server is not None
        assert server.getShortName() == "Server"
        assert server.getPriority().getValue() == 7
        assert server.getSyncInterval().getValue() == 1.0
        assert server.getTimeSyncServerIdentifier().getValue() == "srv-1"
        assert server.getTimeSyncTechnology().getValue() == "NTP--RFC-958"

    def test_read_empty_server_yields_none_attributes(self):
        root = _root("")
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        server = sync.getTimeSyncServer()
        assert server is not None
        assert server.getShortName() == "Server"
        assert server.getPriority() is None
        assert server.getSyncInterval() is None
        assert server.getTimeSyncServerIdentifier() is None
        assert server.getTimeSyncTechnology() is None


class TestReadTimeSynchronization:
    def test_read_time_sync_client_values(self):
        root = _client_root(
            "<ORDERED-MASTER-LIST><ORDERED-MASTER><INDEX>1</INDEX><TIME-SYNC-SERVER-REF>/Pkg/Srv</TIME-SYNC-SERVER-REF></ORDERED-MASTER></ORDERED-MASTER-LIST><TIME-SYNC-TECHNOLOGY>NTP--RFC-958</TIME-SYNC-TECHNOLOGY>"
        )
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        client = sync.getTimeSyncClient()
        assert client is not None
        assert client.getTimeSyncTechnology().getValue() == "NTP--RFC-958"
        masters = client.getOrderedMasters()
        assert len(masters) == 1
        assert masters[0].getIndex().getValue() == 1
        assert masters[0].getTimeSyncServerRef().getValue() == "/Pkg/Srv"

    def test_read_empty_client_yields_none_attributes(self):
        root = _client_root("")
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        client = sync.getTimeSyncClient()
        assert client is not None
        assert client.getTimeSyncTechnology() is None
        assert client.getOrderedMasters() == []

    def test_read_empty_time_synchronization_yields_no_children(self):
        root = ET.fromstring("<PARENT xmlns='%s'><TIME-SYNCHRONIZATION></TIME-SYNCHRONIZATION></PARENT>" % NS)
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        assert sync.getTimeSyncClient() is None
        assert sync.getTimeSyncServer() is None
