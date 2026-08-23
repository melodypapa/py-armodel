from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    RuleBasedAxisCont,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class TestRuleBasedAxisCont:
    def test_inheritance(self):
        """Test that RuleBasedAxisCont inherits from ARObject"""
        spec = RuleBasedAxisCont()
        assert isinstance(spec, ARObject)

    def test_initialization(self):
        """Test RuleBasedAxisCont initialization defaults"""
        spec = RuleBasedAxisCont()
        assert spec is not None
        assert spec.category is None
        assert spec.ruleBasedValues is None
        assert spec.swArraysize is None
        assert spec.swAxisIndex is None
        assert spec.unitRef is None

    def test_get_category(self):
        """Test getCategory method"""
        spec = RuleBasedAxisCont()
        assert spec.getCategory() is None

    def test_set_category(self):
        """Test setCategory method"""
        spec = RuleBasedAxisCont()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        result = spec.setCategory(category)
        assert result is spec
        assert spec.getCategory() is category

    def test_set_category_none(self):
        """Test setCategory with None value is a no-op"""
        spec = RuleBasedAxisCont()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        spec.setCategory(category)
        result = spec.setCategory(None)
        assert result is spec
        assert spec.getCategory() is category

    def test_get_rule_based_values(self):
        """Test getRuleBasedValues method"""
        spec = RuleBasedAxisCont()
        assert spec.getRuleBasedValues() is None

    def test_set_rule_based_values(self):
        """Test setRuleBasedValues method"""
        spec = RuleBasedAxisCont()
        value = RuleBasedValueSpecification()
        result = spec.setRuleBasedValues(value)
        assert result is spec
        assert spec.getRuleBasedValues() is value

    def test_set_rule_based_values_none(self):
        """Test setRuleBasedValues with None value is a no-op"""
        spec = RuleBasedAxisCont()
        value = RuleBasedValueSpecification()
        spec.setRuleBasedValues(value)
        result = spec.setRuleBasedValues(None)
        assert result is spec
        assert spec.getRuleBasedValues() is value

    def test_get_sw_arraysize(self):
        """Test getSwArraysize method"""
        spec = RuleBasedAxisCont()
        assert spec.getSwArraysize() is None

    def test_set_sw_arraysize(self):
        """Test setSwArraysize method"""
        spec = RuleBasedAxisCont()
        value = ValueList()
        result = spec.setSwArraysize(value)
        assert result is spec
        assert spec.getSwArraysize() is value

    def test_set_sw_arraysize_none(self):
        """Test setSwArraysize with None value is a no-op"""
        spec = RuleBasedAxisCont()
        value = ValueList()
        spec.setSwArraysize(value)
        result = spec.setSwArraysize(None)
        assert result is spec
        assert spec.getSwArraysize() is value

    def test_get_sw_axis_index(self):
        """Test getSwAxisIndex method"""
        spec = RuleBasedAxisCont()
        assert spec.getSwAxisIndex() is None

    def test_set_sw_axis_index(self):
        """Test setSwAxisIndex method"""
        spec = RuleBasedAxisCont()
        index = AxisIndexType()
        index.setValue("1")
        result = spec.setSwAxisIndex(index)
        assert result is spec
        assert spec.getSwAxisIndex() is index

    def test_set_sw_axis_index_none(self):
        """Test setSwAxisIndex with None value is a no-op"""
        spec = RuleBasedAxisCont()
        index = AxisIndexType()
        index.setValue("1")
        spec.setSwAxisIndex(index)
        result = spec.setSwAxisIndex(None)
        assert result is spec
        assert spec.getSwAxisIndex() is index

    def test_get_unit_ref(self):
        """Test getUnitRef method"""
        spec = RuleBasedAxisCont()
        assert spec.getUnitRef() is None

    def test_set_unit_ref(self):
        """Test setUnitRef method"""
        spec = RuleBasedAxisCont()
        ref = RefType()
        ref.setValue("/Unit/SomeUnit")
        result = spec.setUnitRef(ref)
        assert result is spec
        assert spec.getUnitRef() is ref

    def test_set_unit_ref_none(self):
        """Test setUnitRef with None value is a no-op"""
        spec = RuleBasedAxisCont()
        ref = RefType()
        ref.setValue("/Unit/SomeUnit")
        spec.setUnitRef(ref)
        result = spec.setUnitRef(None)
        assert result is spec
        assert spec.getUnitRef() is ref
