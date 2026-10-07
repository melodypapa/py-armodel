"""Spec-sync tests for SomeipSdServerServiceInstanceConfig (R23-11 CP_TPS_SystemTemplate, Table 6.169, p.514)."""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    InitialSdDelayConfig,
    RequestResponseDelay,
    SomeipSdServerServiceInstanceConfig,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSomeipSdServerServiceInstanceConfig:
    MEMBERS = [
        "initialOfferBehavior",
        "offerCyclicDelay",
        "priority",
        "requestResponseDelay",
        "serviceOfferTimeToLive",
    ]

    INITIAL_OFFER_BEHAVIOR_NOTE = "Controls offer behavior of the server."
    OFFER_CYCLIC_DELAY_NOTE = "Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds) and greater then 0."
    PRIORITY_NOTE = (
        "This attribute defines the VLAN frame priority for Service Discovery messages that result from ProvidedSomeipServiceInstances "
        "that are referencing the SomeipSdServerServiceInstanceConfig (OfferService, StopOfferService, SubscribeEventGroupAck). "
        "Values from 0 (best effort) to 7 (highest) are allowed."
    )
    REQUEST_RESPONSE_DELAY_NOTE = (
        "Maximum/Minimum allowable response delay to entries received by multicast in seconds. "
        "The Service Discovery shall delay answers to entries that were transported in a multicast SOME/IP-SD message (e.g. FindService)."
    )
    SERVICE_OFFER_TIME_TO_LIVE_NOTE = "Defines the time in seconds the service offer is valid."

    def _config(self):
        return SomeipSdServerServiceInstanceConfig(MockParent(), "sd_server_config")

    def test_rehoused_to_spec_package(self):
        """Spec Package row = Fibex4Ethernet::ServiceInstances (Rule 0007) - rehoused from the ArObject.py stub."""
        module = inspect.getmodule(SomeipSdServerServiceInstanceConfig).__name__

        assert module == "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances"

    def test_inheritance(self):
        config = self._config()

        assert isinstance(config, ARElement)

    def test_top_level_export(self):
        import armodel

        assert armodel.SomeipSdServerServiceInstanceConfig is SomeipSdServerServiceInstanceConfig

    def test_init_parameter_annotations(self):
        annotations = typing.get_type_hints(SomeipSdServerServiceInstanceConfig.__init__)

        assert annotations["parent"] is ARObject
        assert annotations["short_name"] is str

    def test_member_annotations_match_getter_returns(self):
        hints = {
            "getInitialOfferBehavior": InitialSdDelayConfig,
            "getOfferCyclicDelay": TimeValue,
            "getPriority": PositiveInteger,
            "getRequestResponseDelay": RequestResponseDelay,
            "getServiceOfferTimeToLive": PositiveInteger,
        }
        for getter, expected in hints.items():
            assert typing.get_type_hints(getattr(SomeipSdServerServiceInstanceConfig, getter))["return"] == typing.Optional[expected]

    def test_initialization_defaults(self):
        config = self._config()

        assert config.getInitialOfferBehavior() is None
        assert config.getOfferCyclicDelay() is None
        assert config.getPriority() is None
        assert config.getRequestResponseDelay() is None
        assert config.getServiceOfferTimeToLive() is None

    def test_member_order(self):
        config = self._config()

        members = [k for k in vars(config) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_initial_offer_behavior(self):
        config = self._config()
        behavior = InitialSdDelayConfig()
        behavior.setInitialDelayMaxValue(TimeValue().setValue("0.1"))

        assert config.setInitialOfferBehavior(behavior) is config
        assert config.getInitialOfferBehavior() is behavior
        assert config.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1

        config.setInitialOfferBehavior(None)
        assert config.getInitialOfferBehavior() is behavior

    def test_get_set_offer_cyclic_delay(self):
        config = self._config()
        delay = TimeValue().setValue("2.0")

        assert config.setOfferCyclicDelay(delay) is config
        assert config.getOfferCyclicDelay() is delay
        assert config.getOfferCyclicDelay().getValue() == 2.0

        config.setOfferCyclicDelay(None)
        assert config.getOfferCyclicDelay() is delay

    def test_get_set_priority(self):
        config = self._config()
        priority = PositiveInteger().setValue("6")

        assert config.setPriority(priority) is config
        assert config.getPriority() is priority
        assert config.getPriority().getValue() == 6

        config.setPriority(None)
        assert config.getPriority() is priority

    def test_get_set_request_response_delay(self):
        config = self._config()
        delay = RequestResponseDelay()
        delay.setMinValue(TimeValue().setValue("0.05"))

        assert config.setRequestResponseDelay(delay) is config
        assert config.getRequestResponseDelay() is delay
        assert config.getRequestResponseDelay().getMinValue().getValue() == 0.05

        config.setRequestResponseDelay(None)
        assert config.getRequestResponseDelay() is delay

    def test_get_set_service_offer_time_to_live(self):
        config = self._config()
        ttl = PositiveInteger().setValue("30")

        assert config.setServiceOfferTimeToLive(ttl) is config
        assert config.getServiceOfferTimeToLive() is ttl
        assert config.getServiceOfferTimeToLive().getValue() == 30

        config.setServiceOfferTimeToLive(None)
        assert config.getServiceOfferTimeToLive() is ttl

    def test_class_docstring_note(self):
        expected = "Server specific settings that are relevant for the configuration of SOME/IP Service-Discovery. " "Tags: atp.recommendedPackage=SomeipSdTimingConfigs"
        assert inspect.cleandoc(SomeipSdServerServiceInstanceConfig.__doc__) == expected

    def test_notes_verbatim(self):
        accessors = {
            self.INITIAL_OFFER_BEHAVIOR_NOTE: ("getInitialOfferBehavior", "setInitialOfferBehavior", "initialOfferBehavior"),
            self.OFFER_CYCLIC_DELAY_NOTE: ("getOfferCyclicDelay", "setOfferCyclicDelay", "offerCyclicDelay"),
            self.PRIORITY_NOTE: ("getPriority", "setPriority", "priority"),
            self.REQUEST_RESPONSE_DELAY_NOTE: ("getRequestResponseDelay", "setRequestResponseDelay", "requestResponseDelay"),
            self.SERVICE_OFFER_TIME_TO_LIVE_NOTE: ("getServiceOfferTimeToLive", "setServiceOfferTimeToLive", "serviceOfferTimeToLive"),
        }
        for note, (getter, setter, field) in accessors.items():
            assert inspect.cleandoc(getattr(SomeipSdServerServiceInstanceConfig, getter).__doc__) == note
            setter_doc = inspect.cleandoc(getattr(SomeipSdServerServiceInstanceConfig, setter).__doc__)
            assert setter_doc.split("\nA None value")[0] == note
            assert ("A None value is a no-op and does not overwrite an existing %s." % field) in setter_doc
            assert note in inspect.getsource(SomeipSdServerServiceInstanceConfig.__init__)
