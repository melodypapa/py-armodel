"""Writer/reader round-trip tests for EventHandler (Table 6.166, p.492).

EventHandler is an Identifiable value type aggregated by
ProvidedServiceInstance.eventHandler.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventHandler,
    PduActivationRoutingGroup,
    SdServerConfig,
)
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


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _full_handler():
    handler = EventHandler(MockParent(), "EH1")
    ref = RefType()
    ref.setValue("/Ether/ConsumedEventGroup/CEG1")
    handler.addConsumedEventGroupRef(ref)
    identifier = PositiveInteger().setValue(7)
    handler.setEventGroupIdentifier(identifier)
    mc_ref = RefType()
    mc_ref.setValue("/Ether/ApplicationEndpoint/MC1")
    handler.setEventMulticastAddressRef(mc_ref)
    threshold = PositiveInteger().setValue(3)
    handler.setMulticastThreshold(threshold)
    group = PduActivationRoutingGroup(MockParent(), "PARG1")
    handler.addPduActivationRoutingGroup(group)
    routing_ref = RefType()
    routing_ref.setValue("/Ether/SoAdRoutingGroup/RG1")
    handler.addRoutingGroupRef(routing_ref)
    server_config = SdServerConfig()
    handler.setSdServerConfig(server_config)
    timing_ref = RefType()
    timing_ref.setValue("/SomeipSdTimingConfigs/ServerTiming1")
    handler.setSdServerEgTimingConfigRef(timing_ref)
    return handler


class TestWriteEventHandler:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PROVIDED-SERVICE-INSTANCE")
        writer.writeEventHandler(parent, _full_handler())

        el = parent.find("EVENT-HANDLER")
        assert el is not None
        assert el.find("SHORT-NAME").text == "EH1"
        ceg_refs = el.findall("CONSUMED-EVENT-GROUP-REFS/CONSUMED-EVENT-GROUP-REF")
        assert len(ceg_refs) == 1
        assert ceg_refs[0].text == "/Ether/ConsumedEventGroup/CEG1"
        assert el.find("EVENT-GROUP-IDENTIFIER").text == "7"
        mc = el.find("EVENT-MULTICAST-ADDRESSS/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF")
        assert mc is not None
        assert mc.text == "/Ether/ApplicationEndpoint/MC1"
        assert el.find("MULTICAST-THRESHOLD").text == "3"
        group = el.find("PDU-ACTIVATION-ROUTING-GROUPS/PDU-ACTIVATION-ROUTING-GROUP")
        assert group is not None
        assert group.find("SHORT-NAME").text == "PARG1"
        rg_refs = el.findall("ROUTING-GROUP-REFS/ROUTING-GROUP-REF")
        assert len(rg_refs) == 1
        assert rg_refs[0].text == "/Ether/SoAdRoutingGroup/RG1"
        assert el.find("SD-SERVER-CONFIG") is not None
        timing_ref = el.find("SD-SERVER-EG-TIMING-CONFIGS/SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL/SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF")
        assert timing_ref.text == "/SomeipSdTimingConfigs/ServerTiming1"

    def test_write_removed_application_endpoint_ref_omitted(self, writer):
        """APPLICATION-ENDPOINT-REF is atp.Status=removed since 4.4.0 (Rule 0015)."""
        parent = ET.Element("PROVIDED-SERVICE-INSTANCE")
        handler = EventHandler(MockParent(), "EH1")
        writer.writeEventHandler(parent, handler)

        el = parent.find("EVENT-HANDLER")
        assert el.find("APPLICATION-ENDPOINT-REF") is None


class TestEventHandlerRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PROVIDED-SERVICE-INSTANCE")
        writer.writeEventHandler(parent, _full_handler())

        out_file = str(tmp_path / "event_handler.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = EventHandler(MockParent(), "EH1")
        parser.readEventHandler(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "EH1"
        assert recovered.getConsumedEventGroupRefs()[0].getValue() == "/Ether/ConsumedEventGroup/CEG1"
        assert recovered.getEventGroupIdentifier().getValue() == 7
        assert recovered.getEventMulticastAddressRef().getValue() == "/Ether/ApplicationEndpoint/MC1"
        assert recovered.getMulticastThreshold().getValue() == 3
        groups = recovered.getPduActivationRoutingGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], PduActivationRoutingGroup)
        assert groups[0].getShortName() == "PARG1"
        assert recovered.getRoutingGroupRefs()[0].getValue() == "/Ether/SoAdRoutingGroup/RG1"
        assert isinstance(recovered.getSdServerConfig(), SdServerConfig)
        assert recovered.getSdServerEgTimingConfigRef().getValue() == "/SomeipSdTimingConfigs/ServerTiming1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring(f"<EVENT-HANDLER xmlns='{NS}'><SHORT-NAME>Empty</SHORT-NAME></EVENT-HANDLER>")
        recovered = EventHandler(MockParent(), "Empty")
        parser.readEventHandler(element, recovered)

        assert recovered.getEventGroupIdentifier() is None
        assert recovered.getEventMulticastAddressRef() is None
        assert recovered.getPduActivationRoutingGroups() == []
        assert recovered.getSdServerEgTimingConfigRef() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
