"""
This module contains comprehensive tests for the PortInterface module in SWComponentTemplate.
Tests cover all classes and methods in the PortInterface module files to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
    ApplicationCompositeElementInPortInterfaceInstanceRef
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    InvalidationPolicy, MetaDataItem,
    MetaDataItemSet, TriggerInterface, ModeSwitchInterface, PortInterfaceMapping,
    ClientServerApplicationErrorMapping, ClientServerOperationMapping, DataPrototypeMapping,
    ClientServerInterfaceMapping, VariableAndParameterInterfaceMapping, ModeInterfaceMapping,
    TriggerInterfaceMapping, ModeDeclarationMapping, ModeDeclarationMappingSet,
    PortInterfaceMappingSet, TextTableMapping
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType, ARLiteral, PositiveInteger, ARBoolean
)


class TestApplicationCompositeElementInPortInterfaceInstanceRef:
    """Test class for ApplicationCompositeElementInPortInterfaceInstanceRef class."""
    
    def test_application_composite_element_in_port_interface_instance_ref_initialization(self):
        """Test ApplicationCompositeElementInPortInterfaceInstanceRef initialization and methods."""
        instance_ref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        assert instance_ref.baseRef is None
        assert instance_ref.contextDataPrototypeRef is None
        assert instance_ref.rootDataPrototypeRef is None
        assert instance_ref.targetDataPrototypeRef is None
        
        # Test setters and getters
        base_ref = RefType()
        base_ref.setValue("/Test/Base")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref
        
        context_ref = RefType()
        context_ref.setValue("/Test/Context")
        instance_ref.setContextDataPrototypeRef(context_ref)
        assert instance_ref.getContextDataPrototypeRef() == context_ref
        
        root_ref = RefType()
        root_ref.setValue("/Test/Root")
        instance_ref.setRootDataPrototypeRef(root_ref)
        assert instance_ref.getRootDataPrototypeRef() == root_ref
        
        target_ref = RefType()
        target_ref.setValue("/Test/Target")
        instance_ref.setTargetDataPrototypeRef(target_ref)
        assert instance_ref.getTargetDataPrototypeRef() == target_ref


class TestInvalidationPolicy:
    """Test class for InvalidationPolicy class."""
    
    def test_invalidation_policy_initialization(self):
        """Test InvalidationPolicy initialization and methods."""
        policy = InvalidationPolicy()
        assert policy.dataElementRef is None
        assert policy.handleInvalid is None
        
        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/DataElement")
        policy.setDataElementRef(ref)
        assert policy.getDataElementRef() == ref
        
        literal = ARLiteral()
        literal.setValue("test_handle")
        policy.setHandleInvalid(literal)
        assert policy.getHandleInvalid() == literal


class TestMetaDataItem:
    """Test class for MetaDataItem class."""
    
    def test_meta_data_item_initialization(self):
        """Test MetaDataItem initialization and methods."""
        item = MetaDataItem()
        assert item.length is None
        assert item.metaDataItemType is None
        
        # Test setters and getters
        length = PositiveInteger()
        length.setValue(10)
        item.setLength(length)
        assert item.getLength() == length
        
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
        text_spec = TextValueSpecification()
        item.setMetaDataItemType(text_spec)
        assert item.getMetaDataItemType() == text_spec


class TestMetaDataItemSet:
    """Test class for MetaDataItemSet class."""
    
    def test_meta_data_item_set_initialization(self):
        """Test MetaDataItemSet initialization and methods."""
        item_set = MetaDataItemSet()
        assert item_set.dataElementRefs == []
        assert item_set.metaDataItems == []
        
        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/DataElement")
        item_set.addDataElementRef(ref)
        assert ref in item_set.getDataElementRefs()
        
        meta_item = MetaDataItem()
        item_set.addMetaDataItem(meta_item)
        assert meta_item in item_set.getMetaDataItems()


class TestTriggerInterface:
    """Test class for TriggerInterface class."""
    
    def test_trigger_interface_initialization(self):
        """Test TriggerInterface initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_interface = TriggerInterface(ar_root, "TestTriggerInterface")
        
        assert trigger_interface._triggers == []
        assert trigger_interface.parent == ar_root
        assert trigger_interface.short_name == "TestTriggerInterface"


class TestModeSwitchInterface:
    """Test class for ModeSwitchInterface class."""
    
    def test_mode_switch_interface_initialization(self):
        """Test ModeSwitchInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_switch_interface = ModeSwitchInterface(ar_root, "TestModeSwitchInterface")
        
        assert mode_switch_interface._modeGroup == []
        assert mode_switch_interface.parent == ar_root
        assert mode_switch_interface.short_name == "TestModeSwitchInterface"
        
        # Test createModeGroup and getModeGroups
        mode_group = mode_switch_interface.createModeGroup("TestModeGroup")
        assert mode_group is not None
        assert len(mode_switch_interface.getModeGroups()) == 1


class TestPortInterfaceMapping:
    """Test class for PortInterfaceMapping abstract class."""
    
    def test_port_interface_mapping_abstract(self):
        """Test that PortInterfaceMapping is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        
        # Create a concrete implementation to test the abstract class
        class TestPortInterfaceMapping(PortInterfaceMapping):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        test_mapping = TestPortInterfaceMapping(ar_root, "TestPortInterfaceMapping")
        assert test_mapping is not None
        assert test_mapping.short_name == "TestPortInterfaceMapping"
        
        # Test that the original abstract class raises NotImplementedError
        with pytest.raises(NotImplementedError):
            PortInterfaceMapping(ar_root, "Test")


