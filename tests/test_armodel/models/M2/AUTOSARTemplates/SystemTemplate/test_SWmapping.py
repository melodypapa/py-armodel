import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    SwcToImplMapping,
    ApplicationPartitionToEcuPartitionMapping
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_SWmapping:
    """Test cases for SWmapping-related classes."""
    
    def test_SwcToImplMapping(self):
        """Test SwcToImplMapping class functionality."""
        parent = MockParent()
        mapping = SwcToImplMapping(parent, "test_sw_impl_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getComponentIRefs() == []
        assert mapping.getComponentImplementationRef() is None
        
        # Test setter/getter methods
        mock_impl_ref = "mock_impl_ref"
        mapping.setComponentImplementationRef(mock_impl_ref)
        assert mapping.getComponentImplementationRef() == mock_impl_ref
        
        # Test adding component IRefs
        mock_comp_ref = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(mock_comp_ref)
        assert mapping.getComponentIRefs() == [mock_comp_ref]
        
        # Test multiple component refs
        mock_comp_ref2 = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(mock_comp_ref2)
        assert mapping.getComponentIRefs() == [mock_comp_ref, mock_comp_ref2]

    def test_ApplicationPartitionToEcuPartitionMapping(self):
        """Test ApplicationPartitionToEcuPartitionMapping class functionality."""
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getEcuPartitionRef() is None
        
        # Test setter/getter methods
        mock_ecu_part_ref = "mock_ecu_part_ref"
        mapping.setEcuPartitionRef(mock_ecu_part_ref)
        assert mapping.getEcuPartitionRef() == mock_ecu_part_ref
        
        # Test adding application partition refs
        mock_app_part_ref1 = "app_part_ref1"
        mock_app_part_ref2 = "app_part_ref2"
        mapping.addApplicationPartitionRef(mock_app_part_ref1)
        mapping.addApplicationPartitionRef(mock_app_part_ref2)
        assert mapping.getApplicationPartitionRefs() == [mock_app_part_ref1, mock_app_part_ref2]