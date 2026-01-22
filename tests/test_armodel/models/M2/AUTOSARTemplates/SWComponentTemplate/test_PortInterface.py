"""
This module contains comprehensive tests for the PortInterface module in SWComponentTemplate.
Tests cover all classes and methods in the __init__.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterface, DataInterface, NvDataInterface, ParameterInterface, InvalidationPolicy,
    MetaDataItem, MetaDataItemSet, SenderReceiverInterface, ArgumentDataPrototype,
    ApplicationError, ClientServerOperation, ClientServerInterface, TriggerInterface,
    ModeSwitchInterface, PortInterfaceMapping, ClientServerApplicationErrorMapping,
    ClientServerOperationMapping, DataPrototypeMapping, ClientServerInterfaceMapping,
    VariableAndParameterInterfaceMapping, ModeInterfaceMapping, TriggerInterfaceMapping,
    ModeDeclarationMapping, ModeDeclarationMappingSet, PortInterfaceMappingSet,
    TextTableMapping
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestPortInterface:
    """Test class for PortInterface abstract class."""
    
    def test_port_interface_initialization(self):
        """Test PortInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            PortInterface(ar_root, "TestPortInterface")


class TestDataInterface:
    """Test class for DataInterface abstract class."""
    
    def test_data_interface_initialization(self):
        """Test DataInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            DataInterface(ar_root, "TestDataInterface")


class TestNvDataInterface:
    """Test class for NvDataInterface class."""
    
    def test_nv_data_interface_initialization(self):
        """Test NvDataInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        nv_interface = NvDataInterface(ar_root, "TestNvDataInterface")
        
        assert nv_interface.parent == ar_root
        assert nv_interface.short_name == "TestNvDataInterface"
        assert nv_interface.isService is None
        assert nv_interface.serviceKind is None
        assert nv_interface.nvDatas == []
        
        # Test nvDatas methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
        var_data = VariableDataPrototype(ar_root, "TestVarData")
        nv_interface.setNvData(var_data)
        assert var_data in nv_interface.getNvDatas()


class TestParameterInterface:
    """Test class for ParameterInterface class."""
    
    def test_parameter_interface_initialization(self):
        """Test ParameterInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_interface = ParameterInterface(ar_root, "TestParameterInterface")
        
        assert param_interface.parent == ar_root
        assert param_interface.short_name == "TestParameterInterface"
        assert param_interface.isService is None
        assert param_interface.serviceKind is None
        assert param_interface.parameters == []
        
        # Test parameters methods
        param_data = param_interface.createParameterDataPrototype("TestParamData")
        assert param_data is not None
        assert param_data.short_name == "TestParamData"
        assert param_data in param_interface.getParameters()


class TestInvalidationPolicy:
    """Test class for InvalidationPolicy class."""
    
    def test_invalidation_policy_initialization(self):
        """Test InvalidationPolicy initialization and methods."""
        policy = InvalidationPolicy()
        
        assert policy.dataElementRef is None
        assert policy.handleInvalid is None
        
        # Test dataElementRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        ref = RefType()
        ref.setValue("/Data/Element/Ref")
        policy.setDataElementRef(ref)
        assert policy.getDataElementRef() == ref
        
        # Test handleInvalid methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        handle = ARLiteral()
        handle.setValue("test_handle")
        policy.setHandleInvalid(handle)
        assert policy.getHandleInvalid() == handle


class TestMetaDataItem:
    """Test class for MetaDataItem class."""
    
    def test_meta_data_item_initialization(self):
        """Test MetaDataItem initialization and methods."""
        item = MetaDataItem()
        
        assert item.length is None
        assert item.metaDataItemType is None
        
        # Test length methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
        length = PositiveInteger()
        length.setValue(10)
        item.setLength(length)
        assert item.getLength() == length
        
        # Test metaDataItemType methods
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
        
        # Test dataElementRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        ref = RefType()
        ref.setValue("/Data/Element/Ref")
        item_set.addDataElementRef(ref)
        assert ref in item_set.getDataElementRefs()
        
        # Test metaDataItems methods
        meta_item = MetaDataItem()
        item_set.addMetaDataItem(meta_item)
        assert meta_item in item_set.getMetaDataItems()


class TestSenderReceiverInterface:
    """Test class for SenderReceiverInterface class."""
    
    def test_sender_receiver_interface_initialization(self):
        """Test SenderReceiverInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sr_interface = SenderReceiverInterface(ar_root, "TestSenderReceiverInterface")
        
        assert sr_interface.parent == ar_root
        assert sr_interface.short_name == "TestSenderReceiverInterface"
        assert sr_interface.isService is None
        assert sr_interface.serviceKind is None
        assert sr_interface.invalidationPolicies == []
        assert sr_interface.metaDataItemSets == []
        
        # Test invalidationPolicies methods
        policy = InvalidationPolicy()
        sr_interface.addInvalidationPolicy(policy)
        assert policy in sr_interface.getInvalidationPolicies()
        
        # Test metaDataItemSets methods
        meta_set = MetaDataItemSet()
        sr_interface.addMetaDataItemSet(meta_set)
        assert meta_set in sr_interface.getMetaDataItemSets()
        
        # Test dataElement methods
        data_element = sr_interface.createDataElement("TestDataElement")
        assert data_element is not None
        assert data_element.short_name == "TestDataElement"
        assert data_element in sr_interface.getDataElements()
        
        # Test invalidation policy creation
        policy_created = sr_interface.createInvalidationPolicy()
        assert policy_created is not None
        assert policy_created in sr_interface.getInvalidationPolicys()


