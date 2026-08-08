"""
This module contains tests for the StackUsage related classes in the
AUTOSAR CommonStructure.ResourceConsumption module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    MeasuredStackUsage,
    RoughEstimateStackUsage,
    WorstCaseStackUsage,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestMeasuredStackUsage:
    """
    Test class for MeasuredStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(MeasuredStackUsage, "MeasuredStack")
        assert obj.getShortName() == "MeasuredStack"


class TestRoughEstimateStackUsage:
    """
    Test class for RoughEstimateStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(RoughEstimateStackUsage, "RoughStack")
        assert obj.getShortName() == "RoughStack"


class TestWorstCaseStackUsage:
    """
    Test class for WorstCaseStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(WorstCaseStackUsage, "WorstStack")
        assert obj.getShortName() == "WorstStack"
