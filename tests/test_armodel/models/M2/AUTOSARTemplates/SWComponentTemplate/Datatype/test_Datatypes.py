"""
This module contains comprehensive tests for the Datatypes module in SWComponentTemplate.Datatype.
Tests cover all classes and methods in the Datatypes.py file to achieve 100% test coverage.
"""

import inspect
import typing
from typing import List, Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationRecordElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationArrayDataType,
    ApplicationCompositeDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    ArraySizeHandlingEnum,
    AutosarDataType,
    DataTypeMap,
    DataTypeMappingSet,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestAutosarDataType:
    """Test class for AutosarDataType abstract class."""

    def test_autosar_data_type_abstract(self):
        """Test that AutosarDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AutosarDataType(ar_root, "TestAutosarDataType")


class TestAutosarDataTypeHeritage:
    """Heritage / API tests for the synced AutosarDataType (Table 5.1)."""

    def test_direct_base_is_arelement(self):
        assert AutosarDataType.__bases__[0] is ARElement

    def test_mro_reaches_identifiable_and_arobject(self):
        assert issubclass(AutosarDataType, Identifiable)
        assert issubclass(AutosarDataType, ARObject)
        assert Identifiable in AutosarDataType.__mro__
        assert ARObject in AutosarDataType.__mro__

    def test_atptype_branch_dropped(self):
        # Single role-matching branch chosen (ARElement); AtpType is a parallel
        # branch off Identifiable and is intentionally not multi-inherited.
        assert AtpType not in AutosarDataType.__mro__

    def test_concrete_subclass_is_instance_of_bases(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive = ApplicationPrimitiveDataType(ar_root, "TestPrimitive")
        assert isinstance(primitive, ARElement)
        assert isinstance(primitive, Identifiable)
        assert isinstance(primitive, ARObject)
        assert not isinstance(primitive, AtpType)

    def test_class_docstring_matches_spec_note(self):
        assert AutosarDataType.__doc__ == ("Abstract base class for user defined AUTOSAR data types for software.")

    def test_sw_data_def_props_round_trip(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive = ApplicationPrimitiveDataType(ar_root, "TestPrimitive")
        props = SwDataDefProps()
        primitive.setSwDataDefProps(props)
        assert primitive.getSwDataDefProps() is props

    def test_set_sw_data_def_props_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive = ApplicationPrimitiveDataType(ar_root, "TestPrimitive")
        props = SwDataDefProps()
        primitive.setSwDataDefProps(props)
        result = primitive.setSwDataDefProps(None)
        assert primitive.getSwDataDefProps() is props
        assert result is primitive

    def test_set_sw_data_def_props_chaining(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive = ApplicationPrimitiveDataType(ar_root, "TestPrimitive")
        props = SwDataDefProps()
        assert primitive.setSwDataDefProps(props) is primitive

    def test_get_sw_data_def_props_docstring_verbatim(self):
        assert AutosarDataType.getSwDataDefProps.__doc__ == "The properties of this AutosarDataType."

    def test_set_sw_data_def_props_docstring_verbatim(self):
        assert AutosarDataType.setSwDataDefProps.__doc__ == ("The properties of this AutosarDataType. A None value is a no-op and is not set.")


class TestApplicationDataType:
    """Test class for ApplicationDataType abstract class."""

    def test_application_data_type_abstract(self):
        """Test that ApplicationDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationDataType(ar_root, "TestApplicationDataType")

    def test_application_data_type_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive_type = ApplicationPrimitiveDataType(ar_root, "TestApplicationPrimitiveDataType")

        assert isinstance(primitive_type, ApplicationDataType)
        assert primitive_type.getSwDataDefProps() is None
        assert ApplicationDataType.__doc__.strip() == (
            'ApplicationDataType defines a data type from the application point of view. Especially it should be used whenever something "physical" is at stake. '
            "An ApplicationDataType represents a set of values as seen in the application model, such as measurement units. It does not consider implementation details such as bit-size, endianess, etc. "
            "It should be possible to model the application level aspects of a VFB system by using ApplicationData Types only."
        )


