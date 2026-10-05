from abc import ABC

import pytest

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwDescriptionEntity,
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwDescriptionEntity:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that HwDescriptionEntity abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="HwDescriptionEntity is an abstract class"):
            HwDescriptionEntity(None, "TestEntity")

        assert HwDescriptionEntity.__bases__ == (Referrable, ABC)

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

    def test_get_hw_attribute_values_default(self):
        """Test getHwAttributeValues returns the empty typed list by default"""
        entity = HwElement(None, "TestEntity")
        assert entity.getHwAttributeValues() == []
        assert entity.hwAttributeValues == []

    def test_get_hw_category_refs_default(self):
        """Test getHwCategoryRefs returns the empty typed list by default"""
        entity = HwElement(None, "TestEntity")
        assert entity.getHwCategoryRefs() == []
        assert entity.hwCategoryRefs == []

    def test_member_docstrings_verbatim(self):
        """Member docstrings must carry the Table 2.1 Notes verbatim (Rule 0001.4/0012)."""
        assert HwDescriptionEntity.__doc__ is not None, "Class docstring must contain spec Note"
        assert "This meta-class represents the ability to describe a hardware entity." in HwDescriptionEntity.__doc__, "Class docstring must contain spec Note verbatim"

        notes = {
            "addHwAttributeValue": "This aggregation represents a particular hardware attribute value.",
            "getHwAttributeValues": "This aggregation represents a particular hardware attribute value.",
            "addHwCategoryRef": "One of the associations representing one particular category of the hardware entity.",
            "getHwCategoryRefs": "One of the associations representing one particular category of the hardware entity.",
            "getHwTypeRef": "This association is used to assign an optional HwType which contains the common attribute values for all occurences of this HwDescriptionEntity. Note that Hw Types can not be redefined and therefore shall not have a hwType reference.",
            "setHwTypeRef": "This association is used to assign an optional HwType which contains the common attribute values for all occurences of this HwDescriptionEntity. Note that Hw Types can not be redefined and therefore shall not have a hwType reference.",
        }
        for method_name, note in notes.items():
            method = getattr(HwDescriptionEntity, method_name)
            assert method.__doc__ is not None, "%s must have a docstring" % method_name
            assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name

    def test_member_annotations(self):
        """get/set/add shall resolve to Optional[RefType] / List[HwAttributeValue] / HwDescriptionEntity (Rule 0003/0006 get_type_hints pin)."""
        import typing

        hints = typing.get_type_hints(HwDescriptionEntity.addHwAttributeValue)
        assert hints["value"] == typing.Optional[HwAttributeValue]
        assert hints["return"] is HwDescriptionEntity
        assert typing.get_type_hints(HwDescriptionEntity.getHwAttributeValues)["return"] == typing.List[HwAttributeValue]
        hints = typing.get_type_hints(HwDescriptionEntity.addHwCategoryRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is HwDescriptionEntity
        assert typing.get_type_hints(HwDescriptionEntity.getHwCategoryRefs)["return"] == typing.List[RefType]
        assert typing.get_type_hints(HwDescriptionEntity.getHwTypeRef)["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(HwDescriptionEntity.setHwTypeRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is HwDescriptionEntity
