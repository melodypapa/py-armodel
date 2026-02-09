"""
Test module for PrimitiveTypes.py.

This file tests all classes defined in PrimitiveTypes.py:
- ARType (abstract base)
- ARNumerical
- ARFloat
- Float, TimeValue
- ARLiteral
- AREnum
- String, DisplayFormatString
- MonotonyEnum, ReferrableSubtypesEnum
- ARPositiveInteger
- ARBoolean
- NameToken, PositiveInteger, PositiveUnlimitedInteger
- Integer, UnlimitedInteger
- Boolean
- Identifier, CIdentifier
- RevisionLabelString
- Limit
- RefType, TRefType
- DiagRequirementIdString
- ArgumentDirectionEnum
- Ip4AddressString, Ip6AddressString, MacAddressString
- CategoryString
- ByteOrderEnum
- DateTime
- VerbatimString, RegularExpression

Tests cover:
- Abstract class instantiation
- Value getter/setter methods
- Type conversion and validation
- String representation
- Enum value validation
- Method chaining
- Extended attributes (CODING_RULE_V2_00014)
"""
import pytest

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARType,
    ARNumerical,
    ARFloat,
    Float,
    TimeValue,
    ARLiteral,
    AREnum,
    String,
    DisplayFormatString,
    MonotonyEnum,
    ReferrableSubtypesEnum,
    ARPositiveInteger,
    ARBoolean,
    NameToken,
    PositiveInteger,
    PositiveUnlimitedInteger,
    Integer,
    UnlimitedInteger,
    Boolean,
    Identifier,
    CIdentifier,
    RevisionLabelString,
    Limit,
    RefType,
    TRefType,
    DiagRequirementIdString,
    ArgumentDirectionEnum,
    Ip4AddressString,
    Ip6AddressString,
    MacAddressString,
    CategoryString,
    ByteOrderEnum,
    DateTime,
    VerbatimString,
    RegularExpression,
)


class TestARType:
    """Test class for ARType abstract base class."""

    def test_ar_type_abstract(self):
        """Test that ARType is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError):
            ARType()

    def test_ar_type_concrete_implementation(self):
        """Test that a concrete implementation of ARType can be instantiated."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        assert obj is not None

    def test_ar_type_value_initialization(self):
        """Test that value property is initialized to None."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        assert obj.value is None

    def test_ar_type_set_value(self):
        """Test setValue method."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        result = obj.setValue("test_value")
        assert result is obj  # Method chaining
        assert obj.value == "test_value"

    def test_ar_type_get_value(self):
        """Test getValue method."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        obj.setValue("test_value")
        assert obj.getValue() == "test_value"

    def test_ar_type_set_value_none(self):
        """Test that setValue with None doesn't change the value."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        obj.setValue("test_value")
        obj.setValue(None)
        assert obj.value == "test_value"  # Should not change

    def test_ar_type_get_text(self):
        """Test getText method."""
        class ConcreteARType(ARType):
            def __init__(self):
                super().__init__()
            
            def __str__(self):
                return str(self.value) if self.value is not None else ""

        obj = ConcreteARType()
        obj.setValue("test_value")
        assert obj.getText() == "test_value"


