"""
This module contains tests for the AuxillaryObjects module in MSR.DataDictionary.
"""
import pytest
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import *
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral


class TestSwAddrMethod:
    """Test class for SwAddrMethod class."""
    
    def test_sw_addr_method_initialization(self):
        """Test that a SwAddrMethod object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_addr_method = SwAddrMethod(parent_obj, "test_name")
        assert sw_addr_method.memoryAllocationKeywordPolicy is None
        assert sw_addr_method.options == []
        assert sw_addr_method.sectionInitializationPolicy is None
        assert sw_addr_method.sectionType is None
    
    def test_sw_addr_method_memory_allocation_keyword_policy_methods(self):
        """Test the memoryAllocationKeywordPolicy getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_addr_method = SwAddrMethod(parent_obj, "test_name")
        policy = ARLiteral()
        
        result = sw_addr_method.setMemoryAllocationKeywordPolicy(policy)
        assert sw_addr_method.getMemoryAllocationKeywordPolicy() == policy
        assert result == sw_addr_method
    
    def test_sw_addr_method_options_methods(self):
        """Test adding and getting options."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_addr_method = SwAddrMethod(parent_obj, "test_name")
        option = ARLiteral()
        
        result = sw_addr_method.addOption(option)
        options = sw_addr_method.getOptions()
        assert option in options
        assert result == sw_addr_method
    
    def test_sw_addr_method_section_initialization_policy_methods(self):
        """Test the sectionInitializationPolicy getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_addr_method = SwAddrMethod(parent_obj, "test_name")
        policy = ARLiteral()
        
        result = sw_addr_method.setSectionInitializationPolicy(policy)
        assert sw_addr_method.getSectionInitializationPolicy() == policy
        assert result == sw_addr_method
    
    def test_sw_addr_method_section_type_methods(self):
        """Test the sectionType getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_addr_method = SwAddrMethod(parent_obj, "test_name")
        section_type = ARLiteral()
        
        result = sw_addr_method.setSectionType(section_type)
        assert sw_addr_method.getSectionType() == section_type
        assert result == sw_addr_method