class TestClientServerApplicationErrorMapping:
    """Test class for ClientServerApplicationErrorMapping class."""
    
    def test_client_server_application_error_mapping_initialization(self):
        """Test ClientServerApplicationErrorMapping initialization and methods."""
        mapping = ClientServerApplicationErrorMapping()
        assert mapping.firstApplicationErrorRef is None
        assert mapping.secondApplicationErrorRef is None
        
        # Test setters and getters
        first_ref = RefType()
        first_ref.setValue("/Test/FirstError")
        mapping.setFirstApplicationErrorRef(first_ref)
        assert mapping.getFirstApplicationErrorRef() == first_ref
        
        second_ref = RefType()
        second_ref.setValue("/Test/SecondError")
        mapping.setSecondApplicationErrorRef(second_ref)
        assert mapping.getSecondApplicationErrorRef() == second_ref


class TestClientServerOperationMapping:
    """Test class for ClientServerOperationMapping class."""
    
    def test_client_server_operation_mapping_initialization(self):
        """Test ClientServerOperationMapping initialization and methods."""
        mapping = ClientServerOperationMapping()
        assert mapping.argumentMappings == []
        assert mapping.firstOperationRef is None
        assert mapping.firstToSecondDataTransformationRef is None
        assert mapping.secondOperationRef is None
        
        # Test setters and getters
        first_ref = RefType()
        first_ref.setValue("/Test/FirstOperation")
        mapping.setFirstOperationRef(first_ref)
        assert mapping.getFirstOperationRef() == first_ref
        
        second_ref = RefType()
        second_ref.setValue("/Test/SecondOperation")
        mapping.setSecondOperationRef(second_ref)
        assert mapping.getSecondOperationRef() == second_ref
        
        data_mapping = DataPrototypeMapping()
        mapping.addArgumentMapping(data_mapping)
        assert data_mapping in mapping.getArgumentMappings()


class TestDataPrototypeMapping:
    """Test class for DataPrototypeMapping class."""
    
    def test_data_prototype_mapping_initialization(self):
        """Test DataPrototypeMapping initialization and methods."""
        mapping = DataPrototypeMapping()
        assert mapping.firstDataPrototypeRef is None
        assert mapping.firstToSecondDataTransformationRef is None
        assert mapping.secondDataPrototypeRef is None
        assert mapping.secondToFirstDataTransformationRef is None
        assert mapping.subElementMappings == []
        assert mapping.textTableMappings == []
        
        # Test setters and getters
        first_ref = RefType()
        first_ref.setValue("/Test/FirstData")
        mapping.setFirstDataPrototypeRef(first_ref)
        assert mapping.getFirstDataPrototypeRef() == first_ref
        
        second_ref = RefType()
        second_ref.setValue("/Test/SecondData")
        mapping.setSecondDataPrototypeRef(second_ref)
        assert mapping.getSecondDataPrototypeRef() == second_ref


class TestClientServerInterfaceMapping:
    """Test class for ClientServerInterfaceMapping class."""
    
    def test_client_server_interface_mapping_initialization(self):
        """Test ClientServerInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ClientServerInterfaceMapping(ar_root, "TestClientServerInterfaceMapping")
        
        assert mapping.errorMappings == []
        assert mapping.operationMappings == []
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestClientServerInterfaceMapping"
        
        # Test setters and getters
        error_mapping = ClientServerApplicationErrorMapping()
        mapping.addErrorMapping(error_mapping)
        assert error_mapping in mapping.getErrorMappings()
        
        operation_mapping = ClientServerOperationMapping()
        mapping.addOperationMapping(operation_mapping)
        assert operation_mapping in mapping.getOperationMappings()


class TestVariableAndParameterInterfaceMapping:
    """Test class for VariableAndParameterInterfaceMapping class."""
    
    def test_variable_and_parameter_interface_mapping_initialization(self):
        """Test VariableAndParameterInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = VariableAndParameterInterfaceMapping(ar_root, "TestVariableAndParameterInterfaceMapping")
        
        assert mapping.dataMappings == []
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestVariableAndParameterInterfaceMapping"
        
        # Test setters and getters
        data_mapping = DataPrototypeMapping()
        mapping.addDataMapping(data_mapping)
        assert data_mapping in mapping.getDataMappings()


