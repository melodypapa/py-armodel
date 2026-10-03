"""Parser tests for TimeSyncServerConfiguration (Table 6.147, p.470).

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


class TestReadTimeSyncServerConfiguration:
    def test_read_all_attribute_values(self):
        root = _root(
            "<PRIORITY>7</PRIORITY>" "<SYNC-INTERVAL>1.0</SYNC-INTERVAL>" "<TIME-SYNC-SERVER-IDENTIFIER>srv-1</TIME-SYNC-SERVER-IDENTIFIER>" "<TIME-SYNC-TECHNOLOGY>NTP-RFC-958</TIME-SYNC-TECHNOLOGY>"
        )
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        server = sync.getTimeSyncServer()
        assert server is not None
        assert server.getPriority().getValue() == 7
        assert server.getSyncInterval().getValue() == 1.0
        assert server.getTimeSyncServerIdentifier().getValue() == "srv-1"
        assert server.getTimeSyncTechnology().getValue() == "NTP-RFC-958"

    def test_read_empty_server_yields_none_attributes(self):
        root = _root("")
        sync = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert sync is not None
        server = sync.getTimeSyncServer()
        assert server is not None
        assert server.getPriority() is None
        assert server.getSyncInterval() is None
        assert server.getTimeSyncServerIdentifier() is None
        assert server.getTimeSyncTechnology() is None
