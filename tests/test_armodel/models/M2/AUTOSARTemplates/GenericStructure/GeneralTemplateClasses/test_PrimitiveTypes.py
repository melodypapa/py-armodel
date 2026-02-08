"""
This module contains comprehensive tests for the PrimitiveTypes.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARFloat,
    ArgumentDirectionEnum,
    ARLiteral,
    ARNumerical,
    ARPositiveInteger,
    ARType,
    Boolean,
    ByteOrderEnum,
    CategoryString,
    CIdentifier,
    DateTime,
    DiagRequirementIdString,
    Float,
    Identifier,
    Integer,
    Ip4AddressString,
    Ip6AddressString,
    Limit,
    MacAddressString,
    NameToken,
    PositiveInteger,
    ReferrableSubtypesEnum,
    RefType,
    RegularExpression,
    String,
    TimeValue,
    TRefType,
    UnlimitedInteger,
    VerbatimString,
)


class TestARType:
    """
    Test class for ARType functionality.
    """

    def test_initialization(self):
        """
        Test ARType initialization.
        """
        # ARType is abstract but doesn't raise an error on instantiation
        # as it uses ABCMeta but doesn't have explicit type check
        obj = ARType()

        # Verify basic properties
        assert obj is not None
        assert obj.timestamp is None
        assert obj.uuid is None
        assert obj._value is None

    def test_timestamp_and_uuid(self):
        """
        Test timestamp and uuid attributes in ARType.
        """
        obj = ARType()

        # Test setting values
        obj.timestamp = "2023-01-01"
        obj.uuid = "test-uuid"
        assert obj.timestamp == "2023-01-01"
        assert obj.uuid == "test-uuid"

    def test_value_methods(self):
        """
        Test value property and related methods.
        """
        obj = ARType()

        # Test initial value
        assert obj.getValue() is None

        # Test setting value
        obj.setValue("test_value")
        assert obj.getValue() == "test_value"

        # Test setting None value - this doesn't change the value due to "if val is not None" check
        obj.setValue(None)
        assert obj.getValue() == "test_value"  # Value remains unchanged

    def test_get_text(self):
        """
        Test getText method.
        """
        obj = ARType()
        # getText calls str(self) which returns the object representation
        text = obj.getText()
        assert text is not None
        assert isinstance(text, str)


class TestARNumerical:
    """
    Test class for ARNumerical functionality.
    """

    def test_initialization(self):
        """
        Test ARNumerical initialization.
        """
        numerical = ARNumerical()

        # Verify basic properties
        assert numerical is not None
        assert numerical.shortLabel is None
        assert numerical._text is None
        assert numerical._value is None

    def test_value_property_int(self):
        """
        Test value property with integer values.
        """
        numerical = ARNumerical()

        # Set integer value
        numerical.value = 42
        assert numerical.value == 42
        assert str(numerical) == "42"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        numerical = ARNumerical()

        # Set string value that converts to integer
        numerical.value = "42"
        assert numerical.value == 42
        assert str(numerical) == "42"

    def test_convert_string_to_number_value(self):
        """
        Test _convertStringToNumberValue method.
        """
        numerical = ARNumerical()

        # Test decimal
        assert numerical._convertStringToNumberValue("42") == 42
        # Test hex
        assert numerical._convertStringToNumberValue("0x2A") == 42
        # Test binary
        assert numerical._convertStringToNumberValue("0b101010") == 42
        # Test float
        assert numerical._convertStringToNumberValue("42.5") == 42.5
        # Test boolean strings
        assert numerical._convertStringToNumberValue("true") == 1
        assert numerical._convertStringToNumberValue("false") == 0

    def test_short_label_methods(self):
        """
        Test short label methods.
        """
        numerical = ARNumerical()

        # Test initial value
        assert numerical.getShortLabel() is None

        # Test setting short label
        result = numerical.setShortLabel("TestLabel")
        assert result is numerical  # Verify method chaining
        assert numerical.getShortLabel() == "TestLabel"

        # Test setting None (should not change the value)
        result = numerical.setShortLabel(None)
        assert result is numerical  # Verify method chaining
        assert numerical.getShortLabel() == "TestLabel"


class TestARFloat:
    """
    Test class for ARFloat functionality.
    """

    def test_initialization(self):
        """
        Test ARFloat initialization.
        """
        ar_float = ARFloat()

        # Verify basic properties
        assert ar_float is not None
        assert ar_float._text is None
        assert ar_float._value is None

    def test_value_property_float(self):
        """
        Test value property with float values.
        """
        ar_float = ARFloat()

        # Set float value
        ar_float.value = 42.5
        assert ar_float.value == 42.5
        assert str(ar_float) == "42.5"

    def test_value_property_int(self):
        """
        Test value property with integer values (should convert to float).
        """
        ar_float = ARFloat()

        # Set integer value
        ar_float.value = 42
        assert ar_float.value == 42.0
        assert str(ar_float) == "42.0"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        ar_float = ARFloat()

        # Set string value that converts to float
        ar_float.value = "42.5"
        assert ar_float.value == 42.5
        assert str(ar_float) == "42.5"


class TestFloat:
    """
    Test class for Float functionality.
    """

    def test_initialization(self):
        """
        Test Float initialization.
        """
        float_val = Float()

        # Verify basic properties
        assert float_val is not None
        assert float_val._text is None
        assert float_val._value is None


class TestTimeValue:
    """
    Test class for TimeValue functionality.
    """

    def test_initialization(self):
        """
        Test TimeValue initialization.
        """
        time_val = TimeValue()

        # Verify basic properties
        assert time_val is not None
        assert time_val._text is None
        assert time_val._value is None


class TestARLiteral:
    """
    Test class for ARLiteral functionality.
    """

    def test_initialization(self):
        """
        Test ARLiteral initialization.
        """
        literal = ARLiteral()

        # Verify basic properties
        assert literal is not None
        assert literal._value is None

    def test_value_property(self):
        """
        Test value property with string values.
        """
        literal = ARLiteral()

        # Test default value
        assert literal.value == ""

        # Set string value
        literal.value = "test"
        assert literal.value == "test"
        assert str(literal) == "test"

    def test_upper_method(self):
        """
        Test upper method.
        """
        literal = ARLiteral()
        literal.value = "test"
        assert literal.upper() == "TEST"


class TestAREnum:
    """
    Test class for AREnum functionality.
    """

    def test_initialization(self):
        """
        Test AREnum initialization.
        """
        enum_values = ["value1", "value2", "value3"]
        enum = AREnum(enum_values)

        # Verify basic properties
        assert enum is not None
        assert enum.getEnumValues() == enum_values

    def test_set_enum_values(self):
        """
        Test setEnumValues method.
        """
        enum_values = ["value1", "value2"]
        new_values = ["value3", "value4"]
        enum = AREnum(enum_values)

        # Set new enum values
        result = enum.setEnumValues(new_values)
        assert result is enum  # Verify method chaining
        assert enum.getEnumValues() == new_values

    def test_validate_enum_value(self):
        """
        Test validateEnumValue method.
        """
        enum_values = ["value1", "value2", "value3"]
        enum = AREnum(enum_values)

        # Test valid value
        assert enum.validateEnumValue("value1") is True
        assert enum.validateEnumValue("value2") is True

        # Test invalid value
        assert enum.validateEnumValue("invalid") is False


class TestString:
    """
    Test class for String functionality.
    """

    def test_initialization(self):
        """
        Test String initialization.
        """
        string_val = String()

        # Verify basic properties
        assert string_val is not None
        assert string_val._value is None


class TestReferrableSubtypesEnum:
    """
    Test class for ReferrableSubtypesEnum functionality.
    """

    def test_initialization(self):
        """
        Test ReferrableSubtypesEnum initialization.
        """
        enum = ReferrableSubtypesEnum()

        # Verify basic properties
        assert enum is not None
        assert enum._value is None


class TestARPositiveInteger:
    """
    Test class for ARPositiveInteger functionality.
    """

    def test_initialization(self):
        """
        Test ARPositiveInteger initialization.
        """
        pos_int = ARPositiveInteger()

        # Verify basic properties
        assert pos_int is not None
        assert pos_int.shortLabel is None
        assert pos_int._text is None
        assert pos_int._value is None

    def test_value_property_positive(self):
        """
        Test value property with positive integer values.
        """
        pos_int = ARPositiveInteger()

        # Set positive integer value
        pos_int.value = 42
        assert pos_int.value == 42
        assert str(pos_int) == "42"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        pos_int = ARPositiveInteger()

        # Set string value that converts to positive integer
        pos_int.value = "42"
        assert pos_int.value == 42
        assert str(pos_int) == "42"

    def test_negative_value_error(self):
        """
        Test that negative integer values raise an error.
        """
        pos_int = ARPositiveInteger()
        try:
            pos_int.value = -5
            assert False, "Should raise ValueError for negative value"
        except ValueError:
            pass  # Expected behavior


class TestARBoolean:
    """
    Test class for ARBoolean functionality.
    """

    def test_initialization(self):
        """
        Test ARBoolean initialization.
        """
        boolean = ARBoolean()

        # Verify basic properties
        assert boolean is not None
        assert boolean._text is None
        assert boolean._value is None

    def test_value_property_bool(self):
        """
        Test value property with boolean values.
        """
        boolean = ARBoolean()

        # Set boolean value
        boolean.value = True
        assert boolean.value is True
        assert str(boolean) == "true"

        boolean.value = False
        assert boolean.value is False
        assert str(boolean) == "false"

    def test_value_property_int(self):
        """
        Test value property with integer values.
        """
        boolean = ARBoolean()

        # Set integer value
        boolean.value = 1
        assert boolean.value is True
        assert str(boolean) == "1"

        boolean.value = 0
        assert boolean.value is False
        assert str(boolean) == "0"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        boolean = ARBoolean()

        # Set string values that convert to boolean
        boolean.value = "true"
        assert boolean.value is True
        assert str(boolean) == "true"

        boolean.value = "false"
        assert boolean.value is False
        assert str(boolean) == "false"

        boolean.value = "1"
        assert boolean.value is True

        boolean.value = "0"
        assert boolean.value is False

    def test_convert_number_to_boolean(self):
        """
        Test _convertNumberToBoolean method.
        """
        boolean = ARBoolean()

        assert boolean._convertNumberToBoolean(0) is False
        assert boolean._convertNumberToBoolean(1) is True
        assert boolean._convertNumberToBoolean(42) is True

    def test_convert_string_to_boolean(self):
        """
        Test _convertStringToBoolean method.
        """
        boolean = ARBoolean()

        assert boolean._convertStringToBoolean("true") is True
        assert boolean._convertStringToBoolean("TRUE") is True
        assert boolean._convertStringToBoolean("1") is True
        assert boolean._convertStringToBoolean("false") is False
        assert boolean._convertStringToBoolean("FALSE") is False
        assert boolean._convertStringToBoolean("0") is False


class TestNameToken:
    """
    Test class for NameToken functionality.
    """

    def test_initialization(self):
        """
        Test NameToken initialization.
        """
        name_token = NameToken()

        # Verify basic properties
        assert name_token is not None
        assert name_token._value is None


class TestPositiveInteger:
    """
    Test class for PositiveInteger functionality.
    """

    def test_initialization(self):
        """
        Test PositiveInteger initialization.
        """
        pos_int = PositiveInteger()

        # Verify basic properties
        assert pos_int is not None
        assert pos_int.shortLabel is None
        assert pos_int._text is None
        assert pos_int._value is None


class TestLimit:
    """
    Test class for Limit functionality.
    """

    def test_initialization(self):
        """
        Test Limit initialization.
        """
        limit = Limit()

        # Verify basic properties
        assert limit is not None
        assert limit.intervalType is None
        assert limit.value is None

    def test_interval_type_methods(self):
        """
        Test interval type methods.
        """
        limit = Limit()

        # Test get/set interval type
        assert limit.getIntervalType() is None

        result = limit.setIntervalType("closed")
        assert result is limit  # Verify method chaining
        assert limit.getIntervalType() == "closed"

    def test_value_methods(self):
        """
        Test value methods.
        """
        limit = Limit()

        # Test get/set value
        assert limit.getValue() is None

        result = limit.setValue("10")
        assert result is limit  # Verify method chaining
        assert limit.getValue() == "10"


class TestRefType:
    """
    Test class for RefType functionality.
    """

    def test_initialization(self):
        """
        Test RefType initialization.
        """
        ref_type = RefType()

        # Verify basic properties
        assert ref_type is not None
        assert ref_type.base is None
        assert ref_type.dest is None
        assert ref_type.value is None

    def test_base_methods(self):
        """
        Test base methods.
        """
        ref_type = RefType()

        # Test get/set base
        assert ref_type.getBase() is None

        result = ref_type.setBase("BaseValue")
        assert result is ref_type  # Verify method chaining
        assert ref_type.getBase() == "BaseValue"

    def test_dest_methods(self):
        """
        Test dest methods.
        """
        ref_type = RefType()

        # Test get/set dest
        assert ref_type.getDest() is None

        result = ref_type.setDest("DestValue")
        assert result is ref_type  # Verify method chaining
        assert ref_type.getDest() == "DestValue"

    def test_value_methods(self):
        """
        Test value methods.
        """
        ref_type = RefType()

        # Test get/set value
        assert ref_type.getValue() is None

        result = ref_type.setValue("Value")
        assert result is ref_type  # Verify method chaining
        assert ref_type.getValue() == "Value"

    def test_get_short_value(self):
        """
        Test getShortValue method.
        """
        ref_type = RefType()

        # Test with valid path
        ref_type.setValue("/Package/Element/ShortName")
        assert ref_type.getShortValue() == "ShortName"

        # Test with simple value
        ref_type.setValue("SimpleValue")
        assert ref_type.getShortValue() == "SimpleValue"

        # Test with None value (should raise ValueError)
        ref_type.setValue(None)
        try:
            ref_type.getShortValue()
            assert False, "Should raise ValueError for None value"
        except ValueError:
            pass  # Expected behavior


class TestTRefType:
    """
    Test class for TRefType functionality.
    """

    def test_initialization(self):
        """
        Test TRefType initialization.
        """
        t_ref_type = TRefType()

        # Verify basic properties
        assert t_ref_type is not None
        assert t_ref_type.base is None
        assert t_ref_type.dest is None
        assert t_ref_type.value is None


class TestArgumentDirectionEnum:
    """
    Test class for ArgumentDirectionEnum functionality.
    """

    def test_initialization(self):
        """
        Test ArgumentDirectionEnum initialization.
        """
        enum = ArgumentDirectionEnum()

        # Verify basic properties
        assert enum is not None
        # Enum values are stored as a tuple, not a list
        assert enum.getEnumValues() == ("in", "inout", "out")

    def test_enum_values(self):
        """
        Test ArgumentDirectionEnum values.
        """
        enum = ArgumentDirectionEnum()

        assert ArgumentDirectionEnum.IN == "in"
        assert ArgumentDirectionEnum.INOUT == "inout"
        assert ArgumentDirectionEnum.OUT == "out"

        # Test validation
        assert enum.validateEnumValue("in") is True
        assert enum.validateEnumValue("inout") is True
        assert enum.validateEnumValue("out") is True
        assert enum.validateEnumValue("invalid") is False


class TestByteOrderEnum:
    """
    Test class for ByteOrderEnum functionality.
    """

    def test_initialization(self):
        """
        Test ByteOrderEnum initialization.
        """
        enum = ByteOrderEnum()

        # Verify basic properties
        assert enum is not None
        assert enum.getEnumValues() == []


class TestCIdentifier:
    """
    Test class for CIdentifier functionality.
    """

    def test_initialization(self):
        """
        Test CIdentifier initialization.
        """
        c_id = CIdentifier()

        # Verify basic properties
        assert c_id is not None
        assert c_id._value is None
        assert c_id.blueprintValue is None
        assert c_id.namePattern is None

    def test_blueprint_value_methods(self):
        """
        Test blueprint value methods.
        """
        c_id = CIdentifier()

        # Test get/set blueprint value
        assert c_id.getBlueprintValue() is None

        result = c_id.setBlueprintValue("TestValue")
        assert result is c_id  # Verify method chaining
        assert c_id.getBlueprintValue() == "TestValue"

    def test_name_pattern_methods(self):
        """
        Test name pattern methods.
        """
        c_id = CIdentifier()

        # Test get/set name pattern
        assert c_id.getNamePattern() is None

        result = c_id.setNamePattern("TestPattern")
        assert result is c_id  # Verify method chaining
        assert c_id.getNamePattern() == "TestPattern"

    def test_arnumerical_unsupported_type(self):
        """
        Test ARNumerical with unsupported type to cover line 123.
        """
        numerical = ARNumerical()

        # Try to set value with unsupported type
        try:
            numerical.value = [1, 2, 3]  # list is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arfloat_unsupported_type(self):
        """
        Test ARFloat with unsupported type to cover line 191.
        """
        ar_float = ARFloat()

        # Try to set value with unsupported type
        try:
            ar_float.value = {'key': 'value'}  # dict is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arnumerical_invalid_string_conversion(self):
        """
        Test ARNumerical _convertStringToNumberValue with invalid string to cover lines 106-108.
        """
        numerical = ARNumerical()

        # Test the exception path in _convertStringToNumberValue
        try:
            numerical._convertStringToNumberValue('invalid_number')
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arpositiveinteger_unsupported_type(self):
        """
        Test ARPositiveInteger with unsupported type to cover line 351.
        """
        pos_int = ARPositiveInteger()

        try:
            pos_int.value = object()  # object is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arboolean_unsupported_type(self):
        """
        Test ARBoolean with unsupported type to cover line 413.
        """
        boolean = ARBoolean()

        try:
            boolean.value = set([1, 2, 3])  # set is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arboolean_convert_string_to_boolean_invalid(self):
        """
        Test ARBoolean _convertStringToBoolean with invalid string to cover line 395.
        """
        boolean = ARBoolean()

        # This should trigger the recursive call to convertNumberToBoolean with a string that needs to be converted to int first
        result = boolean._convertStringToBoolean('42')
        assert result is True  # 42 as int would be truthy

    def test_arnumerical_get_value(self):
        """
        Test ARNumerical getValue method to cover line 138.
        """
        numerical = ARNumerical()
        numerical.value = 42
        result = numerical.getValue()
        assert result == 42

    def test_arliteral_value_setter_with_non_string(self):
        """
        Test ARLiteral value setter with non-string to cover line 245.
        """
        literal = ARLiteral()
        literal.value = 123  # non-string value that should be converted to string
        assert literal.value == "123"

    def test_constructors_for_various_types(self):
        """
        Test constructors of various types to cover super().__init__() calls.
        """
        # These will cover the super().__init__() calls on various lines
        pos_int = PositiveInteger()
        assert pos_int is not None

        int_val = Integer()
        assert int_val is not None

        bool_val = Boolean()
        assert bool_val is not None

        identifier = Identifier()
        assert identifier is not None

        c_identifier = CIdentifier()
        assert c_identifier is not None

        limit = Limit()
        assert limit is not None

        ref_type = RefType()
        assert ref_type is not None

        t_ref_type = TRefType()
        assert t_ref_type is not None

        diag_id = DiagRequirementIdString()
        assert diag_id is not None

        ip4_addr = Ip4AddressString()
        assert ip4_addr is not None

        ip6_addr = Ip6AddressString()
        assert ip6_addr is not None

        mac_addr = MacAddressString()
        assert mac_addr is not None

        category = CategoryString()
        assert category is not None

        date_time = DateTime()
        assert date_time is not None

        verbatim = VerbatimString()
        assert verbatim is not None

        regex = RegularExpression()
        assert regex is not None

        unlimited_int = UnlimitedInteger()
        assert unlimited_int is not None
