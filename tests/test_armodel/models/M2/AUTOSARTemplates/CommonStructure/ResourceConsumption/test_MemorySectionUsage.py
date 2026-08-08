"""
This module contains tests for the MemorySectionUsage related classes in the
AUTOSAR CommonStructure.ResourceConsumption module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (
    MemorySection,
    SectionNamePrefix,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestMemorySection:
    """
    Test class for MemorySection functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(MemorySection, "MemorySection")
        assert obj.getShortName() == "MemorySection"


class TestSectionNamePrefix:
    """
    Test class for SectionNamePrefix functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(SectionNamePrefix, "SectionNamePrefix")
        assert obj.getShortName() == "SectionNamePrefix"