class TestArgumentDataPrototype:
    """Test class for ArgumentDataPrototype class."""
    
    def test_argument_data_prototype_initialization(self):
        """Test ArgumentDataPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        arg_proto = ArgumentDataPrototype(ar_root, "TestArgumentDataPrototype")
        
        assert arg_proto.parent == ar_root
        assert arg_proto.short_name == "TestArgumentDataPrototype"
        assert arg_proto.direction is None
        assert arg_proto.serverArgumentImplPolicy is None
        
        # Test direction methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ArgumentDirectionEnum
        direction = ArgumentDirectionEnum()
        direction.setValue("IN")
        arg_proto.setDirection(direction)
        assert arg_proto.getDirection() == direction
        
        # Test serverArgumentImplPolicy methods
        policy = "test_policy"
        arg_proto.setServerArgumentImplPolicy(policy)
        assert arg_proto.getServerArgumentImplPolicy() == policy


class TestApplicationError:
    """Test class for ApplicationError class."""
    
    def test_application_error_initialization(self):
        """Test ApplicationError initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        app_error = ApplicationError(ar_root, "TestApplicationError")
        
        assert app_error.parent == ar_root
        assert app_error.short_name == "TestApplicationError"
        assert app_error.error_code is None


class TestClientServerOperation:
    """Test class for ClientServerOperation class."""
    
    def test_client_server_operation_initialization(self):
        """Test ClientServerOperation initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        operation = ClientServerOperation(ar_root, "TestClientServerOperation")
        
        assert operation.parent == ar_root
        assert operation.short_name == "TestClientServerOperation"
        assert operation.arguments == []
        assert operation.possibleErrorRefs == []
        
        # Test arguments methods
        arg_proto = operation.createArgumentDataPrototype("TestArg")
        assert arg_proto is not None
        assert arg_proto in operation.getArguments()
        
        # Test possibleErrorRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        ref = RefType()
        ref.setValue("/Error/Ref")
        operation.addPossibleErrorRef(ref)
        assert ref in operation.getPossibleErrorRefs()


class TestClientServerInterface:
    """Test class for ClientServerInterface class."""
    
    def test_client_server_interface_initialization(self):
        """Test ClientServerInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        cs_interface = ClientServerInterface(ar_root, "TestClientServerInterface")
        
        assert cs_interface.parent == ar_root
        assert cs_interface.short_name == "TestClientServerInterface"
        assert cs_interface.isService is None
        assert cs_interface.serviceKind is None
        
        # Test operation methods
        operation = cs_interface.createOperation("TestOperation")
        assert operation is not None
        assert operation.short_name == "TestOperation"
        assert operation in cs_interface.getOperations()
        
        # Test application error methods
        app_error = cs_interface.createApplicationError("TestAppError")
        assert app_error is not None
        assert app_error.short_name == "TestAppError"
        assert app_error in cs_interface.getPossibleErrors()


class TestTriggerInterface:
    """Test class for TriggerInterface class."""
    
    def test_trigger_interface_initialization(self):
        """Test TriggerInterface initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_interface = TriggerInterface(ar_root, "TestTriggerInterface")
        
        assert trigger_interface.parent == ar_root
        assert trigger_interface.short_name == "TestTriggerInterface"
        assert trigger_interface.isService is None
        assert trigger_interface.serviceKind is None
        assert trigger_interface._triggers == []


class TestModeSwitchInterface:
    """Test class for ModeSwitchInterface class."""
    
    def test_mode_switch_interface_initialization(self):
        """Test ModeSwitchInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_interface = ModeSwitchInterface(ar_root, "TestModeSwitchInterface")
        
        assert mode_interface.parent == ar_root
        assert mode_interface.short_name == "TestModeSwitchInterface"
        assert mode_interface.isService is None
        assert mode_interface.serviceKind is None
        assert mode_interface._modeGroup == []
        
        # Test mode group methods
        mode_group = mode_interface.createModeGroup("TestModeGroup")
        assert mode_group is not None
        assert mode_group.short_name == "TestModeGroup"
        assert mode_group in mode_interface.getModeGroups()


