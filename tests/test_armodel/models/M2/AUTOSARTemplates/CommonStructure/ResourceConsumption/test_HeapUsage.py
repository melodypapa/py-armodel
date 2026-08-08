"""
This module contains tests for the HeapUsage related classes in the
AUTOSAR CommonStructure.ResourceConsumption module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import (
    MeasuredHeapUsage,
    RoughEstimateHeapUsage,
    WorstCaseHeapUsage,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestMeasuredHeapUsage:
    """
    Test class for MeasuredHeapUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(MeasuredHeapUsage, "MeasuredHeap")
        assert obj.getShortName() == "MeasuredHeap"


class TestRoughEstimateHeapUsage:
    """
    Test class for RoughEstimateHeapUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(RoughEstimateHeapUsage, "RoughHeap")
        assert obj.getShortName() == "RoughHeap"


class TestWorstCaseHeapUsage:
    """
    Test class for WorstCaseHeapUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(WorstCaseHeapUsage, "WorstHeap")
        assert obj.getShortName() == "WorstHeap"
