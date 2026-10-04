"""
This module contains tests for the BaseTypes module in MSR.AsamHdo.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    BaseTypeEncodingString,
    ByteOrderEnum,
    NativeDeclarationString,
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import (
    BaseType,
    BaseTypeDefinition,
    BaseTypeDirectDefinition,
    SwBaseType,
)


class TestBaseTypeDefinition:
    """Test class for BaseTypeDefinition class."""

    def test_base_type_definition_abstract_class(self):
        """Test that BaseTypeDefinition cannot be instantiated directly."""
        with pytest.raises(TypeError, match="BaseTypeDefinition is an abstract class"):
            BaseTypeDefinition()

    def test_base_type_definition_concrete_subclass(self):
        """Test that a concrete subclass of BaseTypeDefinition can be instantiated."""
        base_type_def = BaseTypeDirectDefinition()
        # BaseTypeDefinition inherits from ARObject, so we just check it's created
        assert base_type_def is not None


class TestBaseTypeDirectDefinition:
    """Test class for BaseTypeDirectDefinition class."""

    def test_base_type_direct_definition_initialization(self):
        """Test that a BaseTypeDirectDefinition object can be initialized with default values."""
        base_type_direct_def = BaseTypeDirectDefinition()
        assert base_type_direct_def.baseTypeEncoding is None
        assert base_type_direct_def.baseTypeSize is None
        assert base_type_direct_def.byteOrder is None
        assert base_type_direct_def.memAlignment is None
        assert base_type_direct_def.nativeDeclaration is None

    def test_base_type_direct_definition_base_type_encoding(self):
        """Test get/set of baseTypeEncoding owned by BaseTypeDirectDefinition (Table 5.24)."""
        base_type_direct_def = BaseTypeDirectDefinition()

        assert base_type_direct_def.getBaseTypeEncoding() is None

        encoding = BaseTypeEncodingString().setValue("IEEE754")
        result = base_type_direct_def.setBaseTypeEncoding(encoding)
        assert base_type_direct_def.getBaseTypeEncoding() == encoding
        assert isinstance(base_type_direct_def.getBaseTypeEncoding(), BaseTypeEncodingString)
        assert result == base_type_direct_def

    def test_base_type_direct_definition_base_type_encoding_none_noop(self):
        """A None value must not overwrite an existing baseTypeEncoding."""
        base_type_direct_def = BaseTypeDirectDefinition()
        encoding = BaseTypeEncodingString().setValue("IEEE754")
        base_type_direct_def.setBaseTypeEncoding(encoding)

        result = base_type_direct_def.setBaseTypeEncoding(None)
        assert base_type_direct_def.getBaseTypeEncoding() == encoding
        assert result == base_type_direct_def

    def test_base_type_direct_definition_setters_and_getters(self):
        """Test the setters and getters for BaseTypeDirectDefinition class."""
        base_type_direct_def = BaseTypeDirectDefinition()

        # Create test objects using spec-accurate primitive types
        size = PositiveInteger().setValue("32")
        encoding = BaseTypeEncodingString().setValue("IEEE754")
        byte_order = ByteOrderEnum().setValue("MOST-SIGNIFICANT-BYTE-FIRST")
        alignment = PositiveInteger().setValue("8")
        native_decl = NativeDeclarationString().setValue("unsigned int")

        # Test setBaseTypeSize and getBaseTypeSize
        result = base_type_direct_def.setBaseTypeSize(size)
        assert base_type_direct_def.getBaseTypeSize() == size
        assert isinstance(base_type_direct_def.getBaseTypeSize(), PositiveInteger)
        assert result == base_type_direct_def

        # Test setBaseTypeEncoding and getBaseTypeEncoding
        result = base_type_direct_def.setBaseTypeEncoding(encoding)
        assert base_type_direct_def.getBaseTypeEncoding() == encoding
        assert isinstance(base_type_direct_def.getBaseTypeEncoding(), BaseTypeEncodingString)
        assert result == base_type_direct_def

        # Test setByteOrder and getByteOrder
        result = base_type_direct_def.setByteOrder(byte_order)
        assert base_type_direct_def.getByteOrder() == byte_order
        assert isinstance(base_type_direct_def.getByteOrder(), ByteOrderEnum)
        assert result == base_type_direct_def

        # Test setMemAlignment and getMemAlignment
        result = base_type_direct_def.setMemAlignment(alignment)
        assert base_type_direct_def.getMemAlignment() == alignment
        assert isinstance(base_type_direct_def.getMemAlignment(), PositiveInteger)
        assert result == base_type_direct_def

        # Test setNativeDeclaration and getNativeDeclaration
        result = base_type_direct_def.setNativeDeclaration(native_decl)
        assert base_type_direct_def.getNativeDeclaration() == native_decl
        assert isinstance(base_type_direct_def.getNativeDeclaration(), NativeDeclarationString)
        assert result == base_type_direct_def

    def test_base_type_direct_definition_setters_none_noop(self):
        """None values must not overwrite existing attributes."""
        base_type_direct_def = BaseTypeDirectDefinition()
        size = PositiveInteger().setValue("32")
        encoding = BaseTypeEncodingString().setValue("IEEE754")
        byte_order = ByteOrderEnum().setValue("MOST-SIGNIFICANT-BYTE-FIRST")
        alignment = PositiveInteger().setValue("8")
        native_decl = NativeDeclarationString().setValue("unsigned int")

        base_type_direct_def.setBaseTypeSize(size)
        base_type_direct_def.setBaseTypeEncoding(encoding)
        base_type_direct_def.setByteOrder(byte_order)
        base_type_direct_def.setMemAlignment(alignment)
        base_type_direct_def.setNativeDeclaration(native_decl)

        base_type_direct_def.setBaseTypeSize(None)
        base_type_direct_def.setBaseTypeEncoding(None)
        base_type_direct_def.setByteOrder(None)
        base_type_direct_def.setMemAlignment(None)
        base_type_direct_def.setNativeDeclaration(None)

        assert base_type_direct_def.getBaseTypeSize() == size
        assert base_type_direct_def.getBaseTypeEncoding() == encoding
        assert base_type_direct_def.getByteOrder() == byte_order
        assert base_type_direct_def.getMemAlignment() == alignment
        assert base_type_direct_def.getNativeDeclaration() == native_decl


class TestBaseType:
    """Heritage / API tests for the synced BaseType (Swc TPS Table 5.26, p.292)."""

    def test_base_type_abstract_class(self):
        """Test that BaseType cannot be instantiated directly."""
        with pytest.raises(TypeError, match="BaseType is an abstract class"):
            BaseType(None, "test_name")

    def test_base_shape(self):
        """Base column most-derived class is ARElement (Table 5.26)."""
        assert BaseType.__bases__[0] is ARElement
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "test_type")
        assert isinstance(sw_base_type, BaseType)
        assert isinstance(sw_base_type, ARElement)
        assert isinstance(sw_base_type, Identifiable)
        assert isinstance(sw_base_type, ARObject)

    def test_initialization(self):
        """Defaults through the concrete subclass SwBaseType (Table 5.26 baseTypeDefinition row)."""
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "test_type")

        assert sw_base_type.parent is parent_obj
        assert sw_base_type.short_name == "test_type"

        definition = sw_base_type.getBaseTypeDefinition()
        assert isinstance(definition, BaseTypeDirectDefinition)
        assert definition.getBaseTypeEncoding() is None
        assert definition.getBaseTypeSize() is None
        assert definition.getByteOrder() is None
        assert definition.getMemAlignment() is None
        assert definition.getNativeDeclaration() is None

    def test_class_docstring_matches_spec_note(self):
        assert BaseType.__doc__.strip() == (
            "This abstract meta-class represents the ability to specify a platform dependent base type.\n\n"
            "    [constr_1910] Existence of attribute BaseType.baseTypeDefinition: For each BaseType "
            "(which will be utilized in the form of SwBaseType), the aggregation in the role baseTypeDefinition "
            "shall exist at the time when the contract phase generation is executed."
        )

    def test_base_type_definition_docstrings_match_spec_note(self):
        note = "This is the actual definition of the base type."
        assert BaseType.getBaseTypeDefinition.__doc__.strip() == note
        assert BaseType.setBaseTypeDefinition.__doc__.strip() == (note + " A None value is a no-op and does not overwrite an existing baseTypeDefinition.")

    def test_get_set_base_type_definition(self):
        """Setter returns self, value round-trips, None is a no-op."""
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "test_type")

        definition = BaseTypeDirectDefinition()
        result = sw_base_type.setBaseTypeDefinition(definition)
        assert sw_base_type.getBaseTypeDefinition() is definition
        assert result is sw_base_type

        result = sw_base_type.setBaseTypeDefinition(None)
        assert sw_base_type.getBaseTypeDefinition() is definition
        assert result is sw_base_type

    def test_base_type_definition_value_round_trip(self):
        """Values set on the aggregated definition are visible one level up."""
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "test_type")

        definition = sw_base_type.getBaseTypeDefinition()
        definition.setBaseTypeSize(PositiveInteger().setValue("32"))
        definition.setBaseTypeEncoding(BaseTypeEncodingString().setValue("IEEE754"))

        assert sw_base_type.getBaseTypeDefinition().getBaseTypeSize().getValue() == 32
        assert sw_base_type.getBaseTypeDefinition().getBaseTypeEncoding().getValue() == "IEEE754"


class TestSwBaseType:
    """Heritage / API tests for the synced SwBaseType (Swc TPS Table 5.22, p.290)."""

    def test_base_shape(self):
        """Base column most-derived class is BaseType (Table 5.22)."""
        assert SwBaseType.__bases__[0] is BaseType
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "uint8")
        assert isinstance(sw_base_type, BaseType)
        assert isinstance(sw_base_type, ARElement)
        assert isinstance(sw_base_type, Identifiable)
        assert isinstance(sw_base_type, ARObject)

    def test_initialization(self):
        """SwBaseType declares no own attributes (Table 5.22 Attribute rows: none)."""
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "uint8")

        assert sw_base_type.parent is parent_obj
        assert sw_base_type.short_name == "uint8"

        definition = sw_base_type.getBaseTypeDefinition()
        assert isinstance(definition, BaseTypeDirectDefinition)
        assert definition.getBaseTypeEncoding() is None
        assert definition.getBaseTypeSize() is None
        assert definition.getByteOrder() is None
        assert definition.getMemAlignment() is None
        assert definition.getNativeDeclaration() is None

    def test_class_docstring_matches_spec_note(self):
        assert SwBaseType.__doc__.strip() == "This meta-class represents a base type used within ECU software."

    def test_set_base_type_definition_via_concrete_class(self):
        """Base accessors exercised through the concrete subclass; setter returns self; None no-op."""
        parent_obj = ARPackage(None, "parent_test")
        sw_base_type = SwBaseType(parent_obj, "uint8")

        definition = BaseTypeDirectDefinition()
        assert sw_base_type.setBaseTypeDefinition(definition) is sw_base_type
        assert sw_base_type.getBaseTypeDefinition() is definition
        assert sw_base_type.setBaseTypeDefinition(None) is sw_base_type
        assert sw_base_type.getBaseTypeDefinition() is definition
