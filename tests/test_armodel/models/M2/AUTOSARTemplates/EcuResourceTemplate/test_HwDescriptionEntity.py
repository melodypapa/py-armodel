import pytest

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwDescriptionEntity,
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwDescriptionEntity:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that HwDescriptionEntity abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="HwDescriptionEntity is an abstract class"):
            HwDescriptionEntity(None, "TestEntity")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of HwDescriptionEntity can be instantiated"""
        element = HwElement(None, "TestElement")
        assert element is not None
        assert element.getShortName() == "TestElement"
        assert element.getHwAttributeValues() == []
        assert element.getHwCategoryRefs() == []
        assert element.getHwTypeRef() is None

    def test_add_hw_attribute_value(self):
        """Test addHwAttributeValue method"""
        entity = HwElement(None, "TestEntity")
        value = HwAttributeValue()
        result = entity.addHwAttributeValue(value)
        assert result is entity
        assert entity.getHwAttributeValues() == [value]

    def test_add_hw_attribute_value_none(self):
        """Test addHwAttributeValue with None value"""
        entity = HwElement(None, "TestEntity")
        result = entity.addHwAttributeValue(None)
        assert result is entity
        assert entity.getHwAttributeValues() == []

    def test_add_hw_category_ref(self):
        """Test addHwCategoryRef method"""
        entity = HwElement(None, "TestEntity")
        ref = RefType()
        result = entity.addHwCategoryRef(ref)
        assert result is entity
        assert entity.getHwCategoryRefs() == [ref]

    def test_add_hw_category_ref_none(self):
        """Test addHwCategoryRef with None value"""
        entity = HwElement(None, "TestEntity")
        result = entity.addHwCategoryRef(None)
        assert result is entity
        assert entity.getHwCategoryRefs() == []

    def test_set_hw_type_ref(self):
        """Test setHwTypeRef method"""
        entity = HwElement(None, "TestEntity")
        ref = RefType()
        result = entity.setHwTypeRef(ref)
        assert result is entity
        assert entity.getHwTypeRef() == ref

    def test_set_hw_type_ref_none(self):
        """Test setHwTypeRef with None value"""
        entity = HwElement(None, "TestEntity")
        result = entity.setHwTypeRef(None)
        assert result is entity
        assert entity.getHwTypeRef() is None