class TestARNumerical:
    """Test class for ARNumerical functionality."""

    def test_ar_numerical_can_be_instantiated(self):
        """Test that ARNumerical can be instantiated."""
        obj = ARNumerical()
        assert obj is not None

    def test_ar_numerical_value_initialization(self):
        """Test that value property is initialized to None."""
        obj = ARNumerical()
        assert obj.value is None

    def test_ar_numerical_set_value_int(self):
        """Test setValue with integer."""
        obj = ARNumerical()
        obj.setValue(42)
        assert obj.value == 42

    def test_ar_numerical_set_value_string(self):
        """Test setValue with string."""
        obj = ARNumerical()
        obj.setValue("123")
        assert obj.value == 123

    def test_ar_numerical_set_value_hex_string(self):
        """Test setValue with hexadecimal string."""
        obj = ARNumerical()
        obj.setValue("0xFF")
        assert obj.value == 255

    def test_ar_numerical_set_value_binary_string(self):
        """Test setValue with binary string."""
        obj = ARNumerical()
        obj.setValue("0b1010")
        assert obj.value == 10

    def test_ar_numerical_set_value_float_string(self):
        """Test setValue with float string."""
        obj = ARNumerical()
        obj.setValue("3.14")
        assert obj.value == 3.14

    def test_ar_numerical_set_value_true_string(self):
        """Test setValue with 'true' string."""
        obj = ARNumerical()
        obj.setValue("true")
        assert obj.value == 1

    def test_ar_numerical_set_value_false_string(self):
        """Test setValue with 'false' string."""
        obj = ARNumerical()
        obj.setValue("false")
        assert obj.value == 0

    def test_ar_numerical_set_value_invalid_string(self):
        """Test setValue with invalid string raises ValueError."""
        obj = ARNumerical()
        with pytest.raises(ValueError, match="Invalid Numerical Type"):
            obj.setValue("invalid")

    def test_ar_numerical_set_value_unsupported_type(self):
        """Test setValue with unsupported type raises ValueError."""
        obj = ARNumerical()
        with pytest.raises(ValueError):
            obj.value = [1, 2, 3]

    def test_ar_numerical_short_label_initialization(self):
        """Test that shortLabel property is initialized to None."""
        obj = ARNumerical()
        assert obj.shortLabel is None

    def test_ar_numerical_set_short_label(self):
        """Test setShortLabel method."""
        obj = ARNumerical()
        result = obj.setShortLabel("test_label")
        assert result is obj  # Method chaining
        assert obj.shortLabel == "test_label"

    def test_ar_numerical_get_short_label(self):
        """Test getShortLabel method."""
        obj = ARNumerical()
        obj.setShortLabel("test_label")
        assert obj.getShortLabel() == "test_label"

    def test_ar_numerical_str_representation(self):
        """Test __str__ method."""
        obj = ARNumerical()
        obj.setValue("123")
        assert str(obj) == "123"

    def test_ar_numerical_method_chaining(self):
        """Test method chaining."""
        obj = ARNumerical()
        result = obj.setValue(42).setShortLabel("test")
        assert result is obj


class TestARFloat:
    """Test class for ARFloat functionality."""

    def test_ar_float_can_be_instantiated(self):
        """Test that ARFloat can be instantiated."""
        obj = ARFloat()
        assert obj is not None

    def test_ar_float_set_value_float(self):
        """Test setValue with float."""
        obj = ARFloat()
        obj.setValue(3.14)
        assert obj.value == 3.14

    def test_ar_float_set_value_int(self):
        """Test setValue with integer."""
        obj = ARFloat()
        obj.setValue(42)
        assert obj.value == 42.0

    def test_ar_float_set_value_string(self):
        """Test setValue with string."""
        obj = ARFloat()
        obj.setValue("3.14")
        assert obj.value == 3.14


class TestFloat:
    """Test class for Float primitive type."""

    def test_float_can_be_instantiated(self):
        """Test that Float can be instantiated."""
        obj = Float()
        assert obj is not None


class TestTimeValue:
    """Test class for TimeValue primitive type."""

    def test_time_value_can_be_instantiated(self):
        """Test that TimeValue can be instantiated."""
        obj = TimeValue()
        assert obj is not None


class TestARLiteral:
    """Test class for ARLiteral functionality."""

    def test_ar_literal_can_be_instantiated(self):
        """Test that ARLiteral can be instantiated."""
        obj = ARLiteral()
        assert obj is not None

    def test_ar_literal_value_empty_string_initially(self):
        """Test that value property is empty string initially."""
        obj = ARLiteral()
        assert obj.value == ""

    def test_ar_literal_set_value_string(self):
        """Test setValue with string."""
        obj = ARLiteral()
        obj.setValue("test_value")
        assert obj.value == "test_value"

    def test_ar_literal_set_value_number(self):
        """Test setValue with number (converted to string)."""
        obj = ARLiteral()
        obj.setValue(42)
        assert obj.value == "42"

    def test_ar_literal_upper_method(self):
        """Test upper method."""
        obj = ARLiteral()
        obj.setValue("test_value")
        assert obj.upper() == "TEST_VALUE"

    def test_ar_literal_str_representation(self):
        """Test __str__ method."""
        obj = ARLiteral()
        obj.setValue("test_value")
        assert str(obj) == "test_value"


