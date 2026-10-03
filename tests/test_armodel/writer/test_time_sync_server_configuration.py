"""Writer round-trip tests for TimeSyncServerConfiguration (Table 6.147, p.470).

XML element order per XSD group TIME-SYNC-SERVER-CONFIGURATION:
PRIORITY, SYNC-INTERVAL, TIME-SYNC-SERVER-IDENTIFIER, TIME-SYNC-TECHNOLOGY.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSynchronization,
    TimeSyncServerConfiguration,
    TimeSyncTechnologyEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

SERVER_ELEMENTS = ["PRIORITY", "SYNC-INTERVAL", "TIME-SYNC-SERVER-IDENTIFIER", "TIME-SYNC-TECHNOLOGY"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time_value(value):
    interval = TimeValue()
    interval.setValue(value)
    return interval


def _string(value):
    text = String()
    text.setValue(value)
    return text


def _enum(value):
    technology = TimeSyncTechnologyEnum()
    technology.setValue(value)
    return technology


def _sync_with_server():
    server = TimeSyncServerConfiguration(None, "Server")
    server.setPriority(_pos_int("7"))
    server.setSyncInterval(_time_value("1.0"))
    server.setTimeSyncServerIdentifier(_string("srv-1"))
    server.setTimeSyncTechnology(_enum(TimeSyncTechnologyEnum.NTP_RFC958))
    sync = TimeSynchronization()
    sync.setTimeSyncServer(server)
    return sync


class TestWriteTimeSyncServerConfiguration:
    def test_write_server_element_order_and_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", _sync_with_server())
        server = parent.find("TIME-SYNCHRONIZATION/TIME-SYNC-SERVER")
        assert server is not None
        children = [child.tag for child in server]
        positions = [children.index(tag) for tag in SERVER_ELEMENTS]
        assert positions == sorted(positions)
        assert server.find("PRIORITY").text == "7"
        assert server.find("SYNC-INTERVAL").text == "1.0"
        assert server.find("TIME-SYNC-SERVER-IDENTIFIER").text == "srv-1"
        assert server.find("TIME-SYNC-TECHNOLOGY").text == "NTP-RFC-958"

    def test_write_empty_server_omits_attributes(self):
        server = TimeSyncServerConfiguration(None, "Server")
        sync = TimeSynchronization()
        sync.setTimeSyncServer(server)
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", sync)
        server_element = parent.find("TIME-SYNCHRONIZATION/TIME-SYNC-SERVER")
        assert server_element is not None
        for tag in SERVER_ELEMENTS:
            assert server_element.find(tag) is None

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", _sync_with_server())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        reloaded = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert reloaded is not None
        server = reloaded.getTimeSyncServer()
        assert server is not None
        assert server.getPriority().getValue() == 7
        assert server.getSyncInterval().getValue() == 1.0
        assert server.getTimeSyncServerIdentifier().getValue() == "srv-1"
        assert server.getTimeSyncTechnology().getValue() == "NTP-RFC-958"