class TestPortInterfaceMapping:
    """Test class for PortInterfaceMapping abstract class."""
    
    def test_port_interface_mapping_initialization(self):
        """Test PortInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            PortInterfaceMapping(ar_root, "TestPortInterfaceMapping")


class TestClientServerApplicationErrorMapping:
    """Test class for ClientServerApplicationErrorMapping class."""
    
    def test_client_server_application_error_mapping_initialization(self):
        """Test ClientServerApplicationErrorMapping initialization and methods."""
        error_mapping = ClientServerApplicationErrorMapping()
        
        assert error_mapping.firstApplicationErrorRef is None
        assert error_mapping.secondApplicationErrorRef is None
        
        # Test firstApplicationErrorRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        first_ref = RefType()
        first_ref.setValue("/First/Error/Ref")
        error_mapping.setFirstApplicationErrorRef(first_ref)
        assert error_mapping.getFirstApplicationErrorRef() == first_ref
        
        # Test secondApplicationErrorRef methods
        second_ref = RefType()
        second_ref.setValue("/Second/Error/Ref")
        error_mapping.setSecondApplicationErrorRef(second_ref)
        assert error_mapping.getSecondApplicationErrorRef() == second_ref


class TestClientServerOperationMapping:
    """Test class for ClientServerOperationMapping class."""
    
    def test_client_server_operation_mapping_initialization(self):
        """Test ClientServerOperationMapping initialization and methods."""
        op_mapping = ClientServerOperationMapping()
        
        assert op_mapping.argumentMappings == []
        assert op_mapping.firstOperationRef is None
        assert op_mapping.firstToSecondDataTransformationRef is None
        assert op_mapping.secondOperationRef is None
        
        # Test argumentMappings methods
        data_mapping = DataPrototypeMapping()
        op_mapping.addArgumentMapping(data_mapping)
        assert data_mapping in op_mapping.getArgumentMappings()
        
        # Test firstOperationRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        first_ref = RefType()
        first_ref.setValue("/First/Op/Ref")
        op_mapping.setFirstOperationRef(first_ref)
        assert op_mapping.getFirstOperationRef() == first_ref
        
        # Test firstToSecondDataTransformationRef methods
        transform_ref = RefType()
        transform_ref.setValue("/Transform/Ref")
        op_mapping.setFirstToSecondDataTransformationRef(transform_ref)
        assert op_mapping.getFirstToSecondDataTransformationRef() == transform_ref
        
        # Test secondOperationRef methods
        second_ref = RefType()
        second_ref.setValue("/Second/Op/Ref")
        op_mapping.setSecondOperationRef(second_ref)
        assert op_mapping.getSecondOperationRef() == second_ref


class TestDataPrototypeMapping:
    """Test class for DataPrototypeMapping class."""
    
    def test_data_prototype_mapping_initialization(self):
        """Test DataPrototypeMapping initialization and methods."""
        data_mapping = DataPrototypeMapping()
        
        assert data_mapping.firstDataPrototypeRef is None
        assert data_mapping.firstToSecondDataTransformationRef is None
        assert data_mapping.secondDataPrototypeRef is None
        assert data_mapping.secondToFirstDataTransformationRef is None
        assert data_mapping.subElementMappings == []
        assert data_mapping.textTableMappings == []
        
        # Test firstDataPrototypeRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        first_ref = RefType()
        first_ref.setValue("/First/Data/Ref")
        data_mapping.setFirstDataPrototypeRef(first_ref)
        assert data_mapping.getFirstDataPrototypeRef() == first_ref
        
        # Test firstToSecondDataTransformationRef methods
        transform_ref = RefType()
        transform_ref.setValue("/Transform/Ref")
        data_mapping.setFirstToSecondDataTransformationRef(transform_ref)
        assert data_mapping.getFirstToSecondDataTransformationRef() == transform_ref
        
        # Test secondDataPrototypeRef methods
        second_ref = RefType()
        second_ref.setValue("/Second/Data/Ref")
        data_mapping.setSecondDataPrototypeRef(second_ref)
        assert data_mapping.getSecondDataPrototypeRef() == second_ref
        
        # Test secondToFirstDataTransformationRef methods
        second_transform_ref = RefType()
        second_transform_ref.setValue("/Second/Transform/Ref")
        data_mapping.setSecondToFirstDataTransformationRef(second_transform_ref)
        assert data_mapping.getSecondToFirstDataTransformationRef() == second_transform_ref
        
        # Test subElementMappings methods
        sub_element = "test_sub_element"
        data_mapping.setSubElementMappings(sub_element)
        assert data_mapping.getSubElementMappings() == sub_element
        
        # Test textTableMappings methods
        text_table_mapping = TextTableMapping()
        data_mapping.setTextTableMappings([text_table_mapping])
        assert text_table_mapping in data_mapping.getTextTableMappings()


class TestClientServerInterfaceMapping:
    """Test class for ClientServerInterfaceMapping class."""
    
    def test_client_server_interface_mapping_initialization(self):
        """Test ClientServerInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        cs_mapping = ClientServerInterfaceMapping(ar_root, "TestClientServerInterfaceMapping")
        
        assert cs_mapping.parent == ar_root
        assert cs_mapping.short_name == "TestClientServerInterfaceMapping"
        assert cs_mapping.errorMappings == []
        assert cs_mapping.operationMappings == []
        
        # Test errorMappings methods
        error_mapping = ClientServerApplicationErrorMapping()
        cs_mapping.addErrorMapping(error_mapping)
        assert error_mapping in cs_mapping.getErrorMappings()
        
        # Test operationMappings methods
        op_mapping = ClientServerOperationMapping()
        cs_mapping.addOperationMapping(op_mapping)
        assert op_mapping in cs_mapping.getOperationMappings()