class TestAREnum:
    """Test class for AREnum functionality."""

    def test_ar_enum_can_be_instantiated(self):
        """Test that AREnum can be instantiated."""
        obj = AREnum(["VALUE1", "VALUE2"])
        assert obj is not None

    def test_ar_enum_enum_values(self):
        """Test that enumValues are set correctly."""
        obj = AREnum(["VALUE1", "VALUE2"])
        assert obj.enumValues == ["VALUE1", "VALUE2"]

    def test_ar_enum_get_enum_values(self):
        """Test getEnumValues method."""
        obj = AREnum(["VALUE1", "VALUE2"])
        assert obj.getEnumValues() == ["VALUE1", "VALUE2"]

    def test_ar_enum_set_enum_values(self):
        """Test setEnumValues method."""
        obj = AREnum([])
        result = obj.setEnumValues(["VALUE1", "VALUE2"])
        assert result is obj  # Method chaining
        assert obj.getEnumValues() == ["VALUE1", "VALUE2"]

    def test_ar_enum_validate_enum_value_valid(self):
        """Test validateEnumValue with valid value."""
        obj = AREnum(["VALUE1", "VALUE2"])
        assert obj.validateEnumValue("VALUE1") is True

    def test_ar_enum_validate_enum_value_invalid(self):
        """Test validateEnumValue with invalid value."""
        obj = AREnum(["VALUE1", "VALUE2"])
        assert obj.validateEnumValue("INVALID") is False


class TestString:
    """Test class for String primitive type."""

    def test_string_can_be_instantiated(self):
        """Test that String can be instantiated."""
        obj = String()
        assert obj is not None

    def test_string_set_value(self):
        """Test setValue with string."""
        obj = String()
        obj.setValue("test_value")
        assert obj.value == "test_value"


class TestDisplayFormatString:
    """Test class for DisplayFormatString primitive type."""

    def test_display_format_string_can_be_instantiated(self):
        """Test that DisplayFormatString can be instantiated."""
        obj = DisplayFormatString()
        assert obj is not None


class TestMonotonyEnum:
    """Test class for MonotonyEnum."""

    def test_monotony_enum_can_be_instantiated(self):
        """Test that MonotonyEnum can be instantiated."""
        obj = MonotonyEnum()
        assert obj is not None

    def test_monotony_enum_values(self):
        """Test that MonotonyEnum has correct enum values."""
        obj = MonotonyEnum()
        assert MonotonyEnum.INCREASE == "INCREASE"
        assert MonotonyEnum.DECREASE == "DECREASE"
        assert MonotonyEnum.STRICT_INCREASE == "STRICT_INCREASE"
        assert MonotonyEnum.STRICT_DECREASE == "STRICT_DECREASE"
        assert MonotonyEnum.MONOTONOUS == "MONOTONOUS"
        assert MonotonyEnum.NOT_MONOTONOUS == "NOT_MONOTONOUS"

    def test_monotony_enum_enum_values(self):
        """Test that enumValues contain all values."""
        obj = MonotonyEnum()
        assert len(obj.enumValues) == 6
        assert "INCREASE" in obj.enumValues
        assert "DECREASE" in obj.enumValues


class TestReferrableSubtypesEnum:
    """Test class for ReferrableSubtypesEnum."""

    def test_referrable_subtypes_enum_can_be_instantiated(self):
        """Test that ReferrableSubtypesEnum can be instantiated."""
        obj = ReferrableSubtypesEnum()
        assert obj is not None


