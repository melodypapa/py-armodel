"""
This module contains tests for the CalibrationParameter module in MSR.DataDictionary.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DisplayFormatString, Float, MonotonyEnum
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
    SwCalprmAxis,
    SwCalprmAxisSet,
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class TestCalprmAxisCategoryEnum:
    """Test class for CalprmAxisCategoryEnum class."""

    def test_calprm_axis_category_enum_initialization(self):
        enum = CalprmAxisCategoryEnum()
        enum.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        assert enum.getValue() == "STD_AXIS"

    def test_calprm_axis_category_enum_values(self):
        assert CalprmAxisCategoryEnum.COM_AXIS == "COM_AXIS"
        assert CalprmAxisCategoryEnum.FIX_AXIS == "FIX_AXIS"
        assert CalprmAxisCategoryEnum.RES_AXIS == "RES_AXIS"
        assert CalprmAxisCategoryEnum.STD_AXIS == "STD_AXIS"
        assert CalprmAxisCategoryEnum().getEnumValues() == ["COM_AXIS", "FIX_AXIS", "RES_AXIS", "STD_AXIS"]


class TestSwCalprmAxisTypeProps:
    """Test class for SwCalprmAxisTypeProps abstract class."""

    def test_sw_calprm_axis_type_props_abstract_class(self):
        """Test that SwCalprmAxisTypeProps cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            SwCalprmAxisTypeProps()

    def test_sw_calprm_axis_type_props_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""

        # Create a concrete subclass for testing
        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        concrete_axis_type_props = ConcreteSwCalprmAxisTypeProps()
        assert concrete_axis_type_props.getMaxGradient() is None
        assert concrete_axis_type_props.getMonotony() is None

    def test_sw_calprm_axis_type_props_max_gradient(self):
        """Test getMaxGradient/setMaxGradient (spec Table 5.49, maxGradient: Float 0..1 attr)."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        gradient = Float()
        gradient.setValue(1.5)
        assert props.setMaxGradient(gradient) is props
        assert props.getMaxGradient() is gradient
        assert props.getMaxGradient().getValue() == 1.5

    def test_sw_calprm_axis_type_props_monotony(self):
        """Test getMonotony/setMonotony (spec Table 5.49, monotony: MonotonyEnum 0..1 attr)."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        monotony = MonotonyEnum()
        monotony.setValue(MonotonyEnum.STRICTLY_INCREASING)
        assert props.setMonotony(monotony) is props
        assert props.getMonotony() is monotony
        assert props.getMonotony().getValue() == "strictlyIncreasing"

    def test_sw_calprm_axis_type_props_none_no_op(self):
        """Test that setMaxGradient(None)/setMonotony(None) do not overwrite existing values."""

        class ConcreteSwCalprmAxisTypeProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        props = ConcreteSwCalprmAxisTypeProps()
        gradient = Float()
        gradient.setValue(1.5)
        props.setMaxGradient(gradient)
        monotony = MonotonyEnum()
        monotony.setValue(MonotonyEnum.STRICTLY_INCREASING)
        props.setMonotony(monotony)

        assert props.setMaxGradient(None) is props
        assert props.setMonotony(None) is props
        assert props.getMaxGradient() is gradient
        assert props.getMonotony() is monotony