class TestModeInterfaceMapping:
    """Test class for ModeInterfaceMapping class."""
    
    def test_mode_interface_mapping_initialization(self):
        """Test ModeInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ModeInterfaceMapping(ar_root, "TestModeInterfaceMapping")
        
        assert mapping.modeMapping is None
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestModeInterfaceMapping"
        
        # Test setter and getter - create a mock mapping object for testing
        class MockModeDeclarationGroupPrototypeMapping:
            def __init__(self):
                pass
        
        mode_mapping = MockModeDeclarationGroupPrototypeMapping()
        mapping.setModeMapping(mode_mapping)
        assert mapping.getModeMapping() == mode_mapping


class TestTriggerInterfaceMapping:
    """Test class for TriggerInterfaceMapping class."""
    
    def test_trigger_interface_mapping_initialization(self):
        """Test TriggerInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = TriggerInterfaceMapping(ar_root, "TestTriggerInterfaceMapping")
        
        assert mapping.triggerMapping == []
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestTriggerInterfaceMapping"
        
        # Test setter and getter
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
        trigger_mapping = TriggerMapping()
        mapping.setTriggerMapping([trigger_mapping])
        assert trigger_mapping in mapping.getTriggerMapping()


class TestModeDeclarationMapping:
    """Test class for ModeDeclarationMapping class."""
    
    def test_mode_declaration_mapping_initialization(self):
        """Test ModeDeclarationMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ModeDeclarationMapping(ar_root, "TestModeDeclarationMapping")
        
        assert mapping.getFirstModeRefs() == []
        assert mapping.getSecondModeRef() == []
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestModeDeclarationMapping"
        
        # Test setters and getters
        first_ref = RefType()
        first_ref.setValue("/Test/FirstMode")
        mapping.addFirstModeRef(first_ref)  # Fixed to take single ref, not list
        assert first_ref in mapping.getFirstModeRefs()
        
        second_ref = RefType()
        second_ref.setValue("/Test/SecondMode")
        mapping.setSecondModeRef(second_ref)  # Fixed to take single ref, not list
        assert second_ref == mapping.getSecondModeRef()


class TestModeDeclarationMappingSet:
    """Test class for ModeDeclarationMappingSet class."""
    
    def test_mode_declaration_mapping_set_initialization(self):
        """Test ModeDeclarationMappingSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping_set = ModeDeclarationMappingSet(ar_root, "TestModeDeclarationMappingSet")
        
        assert mapping_set.getModeDeclarationMappings() == []
        assert mapping_set.parent == ar_root
        assert mapping_set.short_name == "TestModeDeclarationMappingSet"
        
        # Test createModeDeclarationMapping
        mode_mapping = mapping_set.createModeDeclarationMapping("TestMapping")
        assert mode_mapping is not None
        assert len(mapping_set.getModeDeclarationMappings()) == 1


class TestPortInterfaceMappingSet:
    """Test class for PortInterfaceMappingSet class."""
    
    def test_port_interface_mapping_set_initialization(self):
        """Test PortInterfaceMappingSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping_set = PortInterfaceMappingSet(ar_root, "TestPortInterfaceMappingSet")
        
        assert mapping_set.getPortInterfaceMappings() == []
        assert mapping_set.parent == ar_root
        assert mapping_set.short_name == "TestPortInterfaceMappingSet"
        
        # Test creating different types of mappings
        var_param_mapping = mapping_set.createVariableAndParameterInterfaceMapping("VarParamMapping")
        assert var_param_mapping is not None
        
        cs_mapping = mapping_set.createClientServerInterfaceMapping("CSMapping")
        assert cs_mapping is not None
        
        mode_mapping = mapping_set.createModeInterfaceMapping("ModeMapping")
        assert mode_mapping is not None
        
        trigger_mapping = mapping_set.createTriggerInterfaceMapping("TriggerMapping")
        assert trigger_mapping is not None
        
        assert len(mapping_set.getPortInterfaceMappings()) == 4


class TestTextTableMapping:
    """Test class for TextTableMapping class."""
    
    def test_text_table_mapping_initialization(self):
        """Test TextTableMapping initialization and methods."""
        mapping = TextTableMapping()
        assert mapping.bitfieldTextTableMaskFirst is None
        assert mapping.bitfieldTextTableMaskSecond is None
        assert mapping.identicalMapping is None
        assert mapping.mappingDirection is None
        assert mapping.valuePairs == []
        
        # Test setters and getters
        first_mask = PositiveInteger()
        first_mask.setValue(15)
        mapping.setBitfieldTextTableMaskFirst(first_mask)
        assert mapping.getBitfieldTextTableMaskFirst() == first_mask
        
        second_mask = PositiveInteger()
        second_mask.setValue(31)
        mapping.setBitfieldTextTableMaskSecond(second_mask)
        assert mapping.getBitfieldTextTableMaskSecond() == second_mask
        
        identical = ARBoolean()
        identical.setValue(True)
        mapping.setIdenticalMapping(identical)
        assert mapping.getIdenticalMapping() == identical