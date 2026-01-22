import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import AbstractImplementationDataType, AbstractImplementationDataTypeElement, ImplementationDataTypeElement, ImplementationDataType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Boolean, String, ARBoolean
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps


class TestAbstractImplementationDataTypeElement:
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
    def test_initialization(self):
        """Test ImplementationDataTypeElement initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        
        assert element is not None
        assert element.getShortName() == "TestElement"
        assert element.arrayImplPolicy is None
        assert element.arraySize is None
        assert element.arraySizeHandling is None
        assert element.arraySizeSemantics is None
        assert element.isOptional is None
        assert element.subElements == []
        assert element.swDataDefProps is None
        assert ImplementationDataTypeElement.ARRAY_SIZE_SEMANTICS_FIXED_SIZE == "FIXED-SIZE"
        assert ImplementationDataTypeElement.ARRAY_SIZE_SEMANTICS_VARIABLE_SIZE == "VARIABLE_SIZE"

    def test_get_array_size_semantics_constants(self):
        """Test array size semantics constants"""
        assert ImplementationDataTypeElement.ARRAY_SIZE_SEMANTICS_FIXED_SIZE == "FIXED-SIZE"
        assert ImplementationDataTypeElement.ARRAY_SIZE_SEMANTICS_VARIABLE_SIZE == "VARIABLE_SIZE"

    def test_get_array_impl_policy(self):
        """Test getArrayImplPolicy method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getArrayImplPolicy() is None

    def test_set_array_impl_policy(self):
        """Test setArrayImplPolicy method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = ARLiteral().setValue("TEST_POLICY")
        result = element.setArrayImplPolicy(test_value)
        assert result is element
        assert element.getArrayImplPolicy() == test_value

    def test_set_array_impl_policy_none(self):
        """Test setArrayImplPolicy with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setArrayImplPolicy(None)
        assert result is element
        assert element.getArrayImplPolicy() is None

    def test_get_array_size(self):
        """Test getArraySize method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getArraySize() is None

    def test_set_array_size(self):
        """Test setArraySize method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = ARNumerical().setValue(10)
        result = element.setArraySize(test_value)
        assert result is element
        assert element.getArraySize() == test_value

    def test_set_array_size_none(self):
        """Test setArraySize with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setArraySize(None)
        assert result is element
        assert element.getArraySize() is None

    def test_get_array_size_handling(self):
        """Test getArraySizeHandling method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getArraySizeHandling() is None

    def test_set_array_size_handling(self):
        """Test setArraySizeHandling method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = ARLiteral().setValue("TEST_HANDLING")
        result = element.setArraySizeHandling(test_value)
        assert result is element
        assert element.getArraySizeHandling() == test_value

    def test_set_array_size_handling_none(self):
        """Test setArraySizeHandling with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setArraySizeHandling(None)
        assert result is element
        assert element.getArraySizeHandling() is None

    def test_get_array_size_semantics(self):
        """Test getArraySizeSemantics method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getArraySizeSemantics() is None

    def test_set_array_size_semantics(self):
        """Test setArraySizeSemantics method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = ARLiteral().setValue("FIXED-SIZE")
        result = element.setArraySizeSemantics(test_value)
        assert result is element
        assert element.getArraySizeSemantics() == test_value

    def test_set_array_size_semantics_none(self):
        """Test setArraySizeSemantics with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setArraySizeSemantics(None)
        assert result is element
        assert element.getArraySizeSemantics() is None

    def test_get_is_optional(self):
        """Test getIsOptional method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getIsOptional() is None

    def test_set_is_optional(self):
        """Test setIsOptional method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = ARBoolean().setValue(True)
        result = element.setIsOptional(test_value)
        assert result is element
        assert element.getIsOptional() == test_value

    def test_set_is_optional_none(self):
        """Test setIsOptional with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setIsOptional(None)
        assert result is element
        assert element.getIsOptional() is None

    def test_get_sw_data_def_props(self):
        """Test getSwDataDefProps method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getSwDataDefProps() is None

    def test_set_sw_data_def_props(self):
        """Test setSwDataDefProps method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        test_value = SwDataDefProps()
        result = element.setSwDataDefProps(test_value)
        assert result is element
        assert element.getSwDataDefProps() == test_value

    def test_set_sw_data_def_props_none(self):
        """Test setSwDataDefProps with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        result = element.setSwDataDefProps(None)
        assert result is element
        assert element.getSwDataDefProps() is None

    def test_create_implementation_data_type_element(self):
        """Test createImplementationDataTypeElement method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        
        sub_element = element.createImplementationDataTypeElement("SubElement")
        assert isinstance(sub_element, ImplementationDataTypeElement)
        assert sub_element.getShortName() == "SubElement"
        assert sub_element in element.getSubElements()
        assert len(element.getSubElements()) == 1

    def test_create_implementation_data_type_element_duplicate(self):
        """Test createImplementationDataTypeElement with duplicate name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        
        sub_element1 = element.createImplementationDataTypeElement("SubElement")
        sub_element2 = element.createImplementationDataTypeElement("SubElement")  # Should return same instance
        
        assert sub_element1 is sub_element2
        assert len(element.getSubElements()) == 1

    def test_get_sub_elements(self):
        """Test getSubElements method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        assert element.getSubElements() == []

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = ImplementationDataTypeElement(ar_root, "TestElement")
        
        # Set all properties
        element.setArrayImplPolicy(ARLiteral().setValue("POLICY"))
        element.setArraySize(ARNumerical().setValue(10))
        element.setArraySizeHandling(ARLiteral().setValue("HANDLING"))
        element.setArraySizeSemantics(ARLiteral().setValue("FIXED-SIZE"))
        element.setIsOptional(ARBoolean().setValue(True))
        element.setSwDataDefProps(SwDataDefProps())
        
        # Verify all properties are set
        assert element.getArrayImplPolicy().getValue() == "POLICY"
        assert element.getArraySize().getValue() == 10
        assert element.getArraySizeHandling().getValue() == "HANDLING"
        assert element.getArraySizeSemantics().getValue() == "FIXED-SIZE"
        assert element.getIsOptional().getValue() is True
        assert element.getSwDataDefProps() is not None


class TestAbstractImplementationDataType:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractImplementationDataType abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError, match="AbstractImplementationDataType is an abstract class."):
            AbstractImplementationDataType(ar_root, "TestAbstractImplementationDataType")


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

    def test_get_array_element_type(self):
        """Test getArrayElementType method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getArrayElementType() is None

    def test_set_array_element_type(self):
        """Test setArrayElementType method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        data_type.setArrayElementType("test_type")
        assert data_type.getArrayElementType() == "test_type"

    def test_set_type_emitter(self):
        """Test setTypeEmitter method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        result = data_type.setTypeEmitter("test_emitter")
        assert result is data_type
        assert data_type.getTypeEmitter() == "test_emitter"

    def test_get_type_emitter(self):
        """Test getTypeEmitter method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getTypeEmitter() is None

    def test_set_struct_element_type(self):
        """Test setStructElementType method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        result = data_type.setStructElementType("test_struct_type")
        assert result is data_type
        assert data_type.getStructElementType() == "test_struct_type"

    def test_get_struct_element_type(self):
        """Test getStructElementType method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_type = ImplementationDataType(ar_root, "TestImplementationDataType")
        assert data_type.getStructElementType() is None

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
        data_type.setTypeEmitter("EMITTER")
        
        # Verify all properties are set
        assert data_type.getDynamicArraySizeProfile().getValue() == "PROFILE"
        assert data_type.getIsStructWithOptionalElement().getValue() is True
        assert data_type.getTypeEmitter() == "EMITTER"