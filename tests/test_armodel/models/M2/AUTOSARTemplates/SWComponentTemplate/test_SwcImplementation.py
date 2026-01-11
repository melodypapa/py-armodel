"""
This module contains comprehensive tests for the SwcImplementation module in SWComponentTemplate.
Tests cover all classes and methods in the SwcImplementation.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (
    SwcImplementation
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestSwcImplementation:
    """Test class for SwcImplementation class."""
    
    def test_swc_implementation_initialization(self):
        """Test SwcImplementation initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc_impl = SwcImplementation(ar_root, "TestSwcImplementation")
        
        assert swc_impl.parent == ar_root
        assert swc_impl.short_name == "TestSwcImplementation"
        assert swc_impl.behaviorRef is None
        assert swc_impl.perInstanceMemorySizes == []
        assert swc_impl.requiredRTEVendor is None
        
        # Test behaviorRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        behavior_ref = RefType()
        behavior_ref.setValue("/Behavior/Ref")
        swc_impl.setBehaviorRef(behavior_ref)
        assert swc_impl.getBehaviorRef() == behavior_ref
        
        # Test perInstanceMemorySizes methods
        mem_size = "test_memory_size"
        swc_impl.addPerInstanceMemorySize(mem_size)
        assert mem_size in swc_impl.getPerInstanceMemorySizes()
        
        # Test requiredRTEVendor methods
        rte_vendor = "TestRTEVendor"
        swc_impl.setRequiredRTEVendor(rte_vendor)
        assert swc_impl.getRequiredRTEVendor() == rte_vendor