"""Model tests for the EventTriggeringConstraint family (Tables 3.59-3.64)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    EventTriggeringConstraint,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Float,
    Integer,
    PositiveInteger,
    RefType,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


def _mdt(factor: str = "50") -> MultidimensionalTime:
    mdt = MultidimensionalTime()
    mdt.setCseCode(CseCodeType().setValue("0"))
    mdt.setCseCodeFactor(Integer().setValue(factor))
    return mdt


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class _ConcreteEventTriggering(EventTriggeringConstraint):
    pass


class TestEventTriggeringConstraint:
    def test_abstract_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            EventTriggeringConstraint(AUTOSAR.getInstance(), "Evt")

    def test_initialization(self):
        obj = _ConcreteEventTriggering(AUTOSAR.getInstance(), "Evt")
        assert obj.getShortName() == "Evt"
        assert obj.getEventRef() is None

    def test_get_set_event_ref(self):
        obj = _ConcreteEventTriggering(AUTOSAR.getInstance(), "Evt")
        ref = RefType().setValue("/AUTOSAR/TdEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert obj.setEventRef(ref) is obj
        assert obj.getEventRef() is ref
        assert obj.getEventRef().getValue() == "/AUTOSAR/TdEvent"
        assert obj.setEventRef(None) is obj
        assert obj.getEventRef() is ref


class TestPeriodicEventTriggering:
    def test_instantiation(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        assert isinstance(obj, EventTriggeringConstraint)
        assert obj.getShortName() == "Periodic"

    def test_initialization(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        assert obj.getJitter() is None
        assert obj.getMinimumInterArrivalTime() is None
        assert obj.getPeriod() is None

    def test_get_set_jitter(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        value = _mdt("20")
        assert obj.setJitter(value) is obj
        assert obj.getJitter() is value
        assert obj.getJitter().getCseCodeFactor().getValue() == 20
        assert obj.setJitter(None) is obj
        assert obj.getJitter() is value

    def test_get_set_minimum_inter_arrival_time(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        value = _mdt("10")
        assert obj.setMinimumInterArrivalTime(value) is obj
        assert obj.getMinimumInterArrivalTime() is value
        assert obj.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert obj.setMinimumInterArrivalTime(None) is obj
        assert obj.getMinimumInterArrivalTime() is value

    def test_get_set_period(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        value = _mdt("30")
        assert obj.setPeriod(value) is obj
        assert obj.getPeriod() is value
        assert obj.getPeriod().getCseCodeFactor().getValue() == 30
        assert obj.setPeriod(None) is obj
        assert obj.getPeriod() is value

    def test_base_properties(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        ref = RefType().setValue("/AUTOSAR/TdEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert obj.setEventRef(ref) is obj
        assert obj.getEventRef() is ref
        condition_ref = RefType().setValue("/AUTOSAR/Cond").setDest("TIMING-CONDITION")
        assert obj.setTimingConditionRef(condition_ref) is obj
        assert obj.getTimingConditionRef() is condition_ref
        assert obj.setEventRef(None) is obj
        assert obj.getEventRef() is ref
        assert obj.setTimingConditionRef(None) is obj
        assert obj.getTimingConditionRef() is condition_ref


class TestSporadicEventTriggering:
    def test_instantiation(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        assert isinstance(obj, EventTriggeringConstraint)
        assert obj.getShortName() == "Sporadic"

    def test_initialization(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        assert obj.getJitter() is None
        assert obj.getMaximumInterArrivalTime() is None
        assert obj.getMinimumInterArrivalTime() is None
        assert obj.getPeriod() is None

    def test_get_set_jitter(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        value = _mdt("30")
        assert obj.setJitter(value) is obj
        assert obj.getJitter() is value
        assert obj.getJitter().getCseCodeFactor().getValue() == 30
        assert obj.setJitter(None) is obj
        assert obj.getJitter() is value

    def test_get_set_maximum_inter_arrival_time(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        value = _mdt("20")
        assert obj.setMaximumInterArrivalTime(value) is obj
        assert obj.getMaximumInterArrivalTime() is value
        assert obj.getMaximumInterArrivalTime().getCseCodeFactor().getValue() == 20
        assert obj.setMaximumInterArrivalTime(None) is obj
        assert obj.getMaximumInterArrivalTime() is value

    def test_get_set_minimum_inter_arrival_time(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        value = _mdt("10")
        assert obj.setMinimumInterArrivalTime(value) is obj
        assert obj.getMinimumInterArrivalTime() is value
        assert obj.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 10
        assert obj.setMinimumInterArrivalTime(None) is obj
        assert obj.getMinimumInterArrivalTime() is value

    def test_get_set_period(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        value = _mdt("40")
        assert obj.setPeriod(value) is obj
        assert obj.getPeriod() is value
        assert obj.getPeriod().getCseCodeFactor().getValue() == 40
        assert obj.setPeriod(None) is obj
        assert obj.getPeriod() is value


class TestConcretePatternEventTriggering:
    def test_instantiation(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        assert isinstance(obj, EventTriggeringConstraint)
        assert obj.getShortName() == "Concrete"

    def test_initialization(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        assert obj.getOffsets() == []
        assert obj.getPatternJitter() is None
        assert obj.getPatternLength() is None
        assert obj.getPatternPeriod() is None

    def test_add_offset(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        offset1 = _mdt("5")
        offset2 = _mdt("15")
        assert obj.addOffset(offset1) is obj
        assert obj.addOffset(offset2) is obj
        offsets = obj.getOffsets()
        assert offsets[0] is offset1
        assert offsets[1] is offset2
        assert obj.addOffset(None) is obj
        assert len(obj.getOffsets()) == 2

    def test_get_set_pattern_jitter(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        value = _mdt("2")
        assert obj.setPatternJitter(value) is obj
        assert obj.getPatternJitter() is value
        assert obj.getPatternJitter().getCseCodeFactor().getValue() == 2
        assert obj.setPatternJitter(None) is obj
        assert obj.getPatternJitter() is value

    def test_get_set_pattern_length(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        value = _mdt("100")
        assert obj.setPatternLength(value) is obj
        assert obj.getPatternLength() is value
        assert obj.getPatternLength().getCseCodeFactor().getValue() == 100
        assert obj.setPatternLength(None) is obj
        assert obj.getPatternLength() is value

    def test_get_set_pattern_period(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        value = _mdt("200")
        assert obj.setPatternPeriod(value) is obj
        assert obj.getPatternPeriod() is value
        assert obj.getPatternPeriod().getCseCodeFactor().getValue() == 200
        assert obj.setPatternPeriod(None) is obj
        assert obj.getPatternPeriod() is value


class TestBurstPatternEventTriggering:
    def test_instantiation(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        assert isinstance(obj, EventTriggeringConstraint)
        assert obj.getShortName() == "Burst"

    def test_initialization(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        assert obj.getMaxNumberOfOccurrences() is None
        assert obj.getMinimumInterArrivalTime() is None
        assert obj.getMinNumberOfOccurrences() is None
        assert obj.getPatternJitter() is None
        assert obj.getPatternLength() is None
        assert obj.getPatternPeriod() is None

    def test_get_set_max_number_of_occurrences(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = PositiveInteger().setValue("10")
        assert obj.setMaxNumberOfOccurrences(value) is obj
        assert obj.getMaxNumberOfOccurrences() is value
        assert obj.getMaxNumberOfOccurrences().getValue() == 10
        assert obj.setMaxNumberOfOccurrences(None) is obj
        assert obj.getMaxNumberOfOccurrences() is value

    def test_get_set_minimum_inter_arrival_time(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = _mdt("5")
        assert obj.setMinimumInterArrivalTime(value) is obj
        assert obj.getMinimumInterArrivalTime() is value
        assert obj.getMinimumInterArrivalTime().getCseCodeFactor().getValue() == 5
        assert obj.setMinimumInterArrivalTime(None) is obj
        assert obj.getMinimumInterArrivalTime() is value

    def test_get_set_min_number_of_occurrences(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = PositiveInteger().setValue("3")
        assert obj.setMinNumberOfOccurrences(value) is obj
        assert obj.getMinNumberOfOccurrences() is value
        assert obj.getMinNumberOfOccurrences().getValue() == 3
        assert obj.setMinNumberOfOccurrences(None) is obj
        assert obj.getMinNumberOfOccurrences() is value

    def test_get_set_pattern_jitter(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = _mdt("1")
        assert obj.setPatternJitter(value) is obj
        assert obj.getPatternJitter() is value
        assert obj.getPatternJitter().getCseCodeFactor().getValue() == 1
        assert obj.setPatternJitter(None) is obj
        assert obj.getPatternJitter() is value

    def test_get_set_pattern_length(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = _mdt("50")
        assert obj.setPatternLength(value) is obj
        assert obj.getPatternLength() is value
        assert obj.getPatternLength().getCseCodeFactor().getValue() == 50
        assert obj.setPatternLength(None) is obj
        assert obj.getPatternLength() is value

    def test_get_set_pattern_period(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        value = _mdt("80")
        assert obj.setPatternPeriod(value) is obj
        assert obj.getPatternPeriod() is value
        assert obj.getPatternPeriod().getCseCodeFactor().getValue() == 80
        assert obj.setPatternPeriod(None) is obj
        assert obj.getPatternPeriod() is value


class TestArbitraryEventTriggering:
    def test_instantiation(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        assert isinstance(obj, EventTriggeringConstraint)
        assert obj.getShortName() == "Arbitrary"

    def test_initialization(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        assert obj.getConfidenceIntervals() == []
        assert obj.getMaximumDistances() == []
        assert obj.getMinimumDistances() == []

    def test_add_confidence_interval(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        interval1 = ConfidenceInterval()
        interval1.setLowerBound(_mdt("10"))
        interval1.setPropability(Float().setValue("0.95"))
        interval1.setUpperBound(_mdt("100"))
        interval2 = ConfidenceInterval()
        interval2.setUpperBound(_mdt("200"))
        assert obj.addConfidenceInterval(interval1) is obj
        assert obj.addConfidenceInterval(interval2) is obj
        intervals = obj.getConfidenceIntervals()
        assert intervals[0] is interval1
        assert intervals[0].getLowerBound().getCseCodeFactor().getValue() == 10
        assert intervals[0].getPropability().getValue() == 0.95
        assert intervals[0].getUpperBound().getCseCodeFactor().getValue() == 100
        assert intervals[1] is interval2
        assert obj.addConfidenceInterval(None) is obj
        assert len(obj.getConfidenceIntervals()) == 2

    def test_add_maximum_distance(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        distance1 = _mdt("20")
        distance2 = _mdt("40")
        assert obj.addMaximumDistance(distance1) is obj
        assert obj.addMaximumDistance(distance2) is obj
        distances = obj.getMaximumDistances()
        assert distances[0] is distance1
        assert distances[1] is distance2
        assert obj.addMaximumDistance(None) is obj
        assert len(obj.getMaximumDistances()) == 2

    def test_add_minimum_distance(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        distance1 = _mdt("10")
        distance2 = _mdt("30")
        assert obj.addMinimumDistance(distance1) is obj
        assert obj.addMinimumDistance(distance2) is obj
        distances = obj.getMinimumDistances()
        assert distances[0] is distance1
        assert distances[1] is distance2
        assert obj.addMinimumDistance(None) is obj
        assert len(obj.getMinimumDistances()) == 2
