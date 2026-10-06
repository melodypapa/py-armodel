"""Writer round-trip tests for LinPhysicalChannel (Table 3.46, p.100).

The XSD group LIN-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd line 77544) contributes
BUS-IDLE-TIMEOUT-PERIOD and the SCHEDULE-TABLES wrapper (choice of
LIN-SCHEDULE-TABLE) in that sequenceOffset order; writeLinPhysicalChannel
emits the LIN-PHYSICAL-CHANNEL element, calls the base writePhysicalChannel
helper exactly once, and emits the LIN level after the inherited
PHYSICAL-CHANNEL content. The class is emitted as a concrete element of the
CommunicationClusterContent PHYSICAL-CHANNELS choice (line 20219, Rule
0001.7): dispatch coverage runs through writeCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCluster, LinPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LIN_XSD_TAIL_ORDER = ["BUS-IDLE-TIMEOUT-PERIOD", "SCHEDULE-TABLES"]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _time_value(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_channel():
    channel = LinPhysicalChannel(MockParent(), "lin_ch")
    channel.addCommConnectorRef(_ref("/ecu/lin_conn", "LIN-COMMUNICATION-CONNECTOR"))
    channel.setBusIdleTimeoutPeriod(_time_value("0.5"))
    channel.createLinScheduleTable("table1")
    channel.createLinScheduleTable("table2")
    return channel


def _bare_channel():
    return LinPhysicalChannel(MockParent(), "lin_ch")


def _write_channel(channel):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeLinPhysicalChannel(parent, channel)
    return parent


def _namespaced_channel_tag(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteLinPhysicalChannel:
    def test_write_lin_level_in_xsd_order_after_inherited_content(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("LIN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        tags = [child.tag for child in channel_tag]
        assert tags == ["SHORT-NAME", "COMM-CONNECTORS"] + LIN_XSD_TAIL_ORDER

    def test_write_field_values(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("LIN-PHYSICAL-CHANNEL")

        bus_idle_timeout = channel_tag.find("BUS-IDLE-TIMEOUT-PERIOD")
        assert bus_idle_timeout is not None
        assert bus_idle_timeout.text == "0.5"

        comm_connectors = channel_tag.find("COMM-CONNECTORS")
        assert comm_connectors is not None
        comm_ref = comm_connectors.find("COMMUNICATION-CONNECTOR-REF-CONDITIONAL/COMMUNICATION-CONNECTOR-REF")
        assert comm_ref.get("DEST") == "LIN-COMMUNICATION-CONNECTOR"
        assert comm_ref.text == "/ecu/lin_conn"

        schedule_tables = channel_tag.find("SCHEDULE-TABLES")
        assert schedule_tables is not None
        tables = schedule_tables.findall("LIN-SCHEDULE-TABLE")
        assert [t.find("SHORT-NAME").text for t in tables] == ["table1", "table2"]

    def test_write_omits_empty_wrappers_and_optional_elements(self, writer):
        parent = _write_channel(_bare_channel())
        channel_tag = parent.find("LIN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        assert [child.tag for child in channel_tag] == ["SHORT-NAME"]
        assert channel_tag.find("BUS-IDLE-TIMEOUT-PERIOD") is None
        assert channel_tag.find("SCHEDULE-TABLES") is None
        assert channel_tag.find("COMM-CONNECTORS") is None

    def test_round_trip_full(self, writer, parser):
        parent = _write_channel(_full_channel())
        reloaded = _bare_channel()
        parser.readLinPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert isinstance(reloaded, LinPhysicalChannel)
        assert reloaded.getShortName() == "lin_ch"

        bus_idle_timeout = reloaded.getBusIdleTimeoutPeriod()
        assert bus_idle_timeout is not None
        assert bus_idle_timeout.getValue() == 0.5

        refs = reloaded.getCommConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/ecu/lin_conn"
        assert refs[0].getDest() == "LIN-COMMUNICATION-CONNECTOR"

        tables = reloaded.getScheduleTables()
        assert [t.getShortName() for t in tables] == ["table1", "table2"]
        assert all(isinstance(t, LinScheduleTable) for t in tables)

    def test_round_trip_empty(self, writer, parser):
        parent = _write_channel(_bare_channel())
        reloaded = _bare_channel()
        parser.readLinPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert reloaded.getShortName() == "lin_ch"
        assert reloaded.getBusIdleTimeoutPeriod() is None
        assert reloaded.getScheduleTables() == []
        assert reloaded.getCommConnectorRefs() == []


class TestWriteCommunicationClusterLinDispatch:
    """Table 3.46: the PHYSICAL-CHANNELS writer dispatch emits LIN-PHYSICAL-CHANNEL for a LinPhysicalChannel instance (Rule 0001.7)."""

    def test_dispatch_emits_lin_physical_channel_element(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cluster = LinCluster(pkg, "Cluster")
        cluster.createLinPhysicalChannel("lin_ch")

        parent = ET.Element("PARENT")
        writer.writeCommunicationClusterPhysicalChannels(parent, cluster)
        channels = parent.find("PHYSICAL-CHANNELS")
        assert channels is not None
        assert len(channels.findall("LIN-PHYSICAL-CHANNEL")) == 1
        assert channels.find("LIN-PHYSICAL-CHANNEL/SHORT-NAME").text == "lin_ch"
