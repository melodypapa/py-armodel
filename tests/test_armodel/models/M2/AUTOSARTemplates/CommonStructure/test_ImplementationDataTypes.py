import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    AbstractImplementationDataType,
    AbstractImplementationDataTypeElement,
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
    ImplementationDataType,
    ImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, NameToken, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ArraySizeHandlingEnum, AutosarDataType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestAbstractImplementationDataTypeElement:
    def test_spec_note_and_base_class(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")

        assert isinstance(element, AtpStructureElement)
        assert AbstractImplementationDataTypeElement.__doc__.strip() == (
            "This meta-class represents the ability to act as an abstract base class for specific derived meta-classes "
            "that support the modeling of ImplementationDataTypes for a particular language binding."
        )

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractImplementationDataTypeElement abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractImplementationDataTypeElement is an abstract class"):
            AbstractImplementationDataTypeElement(ar_root, "TestElement")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of AbstractImplementationDataTypeElement can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")

        assert element is not None
        assert element.getShortName() == "TestElement"


class TestImplementationDataTypeElement:
    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 5.17 Notes copied verbatim."""
        assert (
            ImplementationDataTypeElement.__doc__.strip() == "Declares a data object which is locally aggregated. Such an element can only be used within the scope where it is aggregated. "
            "This element either consists of further subElements or it is further defined via its swDataDefProps. There are several use cases "
            "within the system of ImplementationDataTypes fur such a local declaration: \u2022 It can represent the elements of an array, defining "
            "the element type and array size \u2022 It can represent an element of a struct, defining its type \u2022 It can be the local declaration of a debug element."
        )
        array_impl_policy_note = "This attribute controls the implementation of the payload of an array. It shall only be used if the enclosing ImplementationDataType constitutes an array."
        assert ImplementationDataTypeElement.getArrayImplPolicy.__doc__.strip() == array_impl_policy_note
        assert ImplementationDataTypeElement.setArrayImplPolicy.__doc__.strip() == array_impl_policy_note + " A None value is a no-op and does not overwrite an existing arrayImplPolicy."
        array_size_note = (
            "The existence of this attributes (if bigger than 0) defines the size of an array and declares that this " "ImplementationDataTypeElement represents the type of each single array element."
        )
        assert ImplementationDataTypeElement.getArraySize.__doc__.strip() == array_size_note
        assert ImplementationDataTypeElement.setArraySize.__doc__.strip() == array_size_note + " A None value is a no-op and does not overwrite an existing arraySize."
        array_size_handling_note = "The way how the size of the array is handled in case of a variable size array."
        assert ImplementationDataTypeElement.getArraySizeHandling.__doc__.strip() == array_size_handling_note
        assert ImplementationDataTypeElement.setArraySizeHandling.__doc__.strip() == array_size_handling_note + " A None value is a no-op and does not overwrite an existing arraySizeHandling."
        array_size_semantics_note = "This attribute controls the meaning of the value of the array size."
        assert ImplementationDataTypeElement.getArraySizeSemantics.__doc__.strip() == array_size_semantics_note
        assert ImplementationDataTypeElement.setArraySizeSemantics.__doc__.strip() == array_size_semantics_note + " A None value is a no-op and does not overwrite an existing arraySizeSemantics."
        is_optional_note = (
            "This attribute represents the ability to declare the enclosing ImplementationDataTypeElement as optional. This means that, at runtime, "
            "the ImplementationDataTypeElement may or may not have a valid value and shall therefore be ignored. The underlying runtime software "
            "provides means to set the CppImplementationDataTypeElement as not valid at the sending end of a communication and determine its validity at the receiving end."
        )
        assert ImplementationDataTypeElement.getIsOptional.__doc__.strip() == is_optional_note
        assert ImplementationDataTypeElement.setIsOptional.__doc__.strip() == is_optional_note + " A None value is a no-op and does not overwrite an existing isOptional."
        sub_element_note = (
            'Element of an array, struct, or union in case of a nested declaration (i.e. without using "typedefs"). The aggregation of '
            "ImplementionDataTypeElement is subject to variability with the purpose to support the conditional existence of elements "
            "inside a ImplementationDataType representing a structure."
        )
        assert ImplementationDataTypeElement.createImplementationDataTypeElement.__doc__.strip() == sub_element_note
        assert ImplementationDataTypeElement.getSubElements.__doc__.strip() == sub_element_note
        sw_data_def_props_note = "The properties of this ImplementationDataTypeElement."
        assert ImplementationDataTypeElement.getSwDataDefProps.__doc__.strip() == sw_data_def_props_note
        assert ImplementationDataTypeElement.setSwDataDefProps.__doc__.strip() == sw_data_def_props_note + " A None value is a no-op and does not overwrite an existing swDataDefProps."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject, AbstractImplementationDataTypeElement, ... \u2014 Python base is the most-derived AbstractImplementationDataTypeElement (+ VariationPointCapable per the subElement atpVariation row); setter return annotations are bare names (PEP 563, Rule 0003)."""
        assert issubclass(ImplementationDataTypeElement, AbstractImplementationDataTypeElement)
        assert issubclass(ImplementationDataTypeElement, VariationPointCapable)
        for name in ("setArrayImplPolicy", "setArraySize", "setArraySizeHandling", "setArraySizeSemantics", "setIsOptional", "setSwDataDefProps", "createImplementationDataTypeElement"):
            assert ImplementationDataTypeElement.__dict__[name].__annotations__["return"] == "ImplementationDataTypeElement"

    def test_initialization_defaults(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.parent == ar_root
        assert element.short_name == "TestElement"
        assert element.arrayImplPolicy is None
        assert element.arraySize is None
        assert element.arraySizeHandling is None
        assert element.arraySizeSemantics is None
        assert element.isOptional is None
        assert element.subElements == []
        assert element.swDataDefProps is None
        assert element.getArrayImplPolicy() is None
        assert element.getArraySize() is None
        assert element.getArraySizeHandling() is None
        assert element.getArraySizeSemantics() is None
        assert element.getIsOptional() is None
        assert element.getSubElements() == []
        assert element.getSwDataDefProps() is None

    def test_get_set_array_impl_policy(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = ArrayImplPolicyEnum().setValue(ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY)
        result = element.setArrayImplPolicy(value)
        assert result is element
        assert element.getArrayImplPolicy() is value
        assert element.getArrayImplPolicy().getValue() == ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY
        assert element.setArrayImplPolicy(None) is element
        assert element.getArrayImplPolicy() is value

    def test_get_set_array_size(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = PositiveInteger().setValue("4")
        result = element.setArraySize(value)
        assert result is element
        assert element.getArraySize() is value
        assert element.getArraySize().getValue() == 4
        assert element.setArraySize(None) is element
        assert element.getArraySize() is value

    def test_get_set_array_size_handling(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = ArraySizeHandlingEnum().setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE)
        result = element.setArraySizeHandling(value)
        assert result is element
        assert element.getArraySizeHandling() is value
        assert element.getArraySizeHandling().getValue() == ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE
        assert element.setArraySizeHandling(None) is element
        assert element.getArraySizeHandling() is value

    def test_get_set_array_size_semantics(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE)
        result = element.setArraySizeSemantics(value)
        assert result is element
        assert element.getArraySizeSemantics() is value
        assert element.getArraySizeSemantics().getValue() == ArraySizeSemanticsEnum.FIXED_SIZE
        assert element.setArraySizeSemantics(None) is element
        assert element.getArraySizeSemantics() is value

    def test_get_set_is_optional(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = Boolean().setValue(True)
        result = element.setIsOptional(value)
        assert result is element
        assert element.getIsOptional() is value
        assert element.getIsOptional().getValue() is True
        assert element.setIsOptional(None) is element
        assert element.getIsOptional() is value

    def test_get_set_sw_data_def_props(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        value = SwDataDefProps()
        result = element.setSwDataDefProps(value)
        assert result is element
        assert element.getSwDataDefProps() is value
        assert element.setSwDataDefProps(None) is element
        assert element.getSwDataDefProps() is value

    def test_create_and_get_sub_elements(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        sub_element = element.createImplementationDataTypeElement("SubElement")
        assert isinstance(sub_element, ImplementationDataTypeElement)
        assert sub_element.getShortName() == "SubElement"
        assert element.getSubElements() == [sub_element]
        assert element.createImplementationDataTypeElement("SubElement") is sub_element
        assert len(element.getSubElements()) == 1


class TestAbstractImplementationDataType:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractImplementationDataType abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractImplementationDataType is an abstract class."):
            AbstractImplementationDataType(ar_root, "TestAbstractImplementationDataType")

    def test_direct_base_is_autosar_data_type(self):
        assert AbstractImplementationDataType.__bases__[0] is AutosarDataType

    def test_concrete_subclass_inherits_autosar_data_type_state(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestAbstractImplementationDataType")

        assert isinstance(data_type, AutosarDataType)
        assert data_type.swDataDefProps is None

    def test_class_docstring_matches_spec_note(self):
        assert AbstractImplementationDataType.__doc__ == ("This meta-class represents an abstract base class for different flavors of ImplementationDataType.")


class TestImplementationDataType:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        assert data_type is not None
        assert data_type.getShortName() == "TestImplementationDataType"
        assert data_type.dynamicArraySizeProfile is None
        assert data_type.isStructWithOptionalElement is None
        assert data_type.subElements == []
        assert data_type.symbolProps is None
        assert data_type.typeEmitter is None

    def test_inheritance_chain(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        assert isinstance(data_type, AbstractImplementationDataType)
        assert isinstance(data_type, AutosarDataType)
        assert ImplementationDataType.__bases__[0] is AbstractImplementationDataType

    def test_category_constants(self):
        assert ImplementationDataType.CATEGORY_TYPE_REFERENCE == "TYPE_REFERENCE"
        assert ImplementationDataType.CATEGORY_TYPE_VALUE == "VALUE"
        assert ImplementationDataType.CATEGORY_TYPE_STRUCTURE == "STRUCTURE"
        assert ImplementationDataType.CATEGORY_DATA_REFERENCE == "DATA_REFERENCE"
        assert ImplementationDataType.CATEGORY_ARRAY == "ARRAY"

    def test_class_docstring_matches_spec_note(self):
        assert ImplementationDataType.__doc__.strip() == ("Describes a reusable data type on the implementation level. This will typically correspond to a typedef in C-code.")

    def test_get_set_dynamic_array_size_profile(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getDynamicArraySizeProfile() is None

        profile = String().setValue("VARIABLE_LENGTH_PROFILE")
        assert data_type.setDynamicArraySizeProfile(profile) is data_type
        assert data_type.getDynamicArraySizeProfile() is profile

        data_type.setDynamicArraySizeProfile(None)
        assert data_type.getDynamicArraySizeProfile() is profile

    def test_get_dynamic_array_size_profile_docstring_verbatim(self):
        assert ImplementationDataType.getDynamicArraySizeProfile.__doc__.strip() == ("Specifies the profile which the array will follow in case this data type is a variable size array.")

    def test_set_dynamic_array_size_profile_docstring_verbatim(self):
        assert ImplementationDataType.setDynamicArraySizeProfile.__doc__.strip() == (
            "Specifies the profile which the array will follow in case this data type is a variable size array. " "A None value is a no-op and does not overwrite an existing dynamicArraySizeProfile."
        )

    def test_get_set_is_struct_with_optional_element(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getIsStructWithOptionalElement() is None

        flag = Boolean().setValue(True)
        assert data_type.setIsStructWithOptionalElement(flag) is data_type
        assert data_type.getIsStructWithOptionalElement() is flag
        assert data_type.getIsStructWithOptionalElement().getValue() is True

        data_type.setIsStructWithOptionalElement(None)
        assert data_type.getIsStructWithOptionalElement() is flag

    def test_get_is_struct_with_optional_element_docstring_verbatim(self):
        assert ImplementationDataType.getIsStructWithOptionalElement.__doc__.strip() == (
            "This attribute is only valid if the attribute category is set to STRUCTURE. "
            "If set to true, this attribute indicates that the ImplementationDataType has been created "
            "with the intention to define at least one element of the structure as optional."
        )

    def test_set_is_struct_with_optional_element_docstring_verbatim(self):
        assert ImplementationDataType.setIsStructWithOptionalElement.__doc__.strip() == (
            "This attribute is only valid if the attribute category is set to STRUCTURE. "
            "If set to true, this attribute indicates that the ImplementationDataType has been created "
            "with the intention to define at least one element of the structure as optional. "
            "A None value is a no-op and does not overwrite an existing isStructWithOptionalElement."
        )

    def test_create_implementation_data_type_element(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getSubElements() == []

        element = data_type.createImplementationDataTypeElement("Elem")
        assert isinstance(element, ImplementationDataTypeElement)
        assert element.getShortName() == "Elem"
        assert element.parent is data_type
        assert data_type.getSubElements() == [element]
        assert len(data_type.getSubElements()) == 1

        duplicate = data_type.createImplementationDataTypeElement("Elem")
        assert duplicate is element
        assert len(data_type.getSubElements()) == 1

    def test_create_implementation_data_type_element_docstring_verbatim(self):
        assert ImplementationDataType.createImplementationDataTypeElement.__doc__.strip() == (
            "Specifies an element of an array, struct, or union data type. "
            "The aggregation of ImplementionDataTypeElement is subject to variability with the purpose "
            "to support the conditional existence of elements inside a Implementation DataType "
            "representing a structure."
        )

    def test_get_sub_elements_docstring_verbatim(self):
        assert ImplementationDataType.getSubElements.__doc__.strip() == (
            "Specifies an element of an array, struct, or union data type. "
            "The aggregation of ImplementionDataTypeElement is subject to variability with the purpose "
            "to support the conditional existence of elements inside a Implementation DataType "
            "representing a structure."
        )

    def test_create_symbol_props(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getSymbolProps() is None

        symbol_props = data_type.createSymbolProps("Sym")
        assert isinstance(symbol_props, SymbolProps)
        assert symbol_props.getShortName() == "Sym"
        assert symbol_props.parent is data_type
        assert data_type.getSymbolProps() is symbol_props

        duplicate = data_type.createSymbolProps("Sym")
        assert duplicate is symbol_props

    def test_create_symbol_props_docstring_verbatim(self):
        assert ImplementationDataType.createSymbolProps.__doc__.strip() == ("This represents the SymbolProps for the Implementation DataType.")

    def test_get_symbol_props_docstring_verbatim(self):
        assert ImplementationDataType.getSymbolProps.__doc__.strip() == ("This represents the SymbolProps for the Implementation DataType.")

    def test_get_set_type_emitter(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getTypeEmitter() is None

        emitter = NameToken().setValue("RTE")
        assert data_type.setTypeEmitter(emitter) is data_type
        assert data_type.getTypeEmitter() is emitter
        assert data_type.getTypeEmitter().getValue() == "RTE"

        data_type.setTypeEmitter(None)
        assert data_type.getTypeEmitter() is emitter

    def test_get_type_emitter_docstring_verbatim(self):
        assert ImplementationDataType.getTypeEmitter.__doc__.strip() == ("This attribute is used to control which part of the AUTOSAR toolchain is supposed to trigger data type definitions.")

    def test_set_type_emitter_docstring_verbatim(self):
        assert ImplementationDataType.setTypeEmitter.__doc__.strip() == (
            "This attribute is used to control which part of the AUTOSAR toolchain is supposed to trigger data type definitions. "
            "A None value is a no-op and does not overwrite an existing typeEmitter."
        )


class TestArraySizeSemanticsEnum:
    """Test class for ArraySizeSemanticsEnum functionality (Table 5.10, p.253)."""

    def test_initialization(self):
        """Test enum instantiability per Rule 0011"""
        enum = ArraySizeSemanticsEnum()
        assert enum is not None
        assert isinstance(enum, AREnum)

    def test_literal_values(self):
        """Test literal values per AUTOSAR_CP_TPS_SoftwareComponentTemplate Table 5.10"""
        assert ArraySizeSemanticsEnum.FIXED_SIZE == "FIXED-SIZE"
        assert ArraySizeSemanticsEnum.VARIABLE_SIZE == "VARIABLE-SIZE"
        enum = ArraySizeSemanticsEnum()
        assert list(enum.getEnumValues()) == ["FIXED-SIZE", "VARIABLE-SIZE"]

    def test_set_value_round_trip(self):
        """Test instantiability and setValue/getValue round-trip per Rule 0011"""
        enum = ArraySizeSemanticsEnum()
        assert enum == enum.setValue(None)
        assert enum.getValue() == ""
        assert enum == enum.setValue(ArraySizeSemanticsEnum.FIXED_SIZE)
        assert enum.getValue() == ArraySizeSemanticsEnum.FIXED_SIZE
        assert enum == enum.setValue(ArraySizeSemanticsEnum.VARIABLE_SIZE)
        assert enum.getValue() == ArraySizeSemanticsEnum.VARIABLE_SIZE

    def test_set_value_none_noop(self):
        """Test setValue(None) is a no-op"""
        enum = ArraySizeSemanticsEnum()
        assert enum.setValue(None) is enum
        assert enum.getValue() == ""
        enum.setValue(ArraySizeSemanticsEnum.VARIABLE_SIZE)
        enum.setValue(None)
        assert enum.getValue() == ArraySizeSemanticsEnum.VARIABLE_SIZE

    def test_validate_enum_value(self):
        """Test validateEnumValue accepts spec literals and rejects others"""
        enum = ArraySizeSemanticsEnum()
        assert enum.validateEnumValue("FIXED-SIZE") is True
        assert enum.validateEnumValue("VARIABLE-SIZE") is True
        assert enum.validateEnumValue("bogus") is False

    def test_spec_note(self):
        """Test the Table 5.10 class note."""
        assert ArraySizeSemanticsEnum.__doc__.strip() == "This type controls how the information about the number of elements in an ApplicationArrayDataType is to be interpreted."


class TestArrayImplPolicyEnum:
    def test_literals(self):
        """Test ArrayImplPolicyEnum literal values per AUTOSAR_CP_TPS_SoftwareComponentTemplate Table 5.18"""
        assert ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY == "PAYLOAD-AS-ARRAY"
        assert ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY == "PAYLOAD-AS-POINTER-TO-ARRAY"

    def test_enum_values(self):
        """Test the valid enum value set in spec literal order (Table 5.18)"""
        enum = ArrayImplPolicyEnum()
        assert enum.getEnumValues() == (
            ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY,
            ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY,
        )

    def test_instantiation_set_value(self):
        """Test enum instantiability and setValue/getValue round-trip per Rule 0011"""
        enum = ArrayImplPolicyEnum()
        result = enum.setValue(ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY)
        assert result is enum  # Method chaining
        assert enum.getValue() == ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY

    def test_set_value_none_noop(self):
        """Test setValue(None) is a no-op"""
        enum = ArrayImplPolicyEnum()
        assert enum.setValue(None) is enum
        assert enum.getValue() == ""  # ARLiteral's empty representation for an unset literal
        enum.setValue(ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY)
        enum.setValue(None)
        assert enum.getValue() == ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY

    def test_validate_enum_value(self):
        """Test validateEnumValue accepts spec literals and rejects others"""
        enum = ArrayImplPolicyEnum()
        assert enum.validateEnumValue("PAYLOAD-AS-ARRAY") is True
        assert enum.validateEnumValue("PAYLOAD-AS-POINTER-TO-ARRAY") is True
        assert enum.validateEnumValue("bogus") is False

    def test_spec_note(self):
        """Test the Table 5.18 class note."""
        assert ArrayImplPolicyEnum.__doc__.strip() == "This meta-class provides values to configure the implementation of the payload part of an array."
