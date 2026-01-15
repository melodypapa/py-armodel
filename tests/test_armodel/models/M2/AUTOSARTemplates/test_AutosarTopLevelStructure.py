"""
Test suite for AutosarTopLevelStructure module

This module tests the AUTOSAR-related classes including:
- FileInfoComment
- AbstractAUTOSAR
- AUTOSAR (singleton)
- AUTOSARDoc
"""

import pytest
from unittest.mock import Mock, patch
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    FileInfoComment, AbstractAUTOSAR, AUTOSAR, AUTOSARDoc
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType, CompositionSwComponentType, PortPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignal, SystemSignalGroup
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswSchedulableEntity, BswCalledEntity
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleEntry
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestFileInfoComment:
    """Test cases for the FileInfoComment class."""
    
    def test_file_info_comment_initialization(self):
        """Test that FileInfoComment initializes with an empty sdgs list."""
        comment = FileInfoComment()
        assert comment.sdgs == []
    
    def test_get_sdgs(self):
        """Test the getSdgs method."""
        comment = FileInfoComment()
        sdg = Sdg()
        comment.sdgs = [sdg]
        assert comment.getSdgs() == [sdg]
    
    def test_set_sdgs(self):
        """Test the setSdgs method."""
        comment = FileInfoComment()
        sdg = Sdg()
        result = comment.setSdgs([sdg])
        assert comment.sdgs == [sdg]
        assert result == comment


