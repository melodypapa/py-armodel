"""Tests for ProvidedServiceInstance reader coverage (sync R23-11, Table E.37)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    ProvidedServiceInstance,
    SoAdConfig,
    SocketAddress,
)

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
            "<ALLOWED-SERVICE-CONSUMERS>"
            "<NETWORK-ENDPOINT-REF-CONDITIONAL>"
            "<NETWORK-ENDPOINT-REF DEST='NETWORK-ENDPOINT'>/nep1</NETWORK-ENDPOINT-REF>"
            "</NETWORK-ENDPOINT-REF-CONDITIONAL>"
            "</ALLOWED-SERVICE-CONSUMERS>"
            "<AUTO-AVAILABLE>true</AUTO-AVAILABLE>"
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
        assert len(instance.getAllowedServiceConsumerRefs()) == 1
        assert instance.getAllowedServiceConsumerRefs()[0].getValue() == "/nep1"
        assert instance.getAutoAvailable().getValue() is True
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
        assert instance.getAllowedServiceConsumerRefs() == []
        assert instance.getAutoAvailable() is None
        assert instance.getSdServerTimerConfigRef() is None
