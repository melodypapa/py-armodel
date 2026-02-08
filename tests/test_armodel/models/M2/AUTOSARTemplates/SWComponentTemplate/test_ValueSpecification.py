import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueArgument,
    CompositeValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARNumerical,
    RefType,
)


class TestValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ValueSpecification abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="ValueSpecification is an abstract class."):
            ValueSpecification()

    def test_get_short_label(self):
        """Test getShortLabel method"""
        # Create a concrete subclass for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        assert spec.getShortLabel() is None

    def test_set_short_label(self):
        """Test setShortLabel method"""
        # Create a concrete subclass for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        spec.setShortLabel("TestLabel")
        assert spec.getShortLabel() == "TestLabel"

    def test_set_short_label_none(self):
        """Test setShortLabel with None value"""
        # Create a concrete subclass for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        spec = ConcreteValueSpecification()
        spec.setShortLabel(None)
        assert spec.getShortLabel() is None


class TestCompositeValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that CompositeValueSpecification abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="CompositeValueSpecification is an abstract class."):
            CompositeValueSpecification()


class TestCompositeRuleBasedValueArgument:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that CompositeRuleBasedValueArgument abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="CompositeRuleBasedValueArgument is an abstract class."):
            CompositeRuleBasedValueArgument()


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
        spec.setCategory("TestCategory")
        assert spec.getCategory() == "TestCategory"

    def test_set_category_none(self):
        """Test setCategory with None value"""
        spec = ApplicationValueSpecification()
        spec.setCategory(None)
        assert spec.getCategory() is None

    def test_get_sw_axis_cont(self):
        """Test getSwAxisCont method"""
        spec = ApplicationValueSpecification()
        assert spec.getSwAxisCont() == []

    def test_set_sw_axis_cont(self):
        """Test setSwAxisCont method"""
        spec = ApplicationValueSpecification()
        test_value = ["axis1", "axis2"]
        spec.setSwAxisCont(test_value)
        assert spec.getSwAxisCont() == test_value

    def test_set_sw_axis_cont_none(self):
        """Test setSwAxisCont with None value"""
        spec = ApplicationValueSpecification()
        spec.setSwAxisCont(None)
        assert spec.getSwAxisCont() is None

    def test_get_sw_value_cont(self):
        """Test getSwValueCont method"""
        spec = ApplicationValueSpecification()
        assert spec.getSwValueCont() is None

    def test_set_sw_value_cont(self):
        """Test setSwValueCont method"""
        spec = ApplicationValueSpecification()
        test_value = "test_value"
        spec.setSwValueCont(test_value)
        assert spec.getSwValueCont() == test_value

    def test_set_sw_value_cont_none(self):
        """Test setSwValueCont with None value"""
        spec = ApplicationValueSpecification()
        spec.setSwValueCont(None)
        assert spec.getSwValueCont() is None

    def test_all_properties(self):
        """Test setting all properties"""
        spec = ApplicationValueSpecification()

        spec.setCategory("TestCategory")
        spec.setSwAxisCont(["axis1", "axis2"])
        spec.setSwValueCont("test_value")

        assert spec.getCategory() == "TestCategory"
        assert spec.getSwAxisCont() == ["axis1", "axis2"]
        assert spec.getSwValueCont() == "test_value"


class TestRecordValueSpecification:
    def test_initialization(self):
        """Test RecordValueSpecification initialization"""
        spec = RecordValueSpecification()

        assert spec is not None
        assert spec.fields == []

    def test_add_field(self):
        """Test addField method"""
        spec = RecordValueSpecification()

        # Create a concrete ValueSpecification instance for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        field = ConcreteValueSpecification()
        spec.addField(field)
        assert field in spec.getFields()
        assert len(spec.getFields()) == 1
        assert spec.getFields()[0] == field

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
        test_value = ARLiteral().setValue("test_text")
        spec.setValue(test_value)
        assert spec.getValue() == test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        spec = TextValueSpecification()
        spec.setValue(None)
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
        test_value = ARNumerical().setValue(42)
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
        spec.setIntendedPartialInitializationCount(5)
        assert spec.getIntendedPartialInitializationCount() == 5

    def test_set_intended_partial_initialization_count_none(self):
        """Test setIntendedPartialInitializationCount with None value"""
        spec = ArrayValueSpecification()
        spec.setIntendedPartialInitializationCount(None)
        assert spec.getIntendedPartialInitializationCount() is None

    def test_add_element(self):
        """Test addElement method"""
        spec = ArrayValueSpecification()

        # Create a concrete ValueSpecification instance for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        element = ConcreteValueSpecification()
        spec.addElement(element)
        assert element in spec.getElements()
        assert len(spec.getElements()) == 1
        assert spec.getElements()[0] == element

    def test_get_elements(self):
        """Test getElements method"""
        spec = ArrayValueSpecification()
        elements = spec.getElements()
        assert elements == []
        assert isinstance(elements, list)

    def test_all_properties(self):
        """Test setting all properties"""
        spec = ArrayValueSpecification()

        # Create a concrete ValueSpecification instance for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        element = ConcreteValueSpecification()
        spec.addElement(element)
        spec.setIntendedPartialInitializationCount(10)

        assert len(spec.getElements()) == 1
        assert spec.getIntendedPartialInitializationCount() == 10


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

        # Create a concrete ValueSpecification instance for testing
        class ConcreteValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()

        test_value = ConcreteValueSpecification()
        spec.setValueSpec(test_value)
        assert spec.getValueSpec() == test_value

    def test_set_value_spec_none(self):
        """Test setValueSpec with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "TestConstantSpec")
        spec.setValueSpec(None)
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
        test_value = RefType().setValue("TestRef")
        spec.setConstantRef(test_value)
        assert spec.getConstantRef() == test_value

    def test_set_constant_ref_none(self):
        """Test setConstantRef with None value"""
        spec = ConstantReference()
        spec.setConstantRef(None)
        assert spec.getConstantRef() is None
