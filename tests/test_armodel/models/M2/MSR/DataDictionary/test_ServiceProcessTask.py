"""
This module contains tests for the ServiceProcessTask module in MSR.DataDictionary.
"""
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import *
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, ValueList
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ArgumentDirectionEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage


class TestSwServiceArg:
    """Test class for SwServiceArg class."""
    
    def test_sw_service_arg_initialization(self):
        """Test that a SwServiceArg object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_service_arg = SwServiceArg(parent_obj, "test_name")
        assert sw_service_arg.direction is None
        assert sw_service_arg.swArraysize is None
        assert sw_service_arg.swDataDefProps is None
    
    def test_sw_service_arg_direction_methods(self):
        """Test the direction getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_service_arg = SwServiceArg(parent_obj, "test_name")
        direction = ArgumentDirectionEnum()
        
        result = sw_service_arg.setDirection(direction)
        assert sw_service_arg.getDirection() == direction
        assert result == sw_service_arg
    
    def test_sw_service_arg_sw_array_size_methods(self):
        """Test the swArraysize getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_service_arg = SwServiceArg(parent_obj, "test_name")
        array_size = ValueList()
        
        result = sw_service_arg.setSwArraysize(array_size)
        assert sw_service_arg.getSwArraysize() == array_size
        assert result == sw_service_arg
    
    def test_sw_service_arg_sw_data_def_props_methods(self):
        """Test the swDataDefProps getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_service_arg = SwServiceArg(parent_obj, "test_name")
        data_def_props = SwDataDefProps()
        
        result = sw_service_arg.setSwDataDefProps(data_def_props)
        assert sw_service_arg.getSwDataDefProps() == data_def_props
        assert result == sw_service_arg