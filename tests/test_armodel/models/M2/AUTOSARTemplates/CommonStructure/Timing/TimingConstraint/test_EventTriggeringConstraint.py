"""
This module contains tests for the EventTriggeringConstraint related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestPeriodicEventTriggering:
    """
    Test class for PeriodicEventTriggering functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(PeriodicEventTriggering, "Periodic")
        assert obj.getShortName() == "Periodic"


class TestSporadicEventTriggering:
    """
    Test class for SporadicEventTriggering functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(SporadicEventTriggering, "Sporadic")
        assert obj.getShortName() == "Sporadic"


class TestArbitraryEventTriggering:
    """
    Test class for ArbitraryEventTriggering functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(ArbitraryEventTriggering, "Arbitrary")
        assert obj.getShortName() == "Arbitrary"


class TestBurstPatternEventTriggering:
    """
    Test class for BurstPatternEventTriggering functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(BurstPatternEventTriggering, "Burst")
        assert obj.getShortName() == "Burst"


class TestConcretePatternEventTriggering:
    """
    Test class for ConcretePatternEventTriggering functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(ConcretePatternEventTriggering, "Concrete")
        assert obj.getShortName() == "Concrete"


class TestConfidenceInterval:
    """
    Test class for ConfidenceInterval functionality.
    """

    def test_instantiation(self):
        obj = ConfidenceInterval()
        assert isinstance(obj, ConfidenceInterval)
