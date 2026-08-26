"""Writer/reader round-trip tests for OrderedMaster (Table 6.148, p.470)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    OrderedMaster,
    TimeSyncClientConfiguration,
    TimeSynchronization,
)

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    from armodel.writer.arxml_writer import ARXMLWriter

    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    from armodel.parser.arxml_parser import ARXMLParser

    return ARXMLParser()


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _new_sync():
    sync = TimeSynchronization()
    client = TimeSyncClientConfiguration()
    first = OrderedMaster()
    first.setIndex(_pos_int("0"))
    ref = RefType()
    ref.setDest("TIME-SYNC-SERVER-CONFIGURATION")
    ref.setValue("/Server/Master1")
    first.setTimeSyncServer(ref)
    client.addOrderedMaster(first)
    second = OrderedMaster()
    second.setIndex(_pos_int("1"))
    client.addOrderedMaster(second)
    sync.setTimeSyncClient(client)
    return sync


class TestOrderedMasterRoundTrip:
    def test_round_trip_preserves_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setTimeSynchronization(parent, _new_sync())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getTimeSynchronization(root[0], "TIME-SYNCHRONIZATION")

        assert isinstance(parsed, TimeSynchronization)
        client = parsed.getTimeSyncClient()
        assert isinstance(client, TimeSyncClientConfiguration)
        masters = client.getOrderedMasters()
        assert len(masters) == 2
        assert isinstance(masters[0], OrderedMaster)
        assert masters[0].getIndex().getValue() == 0
        assert masters[0].getTimeSyncServer().getValue() == "/Server/Master1"
        assert masters[0].getTimeSyncServer().getDest() == "TIME-SYNC-SERVER-CONFIGURATION"
        assert masters[1].getIndex().getValue() == 1
        assert masters[1].getTimeSyncServer() is None

    def test_empty_ordered_masters(self, writer, parser):
        sync = TimeSynchronization()
        sync.setTimeSyncClient(TimeSyncClientConfiguration())
        parent = ET.Element("PARENT")
        writer.setTimeSynchronization(parent, sync)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getTimeSynchronization(root[0], "TIME-SYNCHRONIZATION")
        assert parsed.getTimeSyncClient().getOrderedMasters() == []
