"""
This module contains comprehensive tests for the DataPrototypes module in SWComponentTemplate.Datatype.
Tests cover all classes and methods in the DataPrototypes.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationArrayElement,
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AtpPrototype,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)


class TestAtpPrototype:
    """Test class for AtpPrototype abstract class."""

    def test_atp_prototype_abstract(self):
        """Test that AtpPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AtpPrototype(ar_root, "TestAtpPrototype")


class TestDataPrototype:
    """Test class for DataPrototype abstract class."""

    def test_data_prototype_abstract(self):
        """Test that DataPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            DataPrototype(ar_root, "TestDataPrototype")


class TestAutosarDataPrototype:
    """Test class for AutosarDataPrototype abstract class."""

    def test_autosar_data_prototype_abstract(self):
        """Test that AutosarDataPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AutosarDataPrototype(ar_root, "TestAutosarDataPrototype")


class TestVariableDataPrototype:
    """Test class for VariableDataPrototype class."""

    def test_variable_data_prototype_initialization(self):
        """Test VariableDataPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_proto = VariableDataPrototype(ar_root, "TestVariableDataPrototype")

        assert var_proto.parent == ar_root
        assert var_proto.short_name == "TestVariableDataPrototype"
        assert var_proto.swDataDefProps is None
        assert var_proto.typeTRef is None
        assert var_proto.initValue is None

        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        sw_data_def = SwDataDefProps()
        var_proto.setSwDataDefProps(sw_data_def)
        assert var_proto.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TRefType,
        )
        type_ref = TRefType()
        type_ref.setValue("/Type/Ref")
        var_proto.setTypeTRef(type_ref)
        assert var_proto.getTypeTRef() == type_ref

        # Test initValue methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
            TextValueSpecification,
        )
        init_value = TextValueSpecification()
        var_proto.setInitValue(init_value)
        assert var_proto.getInitValue() == init_value


class TestApplicationCompositeElementDataPrototype:
    """Test class for ApplicationCompositeElementDataPrototype abstract class."""

    def test_application_composite_element_data_prototype_abstract(self):
        """Test that ApplicationCompositeElementDataPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationCompositeElementDataPrototype(ar_root, "TestApplicationCompositeElementDataPrototype")


class TestApplicationArrayElement:
    """Test class for ApplicationArrayElement class."""

    def test_application_array_element_initialization(self):
        """Test ApplicationArrayElement initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")

        assert array_element.parent == ar_root
        assert array_element.short_name == "TestApplicationArrayElement"
        assert array_element.swDataDefProps is None
        assert array_element.typeTRef is None
        assert array_element.arraySizeHandling is None
        assert array_element.arraySizeSemantics is None
        assert array_element.indexDataTypeRef is None
        assert array_element.maxNumberOfElements is None

        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        sw_data_def = SwDataDefProps()
        array_element.setSwDataDefProps(sw_data_def)
        assert array_element.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        type_ref = RefType()
        type_ref.setValue("/Type/Ref")
        array_element.setTypeTRef(type_ref)
        assert array_element.getTypeTRef() == type_ref

        # Test arraySizeHandling methods
        array_size_handling = "test_handling"
        array_element.setArraySizeHandling(array_size_handling)
        assert array_element.getArraySizeHandling() == array_size_handling

        # Test arraySizeSemantics methods
        array_size_semantics = "test_semantics"
        array_element.setArraySizeSemantics(array_size_semantics)
        assert array_element.getArraySizeSemantics() == array_size_semantics

        # Test indexDataTypeRef methods
        index_ref = RefType()
        index_ref.setValue("/Index/Type")
        array_element.setIndexDataTypeRef(index_ref)
        assert array_element.getIndexDataTypeRef() == index_ref

        # Test maxNumberOfElements methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            PositiveInteger,
        )
        max_num = PositiveInteger()
        max_num.setValue(100)
        array_element.setMaxNumberOfElements(max_num)
        assert array_element.getMaxNumberOfElements() == max_num


class TestApplicationRecordElement:
    """Test class for ApplicationRecordElement class."""

    def test_application_record_element_initialization(self):
        """Test ApplicationRecordElement initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_element = ApplicationRecordElement(ar_root, "TestApplicationRecordElement")

        assert record_element.parent == ar_root
        assert record_element.short_name == "TestApplicationRecordElement"
        assert record_element.swDataDefProps is None
        assert record_element.typeTRef is None
        assert record_element.isOptional is None

        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        sw_data_def = SwDataDefProps()
        record_element.setSwDataDefProps(sw_data_def)
        assert record_element.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        type_ref = RefType()
        type_ref.setValue("/Type/Ref")
        record_element.setTypeTRef(type_ref)
        assert record_element.getTypeTRef() == type_ref

        # Test isOptional methods
        is_optional = True
        record_element.setIsOptional(is_optional)
        assert record_element.getIsOptional() == is_optional


class TestParameterDataPrototype:
    """Test class for ParameterDataPrototype class."""

    def test_parameter_data_prototype_initialization(self):
        """Test ParameterDataPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_proto = ParameterDataPrototype(ar_root, "TestParameterDataPrototype")

        assert param_proto.parent == ar_root
        assert param_proto.short_name == "TestParameterDataPrototype"
        assert param_proto.swDataDefProps is None
        assert param_proto.typeTRef is None
        assert param_proto.initValue is None

        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        sw_data_def = SwDataDefProps()
        param_proto.setSwDataDefProps(sw_data_def)
        assert param_proto.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TRefType,
        )
        type_ref = TRefType()
        type_ref.setValue("/Type/Ref")
        param_proto.setTypeTRef(type_ref)
        assert param_proto.getTypeTRef() == type_ref

        # Test initValue methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
            TextValueSpecification,
        )
        init_value = TextValueSpecification()
        param_proto.setInitValue(init_value)
        assert param_proto.getInitValue() == init_value