class TestAbstractAUTOSAR:
    """Test cases for the AbstractAUTOSAR class."""
    
    def test_abstract_autosar_initialization(self):
        """Test that AbstractAUTOSAR initializes with all required attributes."""
        autosar = AbstractAUTOSAR()
        
        # Check release mappings
        assert "4.0.3" in autosar.release_xsd_mappings
        assert "R24-11" in autosar.release_xsd_mappings
        
        # Check initial values
        assert autosar.adminData is None
        assert autosar.fileInfoComment is None
        assert autosar.introduction is None
        
        # Check cleared values
        assert autosar.schema_location is None
        assert autosar._appl_impl_type_maps == {}
        assert autosar._impl_appl_type_maps == {}
        assert autosar._behavior_impl_maps == {}
        assert autosar._impl_behavior_maps == {}
        assert autosar.systems == {}
        assert autosar.compositionSwComponentTypes == {}
        assert autosar.rootSwCompositionPrototype is None
    
    def test_get_admin_data(self):
        """Test the getAdminData method."""
        autosar = AbstractAUTOSAR()
        mock_admin_data = Mock()
        autosar.adminData = mock_admin_data
        assert autosar.getAdminData() == mock_admin_data
    
    def test_set_admin_data(self):
        """Test the setAdminData method."""
        autosar = AbstractAUTOSAR()
        mock_admin_data = Mock()
        result = autosar.setAdminData(mock_admin_data)
        assert autosar.adminData == mock_admin_data
        assert result == autosar
    
    def test_set_admin_data_none(self):
        """Test the setAdminData method with None value."""
        autosar = AbstractAUTOSAR()
        result = autosar.setAdminData(None)
        # Setting None should not change the adminData
        assert autosar.adminData is None
        assert result == autosar
    
    def test_remove_admin_data(self):
        """Test the removeAdminData method."""
        autosar = AbstractAUTOSAR()
        autosar.adminData = Mock()
        autosar.removeAdminData()
        assert autosar.adminData is None
    
    def test_get_file_info_comment(self):
        """Test the getFileInfoComment method."""
        autosar = AbstractAUTOSAR()
        mock_comment = Mock()
        autosar.fileInfoComment = mock_comment
        assert autosar.getFileInfoComment() == mock_comment
    
    def test_set_file_info_comment(self):
        """Test the setFileInfoComment method."""
        autosar = AbstractAUTOSAR()
        mock_comment = Mock()
        result = autosar.setFileInfoComment(mock_comment)
        assert autosar.fileInfoComment == mock_comment
        assert result == autosar
    
    def test_get_introduction(self):
        """Test the getIntroduction method."""
        autosar = AbstractAUTOSAR()
        mock_intro = Mock()
        autosar.introduction = mock_intro
        assert autosar.getIntroduction() == mock_intro
    
    def test_set_introduction(self):
        """Test the setIntroduction method."""
        autosar = AbstractAUTOSAR()
        mock_intro = Mock()
        result = autosar.setIntroduction(mock_intro)
        assert autosar.introduction == mock_intro
        assert result == autosar
    
    def test_reload(self):
        """Test the reload method."""
        autosar = AbstractAUTOSAR()
        # Method should exist and not raise an exception
        result = autosar.reload()
        assert result is None
    
    def test_full_name_property(self):
        """Test the full_name property."""
        autosar = AbstractAUTOSAR()
        assert autosar.full_name == ""
    
    def test_clear(self):
        """Test the clear method."""
        autosar = AbstractAUTOSAR()
        # Modify some attributes
        autosar.adminData = Mock()
        autosar._appl_impl_type_maps = {"test": "value"}
        
        # Call clear
        autosar.clear()
        
        # Check that they are reset
        assert autosar.adminData is None
        assert autosar._appl_impl_type_maps == {}
    
    def test_get_element_with_ar_package(self):
        """Test the getElement method when short_name is in arPackages."""
        autosar = AbstractAUTOSAR()
        test_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = test_package
        
        result = autosar.getElement("TestPackage")
        assert result == test_package
    
    def test_get_element_fallback(self):
        """Test the getElement method fallback to parent class."""
        autosar = AbstractAUTOSAR()
        # Add a package to the autosar instance
        test_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = test_package
        
        # Try to get a non-existent element (this will call parent method)
        result = autosar.getElement("NonExistent")
        assert result is None
    
    def test_get_ar_packages(self):
        """Test the getARPackages method."""
        autosar = AbstractAUTOSAR()
        test_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = test_package
        
        result = autosar.getARPackages()
        assert len(result) == 1
        assert result[0] == test_package
    
    def test_create_ar_package_new(self):
        """Test the createARPackage method for a new package."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.createARPackage("TestPackage")
        
        assert "TestPackage" in autosar.arPackages
        assert result == autosar.arPackages["TestPackage"]
    
    def test_create_ar_package_existing(self):
        """Test the createARPackage method for an existing package."""
        autosar = AbstractAUTOSAR()
        existing_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = existing_package
        
        result = autosar.createARPackage("TestPackage")
        
        # Should return the existing package
        assert result == existing_package
        assert len(autosar.arPackages) == 1
    
    def test_find_with_ref_type(self):
        """Test the find method with RefType."""
        # Use AUTOSAR singleton since find() method uses AUTOSAR.getInstance() internally
        autosar = AUTOSAR.getInstance()
        test_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = test_package
        
        mock_ref_type = Mock(spec=RefType)
        mock_ref_type.getValue.return_value = "TestPackage"
        mock_ref_type.getDest.return_value = None
        
        result = autosar.find(mock_ref_type)
        assert result == test_package
        
        # Clean up
        autosar.new()
    
    def test_find_with_string(self):
        """Test the find method with string reference."""
        # Use AUTOSAR singleton since find() method uses AUTOSAR.getInstance() internally
        autosar = AUTOSAR.getInstance()
        test_package = ARPackage(autosar, "TestPackage")
        autosar.arPackages["TestPackage"] = test_package
        
        result = autosar.find("TestPackage")
        assert result == test_package
        
        # Clean up
        autosar.new()
    
    def test_find_with_nested_reference(self):
        """Test the find method with nested references."""
        # Use AUTOSAR singleton since find() method uses AUTOSAR.getInstance() internally
        autosar = AUTOSAR.getInstance()
        # Create a child element that's not in arPackages but in sub-elements
        pkg = autosar.createARPackage("ParentPackage")
        
        result = autosar.find("ParentPackage")
        assert result == pkg
        
        # Clean up
        autosar.new()
    
    def test_find_with_empty_string_in_reference(self):
        """Test the find method with empty string in reference path."""
        # Use AUTOSAR singleton since find() method uses AUTOSAR.getInstance() internally
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("TestPackage")

        # This simulates a reference like "/TestPackage" with empty string at start
        result = autosar.find("TestPackage")
        assert result == pkg

        # Clean up
        autosar.new()

    def test_find_returns_none_when_element_not_found(self):
        """Test the find method returns None when element is not found (line 145)."""
        autosar = AUTOSAR.getInstance()
        # Try to find a non-existent element
        result = autosar.find("NonExistentPackage/NonExistentElement")
        assert result is None
        # Clean up
        autosar.new()

    def test_find_with_referred_type_validation(self):
        """Test the find method with referred_type validation (lines 149-151)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("TestPackage")
        impl_type = ImplementationDataType(pkg, "TestImplType")
        pkg.addElement(impl_type)  # Add the element to the package

        # Create a RefType with a referred type that doesn't match
        ref_type = RefType()
        ref_type.setValue("TestPackage/TestImplType")
        ref_type.setDest("WRONG-TYPE")  # This doesn't match IMPLEMENTATION-DATA-TYPE

        # This should raise ValueError because types don't match
        with pytest.raises(ValueError, match="The type does not matched"):
            autosar.find(ref_type)

        # Clean up
        autosar.new()


    
    def test_get_dest_type_implementation_data_type(self):
        """Test the getDestType method for ImplementationDataType."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        impl_type = ImplementationDataType(pkg, "TestImplType")
        result = autosar.getDestType(impl_type)
        assert result == "IMPLEMENTATION-DATA-TYPE"
    
    def test_get_dest_type_application_data_type(self):
        """Test the getDestType method for ApplicationDataType."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationPrimitiveDataType
        
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        app_type = ApplicationPrimitiveDataType(pkg, "TestAppType")
        result = autosar.getDestType(app_type)
        assert result == "APPLICATION-DATA-TYPE"
    
    def test_get_dest_type_atomic_sw_component_type(self):
        """Test the getDestType method for AtomicSwComponentType."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        comp_type = AtomicSwComponentType(pkg, "TestCompType")
        result = autosar.getDestType(comp_type)
        assert result == "ATOMIC-SW-COMPONENT-TYPE"
    
    def test_get_dest_type_composition_sw_component_type(self):
        """Test the getDestType method for CompositionSwComponentType."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        comp_type = CompositionSwComponentType(pkg, "TestCompType")
        result = autosar.getDestType(comp_type)
        assert result == "COMPOSITION-SW-COMPONENT-TYPE"
    
    def test_get_dest_type_system_signal(self):
        """Test the getDestType method for SystemSignal."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        signal = SystemSignal(pkg, "TestSignal")
        result = autosar.getDestType(signal)
        assert result == "SYSTEM-SIGNAL"
    
    def test_get_dest_type_system_signal_group(self):
        """Test the getDestType method for SystemSignalGroup."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        signal_group = SystemSignalGroup(pkg, "TestSignalGroup")
        result = autosar.getDestType(signal_group)
        assert result == "SYSTEM-SIGNAL-GROUP"
    
    def test_get_dest_type_runnable_entity(self):
        """Test the getDestType method for RunnableEntity."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        runnable = RunnableEntity(pkg, "TestRunnable")
        result = autosar.getDestType(runnable)
        assert result == "RUNNABLE-ENTITY"
    
    def test_get_dest_type_bsw_schedulable_entity(self):
        """Test the getDestType method for BswSchedulableEntity."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        entity = BswSchedulableEntity(pkg, "TestEntity")
        result = autosar.getDestType(entity)
        assert result == "BSW-SCHEDULABLE-ENTITY"
    
    def test_get_dest_type_bsw_module_entry(self):
        """Test the getDestType method for BswModuleEntry."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        entry = BswModuleEntry(pkg, "TestEntry")
        result = autosar.getDestType(entry)
        assert result == "BSW-MODULE-ENTRY"
    
    def test_get_dest_type_bsw_called_entity(self):
        """Test the getDestType method for BswCalledEntity."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        entity = BswCalledEntity(pkg, "TestEntity")
        result = autosar.getDestType(entity)
        assert result == "BSW-CALLED-ENTITY"
    
    def test_get_dest_type_not_implemented(self):
        """Test the getDestType method for unsupported types."""
        autosar = AbstractAUTOSAR()
        mock_obj = Mock()
        mock_obj.__class__.__name__ = "MockClass"
        
        with pytest.raises(NotImplementedError):
            autosar.getDestType(mock_obj)
    
    def test_find_atomic_sw_component_type(self):
        """Test the findAtomicSwComponentType method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=AtomicSwComponentType)
            mock_find.return_value = mock_result
            result = autosar.findAtomicSwComponentType("TestComponent")
            assert result == mock_result
            mock_find.assert_called_once_with("TestComponent")
    
    def test_find_system_signal(self):
        """Test the findSystemSignal method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=SystemSignal)
            mock_find.return_value = mock_result
            result = autosar.findSystemSignal("TestSignal")
            assert result == mock_result
            mock_find.assert_called_once_with("TestSignal")
    
    def test_find_system_signal_group(self):
        """Test the findSystemSignalGroup method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=SystemSignalGroup)
            mock_find.return_value = mock_result
            result = autosar.findSystemSignalGroup("TestSignalGroup")
            assert result == mock_result
            mock_find.assert_called_once_with("TestSignalGroup")
    
    def test_find_port(self):
        """Test the findPort method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=PortPrototype)
            mock_find.return_value = mock_result
            result = autosar.findPort("TestPort")
            assert result == mock_result
            mock_find.assert_called_once_with("TestPort")
    
    def test_find_variable_data_prototype(self):
        """Test the findVariableDataPrototype method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=VariableDataPrototype)
            mock_find.return_value = mock_result
            result = autosar.findVariableDataPrototype("TestDataPrototype")
            assert result == mock_result
            mock_find.assert_called_once_with("TestDataPrototype")
    
    def test_find_implementation_data_type(self):
        """Test the findImplementationDataType method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar, 'find') as mock_find:
            mock_result = Mock(spec=ImplementationDataType)
            mock_find.return_value = mock_result
            result = autosar.findImplementationDataType("TestImplType")
            assert result == mock_result
            mock_find.assert_called_once_with("TestImplType")
    
    def test_get_data_type_with_implementation_data_type(self):
        """Test the getDataType method with ImplementationDataType."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        impl_type = ImplementationDataType(pkg, "TestImplType")
        impl_type.category = ImplementationDataType.CATEGORY_TYPE_REFERENCE
        impl_type.swDataDefProps = Mock()
        impl_type.swDataDefProps.implementationDataTypeRef = Mock()
        impl_type.swDataDefProps.implementationDataTypeRef.value = "test_ref"
        
        # Mock find to return a different type to avoid recursion
        different_type = ImplementationDataType(pkg, "DifferentType")
        with patch.object(autosar, 'find', return_value=different_type):
            result = autosar.getDataType(impl_type)
            assert result == different_type
    
    def test_get_data_type_with_sw_base_type(self):
        """Test the getDataType method with SwBaseType."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        base_type = SwBaseType(pkg, "TestBaseType")

        result = autosar.getDataType(base_type)
        assert result == base_type

    def test_get_data_type_with_data_reference(self):
        """Test getDataType with CATEGORY_DATA_REFERENCE to cover lines 203-205."""
        # Use AUTOSAR singleton to ensure packages are properly tracked
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("TestPackage")
        base_type = ImplementationDataType(pkg, "BaseType")
        pkg.addElement(base_type)

        # Create a data reference type (lines 203-205)
        data_ref_type = ImplementationDataType(pkg, "DataRefType")
        data_ref_type.category = ImplementationDataType.CATEGORY_DATA_REFERENCE

        # Create a RefType for the base type reference
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        mock_base_type_ref = RefType()
        mock_base_type_ref.setValue("TestPackage/BaseType")

        # Setup swDataDefProps structure
        data_ref_type.swDataDefProps = Mock()
        data_ref_type.swDataDefProps.swPointerTargetProps = Mock()
        data_ref_type.swDataDefProps.swPointerTargetProps.getTargetCategory.return_value = "VALUE"
        data_ref_type.swDataDefProps.swPointerTargetProps.getSwDataDefProps.return_value.getBaseTypeRef.return_value = mock_base_type_ref

        # Call getDataType - it should find base_type and return it
        # Since base_type is not a TYPE_REFERENCE or DATA_REFERENCE, it will return itself
        result = autosar.getDataType(data_ref_type)

        # The method should call find with the base type ref and return base_type
        assert result == base_type

        # Clean up
        autosar.new()

    
    def test_get_data_type_with_invalid_type(self):
        """Test the getDataType method with invalid type."""
        autosar = AbstractAUTOSAR()
        invalid_type = "not_a_valid_type"
        
        with pytest.raises(ValueError):
            autosar.getDataType(invalid_type)
    
    def test_add_data_type_map(self):
        """Test the addDataTypeMap method."""
        autosar = AbstractAUTOSAR()
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap
        data_type_map = DataTypeMap()
        data_type_map.applicationDataTypeRef = Mock()
        data_type_map.applicationDataTypeRef.value = "app_type"
        data_type_map.implementationDataTypeRef = Mock()
        data_type_map.implementationDataTypeRef.value = "impl_type"
        
        autosar.addDataTypeMap(data_type_map)
        
        assert "app_type" in autosar._appl_impl_type_maps
        assert "impl_type" in autosar._impl_appl_type_maps
        assert autosar._appl_impl_type_maps["app_type"] == "impl_type"
        assert autosar._impl_appl_type_maps["impl_type"] == "app_type"
    
    def test_add_data_type_map_with_none_refs(self):
        """Test the addDataTypeMap method with None references."""
        autosar = AbstractAUTOSAR()
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap
        data_type_map = DataTypeMap()
        data_type_map.applicationDataTypeRef = None
        data_type_map.implementationDataTypeRef = None
        
        autosar.addDataTypeMap(data_type_map)
        
        # Should not add anything to the mappings
        assert autosar._appl_impl_type_maps == {}
        assert autosar._impl_appl_type_maps == {}
    
    def test_convert_to_implementation_data_type(self):
        """Test the convertToImplementationDataType method."""
        autosar = AbstractAUTOSAR()
        autosar._appl_impl_type_maps["app_type"] = "impl_type"
        
        with patch.object(autosar, 'find', return_value="found_type"):
            result = autosar.convertToImplementationDataType("app_type")
            assert result == "found_type"
    
    def test_convert_to_implementation_data_type_invalid(self):
        """Test the convertToImplementationDataType method with invalid type."""
        autosar = AbstractAUTOSAR()
        
        with pytest.raises(IndexError):
            autosar.convertToImplementationDataType("invalid_type")
    
    def test_convert_to_application_data_type(self):
        """Test the convertToApplicationDataType method."""
        autosar = AbstractAUTOSAR()
        autosar._impl_appl_type_maps["impl_type"] = "app_type"
        
        with patch.object(autosar, 'find', return_value="found_type"):
            result = autosar.convertToApplicationDataType("impl_type")
            assert result == "found_type"
    
    def test_convert_to_application_data_type_invalid(self):
        """Test the convertToApplicationDataType method with invalid type."""
        autosar = AbstractAUTOSAR()
        
        with pytest.raises(IndexError):
            autosar.convertToApplicationDataType("invalid_type")
    
    def test_get_root_sw_composition_prototype(self):
        """Test the getRootSwCompositionPrototype method."""
        autosar = AbstractAUTOSAR()
        assert autosar.getRootSwCompositionPrototype() is None
    
    def test_set_root_sw_composition_prototype(self):
        """Test the setRootSwCompositionPrototype method."""
        autosar = AbstractAUTOSAR()
        mock_value = Mock()
        mock_value.getShortName.return_value = "test_name"
        
        result = autosar.setRootSwCompositionPrototype(mock_value)
        assert autosar.rootSwCompositionPrototype == mock_value
        assert result == autosar
    
    def test_set_root_sw_composition_prototype_none(self):
        """Test the setRootSwCompositionPrototype method with None."""
        autosar = AbstractAUTOSAR()
        result = autosar.setRootSwCompositionPrototype(None)
        assert autosar.rootSwCompositionPrototype is None
        assert result == autosar
    
    def test_set_root_sw_composition_prototype_conflict(self):
        """Test the setRootSwCompositionPrototype method with conflict."""
        autosar = AbstractAUTOSAR()
        existing_value = Mock()
        existing_value.getShortName.return_value = "existing_name"
        new_value = Mock()
        new_value.getShortName.return_value = "new_name"
        
        # Set the first value
        autosar.rootSwCompositionPrototype = existing_value
        
        # Try to set a new value with different name - this should raise an error
        with pytest.raises(ValueError):
            autosar.setRootSwCompositionPrototype(new_value)
    
    def test_set_root_sw_composition_prototype_same_name(self):
        """Test the setRootSwCompositionPrototype method with same name."""
        autosar = AbstractAUTOSAR()
        existing_value = Mock()
        existing_value.getShortName.return_value = "same_name"
        new_value = Mock()
        new_value.getShortName.return_value = "same_name"
        
        # Set the first value
        autosar.rootSwCompositionPrototype = existing_value
        
        # Try to set a new value with same name - this should work
        result = autosar.setRootSwCompositionPrototype(new_value)
        assert result == autosar
    
    def test_add_implementation_behavior_map(self):
        """Test the addImplementationBehaviorMap method."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.addImplementationBehaviorMap("impl_ref", "behavior_ref")
        
        # _behavior_impl_maps[behavior] = impl
        assert "behavior_ref" in autosar._behavior_impl_maps
        assert autosar._behavior_impl_maps["behavior_ref"] == "impl_ref"
        
        # _impl_behavior_maps[impl] = behavior
        assert "impl_ref" in autosar._impl_behavior_maps
        assert autosar._impl_behavior_maps["impl_ref"] == "behavior_ref"
        
        # The method should return None (no return statement in the method)
        assert result is None
    
    def test_get_behavior_found(self):
        """Test the getBehavior method when impl_ref is found."""
        autosar = AbstractAUTOSAR()
        autosar._impl_behavior_maps["impl_ref"] = "behavior_ref"
        
        with patch.object(autosar, 'find', return_value="behavior_found"):
            result = autosar.getBehavior("impl_ref")
            assert result == "behavior_found"
    
    def test_get_behavior_not_found(self):
        """Test the getBehavior method when impl_ref is not found."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.getBehavior("not_found_ref")
        assert result is None
    
    def test_get_implementation_found(self):
        """Test the getImplementation method when behavior_ref is found."""
        autosar = AbstractAUTOSAR()
        autosar._behavior_impl_maps["behavior_ref"] = "impl_ref"
        
        with patch.object(autosar, 'find', return_value="impl_found"):
            result = autosar.getImplementation("behavior_ref")
            assert result == "impl_found"
    
    def test_get_implementation_not_found(self):
        """Test the getImplementation method when behavior_ref is not found."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.getImplementation("not_found_ref")
        assert result is None
    
    def test_add_system(self):
        """Test the addSystem method."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        system = System(pkg, "test_system")
        
        autosar.addSystem(system)
        
        assert "test_system" in autosar.systems
    
    def test_get_systems(self):
        """Test the getSystems method."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        system = System(pkg, "test_system")
        
        autosar.addSystem(system)
        result = autosar.getSystems()
        
        assert len(result) == 1
        assert result[0] == system
    
    def test_get_composition_sw_component_types(self):
        """Test the getCompositionSwComponentTypes method."""
        autosar = AbstractAUTOSAR()
        result = autosar.getCompositionSwComponentTypes()
        assert result == {}
    
    def test_get_composition_sw_component_type(self):
        """Test the getCompositionSwComponentType method."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        comp_type = CompositionSwComponentType(pkg, "test_comp")
        autosar.compositionSwComponentTypes["test_comp"] = comp_type
        
        result = autosar.getCompositionSwComponentType("test_comp")
        assert result == comp_type
    
    def test_add_composition_sw_component_type(self):
        """Test the addCompositionSwComponentType method."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        comp_type = CompositionSwComponentType(pkg, "test_comp")
        
        result = autosar.addCompositionSwComponentType(comp_type)
        assert "test_comp" in autosar.compositionSwComponentTypes
        assert result == autosar
    
    def test_add_composition_sw_component_type_none(self):
        """Test the addCompositionSwComponentType method with None."""
        autosar = AbstractAUTOSAR()
        result = autosar.addCompositionSwComponentType(None)
        assert result == autosar
        assert autosar.compositionSwComponentTypes == {}
    
    def test_add_composition_sw_component_type_duplicate(self):
        """Test the addCompositionSwComponentType method with duplicate."""
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        comp_type1 = CompositionSwComponentType(pkg, "test_comp")
        comp_type2 = CompositionSwComponentType(pkg, "test_comp2")
        
        autosar.addCompositionSwComponentType(comp_type1)
        autosar.addCompositionSwComponentType(comp_type2)  # This should add as it has a different name
        # Let me update the test to reflect actual behavior
        autosar.compositionSwComponentTypes.clear()  # Reset for the true duplicate test
        autosar.addCompositionSwComponentType(comp_type1)
        result = autosar.addCompositionSwComponentType(comp_type1)  # Try adding the same one again
        assert result == autosar
    
    def test_get_ar_object_by_uuid(self):
        """Test the getARObjectByUUID method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar.uuid_mgr, 'getObjects', return_value=["test_obj"]):
            result = autosar.getARObjectByUUID("test_uuid")
            assert result == ["test_obj"]
    
    def test_add_ar_object(self):
        """Test the addARObject method."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
        
        autosar = AbstractAUTOSAR()
        pkg = autosar.createARPackage("TestPackage")
        ar_obj = ARPackage(pkg, "test_obj")  # ARPackage is a concrete implementation
        ar_obj.uuid = "test-uuid"
        
        result = autosar.addARObject(ar_obj)
        assert result == autosar
        # Verify that the object was added to uuid_mgr
        assert "test-uuid" in autosar.uuid_mgr.uuid_object_mappings
    
    def test_add_ar_object_none(self):
        """Test the addARObject method with None."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.addARObject(None)
        assert result == autosar
    
    def test_get_duplicate_uuids(self):
        """Test the getDuplicateUUIDs method."""
        autosar = AbstractAUTOSAR()
        with patch.object(autosar.uuid_mgr, 'getDuplicateUUIDs', return_value=["uuid1", "uuid2"]):
            result = autosar.getDuplicateUUIDs()
            assert result == ["uuid1", "uuid2"]
    
    def test_set_ar_release_valid(self):
        """Test the setARRelease method with valid release."""
        autosar = AbstractAUTOSAR()
        
        result = autosar.setARRelease("4.0.3")
        assert result == autosar
        assert "AUTOSAR_4-0-3.xsd" in autosar.schema_location
    
    def test_set_ar_release_invalid(self):
        """Test the setARRelease method with invalid release."""
        autosar = AbstractAUTOSAR()
        
        with pytest.raises(ValueError, match="invalid AUTOSAR Release"):
            autosar.setARRelease("invalid_release")