class TestVariableAndParameterInterfaceMapping:
    """Test class for VariableAndParameterInterfaceMapping class."""
    
    def test_variable_and_parameter_interface_mapping_initialization(self):
        """Test VariableAndParameterInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        vp_mapping = VariableAndParameterInterfaceMapping(ar_root, "TestVariableAndParameterInterfaceMapping")
        
        assert vp_mapping.parent == ar_root
        assert vp_mapping.short_name == "TestVariableAndParameterInterfaceMapping"
        assert vp_mapping.dataMappings == []
        
        # Test dataMappings methods
        data_mapping = DataPrototypeMapping()
        vp_mapping.addDataMapping(data_mapping)
        assert data_mapping in vp_mapping.getDataMappings()


class TestModeInterfaceMapping:
    """Test class for ModeInterfaceMapping class."""
    
    def test_mode_interface_mapping_initialization(self):
        """Test ModeInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_mapping = ModeInterfaceMapping(ar_root, "TestModeInterfaceMapping")
        
        assert mode_mapping.parent == ar_root
        assert mode_mapping.short_name == "TestModeInterfaceMapping"
        assert mode_mapping.modeMapping is None
        
        # Test modeMapping methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototypeMapping
        mode_group_mapping = ModeDeclarationGroupPrototypeMapping()
        mode_mapping.setModeMapping(mode_group_mapping)
        assert mode_mapping.getModeMapping() == mode_group_mapping


class TestTriggerInterfaceMapping:
    """Test class for TriggerInterfaceMapping class."""
    
    def test_trigger_interface_mapping_initialization(self):
        """Test TriggerInterfaceMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_mapping = TriggerInterfaceMapping(ar_root, "TestTriggerInterfaceMapping")
        
        assert trigger_mapping.parent == ar_root
        assert trigger_mapping.short_name == "TestTriggerInterfaceMapping"
        assert trigger_mapping.triggerMapping == []
        
        # Test triggerMapping methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
        trigger_map = TriggerMapping()
        trigger_mapping.setTriggerMapping([trigger_map])
        assert trigger_map in trigger_mapping.getTriggerMapping()


class TestModeDeclarationMapping:
    """Test class for ModeDeclarationMapping class."""
    
    def test_mode_declaration_mapping_initialization(self):
        """Test ModeDeclarationMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_decl_mapping = ModeDeclarationMapping(ar_root, "TestModeDeclarationMapping")
        
        assert mode_decl_mapping.parent == ar_root
        assert mode_decl_mapping.short_name == "TestModeDeclarationMapping"
        assert mode_decl_mapping.firstModeRefs == []
        assert mode_decl_mapping.secondModeRef == []
        
        # Test firstModeRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        first_ref = RefType()
        first_ref.setValue("/First/Mode/Ref")
        mode_decl_mapping.addFirstModeRef(first_ref)
        assert first_ref in mode_decl_mapping.getFirstModeRefs()
        
        # Test secondModeRef methods
        second_ref = RefType()
        second_ref.setValue("/Second/Mode/Ref")
        mode_decl_mapping.setSecondModeRef([second_ref])
        assert second_ref in mode_decl_mapping.getSecondModeRef()


