"""
This module contains comprehensive tests for the CommonStructure __init__.py file
in the AUTOSAR model. The file contains several value specification classes that need
to be thoroughly tested for complete coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationRuleBasedValueSpecification,
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueArgument,
    CompositeValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    RuleArguments,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    RuleBasedValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, RefType


class TestValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ValueSpecification abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="ValueSpecification is an abstract class."):
            ValueSpecification()

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of ValueSpecification can be instantiated"""

        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        assert spec is not None

    def test_get_short_label(self):
        """Test getShortLabel method"""

        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        assert spec.getShortLabel() is None

    def test_set_short_label(self):
        """Test setShortLabel method"""

        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        test_label = "test_label"
        result = spec.setShortLabel(test_label)
        assert result is spec
        assert spec.getShortLabel() == test_label

    def test_set_short_label_none(self):
        """Test setShortLabel with None value"""

        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        result = spec.setShortLabel(None)
        assert result is spec
        assert spec.getShortLabel() is None


class TestCompositeValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that CompositeValueSpecification abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="CompositeValueSpecification is an abstract class."):
            CompositeValueSpecification()

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of CompositeValueSpecification can be instantiated"""

        class ConcreteCompositeValueSpecification(CompositeValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteCompositeValueSpecification()
        assert spec is not None


class TestCompositeRuleBasedValueArgument:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that CompositeRuleBasedValueArgument abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="CompositeRuleBasedValueArgument is an abstract class."):
            CompositeRuleBasedValueArgument()

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of CompositeRuleBasedValueArgument can be instantiated"""

        class ConcreteCompositeRuleBasedValueArgument(CompositeRuleBasedValueArgument):
            def __init__(self):
                super().__init__()

        arg = ConcreteCompositeRuleBasedValueArgument()
        assert arg is not None


class TestApplicationValueSpecification:
    def test_initialization(self):
        """Test ApplicationValueSpecification initialization"""
        spec = ApplicationValueSpecification()

        assert spec is not None
        assert spec.category is None
        assert spec.swAxisCont == []
        assert spec.swValueCont is None

    def test_get_category(self):
        """Test getCategory method"""
        spec = ApplicationValueSpecification()
        assert spec.getCategory() is None

    def test_set_category(self):
        """Test setCategory method"""
        spec = ApplicationValueSpecification()
        test_category = "test_category"
        result = spec.setCategory(test_category)
        assert result is spec
        assert spec.getCategory() == test_category

    def test_set_category_none(self):
        """Test setCategory with None value"""
        spec = ApplicationValueSpecification()
        result = spec.setCategory(None)
        assert result is spec
        assert spec.getCategory() is None

    def test_get_sw_axis_cont(self):
        """Test getSwAxisCont method"""
        spec = ApplicationValueSpecification()
        assert spec.getSwAxisCont() == []

    def test_set_sw_axis_cont(self):
        """Test setSwAxisCont method"""
        spec = ApplicationValueSpecification()
        test_cont = ["axis1", "axis2"]
        result = spec.setSwAxisCont(test_cont)
        assert result is spec
        assert spec.getSwAxisCont() == test_cont

    def test_set_sw_axis_cont_none(self):
        """Test setSwAxisCont with None value"""
        spec = ApplicationValueSpecification()
        result = spec.setSwAxisCont(None)
        assert result is spec
        assert spec.getSwAxisCont() is None

    def test_get_sw_value_cont(self):
        """Test getSwValueCont method"""
        spec = ApplicationValueSpecification()
        assert spec.getSwValueCont() is None

    def test_set_sw_value_cont(self):
        """Test setSwValueCont method"""
        spec = ApplicationValueSpecification()
        test_value = "test_value"
        result = spec.setSwValueCont(test_value)
        assert result is spec
        assert spec.getSwValueCont() == test_value

    def test_set_sw_value_cont_none(self):
        """Test setSwValueCont with None value"""
        spec = ApplicationValueSpecification()
        result = spec.setSwValueCont(None)
        assert result is spec
        assert spec.getSwValueCont() is None


