"""Writer round-trip tests for SomeipSdServerServiceInstanceConfig (R23-11 CP_TPS_SystemTemplate, Table 6.169, p.514).

Aggregated by ARPackage.element - the ARPackage ELEMENTS choice serializes the ARElement
subclass. Also upgrades the ProvidedServiceInstance.sdServerTimerConfigRef identity-only
debt (Rule 0001.7): the referenced config is now serialized with real field values.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    InitialSdDelayConfig,
    ProvidedServiceInstance,
    RequestResponseDelay,
    SocketAddress,
    SomeipSdServerServiceInstanceConfig,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_config(short_name="ServerConfig"):
    config = SomeipSdServerServiceInstanceConfig(None, short_name)
    behavior = InitialSdDelayConfig()
    behavior.setInitialDelayMaxValue(TimeValue().setValue("0.1"))
    behavior.setInitialRepetitionsMax(PositiveInteger().setValue("3"))
    config.setInitialOfferBehavior(behavior)
    config.setOfferCyclicDelay(TimeValue().setValue("2.0"))
    config.setPriority(PositiveInteger().setValue("6"))
    delay = RequestResponseDelay()
    delay.setMaxValue(TimeValue().setValue("0.5"))
    delay.setMinValue(TimeValue().setValue("0.05"))
    config.setRequestResponseDelay(delay)
    config.setServiceOfferTimeToLive(PositiveInteger().setValue("30"))
    return config


def _namespaced(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSomeipSdServerServiceInstanceConfig:
    def test_write_all_attrs(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_config())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG")
        assert node is not None
        assert node.find("SHORT-NAME").text == "ServerConfig"
        assert node.findtext("INITIAL-OFFER-BEHAVIOR/INITIAL-DELAY-MAX-VALUE") == "0.1"
        assert node.findtext("INITIAL-OFFER-BEHAVIOR/INITIAL-REPETITIONS-MAX") == "3"
        assert node.findtext("OFFER-CYCLIC-DELAY") == "2.0"
        assert node.findtext("PRIORITY") == "6"
        assert node.findtext("REQUEST-RESPONSE-DELAY/MAX-VALUE") == "0.5"
        assert node.findtext("REQUEST-RESPONSE-DELAY/MIN-VALUE") == "0.05"
        assert node.findtext("SERVICE-OFFER-TIME-TO-LIVE") == "30"

    def test_write_empty_omits_elements(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(SomeipSdServerServiceInstanceConfig(None, "EmptyConfig"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG")
        assert node is not None
        assert node.find("INITIAL-OFFER-BEHAVIOR") is None
        assert node.find("OFFER-CYCLIC-DELAY") is None
        assert node.find("PRIORITY") is None
        assert node.find("REQUEST-RESPONSE-DELAY") is None
        assert node.find("SERVICE-OFFER-TIME-TO-LIVE") is None

    def test_round_trip_preserves_field_values(self):
        writer = ARXMLWriter()
        parser = ARXMLParser()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_config())
        parent = ET.Element("PARENT")
        writer.writeARPackageElements(parent, package)
        root = _namespaced(parent)

        reloaded_package = AUTOSAR.getInstance().createARPackage("Pkg2")
        parser.readARPackageElements(root, reloaded_package)

        config = reloaded_package.getReferrableElement("ServerConfig", SomeipSdServerServiceInstanceConfig)
        assert isinstance(config, SomeipSdServerServiceInstanceConfig)
        assert config.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1
        assert config.getInitialOfferBehavior().getInitialRepetitionsMax().getValue() == 3
        assert config.getOfferCyclicDelay().getValue() == 2.0
        assert config.getPriority().getValue() == 6
        assert config.getRequestResponseDelay().getMaxValue().getValue() == 0.5
        assert config.getRequestResponseDelay().getMinValue().getValue() == 0.05
        assert config.getServiceOfferTimeToLive().getValue() == 30

    def test_provided_service_instance_sd_server_timer_config_ref_round_trip(self):
        """Rule 0001.7 identity-debt upgrade: the sdServerTimerConfigRef target carries real field values."""
        writer = ARXMLWriter()
        parser = ARXMLParser()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_config("sd1"))

        address = SocketAddress(parent=None, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        ref = RefType()
        ref.setDest("SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG")
        ref.setValue("/Pkg/sd1")
        instance.setSdServerTimerConfigRef(ref)

        parent = ET.Element("PARENT")
        writer.writeProvidedServiceInstance(parent, instance)
        psi_node = parent.find("PROVIDED-SERVICE-INSTANCE")
        psi_root = ET.fromstring(ET.tostring(psi_node).decode("utf-8").replace("<PROVIDED-SERVICE-INSTANCE>", "<PROVIDED-SERVICE-INSTANCE xmlns='%s'>" % NS, 1))
        recovered = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        parser.readProvidedServiceInstance(psi_root, recovered)

        assert recovered.getSdServerTimerConfigRef().getValue() == "/Pkg/sd1"
        assert recovered.getSdServerTimerConfigRef().getDest() == "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG"

        package_parent = ET.Element("PARENT")
        writer.writeARPackageElements(package_parent, package)
        package_root = _namespaced(package_parent)
        reloaded_package = AUTOSAR.getInstance().createARPackage("Pkg2")
        parser.readARPackageElements(package_root, reloaded_package)

        config = reloaded_package.getReferrableElement("sd1", SomeipSdServerServiceInstanceConfig)
        assert isinstance(config, SomeipSdServerServiceInstanceConfig)
        assert config.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1
        assert config.getOfferCyclicDelay().getValue() == 2.0
        assert config.getPriority().getValue() == 6
        assert config.getRequestResponseDelay().getMinValue().getValue() == 0.05
        assert config.getServiceOfferTimeToLive().getValue() == 30
