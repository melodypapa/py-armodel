"""Writer/reader round-trip tests for ConsumedEventGroup (Table 6.168, p.505)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdClientConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedEventGroup, PduActivationRoutingGroup
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("ROOT")


def _namespaced_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _full_group():
    group = ConsumedEventGroup(MockParent(), "MyEventGroup")
    group.setApplicationEndpointRef(_ref("APPLICATION-ENDPOINT", "/Ether/Endpoint/AE1"))
    group.setAutoRequire(_bool("true"))
    group.setEventGroupIdentifier(_pos_int("42"))
    group.addEventMulticastAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/Endpoint/MC1"))
    group.addEventMulticastAddressRef(_ref("APPLICATION-ENDPOINT", "/Ether/Endpoint/MC2"))
    group.setPriority(_pos_int("5"))
    group.addRoutingGroupRef(_ref("SOAD-ROUTING-GROUP", "/SoAd/RoutingGroup/RG1"))
    config = SdClientConfig()
    config.setClientServiceMajorVersion(_pos_int("15"))
    config.setTtl(_pos_int("10"))
    group.setSdClientConfig(config)
    group.setSdClientTimerConfigRef(_ref("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG", "/SomeipSdTimingConfigs/Timing1"))
    return group


class TestWriteConsumedEventGroup:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.writeConsumedEventGroup(parent, _full_group())

        el = parent.find("CONSUMED-EVENT-GROUP")
        assert el is not None
        assert el.find("SHORT-NAME").text == "MyEventGroup"
        assert el.find("APPLICATION-ENDPOINT-REF").text == "/Ether/Endpoint/AE1"
        assert el.find("AUTO-REQUIRE").text == "true"
        assert el.find("EVENT-GROUP-IDENTIFIER").text == "42"
        mc = el.find("EVENT-MULTICAST-ADDRESSS")
        assert mc is not None
        mc_refs = mc.findall("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF")
        assert [r.text for r in mc_refs] == ["/Ether/Endpoint/MC1", "/Ether/Endpoint/MC2"]
        assert el.find("PRIORITY").text == "5"
        rg = el.find("ROUTING-GROUP-REFS")
        assert rg is not None
        assert rg.find("ROUTING-GROUP-REF").text == "/SoAd/RoutingGroup/RG1"
        sdc = el.find("SD-CLIENT-CONFIG")
        assert sdc is not None
        assert sdc.find("CLIENT-SERVICE-MAJOR-VERSION").text == "15"
        assert sdc.find("TTL").text == "10"
        sdtc = el.find("SD-CLIENT-TIMER-CONFIGS")
        assert sdtc is not None
        assert sdtc.find("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL/SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF").text == "/SomeipSdTimingConfigs/Timing1"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = _parent()
        writer.writeConsumedEventGroup(parent, ConsumedEventGroup(MockParent(), "EmptyGroup"))

        el = parent.find("CONSUMED-EVENT-GROUP")
        assert el is not None
        assert el.find("APPLICATION-ENDPOINT-REF") is None
        assert el.find("AUTO-REQUIRE") is None
        assert el.find("EVENT-GROUP-IDENTIFIER") is None
        assert el.find("EVENT-MULTICAST-ADDRESSS") is None
        assert el.find("PRIORITY") is None
        assert el.find("ROUTING-GROUP-REFS") is None
        assert el.find("SD-CLIENT-CONFIG") is None
        assert el.find("SD-CLIENT-TIMER-CONFIGS") is None


class TestConsumedEventGroupRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        group = _full_group()

        parent = _parent()
        writer.writeConsumedEventGroup(parent, group)

        out_file = str(tmp_path / "consumed_event_group.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_namespaced_wrap(parent), encoding="unicode"))

        recovered = ConsumedEventGroup(MockParent(), "MyEventGroup")
        tree = ET.parse(out_file)
        parser.readConsumedEventGroup(tree.getroot(), recovered)

        assert recovered.getShortName() == "MyEventGroup"
        assert recovered.getApplicationEndpointRef().getValue() == "/Ether/Endpoint/AE1"
        assert recovered.getAutoRequire().getValue() is True
        assert recovered.getEventGroupIdentifier().getValue() == 42
        assert [r.getValue() for r in recovered.getEventMulticastAddressRefs()] == ["/Ether/Endpoint/MC1", "/Ether/Endpoint/MC2"]
        assert recovered.getPriority().getValue() == 5
        assert [r.getValue() for r in recovered.getRoutingGroupRefs()] == ["/SoAd/RoutingGroup/RG1"]
        re_config = recovered.getSdClientConfig()
        assert re_config is not None
        assert re_config.getClientServiceMajorVersion().getValue() == 15
        assert re_config.getTtl().getValue() == 10
        assert recovered.getSdClientTimerConfigRef().getValue() == "/SomeipSdTimingConfigs/Timing1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<CONSUMED-EVENT-GROUP xmlns='{NS}'><SHORT-NAME>EmptyGroup</SHORT-NAME></CONSUMED-EVENT-GROUP>")

        recovered = ConsumedEventGroup(MockParent(), "EmptyGroup")
        parser.readConsumedEventGroup(element, recovered)

        assert recovered.getApplicationEndpointRef() is None
        assert recovered.getAutoRequire() is None
        assert recovered.getEventGroupIdentifier() is None
        assert recovered.getEventMulticastAddressRefs() == []
        assert recovered.getPduActivationRoutingGroups() == []
        assert recovered.getPriority() is None
        assert recovered.getRoutingGroupRefs() == []
        assert recovered.getSdClientConfig() is None
        assert recovered.getSdClientTimerConfigRef() is None


def _activation_group(short_name, control_value):
    group = PduActivationRoutingGroup(MockParent(), short_name)
    literal = ARLiteral()
    literal.setValue(control_value)
    group.setEventGroupControlType(literal)
    return group


class TestConsumedEventGroupPduActivationRoutingGroups:
    def test_write_pdu_activation_routing_groups(self, writer):
        parent = _parent()
        group = ConsumedEventGroup(MockParent(), "CEG")
        group.addPduActivationRoutingGroup(_activation_group("PARG1", "activateAndTriggerUnicast"))
        group.addPduActivationRoutingGroup(_activation_group("PARG2", "deactivateAndTriggerUnicast"))
        writer.writeConsumedEventGroup(parent, group)

        el = parent.find("CONSUMED-EVENT-GROUP")
        wrapper = el.find("PDU-ACTIVATION-ROUTING-GROUPS")
        assert wrapper is not None
        entries = wrapper.findall("PDU-ACTIVATION-ROUTING-GROUP")
        assert len(entries) == 2
        assert entries[0].find("SHORT-NAME").text == "PARG1"
        assert entries[0].find("EVENT-GROUP-CONTROL-TYPE").text == "activateAndTriggerUnicast"
        assert entries[1].find("SHORT-NAME").text == "PARG2"

    def test_round_trip_preserves_pdu_activation_routing_groups(self, writer, parser):
        parent = _parent()
        group = ConsumedEventGroup(MockParent(), "CEG")
        group.addPduActivationRoutingGroup(_activation_group("PARG1", "activateAndTriggerUnicast"))
        group.addPduActivationRoutingGroup(_activation_group("PARG2", "deactivateAndTriggerUnicast"))
        writer.writeConsumedEventGroup(parent, group)

        element = _namespaced_wrap(parent)
        recovered = ConsumedEventGroup(MockParent(), "CEG")
        parser.readConsumedEventGroup(element, recovered)

        groups = recovered.getPduActivationRoutingGroups()
        assert len(groups) == 2
        assert isinstance(groups[0], PduActivationRoutingGroup)
        assert groups[0].getShortName() == "PARG1"
        assert groups[0].getEventGroupControlType().getValue() == "activateAndTriggerUnicast"
        assert groups[1].getShortName() == "PARG2"
        assert groups[1].getEventGroupControlType().getValue() == "deactivateAndTriggerUnicast"

    def test_reader_no_wrapper_leaves_list_empty(self, parser):
        element = ET.fromstring(f"<CONSUMED-EVENT-GROUP xmlns='{NS}'><SHORT-NAME>CEG</SHORT-NAME></CONSUMED-EVENT-GROUP>")
        recovered = ConsumedEventGroup(MockParent(), "CEG")
        parser.readConsumedEventGroup(element, recovered)
        assert recovered.getPduActivationRoutingGroups() == []