class TestApplicationRuleBasedValueSpecification:
    def test_initialization(self):
        """Test ApplicationRuleBasedValueSpecification initialization"""
        spec = ApplicationRuleBasedValueSpecification()

        assert spec is not None
        assert spec.category is None
        assert spec.swAxisConts == []
        assert spec.swValueCont is None

    def test_get_category(self):
        """Test getCategory method"""
        spec = ApplicationRuleBasedValueSpecification()
        assert spec.getCategory() is None

    def test_set_category(self):
        """Test setCategory method"""
        spec = ApplicationRuleBasedValueSpecification()
        test_category = "test_category"
        result = spec.setCategory(test_category)
        assert result is spec
        assert spec.getCategory() == test_category

    def test_set_category_none(self):
        """Test setCategory with None value does not overwrite existing category"""
        spec = ApplicationRuleBasedValueSpecification()
        spec.setCategory("existing")
        result = spec.setCategory(None)
        assert result is spec
        assert spec.getCategory() == "existing"

    def test_get_sw_axis_conts(self):
        """Test getSwAxisConts method"""
        spec = ApplicationRuleBasedValueSpecification()
        assert spec.getSwAxisConts() == []

    def test_add_sw_axis_cont(self):
        """Test addSwAxisCont method appends to the list"""
        spec = ApplicationRuleBasedValueSpecification()
        axis = RuleBasedAxisCont()
        axis.setCategory("STD_AXIS")
        result = spec.addSwAxisCont(axis)
        assert result is spec
        assert spec.getSwAxisConts() == [axis]

    def test_add_sw_axis_cont_multiple(self):
        """Test addSwAxisCont accumulates multiple entries"""
        spec = ApplicationRuleBasedValueSpecification()
        axis_1 = RuleBasedAxisCont()
        axis_2 = RuleBasedAxisCont()
        spec.addSwAxisCont(axis_1)
        spec.addSwAxisCont(axis_2)
        assert spec.getSwAxisConts() == [axis_1, axis_2]

    def test_add_sw_axis_cont_none(self):
        """Test addSwAxisCont with None value is a no-op"""
        spec = ApplicationRuleBasedValueSpecification()
        axis = RuleBasedAxisCont()
        spec.addSwAxisCont(axis)
        result = spec.addSwAxisCont(None)
        assert result is spec
        assert spec.getSwAxisConts() == [axis]

    def test_get_sw_value_cont(self):
        """Test getSwValueCont method"""
        spec = ApplicationRuleBasedValueSpecification()
        assert spec.getSwValueCont() is None

    def test_set_sw_value_cont(self):
        """Test setSwValueCont method"""
        spec = ApplicationRuleBasedValueSpecification()
        value = RuleBasedValueCont()
        ref = RefType()
        ref.setDest("Unit")
        ref.setValue("/p/u")
        value.setUnitRef(ref)
        result = spec.setSwValueCont(value)
        assert result is spec
        assert spec.getSwValueCont() == value

    def test_set_sw_value_cont_none(self):
        """Test setSwValueCont with None value does not overwrite existing value content"""
        spec = ApplicationRuleBasedValueSpecification()
        value = RuleBasedValueCont()
        spec.setSwValueCont(value)
        result = spec.setSwValueCont(None)
        assert result is spec
        assert spec.getSwValueCont() == value


class TestRuleArguments:
    def test_initialization(self):
        """Test RuleArguments initialization"""
        arguments = RuleArguments()

        assert arguments is not None
        assert arguments.getVs() == []
        assert arguments.getVt() is None
        assert arguments.getVtfs() == []

    def test_add_v(self):
        """Test addV method appends to the list"""
        arguments = RuleArguments()
        v = ARNumerical()
        v.setValue("1.5")
        arguments.addV(v)
        assert arguments.getVs() == [v]

    def test_add_v_multiple(self):
        """Test addV accumulates multiple entries"""
        arguments = RuleArguments()
        v_1 = ARNumerical()
        v_1.setValue("1")
        v_2 = ARNumerical()
        v_2.setValue("2")
        arguments.addV(v_1)
        arguments.addV(v_2)
        assert arguments.getVs() == [v_1, v_2]

    def test_set_vt(self):
        """Test setVt method"""
        arguments = RuleArguments()
        vt = ARLiteral()
        vt.setValue("label")
        result = arguments.setVt(vt)
        assert result is arguments
        assert arguments.getVt() == vt

    def test_add_vtf(self):
        """Test addVtf method appends to the list"""
        arguments = RuleArguments()
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText

        vtf = NumericalOrText()
        arguments.addVtf(vtf)
        assert arguments.getVtfs() == [vtf]


