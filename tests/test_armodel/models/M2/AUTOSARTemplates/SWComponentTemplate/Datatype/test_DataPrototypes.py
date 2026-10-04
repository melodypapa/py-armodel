"""
This module contains comprehensive tests for the DataPrototypes module in SWComponentTemplate.Datatype.
Tests cover all classes and methods in the DataPrototypes.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationArrayElement,
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ArraySizeHandlingEnum


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

    def test_data_prototype_sw_data_def_props_via_concrete_subclass(self):
        """Test swDataDefProps accessors through a concrete subclass."""
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = VariableDataPrototype(ar_root, "TestDataPrototype")

        assert prototype.getSwDataDefProps() is None

        props = SwDataDefProps()
        prototype.setSwDataDefProps(props)
        assert prototype.getSwDataDefProps() == props

        prototype.setSwDataDefProps(None)
        assert prototype.getSwDataDefProps() == props


class TestDataPrototypeHeritage:
    """Heritage-drift audit for DataPrototype after AtpPrototype re-parent (AtpBlueprintable -> AtpFeature).

    DataPrototype's spec Base closure (SWCT Table 5.28) is
    ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable --
    AtpBlueprintable is NOT in the closure, so losing it transitively (via the AtpPrototype
    re-parent) is spec-correct.
    """

    def test_bases_are_spec_correct(self):
        """DataPrototype's direct base is AtpPrototype; AtpBlueprintable is absent from the MRO."""
        assert DataPrototype.__bases__[0] is AtpPrototype
        assert AtpBlueprintable not in DataPrototype.__mro__
        assert issubclass(DataPrototype, AtpPrototype)
        assert issubclass(DataPrototype, Identifiable)
        assert issubclass(DataPrototype, ARObject)
        assert issubclass(DataPrototype, AtpPrototype)

    def test_concrete_subclass_reaches_inherited_members(self):
        """A concrete DataPrototype subclass initializes through the AtpPrototype -> Identifiable chain."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = VariableDataPrototype(ar_root, "TestDataPrototype")

        assert isinstance(prototype, DataPrototype)
        assert isinstance(prototype, AtpPrototype)
        assert isinstance(prototype, Identifiable)
        assert isinstance(prototype, ARObject)
        assert AtpBlueprintable not in type(prototype).__mro__
        assert prototype.getParent() == ar_root
        assert prototype.getShortName() == "TestDataPrototype"


class TestAutosarDataPrototype:
    """Test class for AutosarDataPrototype abstract class."""

    def test_autosar_data_prototype_abstract(self):
        """Test that AutosarDataPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AutosarDataPrototype(ar_root, "TestAutosarDataPrototype")

    def test_autosar_data_prototype_type_t_ref_via_concrete_subclass(self):
        """Test typeTRef accessors through a concrete subclass."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = VariableDataPrototype(ar_root, "TestAutosarDataPrototype")

        assert prototype.getTypeTRef() is None

        type_ref = TRefType()
        type_ref.setValue("/Type/Ref")
        prototype.setTypeTRef(type_ref)
        assert prototype.getTypeTRef() == type_ref

        prototype.setTypeTRef(None)
        assert prototype.getTypeTRef() == type_ref


class TestVariableDataPrototype:
    """Test class for VariableDataPrototype class (R23-11 Table 5.31)."""

    def test_initialization(self):
        """Test VariableDataPrototype initialization defaults and isinstance chain."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_proto = VariableDataPrototype(ar_root, "TestVariableDataPrototype")

        assert var_proto.parent == ar_root
        assert var_proto.short_name == "TestVariableDataPrototype"
        assert var_proto.swDataDefProps is None
        assert var_proto.typeTRef is None
        assert var_proto.initValue is None
        assert isinstance(var_proto, AutosarDataPrototype)
        assert isinstance(var_proto, DataPrototype)
        assert isinstance(var_proto, AtpPrototype)
        assert isinstance(var_proto, Identifiable)
        assert isinstance(var_proto, ARObject)

    def test_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 5.31)."""
        assert VariableDataPrototype.__doc__.strip() == (
            "A VariableDataPrototype represents a formalized generic piece of information "
            "that is typically mutable by the application software layer. "
            "VariableDataPrototype is used in various contexts and the specific context "
            "gives the otherwise generic VariableDataPrototype a dedicated semantics."
        )

    def test_init_value_round_trip(self):
        """initValue round-trip with chaining, and None is a no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_proto = VariableDataPrototype(ar_root, "TestVariableDataPrototype")

        init_value = TextValueSpecification()
        result = var_proto.setInitValue(init_value)
        assert result is var_proto
        assert var_proto.getInitValue() == init_value

        var_proto.setInitValue(None)
        assert var_proto.getInitValue() == init_value


