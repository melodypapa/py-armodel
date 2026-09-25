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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, NameToken, PositiveInteger, String
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
        assert element.getArrayImplPolicy().getValue() == "payloadAsPointerToArray"
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
        assert element.getArraySizeHandling().getValue() == "allIndicesSameArraySize"
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
        assert element.getArraySizeSemantics().getValue() == "fixedSize"
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
        """Test ImplementationDataType initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        assert data_type is not None
        assert data_type.getShortName() == "TestImplementationDataType"
        assert data_type.dynamicArraySizeProfile is None
        assert data_type.isStructWithOptionalElement is None
        assert data_type.subElements == []
        assert data_type.symbolProps is None
        assert data_type.typeEmitter is None
        assert ImplementationDataType.CATEGORY_TYPE_REFERENCE == "TYPE_REFERENCE"
        assert ImplementationDataType.CATEGORY_TYPE_VALUE == "VALUE"
        assert ImplementationDataType.CATEGORY_TYPE_STRUCTURE == "STRUCTURE"
        assert ImplementationDataType.CATEGORY_DATA_REFERENCE == "DATA_REFERENCE"
        assert ImplementationDataType.CATEGORY_ARRAY == "ARRAY"

    def test_category_constants(self):
        """Test category constants"""
        assert ImplementationDataType.CATEGORY_TYPE_REFERENCE == "TYPE_REFERENCE"
        assert ImplementationDataType.CATEGORY_TYPE_VALUE == "VALUE"
        assert ImplementationDataType.CATEGORY_TYPE_STRUCTURE == "STRUCTURE"
        assert ImplementationDataType.CATEGORY_DATA_REFERENCE == "DATA_REFERENCE"
        assert ImplementationDataType.CATEGORY_ARRAY == "ARRAY"

    def test_get_dynamic_array_size_profile(self):
        """Test getDynamicArraySizeProfile method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getDynamicArraySizeProfile() is None

    def test_set_dynamic_array_size_profile(self):
        """Test setDynamicArraySizeProfile method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        test_value = String().setValue("TEST_PROFILE")
        result = data_type.setDynamicArraySizeProfile(test_value)
        assert result is data_type
        assert data_type.getDynamicArraySizeProfile() == test_value

    def test_set_dynamic_array_size_profile_none(self):
        """Test setDynamicArraySizeProfile with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        result = data_type.setDynamicArraySizeProfile(None)
        assert result is data_type
        assert data_type.getDynamicArraySizeProfile() is None

    def test_get_is_struct_with_optional_element(self):
        """Test getIsStructWithOptionalElement method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getIsStructWithOptionalElement() is None

    def test_set_is_struct_with_optional_element(self):
        """Test setIsStructWithOptionalElement method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        test_value = Boolean().setValue(True)
        result = data_type.setIsStructWithOptionalElement(test_value)
        assert result is data_type
        assert data_type.getIsStructWithOptionalElement() == test_value

    def test_set_is_struct_with_optional_element_none(self):
        """Test setIsStructWithOptionalElement with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        result = data_type.setIsStructWithOptionalElement(None)
        assert result is data_type
        assert data_type.getIsStructWithOptionalElement() is None

    def test_create_implementation_data_type_element(self):
        """Test createImplementationDataTypeElement method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        element = data_type.createImplementationDataTypeElement("Element")
        assert isinstance(element, ImplementationDataTypeElement)
        assert element.getShortName() == "Element"
        assert element in data_type.getSubElements()
        assert len(data_type.getSubElements()) == 1

    def test_get_sub_elements(self):
        """Test getSubElements method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getSubElements() == []

    def test_get_set_type_emitter(self):
        """Test setTypeEmitter/getTypeEmitter methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getTypeEmitter() is None

        value = NameToken().setValue("test_emitter")
        result = data_type.setTypeEmitter(value)
        assert result is data_type
        assert data_type.getTypeEmitter().getValue() == "test_emitter"

        data_type.setTypeEmitter(None)
        assert data_type.getTypeEmitter().getValue() == "test_emitter"

    def test_create_symbol_props(self):
        """Test createSymbolProps method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        symbol_props = data_type.createSymbolProps("SymbolProps")
        assert isinstance(symbol_props, SymbolProps)
        assert symbol_props.getShortName() == "SymbolProps"
        assert data_type.getSymbolProps() is symbol_props

    def test_get_symbol_props(self):
        """Test getSymbolProps method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getSymbolProps() is None

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")

        # Set all properties
        data_type.setDynamicArraySizeProfile(String().setValue("PROFILE"))
        data_type.setIsStructWithOptionalElement(Boolean().setValue(True))
        data_type.setTypeEmitter(NameToken().setValue("EMITTER"))

        # Verify all properties are set
        assert data_type.getDynamicArraySizeProfile().getValue() == "PROFILE"
        assert data_type.getIsStructWithOptionalElement().getValue() is True
        assert data_type.getTypeEmitter().getValue() == "EMITTER"


class TestArraySizeSemanticsEnum:
    """Test class for ArraySizeSemanticsEnum functionality (Table 5.10, p.253)."""

    def test_initialization(self):
        enum = ArraySizeSemanticsEnum()
        enum.setValue(ArraySizeSemanticsEnum.FIXED_SIZE)
        assert enum.getValue() == "fixedSize"

    def test_enum_values(self):
        assert ArraySizeSemanticsEnum.FIXED_SIZE == "fixedSize"
        assert ArraySizeSemanticsEnum.VARIABLE_SIZE == "variableSize"


class TestArrayImplPolicyEnum:
    def test_literals(self):
        """Test ArrayImplPolicyEnum literal values per AUTOSAR_CP_TPS_SoftwareComponentTemplate Table 5.18"""
        assert ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY == "payloadAsArray"
        assert ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY == "payloadAsPointerToArray"

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
        assert enum.getValue() == "payloadAsPointerToArray"

    def test_set_value_none_noop(self):
        """Test setValue(None) is a no-op"""
        enum = ArrayImplPolicyEnum()
        assert enum.setValue(None) is enum
        assert enum.getValue() == ""  # ARLiteral's empty representation for an unset literal
        enum.setValue(ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY)
        enum.setValue(None)
        assert enum.getValue() == "payloadAsArray"

    def test_validate_enum_value(self):
        """Test validateEnumValue accepts spec literals and rejects others"""
        enum = ArrayImplPolicyEnum()
        assert enum.validateEnumValue("payloadAsArray") is True
        assert enum.validateEnumValue("payloadAsPointerToArray") is True
        assert enum.validateEnumValue("bogus") is False

    def test_spec_note(self):
        """Test the Table 5.18 class note."""
        assert ArrayImplPolicyEnum.__doc__.strip() == "This meta-class provides values to configure the implementation of the payload part of an array."
