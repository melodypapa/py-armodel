"""Writer round-trip tests for TimeSyncClientConfiguration (Table 6.146, p.470).

XML element order per XSD group TIME-SYNC-CLIENT-CONFIGURATION:
ORDERED-MASTER-LIST, TIME-SYNC-TECHNOLOGY.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    OrderedMaster,
    TimeSyncClientConfiguration,
    TimeSynchronization,
    TimeSyncTechnologyEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _new_sync():
    sync = TimeSynchronization()
    client = TimeSyncClientConfiguration()
    technology = TimeSyncTechnologyEnum()
    technology.setValue("IEEE_802.1AS")
    client.setTimeSyncTechnology(technology)

    master1 = OrderedMaster()
    master1.setIndex(_pos_int(1))
    ref1 = RefType()
    ref1.setDest("TIME-SYNC-SERVER-CONFIGURATION")
    ref1.setValue("/Sync/Server1")
    master1.setTimeSyncServerRef(ref1)
    client.addOrderedMaster(master1)

    master2 = OrderedMaster()
    master2.setIndex(_pos_int(2))
    client.addOrderedMaster(master2)

    sync.setTimeSyncClient(client)
    return sync


class TestWriteTimeSyncClientConfiguration:
    def test_write_client_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", _new_sync())
        client = parent.find("TIME-SYNCHRONIZATION/TIME-SYNC-CLIENT")
        assert client is not None
        children = [child.tag for child in client]
        assert children.index("ORDERED-MASTER-LIST") < children.index("TIME-SYNC-TECHNOLOGY")

        masters = client.findall("ORDERED-MASTER-LIST/ORDERED-MASTER")
        assert len(masters) == 2
        assert masters[0].find("INDEX").text == "1"
        server_ref = masters[0].find("TIME-SYNC-SERVER-REF")
        assert server_ref.text == "/Sync/Server1"
        assert server_ref.attrib["DEST"] == "TIME-SYNC-SERVER-CONFIGURATION"
        assert masters[1].find("INDEX").text == "2"
        assert client.find("TIME-SYNC-TECHNOLOGY").text == "IEEE_802.1AS"

    def test_write_empty_client(self):
        sync = TimeSynchronization()
        sync.setTimeSyncClient(TimeSyncClientConfiguration())
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", sync)
        client = parent.find("TIME-SYNCHRONIZATION/TIME-SYNC-CLIENT")
        assert client is not None
        assert client.find("ORDERED-MASTER-LIST") is None
        assert client.find("TIME-SYNC-TECHNOLOGY") is None

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTimeSynchronization(parent, "TIME-SYNCHRONIZATION", _new_sync())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTimeSynchronization(root, "TIME-SYNCHRONIZATION")
        assert reloaded is not None
        client = reloaded.getTimeSyncClient()
        assert client is not None
        assert client.getTimeSyncTechnology().getValue() == "IEEE_802.1AS"
        masters = client.getOrderedMasters()
        assert len(masters) == 2
        assert masters[0].getIndex().getValue() == 1
        assert masters[0].getTimeSyncServerRef().getValue() == "/Sync/Server1"
        assert masters[0].getTimeSyncServerRef().getDest() == "TIME-SYNC-SERVER-CONFIGURATION"
        assert masters[1].getIndex().getValue() == 2