class TestSwCalprmAxis:
    """Test class for SwCalprmAxis class."""

    def test_sw_calprm_axis_initialization(self):
        """Test that a SwCalprmAxis object can be initialized with default values."""
        sw_calprm_axis = SwCalprmAxis()
        assert sw_calprm_axis.getCategory() is None
        assert sw_calprm_axis.getDisplayFormat() is None
        assert sw_calprm_axis.getSwAxisIndex() is None
        assert sw_calprm_axis.getSwCalibrationAccess() is None
        assert sw_calprm_axis.getSwCalprmAxisTypeProps() is None

    def test_sw_calprm_axis_category(self):
        """Test getCategory/setCategory (spec Table 5.47, category: CalprmAxisCategoryEnum 0..1 attr)."""
        axis = SwCalprmAxis()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        assert axis.setCategory(category) is axis
        assert axis.getCategory() is category
        assert axis.getCategory().getValue() == "STD_AXIS"

    def test_sw_calprm_axis_display_format(self):
        """Test getDisplayFormat/setDisplayFormat (spec Table 5.47, displayFormat: DisplayFormatString 0..1 attr)."""
        axis = SwCalprmAxis()
        display_format = DisplayFormatString()
        display_format.setValue("%.2f")
        assert axis.setDisplayFormat(display_format) is axis
        assert axis.getDisplayFormat() is display_format
        assert axis.getDisplayFormat().getValue() == "%.2f"

    def test_sw_calprm_axis_sw_axis_index(self):
        """Test getSwAxisIndex/setSwAxisIndex (spec Table 5.47, swAxisIndex: AxisIndexType 0..1 attr)."""
        axis = SwCalprmAxis()
        index = AxisIndexType()
        index.setValue("1")
        assert axis.setSwAxisIndex(index) is axis
        assert axis.getSwAxisIndex() is index
        assert axis.getSwAxisIndex().getValue() == "1"

    def test_sw_calprm_axis_sw_calibration_access(self):
        """Test getSwCalibrationAccess/setSwCalibrationAccess (spec Table 5.47, swCalibrationAccess: SwCalibrationAccessEnum 0..1 attr)."""
        axis = SwCalprmAxis()
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        assert axis.setSwCalibrationAccess(access) is axis
        assert axis.getSwCalibrationAccess() is access

    def test_sw_calprm_axis_sw_calprm_axis_type_props(self):
        """Test getSwCalprmAxisTypeProps/setSwCalprmAxisTypeProps (spec Table 5.47, swCalprmAxisTypeProps: SwCalprmAxisTypeProps 0..1 aggr)."""

        class ConcreteProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        axis = SwCalprmAxis()
        props = ConcreteProps()
        assert axis.setSwCalprmAxisTypeProps(props) is axis
        assert axis.getSwCalprmAxisTypeProps() is props

    def test_sw_calprm_axis_none_no_op(self):
        """Test that None setters do not overwrite existing values."""

        class ConcreteProps(SwCalprmAxisTypeProps):
            def __init__(self):
                super().__init__()

        axis = SwCalprmAxis()
        category = CalprmAxisCategoryEnum()
        category.setValue(CalprmAxisCategoryEnum.STD_AXIS)
        axis.setCategory(category)
        display_format = DisplayFormatString()
        display_format.setValue("%.2f")
        axis.setDisplayFormat(display_format)
        index = AxisIndexType()
        index.setValue("1")
        axis.setSwAxisIndex(index)
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        axis.setSwCalibrationAccess(access)
        props = ConcreteProps()
        axis.setSwCalprmAxisTypeProps(props)

        assert axis.setCategory(None) is axis
        assert axis.setDisplayFormat(None) is axis
        assert axis.setSwAxisIndex(None) is axis
        assert axis.setSwCalibrationAccess(None) is axis
        assert axis.setSwCalprmAxisTypeProps(None) is axis
        assert axis.getCategory() is category
        assert axis.getDisplayFormat() is display_format
        assert axis.getSwAxisIndex() is index
        assert axis.getSwCalibrationAccess() is access
        assert axis.getSwCalprmAxisTypeProps() is props


class TestSwCalprmAxisSet:
    """Test class for SwCalprmAxisSet class."""

    def test_sw_calprm_axis_set_initialization(self):
        """Test that a SwCalprmAxisSet object can be initialized with default values."""
        sw_calprm_axis_set = SwCalprmAxisSet()
        assert sw_calprm_axis_set._swCalprmAxis == []

    def test_sw_calprm_axis_set_methods(self):
        """Test adding and getting calibration axis."""
        sw_calprm_axis_set = SwCalprmAxisSet()
        axis = SwCalprmAxis()

        sw_calprm_axis_set.addSwCalprmAxis(axis)
        axises = sw_calprm_axis_set.getSwCalprmAxises()
        assert axis in axises
        assert len(axises) == 1