class TestARPositiveInteger:
    """Test class for ARPositiveInteger functionality."""

    def test_ar_positive_integer_can_be_instantiated(self):
        """Test that ARPositiveInteger can be instantiated."""
        obj = ARPositiveInteger()
        assert obj is not None

    def test_ar_positive_integer_set_value_positive(self):
        """Test setValue with positive integer."""
        obj = ARPositiveInteger()
        obj.setValue(42)
        assert obj.value == 42

    def test_ar_positive_integer_set_value_zero(self):
        """Test setValue with zero."""
        obj = ARPositiveInteger()
        obj.setValue(0)
        assert obj.value == 0

    def test_ar_positive_integer_set_value_negative_raises_error(self):
        """Test setValue with negative integer raises ValueError."""
        obj = ARPositiveInteger()
        with pytest.raises(ValueError, match="Invalid Positive Integer"):
            obj.setValue(-1)


class TestARBoolean:
    """Test class for ARBoolean functionality."""

    def test_ar_boolean_can_be_instantiated(self):
        """Test that ARBoolean can be instantiated."""
        obj = ARBoolean()
        assert obj is not None

    def test_ar_boolean_set_value_true(self):
        """Test setValue with True."""
        obj = ARBoolean()
        obj.setValue(True)
        assert obj.value is True

    def test_ar_boolean_set_value_false(self):
        """Test setValue with False."""
        obj = ARBoolean()
        obj.setValue(False)
        assert obj.value is False

    def test_ar_boolean_set_value_string_true(self):
        """Test setValue with 'true' string."""
        obj = ARBoolean()
        obj.setValue("true")
        assert obj.value is True

    def test_ar_boolean_set_value_string_false(self):
        """Test setValue with 'false' string."""
        obj = ARBoolean()
        obj.setValue("false")
        assert obj.value is False

    def test_ar_boolean_set_value_string_1(self):
        """Test setValue with '1' string."""
        obj = ARBoolean()
        obj.setValue("1")
        assert obj.value is True

    def test_ar_boolean_set_value_string_0(self):
        """Test setValue with '0' string."""
        obj = ARBoolean()
        obj.setValue("0")
        assert obj.value is False

    def test_ar_boolean_set_value_int_1(self):
        """Test setValue with integer 1."""
        obj = ARBoolean()
        obj.setValue(1)
        assert obj.value is True

    def test_ar_boolean_set_value_int_0(self):
        """Test setValue with integer 0."""
        obj = ARBoolean()
        obj.setValue(0)
        assert obj.value is False

    def test_ar_boolean_str_true(self):
        """Test __str__ with True value."""
        obj = ARBoolean()
        obj.setValue(True)
        assert str(obj) == "true"

    def test_ar_boolean_str_false(self):
        """Test __str__ with False value."""
        obj = ARBoolean()
        obj.setValue(False)
        assert str(obj) == "false"

    def test_ar_boolean_str_preserves_text(self):
        """Test that __str__ preserves original text."""
        obj = ARBoolean()
        obj.setValue("1")
        assert str(obj) == "1"

        obj2 = ARBoolean()
        obj2.setValue("true")
        assert str(obj2) == "true"


class TestNameToken:
    """Test class for NameToken primitive type."""

    def test_name_token_can_be_instantiated(self):
        """Test that NameToken can be instantiated."""
        obj = NameToken()
        assert obj is not None


class TestPositiveInteger:
    """Test class for PositiveInteger primitive type."""

    def test_positive_integer_can_be_instantiated(self):
        """Test that PositiveInteger can be instantiated."""
        obj = PositiveInteger()
        assert obj is not None


class TestPositiveUnlimitedInteger:
    """Test class for PositiveUnlimitedInteger primitive type."""

    def test_positive_unlimited_integer_can_be_instantiated(self):
        """Test that PositiveUnlimitedInteger can be instantiated."""
        obj = PositiveUnlimitedInteger()
        assert obj is not None


class TestInteger:
    """Test class for Integer primitive type."""

    def test_integer_can_be_instantiated(self):
        """Test that Integer can be instantiated."""
        obj = Integer()
        assert obj is not None

    def test_integer_set_value_negative(self):
        """Test setValue with negative integer."""
        obj = Integer()
        obj.setValue(-42)
        assert obj.value == -42

    def test_integer_set_value_positive(self):
        """Test setValue with positive integer."""
        obj = Integer()
        obj.setValue(42)
        assert obj.value == 42


