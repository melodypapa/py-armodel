"""Model unit tests for SomeipSdServerEventGroupTimingConfig — Table 6.172, p.517 (R23-11).

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.172, p.517.
Base most-derived = ARElement; single attribute requestResponseDelay
(RequestResponseDelay, 0..1, aggr — non-Referrable child → set/get shape).
"""

import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    RequestResponseDelay,
    SomeipSdServerEventGroupTimingConfig,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestSomeipSdServerEventGroupTimingConfig:
    def test_inheritance(self):
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        assert isinstance(config, ARElement)
        assert config.getShortName() == "Timing1"

    def test_initialization(self):
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        assert config.getRequestResponseDelay() is None

    def test_get_set_request_response_delay(self):
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        delay = RequestResponseDelay()
        delay.setMinValue(TimeValue().setValue(2000))
        delay.setMaxValue(TimeValue().setValue(8000))

        result = config.setRequestResponseDelay(delay)
        assert result is config
        assert config.getRequestResponseDelay() is delay

    def test_set_request_response_delay_none_no_op(self):
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        delay = RequestResponseDelay()
        config.setRequestResponseDelay(delay)
        config.setRequestResponseDelay(None)
        assert config.getRequestResponseDelay() is delay

    def test_type_annotations(self):
        config = SomeipSdServerEventGroupTimingConfig(AUTOSAR.getInstance(), "Timing1")
        hints = typing.get_type_hints(config.setRequestResponseDelay)
        assert hints["return"] is SomeipSdServerEventGroupTimingConfig
        assert hints["value"] == typing.Optional[RequestResponseDelay]
        assert typing.get_type_hints(config.getRequestResponseDelay)["return"] == typing.Optional[RequestResponseDelay]

    def test_class_docstring_verbatim(self):
        assert SomeipSdServerEventGroupTimingConfig.__doc__ == ("EventGroup specific timing configuration settings. Tags: atp.recommendedPackage=SomeipSdTimingConfigs")