class TestModeDeclarationMappingSet:
    """Test class for ModeDeclarationMappingSet class."""
    
    def test_mode_declaration_mapping_set_initialization(self):
        """Test ModeDeclarationMappingSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_decl_mapping_set = ModeDeclarationMappingSet(ar_root, "TestModeDeclarationMappingSet")
        
        assert mode_decl_mapping_set.parent == ar_root
        assert mode_decl_mapping_set.short_name == "TestModeDeclarationMappingSet"
        assert mode_decl_mapping_set.modeDeclarationMappings == []
        
        # Test modeDeclarationMappings methods
        mode_decl_mapping = mode_decl_mapping_set.createModeDeclarationMapping("TestModeDeclMapping")
        assert mode_decl_mapping is not None
        assert mode_decl_mapping.short_name == "TestModeDeclMapping"
        assert mode_decl_mapping in mode_decl_mapping_set.getModeDeclarationMappings()


class TestPortInterfaceMappingSet:
    """Test class for PortInterfaceMappingSet class."""
    
    def test_port_interface_mapping_set_initialization(self):
        """Test PortInterfaceMappingSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping_set = PortInterfaceMappingSet(ar_root, "TestPortInterfaceMappingSet")
        
        assert mapping_set.parent == ar_root
        assert mapping_set.short_name == "TestPortInterfaceMappingSet"
        assert mapping_set.portInterfaceMappings == []
        
        # Test various mapping creation methods
        vp_mapping = mapping_set.createVariableAndParameterInterfaceMapping("TestVPMapping")
        assert vp_mapping is not None
        assert vp_mapping.short_name == "TestVPMapping"
        assert vp_mapping in mapping_set.getPortInterfaceMappings()
        
        cs_mapping = mapping_set.createClientServerInterfaceMapping("TestCSMapping")
        assert cs_mapping is not None
        assert cs_mapping.short_name == "TestCSMapping"
        assert cs_mapping in mapping_set.getPortInterfaceMappings()
        
        mode_mapping = mapping_set.createModeInterfaceMapping("TestModeMapping")
        assert mode_mapping is not None
        assert mode_mapping.short_name == "TestModeMapping"
        assert mode_mapping in mapping_set.getPortInterfaceMappings()
        
        trigger_mapping = mapping_set.createTriggerInterfaceMapping("TestTriggerMapping")
        assert trigger_mapping is not None
        assert trigger_mapping.short_name == "TestTriggerMapping"
        assert trigger_mapping in mapping_set.getPortInterfaceMappings()


class TestTextTableMapping:
    """Test class for TextTableMapping class."""
    
    def test_text_table_mapping_initialization(self):
        """Test TextTableMapping initialization and methods."""
        text_mapping = TextTableMapping()
        
        assert text_mapping.bitfieldTextTableMaskFirst is None
        assert text_mapping.bitfieldTextTableMaskSecond is None
        assert text_mapping.identicalMapping is None
        assert text_mapping.mappingDirection is None
        assert text_mapping.valuePairs == []
        
        # Test bitfieldTextTableMaskFirst methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
        mask_first = PositiveInteger()
        mask_first.setValue(0xFF)
        text_mapping.setBitfieldTextTableMaskFirst(mask_first)
        assert text_mapping.getBitfieldTextTableMaskFirst() == mask_first
        
        # Test bitfieldTextTableMaskSecond methods
        mask_second = PositiveInteger()
        mask_second.setValue(0xF0)
        text_mapping.setBitfieldTextTableMaskSecond(mask_second)
        assert text_mapping.getBitfieldTextTableMaskSecond() == mask_second
        
        # Test identicalMapping methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
        identical = Boolean()
        identical.setValue(True)
        text_mapping.setIdenticalMapping(identical)
        assert text_mapping.getIdenticalMapping() == identical
        
        # Test mappingDirection methods
        direction = "test_direction"
        text_mapping.setMappingDirection(direction)
        assert text_mapping.getMappingDirection() == direction
        
        # Test valuePairs methods
        value_pair = "test_value_pair"
        text_mapping.setValuePairs([value_pair])
        assert value_pair in text_mapping.getValuePairs()