"""
This module contains tests for the FMFeatureDecomposition class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMFeatureDecomposition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, PositiveInteger, RefType


class TestFMFeatureDecomposition:
    """
    Test class for FMFeatureDecomposition functionality.
    """

    def test_initialization(self):
        obj = FMFeatureDecomposition()
        assert isinstance(obj, FMFeatureDecomposition)
        assert obj.getCategory() is None
        assert obj.getFeatureRefs() == []
        assert obj.getMax() is None
        assert obj.getMin() is None

    def test_get_set_category(self):
        obj = FMFeatureDecomposition()
        category = CategoryString()
        category.setValue("MANDATORYFEATURE")
        assert obj.setCategory(category) is obj
        assert obj.getCategory() is category

    def test_set_category_none_noop(self):
        obj = FMFeatureDecomposition()
        category = CategoryString()
        category.setValue("MANDATORYFEATURE")
        obj.setCategory(category)
        assert obj.setCategory(None) is obj
        assert obj.getCategory() is category

    def test_add_get_feature_refs(self):
        obj = FMFeatureDecomposition()
        ref = RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE")
        assert obj.addFeatureRef(ref) is obj
        assert obj.getFeatureRefs() == [ref]

    def test_get_set_max(self):
        obj = FMFeatureDecomposition()
        max_value = PositiveInteger()
        max_value.setValue(5)
        assert obj.setMax(max_value) is obj
        assert obj.getMax() is max_value

    def test_set_max_none_noop(self):
        obj = FMFeatureDecomposition()
        max_value = PositiveInteger()
        max_value.setValue(5)
        obj.setMax(max_value)
        assert obj.setMax(None) is obj
        assert obj.getMax() is max_value

    def test_get_set_min(self):
        obj = FMFeatureDecomposition()
        min_value = PositiveInteger()
        min_value.setValue(2)
        assert obj.setMin(min_value) is obj
        assert obj.getMin() is min_value

    def test_set_min_none_noop(self):
        obj = FMFeatureDecomposition()
        min_value = PositiveInteger()
        min_value.setValue(2)
        obj.setMin(min_value)
        assert obj.setMin(None) is obj
        assert obj.getMin() is min_value
