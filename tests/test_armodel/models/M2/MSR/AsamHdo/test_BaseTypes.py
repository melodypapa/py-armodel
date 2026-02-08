"""
This module contains tests for the BaseTypes module in MSR.AsamHdo.
"""
import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    ByteOrderEnum,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import *


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

    def test_base_type_direct_definition_setters_and_getters(self):
        """Test the setters and getters for BaseTypeDirectDefinition class."""
        base_type_direct_def = BaseTypeDirectDefinition()

        # Create test objects
        encoding = "some_encoding"
        size = ARNumerical()
        byte_order = ByteOrderEnum()
        alignment = ARNumerical()
        native_decl = "native_declaration"

        # Test setBaseTypeEncoding and getBaseTypeEncoding
        result = base_type_direct_def.setBaseTypeEncoding(encoding)
        assert base_type_direct_def.getBaseTypeEncoding() == encoding
        assert result == base_type_direct_def

        # Test setBaseTypeSize and getBaseTypeSize
        result = base_type_direct_def.setBaseTypeSize(size)
        assert base_type_direct_def.getBaseTypeSize() == size
        assert result == base_type_direct_def

        # Test setByteOrder and getByteOrder
        result = base_type_direct_def.setByteOrder(byte_order)
        assert base_type_direct_def.getByteOrder() == byte_order
        assert result == base_type_direct_def

        # Test setMemAlignment and getMemAlignment
        result = base_type_direct_def.setMemAlignment(alignment)
        assert base_type_direct_def.getMemAlignment() == alignment
        assert result == base_type_direct_def

        # Test setNativeDeclaration and getNativeDeclaration
        result = base_type_direct_def.setNativeDeclaration(native_decl)
        assert base_type_direct_def.getNativeDeclaration() == native_decl
        assert result == base_type_direct_def


class TestBaseType:
    """Test class for BaseType abstract class."""

    def test_base_type_abstract_class(self):
        """Test that BaseType cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            BaseType(None, "test_name")

    def test_base_type_definition_methods(self):
        """Test the getBaseTypeDefinition and setBaseTypeDefinition methods."""
        # Create a concrete subclass for testing
        class ConcreteBaseType(BaseType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        concrete_type = ConcreteBaseType(parent_obj, "test_type")

        # Test initial baseTypeDefinition
        assert concrete_type.getBaseTypeDefinition() is not None

        # Create a new definition to test setter
        new_def = BaseTypeDirectDefinition()
        result = concrete_type.setBaseTypeDefinition(new_def)
        assert concrete_type.getBaseTypeDefinition() == new_def
        assert result == concrete_type


class TestSwBaseType:
    """Test class for SwBaseType class."""

    def test_sw_base_type_initialization(self):
        """Test that a SwBaseType object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sw_base_type = SwBaseType(parent_obj, "test_name")

        # Check that it inherits from BaseType and has baseTypeDefinition
        assert sw_base_type.getBaseTypeDefinition() is not None