class TestApplicationCompositeElementDataPrototype:
    """Test class for ApplicationCompositeElementDataPrototype abstract class."""

    def test_application_composite_element_data_prototype_abstract(self):
        """Test that ApplicationCompositeElementDataPrototype is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            ApplicationCompositeElementDataPrototype(ar_root, "TestApplicationCompositeElementDataPrototype")

    def test_application_composite_element_data_prototype_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")
        type_ref = TRefType()
        type_ref.setValue("/Types/Application")
        type_ref.setDest("APPLICATION-DATA-TYPE")

        assert isinstance(array_element, ApplicationCompositeElementDataPrototype)
        assert array_element.getTypeTRef() is None
        assert array_element.setTypeTRef(type_ref) is array_element
        assert array_element.getTypeTRef() is type_ref
        array_element.setTypeTRef(None)
        assert array_element.getTypeTRef() is type_ref
        assert ApplicationCompositeElementDataPrototype.__doc__.strip() == (
            "This class represents a data prototype which is aggregated within a composite application data type (record or array). "
            "It is introduced to provide a better distinction between target and context in instance Refs."
        )


class TestApplicationArrayElement:
    """Test class for ApplicationArrayElement class."""

    def test_application_array_element_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")

        assert isinstance(array_element, ApplicationCompositeElementDataPrototype)
        assert array_element.parent == ar_root
        assert array_element.short_name == "TestApplicationArrayElement"
        assert array_element.swDataDefProps is None
        assert array_element.typeTRef is None
        assert array_element.arraySizeHandling is None
        assert array_element.arraySizeSemantics is None
        assert array_element.indexDataTypeRef is None
        assert array_element.maxNumberOfElements is None

    def test_get_set_array_size_handling(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")
        handling = ArraySizeHandlingEnum().setValue(ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE)

        assert array_element.setArraySizeHandling(handling) is array_element
        assert array_element.getArraySizeHandling() is handling
        assert array_element.getArraySizeHandling().getValue() == "allIndicesSameArraySize"

        array_element.setArraySizeHandling(None)
        assert array_element.getArraySizeHandling() is handling

    def test_get_set_array_size_semantics(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")
        semantics = ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.VARIABLE_SIZE)

        assert array_element.setArraySizeSemantics(semantics) is array_element
        assert array_element.getArraySizeSemantics() is semantics
        assert array_element.getArraySizeSemantics().getValue() == "variableSize"

        array_element.setArraySizeSemantics(None)
        assert array_element.getArraySizeSemantics() is semantics

    def test_get_set_index_data_type_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")
        index_ref = RefType()
        index_ref.setValue("/DataTypes/IndexPrimitiveDataType")
        index_ref.setDest("APPLICATION-PRIMITIVE-DATA-TYPE")

        assert array_element.setIndexDataTypeRef(index_ref) is array_element
        assert array_element.getIndexDataTypeRef() is index_ref
        assert array_element.getIndexDataTypeRef().getValue() == "/DataTypes/IndexPrimitiveDataType"
        assert array_element.getIndexDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"

        array_element.setIndexDataTypeRef(None)
        assert array_element.getIndexDataTypeRef() is index_ref

    def test_get_set_max_number_of_elements(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")
        max_num = PositiveInteger().setValue("4")

        assert array_element.setMaxNumberOfElements(max_num) is array_element
        assert array_element.getMaxNumberOfElements() is max_num
        assert array_element.getMaxNumberOfElements().getValue() == 4

        array_element.setMaxNumberOfElements(None)
        assert array_element.getMaxNumberOfElements() is max_num

    def test_inherited_base_accessors_via_concrete_subclass(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        array_element = ApplicationArrayElement(ar_root, "TestApplicationArrayElement")

        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        sw_data_def = SwDataDefProps()
        assert array_element.setSwDataDefProps(sw_data_def) is array_element
        assert array_element.getSwDataDefProps() is sw_data_def
        array_element.setSwDataDefProps(None)
        assert array_element.getSwDataDefProps() is sw_data_def

        type_ref = TRefType()
        type_ref.setValue("/Types/Application")
        type_ref.setDest("APPLICATION-DATA-TYPE")
        assert array_element.setTypeTRef(type_ref) is array_element
        assert array_element.getTypeTRef() is type_ref
        array_element.setTypeTRef(None)
        assert array_element.getTypeTRef() is type_ref

    def test_class_docstring_matches_spec_note(self):
        assert ApplicationArrayElement.__doc__.strip() == "Describes the properties of the elements of an application array data type."

    def test_get_array_size_handling_docstring_verbatim(self):
        assert ApplicationArrayElement.getArraySizeHandling.__doc__.strip() == "The way how the size of the array is handled."

    def test_set_array_size_handling_docstring_verbatim(self):
        assert ApplicationArrayElement.setArraySizeHandling.__doc__.strip() == (
            "The way how the size of the array is handled. " "A None value is a no-op and does not overwrite an existing arraySizeHandling."
        )

    def test_get_array_size_semantics_docstring_verbatim(self):
        assert ApplicationArrayElement.getArraySizeSemantics.__doc__.strip() == "This attribute controls how the information about the array size shall be interpreted."

    def test_set_array_size_semantics_docstring_verbatim(self):
        assert ApplicationArrayElement.setArraySizeSemantics.__doc__.strip() == (
            "This attribute controls how the information about the array size shall be interpreted. " "A None value is a no-op and does not overwrite an existing arraySizeSemantics."
        )

    def test_get_index_data_type_ref_docstring_verbatim(self):
        assert ApplicationArrayElement.getIndexDataTypeRef.__doc__.strip() == (
            "This reference can be taken to assign a CompuMethod of category TEXTTABLE to the array. "
            "The texttable entries associate a textual value to an index number such that the element "
            "with that index number is represented by a symbolic name."
        )

    def test_set_index_data_type_ref_docstring_verbatim(self):
        assert ApplicationArrayElement.setIndexDataTypeRef.__doc__.strip() == (
            "This reference can be taken to assign a CompuMethod of category TEXTTABLE to the array. "
            "The texttable entries associate a textual value to an index number such that the element "
            "with that index number is represented by a symbolic name. "
            "A None value is a no-op and does not overwrite an existing indexDataTypeRef."
        )

    def test_get_max_number_of_elements_docstring_verbatim(self):
        assert ApplicationArrayElement.getMaxNumberOfElements.__doc__.strip() == "The maximum number of elements that the array can contain."

    def test_set_max_number_of_elements_docstring_verbatim(self):
        assert ApplicationArrayElement.setMaxNumberOfElements.__doc__.strip() == (
            "The maximum number of elements that the array can contain. " "A None value is a no-op and does not overwrite an existing maxNumberOfElements."
        )


class TestApplicationRecordElement:
    """Test class for ApplicationRecordElement class."""

    def test_application_record_element_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        record_element = ApplicationRecordElement(ar_root, "TestApplicationRecordElement")

        assert isinstance(record_element, ApplicationCompositeElementDataPrototype)
        assert record_element.__class__.__doc__.strip() == "Describes the properties of one particular element of an application record data type."
        optional = Boolean().setValue(True)
        assert record_element.setIsOptional(optional) is record_element
        assert record_element.getIsOptional() is optional
        record_element.setIsOptional(None)
        assert record_element.getIsOptional() is optional

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
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        sw_data_def = SwDataDefProps()
        record_element.setSwDataDefProps(sw_data_def)
        assert record_element.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

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
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        sw_data_def = SwDataDefProps()
        param_proto.setSwDataDefProps(sw_data_def)
        assert param_proto.getSwDataDefProps() == sw_data_def

        # Test typeTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

        type_ref = TRefType()
        type_ref.setValue("/Type/Ref")
        param_proto.setTypeTRef(type_ref)
        assert param_proto.getTypeTRef() == type_ref

    def test_parameter_data_prototype_init_value_none_no_op(self):
        """Test setInitValue treats None as a no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_proto = ParameterDataPrototype(ar_root, "TestParameterDataPrototype")

        init_value = TextValueSpecification()
        param_proto.setInitValue(init_value)
        assert param_proto.getInitValue() == init_value

        param_proto.setInitValue(None)
        assert param_proto.getInitValue() == init_value

        # Test initValue methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        init_value = TextValueSpecification()
        param_proto.setInitValue(init_value)
        assert param_proto.getInitValue() == init_value
