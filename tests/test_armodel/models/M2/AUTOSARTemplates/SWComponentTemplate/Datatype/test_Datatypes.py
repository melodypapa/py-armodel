"""
This module contains comprehensive tests for the Datatypes module in SWComponentTemplate.Datatype.
Tests cover all classes and methods in the Datatypes.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    AutosarDataType, ApplicationDataType, ApplicationPrimitiveDataType,
    ApplicationCompositeDataType, ApplicationArrayDataType, ApplicationRecordDataType,
    DataTypeMap, DataTypeMappingSet
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestAutosarDataType:
    """Test class for AutosarDataType abstract class."""
    
    def test_autosar_data_type_abstract(self):
        """Test that AutosarDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AutosarDataType(ar_root, "TestAutosarDataType")


class TestApplicationDataType:
    """Test class for ApplicationDataType abstract class."""
    
    def test_application_data_type_abstract(self):
        """Test that ApplicationDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationDataType(ar_root, "TestApplicationDataType")


class TestApplicationPrimitiveDataType:
    """Test class for ApplicationPrimitiveDataType class."""
    
    def test_application_primitive_data_type_initialization(self):
        """Test ApplicationPrimitiveDataType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive_type = ApplicationPrimitiveDataType(ar_root, "TestApplicationPrimitiveDataType")
        
        assert primitive_type.parent == ar_root
        assert primitive_type.short_name == "TestApplicationPrimitiveDataType"
        assert primitive_type.swDataDefProps is None
        
        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        primitive_type.setSwDataDefProps(sw_data_def)
        assert primitive_type.getSwDataDefProps() == sw_data_def


class TestApplicationCompositeDataType:
    """Test class for ApplicationCompositeDataType abstract class."""
    
    def test_application_composite_data_type_abstract(self):
        """Test that ApplicationCompositeDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationCompositeDataType(ar_root, "TestApplicationCompositeDataType")


class TestApplicationArrayDataType:
    """Test class for ApplicationArrayDataType class."""
    
    def test_application_array_data_type_initialization(self):
        """Test ApplicationArrayDataType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_type = ApplicationArrayDataType(ar_root, "TestApplicationArrayDataType")
        
        assert array_type.parent == ar_root
        assert array_type.short_name == "TestApplicationArrayDataType"
        assert array_type.swDataDefProps is None
        assert array_type.dynamicArraySizeProfile is None
        assert array_type.element is None
        
        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        array_type.setSwDataDefProps(sw_data_def)
        assert array_type.getSwDataDefProps() == sw_data_def
        
        # Test dynamicArraySizeProfile methods
        profile = "test_profile"
        array_type.setDynamicArraySizeProfile(profile)
        assert array_type.getDynamicArraySizeProfile() == profile
        
        # Test createApplicationArrayElement and related methods
        array_element = array_type.createApplicationArrayElement("TestArrayElement")
        assert array_element is not None
        assert array_element.short_name == "TestArrayElement"
        assert array_element.parent == array_type
        assert array_type.element == array_element


class TestApplicationRecordDataType:
    """Test class for ApplicationRecordDataType class."""
    
    def test_application_record_data_type_initialization(self):
        """Test ApplicationRecordDataType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")
        
        assert record_type.parent == ar_root
        assert record_type.short_name == "TestApplicationRecordDataType"
        assert record_type.swDataDefProps is None
        assert record_type.record_elements == []
        
        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        record_type.setSwDataDefProps(sw_data_def)
        assert record_type.getSwDataDefProps() == sw_data_def
        
        # Test createApplicationRecordElement and related methods
        record_element = record_type.createApplicationRecordElement("TestRecordElement")
        assert record_element is not None
        assert record_element.short_name == "TestRecordElement"
        assert record_element.parent == record_type
        assert record_element in record_type.getApplicationRecordElements()


class TestDataTypeMap:
    """Test class for DataTypeMap class."""
    
    def test_data_type_map_initialization(self):
        """Test DataTypeMap initialization and methods."""
        data_type_map = DataTypeMap()
        
        assert data_type_map.applicationDataTypeRef is None
        assert data_type_map.implementationDataTypeRef is None
        
        # Test applicationDataTypeRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        app_ref = RefType()
        app_ref.setValue("/Application/Type")
        data_type_map.setApplicationDataTypeRef(app_ref)
        assert data_type_map.getApplicationDataTypeRef() == app_ref
        
        # Test implementationDataTypeRef methods
        impl_ref = RefType()
        impl_ref.setValue("/Implementation/Type")
        data_type_map.setImplementationDataTypeRef(impl_ref)
        assert data_type_map.getImplementationDataTypeRef() == impl_ref


class TestDataTypeMappingSet:
    """Test class for DataTypeMappingSet class."""
    
    def test_data_type_mapping_set_initialization(self):
        """Test DataTypeMappingSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping_set = DataTypeMappingSet(ar_root, "TestDataTypeMappingSet")
        
        assert mapping_set.parent == ar_root
        assert mapping_set.short_name == "TestDataTypeMappingSet"
        assert mapping_set.dataTypeMaps == []
        assert mapping_set.modeRequestTypeMaps == []
        
        # Test DataTypeMap methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap
        data_map = DataTypeMap()
        mapping_set.addDataTypeMap(data_map)
        assert data_map in mapping_set.getDataTypeMaps()
        
        # Test ModeRequestTypeMap methods (import and test)
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
        mode_map = ModeRequestTypeMap()
        mapping_set.addModeRequestTypeMap(mode_map)
        assert mode_map in mapping_set.getModeRequestTypeMaps()