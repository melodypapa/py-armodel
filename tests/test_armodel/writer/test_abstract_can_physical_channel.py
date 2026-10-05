"""Writer round-trip tests for AbstractCanPhysicalChannel (Table 3.20, p.73).

The class is abstract with no own attribute rows (Table 3.20 renders the
Attribute header only) and its XSD group ABSTRACT-CAN-PHYSICAL-CHANNEL
(AUTOSAR_00052.xsd line 218) is an empty <xsd:sequence/>: the abstract level
contributes no XML elements of its own. Coverage therefore runs through the
concrete CAN-PHYSICAL-CHANNEL emission (writeCanPhysicalChannel on a
CanPhysicalChannel instance, which calls the base writePhysicalChannel helper
exactly once) and asserts the abstract level neither adds nor drops elements.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanPhysicalChannel,
    CanPhysicalChannel,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_channel():
    channel = CanPhysicalChannel(MockParent(), "ch")
    channel.addCommConnectorRef(_ref("/ecu/can_conn", "CAN-COMMUNICATION-CONNECTOR"))
    can_ft = channel.createCanFrameTriggering("can_ft")
    can_ft.setFrameRef(_ref("/cluster/frames/frame1", "CAN-FRAME"))
    channel.createISignalTriggering("ist")
    channel.addManagedPhysicalChannelRef(_ref("/cluster/ch2", "FLEXRAY-PHYSICAL-CHANNEL"))
    channel.createPduTriggering("pdt")
    return channel


def _bare_channel():
    return CanPhysicalChannel(MockParent(), "ch")


def _write_channel(channel):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeCanPhysicalChannel(parent, channel)
    return parent


def _namespaced_channel_tag(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteAbstractCanPhysicalChannel:
    def test_writes_instance_of_abstract_can_physical_channel_with_values(self, writer):
        channel = _full_channel()
        assert isinstance(channel, AbstractCanPhysicalChannel)

        parent = _write_channel(channel)
        channel_tag = parent.find("CAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        assert channel_tag.find("SHORT-NAME").text == "ch"

        conditional = channel_tag.find("COMM-CONNECTORS/COMMUNICATION-CONNECTOR-REF-CONDITIONAL")
        assert conditional is not None
        comm_ref = conditional.find("COMMUNICATION-CONNECTOR-REF")
        assert comm_ref.get("DEST") == "CAN-COMMUNICATION-CONNECTOR"
        assert comm_ref.text == "/ecu/can_conn"

        assert channel_tag.find("FRAME-TRIGGERINGS/CAN-FRAME-TRIGGERING/SHORT-NAME").text == "can_ft"
        assert channel_tag.find("I-SIGNAL-TRIGGERINGS/I-SIGNAL-TRIGGERING/SHORT-NAME").text == "ist"
        managed_ref = channel_tag.find("MANAGED-PHYSICAL-CHANNEL-REFS/MANAGED-PHYSICAL-CHANNEL-REF")
        assert managed_ref.get("DEST") == "FLEXRAY-PHYSICAL-CHANNEL"
        assert managed_ref.text == "/cluster/ch2"
        assert channel_tag.find("PDU-TRIGGERINGS/PDU-TRIGGERING/SHORT-NAME").text == "pdt"

    def test_write_empty_wrapper_emits_no_abstract_level_elements(self, writer):
        parent = _write_channel(_bare_channel())
        channel_tag = parent.find("CAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        assert [child.tag for child in channel_tag] == ["SHORT-NAME"]

    def test_round_trip_full(self, writer, parser):
        parent = _write_channel(_full_channel())
        reloaded = _bare_channel()
        parser.readCanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert isinstance(reloaded, AbstractCanPhysicalChannel)

        comm_refs = reloaded.getCommConnectorRefs()
        assert len(comm_refs) == 1
        assert comm_refs[0].getValue() == "/ecu/can_conn"
        assert comm_refs[0].getDest() == "CAN-COMMUNICATION-CONNECTOR"

        triggerings = reloaded.getFrameTriggerings()
        assert len(triggerings) == 1
        assert triggerings[0].getShortName() == "can_ft"
        assert triggerings[0].getFrameRef().getValue() == "/cluster/frames/frame1"

        assert reloaded.getISignalTriggerings()[0].getShortName() == "ist"

        managed_refs = reloaded.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/cluster/ch2"

        assert reloaded.getPduTriggerings()[0].getShortName() == "pdt"

    def test_round_trip_empty(self, writer, parser):
        parent = _write_channel(_bare_channel())
        reloaded = _bare_channel()
        parser.readCanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert reloaded.getCommConnectorRefs() == []
        assert reloaded.getFrameTriggerings() == []
        assert reloaded.getISignalTriggerings() == []
        assert reloaded.getManagedPhysicalChannelRefs() == []
        assert reloaded.getPduTriggerings() == []
