"""Writer tests for ProvidedServiceInstance (sync R23-11, Table E.37)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    ProvidedServiceInstance,
    SoAdConfig,
    SocketAddress,
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
