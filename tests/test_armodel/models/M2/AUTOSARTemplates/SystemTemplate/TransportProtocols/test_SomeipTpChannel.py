import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpChannel


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time_value(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _channel(short_name: str) -> SomeipTpChannel:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return SomeipTpChannel(package, short_name)


class Test_SomeipTpChannel:
    # Table 6.266, p.620 — class Note verbatim from the markdown (incl. the spec's own
    # "SomeipTp Channel" spacing); attribute Notes verbatim from the markdown
    NOTE_BURST_SIZE = "Specifies the number of segments that shall be transmitted in a burst ignoring separationTime. SeparationTime will then only be applied between bursts. If not configured, SeparationTime will be applied between all frames."
    NOTE_RX_TIMEOUT_TIME = "Timer to monitor the successful reception. It is started when the first NPdu is received, restarted after reception of intermediate NPdus, and is stopped when the last NPdu has been received."
    NOTE_SEPARATION_TIME = "Sets the duration of the minimum time in seconds the SOME/IP TP module shall wait between the transmissions of NPdus."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.266, p.620 — class Note verbatim from the markdown (no table constraints)
        assert cleandoc(SomeipTpChannel.__doc__) == "This element is used to assign properties to SomeipTpConnections that are referencing this SomeipTp Channel."

    def test_init_has_no_docstring(self):
        assert SomeipTpChannel.__init__.__doc__ is None

    def test_heritage(self):
        channel = _channel("Chan1")
        assert isinstance(channel, Identifiable)

    def test_initialization(self):
        channel = _channel("Chan1")
        assert channel.getBurstSize() is None
        assert channel.getRxTimeoutTime() is None
        assert channel.getSeparationTime() is None

    def test_get_set_burst_size(self):
        channel = _channel("Chan1")
        value = _positive_integer("8")
        assert channel.setBurstSize(value) is channel
        assert channel.getBurstSize() is value
        assert channel.getBurstSize().getValue() == 8
        channel.setBurstSize(None)
        assert channel.getBurstSize() is value

    def test_get_set_rx_timeout_time(self):
        channel = _channel("Chan1")
        value = _time_value("0.5")
        assert channel.setRxTimeoutTime(value) is channel
        assert channel.getRxTimeoutTime() is value
        channel.setRxTimeoutTime(None)
        assert channel.getRxTimeoutTime() is value

    def test_get_set_separation_time(self):
        channel = _channel("Chan1")
        value = _time_value("0.02")
        assert channel.setSeparationTime(value) is channel
        assert channel.getSeparationTime() is value
        channel.setSeparationTime(None)
        assert channel.getSeparationTime() is value

    def test_type_hints_pins(self):
        assert typing.get_type_hints(SomeipTpChannel.getBurstSize).get("return") == Optional[PositiveInteger]
        assert typing.get_type_hints(SomeipTpChannel.setBurstSize).get("value") == Optional[PositiveInteger]
        assert typing.get_type_hints(SomeipTpChannel.setBurstSize).get("return") is SomeipTpChannel
        assert typing.get_type_hints(SomeipTpChannel.getRxTimeoutTime).get("return") == Optional[TimeValue]
        assert typing.get_type_hints(SomeipTpChannel.setRxTimeoutTime).get("value") == Optional[TimeValue]
        assert typing.get_type_hints(SomeipTpChannel.setRxTimeoutTime).get("return") is SomeipTpChannel
        assert typing.get_type_hints(SomeipTpChannel.getSeparationTime).get("return") == Optional[TimeValue]
        assert typing.get_type_hints(SomeipTpChannel.setSeparationTime).get("value") == Optional[TimeValue]
        assert typing.get_type_hints(SomeipTpChannel.setSeparationTime).get("return") is SomeipTpChannel

    def test_not_variation_point_capable(self):
        # XSD complexType SOMEIP-TP-CHANNEL group chain carries no VARIATION-POINT element
        assert not hasattr(SomeipTpChannel, "getVariationPoint")
