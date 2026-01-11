"""
Test suite for BswModuleDescription class in armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.

This module tests the BSW (Basic Software) module description class which serves as the root element 
for describing a single BSW module or BSW cluster. It includes functionality for managing BSW 
dependencies, documentation, entry references, internal behaviors, and various other BSW-specific elements.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleDependency
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from armodel import AUTOSAR


class TestBswModuleDescription:
    """Test cases for BswModuleDescription class - represents BSW module description details."""
    
    def test_initialization(self):
        """Test BswModuleDescription initialization with default values."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.short_name == "test_bsw_module"
        assert desc.getBswModuleDependencies() == []
        assert desc.getBswModuleDocumentation() is None
        assert desc.getExpectedEntryRefs() == []
        assert desc.getImplementedEntryRefs() == []
        assert desc.getInternalBehaviors() == []
        assert desc.getModuleId() is None
        assert desc.getProvidedClientServerEntries() == []
        assert desc.getProvidedDatas() == []
        assert desc.getProvidedModeGroups() == []
        assert desc.getReleasedTriggers() == []
        assert desc.getRequiredClientServerEntries() == []
        assert desc.getRequiredDatas() == []
        assert desc.getRequiredModeGroups() == []
        assert desc.getRequiredTriggers() == []
    
    def test_get_set_bsw_module_dependencies(self):
        """Test getter and setter for BSW module dependencies."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        # Create a mock dependency
        dependency = BswModuleDependency(ar_root, "test_dependency")
        dependencies = [dependency]
        result = desc.setBswModuleDependencies(dependencies)
        
        assert result == desc
        assert desc.getBswModuleDependencies() == dependencies
        
        # Test setting None (should not change value)
        result = desc.setBswModuleDependencies(None)
        assert result == desc
        assert desc.getBswModuleDependencies() == dependencies  # Should remain unchanged
    
    def test_get_set_bsw_module_documentation(self):
        """Test getter and setter for BSW module documentation."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        doc = SwComponentDocumentation()
        result = desc.setBswModuleDocumentation(doc)
        
        assert result == desc
        assert desc.getBswModuleDocumentation() == doc
        
        # Test setting None (should not change value)
        result = desc.setBswModuleDocumentation(None)
        assert result == desc
        assert desc.getBswModuleDocumentation() == doc  # Should remain unchanged
    
    def test_get_set_expected_entry_refs(self):
        """Test getter and setter for expected entry references."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        ref = RefType()
        ref.setValue("/path/to/expected/entry")
        refs = [ref]
        result = desc.setExpectedEntryRefs(refs)
        
        assert result == desc
        assert desc.getExpectedEntryRefs() == refs
        
        # Test setting None (should not change value)
        result = desc.setExpectedEntryRefs(None)
        assert result == desc
        assert desc.getExpectedEntryRefs() == refs  # Should remain unchanged
    
    def test_get_implemented_entry_refs(self):
        """Test getter for implemented entry references."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getImplementedEntryRefs() == []
    
    def test_add_implemented_entry_ref(self):
        """Test adding implemented entry reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        ref = RefType()
        ref.setValue("/path/to/implemented/entry")
        result = desc.addImplementedEntryRef(ref)
        
        assert result == desc
        assert desc.getImplementedEntryRefs() == [ref]
        
        # Test adding None (should not be added)
        result = desc.addImplementedEntryRef(None)
        assert result == desc
        assert len(desc.getImplementedEntryRefs()) == 1  # Should remain unchanged
    
    def test_get_set_internal_behaviors(self):
        """Test getter and setter for internal behaviors."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        behavior = BswInternalBehavior(ar_root, "test_behavior")
        behaviors = [behavior]
        result = desc.setInternalBehaviors(behaviors)
        
        assert result == desc
        assert desc.getInternalBehaviors() == behaviors
        
        # Test setting None (should not change value)
        result = desc.setInternalBehaviors(None)
        assert result == desc
        assert desc.getInternalBehaviors() == behaviors  # Should remain unchanged
    
    def test_create_bsw_internal_behavior(self):
        """Test creating BSW internal behavior."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        behavior = desc.createBswInternalBehavior("test_behavior")
        
        assert behavior.short_name == "test_behavior"
        assert len(desc.getInternalBehaviors()) == 1
        assert desc.getInternalBehaviors()[0] == behavior
    
    def test_get_set_module_id(self):
        """Test getter and setter for module ID."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        module_id = PositiveInteger()
        module_id.setValue(123)
        result = desc.setModuleId(module_id)
        
        assert result == desc
        assert desc.getModuleId() == module_id
        
        # Test setting None (should not change value)
        result = desc.setModuleId(None)
        assert result == desc
        assert desc.getModuleId() == module_id  # Should remain unchanged
    
    def test_get_provided_client_server_entries(self):
        """Test getter for provided client server entries."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getProvidedClientServerEntries() == []
    
    def test_create_provided_client_server_entry(self):
        """Test creating provided client server entry."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        entry = desc.createProvidedClientServerEntry("test_entry")
        
        assert entry.short_name == "test_entry"
        assert len(desc.getProvidedClientServerEntries()) == 1
        assert desc.getProvidedClientServerEntries()[0] == entry
    
    def test_get_provided_datas(self):
        """Test getter for provided data prototypes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getProvidedDatas() == []
    
    def test_create_provided_data(self):
        """Test creating provided data prototype."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        data = desc.createProvidedData("test_data")
        
        assert data.short_name == "test_data"
        assert len(desc.getProvidedDatas()) == 1
        assert desc.getProvidedDatas()[0] == data
    
    def test_get_provided_mode_groups(self):
        """Test getter for provided mode groups."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getProvidedModeGroups() == []
    
    def test_create_provided_mode_group(self):
        """Test creating provided mode group."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        mode_group = desc.createProvidedModeGroup("test_mode_group")
        
        assert mode_group.short_name == "test_mode_group"
        assert len(desc.getProvidedModeGroups()) == 1
        assert desc.getProvidedModeGroups()[0] == mode_group
    
    def test_get_released_triggers(self):
        """Test getter for released triggers."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getReleasedTriggers() == []
    
    def test_create_released_trigger(self):
        """Test creating released trigger."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        trigger = desc.createReleasedTrigger("test_trigger")
        
        assert trigger.short_name == "test_trigger"
        assert len(desc.getReleasedTriggers()) == 1
        assert desc.getReleasedTriggers()[0] == trigger
    
    def test_get_required_client_server_entries(self):
        """Test getter for required client server entries."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getRequiredClientServerEntries() == []
    
    def test_create_required_client_server_entry(self):
        """Test creating required client server entry."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        entry = desc.createRequiredClientServerEntry("test_required_entry")
        
        assert entry.short_name == "test_required_entry"
        assert len(desc.getRequiredClientServerEntries()) == 1
        assert desc.getRequiredClientServerEntries()[0] == entry
    
    def test_get_required_datas(self):
        """Test getter for required data prototypes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getRequiredDatas() == []
    
    def test_create_required_data(self):
        """Test creating required data prototype."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        data = desc.createRequiredData("test_required_data")
        
        assert data.short_name == "test_required_data"
        assert len(desc.getRequiredDatas()) == 1
        assert desc.getRequiredDatas()[0] == data
    
    def test_get_required_mode_groups(self):
        """Test getter for required mode groups."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getRequiredModeGroups() == []
    
    def test_create_required_mode_group(self):
        """Test creating required mode group."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        mode_group = desc.createRequiredModeGroup("test_required_mode_group")
        
        assert mode_group.short_name == "test_required_mode_group"
        assert len(desc.getRequiredModeGroups()) == 1
        assert desc.getRequiredModeGroups()[0] == mode_group
    
    def test_get_required_triggers(self):
        """Test getter for required triggers."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        assert desc.getRequiredTriggers() == []
    
    def test_create_required_trigger(self):
        """Test creating required trigger."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = BswModuleDescription(ar_root, "test_bsw_module")
        
        trigger = desc.createRequiredTrigger("test_required_trigger")
        
        assert trigger.short_name == "test_required_trigger"
        assert len(desc.getRequiredTriggers()) == 1
        assert desc.getRequiredTriggers()[0] == trigger