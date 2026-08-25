"""Writer/reader round-trip tests for PduActivationRoutingGroup (Table 6.161, p.489).

PduActivationRoutingGroup is an Identifiable value type aggregated by
AbstractServiceInstance.methodActivationRoutingGroup,
ConsumedEventGroup.pduActivationRoutingGroups and EventHandler.pduActivationRoutingGroups.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduActivationRoutingGroup
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


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_group(short_name="Group1"):
    group = PduActivationRoutingGroup(MockParent(), short_name)
    control_type = ARLiteral().setValue("activateAndTriggerUnicast")
    group.setEventGroupControlType(control_type)
    ref_tcp_1 = RefType()
    ref_tcp_1.setValue("/SoCon/IPduTcp1")
    ref_tcp_2 = RefType()
    ref_tcp_2.setValue("/SoCon/IPduTcp2")
    ref_udp = RefType()
    ref_udp.setValue("/SoCon/IPduUdp1")
    group.addIPduIdentifierTcpRef(ref_tcp_1)
    group.addIPduIdentifierTcpRef(ref_tcp_2)
    group.addIPduIdentifierUdpRef(ref_udp)
    return group


class TestWritePduActivationRoutingGroup:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setPduActivationRoutingGroup(parent, _new_group())
        node = parent.find("PDU-ACTIVATION-ROUTING-GROUP")
        assert node is not None
        assert node.find("EVENT-GROUP-CONTROL-TYPE").text == "activateAndTriggerUnicast"
        tcp_refs = node.findall("I-PDU-IDENTIFIER-TCP-REFS/I-PDU-IDENTIFIER-TCP-REF")
        assert len(tcp_refs) == 2
        assert tcp_refs[0].text == "/SoCon/IPduTcp1"
        assert tcp_refs[1].text == "/SoCon/IPduTcp2"
        udp_refs = node.findall("I-PDU-IDENTIFIER-UDP-REFS/I-PDU-IDENTIFIER-UDP-REF")
        assert len(udp_refs) == 1
        assert udp_refs[0].text == "/SoCon/IPduUdp1"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.setPduActivationRoutingGroup(parent, PduActivationRoutingGroup(MockParent(), "Empty"))
        node = parent.find("PDU-ACTIVATION-ROUTING-GROUP")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("EVENT-GROUP-CONTROL-TYPE") is None
        assert node.find("I-PDU-IDENTIFIER-TCP-REFS") is None
        assert node.find("I-PDU-IDENTIFIER-UDP-REFS") is None


class TestPduActivationRoutingGroupRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setPduActivationRoutingGroup(parent, _new_group())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getPduActivationRoutingGroup(root[0][0])
        assert isinstance(parsed, PduActivationRoutingGroup)
        assert parsed.getShortName() == "Group1"
        assert parsed.getEventGroupControlType().getValue() == "activateAndTriggerUnicast"
        tcp_refs = parsed.getIPduIdentifierTcpRefs()
        assert len(tcp_refs) == 2
        assert tcp_refs[0].getValue() == "/SoCon/IPduTcp1"
        assert tcp_refs[1].getValue() == "/SoCon/IPduTcp2"
        udp_refs = parsed.getIPduIdentifierUdpRefs()
        assert len(udp_refs) == 1
        assert udp_refs[0].getValue() == "/SoCon/IPduUdp1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<PDU-ACTIVATION-ROUTING-GROUP xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></PDU-ACTIVATION-ROUTING-GROUP>" % NS)
        parsed = parser.getPduActivationRoutingGroup(element)
        assert isinstance(parsed, PduActivationRoutingGroup)
        assert parsed.getEventGroupControlType() is None
        assert parsed.getIPduIdentifierTcpRefs() == []
        assert parsed.getIPduIdentifierUdpRefs() == []
