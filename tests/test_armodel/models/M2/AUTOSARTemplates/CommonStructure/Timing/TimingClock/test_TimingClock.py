import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ConcreteTimingClock(TimingClock):
    pass


class TestTimingClock:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_class_cannot_be_instantiated(self):
        parent = self._parent()
        with pytest.raises(TypeError, match="TimingClock is an abstract class"):
            TimingClock(parent, "Clock")

    def test_base_is_identifiable(self):
        assert issubclass(TimingClock, Identifiable)

    def test_initialization_defaults(self):
        clock = ConcreteTimingClock(self._parent(), "Clock1")
        assert clock.getShortName() == "Clock1"
        assert clock.getPlatformTimeBaseRef() is None

    def test_get_set_platform_time_base_ref(self):
        clock = ConcreteTimingClock(self._parent(), "Clock1")
        ref = RefType().setValue("/AUTOSAR/GlobalTimeDomain").setDest("GLOBAL-TIME-DOMAIN")
        assert clock.setPlatformTimeBaseRef(ref) is clock
        assert clock.getPlatformTimeBaseRef() is ref
        assert clock.getPlatformTimeBaseRef().getValue() == "/AUTOSAR/GlobalTimeDomain"
        assert clock.getPlatformTimeBaseRef().getDest() == "GLOBAL-TIME-DOMAIN"

    def test_set_platform_time_base_ref_none_is_no_op(self):
        clock = ConcreteTimingClock(self._parent(), "Clock1")
        ref = RefType().setValue("/AUTOSAR/GlobalTimeDomain").setDest("GLOBAL-TIME-DOMAIN")
        clock.setPlatformTimeBaseRef(ref)
        clock.setPlatformTimeBaseRef(None)
        assert clock.getPlatformTimeBaseRef() is ref
