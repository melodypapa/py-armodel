"""
This module contains tests for the BlueprintGenerator class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintGenerator module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import (
    BlueprintGenerator,
)


class TestBlueprintGenerator:
    """
    Test class for BlueprintGenerator functionality.
    """

    def test_set_get_generator_name(self):
        obj = BlueprintGenerator()
        assert obj.setGeneratorName("gen") is obj
        assert obj.getGeneratorName() == "gen"
