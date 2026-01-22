"""
This module contains comprehensive tests for the InstanceRefs module in SWComponentTemplate.PortInterface.
Tests cover all classes and methods in the InstanceRefs.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
    ApplicationCompositeElementInPortInterfaceInstanceRef
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestApplicationCompositeElementInPortInterfaceInstanceRef:
    """Test class for ApplicationCompositeElementInPortInterfaceInstanceRef class."""
    
    def test_application_composite_element_in_port_interface_instance_ref_initialization(self):
        """Test ApplicationCompositeElementInPortInterfaceInstanceRef initialization and methods."""
        instance_ref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        
        assert instance_ref.baseRef is None
        assert instance_ref.contextDataPrototypeRef is None
        assert instance_ref.rootDataPrototypeRef is None
        assert instance_ref.targetDataPrototypeRef is None
        
        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref
        
        # Test contextDataPrototypeRef methods
        context_ref = RefType()
        context_ref.setValue("/Context/DataPrototype")
        instance_ref.setContextDataPrototypeRef(context_ref)
        assert instance_ref.getContextDataPrototypeRef() == context_ref
        
        # Test rootDataPrototypeRef methods
        root_ref = RefType()
        root_ref.setValue("/Root/DataPrototype")
        instance_ref.setRootDataPrototypeRef(root_ref)
        assert instance_ref.getRootDataPrototypeRef() == root_ref
        
        # Test targetDataPrototypeRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/DataPrototype")
        instance_ref.setTargetDataPrototypeRef(target_ref)
        assert instance_ref.getTargetDataPrototypeRef() == target_ref