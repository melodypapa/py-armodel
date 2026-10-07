"""Tests for ProvidedServiceInstance reader coverage (sync R23-11, Table E.37)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    EventHandler,
    ProvidedServiceInstance,
    SoAdConfig,
    SocketAddress,
    SoConIPduIdentifier,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "PROVIDED-SERVICE-INSTANCE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadProvidedServiceInstance:
    def test_read_provided_service_instance_all_attrs(self, parser):
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip(
            "<SHORT-NAME>psi</SHORT-NAME>"
            "<INSTANCE-IDENTIFIER>200</INSTANCE-IDENTIFIER>"
            "<LOAD-BALANCING-PRIORITY>7</LOAD-BALANCING-PRIORITY>"
            "<LOAD-BALANCING-WEIGHT>3</LOAD-BALANCING-WEIGHT>"
            "<LOCAL-UNICAST-ADDRESSS>"
            "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/ep1</APPLICATION-ENDPOINT-REF>"
            "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "</LOCAL-UNICAST-ADDRESSS>"
            "<MINOR-VERSION>2</MINOR-VERSION>"
            "<PRIORITY>3</PRIORITY>"
            "<REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS>"
            "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/ep2</APPLICATION-ENDPOINT-REF>"
            "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "</REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS>"
            "<REMOTE-UNICAST-ADDRESSS>"
            "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/ep3</APPLICATION-ENDPOINT-REF>"
            "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "</REMOTE-UNICAST-ADDRESSS>"
            "<SD-SERVER-TIMER-CONFIGS>"
            "<SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL>"
            "<SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF DEST='SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG'>/sd1</SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF>"
            "</SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL>"
            "</SD-SERVER-TIMER-CONFIGS>"
            "<SERVICE-IDENTIFIER>25</SERVICE-IDENTIFIER>"
        )
        parser.readProvidedServiceInstance(element, instance)
        assert instance.getInstanceIdentifier().getValue() == 200
        assert instance.getLoadBalancingPriority().getValue() == 7
        assert instance.getLoadBalancingWeight().getValue() == 3
        assert len(instance.getLocalUnicastAddressRefs()) == 1
        assert instance.getLocalUnicastAddressRefs()[0].getValue() == "/ep1"
        assert instance.getMinorVersion().getValue() == 2
        assert instance.getPriority().getValue() == 3
        assert len(instance.getRemoteMulticastSubscriptionAddressRefs()) == 1
        assert instance.getRemoteMulticastSubscriptionAddressRefs()[0].getValue() == "/ep2"
        assert len(instance.getRemoteUnicastAddressRefs()) == 1
        assert instance.getRemoteUnicastAddressRefs()[0].getValue() == "/ep3"
        assert instance.getSdServerTimerConfigRef().getValue() == "/sd1"
        assert instance.getServiceIdentifier().getValue() == 25

    def test_read_provided_service_instance_empty_ref_lists(self, parser):
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip("<SHORT-NAME>psi</SHORT-NAME>")
        parser.readProvidedServiceInstance(element, instance)
        assert instance.getLocalUnicastAddressRefs() == []
        assert instance.getRemoteMulticastSubscriptionAddressRefs() == []
        assert instance.getRemoteUnicastAddressRefs() == []
        assert instance.getSdServerTimerConfigRef() is None


def _so_con_snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<SO-CON-I-PDU-IDENTIFIER xmlns='{NS}'>{inner}</SO-CON-I-PDU-IDENTIFIER>")


class TestReadSoConIPduIdentifier:
    def _identifier(self):
        return SoConIPduIdentifier(parent=None, short_name="ipdu_id1")

    def test_read_so_con_ipdu_identifier_all_attrs(self, parser):
        identifier = self._identifier()
        element = _so_con_snip(
            "<SHORT-NAME>ipdu_id1</SHORT-NAME>"
            "<HEADER-ID>4</HEADER-ID>"
            "<PDU-COLLECTION-PDU-TIMEOUT>0.5</PDU-COLLECTION-PDU-TIMEOUT>"
            "<PDU-COLLECTION-SEMANTICS>QUEUED</PDU-COLLECTION-SEMANTICS>"
            "<PDU-COLLECTION-TRIGGER>ALWAYS</PDU-COLLECTION-TRIGGER>"
            "<PDU-TRIGGERING-REF DEST='PDU-TRIGGERING'>/PduTriggerings/pt1</PDU-TRIGGERING-REF>"
        )
        parser.readSoConIPduIdentifier(element, identifier)
        assert identifier.getHeaderId().getValue() == 4
        assert identifier.getPduCollectionPduTimeout().getValue() == 0.5
        assert identifier.getPduCollectionSemantics().getValue() == "QUEUED"
        assert identifier.getPduCollectionTrigger().getValue() == "ALWAYS"
        assert identifier.getPduTriggeringRef().getValue() == "/PduTriggerings/pt1"
        assert identifier.getPduTriggeringRef().getDest() == "PDU-TRIGGERING"

    def test_read_so_con_ipdu_identifier_empty(self, parser):
        identifier = self._identifier()
        element = _so_con_snip("<SHORT-NAME>ipdu_id1</SHORT-NAME>")
        parser.readSoConIPduIdentifier(element, identifier)
        assert identifier.getHeaderId() is None
        assert identifier.getPduCollectionPduTimeout() is None
        assert identifier.getPduCollectionSemantics() is None
        assert identifier.getPduCollectionTrigger() is None
        assert identifier.getPduTriggeringRef() is None


class TestReadEventHandler:
    def _handler(self):
        return EventHandler(parent=None, short_name="eh1")

    def test_read_event_handler_all_attrs(self, parser):
        handler = self._handler()
        element = ET.fromstring(
            f"<EVENT-HANDLER xmlns='{NS}'>"
            "<SHORT-NAME>eh1</SHORT-NAME>"
            "<CONSUMED-EVENT-GROUP-REFS>"
            "<CONSUMED-EVENT-GROUP-REF DEST='CONSUMED-EVENT-GROUP'>/ceg1</CONSUMED-EVENT-GROUP-REF>"
            "</CONSUMED-EVENT-GROUP-REFS>"
            "<EVENT-GROUP-IDENTIFIER>1</EVENT-GROUP-IDENTIFIER>"
            "<EVENT-MULTICAST-ADDRESSS>"
            "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/mc1</APPLICATION-ENDPOINT-REF>"
            "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
            "</EVENT-MULTICAST-ADDRESSS>"
            "<MULTICAST-THRESHOLD>2</MULTICAST-THRESHOLD>"
            "<ROUTING-GROUP-REFS>"
            "<ROUTING-GROUP-REF DEST='SO-AD-ROUTING-GROUP'>/rg1</ROUTING-GROUP-REF>"
            "</ROUTING-GROUP-REFS>"
            "<SD-SERVER-EG-TIMING-CONFIGS>"
            "<SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
            "<SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF DEST='SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG'>/timing1</SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF>"
            "</SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
            "</SD-SERVER-EG-TIMING-CONFIGS>"
            "</EVENT-HANDLER>"
        )
        parser.readEventHandler(element, handler)
        assert [r.getValue() for r in handler.getConsumedEventGroupRefs()] == ["/ceg1"]
        assert handler.getEventGroupIdentifier().getValue() == 1
        assert handler.getEventMulticastAddressRef().getValue() == "/mc1"
        assert handler.getMulticastThreshold().getValue() == 2
        assert [r.getValue() for r in handler.getRoutingGroupRefs()] == ["/rg1"]
        assert handler.getSdServerEgTimingConfigRef().getValue() == "/timing1"
        assert handler.getSdServerEgTimingConfigRef().getDest() == "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG"

    def test_read_event_handler_empty(self, parser):
        handler = self._handler()
        element = ET.fromstring(f"<EVENT-HANDLER xmlns='{NS}'><SHORT-NAME>eh1</SHORT-NAME></EVENT-HANDLER>")
        parser.readEventHandler(element, handler)
        assert handler.getConsumedEventGroupRefs() == []
        assert handler.getEventGroupIdentifier() is None
        assert handler.getEventMulticastAddressRef() is None
        assert handler.getMulticastThreshold() is None
        assert handler.getPduActivationRoutingGroups() == []
        assert handler.getRoutingGroupRefs() == []
        assert handler.getSdServerConfig() is None
        assert handler.getSdServerEgTimingConfigRef() is None