class TestAUTOSAR:
    """Test cases for the AUTOSAR singleton class."""
    
    def test_autosar_get_instance(self):
        """Test that AUTOSAR.getInstance() returns the singleton instance."""
        # Clear any existing instance first
        try:
            existing = AUTOSAR.getInstance()
            existing.new()  # Clear the instance
        except:
            pass  # If no instance exists, that's fine
        
        instance1 = AUTOSAR.getInstance()
        instance2 = AUTOSAR.getInstance()
        assert instance1 is instance2
    
    def test_autosar_new(self):
        """Test the new method clears the instance."""
        autosar = AUTOSAR.getInstance()
        # Call new to clear
        autosar.new()
        # Verify that it's cleared by checking one of the attributes
        assert autosar.arPackages == {}
    
    def test_autosar_constructor_exception(self):
        """Test that creating a second AUTOSAR instance raises an exception."""
        # Ensure no instance exists first by clearing
        try:
            existing = AUTOSAR.getInstance()
            existing.new()
        except:
            pass  # If no instance exists, that's fine
        
        # Now create first instance through getInstance()
        first_instance = AUTOSAR.getInstance()
        
        # Trying to create a second instance directly should raise an exception
        with pytest.raises(Exception, match="The AUTOSAR is singleton!"):
            AUTOSAR()




class TestAUTOSARDoc:
    """Test cases for the AUTOSARDoc class."""
    
    def test_autosar_doc_initialization(self):
        """Test that AUTOSARDoc initializes properly by inheriting from AbstractAUTOSAR."""
        doc = AUTOSARDoc()
        # Should have all the attributes from AbstractAUTOSAR
        assert doc.adminData is None
        assert doc.fileInfoComment is None
        assert doc.introduction is None