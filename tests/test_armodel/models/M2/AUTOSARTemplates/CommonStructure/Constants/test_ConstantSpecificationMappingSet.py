"""
This module contains tests for the ConstantSpecificationMappingSet class in the
AUTOSAR CommonStructure.Constants module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ConstantSpecificationMapping,
    ConstantSpecificationMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class TestConstantSpecificationMappingSet:
    """
    Test class for ConstantSpecificationMappingSet functionality.
    """

    def test_inheritance(self):
        obj = ConstantSpecificationMappingSet(None, "ConstantSpecificationMappingSet")
        assert isinstance(obj, ARElement)

    def test_initialization(self):
        obj = ConstantSpecificationMappingSet(None, "ConstantSpecificationMappingSet")
        assert isinstance(obj, ConstantSpecificationMappingSet)
        assert obj.getMappings() == []

    def test_add_and_get_mapping(self):
        obj = ConstantSpecificationMappingSet(None, "ConstantSpecificationMappingSet")
        mapping = ConstantSpecificationMapping()
        obj.addMapping(mapping)
        assert obj.getMappings() == [mapping]
        assert isinstance(obj.getMappings()[0], ConstantSpecificationMapping)

    def test_add_mapping_none_is_noop(self):
        obj = ConstantSpecificationMappingSet(None, "ConstantSpecificationMappingSet")
        obj.addMapping(None)
        assert obj.getMappings() == []

    def test_add_mapping_chaining(self):
        obj = ConstantSpecificationMappingSet(None, "ConstantSpecificationMappingSet")
        returned = obj.addMapping(ConstantSpecificationMapping())
        assert returned is obj
