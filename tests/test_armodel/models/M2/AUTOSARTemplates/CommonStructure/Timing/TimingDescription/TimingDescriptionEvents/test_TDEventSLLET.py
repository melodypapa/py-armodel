import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)


class _ConcreteTDEventSLLET(TDEventSLLET):
    pass


class TestTDEventSLLET:
    def test_abstract_instantiation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            TDEventSLLET(ar_root, "tdEventSLLET")
        assert str(err.value) == "TDEventSLLET is an abstract class."

    def test_base_is_timing_description_event(self):
        assert issubclass(TDEventSLLET, TimingDescriptionEvent)

    def test_construct_via_concrete_subclass(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = _ConcreteTDEventSLLET(ar_root, "SLLET1")
        assert event is not None
        assert event.short_name == "SLLET1"
