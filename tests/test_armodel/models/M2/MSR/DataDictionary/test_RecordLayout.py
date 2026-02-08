"""
This module contains tests for the RecordLayout module in MSR.DataDictionary.
"""
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARNumerical,
    Integer,
    RefType,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import *
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)


class TestSwRecordLayoutV:
    """Test class for SwRecordLayoutV class."""

    def test_sw_record_layout_v_initialization(self):
        """Test that a SwRecordLayoutV object can be initialized with default values."""
        sw_record_layout_v = SwRecordLayoutV()
        assert sw_record_layout_v.baseTypeRef is None
        assert sw_record_layout_v.desc is None
        assert sw_record_layout_v.shortLabel is None
        assert sw_record_layout_v.swGenericAxisParamTypeRef is None
        assert sw_record_layout_v.swRecordLayoutVAxis is None
        assert sw_record_layout_v.swRecordLayoutVFixValue is None
        assert sw_record_layout_v.swRecordLayoutVIndex is None
        assert sw_record_layout_v.swRecordLayoutVProp is None

    def test_sw_record_layout_v_base_type_ref_methods(self):
        """Test the baseTypeRef getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        ref = RefType()

        result = sw_record_layout_v.setBaseTypeRef(ref)
        assert sw_record_layout_v.getBaseTypeRef() == ref
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_desc_methods(self):
        """Test the desc getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        desc = MultiLanguageOverviewParagraph()

        result = sw_record_layout_v.setDesc(desc)
        assert sw_record_layout_v.getDesc() == desc
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_short_label_methods(self):
        """Test the shortLabel getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        label = ARLiteral()

        result = sw_record_layout_v.setShortLabel(label)
        assert sw_record_layout_v.getShortLabel() == label
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_sw_generic_axis_param_type_ref_methods(self):
        """Test the swGenericAxisParamTypeRef getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        ref = RefType()

        result = sw_record_layout_v.setSwGenericAxisParamTypeRef(ref)
        assert sw_record_layout_v.getSwGenericAxisParamTypeRef() == ref
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_sw_record_layout_v_axis_methods(self):
        """Test the swRecordLayoutVAxis getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        axis = ARNumerical()

        result = sw_record_layout_v.setSwRecordLayoutVAxis(axis)
        assert sw_record_layout_v.getSwRecordLayoutVAxis() == axis
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_sw_record_layout_v_fix_value_methods(self):
        """Test the swRecordLayoutVFixValue getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        fix_value = ARNumerical()

        result = sw_record_layout_v.setSwRecordLayoutVFixValue(fix_value)
        assert sw_record_layout_v.getSwRecordLayoutVFixValue() == fix_value
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_sw_record_layout_v_index_methods(self):
        """Test the swRecordLayoutVIndex getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        index = ARLiteral()

        result = sw_record_layout_v.setSwRecordLayoutVIndex(index)
        assert sw_record_layout_v.getSwRecordLayoutVIndex() == index
        assert result == sw_record_layout_v

    def test_sw_record_layout_v_sw_record_layout_v_prop_methods(self):
        """Test the swRecordLayoutVProp getter and setter."""
        sw_record_layout_v = SwRecordLayoutV()
        prop = ARLiteral()

        result = sw_record_layout_v.setSwRecordLayoutVProp(prop)
        assert sw_record_layout_v.getSwRecordLayoutVProp() == prop
        assert result == sw_record_layout_v


class TestSwRecordLayoutGroupContent:
    """Test class for SwRecordLayoutGroupContent class."""

    def test_sw_record_layout_group_content_initialization(self):
        """Test that a SwRecordLayoutGroupContent object can be initialized with default values."""
        sw_record_layout_group_content = SwRecordLayoutGroupContent()
        assert sw_record_layout_group_content.swRecordLayoutRef is None
        assert sw_record_layout_group_content.swRecordLayoutGroup is None
        assert sw_record_layout_group_content.swRecordLayoutV is None

    def test_sw_record_layout_group_content_sw_record_layout_ref_methods(self):
        """Test the swRecordLayoutRef getter and setter."""
        sw_record_layout_group_content = SwRecordLayoutGroupContent()
        ref = RefType()

        result = sw_record_layout_group_content.setSwRecordLayoutRef(ref)
        assert sw_record_layout_group_content.getSwRecordLayoutRef() == ref
        assert result == sw_record_layout_group_content

    def test_sw_record_layout_group_content_sw_record_layout_group_methods(self):
        """Test the swRecordLayoutGroup getter and setter."""
        sw_record_layout_group_content = SwRecordLayoutGroupContent()
        group = SwRecordLayoutGroup()

        result = sw_record_layout_group_content.setSwRecordLayoutGroup(group)
        assert sw_record_layout_group_content.getSwRecordLayoutGroup() == group
        assert result == sw_record_layout_group_content

    def test_sw_record_layout_group_content_sw_record_layout_v_methods(self):
        """Test the swRecordLayoutV getter and setter."""
        sw_record_layout_group_content = SwRecordLayoutGroupContent()
        layout_v = SwRecordLayoutV()

        result = sw_record_layout_group_content.setSwRecordLayoutV(layout_v)
        assert sw_record_layout_group_content.getSwRecordLayoutV() == layout_v
        assert result == sw_record_layout_group_content


class TestSwRecordLayoutGroup:
    """Test class for SwRecordLayoutGroup class."""

    def test_sw_record_layout_group_initialization(self):
        """Test that a SwRecordLayoutGroup object can be initialized with default values."""
        sw_record_layout_group = SwRecordLayoutGroup()
        assert sw_record_layout_group.category is None
        assert sw_record_layout_group.desc is None
        assert sw_record_layout_group.shortLabel is None
        assert sw_record_layout_group.swGenericAxisParamTypeRef is None
        assert sw_record_layout_group.swRecordLayoutComponent is None
        assert sw_record_layout_group.swRecordLayoutGroupAxis is None
        assert sw_record_layout_group.swRecordLayoutGroupContentType is None
        assert sw_record_layout_group.swRecordLayoutGroupFrom is None
        assert sw_record_layout_group.swRecordLayoutGroupIndex is None
        assert sw_record_layout_group.swRecordLayoutGroupStep is None
        assert sw_record_layout_group.swRecordLayoutGroupTo is None

    def test_sw_record_layout_group_category_methods(self):
        """Test the category getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        category = ARLiteral()

        result = sw_record_layout_group.setCategory(category)
        assert sw_record_layout_group.getCategory() == category
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_desc_methods(self):
        """Test the desc getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        desc = MultiLanguageOverviewParagraph()

        result = sw_record_layout_group.setDesc(desc)
        assert sw_record_layout_group.getDesc() == desc
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_short_label_methods(self):
        """Test the shortLabel getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        label = ARLiteral()

        result = sw_record_layout_group.setShortLabel(label)
        assert sw_record_layout_group.getShortLabel() == label
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_generic_axis_param_type_ref_methods(self):
        """Test the swGenericAxisParamTypeRef getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        ref = RefType()

        result = sw_record_layout_group.setSwGenericAxisParamTypeRef(ref)
        assert sw_record_layout_group.getSwGenericAxisParamTypeRef() == ref
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_component_methods(self):
        """Test the swRecordLayoutComponent getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        component = ARLiteral()

        result = sw_record_layout_group.setSwRecordLayoutComponent(component)
        assert sw_record_layout_group.getSwRecordLayoutComponent() == component
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_axis_methods(self):
        """Test the swRecordLayoutGroupAxis getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        axis = Integer()

        result = sw_record_layout_group.setSwRecordLayoutGroupAxis(axis)
        assert sw_record_layout_group.getSwRecordLayoutGroupAxis() == axis
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_content_type_methods(self):
        """Test the swRecordLayoutGroupContentType getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        content_type = SwRecordLayoutGroupContent()

        result = sw_record_layout_group.setSwRecordLayoutGroupContentType(content_type)
        assert sw_record_layout_group.getSwRecordLayoutGroupContentType() == content_type
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_from_methods(self):
        """Test the swRecordLayoutGroupFrom getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        from_val = ARLiteral()

        result = sw_record_layout_group.setSwRecordLayoutGroupFrom(from_val)
        assert sw_record_layout_group.getSwRecordLayoutGroupFrom() == from_val
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_index_methods(self):
        """Test the swRecordLayoutGroupIndex getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        index = ARLiteral()

        result = sw_record_layout_group.setSwRecordLayoutGroupIndex(index)
        assert sw_record_layout_group.getSwRecordLayoutGroupIndex() == index
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_step_methods(self):
        """Test the swRecordLayoutGroupStep getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        step = Integer()

        result = sw_record_layout_group.setSwRecordLayoutGroupStep(step)
        assert sw_record_layout_group.getSwRecordLayoutGroupStep() == step
        assert result == sw_record_layout_group

    def test_sw_record_layout_group_sw_record_layout_group_to_methods(self):
        """Test the swRecordLayoutGroupTo getter and setter."""
        sw_record_layout_group = SwRecordLayoutGroup()
        to_val = ARLiteral()

        result = sw_record_layout_group.setSwRecordLayoutGroupTo(to_val)
        assert sw_record_layout_group.getSwRecordLayoutGroupTo() == to_val
        assert result == sw_record_layout_group


class TestSwRecordLayout:
    """Test class for SwRecordLayout class."""

    def test_sw_record_layout_initialization(self):
        """Test that a SwRecordLayout object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_record_layout = SwRecordLayout(parent_obj, "test_name")
        assert sw_record_layout.swRecordLayoutGroup is None

    def test_sw_record_layout_group_methods(self):
        """Test the swRecordLayoutGroup getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_record_layout = SwRecordLayout(parent_obj, "test_name")
        group = SwRecordLayoutGroup()

        result = sw_record_layout.setSwRecordLayoutGroup(group)
        assert sw_record_layout.getSwRecordLayoutGroup() == group
        assert result == sw_record_layout