class TestApplicationPrimitiveDataType:
    """Test class for ApplicationPrimitiveDataType class."""

    def test_application_primitive_data_type_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        primitive_type = ApplicationPrimitiveDataType(ar_root, "TestApplicationPrimitiveDataType")

        assert isinstance(primitive_type, ApplicationDataType)
        assert isinstance(primitive_type, AutosarDataType)
        assert primitive_type.getSwDataDefProps() is None
        assert primitive_type.__class__.__doc__.strip() == "A primitive data type defines a set of allowed values."

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

    def test_application_composite_data_type_spec_contract(self):
        assert ApplicationCompositeDataType.__doc__.strip() == "Abstract base class for all application data types composed of other data types."

    def test_application_composite_data_type_abstract(self):
        """Test that ApplicationCompositeDataType is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationCompositeDataType(ar_root, "TestApplicationCompositeDataType")


class TestApplicationArrayDataType:
    """Heritage / API tests for the synced ApplicationArrayDataType (Table 5.8)."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_type = ApplicationArrayDataType(ar_root, "TestApplicationArrayDataType")

        assert array_type.parent == ar_root
        assert array_type.short_name == "TestApplicationArrayDataType"
        assert array_type.dynamicArraySizeProfile is None
        assert array_type.element is None
        assert array_type.getDynamicArraySizeProfile() is None
        assert array_type.getApplicationArrayElement() is None
        assert array_type.getSwDataDefProps() is None

    def test_base_shape(self):
        assert ApplicationArrayDataType.__bases__[0] is ApplicationCompositeDataType
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_type = ApplicationArrayDataType(ar_root, "TestApplicationArrayDataType")
        assert isinstance(array_type, ApplicationDataType)
        assert isinstance(array_type, AutosarDataType)
        assert isinstance(array_type, ARElement)
        assert isinstance(array_type, Identifiable)
        assert isinstance(array_type, ARObject)

    def test_class_docstring_matches_spec_note(self):
        assert inspect.cleandoc(ApplicationArrayDataType.__doc__) == inspect.cleandoc(
            "An application data type which is an array, each element is of the same application data type.\n\n"
            "    [constr_1907] Existence of attribute ApplicationArrayDataType.element: For each ApplicationArrayDataType, "
            "the aggregation of ApplicationArrayElement in the role element shall exist at the time when the RTE is generated."
        )

    def test_get_set_dynamic_array_size_profile(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_type = ApplicationArrayDataType(ar_root, "TestApplicationArrayDataType")
        profile = String().setValue("FIXED_LENGTH")

        assert array_type.setDynamicArraySizeProfile(profile) is array_type
        assert array_type.getDynamicArraySizeProfile() is profile

        array_type.setDynamicArraySizeProfile(None)
        assert array_type.getDynamicArraySizeProfile() is profile

    def test_get_dynamic_array_size_profile_docstring_verbatim(self):
        assert ApplicationArrayDataType.getDynamicArraySizeProfile.__doc__.strip() == ("Specifies the profile which the array will follow if it is a variable size array.")

    def test_set_dynamic_array_size_profile_docstring_verbatim(self):
        assert ApplicationArrayDataType.setDynamicArraySizeProfile.__doc__.strip() == (
            "Specifies the profile which the array will follow if it is a variable size array. " "A None value is a no-op and does not overwrite an existing dynamicArraySizeProfile."
        )

    def test_get_application_array_element_docstring_verbatim(self):
        assert ApplicationArrayDataType.getApplicationArrayElement.__doc__.strip() == (
            "This association implements the concept of an array element. That is, in some cases it is necessary to be "
            "able to identify single array elements, e.g. as input values for an interpolation routine."
        )

    def test_create_application_array_element_docstring_verbatim(self):
        assert ApplicationArrayDataType.createApplicationArrayElement.__doc__.strip() == (
            "This association implements the concept of an array element. That is, in some cases it is necessary to be "
            "able to identify single array elements, e.g. as input values for an interpolation routine."
        )

    def test_create_application_array_element(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_type = ApplicationArrayDataType(ar_root, "TestApplicationArrayDataType")

        array_element = array_type.createApplicationArrayElement("TestArrayElement")
        assert array_element is not None
        assert array_element.short_name == "TestArrayElement"
        assert array_element.parent == array_type
        assert array_type.element is array_element
        assert array_type.getApplicationArrayElement() is array_element

        duplicate = array_type.createApplicationArrayElement("TestArrayElement")
        assert duplicate is array_element


class TestApplicationRecordDataType:
    """Test class for ApplicationRecordDataType (Table 5.12, R23-11)."""

    ATTRIBUTE_NOTE = (
        "Specifies an element of a record. The aggregation of ApplicationRecordElement is subject to variability "
        "with the purpose to support the conditional existence of elements inside a ApplicationrecordData Type. "
        "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=element.shortName, element.variation Point.shortLabel "
        "vh.latestBindingTime=preCompileTime"
    )

    def test_base_shape(self):
        assert ApplicationRecordDataType.__bases__[0] is ApplicationCompositeDataType
        signature = inspect.signature(ApplicationRecordDataType.__init__)
        assert list(signature.parameters.keys()) == ["self", "parent", "short_name"]
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")
        assert isinstance(record_type, ApplicationDataType)
        assert isinstance(record_type, AutosarDataType)
        assert isinstance(record_type, ARElement)
        assert isinstance(record_type, Identifiable)
        assert isinstance(record_type, ARObject)

    def test_class_docstring_matches_spec_note(self):
        assert inspect.cleandoc(ApplicationRecordDataType.__doc__) == inspect.cleandoc(
            "An application data type which can be decomposed into prototypes of other application data types. "
            "Tags: atp.recommendedPackage=ApplicationDataTypes\n\n"
            "    [constr_1908] Existence of attribute ApplicationRecordDataType.element: For each ApplicationRecordDataType, "
            "the aggregation of ApplicationRecordElement in the role element shall exist at the time when the RTE is generated."
        )

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")

        assert record_type.parent == ar_root
        assert record_type.short_name == "TestApplicationRecordDataType"
        assert record_type.swDataDefProps is None
        assert record_type.elements == []
        assert record_type.getElements() == []

    def test_get_set_sw_data_def_props(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")
        sw_data_def_props = SwDataDefProps()

        assert record_type.setSwDataDefProps(sw_data_def_props) is record_type
        assert record_type.getSwDataDefProps() is sw_data_def_props

        record_type.setSwDataDefProps(None)
        assert record_type.getSwDataDefProps() is sw_data_def_props

    def test_get_elements_type_hint(self):
        hints = typing.get_type_hints(ApplicationRecordDataType.getElements)
        assert hints.get("return") == List[ApplicationRecordElement]
        assert ApplicationRecordDataType.getElements.__annotations__.get("return") == List[ApplicationRecordElement]

    def test_create_application_record_element(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")

        first = record_type.createApplicationRecordElement("First")
        second = record_type.createApplicationRecordElement("Second")

        assert isinstance(first, ApplicationRecordElement)
        assert first.short_name == "First"
        assert first.parent == record_type
        assert record_type.elements == [first, second]
        assert record_type.getElements() == [first, second]

    def test_create_application_record_element_duplicate_returns_existing(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")

        first = record_type.createApplicationRecordElement("First")
        assert record_type.createApplicationRecordElement("First") is first
        assert record_type.getElements() == [first]

    def test_create_application_record_element_registers_in_referrable_registry(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")

        first = record_type.createApplicationRecordElement("First")
        assert record_type.IsReferrableElementExists("First", ApplicationRecordElement)
        assert record_type.getReferrableElement("First", ApplicationRecordElement) is first

    def test_get_elements_returns_the_dedicated_field(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")
        record_type.createApplicationRecordElement("First")

        assert record_type.getElements() is record_type.elements

    def test_get_elements_docstring_verbatim(self):
        assert ApplicationRecordDataType.getElements.__doc__.strip() == self.ATTRIBUTE_NOTE

    def test_create_application_record_element_docstring_verbatim(self):
        assert ApplicationRecordDataType.createApplicationRecordElement.__doc__.strip() == self.ATTRIBUTE_NOTE

    def test_legacy_naming_is_gone(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_type = ApplicationRecordDataType(ar_root, "TestApplicationRecordDataType")

        assert not hasattr(record_type, "recordElements")
        assert not hasattr(record_type, "getApplicationRecordElements")


class TestDataTypeMap:
    """Heritage / API tests for the synced DataTypeMap (Table 5.3)."""

    def test_spec_notes_are_verbatim(self):
        assert DataTypeMap.__doc__.strip() == ("This class represents the relationship between ApplicationDataType and its implementing AbstractImplementationDataType.")
        assert DataTypeMap.getApplicationDataTypeRef.__doc__.strip() == ("This is the corresponding ApplicationDataType [constr_1903]")
        assert DataTypeMap.setApplicationDataTypeRef.__doc__.strip() == (
            "This is the corresponding ApplicationDataType [constr_1903] A None value is a no-op and does not overwrite an existing applicationDataTypeRef."
        )
        assert DataTypeMap.getImplementationDataTypeRef.__doc__.strip() == ("This is the corresponding AbstractImplementationDataType. [constr_1904]")
        assert DataTypeMap.setImplementationDataTypeRef.__doc__.strip() == (
            "This is the corresponding AbstractImplementationDataType. [constr_1904] A None value is a no-op and does not overwrite an existing implementationDataTypeRef."
        )

    def test_base_shape(self):
        assert DataTypeMap.__bases__[0] is ARObject
        signature = inspect.signature(DataTypeMap.__init__)
        assert list(signature.parameters.keys()) == ["self"]
        hints = typing.get_type_hints(DataTypeMap.setApplicationDataTypeRef)
        assert hints.get("value") == Optional[RefType]
        assert hints.get("return") is DataTypeMap
        hints = typing.get_type_hints(DataTypeMap.setImplementationDataTypeRef)
        assert hints.get("value") == Optional[RefType]
        assert hints.get("return") is DataTypeMap
        hints = typing.get_type_hints(DataTypeMap.getApplicationDataTypeRef)
        assert hints.get("return") == Optional[RefType]
        hints = typing.get_type_hints(DataTypeMap.getImplementationDataTypeRef)
        assert hints.get("return") == Optional[RefType]

    def test_initialization(self):
        data_type_map = DataTypeMap()

        assert data_type_map.applicationDataTypeRef is None
        assert data_type_map.implementationDataTypeRef is None

    def test_get_set_application_data_type_ref(self):
        data_type_map = DataTypeMap()
        app_ref = RefType()
        app_ref.setValue("/Application/Type")

        assert data_type_map.setApplicationDataTypeRef(app_ref) is data_type_map
        assert data_type_map.getApplicationDataTypeRef() is app_ref

        data_type_map.setApplicationDataTypeRef(None)
        assert data_type_map.getApplicationDataTypeRef() is app_ref

    def test_get_set_implementation_data_type_ref(self):
        data_type_map = DataTypeMap()
        impl_ref = RefType()
        impl_ref.setValue("/Implementation/Type")

        assert data_type_map.setImplementationDataTypeRef(impl_ref) is data_type_map
        assert data_type_map.getImplementationDataTypeRef() is impl_ref

        data_type_map.setImplementationDataTypeRef(None)
        assert data_type_map.getImplementationDataTypeRef() is impl_ref


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
        assert isinstance(mapping_set, AtpBlueprintable)
        assert mapping_set.__class__.__doc__.strip() == (
            "This class represents a list of mappings between ApplicationDataTypes and ImplementationDataTypes. "
            "In addition, it can contain mappings between ImplementationDataTypes and ModeDeclarationGroups."
        )

        # Test DataTypeMap methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMap

        data_map = DataTypeMap()
        assert mapping_set.addDataTypeMap(data_map) is mapping_set
        assert mapping_set.getDataTypeMaps() == [data_map]
        assert mapping_set.addDataTypeMap(None) is mapping_set
        assert mapping_set.getDataTypeMaps() == [data_map]

        # Test ModeRequestTypeMap methods (import and test)
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap

        mode_map = ModeRequestTypeMap()
        assert mapping_set.addModeRequestTypeMap(mode_map) is mapping_set
        assert mapping_set.getModeRequestTypeMaps() == [mode_map]
        assert mapping_set.addModeRequestTypeMap(None) is mapping_set
        assert mapping_set.getModeRequestTypeMaps() == [mode_map]


class TestArraySizeHandlingEnum:
    """Test class for ArraySizeHandlingEnum functionality (Table 5.11, p.254)."""

    def test_initialization(self):
        """Test enum instantiability per Rule 0011"""
        enum = ArraySizeHandlingEnum()
        assert enum is not None
        assert isinstance(enum, AREnum)

    def test_literal_values(self):
        """Test literal values per AUTOSAR_CP_TPS_SoftwareComponentTemplate Table 5.11"""
        assert ArraySizeHandlingEnum.ALL_INDICES_DIFFERENT_ARRAY_SIZE == "ALL-INDICES-DIFFERENT-ARRAY-SIZE"
        assert ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE == "ALL-INDICES-SAME-ARRAY-SIZE"
        assert ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE == "INHERITED-FROM-ARRAY-ELEMENT-TYPE-SIZE"
        enum = ArraySizeHandlingEnum()
        assert list(enum.getEnumValues()) == ["ALL-INDICES-DIFFERENT-ARRAY-SIZE", "ALL-INDICES-SAME-ARRAY-SIZE", "INHERITED-FROM-ARRAY-ELEMENT-TYPE-SIZE"]

    def test_set_value_round_trip(self):
        """Test instantiability and setValue/getValue round-trip per Rule 0011"""
        enum = ArraySizeHandlingEnum()
        assert enum == enum.setValue(None)
        assert enum.getValue() == ""
        assert enum == enum.setValue(ArraySizeHandlingEnum.ALL_INDICES_DIFFERENT_ARRAY_SIZE)
        assert enum.getValue() == ArraySizeHandlingEnum.ALL_INDICES_DIFFERENT_ARRAY_SIZE
        assert enum == enum.setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE)
        assert enum.getValue() == ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE
        assert enum == enum.setValue(ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE)
        assert enum.getValue() == ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE

    def test_set_value_none_noop(self):
        """Test setValue(None) is a no-op"""
        enum = ArraySizeHandlingEnum()
        assert enum.setValue(None) is enum
        assert enum.getValue() == ""
        enum.setValue(ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE)
        enum.setValue(None)
        assert enum.getValue() == ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE

    def test_validate_enum_value(self):
        """Test validateEnumValue accepts spec literals and rejects others"""
        enum = ArraySizeHandlingEnum()
        assert enum.validateEnumValue("ALL-INDICES-DIFFERENT-ARRAY-SIZE") is True
        assert enum.validateEnumValue("ALL-INDICES-SAME-ARRAY-SIZE") is True
        assert enum.validateEnumValue("INHERITED-FROM-ARRAY-ELEMENT-TYPE-SIZE") is True
        assert enum.validateEnumValue("bogus") is False

    def test_spec_note(self):
        """Test the Table 5.11 class note."""
        assert ArraySizeHandlingEnum.__doc__.strip() == "This enumeration defines different ways to handle the sizes of variable size arrays."
