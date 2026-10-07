"""Writer round-trip tests for UserDefinedPhysicalChannel (Table 3.130, p.179).

XML element order per XSD USER-DEFINED-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd line
128989): heritage groups (SHORT-NAME via writeIdentifiable) first, then the
inherited PHYSICAL-CHANNEL group content in sequenceOffset order (COMM-CONNECTORS,
FRAME-TRIGGERINGS, I-SIGNAL-TRIGGERINGS, MANAGED-PHYSICAL-CHANNEL-REFS,
PDU-TRIGGERINGS); the USER-DEFINED-PHYSICAL-CHANNEL own group (lines 128980-128988)
is an empty sequence — no atpVariation wrapper.
writeUserDefinedPhysicalChannel calls writeIdentifiable on the outer element and the
reusable writePhysicalChannel helper exactly once.

Verifies that a UserDefinedPhysicalChannel created on a UserDefinedCluster survives
a full set -> save -> reload cycle with its inherited PhysicalChannel attributes
intact, including the bare-channel case.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster, UserDefinedPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

PHYSICAL_CHANNEL_XSD_ORDER = [
    "SHORT-NAME",
    "COMM-CONNECTORS",
    "MANAGED-PHYSICAL-CHANNEL-REFS",
]


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
    return ARXMLParser(options={"warning": True})


def _reload(parser, path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(path, document)
    return document


def _full_channel():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("Cluster")
    channel = cluster.createUserDefinedPhysicalChannel("UserDefinedPhysicalChannel")
    comm_connector_ref = RefType()
    comm_connector_ref.setDest("COMMUNICATION-CONNECTOR")
    comm_connector_ref.setValue("/EcuInst/Conn")
    channel.addCommConnectorRef(comm_connector_ref)
    managed_ref = RefType()
    managed_ref.setDest("USER-DEFINED-PHYSICAL-CHANNEL")
    managed_ref.setValue("/Cluster/ManagedCh")
    channel.addManagedPhysicalChannelRef(managed_ref)
    return channel


def _new_channel(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("Cluster")
    return UserDefinedPhysicalChannel(cluster, name)


def _write_user_defined_physical_channel(channel):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeUserDefinedPhysicalChannel(parent, channel)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteUserDefinedPhysicalChannel:
    def test_entry_point_emits_short_name(self):
        parent = _write_user_defined_physical_channel(_full_channel())
        user_defined_channel = parent.find("USER-DEFINED-PHYSICAL-CHANNEL")

        assert user_defined_channel.find("SHORT-NAME").text == "UserDefinedPhysicalChannel"

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_user_defined_physical_channel(_full_channel())
        user_defined_channel = parent.find("USER-DEFINED-PHYSICAL-CHANNEL")

        assert [child.tag for child in user_defined_channel] == PHYSICAL_CHANNEL_XSD_ORDER

        all_tags = [child.tag for child in user_defined_channel.iter()]
        for tag in PHYSICAL_CHANNEL_XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_user_defined_physical_channel(_full_channel())
        user_defined_channel = parent.find("USER-DEFINED-PHYSICAL-CHANNEL")

        connector_ref = user_defined_channel.find("COMM-CONNECTORS/COMMUNICATION-CONNECTOR-REF-CONDITIONAL/COMMUNICATION-CONNECTOR-REF")
        assert connector_ref.get("DEST") == "COMMUNICATION-CONNECTOR"
        assert connector_ref.text == "/EcuInst/Conn"

        managed_ref = user_defined_channel.find("MANAGED-PHYSICAL-CHANNEL-REFS/MANAGED-PHYSICAL-CHANNEL-REF")
        assert managed_ref.get("DEST") == "USER-DEFINED-PHYSICAL-CHANNEL"
        assert managed_ref.text == "/Cluster/ManagedCh"

    def test_bare_channel_emits_short_name_only(self):
        parent = _write_user_defined_physical_channel(_new_channel("Channel"))
        user_defined_channel = parent.find("USER-DEFINED-PHYSICAL-CHANNEL")

        assert user_defined_channel.find("SHORT-NAME").text == "Channel"
        assert [child.tag for child in user_defined_channel] == ["SHORT-NAME"]

    def test_round_trip_full_through_user_defined_physical_channel(self):
        parent = _write_user_defined_physical_channel(_full_channel())
        reloaded = _new_channel("UserDefinedPhysicalChannel")
        ARXMLParser().readUserDefinedPhysicalChannel(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "UserDefinedPhysicalChannel"
        comm_connector_refs = reloaded.getCommConnectorRefs()
        assert len(comm_connector_refs) == 1
        assert comm_connector_refs[0].getValue() == "/EcuInst/Conn"
        assert comm_connector_refs[0].getDest() == "COMMUNICATION-CONNECTOR"
        managed_refs = reloaded.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/Cluster/ManagedCh"
        assert managed_refs[0].getDest() == "USER-DEFINED-PHYSICAL-CHANNEL"

    def test_round_trip_empty_through_user_defined_physical_channel(self):
        parent = _write_user_defined_physical_channel(_new_channel("Channel"))
        reloaded = _new_channel("Channel")
        ARXMLParser().readUserDefinedPhysicalChannel(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Channel"
        assert reloaded.getCommConnectorRefs() == []
        assert reloaded.getManagedPhysicalChannelRefs() == []


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("Cluster")
    channel = cluster.createUserDefinedPhysicalChannel("UserDefinedPhysicalChannel")
    comm_connector_ref = RefType()
    comm_connector_ref.setDest("COMMUNICATION-CONNECTOR")
    comm_connector_ref.setValue("/EcuInst/Conn")
    channel.addCommConnectorRef(comm_connector_ref)
    managed_ref = RefType()
    managed_ref.setDest("USER-DEFINED-PHYSICAL-CHANNEL")
    managed_ref.setValue("/Cluster/ManagedCh")
    channel.addManagedPhysicalChannelRef(managed_ref)

    out_file = str(tmp_path / "user_defined_physical_channel.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_cluster = re_pkg.getReferrableElement("Cluster", UserDefinedCluster)
    assert re_cluster is not None

    re_channels = re_cluster.getPhysicalChannels()
    assert len(re_channels) == 1
    re_channel = re_channels[0]
    assert isinstance(re_channel, UserDefinedPhysicalChannel)
    assert re_channel.getShortName() == "UserDefinedPhysicalChannel"
    comm_connector_refs = re_channel.getCommConnectorRefs()
    assert len(comm_connector_refs) == 1
    assert comm_connector_refs[0].getValue() == "/EcuInst/Conn"
    assert comm_connector_refs[0].getDest() == "COMMUNICATION-CONNECTOR"
    managed_refs = re_channel.getManagedPhysicalChannelRefs()
    assert len(managed_refs) == 1
    assert managed_refs[0].getValue() == "/Cluster/ManagedCh"
    assert managed_refs[0].getDest() == "USER-DEFINED-PHYSICAL-CHANNEL"


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = pkg.createUserDefinedCluster("Cluster")
    cluster.createUserDefinedPhysicalChannel("EmptyChannel")

    out_file = str(tmp_path / "user_defined_physical_channel_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_cluster = re_pkg.getReferrableElement("Cluster", UserDefinedCluster)
    re_channels = re_cluster.getPhysicalChannels()
    assert len(re_channels) == 1
    assert isinstance(re_channels[0], UserDefinedPhysicalChannel)
    assert re_channels[0].getShortName() == "EmptyChannel"
    assert re_channels[0].getCommConnectorRefs() == []
    assert re_channels[0].getManagedPhysicalChannelRefs() == []
