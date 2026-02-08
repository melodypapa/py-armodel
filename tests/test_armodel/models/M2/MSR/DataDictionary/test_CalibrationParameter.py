"""
This module contains tests for the CalibrationParameter module in MSR.DataDictionary.
"""
import pytest

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import *


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
        assert concrete_axis_type_props.maxGradient is None
        assert concrete_axis_type_props.monotony is None


class TestSwCalprmAxis:
    """Test class for SwCalprmAxis class."""

    def test_sw_calprm_axis_initialization(self):
        """Test that a SwCalprmAxis object can be initialized with default values."""
        sw_calprm_axis = SwCalprmAxis()
        assert sw_calprm_axis.category is None
        assert sw_calprm_axis.displayFormat is None
        assert sw_calprm_axis.sw_axis_index is None
        assert sw_calprm_axis.swCalibrationAccess is None
        assert sw_calprm_axis.sw_calprm_axis_type_props is None


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