class TestRuleBasedAxisCont:
    def test_initialization(self):
        """Test RuleBasedAxisCont initialization"""
        cont = RuleBasedAxisCont()

        assert cont is not None
        assert cont.getCategory() is None
        assert cont.getUnitRef() is None
        assert cont.getSwArraysize() is None
        assert cont.getSwAxisIndex() is None
        assert cont.getRuleBasedValues() is None

    def test_set_category(self):
        """Test setCategory method"""
        cont = RuleBasedAxisCont()
        result = cont.setCategory("STD_AXIS")
        assert result is cont
        assert cont.getCategory() == "STD_AXIS"

    def test_set_unit_ref(self):
        """Test setUnitRef method"""
        cont = RuleBasedAxisCont()
        ref = RefType()
        ref.setDest("Unit")
        ref.setValue("/p/u")
        result = cont.setUnitRef(ref)
        assert result is cont
        assert cont.getUnitRef() == ref

    def test_set_sw_arraysize(self):
        """Test setSwArraysize method"""
        cont = RuleBasedAxisCont()
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList

        size = ValueList()
        result = cont.setSwArraysize(size)
        assert result is cont
        assert cont.getSwArraysize() == size

    def test_set_sw_axis_index(self):
        """Test setSwAxisIndex method"""
        cont = RuleBasedAxisCont()
        result = cont.setSwAxisIndex("1")
        assert result is cont
        assert cont.getSwAxisIndex() == "1"

    def test_set_rule_based_values(self):
        """Test setRuleBasedValues method"""
        cont = RuleBasedAxisCont()
        values = RuleBasedValueSpecification()
        result = cont.setRuleBasedValues(values)
        assert result is cont
        assert cont.getRuleBasedValues() == values


class TestRuleBasedValueCont:
    def test_initialization(self):
        """Test RuleBasedValueCont initialization"""
        cont = RuleBasedValueCont()

        assert cont is not None
        assert cont.getUnitRef() is None
        assert cont.getSwArraysize() is None
        assert cont.getRuleBasedValues() is None

    def test_set_unit_ref(self):
        """Test setUnitRef method"""
        cont = RuleBasedValueCont()
        ref = RefType()
        ref.setDest("Unit")
        ref.setValue("/p/u")
        result = cont.setUnitRef(ref)
        assert result is cont
        assert cont.getUnitRef() == ref

    def test_set_sw_arraysize(self):
        """Test setSwArraysize method"""
        cont = RuleBasedValueCont()
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList

        size = ValueList()
        result = cont.setSwArraysize(size)
        assert result is cont
        assert cont.getSwArraysize() == size

    def test_set_rule_based_values(self):
        """Test setRuleBasedValues method"""
        cont = RuleBasedValueCont()
        values = RuleBasedValueSpecification()
        result = cont.setRuleBasedValues(values)
        assert result is cont
        assert cont.getRuleBasedValues() == values


class TestRuleBasedValueSpecification:
    def test_initialization(self):
        """Test RuleBasedValueSpecification initialization"""
        spec = RuleBasedValueSpecification()

        assert spec is not None
        assert spec.getRule() is None
        assert spec.getArguments() == []
        assert spec.getMaxSizeToFill() is None

    def test_set_rule(self):
        """Test setRule method"""
        spec = RuleBasedValueSpecification()
        result = spec.setRule("FILL_UNTIL_END")
        assert result is spec
        assert spec.getRule() == "FILL_UNTIL_END"

    def test_add_argument(self):
        """Test addArgument method appends to the list"""
        spec = RuleBasedValueSpecification()
        argument = RuleArguments()
        spec.addArgument(argument)
        assert spec.getArguments() == [argument]

    def test_set_max_size_to_fill(self):
        """Test setMaxSizeToFill method"""
        spec = RuleBasedValueSpecification()
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer

        size = Integer()
        size.setValue("8")
        result = spec.setMaxSizeToFill(size)
        assert result is spec
        assert spec.getMaxSizeToFill() == size


class TestRecordValueSpecification:
    def test_initialization(self):
        """Test RecordValueSpecification initialization"""
        spec = RecordValueSpecification()

        assert spec is not None
        assert spec.fields == []

    def test_add_field(self):
        """Test addField method"""
        spec = RecordValueSpecification()

        # Create a mock ValueSpecification for testing
        class MockValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        mock_field = MockValueSpecification()
        spec.addField(mock_field)

        fields = spec.getFields()
        assert len(fields) == 1
        assert fields[0] == mock_field

    def test_get_fields(self):
        """Test getFields method"""
        spec = RecordValueSpecification()
        fields = spec.getFields()
        assert fields == []
        assert isinstance(fields, list)


