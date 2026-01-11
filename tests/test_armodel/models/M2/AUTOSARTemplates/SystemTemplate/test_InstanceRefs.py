import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    VariableDataPrototypeInSystemInstanceRef,
    ComponentInSystemInstanceRef
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class Test_InstanceRefs:
    """Test cases for InstanceRefs-related classes."""
    
    def test_VariableDataPrototypeInSystemInstanceRef(self):
        """Test VariableDataPrototypeInSystemInstanceRef class functionality."""
        ref = VariableDataPrototypeInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)
        
        # Test default values
        assert ref.getBaseRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextCompositionRef() is None
        assert ref.getContextPortRef() is None
        assert ref.getTargetDataPrototypeRef() is None
        
        # Test setter/getter methods
        mock_base_ref = "mock_base_ref"
        ref.setBaseRef(mock_base_ref)
        assert ref.getBaseRef() == mock_base_ref
        
        mock_context_comp_ref = "mock_context_comp_ref"
        ref.setContextCompositionRef(mock_context_comp_ref)
        assert ref.getContextCompositionRef() == mock_context_comp_ref
        
        mock_context_port_ref = "mock_context_port_ref"
        ref.setContextPortRef(mock_context_port_ref)
        assert ref.getContextPortRef() == mock_context_port_ref
        
        mock_target_ref = "mock_target_ref"
        ref.setTargetDataPrototypeRef(mock_target_ref)
        assert ref.getTargetDataPrototypeRef() == mock_target_ref
        
        # Test adding context component refs
        mock_comp_ref1 = "comp1"
        mock_comp_ref2 = "comp2"
        ref.addContextComponentRef(mock_comp_ref1)
        ref.addContextComponentRef(mock_comp_ref2)
        assert ref.getContextComponentRefs() == [mock_comp_ref1, mock_comp_ref2]

    def test_ComponentInSystemInstanceRef(self):
        """Test ComponentInSystemInstanceRef class functionality."""
        ref = ComponentInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)
        
        # Test default values
        assert ref.getBaseRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextCompositionRef() is None
        assert ref.getTargetComponentRef() is None
        
        # Test setter/getter methods
        mock_base_ref = "mock_base_ref"
        ref.setBaseRef(mock_base_ref)
        assert ref.getBaseRef() == mock_base_ref
        
        mock_context_comp_ref = "mock_context_comp_ref"
        ref.setContextCompositionRef(mock_context_comp_ref)
        assert ref.getContextCompositionRef() == mock_context_comp_ref
        
        mock_target_comp_ref = "mock_target_comp_ref"
        ref.setTargetComponentRef(mock_target_comp_ref)
        assert ref.getTargetComponentRef() == mock_target_comp_ref
        
        # Test adding context component refs
        mock_comp_ref1 = "comp1"
        mock_comp_ref2 = "comp2"
        ref.addContextComponentRef(mock_comp_ref1)
        ref.addContextComponentRef(mock_comp_ref2)
        assert ref.getContextComponentRefs() == [mock_comp_ref1, mock_comp_ref2]