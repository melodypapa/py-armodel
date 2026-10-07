"""Writer tests for ProvidedServiceInstance (sync R23-11, Table E.37)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    EventGroupControlTypeEnum,
    EventHandler,
    PduActivationRoutingGroup,
    PduCollectionSemanticsEnum,
    PduCollectionTriggerEnum,
    ProvidedServiceInstance,
    SoAdConfig,
    SocketAddress,
    SoConIPduIdentifier,
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
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


class TestWriteProvidedServiceInstance:
    def test_write_provided_service_instance_all_attrs(self, writer):
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        instance.setInstanceIdentifier(_pos_int("200"))
        instance.setLoadBalancingPriority(_pos_int("7"))
        instance.setLoadBalancingWeight(_pos_int("3"))
        instance.addLocalUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/ep1"))
        instance.setMinorVersion(_pos_int("2"))
        instance.setPriority(_pos_int("3"))
        instance.addRemoteMulticastSubscriptionAddressRef(_ref("APPLICATION-ENDPOINT", "/ep2"))
        instance.addRemoteUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/ep3"))
        instance.setSdServerTimerConfigRef(_ref("SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG", "/sd1"))
        instance.addAllowedServiceConsumerRef(_ref("NETWORK-ENDPOINT", "/nep1"))
        instance.setAutoAvailable(_bool("true"))
        instance.setServiceIdentifier(_pos_int("25"))

        parent = _parent()
        writer.writeProvidedServiceInstance(parent, instance)

        psi = parent.find("PROVIDED-SERVICE-INSTANCE")
        assert psi is not None
        assert psi.find("INSTANCE-IDENTIFIER").text == "200"
        assert psi.find("LOAD-BALANCING-PRIORITY").text == "7"
        assert psi.find("LOAD-BALANCING-WEIGHT").text == "3"
        assert psi.find("MINOR-VERSION").text == "2"
        assert psi.find("PRIORITY").text == "3"
        assert psi.find("SERVICE-IDENTIFIER").text == "25"
        lus = psi.find("LOCAL-UNICAST-ADDRESSS")
        assert lus is not None
        assert lus.find("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/ep1"
        rms = psi.find("REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS")
        assert rms is not None
        assert rms.find("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/ep2"
        ru = psi.find("REMOTE-UNICAST-ADDRESSS")
        assert ru is not None
        assert ru.find("APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF").text == "/ep3"
        sstc = psi.find("SD-SERVER-TIMER-CONFIGS")
        assert sstc is not None
        assert sstc.find("SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL/SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF").text == "/sd1"
        asc = psi.find("ALLOWED-SERVICE-CONSUMERS")
        assert asc is not None
        assert asc.find("NETWORK-ENDPOINT-REF-CONDITIONAL/NETWORK-ENDPOINT-REF").text == "/nep1"
        assert psi.find("AUTO-AVAILABLE").text == "true"

    def test_write_provided_service_instance_empty_ref_lists(self, writer):
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        parent = _parent()
        writer.writeProvidedServiceInstance(parent, instance)
        psi = parent.find("PROVIDED-SERVICE-INSTANCE")
        assert psi.find("LOCAL-UNICAST-ADDRESSS") is None
        assert psi.find("REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS") is None
        assert psi.find("REMOTE-UNICAST-ADDRESSS") is None
        assert psi.find("SD-SERVER-TIMER-CONFIGS") is None
        assert psi.find("ALLOWED-SERVICE-CONSUMERS") is None
        assert psi.find("AUTO-AVAILABLE") is None

    def test_round_trip_provided_service_instance(self, writer, parser):
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        instance.setInstanceIdentifier(_pos_int("200"))
        instance.setLoadBalancingPriority(_pos_int("7"))
        instance.setLoadBalancingWeight(_pos_int("3"))
        instance.addLocalUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/ep1"))
        instance.setMinorVersion(_pos_int("2"))
        instance.setPriority(_pos_int("3"))
        instance.addRemoteMulticastSubscriptionAddressRef(_ref("APPLICATION-ENDPOINT", "/ep2"))
        instance.addRemoteUnicastAddressRef(_ref("APPLICATION-ENDPOINT", "/ep3"))
        instance.setSdServerTimerConfigRef(_ref("SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG", "/sd1"))
        instance.addAllowedServiceConsumerRef(_ref("NETWORK-ENDPOINT", "/nep1"))
        instance.setAutoAvailable(_bool("true"))
        instance.setServiceIdentifier(_pos_int("25"))

        parent = _parent()
        writer.writeProvidedServiceInstance(parent, instance)
        element = _serialize_and_wrap(parent)

        recovered = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        parser.readProvidedServiceInstance(element, recovered)
        assert recovered.getInstanceIdentifier().getValue() == 200
        assert recovered.getLoadBalancingPriority().getValue() == 7
        assert recovered.getLoadBalancingWeight().getValue() == 3
        assert [r.getValue() for r in recovered.getLocalUnicastAddressRefs()] == ["/ep1"]
        assert recovered.getMinorVersion().getValue() == 2
        assert recovered.getPriority().getValue() == 3
        assert [r.getValue() for r in recovered.getRemoteMulticastSubscriptionAddressRefs()] == ["/ep2"]
        assert [r.getValue() for r in recovered.getRemoteUnicastAddressRefs()] == ["/ep3"]
        assert recovered.getSdServerTimerConfigRef().getValue() == "/sd1"
        assert [r.getValue() for r in recovered.getAllowedServiceConsumerRefs()] == ["/nep1"]
        assert recovered.getAutoAvailable().getValue() is True
        assert recovered.getServiceIdentifier().getValue() == 25


class TestWriteSoConIPduIdentifier:
    def test_write_and_read_back_so_con_ipdu_identifier(self, writer, parser):
        identifier = SoConIPduIdentifier(parent=None, short_name="ipdu_id1")
        header_id = PositiveInteger()
        header_id.setValue("4")
        timeout = TimeValue()
        timeout.setValue("0.5")
        semantics = PduCollectionSemanticsEnum().setValue(PduCollectionSemanticsEnum.QUEUED)
        trigger = PduCollectionTriggerEnum().setValue(PduCollectionTriggerEnum.ALWAYS)
        ref = RefType()
        ref.setDest("PDU-TRIGGERING")
        ref.setValue("/PduTriggerings/pt1")
        identifier.setHeaderId(header_id)
        identifier.setPduCollectionPduTimeout(timeout)
        identifier.setPduCollectionSemantics(semantics)
        identifier.setPduCollectionTrigger(trigger)
        identifier.setPduTriggeringRef(ref)

        parent = _parent()
        writer.writeSoConIPduIdentifier(parent, identifier)
        element = _serialize_and_wrap(parent)

        assert element.find(f"{{{NS}}}HEADER-ID").text == "4"
        assert element.find(f"{{{NS}}}PDU-COLLECTION-PDU-TIMEOUT").text == "0.5"
        assert element.find(f"{{{NS}}}PDU-COLLECTION-SEMANTICS").text == "QUEUED"
        assert element.find(f"{{{NS}}}PDU-COLLECTION-TRIGGER").text == "ALWAYS"
        triggering_ref = element.find(f"{{{NS}}}PDU-TRIGGERING-REF")
        assert triggering_ref.text == "/PduTriggerings/pt1"
        assert triggering_ref.get("DEST") == "PDU-TRIGGERING"

        recovered = SoConIPduIdentifier(parent=None, short_name="ipdu_id1")
        parser.readSoConIPduIdentifier(element, recovered)
        assert recovered.getHeaderId().getValue() == 4
        assert recovered.getPduCollectionPduTimeout().getValue() == 0.5
        assert recovered.getPduCollectionSemantics().getValue() == PduCollectionSemanticsEnum.QUEUED
        assert recovered.getPduCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS
        assert recovered.getPduTriggeringRef().getValue() == "/PduTriggerings/pt1"
        assert recovered.getPduTriggeringRef().getDest() == "PDU-TRIGGERING"

    def test_write_so_con_ipdu_identifier_empty_omits_elements(self, writer, parser):
        identifier = SoConIPduIdentifier(parent=None, short_name="ipdu_id1")

        parent = _parent()
        writer.writeSoConIPduIdentifier(parent, identifier)
        element = _serialize_and_wrap(parent)

        assert element.find(f"{{{NS}}}HEADER-ID") is None
        assert element.find(f"{{{NS}}}PDU-COLLECTION-PDU-TIMEOUT") is None
        assert element.find(f"{{{NS}}}PDU-COLLECTION-SEMANTICS") is None
        assert element.find(f"{{{NS}}}PDU-COLLECTION-TRIGGER") is None
        assert element.find(f"{{{NS}}}PDU-TRIGGERING-REF") is None

        recovered = SoConIPduIdentifier(parent=None, short_name="ipdu_id1")
        parser.readSoConIPduIdentifier(element, recovered)
        assert recovered.getHeaderId() is None
        assert recovered.getPduCollectionPduTimeout() is None
        assert recovered.getPduCollectionSemantics() is None
        assert recovered.getPduCollectionTrigger() is None
        assert recovered.getPduTriggeringRef() is None


class TestWriteEventHandler:
    def test_write_and_read_back_event_handler(self, writer, parser):
        handler = EventHandler(parent=None, short_name="eh1")
        group_ref = RefType()
        group_ref.setDest("CONSUMED-EVENT-GROUP")
        group_ref.setValue("/ceg1")
        event_group_identifier = PositiveInteger()
        event_group_identifier.setValue("1")
        multicast_ref = RefType()
        multicast_ref.setDest("APPLICATION-ENDPOINT")
        multicast_ref.setValue("/mc1")
        threshold = PositiveInteger()
        threshold.setValue("2")
        routing_group = PduActivationRoutingGroup(parent=None, short_name="parg1")
        control_type = EventGroupControlTypeEnum().setValue(EventGroupControlTypeEnum.ACTIVATION_MULTICAST)
        routing_group.setEventGroupControlType(control_type)
        routing_ref = RefType()
        routing_ref.setDest("SO-AD-ROUTING-GROUP")
        routing_ref.setValue("/rg1")
        timing_ref = RefType()
        timing_ref.setDest("SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG")
        timing_ref.setValue("/timing1")
        handler.addConsumedEventGroupRef(group_ref)
        handler.setEventGroupIdentifier(event_group_identifier)
        handler.setEventMulticastAddressRef(multicast_ref)
        handler.setMulticastThreshold(threshold)
        handler.addPduActivationRoutingGroup(routing_group)
        handler.addRoutingGroupRef(routing_ref)
        handler.setSdServerEgTimingConfigRef(timing_ref)

        parent = _parent()
        writer.writeEventHandler(parent, handler)
        element = _serialize_and_wrap(parent)

        assert element.find(f"{{{NS}}}EVENT-GROUP-IDENTIFIER").text == "1"
        assert element.find(f"{{{NS}}}MULTICAST-THRESHOLD").text == "2"
        control_type_tag = element.find(f"{{{NS}}}PDU-ACTIVATION-ROUTING-GROUPS/{{{NS}}}PDU-ACTIVATION-ROUTING-GROUP/{{{NS}}}EVENT-GROUP-CONTROL-TYPE")
        assert control_type_tag.text == "ACTIVATION-MULTICAST"

        recovered = EventHandler(parent=None, short_name="eh1")
        parser.readEventHandler(element, recovered)
        assert [r.getValue() for r in recovered.getConsumedEventGroupRefs()] == ["/ceg1"]
        assert recovered.getEventGroupIdentifier().getValue() == 1
        assert recovered.getEventMulticastAddressRef().getValue() == "/mc1"
        assert recovered.getMulticastThreshold().getValue() == 2
        assert len(recovered.getPduActivationRoutingGroups()) == 1
        assert recovered.getPduActivationRoutingGroups()[0].getEventGroupControlType().getValue() == EventGroupControlTypeEnum.ACTIVATION_MULTICAST
        assert [r.getValue() for r in recovered.getRoutingGroupRefs()] == ["/rg1"]
        assert recovered.getSdServerEgTimingConfigRef().getValue() == "/timing1"

    def test_write_event_handler_empty_omits_elements(self, writer, parser):
        handler = EventHandler(parent=None, short_name="eh1")

        parent = _parent()
        writer.writeEventHandler(parent, handler)
        element = _serialize_and_wrap(parent)

        assert element.find(f"{{{NS}}}CONSUMED-EVENT-GROUP-REFS") is None
        assert element.find(f"{{{NS}}}EVENT-GROUP-IDENTIFIER") is None
        assert element.find(f"{{{NS}}}EVENT-MULTICAST-ADDRESSS") is None
        assert element.find(f"{{{NS}}}MULTICAST-THRESHOLD") is None
        assert element.find(f"{{{NS}}}PDU-ACTIVATION-ROUTING-GROUPS") is None
        assert element.find(f"{{{NS}}}ROUTING-GROUP-REFS") is None
        assert element.find(f"{{{NS}}}SD-SERVER-CONFIG") is None
        assert element.find(f"{{{NS}}}SD-SERVER-EG-TIMING-CONFIGS") is None
