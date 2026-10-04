"""
This module contains tests for the BaseTypes module in MSR.AsamHdo.
"""

import typing
from abc import ABC

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
    """Heritage / API tests for the synced BaseTypeDefinition (Swc TPS Table 5.23, p.290)."""

    def test_base_type_definition_abstract_class(self):
        """Test that BaseTypeDefinition cannot be instantiated directly."""
        with pytest.raises(TypeError, match="BaseTypeDefinition is an abstract class"):
            BaseTypeDefinition()

    def test_base_shape(self):
        """Base column is ARObject only (Table 5.23); ABC marks the abstract convention."""
        assert BaseTypeDefinition.__bases__[0] is ARObject
        assert ABC in BaseTypeDefinition.__bases__

    def test_base_type_definition_concrete_subclass(self):
        """Test that a concrete subclass of BaseTypeDefinition can be instantiated."""
        base_type_def = BaseTypeDirectDefinition()
        assert isinstance(base_type_def, BaseTypeDefinition)
        assert isinstance(base_type_def, ARObject)
        # BaseTypeDefinition declares no own attributes (Table 5.23 Attribute rows: none)
        assert not any(name in BaseTypeDirectDefinition.__dict__ for name in ("baseTypeDefinition", "definition"))

    def test_class_docstring_matches_spec_note(self):
        assert BaseTypeDefinition.__doc__.strip() == "This meta-class represents the ability to define a basetype."


class TestBaseTypeDirectDefinition:
    """Test class for BaseTypeDirectDefinition class."""

    def test_base_shape(self):
        """Base column most-derived class is BaseTypeDefinition (Table 5.24)."""
        assert BaseTypeDirectDefinition.__bases__[0] is BaseTypeDefinition
        definition = BaseTypeDirectDefinition()
        assert isinstance(definition, BaseTypeDefinition)
        assert isinstance(definition, ARObject)

    def test_class_docstring_matches_spec_note(self):
        assert BaseTypeDirectDefinition.__doc__.strip() == "This BaseType is defined directly (as opposite to a derived BaseType)"

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

    def test_accessor_docstrings_match_spec_notes(self):
        """Getter docstrings are the Table 5.24 spec Notes verbatim; setters append the None-no-op sentence."""
        notes = {
            "BaseTypeEncoding": "This specifies, how an object of the current BaseType is encoded, e.g. in an ECU within a message sequence.",
            "BaseTypeSize": "Describes the length of the data type specified in the container in bits.",
            "ByteOrder": "This attribute specifies the byte order of the base type.",
            "MemAlignment": 'This attribute describes the alignment of the memory object in bits. E.g. "8" specifies, that the object in question is aligned to a byte while "32" specifies that it is aligned four byte. If the value is set to "0" the meaning shall be interpreted as "unspecified".',
            "NativeDeclaration": 'This attribute describes the declaration of such a base type in the native programming language, primarily in the Programming language C. This can then be used by a code generator to include the necessary declarations into a header file. For example BaseType with shortName: "MyUnsignedInt" native Declaration: "unsigned short" Results in typedef unsigned short MyUnsignedInt; If the attribute is not defined the referring Implementation DataTypes will not be generated as a typedef by RTE. If a nativeDeclaration type is given it shall fulfill the characteristic given by basetypeEncoding and baseType Size. This is required to ensure the consistent handling and interpretation by software components, RTE, COM and MCM systems.',
        }
        for attr, note in notes.items():
            getter = getattr(BaseTypeDirectDefinition, "get" + attr)
            setter = getattr(BaseTypeDirectDefinition, "set" + attr)
            field_name = attr[0].lower() + attr[1:]
            assert getter.__doc__.strip() == note, "getter docstring drift on %s" % field_name
            assert setter.__doc__.strip() == note + " A None value is a no-op and does not overwrite an existing %s." % field_name, "setter docstring drift on %s" % field_name

    def test_setter_return_type_hints_resolve(self):
        """Setter return annotations resolve to the class itself under typing.get_type_hints (Rule 0003)."""
        for attr in ("BaseTypeEncoding", "BaseTypeSize", "ByteOrder", "MemAlignment", "NativeDeclaration"):
            setter = getattr(BaseTypeDirectDefinition, "set" + attr)
            assert typing.get_type_hints(setter).get("return") is BaseTypeDirectDefinition


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
