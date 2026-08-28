from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventComplex import (
    TDEventComplex,
)


class TestTDEventComplex:
    def test_construct(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventComplex(ar_root, "Complex1")
        assert event is not None
        assert event.short_name == "Complex1"

    def test_base_is_timing_description_event(self):
        assert issubclass(TDEventComplex, TimingDescriptionEvent)
