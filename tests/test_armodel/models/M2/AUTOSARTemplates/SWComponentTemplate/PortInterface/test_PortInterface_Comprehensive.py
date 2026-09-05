"""
This module contains comprehensive tests for the PortInterface module in SWComponentTemplate.
Tests cover all classes and methods in the PortInterface module files to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerApplicationErrorMapping,
    ClientServerInterfaceMapping,
    ClientServerOperationMapping,
    DataPrototypeMapping,
    InvalidationPolicy,
    MetaDataItem,
    MetaDataItemSet,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchInterface,
    PortInterfaceMapping,
    PortInterfaceMappingSet,
    SubElementRef,
    TriggerInterface,
    TriggerInterfaceMapping,
    VariableAndParameterInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef


class TestApplicationCompositeElementInPortInterfaceInstanceRef:
    """Test class for ApplicationCompositeElementInPortInterfaceInstanceRef class."""

    def test_application_composite_element_in_port_interface_instance_ref_initialization(self):
        """Test ApplicationCompositeElementInPortInterfaceInstanceRef initialization and methods."""
        instance_ref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        assert instance_ref.getBaseRef() is None
        assert instance_ref.getContextDataPrototypeRefs() == []
        assert instance_ref.getRootDataPrototypeRef() is None
        assert instance_ref.getTargetDataPrototypeRef() is None

        # Test setters and getters
        base_ref = RefType()
        base_ref.setValue("/Test/Base")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        context_ref = RefType()
        context_ref.setValue("/Test/Context")
        instance_ref.addContextDataPrototypeRef(context_ref)
        assert instance_ref.getContextDataPrototypeRefs() == [context_ref]

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

        assert trigger_interface.getTriggers() == []
        assert trigger_interface.parent == ar_root
        assert trigger_interface.short_name == "TestTriggerInterface"


class TestModeSwitchInterface:
    """Test class for ModeSwitchInterface class."""

    def test_mode_switch_interface_initialization(self):
        """Test ModeSwitchInterface initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_switch_interface = ModeSwitchInterface(ar_root, "TestModeSwitchInterface")

        assert mode_switch_interface.getModeGroup() is None
        assert mode_switch_interface.parent == ar_root
        assert mode_switch_interface.short_name == "TestModeSwitchInterface"

        # Test createModeGroup and getModeGroup
        mode_group = mode_switch_interface.createModeGroup("TestModeGroup")
        assert mode_group is not None
        assert mode_switch_interface.getModeGroup() is mode_group


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
        with pytest.raises(TypeError):
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

    def test_first_data_prototype_ref_none_noop(self):
        """Test setFirstDataPrototypeRef with None is a no-op."""
        mapping = DataPrototypeMapping()
        ref = RefType()
        ref.setValue("/Test/FirstData")
        mapping.setFirstDataPrototypeRef(ref)
        mapping.setFirstDataPrototypeRef(None)
        assert mapping.getFirstDataPrototypeRef() == ref

    def test_first_to_second_data_transformation_ref(self):
        """Test firstToSecondDataTransformationRef getter and setter with None no-op."""
        mapping = DataPrototypeMapping()
        assert mapping.getFirstToSecondDataTransformationRef() is None
        ref = RefType()
        ref.setValue("/Test/Transform")
        mapping.setFirstToSecondDataTransformationRef(ref)
        assert mapping.getFirstToSecondDataTransformationRef() == ref
        mapping.setFirstToSecondDataTransformationRef(None)
        assert mapping.getFirstToSecondDataTransformationRef() == ref

    def test_second_to_first_data_transformation_ref(self):
        """Test secondToFirstDataTransformationRef getter and setter with None no-op."""
        mapping = DataPrototypeMapping()
        assert mapping.getSecondToFirstDataTransformationRef() is None
        ref = RefType()
        ref.setValue("/Test/Transform2")
        mapping.setSecondToFirstDataTransformationRef(ref)
        assert mapping.getSecondToFirstDataTransformationRef() == ref
        mapping.setSecondToFirstDataTransformationRef(None)
        assert mapping.getSecondToFirstDataTransformationRef() == ref

    def test_add_sub_element_mapping(self):
        """Test addSubElementMapping and getSubElementMappings with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementMapping

        mapping = DataPrototypeMapping()
        assert mapping.getSubElementMappings() == []
        sub = SubElementMapping()
        result = mapping.addSubElementMapping(sub)
        assert result is mapping
        assert mapping.getSubElementMappings() == [sub]
        mapping.addSubElementMapping(None)
        assert mapping.getSubElementMappings() == [sub]

    def test_add_text_table_mapping(self):
        """Test addTextTableMapping and getTextTableMappings with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping

        mapping = DataPrototypeMapping()
        assert mapping.getTextTableMappings() == []
        text_map = TextTableMapping()
        result = mapping.addTextTableMapping(text_map)
        assert result is mapping
        assert mapping.getTextTableMappings() == [text_map]
        mapping.addTextTableMapping(None)
        assert mapping.getTextTableMappings() == [text_map]


