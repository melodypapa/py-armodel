"""
This module contains tests for the BlueprintMappingSet class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintMapping module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMappingSet,
)


class TestBlueprintMappingSet:
    """
    Test class for BlueprintMappingSet functionality.
    """

    def test_initialization(self):
        obj = BlueprintMappingSet()
        assert isinstance(obj, BlueprintMappingSet)