class TestUnlimitedInteger:
    """Test class for UnlimitedInteger primitive type."""

    def test_unlimited_integer_can_be_instantiated(self):
        """Test that UnlimitedInteger can be instantiated."""
        obj = UnlimitedInteger()
        assert obj is not None


class TestBoolean:
    """Test class for Boolean primitive type."""

    def test_boolean_can_be_instantiated(self):
        """Test that Boolean can be instantiated."""
        obj = Boolean()
        assert obj is not None


class TestIdentifier:
    """Test class for Identifier primitive type."""

    def test_identifier_can_be_instantiated(self):
        """Test that Identifier can be instantiated."""
        obj = Identifier()
        assert obj is not None


class TestCIdentifier:
    """Test class for CIdentifier primitive type."""

    def test_c_identifier_can_be_instantiated(self):
        """Test that CIdentifier can be instantiated."""
        obj = CIdentifier()
        assert obj is not None

    def test_c_identifier_blueprint_value_initialization(self):
        """Test that blueprintValue property is initialized to None."""
        obj = CIdentifier()
        assert obj.blueprintValue is None

    def test_c_identifier_name_pattern_initialization(self):
        """Test that namePattern property is initialized to None."""
        obj = CIdentifier()
        assert obj.namePattern is None

    def test_c_identifier_set_blueprint_value(self):
        """Test setBlueprintValue method."""
        obj = CIdentifier()
        result = obj.setBlueprintValue("test_blueprint")
        assert result is obj  # Method chaining
        assert obj.getBlueprintValue() == "test_blueprint"

    def test_c_identifier_set_name_pattern(self):
        """Test setNamePattern method."""
        obj = CIdentifier()
        result = obj.setNamePattern("test_pattern")
        assert result is obj  # Method chaining
        assert obj.getNamePattern() == "test_pattern"


class TestRevisionLabelString:
    """Test class for RevisionLabelString primitive type."""

    def test_revision_label_string_can_be_instantiated(self):
        """Test that RevisionLabelString can be instantiated."""
        obj = RevisionLabelString()
        assert obj is not None


class TestLimit:
    """Test class for Limit functionality."""

    def test_limit_can_be_instantiated(self):
        """Test that Limit can be instantiated."""
        obj = Limit()
        assert obj is not None

    def test_limit_interval_type_initialization(self):
        """Test that intervalType property is initialized to None."""
        obj = Limit()
        assert obj.intervalType is None

    def test_limit_value_initialization(self):
        """Test that value property is initialized to None."""
        obj = Limit()
        assert obj.value is None

    def test_limit_set_interval_type(self):
        """Test setIntervalType method."""
        obj = Limit()
        result = obj.setIntervalType("closed")
        assert result is obj  # Method chaining
        assert obj.getIntervalType() == "closed"

    def test_limit_set_value(self):
        """Test setValue method."""
        obj = Limit()
        result = obj.setValue("100")
        assert result is obj  # Method chaining
        assert obj.getValue() == "100"

    def test_limit_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        obj = Limit()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"


class TestRefType:
    """Test class for RefType functionality."""

    def test_ref_type_can_be_instantiated(self):
        """Test that RefType can be instantiated."""
        obj = RefType()
        assert obj is not None

    def test_ref_type_base_initialization(self):
        """Test that base property is initialized to None."""
        obj = RefType()
        assert obj.base is None

    def test_ref_type_dest_initialization(self):
        """Test that dest property is initialized to None."""
        obj = RefType()
        assert obj.dest is None

    def test_ref_type_value_initialization(self):
        """Test that value property is initialized to None."""
        obj = RefType()
        assert obj.value is None

    def test_ref_type_set_base(self):
        """Test setBase method."""
        obj = RefType()
        result = obj.setBase("AUTOSAR")
        assert result is obj  # Method chaining
        assert obj.getBase() == "AUTOSAR"

    def test_ref_type_set_dest(self):
        """Test setDest method."""
        obj = RefType()
        result = obj.setDest("ARPackage")
        assert result is obj  # Method chaining
        assert obj.getDest() == "ARPackage"

    def test_ref_type_set_value(self):
        """Test setValue method."""
        obj = RefType()
        result = obj.setValue("/AUTOSAR/ARPackages/TestPackage")
        assert result is obj  # Method chaining
        assert obj.getValue() == "/AUTOSAR/ARPackages/TestPackage"

    def test_ref_type_get_short_value(self):
        """Test getShortValue method."""
        obj = RefType()
        obj.setValue("/AUTOSAR/ARPackages/TestPackage")
        assert obj.getShortValue() == "TestPackage"

    def test_ref_type_get_short_value_no_match(self):
        """Test getShortValue with value that doesn't match pattern."""
        obj = RefType()
        obj.setValue("TestPackage")
        assert obj.getShortValue() == "TestPackage"

    def test_ref_type_get_short_value_none_raises_error(self):
        """Test getShortValue with None value raises ValueError."""
        obj = RefType()
        with pytest.raises(ValueError, match="Invalid value of RefType"):
            obj.getShortValue()