class TestSubElementRef:
    """Test class for SubElementRef class (Table 4.33, p.138)."""

    SPEC_NOTE = "This meta-class provides the ability to reference elements of composite data type."

    def test_sub_element_ref_abstract(self):
        """SubElementRef is abstract (Table 4.33 header) — direct instantiation must fail."""
        with pytest.raises(TypeError):
            SubElementRef()

    def test_sub_element_ref_heritage(self):
        """Most-derived direct base is ARObject (Table 4.33 Base row), verified via concrete subclass."""
        assert SubElementRef.__mro__[1] is ARObject

        class ConcreteSubElementRef(SubElementRef):
            """Concrete stand-in for the queued ImplementationDataTypeSubElementRef (Table 4.34)."""

        ref = ConcreteSubElementRef()
        assert type(ref).__bases__ == (SubElementRef,)
        for ancestor in (SubElementRef, ARObject):
            assert isinstance(ref, ancestor)

    def test_sub_element_ref_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 4.33)."""
        assert SubElementRef.__doc__.strip() == self.SPEC_NOTE

    def test_sub_element_ref_base_accessors_via_subclass(self):
        """Base member (parent from ARObject) is initialised through a concrete subclass."""

        class ConcreteSubElementRef(SubElementRef):
            pass

        ref = ConcreteSubElementRef()
        assert ref.parent is None


class TestSubElementMapping:
    """Test class for SubElementMapping class."""

    def test_sub_element_mapping_initialization(self):
        """Test SubElementMapping initialization."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementMapping

        mapping = SubElementMapping()
        assert mapping.getFirstElement() is None
        assert mapping.getSecondElement() is None
        assert mapping.getTextTableMappings() == []

    def test_get_set_first_element(self):
        """Test firstElement getter and setter with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementMapping
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef

        mapping = SubElementMapping()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        result = mapping.setFirstElement(iref)
        assert result is mapping
        assert mapping.getFirstElement() == iref
        mapping.setFirstElement(None)
        assert mapping.getFirstElement() == iref

    def test_get_set_second_element(self):
        """Test secondElement getter and setter with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementMapping
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef

        mapping = SubElementMapping()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        result = mapping.setSecondElement(iref)
        assert result is mapping
        assert mapping.getSecondElement() == iref
        mapping.setSecondElement(None)
        assert mapping.getSecondElement() == iref

    def test_add_text_table_mapping(self):
        """Test addTextTableMapping and getTextTableMappings with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementMapping, TextTableMapping

        mapping = SubElementMapping()
        assert mapping.getTextTableMappings() == []
        text_map = TextTableMapping()
        result = mapping.addTextTableMapping(text_map)
        assert result is mapping
        assert mapping.getTextTableMappings() == [text_map]
        mapping.addTextTableMapping(None)
        assert mapping.getTextTableMappings() == [text_map]


class TestTextTableMapping:
    """Test class for TextTableMapping class."""

    def test_text_table_mapping_initialization(self):
        """Test TextTableMapping initialization."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping

        mapping = TextTableMapping()
        assert mapping.getBitfieldTextTableMaskFirst() is None
        assert mapping.getBitfieldTextTableMaskSecond() is None
        assert mapping.getIdenticalMapping() is None
        assert mapping.getValuePairs() == []

    def test_get_set_bitfield_text_table_mask_first(self):
        """Test bitfieldTextTableMaskFirst getter and setter with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping

        mapping = TextTableMapping()
        mask = PositiveInteger()
        mask.setValue(255)
        result = mapping.setBitfieldTextTableMaskFirst(mask)
        assert result is mapping
        assert mapping.getBitfieldTextTableMaskFirst() == mask
        mapping.setBitfieldTextTableMaskFirst(None)
        assert mapping.getBitfieldTextTableMaskFirst() == mask

    def test_get_set_bitfield_text_table_mask_second(self):
        """Test bitfieldTextTableMaskSecond getter and setter with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping

        mapping = TextTableMapping()
        mask = PositiveInteger()
        mask.setValue(255)
        result = mapping.setBitfieldTextTableMaskSecond(mask)
        assert result is mapping
        assert mapping.getBitfieldTextTableMaskSecond() == mask
        mapping.setBitfieldTextTableMaskSecond(None)
        assert mapping.getBitfieldTextTableMaskSecond() == mask

    def test_get_set_identical_mapping(self):
        """Test identicalMapping getter and setter with None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping

        mapping = TextTableMapping()
        flag = Boolean()
        flag.setValue(True)
        result = mapping.setIdenticalMapping(flag)
        assert result is mapping
        assert mapping.getIdenticalMapping() == flag
        mapping.setIdenticalMapping(None)
        assert mapping.getIdenticalMapping() == flag


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
    """Test class for TriggerInterfaceMapping class (Table 4.30, p.134)."""

    SPEC_NOTE = "Defines the mapping of unequal named Triggers in context of two different TriggerInterfaces."

    def test_trigger_interface_mapping_initialization(self):
        """Test TriggerInterfaceMapping initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = TriggerInterfaceMapping(ar_root, "TestTriggerInterfaceMapping")

        assert mapping.triggerMappings == []
        assert mapping.parent == ar_root
        assert mapping.short_name == "TestTriggerInterfaceMapping"

    def test_trigger_interface_mapping_heritage(self):
        """TriggerInterfaceMapping's most-derived direct base is PortInterfaceMapping (Table 4.30 Base chain)."""
        mapping = TriggerInterfaceMapping(None, "Tim")

        assert type(mapping).__bases__ == (PortInterfaceMapping,)
        for ancestor in (PortInterfaceMapping, Identifiable, Referrable, ARObject):
            assert isinstance(mapping, ancestor)

    def test_trigger_interface_mapping_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 4.30)."""
        assert TriggerInterfaceMapping.__doc__.strip() == self.SPEC_NOTE

    def test_trigger_interface_mapping_get_add_round_trip(self):
        """getTriggerMappings / addTriggerMapping round-trip with chaining."""
        mapping = TriggerInterfaceMapping(None, "Tim")
        trigger_mapping = TriggerMapping()

        return_value = mapping.addTriggerMapping(trigger_mapping)
        assert return_value == mapping  # method chaining
        assert mapping.getTriggerMappings() == [trigger_mapping]

    def test_trigger_interface_mapping_add_none_noop(self):
        """addTriggerMapping(None) is a no-op."""
        mapping = TriggerInterfaceMapping(None, "Tim")

        mapping.addTriggerMapping(None)
        assert mapping.getTriggerMappings() == []


class TestModeDeclarationMapping:
    """Test class for ModeDeclarationMapping class."""

    def test_mode_declaration_mapping_initialization(self):
        """Test ModeDeclarationMapping initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ModeDeclarationMapping(ar_root, "TestModeDeclarationMapping")

        assert mapping.getFirstModeRefs() == []
        assert mapping.getSecondModeRef() is None
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

        # Test None no-op on secondModeRef
        mapping.setSecondModeRef(None)
        assert second_ref == mapping.getSecondModeRef()

    def test_add_first_mode_ref_none_noop(self):
        """Test addFirstModeRef with None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ModeDeclarationMapping(ar_root, "TestModeDeclarationMapping")
        mapping.addFirstModeRef(None)
        assert mapping.getFirstModeRefs() == []


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
