"""Model unit tests for SomeipSdClientEventGroupTimingConfig — Table 6.173, p.521 (R23-11).

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.173, p.521.
Base most-derived = ARElement; attributes requestResponseDelay (RequestResponseDelay,
0..1, aggr — non-Referrable child → set/get shape), subscribeEventgroupRetryDelay
(TimeValue), subscribeEventgroupRetryMax (PositiveInteger), timeToLive (PositiveInteger).
"""

import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    RequestResponseDelay,
    SomeipSdClientEventGroupTimingConfig,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestSomeipSdClientEventGroupTimingConfig:
    def test_inheritance(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        assert isinstance(config, ARElement)
        assert config.getShortName() == "Timing1"

    def test_initialization(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        assert config.getRequestResponseDelay() is None
        assert config.getSubscribeEventgroupRetryDelay() is None
        assert config.getSubscribeEventgroupRetryMax() is None
        assert config.getTimeToLive() is None

    def test_get_set_request_response_delay(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        delay = RequestResponseDelay()
        delay.setMinValue(TimeValue().setValue(2000))
        delay.setMaxValue(TimeValue().setValue(8000))

        result = config.setRequestResponseDelay(delay)
        assert result is config
        assert config.getRequestResponseDelay() is delay

    def test_get_set_subscribe_eventgroup_retry_delay(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        retry_delay = TimeValue().setValue(2.0)

        result = config.setSubscribeEventgroupRetryDelay(retry_delay)
        assert result is config
        assert config.getSubscribeEventgroupRetryDelay() is retry_delay

    def test_get_set_subscribe_eventgroup_retry_max(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        retry_max = PositiveInteger().setValue("255")

        result = config.setSubscribeEventgroupRetryMax(retry_max)
        assert result is config
        assert config.getSubscribeEventgroupRetryMax() is retry_max
        assert config.getSubscribeEventgroupRetryMax().getValue() == 255

    def test_get_set_time_to_live(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        ttl = PositiveInteger().setValue("10")

        result = config.setTimeToLive(ttl)
        assert result is config
        assert config.getTimeToLive() is ttl

    def test_setters_none_no_op(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        delay = RequestResponseDelay()
        retry_delay = TimeValue().setValue(2.0)
        retry_max = PositiveInteger().setValue("255")
        ttl = PositiveInteger().setValue("10")
        config.setRequestResponseDelay(delay)
        config.setSubscribeEventgroupRetryDelay(retry_delay)
        config.setSubscribeEventgroupRetryMax(retry_max)
        config.setTimeToLive(ttl)

        config.setRequestResponseDelay(None)
        config.setSubscribeEventgroupRetryDelay(None)
        config.setSubscribeEventgroupRetryMax(None)
        config.setTimeToLive(None)

        assert config.getRequestResponseDelay() is delay
        assert config.getSubscribeEventgroupRetryDelay() is retry_delay
        assert config.getSubscribeEventgroupRetryMax() is retry_max
        assert config.getTimeToLive() is ttl

    def test_type_annotations(self):
        config = SomeipSdClientEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        assert typing.get_type_hints(config.setRequestResponseDelay)["value"] == typing.Optional[RequestResponseDelay]
        assert typing.get_type_hints(config.setSubscribeEventgroupRetryDelay)["value"] == typing.Optional[TimeValue]
        assert typing.get_type_hints(config.setSubscribeEventgroupRetryMax)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(config.setTimeToLive)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(config.getRequestResponseDelay)["return"] == typing.Optional[RequestResponseDelay]
        assert typing.get_type_hints(config.getTimeToLive)["return"] == typing.Optional[PositiveInteger]

    def test_class_docstring_verbatim(self):
        assert SomeipSdClientEventGroupTimingConfig.__doc__ == (
            "This meta-class is used to specify configuration related to service discovery in the context of an event group on SOME/IP. Tags: atp.recommendedPackage=SomeipSdTimingConfigs"
        )