class TestTRefType:
    """Test class for TRefType primitive type."""

    def test_t_ref_type_can_be_instantiated(self):
        """Test that TRefType can be instantiated."""
        obj = TRefType()
        assert obj is not None


class TestDiagRequirementIdString:
    """Test class for DiagRequirementIdString primitive type."""

    def test_diag_requirement_id_string_can_be_instantiated(self):
        """Test that DiagRequirementIdString can be instantiated."""
        obj = DiagRequirementIdString()
        assert obj is not None


class TestArgumentDirectionEnum:
    """Test class for ArgumentDirectionEnum."""

    def test_argument_direction_enum_can_be_instantiated(self):
        """Test that ArgumentDirectionEnum can be instantiated."""
        obj = ArgumentDirectionEnum()
        assert obj is not None

    def test_argument_direction_enum_values(self):
        """Test that ArgumentDirectionEnum has correct enum values."""
        assert ArgumentDirectionEnum.IN == "in"
        assert ArgumentDirectionEnum.INOUT == "inout"
        assert ArgumentDirectionEnum.OUT == "out"

    def test_argument_direction_enum_enum_values(self):
        """Test that enumValues contain all values."""
        obj = ArgumentDirectionEnum()
        assert len(obj.enumValues) == 3
        assert "in" in obj.enumValues
        assert "inout" in obj.enumValues
        assert "out" in obj.enumValues


class TestIp4AddressString:
    """Test class for Ip4AddressString primitive type."""

    def test_ip4_address_string_can_be_instantiated(self):
        """Test that Ip4AddressString can be instantiated."""
        obj = Ip4AddressString()
        assert obj is not None


class TestIp6AddressString:
    """Test class for Ip6AddressString primitive type."""

    def test_ip6_address_string_can_be_instantiated(self):
        """Test that Ip6AddressString can be instantiated."""
        obj = Ip6AddressString()
        assert obj is not None


class TestMacAddressString:
    """Test class for MacAddressString primitive type."""

    def test_mac_address_string_can_be_instantiated(self):
        """Test that MacAddressString can be instantiated."""
        obj = MacAddressString()
        assert obj is not None


class TestCategoryString:
    """Test class for CategoryString primitive type."""

    def test_category_string_can_be_instantiated(self):
        """Test that CategoryString can be instantiated."""
        obj = CategoryString()
        assert obj is not None


class TestByteOrderEnum:
    """Test class for ByteOrderEnum."""

    def test_byte_order_enum_can_be_instantiated(self):
        """Test that ByteOrderEnum can be instantiated."""
        obj = ByteOrderEnum()
        assert obj is not None


class TestDateTime:
    """Test class for DateTime primitive type."""

    def test_date_time_can_be_instantiated(self):
        """Test that DateTime can be instantiated."""
        obj = DateTime()
        assert obj is not None


class TestVerbatimString:
    """Test class for VerbatimString primitive type."""

    def test_verbatim_string_can_be_instantiated(self):
        """Test that VerbatimString can be instantiated."""
        obj = VerbatimString()
        assert obj is not None


class TestRegularExpression:
    """Test class for RegularExpression primitive type."""

    def test_regular_expression_can_be_instantiated(self):
        """Test that RegularExpression can be instantiated."""
        obj = RegularExpression()
        assert obj is not None