class TestTextValueSpecification:
    def test_initialization(self):
        """Test TextValueSpecification initialization"""
        spec = TextValueSpecification()

        assert spec is not None
        assert spec.value is None

    def test_get_value(self):
        """Test getValue method"""
        spec = TextValueSpecification()
        assert spec.getValue() is None

    def test_set_value(self):
        """Test setValue method"""
        spec = TextValueSpecification()
        test_value = ARLiteral()
        test_value.setValue("test_text")
        result = spec.setValue(test_value)
        assert result is spec
        assert spec.getValue() == test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        spec = TextValueSpecification()
        result = spec.setValue(None)
        assert result is spec
        assert spec.getValue() is None


class TestNumericalValueSpecification:
    def test_initialization(self):
        """Test NumericalValueSpecification initialization"""
        spec = NumericalValueSpecification()

        assert spec is not None
        assert spec.value is None

    def test_get_value(self):
        """Test getValue method"""
        spec = NumericalValueSpecification()
        assert spec.getValue() is None

    def test_set_value(self):
        """Test setValue method"""
        spec = NumericalValueSpecification()
        test_value = ARNumerical()
        test_value.setValue(42)
        result = spec.setValue(test_value)
        assert result is spec
        assert spec.getValue() == test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        spec = NumericalValueSpecification()
        result = spec.setValue(None)
        assert result is spec
        assert spec.getValue() is None


class TestArrayValueSpecification:
    def test_initialization(self):
        """Test ArrayValueSpecification initialization"""
        spec = ArrayValueSpecification()

        assert spec is not None
        assert spec.element == []
        assert spec.intendedPartialInitializationCount is None

    def test_get_intended_partial_initialization_count(self):
        """Test getIntendedPartialInitializationCount method"""
        spec = ArrayValueSpecification()
        assert spec.getIntendedPartialInitializationCount() is None

    def test_set_intended_partial_initialization_count(self):
        """Test setIntendedPartialInitializationCount method"""
        spec = ArrayValueSpecification()
        test_count = 5
        result = spec.setIntendedPartialInitializationCount(test_count)
        assert result is spec
        assert spec.getIntendedPartialInitializationCount() == test_count

    def test_set_intended_partial_initialization_count_none(self):
        """Test setIntendedPartialInitializationCount with None value"""
        spec = ArrayValueSpecification()
        result = spec.setIntendedPartialInitializationCount(None)
        assert result is spec
        assert spec.getIntendedPartialInitializationCount() is None

    def test_add_element(self):
        """Test addElement method"""
        spec = ArrayValueSpecification()

        # Create a mock ValueSpecification for testing
        class MockValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        mock_element = MockValueSpecification()
        spec.addElement(mock_element)

        elements = spec.getElements()
        assert len(elements) == 1
        assert elements[0] == mock_element

    def test_get_elements(self):
        """Test getElements method"""
        spec = ArrayValueSpecification()
        elements = spec.getElements()
        assert elements == []
        assert isinstance(elements, list)


class TestConstantSpecification:
    def test_initialization(self):
        """Test ConstantSpecification initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "TestConstantSpec")

        assert spec is not None
        assert spec.getShortName() == "TestConstantSpec"
        assert spec.valueSpec is None

    def test_get_value_spec(self):
        """Test getValueSpec method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "TestConstantSpec")
        assert spec.getValueSpec() is None

    def test_set_value_spec(self):
        """Test setValueSpec method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "TestConstantSpec")

        # Create a mock ValueSpecification for testing
        class MockValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        mock_spec = MockValueSpecification()
        result = spec.setValueSpec(mock_spec)
        assert result is spec
        assert spec.getValueSpec() == mock_spec

    def test_set_value_spec_none(self):
        """Test setValueSpec with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "TestConstantSpec")
        result = spec.setValueSpec(None)
        assert result is spec
        assert spec.getValueSpec() is None


class TestConstantReference:
    def test_initialization(self):
        """Test ConstantReference initialization"""
        spec = ConstantReference()

        assert spec is not None
        assert spec.constantRef is None

    def test_get_constant_ref(self):
        """Test getConstantRef method"""
        spec = ConstantReference()
        assert spec.getConstantRef() is None

    def test_set_constant_ref(self):
        """Test setConstantRef method"""
        spec = ConstantReference()
        test_ref = RefType().setValue("TestRef")
        result = spec.setConstantRef(test_ref)
        assert result is spec
        assert spec.getConstantRef() == test_ref

    def test_set_constant_ref_none(self):
        """Test setConstantRef with None value"""
        spec = ConstantReference()
        result = spec.setConstantRef(None)
        assert result is spec
        assert spec.getConstantRef() is None
