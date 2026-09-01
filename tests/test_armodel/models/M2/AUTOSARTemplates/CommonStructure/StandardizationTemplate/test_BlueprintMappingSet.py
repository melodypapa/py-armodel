"""
This module contains tests for the BlueprintMappingSet class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintMapping module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
    BlueprintMappingSet,
)


class TestBlueprintMappingSet:
    """
    Test class for BlueprintMappingSet functionality.
    """

    def test_initialization(self):
        obj = BlueprintMappingSet(None, "BlueprintMappingSet")
        assert isinstance(obj, BlueprintMappingSet)
        assert obj.getBlueprintMaps() == []

    def test_add_and_get_blueprint_map(self):
        obj = BlueprintMappingSet(None, "BlueprintMappingSet")
        mapping = BlueprintMapping()
        obj.addBlueprintMap(mapping)
        assert obj.getBlueprintMaps() == [mapping]
        assert isinstance(obj.getBlueprintMaps()[0], AtpBlueprintMapping)

    def test_add_blueprint_map_none_is_noop(self):
        obj = BlueprintMappingSet(None, "BlueprintMappingSet")
        obj.addBlueprintMap(None)
        assert obj.getBlueprintMaps() == []

    def test_add_blueprint_map_chaining(self):
        obj = BlueprintMappingSet(None, "BlueprintMappingSet")
        returned = obj.addBlueprintMap(BlueprintMapping())
        assert returned is obj

    def test_blueprint_mapping_is_concrete(self):
        mapping = BlueprintMapping()
        assert isinstance(mapping, AtpBlueprintMapping)
