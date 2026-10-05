"""
This module contains comprehensive tests for the PrimitiveTypes.py file
in the AUTOSAR GenericStructure module.
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    AlignmentType,
    AnyServiceInstanceId,
    AnyVersionString,
    AREnum,
    ArgumentDirectionEnum,
    ARLiteral,
    ARType,
    BaseTypeEncodingString,
    Boolean,
    ByteOrderEnum,
    CategoryString,
    CIdentifier,
    CseCodeType,
    DateTime,
    DiagnosticClearDtcLimitationEnum,
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticConnectedIndicatorBehaviorEnum,
    DiagnosticDebounceBehaviorEnum,
    DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticEventDisplacementStrategyEnum,
    DiagnosticEventKindEnum,
    DiagnosticEventWindowTimeEnum,
    DiagnosticHandleDDDIConfigurationEnum,
    DiagnosticInhibitionMaskEnum,
    DiagnosticIumprKindEnum,
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticObdSupportEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    DiagnosticOperationCycleTypeEnum,
    DiagnosticPeriodicRateCategoryEnum,
    DiagnosticRecordTriggerEnum,
    DiagnosticResponseOnEventActionEnum,
    DiagnosticResponseToEcuResetEnum,
    DiagnosticSignificanceEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
    DiagnosticTestResultUpdateEnum,
    DiagnosticTroubleCodeJ1939DtcKindEnum,
    DiagnosticTypeOfDtcSupportedEnum,
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
    DiagRequirementIdString,
    DisplayFormatString,
    Float,
    Identifier,
    Integer,
    IntervalTypeEnum,
    Ip4AddressString,
    Ip6AddressString,
    Limit,
    MacAddressString,
    McdIdentifier,
    MimeTypeString,
    MonotonyEnum,
    NameToken,
    NameTokens,
    NativeDeclarationString,
    Numerical,
    PositiveInteger,
    PositiveUnlimitedInteger,
    PrimitiveIdentifier,
    Ref,
    ReferrableSubtypesEnum,
    RefType,
    RegularExpression,
    RevisionLabelString,
    SectionInitializationPolicyType,
    String,
    SymbolString,
    TimeValue,
    TRefType,
    UnlimitedInteger,
    UriString,
    VerbatimString,
    VerbatimStringPlain,
    ViewTokens,
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
        assert obj._value is None

    def test_timestamp(self):
        """
        Test the timestamp attribute in ARType (uuid is owned by Identifiable).
        """
        obj = ARType()

        # Test setting values
        obj.timestamp = "2023-01-01"
        assert obj.timestamp == "2023-01-01"

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


class TestNumerical:
    """
    Test class for Numerical functionality.
    """

    def test_initialization(self):
        """
        Test Numerical initialization.
        """
        numerical = Numerical()

        # Verify basic properties
        assert numerical is not None
        assert numerical.shortLabel is None
        assert numerical._text is None
        assert numerical._value is None

    def test_value_property_int(self):
        """
        Test value property with integer values.
        """
        numerical = Numerical()

        # Set integer value
        numerical.value = 42
        assert numerical.value == 42
        assert str(numerical) == "42"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        numerical = Numerical()

        # Set string value that converts to integer
        numerical.value = "42"
        assert numerical.value == 42
        assert str(numerical) == "42"

    def test_convert_string_to_number_value(self):
        """
        Test _convertStringToNumberValue method.
        """
        numerical = Numerical()

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
        numerical = Numerical()

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


class TestFloat:
    """
    Test class for Float functionality.
    """

    def test_initialization(self):
        """
        Test Float initialization.
        """
        ar_float = Float()

        # Verify basic properties
        assert ar_float is not None
        assert ar_float._text is None
        assert ar_float._value is None

    def test_value_property_float(self):
        """
        Test value property with float values.
        """
        ar_float = Float()

        # Set float value
        ar_float.value = 42.5
        assert ar_float.value == 42.5
        assert str(ar_float) == "42.5"

    def test_value_property_int(self):
        """
        Test value property with integer values (should convert to float).
        """
        ar_float = Float()

        # Set integer value
        ar_float.value = 42
        assert ar_float.value == 42.0
        assert str(ar_float) == "42.0"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        ar_float = Float()

        # Set string value that converts to float
        ar_float.value = "42.5"
        assert ar_float.value == 42.5
        assert str(ar_float) == "42.5"


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

    def test_set_value(self):
        """
        Test String value assignment.
        """
        string_val = String().setValue("Hello World")
        assert string_val.getValue() == "Hello World"


class TestAlignmentType:
    """
    Test class for AlignmentType functionality (Table 8.3).
    """

    def test_initialization(self):
        """
        Test AlignmentType initialization defaults.
        """
        alignment = AlignmentType()

        # Verify basic properties
        assert alignment is not None
        assert isinstance(alignment, ARLiteral)
        assert alignment._value is None
        assert alignment.getValue() == ""

    def test_get_set_value(self):
        """
        Test AlignmentType get/set round-trip and None no-op.
        """
        alignment = AlignmentType()
        assert alignment.setValue("8") is alignment
        assert alignment.getValue() == "8"

        alignment.setValue("UNSPECIFIED")
        assert alignment.getValue() == "UNSPECIFIED"

        # None is a no-op
        alignment.setValue(None)
        assert alignment.getValue() == "UNSPECIFIED"


class TestSectionInitializationPolicyType:
    """
    Test class for SectionInitializationPolicyType functionality.
    """

    def test_initialization(self):
        policy = SectionInitializationPolicyType()

        assert policy is not None
        assert policy._value is None

    def test_set_value(self):
        policy = SectionInitializationPolicyType().setValue("INIT")
        assert policy.getValue() == "INIT"

        cleared = SectionInitializationPolicyType().setValue(SectionInitializationPolicyType.CLEARED)
        assert cleared.getValue() == "CLEARED"

        power_on_cleared = SectionInitializationPolicyType().setValue(SectionInitializationPolicyType.POWER_ON_CLEARED)
        assert power_on_cleared.getValue() == "POWER-ON-CLEARED"


class TestCseCodeType:
    """
    Test class for CseCodeType functionality.
    """

    def test_initialization(self):
        """
        Test CseCodeType initialization.
        """
        cse = CseCodeType()

        # Verify basic properties
        assert cse is not None
        assert cse._value is None

    def test_set_value(self):
        """
        Test CseCodeType value assignment.
        """
        cse = CseCodeType().setValue("100")
        assert cse.getValue() == "100"

        cse_zero = CseCodeType().setValue("0")
        assert cse_zero.getValue() == "0"


class TestDisplayFormatString:
    """
    Test class for DisplayFormatString functionality.
    """

    def test_initialization(self):
        """
        Test DisplayFormatString initialization.
        """
        display_format = DisplayFormatString()
        assert display_format is not None
        assert display_format._value is None

    def test_set_value(self):
        """
        Test DisplayFormatString value assignment.
        """
        display_format = DisplayFormatString().setValue("%5.2f")
        assert display_format.getValue() == "%5.2f"


class TestNativeDeclarationString:
    """
    Test class for NativeDeclarationString functionality.
    """

    def test_initialization(self):
        """
        Test NativeDeclarationString initialization.
        """
        native_declaration = NativeDeclarationString()
        assert native_declaration is not None
        assert native_declaration._value is None

    def test_set_value(self):
        """
        Test NativeDeclarationString value assignment.
        """
        native_declaration = NativeDeclarationString().setValue("volatile")
        assert native_declaration.getValue() == "volatile"


class TestPrimitiveIdentifier:
    """
    Test class for PrimitiveIdentifier functionality.
    """

    def test_initialization(self):
        """
        Test PrimitiveIdentifier initialization.
        """
        primitive_identifier = PrimitiveIdentifier()
        assert primitive_identifier is not None
        assert primitive_identifier._value is None

    def test_set_value(self):
        """
        Test PrimitiveIdentifier value assignment.
        """
        primitive_identifier = PrimitiveIdentifier().setValue("INFORMAL")
        assert primitive_identifier.getValue() == "INFORMAL"


@pytest.mark.parametrize(
    "primitive_type, value, expected",
    [
        (UriString, "https://example.com/resource", "https://example.com/resource"),
        (BaseTypeEncodingString, "PACKED", "PACKED"),
        (PositiveUnlimitedInteger, "1", 1.0),
        (RevisionLabelString, "R23-11", "R23-11"),
        (SymbolString, "MySymbol", "MySymbol"),
        (McdIdentifier, "MCD-1", "MCD-1"),
    ],
)
def test_remaining_primitive_types_support_initialization_and_value_roundtrip(primitive_type, value, expected):
    primitive = primitive_type()

    assert primitive is not None
    assert primitive._value is None
    assert primitive.setValue(value) is primitive
    assert primitive.getValue() == expected


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

    def test_value_property_positive(self):
        """
        Test value property with positive integer values.
        """
        pos_int = PositiveInteger()

        # Set positive integer value
        pos_int.value = 42
        assert pos_int.value == 42
        assert str(pos_int) == "42"

    def test_value_property_string(self):
        """
        Test value property with string values.
        """
        pos_int = PositiveInteger()

        # Set string value that converts to positive integer
        pos_int.value = "42"
        assert pos_int.value == 42
        assert str(pos_int) == "42"

    def test_negative_value_error(self):
        """
        Test that negative integer values raise an error.
        """
        pos_int = PositiveInteger()
        try:
            pos_int.value = -5
            assert False, "Should raise ValueError for negative value"
        except ValueError:
            pass  # Expected behavior

    def test_set_value_string(self):
        """Test setValue with decimal string round-trip and method chaining."""
        pos_int = PositiveInteger()
        assert pos_int.setValue("42") is pos_int
        assert pos_int.getValue() == 42
        assert str(pos_int) == "42"

    def test_set_value_int(self):
        """Test setValue with an int round-trip."""
        pos_int = PositiveInteger()
        pos_int.setValue(7)
        assert pos_int.getValue() == 7

    def test_denotations(self):
        """Test that hexadecimal and binary denotations are supported."""
        assert PositiveInteger().setValue("255").getValue() == 255
        assert PositiveInteger().setValue("0xFF").getValue() == 255
        assert PositiveInteger().setValue("0b101").getValue() == 5

    def test_zero_is_valid(self):
        """Test that 0 is within the valid range (0..4294967295)."""
        pos_int = PositiveInteger()
        pos_int.setValue(0)
        assert pos_int.getValue() == 0

    def test_negative_raises(self):
        """Test that a negative value is rejected."""
        with pytest.raises(ValueError):
            PositiveInteger().setValue(-1)


class TestBoolean:
    """
    Test class for Boolean functionality.
    """

    def test_initialization(self):
        """
        Test Boolean initialization.
        """
        boolean = Boolean()

        # Verify basic properties
        assert boolean is not None
        assert boolean._text is None
        assert boolean._value is None

    def test_value_property_bool(self):
        """
        Test value property with boolean values.
        """
        boolean = Boolean()

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
        boolean = Boolean()

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
        boolean = Boolean()

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
        boolean = Boolean()

        assert boolean._convertNumberToBoolean(0) is False
        assert boolean._convertNumberToBoolean(1) is True
        assert boolean._convertNumberToBoolean(42) is True

    def test_convert_string_to_boolean(self):
        """
        Test _convertStringToBoolean method.
        """
        boolean = Boolean()

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


class TestIntervalTypeEnum:
    """
    Test class for IntervalTypeEnum functionality.
    """

    def test_initialization(self):
        enum = IntervalTypeEnum()
        enum.setValue(IntervalTypeEnum.OPEN)
        assert enum.getValue() == "open"

    def test_enum_values(self):
        enum = IntervalTypeEnum()

        assert IntervalTypeEnum.CLOSED == "closed"
        assert IntervalTypeEnum.OPEN == "open"

        assert enum.validateEnumValue("closed") is True
        assert enum.validateEnumValue("open") is True
        assert enum.validateEnumValue("invalid") is False


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
        assert limit.getIntervalType() is None
        assert limit.getValue() is None

    def test_interval_type_methods(self):
        """
        Test interval type methods.
        """
        limit = Limit()

        # Test get/set interval type
        assert limit.getIntervalType() is None

        result = limit.setIntervalType(IntervalTypeEnum().setValue("closed"))
        assert result is limit  # Verify method chaining
        assert limit.getIntervalType().getValue() == "closed"

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


BASE_NOTE = "This attribute reflects the base to be used for this reference."
BLUEPRINT_NOTE = "This represents a description that documents how the value shall be defined when deriving objects from the blueprint."
INDEX_NOTE = (
    "This attribute supports the use case to point on specific elements in an array. This is in particular required if arrays are used to implement "
    "particular data objects. The counting of array indices starts with the value 0, i.e. the index of the first array element is 0."
)
REF_NOTE = (
    "This primitive denotes a name based reference. For detailed syntax see the xsd.pattern. \u2022 first slash (relative or absolute reference) [optional] "
    "\u2022 Identifier [required] \u2022 a sequence of slashes and Identifiers [optional] This primitive is used by the meta-model tools to create the references."
)


class TestRef:
    """
    Spec-contract tests for the AUTOSAR Primitive Ref (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 5.35, p.318).
    """

    def test_defaults(self):
        ref = Ref()

        assert ref.getBase() is None
        assert ref.getBlueprintValue() is None
        assert ref.getIndex() is None
        assert ref.getValue() == ""

    def test_is_ar_literal_subclass(self):
        assert issubclass(Ref, ARLiteral)
        assert isinstance(Ref(), ARLiteral)

    def test_value_round_trip(self):
        ref = Ref()

        result = ref.setValue("/Demo/EnumerationTables/ActiveComponent/E")

        assert result is ref
        assert ref.getValue() == "/Demo/EnumerationTables/ActiveComponent/E"

    def test_base_methods(self):
        ref = Ref()

        assert ref.getBase() is None
        result = ref.setBase(Identifier().setValue("/Demo/EnumerationTables"))

        assert result is ref
        assert isinstance(ref.getBase(), Identifier)
        assert ref.getBase().getValue() == "/Demo/EnumerationTables"
        ref.setBase(None)
        assert ref.getBase().getValue() == "/Demo/EnumerationTables"

    def test_blueprint_value_methods(self):
        ref = Ref()

        assert ref.getBlueprintValue() is None
        result = ref.setBlueprintValue(String().setValue("derived"))

        assert result is ref
        assert ref.getBlueprintValue().getValue() == "derived"
        ref.setBlueprintValue(None)
        assert ref.getBlueprintValue().getValue() == "derived"

    def test_index_methods(self):
        ref = Ref()

        assert ref.getIndex() is None
        result = ref.setIndex(PositiveInteger().setValue("0"))

        assert result is ref
        assert ref.getIndex().getValue() == 0
        ref.setIndex(None)
        assert ref.getIndex().getValue() == 0

    def test_docstrings(self):
        assert Ref.getBase.__doc__.strip() == BASE_NOTE
        assert Ref.getBlueprintValue.__doc__.strip() == BLUEPRINT_NOTE
        assert Ref.getIndex.__doc__.strip() == INDEX_NOTE
        assert Ref.setBase.__doc__.strip().startswith(BASE_NOTE)
        assert Ref.setBlueprintValue.__doc__.strip().startswith(BLUEPRINT_NOTE)
        assert Ref.setIndex.__doc__.strip().startswith(INDEX_NOTE)

    def test_class_docstring_note_and_tags(self):
        doc = Ref.__doc__.strip()

        assert doc.startswith(REF_NOTE)
        assert "* xml.xsd.customType=REF" in doc
        assert "* xml.xsd.pattern=/?[a-zA-Z][a-zA-Z0-9_]{0,127}(/[a-zA-Z][a-zA-Z0-9_]{0,127})*" in doc
        assert "* xml.xsd.type=string" in doc

    def test_type_hints(self):
        assert typing.get_type_hints(Ref.getBase)["return"] == typing.Optional[Identifier]
        assert typing.get_type_hints(Ref.setBase)["value"] == typing.Optional[Identifier]
        assert typing.get_type_hints(Ref.setBase)["return"] is Ref
        assert typing.get_type_hints(Ref.getBlueprintValue)["return"] == typing.Optional[String]
        assert typing.get_type_hints(Ref.getIndex)["return"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ref.setIndex)["value"] == typing.Optional[PositiveInteger]


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
        assert enum.getEnumValues() == [
            "mostSignificantByteFirst",
            "mostSignificantByteLast",
            "opaque",
        ]

    def test_enum_values(self):
        """
        Test ByteOrderEnum values.
        """
        enum = ByteOrderEnum()

        assert ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST == "mostSignificantByteFirst"
        assert ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST == "mostSignificantByteLast"
        assert ByteOrderEnum.OPAQUE == "opaque"

        # Test validation
        assert enum.validateEnumValue("mostSignificantByteFirst") is True
        assert enum.validateEnumValue("mostSignificantByteLast") is True
        assert enum.validateEnumValue("opaque") is True
        assert enum.validateEnumValue("invalid") is False

    def test_set_value_round_trip(self):
        """
        Test ByteOrderEnum instantiability and setValue/getValue round-trip (Swc TPS Table 5.27).
        """
        enum = ByteOrderEnum()
        assert enum.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST) is enum
        assert enum.getValue() == "mostSignificantByteFirst"

        enum.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST)
        assert enum.getValue() == "mostSignificantByteLast"

        enum.setValue(ByteOrderEnum.OPAQUE)
        assert enum.getValue() == "opaque"

    def test_set_value_none_no_op(self):
        """
        Test that setting None does not overwrite an existing ByteOrderEnum value.
        """
        enum = ByteOrderEnum()
        enum.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)
        enum.setValue(None)
        assert enum.getValue() == "mostSignificantByteFirst"


class TestMonotonyEnum:
    """
    Test class for MonotonyEnum functionality.
    """

    def test_initialization(self):
        enum = MonotonyEnum()
        enum.setValue(MonotonyEnum.STRICTLY_INCREASING)
        assert enum.getValue() == "strictlyIncreasing"

    def test_enum_values(self):
        enum = MonotonyEnum()

        assert MonotonyEnum.DECREASING == "decreasing"
        assert MonotonyEnum.INCREASING == "increasing"
        assert MonotonyEnum.MONOTONOUS == "monotonous"
        assert MonotonyEnum.NO_MONOTONY == "noMonotony"
        assert MonotonyEnum.STRICTLY_DECREASING == "strictlyDecreasing"
        assert MonotonyEnum.STRICTLY_INCREASING == "strictlyIncreasing"
        assert MonotonyEnum.STRICT_MONOTONOUS == "strictMonotonous"

        assert enum.validateEnumValue("decreasing") is True
        assert enum.validateEnumValue("strictMonotonous") is True
        assert enum.validateEnumValue("invalid") is False


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
        Test Numerical with unsupported type to cover line 123.
        """
        numerical = Numerical()

        # Try to set value with unsupported type
        try:
            numerical.value = [1, 2, 3]  # list is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arfloat_unsupported_type(self):
        """
        Test Float with unsupported type to cover line 191.
        """
        ar_float = Float()

        # Try to set value with unsupported type
        try:
            ar_float.value = {"key": "value"}  # dict is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arnumerical_invalid_string_conversion(self):
        """
        Test Numerical _convertStringToNumberValue with invalid string to cover lines 106-108.
        """
        numerical = Numerical()

        # Test the exception path in _convertStringToNumberValue
        try:
            numerical._convertStringToNumberValue("invalid_number")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arpositiveinteger_unsupported_type(self):
        """
        Test PositiveInteger with unsupported type to cover line 351.
        """
        pos_int = PositiveInteger()

        try:
            pos_int.value = object()  # object is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arboolean_unsupported_type(self):
        """
        Test Boolean with unsupported type to cover line 413.
        """
        boolean = Boolean()

        try:
            boolean.value = set([1, 2, 3])  # set is not supported
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected behavior

    def test_arboolean_convert_string_to_boolean_invalid(self):
        """
        Test Boolean _convertStringToBoolean with invalid string to cover line 395.
        """
        boolean = Boolean()

        # This should trigger the recursive call to convertNumberToBoolean with a string that needs to be converted to int first
        result = boolean._convertStringToBoolean("42")
        assert result is True  # 42 as int would be truthy

    def test_arnumerical_get_value(self):
        """
        Test Numerical getValue method to cover line 138.
        """
        numerical = Numerical()
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


class TestIdentifier:
    """
    Test class for Identifier functionality.
    """

    def test_initialization(self):
        """
        Test Identifier initialization.
        """
        identifier = Identifier()

        # Verify basic properties
        assert identifier is not None
        assert identifier._value is None
        assert identifier.blueprintValue is None
        assert identifier.namePattern is None

    def test_blueprint_value_methods(self):
        """
        Test blueprint value methods.
        """
        identifier = Identifier()

        assert identifier.getBlueprintValue() is None

        bp_value = String()
        bp_value.setValue("TestValue")
        result = identifier.setBlueprintValue(bp_value)
        assert result is identifier  # Verify method chaining
        assert identifier.getBlueprintValue() == bp_value

        identifier.setBlueprintValue(None)
        assert identifier.getBlueprintValue() == bp_value

    def test_name_pattern_methods(self):
        """
        Test name pattern methods.
        """
        identifier = Identifier()

        assert identifier.getNamePattern() is None

        name_pattern = String()
        name_pattern.setValue("TestPattern")
        result = identifier.setNamePattern(name_pattern)
        assert result is identifier  # Verify method chaining
        assert identifier.getNamePattern() == name_pattern

        identifier.setNamePattern(None)
        assert identifier.getNamePattern() == name_pattern


class TestVerbatimString:
    """
    Test class for VerbatimString functionality.
    """

    def test_initialization(self):
        verbatim = VerbatimString()
        assert verbatim is not None
        assert verbatim._value is None

    def test_subclass_of_arliteral(self):
        verbatim = VerbatimString()
        assert isinstance(verbatim, ARLiteral)

    def test_set_get_value(self):
        verbatim = VerbatimString()
        assert verbatim.setValue("verbatim text") is verbatim
        assert verbatim.getValue() == "verbatim text"


class TestVerbatimStringPlain:
    """
    Test class for VerbatimStringPlain functionality.
    """

    def test_initialization(self):
        verbatim = VerbatimStringPlain()
        assert verbatim is not None
        assert verbatim._value is None

    def test_set_get_value(self):
        verbatim = VerbatimStringPlain()
        assert verbatim.setValue("plain text") is verbatim
        assert verbatim.getValue() == "plain text"


class TestNumericalConversion:
    """
    Test class for Numerical functionality.
    """

    def test_initialization(self):
        numerical = Numerical()
        assert numerical is not None
        assert numerical._value is None

    def test_set_get_value(self):
        numerical = Numerical()
        assert numerical.setValue("0x1F") is numerical
        assert numerical.getValue() == 31


class TestAnyServiceInstanceId:
    """
    Test class for AnyServiceInstanceId functionality (Table E.6).
    """

    def test_initialization(self):
        """
        Test AnyServiceInstanceId initialization.
        """
        instance_id = AnyServiceInstanceId()

        assert instance_id is not None
        assert instance_id._value is None

    def test_set_get_value_decimal(self):
        """Test setValue with a decimal string round-trip and method chaining."""
        instance_id = AnyServiceInstanceId()
        assert instance_id.setValue("65535") is instance_id
        assert str(instance_id) == "65535"

    def test_denotations(self):
        """Test that decimal, octal, hexadecimal denotations are supported as text."""
        assert AnyServiceInstanceId().setValue("42").value == "42"
        assert AnyServiceInstanceId().setValue("0x10").value == "0x10"
        assert AnyServiceInstanceId().setValue("0o17").value == "0o17"

    def test_special_literals(self):
        """Test that the ALL literal (and deprecated ANY) are stored verbatim."""
        assert AnyServiceInstanceId().setValue("ALL").value == "ALL"
        assert AnyServiceInstanceId().setValue("ANY").value == "ANY"


class TestAnyVersionString:
    """
    Test class for AnyVersionString functionality (Table E.7).
    """

    def test_initialization(self):
        """
        Test AnyVersionString initialization.
        """
        version = AnyVersionString()

        assert version is not None
        assert version._value is None

    def test_set_get_value(self):
        """Test setValue round-trip and method chaining."""
        version = AnyVersionString()
        assert version.setValue("4") is version
        assert str(version) == "4"

    def test_any_literal(self):
        """Test that the ANY literal is stored verbatim."""
        assert AnyVersionString().setValue("ANY").value == "ANY"


class TestMacAddressString:
    """
    Test class for MacAddressString functionality (Table 4.53).
    """

    def test_initialization(self):
        """
        Test MacAddressString initialization.
        """
        mac_addr = MacAddressString()

        assert mac_addr is not None
        assert isinstance(mac_addr, ARLiteral)
        assert mac_addr._value is None

    def test_set_get_value(self):
        """Test setValue round-trip and method chaining."""
        mac_addr = MacAddressString()
        assert mac_addr.setValue("FF:FF:FF:FF:FF:FF") is mac_addr
        assert mac_addr.value == "FF:FF:FF:FF:FF:FF"
        assert str(mac_addr) == "FF:FF:FF:FF:FF:FF"

    def test_mac_notation_stored_verbatim(self):
        """Test that colon-grouped hex pairs are stored verbatim in any letter case."""
        assert MacAddressString().setValue("00:11:22:33:44:55").value == "00:11:22:33:44:55"
        assert MacAddressString().setValue("aa:bb:cc:dd:ee:ff").value == "aa:bb:cc:dd:ee:ff"

    def test_class_docstring_matches_spec_note(self):
        """Test the class docstring is the Table 4.53 Note copied verbatim plus the Tags tail."""
        expected = (
            "This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF Alternative notations, "
            "e.g. using dash instead of colon, or another grouping of numbers, is not allowed.\n"
            "\n"
            "Tags:\n"
            "    * xml.xsd.customType=MAC-ADDRESS-STRING\n"
            "    * xml.xsd.pattern=([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\n"
            "    * xml.xsd.type=string"
        )
        assert inspect.cleandoc(MacAddressString.__doc__) == expected


class TestMimeTypeString:
    """
    Test class for MimeTypeString functionality (Table 4.55).
    """

    def test_initialization(self):
        """
        Test MimeTypeString initialization.
        """
        mime_type = MimeTypeString()

        assert mime_type is not None
        assert isinstance(mime_type, ARLiteral)
        assert mime_type._value is None

    def test_set_get_value(self):
        """Test setValue round-trip and method chaining."""
        mime_type = MimeTypeString()
        assert mime_type.setValue("application/xml") is mime_type
        assert mime_type.value == "application/xml"
        assert str(mime_type) == "application/xml"


class TestNameTokens:
    """
    Test class for NameTokens functionality (Table 4.56).
    """

    def test_initialization(self):
        """
        Test NameTokens initialization.
        """
        name_tokens = NameTokens()

        assert name_tokens is not None
        assert isinstance(name_tokens, ARLiteral)
        assert name_tokens._value is None

    def test_set_get_value(self):
        """Test setValue round-trip and method chaining."""
        name_tokens = NameTokens()
        assert name_tokens.setValue("TokenA TokenB") is name_tokens
        assert name_tokens.value == "TokenA TokenB"
        assert str(name_tokens) == "TokenA TokenB"


class TestViewTokens:
    """
    Test class for ViewTokens functionality (Table 9.78).
    """

    def test_initialization(self):
        """
        Test ViewTokens initialization.
        """
        view_tokens = ViewTokens()

        assert view_tokens is not None
        assert isinstance(view_tokens, ARLiteral)
        assert view_tokens._value is None

    def test_set_get_value(self):
        """Test setValue round-trip and method chaining."""
        view_tokens = ViewTokens()
        assert view_tokens.setValue("INTERNAL DETAILED") is view_tokens
        assert view_tokens.value == "INTERNAL DETAILED"
        assert str(view_tokens) == "INTERNAL DETAILED"


class TestAclScopeEnum:
    """
    Test class for AclScopeEnum functionality (Table 11.6).
    """

    def test_initialization(self):
        """
        Test AclScopeEnum initialization.
        """
        enum = AclScopeEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["dependant", "descendant", "explicit"]

    def test_enum_values(self):
        """
        Test AclScopeEnum values.
        """
        enum = AclScopeEnum()

        assert AclScopeEnum.DEPENDANT == "dependant"
        assert AclScopeEnum.DESCENDANT == "descendant"
        assert AclScopeEnum.EXPLICIT == "explicit"

        # Test validation
        assert enum.validateEnumValue("dependant") is True
        assert enum.validateEnumValue("descendant") is True
        assert enum.validateEnumValue("explicit") is True
        assert enum.validateEnumValue("invalid") is False


class TestSymbolStringMembers:
    """
    Test class for SymbolString spec attributes (Table 4.65).
    """

    def test_initialization(self):
        """
        Test SymbolString initialization.
        """
        symbol = SymbolString()

        assert symbol is not None
        assert symbol._value is None
        assert symbol.blueprintValue is None
        assert symbol.namePattern is None

    def test_blueprint_value_methods(self):
        """
        Test blueprint value methods.
        """
        symbol = SymbolString()

        assert symbol.getBlueprintValue() is None

        result = symbol.setBlueprintValue("TestValue")
        assert result is symbol
        assert symbol.getBlueprintValue() == "TestValue"

    def test_name_pattern_methods(self):
        """
        Test name pattern methods.
        """
        symbol = SymbolString()

        assert symbol.getNamePattern() is None

        result = symbol.setNamePattern("TestPattern")
        assert result is symbol
        assert symbol.getNamePattern() == "TestPattern"


class TestCategoryString:
    """
    Test class for CategoryString functionality (Table 4.47).
    """

    def test_initialization(self):
        obj = CategoryString()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = CategoryString().setValue("MyCategory")
        assert obj.getValue() == "MyCategory"


class TestDateTime:
    """
    Test class for DateTime functionality (Table 4.48).
    """

    def test_initialization(self):
        obj = DateTime()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = DateTime().setValue("2009-07-23T14:38:00+01:00")
        assert obj.getValue() == "2009-07-23T14:38:00+01:00"


class TestDiagRequirementIdString:
    """
    Test class for DiagRequirementIdString functionality (Table 4.49).
    """

    def test_initialization(self):
        obj = DiagRequirementIdString()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = DiagRequirementIdString().setValue("REQ-0042")
        assert obj.getValue() == "REQ-0042"


class TestIp4AddressString:
    """
    Test class for Ip4AddressString functionality (Table 4.51).
    """

    def test_initialization(self):
        obj = Ip4AddressString()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = Ip4AddressString().setValue("255.255.255.255")
        assert obj.getValue() == "255.255.255.255"


class TestIp6AddressString:
    """
    Test class for Ip6AddressString functionality (Table 4.52).
    """

    def test_initialization(self):
        obj = Ip6AddressString()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = Ip6AddressString().setValue("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF")
        assert obj.getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"


class TestRegularExpression:
    """
    Test class for RegularExpression functionality (Table 4.60).
    """

    def test_initialization(self):
        obj = RegularExpression()
        assert obj is not None
        assert obj._value is None

    def test_set_value(self):
        obj = RegularExpression().setValue("[0-9]+")
        assert obj.getValue() == "[0-9]+"


class TestDiagnosticOccurrenceCounterProcessingEnum:
    """
    Test class for DiagnosticOccurrenceCounterProcessingEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.20, p.66
    """

    def test_initialization(self):
        """
        Test DiagnosticOccurrenceCounterProcessingEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticOccurrenceCounterProcessingEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["confirmedDtcBit", "testFailedBit"]

    def test_enum_values(self):
        """
        Test DiagnosticOccurrenceCounterProcessingEnum member values.
        """
        enum = DiagnosticOccurrenceCounterProcessingEnum()

        assert DiagnosticOccurrenceCounterProcessingEnum.CONFIRMED_DTC_BIT == "confirmedDtcBit"
        assert DiagnosticOccurrenceCounterProcessingEnum.TEST_FAILED_BIT == "testFailedBit"

        assert enum.validateEnumValue("confirmedDtcBit") is True
        assert enum.validateEnumValue("testFailedBit") is True
        assert enum.validateEnumValue("invalid") is False


class TestDiagnosticTypeOfDtcSupportedEnum:
    """
    Test class for DiagnosticTypeOfDtcSupportedEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.21, p.66
    """

    def test_initialization(self):
        """
        Test DiagnosticTypeOfDtcSupportedEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticTypeOfDtcSupportedEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "iso11992_4",
            "iso14229_1",
            "iso15031_6",
            "saeJ1939_73",
            "saeJ2012_da",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticTypeOfDtcSupportedEnum member values.
        """
        enum = DiagnosticTypeOfDtcSupportedEnum()

        assert DiagnosticTypeOfDtcSupportedEnum.ISO11992_4 == "iso11992_4"
        assert DiagnosticTypeOfDtcSupportedEnum.ISO14229_1 == "iso14229_1"
        assert DiagnosticTypeOfDtcSupportedEnum.ISO15031_6 == "iso15031_6"
        assert DiagnosticTypeOfDtcSupportedEnum.SAEJ1939_73 == "saeJ1939_73"
        assert DiagnosticTypeOfDtcSupportedEnum.SAEJ2012_DA == "saeJ2012_da"

        assert enum.validateEnumValue("iso11992_4") is True
        assert enum.validateEnumValue("iso14229_1") is True
        assert enum.validateEnumValue("iso15031_6") is True
        assert enum.validateEnumValue("saeJ1939_73") is True
        assert enum.validateEnumValue("saeJ2012_da") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticTypeOfDtcSupportedEnum instantiability and getValue.
        """
        enum = DiagnosticTypeOfDtcSupportedEnum()
        enum.setValue(DiagnosticTypeOfDtcSupportedEnum.ISO14229_1)

        assert enum.getValue() == "iso14229_1"


class TestDiagnosticTypeOfFreezeFrameRecordNumerationEnum:
    """
    Test class for DiagnosticTypeOfFreezeFrameRecordNumerationEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.172, p.184
    """

    def test_initialization(self):
        """
        Test DiagnosticTypeOfFreezeFrameRecordNumerationEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticTypeOfFreezeFrameRecordNumerationEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "calculated",
            "configured",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticTypeOfFreezeFrameRecordNumerationEnum member values.
        """
        enum = DiagnosticTypeOfFreezeFrameRecordNumerationEnum()

        assert DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CALCULATED == "calculated"
        assert DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CONFIGURED == "configured"

        assert enum.validateEnumValue("calculated") is True
        assert enum.validateEnumValue("configured") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticTypeOfFreezeFrameRecordNumerationEnum instantiability and getValue.
        """
        enum = DiagnosticTypeOfFreezeFrameRecordNumerationEnum()
        enum.setValue(DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CALCULATED)

        assert enum.getValue() == "calculated"


class TestDiagnosticEventCombinationBehaviorEnum:
    """
    Test class for DiagnosticEventCombinationBehaviorEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.23, p.67
    """

    def test_initialization(self):
        """
        Test DiagnosticEventCombinationBehaviorEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventCombinationBehaviorEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "eventCombinationOnRetrieval",
            "eventCombinationOnStorage",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticEventCombinationBehaviorEnum member values.
        """
        enum = DiagnosticEventCombinationBehaviorEnum()

        assert DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_RETRIEVAL == "eventCombinationOnRetrieval"
        assert DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_STORAGE == "eventCombinationOnStorage"

        assert enum.validateEnumValue("eventCombinationOnRetrieval") is True
        assert enum.validateEnumValue("eventCombinationOnStorage") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventCombinationBehaviorEnum instantiability and getValue.
        """
        enum = DiagnosticEventCombinationBehaviorEnum()
        enum.setValue(DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_RETRIEVAL)

        assert enum.getValue() == "eventCombinationOnRetrieval"


class TestDiagnosticEventCombinationReportingBehaviorEnum:
    """
    Test class for DiagnosticEventCombinationReportingBehaviorEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.24, p.67
    """

    def test_initialization(self):
        """
        Test DiagnosticEventCombinationReportingBehaviorEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventCombinationReportingBehaviorEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["reportingInChronlogicalOrderOldestFirst"]

    def test_enum_values(self):
        """
        Test DiagnosticEventCombinationReportingBehaviorEnum member values.
        """
        enum = DiagnosticEventCombinationReportingBehaviorEnum()

        assert DiagnosticEventCombinationReportingBehaviorEnum.REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST == "reportingInChronlogicalOrderOldestFirst"

        assert enum.validateEnumValue("reportingInChronlogicalOrderOldestFirst") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventCombinationReportingBehaviorEnum instantiability and getValue.
        """
        enum = DiagnosticEventCombinationReportingBehaviorEnum()
        enum.setValue(DiagnosticEventCombinationReportingBehaviorEnum.REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST)

        assert enum.getValue() == "reportingInChronlogicalOrderOldestFirst"


class TestDiagnosticResponseToEcuResetEnum:
    """
    Test class for DiagnosticResponseToEcuResetEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.62, p.102
    """

    def test_initialization(self):
        """
        Test DiagnosticResponseToEcuResetEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticResponseToEcuResetEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["respondAfterReset", "respondBeforeReset"]

    def test_enum_values(self):
        """
        Test DiagnosticResponseToEcuResetEnum member values.
        """
        enum = DiagnosticResponseToEcuResetEnum()

        assert DiagnosticResponseToEcuResetEnum.RESPOND_AFTER_RESET == "respondAfterReset"
        assert DiagnosticResponseToEcuResetEnum.RESPOND_BEFORE_RESET == "respondBeforeReset"

        assert enum.validateEnumValue("respondAfterReset") is True
        assert enum.validateEnumValue("respondBeforeReset") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticResponseToEcuResetEnum instantiability and getValue.
        """
        enum = DiagnosticResponseToEcuResetEnum()
        enum.setValue(DiagnosticResponseToEcuResetEnum.RESPOND_BEFORE_RESET)

        assert enum.getValue() == "respondBeforeReset"


class TestDiagnosticInhibitionMaskEnum:
    """
    Test class for DiagnosticInhibitionMaskEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.217, p.216
    """

    def test_initialization(self):
        """
        Test DiagnosticInhibitionMaskEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticInhibitionMaskEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["lastFailed", "notTested", "tested", "testedAndFailed"]

    def test_enum_values(self):
        """
        Test DiagnosticInhibitionMaskEnum member values.
        """
        enum = DiagnosticInhibitionMaskEnum()

        assert DiagnosticInhibitionMaskEnum.LAST_FAILED == "lastFailed"
        assert DiagnosticInhibitionMaskEnum.NOT_TESTED == "notTested"
        assert DiagnosticInhibitionMaskEnum.TESTED == "tested"
        assert DiagnosticInhibitionMaskEnum.TESTED_AND_FAILED == "testedAndFailed"

        assert enum.validateEnumValue("lastFailed") is True
        assert enum.validateEnumValue("notTested") is True
        assert enum.validateEnumValue("tested") is True
        assert enum.validateEnumValue("testedAndFailed") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticInhibitionMaskEnum instantiability and getValue.
        """
        enum = DiagnosticInhibitionMaskEnum()
        enum.setValue(DiagnosticInhibitionMaskEnum.TESTED_AND_FAILED)

        assert enum.getValue() == "testedAndFailed"


class TestDiagnosticTroubleCodeJ1939DtcKindEnum:
    """
    Test class for DiagnosticTroubleCodeJ1939DtcKindEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.222, p.221
    """

    def test_initialization(self):
        """
        Test DiagnosticTroubleCodeJ1939DtcKindEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticTroubleCodeJ1939DtcKindEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["serviceOnly", "standard"]

    def test_enum_values(self):
        """
        Test DiagnosticTroubleCodeJ1939DtcKindEnum member values.
        """
        enum = DiagnosticTroubleCodeJ1939DtcKindEnum()

        assert DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY == "serviceOnly"
        assert DiagnosticTroubleCodeJ1939DtcKindEnum.STANDARD == "standard"

        assert enum.validateEnumValue("serviceOnly") is True
        assert enum.validateEnumValue("standard") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticTroubleCodeJ1939DtcKindEnum instantiability and getValue.
        """
        enum = DiagnosticTroubleCodeJ1939DtcKindEnum()
        enum.setValue(DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY)

        assert enum.getValue() == "serviceOnly"


class TestDiagnosticHandleDDDIConfigurationEnum:
    """
    Test class for DiagnosticHandleDDDIConfigurationEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.95, p.128
    """

    def test_initialization(self):
        """
        Test DiagnosticHandleDDDIConfigurationEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticHandleDDDIConfigurationEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["nonVolatile", "volatile"]

    def test_enum_values(self):
        """
        Test DiagnosticHandleDDDIConfigurationEnum member values.
        """
        enum = DiagnosticHandleDDDIConfigurationEnum()

        assert DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE == "nonVolatile"
        assert DiagnosticHandleDDDIConfigurationEnum.VOLATILE == "volatile"

        assert enum.validateEnumValue("nonVolatile") is True
        assert enum.validateEnumValue("volatile") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticHandleDDDIConfigurationEnum instantiability and getValue.
        """
        enum = DiagnosticHandleDDDIConfigurationEnum()
        enum.setValue(DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE)

        assert enum.getValue() == "nonVolatile"


class TestDiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum:
    """
    Test class for DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.96, p.129
    """

    def test_initialization(self):
        """
        Test DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["clearDynamicallyDefineDataIdentifier", "defineByIdentifier", "defineByMemoryAddress"]

    def test_enum_values(self):
        """
        Test DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum member values.
        """
        enum = DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum()

        assert DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER == "clearDynamicallyDefineDataIdentifier"
        assert DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_IDENTIFIER == "defineByIdentifier"
        assert DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_MEMORY_ADDRESS == "defineByMemoryAddress"

        assert enum.validateEnumValue("clearDynamicallyDefineDataIdentifier") is True
        assert enum.validateEnumValue("defineByIdentifier") is True
        assert enum.validateEnumValue("defineByMemoryAddress") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum instantiability and getValue.
        """
        enum = DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum()
        enum.setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_IDENTIFIER)

        assert enum.getValue() == "defineByIdentifier"


class TestDiagnosticPeriodicRateCategoryEnum:
    """
    Test class for DiagnosticPeriodicRateCategoryEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.100, p.131
    """

    def test_initialization(self):
        """
        Test DiagnosticPeriodicRateCategoryEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticPeriodicRateCategoryEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["periodicRateFast", "periodicRateMedium", "periodicRateSlow"]

    def test_enum_values(self):
        """
        Test DiagnosticPeriodicRateCategoryEnum member values.
        """
        enum = DiagnosticPeriodicRateCategoryEnum()

        assert DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST == "periodicRateFast"
        assert DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM == "periodicRateMedium"
        assert DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW == "periodicRateSlow"

        assert enum.validateEnumValue("periodicRateFast") is True
        assert enum.validateEnumValue("periodicRateMedium") is True
        assert enum.validateEnumValue("periodicRateSlow") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticPeriodicRateCategoryEnum instantiability and getValue.
        """
        enum = DiagnosticPeriodicRateCategoryEnum()
        enum.setValue(DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW)

        assert enum.getValue() == "periodicRateSlow"


class TestDiagnosticEventWindowTimeEnum:
    """
    Test class for DiagnosticEventWindowTimeEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.104, p.133
    """

    def test_initialization(self):
        """
        Test DiagnosticEventWindowTimeEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventWindowTimeEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["infiniteTimeToResponse", "powerWindowTime"]

    def test_enum_values(self):
        """
        Test DiagnosticEventWindowTimeEnum member values.
        """
        enum = DiagnosticEventWindowTimeEnum()

        assert DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE == "infiniteTimeToResponse"
        assert DiagnosticEventWindowTimeEnum.POWER_WINDOW_TIME == "powerWindowTime"

        assert enum.validateEnumValue("infiniteTimeToResponse") is True
        assert enum.validateEnumValue("powerWindowTime") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventWindowTimeEnum instantiability and getValue.
        """
        enum = DiagnosticEventWindowTimeEnum()
        enum.setValue(DiagnosticEventWindowTimeEnum.POWER_WINDOW_TIME)

        assert enum.getValue() == "powerWindowTime"


class TestDiagnosticRecordTriggerEnum:
    """
    Test class for DiagnosticRecordTriggerEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.182, p.191
    """

    def test_initialization(self):
        """
        Test DiagnosticRecordTriggerEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticRecordTriggerEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "confirmed",
            "custom",
            "fdcThreshold",
            "pending",
            "testFailed",
            "testFailedThisOperationCycle",
            "testPassed",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticRecordTriggerEnum member values.
        """
        enum = DiagnosticRecordTriggerEnum()

        assert DiagnosticRecordTriggerEnum.CONFIRMED == "confirmed"
        assert DiagnosticRecordTriggerEnum.CUSTOM == "custom"
        assert DiagnosticRecordTriggerEnum.FDC_THRESHOLD == "fdcThreshold"
        assert DiagnosticRecordTriggerEnum.PENDING == "pending"
        assert DiagnosticRecordTriggerEnum.TEST_FAILED == "testFailed"
        assert DiagnosticRecordTriggerEnum.TEST_FAILED_THIS_OPERATION_CYCLE == "testFailedThisOperationCycle"
        assert DiagnosticRecordTriggerEnum.TEST_PASSED == "testPassed"

        assert enum.validateEnumValue("confirmed") is True
        assert enum.validateEnumValue("custom") is True
        assert enum.validateEnumValue("fdcThreshold") is True
        assert enum.validateEnumValue("pending") is True
        assert enum.validateEnumValue("testFailed") is True
        assert enum.validateEnumValue("testFailedThisOperationCycle") is True
        assert enum.validateEnumValue("testPassed") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticRecordTriggerEnum instantiability and getValue.
        """
        enum = DiagnosticRecordTriggerEnum()
        enum.setValue(DiagnosticRecordTriggerEnum.TEST_FAILED_THIS_OPERATION_CYCLE)

        assert enum.getValue() == "testFailedThisOperationCycle"


class TestDiagnosticResponseOnEventActionEnum:
    """
    Test class for DiagnosticResponseOnEventActionEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.105, p.134
    """

    def test_initialization(self):
        """
        Test DiagnosticResponseOnEventActionEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticResponseOnEventActionEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "clear",
            "onChangeOfDataIdentifier",
            "onComparisonOfValues",
            "onDTCStatusChange",
            "report",
            "reportDTCRecordInformationOnDtcStatusChange",
            "reportMostRecentDtcOnStatusChange",
            "start",
            "stop",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticResponseOnEventActionEnum member values.
        """
        enum = DiagnosticResponseOnEventActionEnum()

        assert DiagnosticResponseOnEventActionEnum.CLEAR == "clear"
        assert DiagnosticResponseOnEventActionEnum.ON_CHANGE_OF_DATA_IDENTIFIER == "onChangeOfDataIdentifier"
        assert DiagnosticResponseOnEventActionEnum.ON_COMPARISON_OF_VALUES == "onComparisonOfValues"
        assert DiagnosticResponseOnEventActionEnum.ON_DTC_STATUS_CHANGE == "onDTCStatusChange"
        assert DiagnosticResponseOnEventActionEnum.REPORT == "report"
        assert DiagnosticResponseOnEventActionEnum.REPORT_DTC_RECORD_INFORMATION_ON_DTC_STATUS_CHANGE == "reportDTCRecordInformationOnDtcStatusChange"
        assert DiagnosticResponseOnEventActionEnum.REPORT_MOST_RECENT_DTC_ON_STATUS_CHANGE == "reportMostRecentDtcOnStatusChange"
        assert DiagnosticResponseOnEventActionEnum.START == "start"
        assert DiagnosticResponseOnEventActionEnum.STOP == "stop"

        assert enum.validateEnumValue("clear") is True
        assert enum.validateEnumValue("onChangeOfDataIdentifier") is True
        assert enum.validateEnumValue("onComparisonOfValues") is True
        assert enum.validateEnumValue("onDTCStatusChange") is True
        assert enum.validateEnumValue("report") is True
        assert enum.validateEnumValue("reportDTCRecordInformationOnDtcStatusChange") is True
        assert enum.validateEnumValue("reportMostRecentDtcOnStatusChange") is True
        assert enum.validateEnumValue("start") is True
        assert enum.validateEnumValue("stop") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticResponseOnEventActionEnum instantiability and getValue.
        """
        enum = DiagnosticResponseOnEventActionEnum()
        enum.setValue(DiagnosticResponseOnEventActionEnum.ON_CHANGE_OF_DATA_IDENTIFIER)

        assert enum.getValue() == "onChangeOfDataIdentifier"


class TestDiagnosticClearDtcLimitationEnum:
    """
    Test class for DiagnosticClearDtcLimitationEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.169, p.183
    """

    def test_initialization(self):
        """
        Test DiagnosticClearDtcLimitationEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticClearDtcLimitationEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["allSupportedDtcs", "clearAllDtcs"]

    def test_enum_values(self):
        """
        Test DiagnosticClearDtcLimitationEnum member values.
        """
        enum = DiagnosticClearDtcLimitationEnum()

        assert DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS == "allSupportedDtcs"
        assert DiagnosticClearDtcLimitationEnum.CLEAR_ALL_DTCS == "clearAllDtcs"

        assert enum.validateEnumValue("allSupportedDtcs") is True
        assert enum.validateEnumValue("clearAllDtcs") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticClearDtcLimitationEnum instantiability and getValue.
        """
        enum = DiagnosticClearDtcLimitationEnum()
        enum.setValue(DiagnosticClearDtcLimitationEnum.CLEAR_ALL_DTCS)

        assert enum.getValue() == "clearAllDtcs"


class TestDiagnosticClearEventAllowedBehaviorEnum:
    """
    Test class for DiagnosticClearEventAllowedBehaviorEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.150, p.166
    """

    def test_initialization(self):
        """
        Test DiagnosticClearEventAllowedBehaviorEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticClearEventAllowedBehaviorEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == ["noStatusByteChange", "onlyThisCycleAndReadiness"]

    def test_enum_values(self):
        """
        Test DiagnosticClearEventAllowedBehaviorEnum member values.
        """
        enum = DiagnosticClearEventAllowedBehaviorEnum()

        assert DiagnosticClearEventAllowedBehaviorEnum.NO_STATUS_BYTE_CHANGE == "noStatusByteChange"
        assert DiagnosticClearEventAllowedBehaviorEnum.ONLY_THIS_CYCLE_AND_READINESS == "onlyThisCycleAndReadiness"

        assert enum.validateEnumValue("noStatusByteChange") is True
        assert enum.validateEnumValue("onlyThisCycleAndReadiness") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticClearEventAllowedBehaviorEnum instantiability and getValue.
        """
        enum = DiagnosticClearEventAllowedBehaviorEnum()
        enum.setValue(DiagnosticClearEventAllowedBehaviorEnum.ONLY_THIS_CYCLE_AND_READINESS)

        assert enum.getValue() == "onlyThisCycleAndReadiness"


class TestDiagnosticConnectedIndicatorBehaviorEnum:
    """
    Test class for DiagnosticConnectedIndicatorBehaviorEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.155, p.168
    """

    def test_initialization(self):
        """
        Test DiagnosticConnectedIndicatorBehaviorEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticConnectedIndicatorBehaviorEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "blinkMode",
            "blinkOrContinuousOnMode",
            "continuousOnMode",
            "fastFlashingMode",
            "slowFlashingMode",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticConnectedIndicatorBehaviorEnum member values.
        """
        enum = DiagnosticConnectedIndicatorBehaviorEnum()

        assert DiagnosticConnectedIndicatorBehaviorEnum.BLINK_MODE == "blinkMode"
        assert DiagnosticConnectedIndicatorBehaviorEnum.BLINK_OR_CONTINUOUS_ON_MODE == "blinkOrContinuousOnMode"
        assert DiagnosticConnectedIndicatorBehaviorEnum.CONTINUOUS_ON_MODE == "continuousOnMode"
        assert DiagnosticConnectedIndicatorBehaviorEnum.FAST_FLASHING_MODE == "fastFlashingMode"
        assert DiagnosticConnectedIndicatorBehaviorEnum.SLOW_FLASHING_MODE == "slowFlashingMode"

        assert enum.validateEnumValue("blinkMode") is True
        assert enum.validateEnumValue("blinkOrContinuousOnMode") is True
        assert enum.validateEnumValue("continuousOnMode") is True
        assert enum.validateEnumValue("fastFlashingMode") is True
        assert enum.validateEnumValue("slowFlashingMode") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticConnectedIndicatorBehaviorEnum instantiability and getValue.
        """
        enum = DiagnosticConnectedIndicatorBehaviorEnum()
        enum.setValue(DiagnosticConnectedIndicatorBehaviorEnum.BLINK_OR_CONTINUOUS_ON_MODE)

        assert enum.getValue() == "blinkOrContinuousOnMode"


class TestDiagnosticDebounceBehaviorEnum:
    """
    Test class for DiagnosticDebounceBehaviorEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.192, p.199
    """

    def test_initialization(self):
        """
        Test DiagnosticDebounceBehaviorEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticDebounceBehaviorEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "freeze",
            "reset",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticDebounceBehaviorEnum member values.
        """
        enum = DiagnosticDebounceBehaviorEnum()

        assert DiagnosticDebounceBehaviorEnum.FREEZE == "freeze"
        assert DiagnosticDebounceBehaviorEnum.RESET == "reset"

        assert enum.validateEnumValue("freeze") is True
        assert enum.validateEnumValue("reset") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticDebounceBehaviorEnum instantiability and getValue.
        """
        enum = DiagnosticDebounceBehaviorEnum()
        enum.setValue(DiagnosticDebounceBehaviorEnum.RESET)

        assert enum.getValue() == "reset"


class TestDiagnosticEventClearAllowedEnum:
    """
    Test class for DiagnosticEventClearAllowedEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.153, p.167
    """

    def test_initialization(self):
        """
        Test DiagnosticEventClearAllowedEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventClearAllowedEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "always",
            "requiresCallbackExecution",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticEventClearAllowedEnum member values.
        """
        enum = DiagnosticEventClearAllowedEnum()

        assert DiagnosticEventClearAllowedEnum.ALWAYS == "always"
        assert DiagnosticEventClearAllowedEnum.REQUIRES_CALLBACK_EXECUTION == "requiresCallbackExecution"

        assert enum.validateEnumValue("always") is True
        assert enum.validateEnumValue("requiresCallbackExecution") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventClearAllowedEnum instantiability and getValue.
        """
        enum = DiagnosticEventClearAllowedEnum()
        enum.setValue(DiagnosticEventClearAllowedEnum.REQUIRES_CALLBACK_EXECUTION)

        assert enum.getValue() == "requiresCallbackExecution"


class TestDiagnosticEventDisplacementStrategyEnum:
    """
    Test class for DiagnosticEventDisplacementStrategyEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.170, p.183
    """

    def test_initialization(self):
        """
        Test DiagnosticEventDisplacementStrategyEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventDisplacementStrategyEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "full",
            "none",
            "prioOcc",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticEventDisplacementStrategyEnum member values.
        """
        enum = DiagnosticEventDisplacementStrategyEnum()

        assert DiagnosticEventDisplacementStrategyEnum.FULL == "full"
        assert DiagnosticEventDisplacementStrategyEnum.NONE == "none"
        assert DiagnosticEventDisplacementStrategyEnum.PRIO_OCC == "prioOcc"

        assert enum.validateEnumValue("full") is True
        assert enum.validateEnumValue("none") is True
        assert enum.validateEnumValue("prioOcc") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventDisplacementStrategyEnum instantiability and getValue.
        """
        enum = DiagnosticEventDisplacementStrategyEnum()
        enum.setValue(DiagnosticEventDisplacementStrategyEnum.PRIO_OCC)

        assert enum.getValue() == "prioOcc"


class TestDiagnosticEventKindEnum:
    """
    Test class for DiagnosticEventKindEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.154, p.167
    """

    def test_initialization(self):
        """
        Test DiagnosticEventKindEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticEventKindEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "bsw",
            "swc",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticEventKindEnum member values.
        """
        enum = DiagnosticEventKindEnum()

        assert DiagnosticEventKindEnum.BSW == "bsw"
        assert DiagnosticEventKindEnum.SWC == "swc"

        assert enum.validateEnumValue("bsw") is True
        assert enum.validateEnumValue("swc") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticEventKindEnum instantiability and getValue.
        """
        enum = DiagnosticEventKindEnum()
        enum.setValue(DiagnosticEventKindEnum.SWC)

        assert enum.getValue() == "swc"


class TestDiagnosticIumprKindEnum:
    """
    Test class for DiagnosticIumprKindEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.208, p.210
    """

    def test_initialization(self):
        """
        Test DiagnosticIumprKindEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticIumprKindEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "apiBased",
            "observerBased",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticIumprKindEnum member values.
        """
        enum = DiagnosticIumprKindEnum()

        assert DiagnosticIumprKindEnum.API_BASED == "apiBased"
        assert DiagnosticIumprKindEnum.OBSERVER_BASED == "observerBased"

        assert enum.validateEnumValue("apiBased") is True
        assert enum.validateEnumValue("observerBased") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticIumprKindEnum instantiability and getValue.
        """
        enum = DiagnosticIumprKindEnum()
        enum.setValue(DiagnosticIumprKindEnum.OBSERVER_BASED)

        assert enum.getValue() == "observerBased"


class TestDiagnosticMemoryEntryStorageTriggerEnum:
    """
    Test class for DiagnosticMemoryEntryStorageTriggerEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.168, p.183
    """

    def test_initialization(self):
        """
        Test DiagnosticMemoryEntryStorageTriggerEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticMemoryEntryStorageTriggerEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "confirmed",
            "fdcThreshold",
            "testFailed",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticMemoryEntryStorageTriggerEnum member values.
        """
        enum = DiagnosticMemoryEntryStorageTriggerEnum()

        assert DiagnosticMemoryEntryStorageTriggerEnum.CONFIRMED == "confirmed"
        assert DiagnosticMemoryEntryStorageTriggerEnum.FDC_THRESHOLD == "fdcThreshold"
        assert DiagnosticMemoryEntryStorageTriggerEnum.TEST_FAILED == "testFailed"

        assert enum.validateEnumValue("confirmed") is True
        assert enum.validateEnumValue("fdcThreshold") is True
        assert enum.validateEnumValue("testFailed") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticMemoryEntryStorageTriggerEnum instantiability and getValue.
        """
        enum = DiagnosticMemoryEntryStorageTriggerEnum()
        enum.setValue(DiagnosticMemoryEntryStorageTriggerEnum.FDC_THRESHOLD)

        assert enum.getValue() == "fdcThreshold"


class TestDiagnosticObdSupportEnum:
    """
    Test class for DiagnosticObdSupportEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.206, p.207
    """

    def test_initialization(self):
        """
        Test DiagnosticObdSupportEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticObdSupportEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "masterEcu",
            "noObdSupport",
            "primaryEcu",
            "secondaryEcu",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticObdSupportEnum member values.
        """
        enum = DiagnosticObdSupportEnum()

        assert DiagnosticObdSupportEnum.MASTER_ECU == "masterEcu"
        assert DiagnosticObdSupportEnum.NO_OBD_SUPPORT == "noObdSupport"
        assert DiagnosticObdSupportEnum.PRIMARY_ECU == "primaryEcu"
        assert DiagnosticObdSupportEnum.SECONDARY_ECU == "secondaryEcu"

        assert enum.validateEnumValue("masterEcu") is True
        assert enum.validateEnumValue("noObdSupport") is True
        assert enum.validateEnumValue("primaryEcu") is True
        assert enum.validateEnumValue("secondaryEcu") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticObdSupportEnum instantiability and getValue.
        """
        enum = DiagnosticObdSupportEnum()
        enum.setValue(DiagnosticObdSupportEnum.PRIMARY_ECU)

        assert enum.getValue() == "primaryEcu"


class TestDiagnosticOperationCycleTypeEnum:
    """
    Test class for DiagnosticOperationCycleTypeEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.197, p.201
    """

    def test_initialization(self):
        """
        Test DiagnosticOperationCycleTypeEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticOperationCycleTypeEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "ignition",
            "obdDrivingCycle",
            "other",
            "warmup",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticOperationCycleTypeEnum member values.
        """
        enum = DiagnosticOperationCycleTypeEnum()

        assert DiagnosticOperationCycleTypeEnum.IGNITION == "ignition"
        assert DiagnosticOperationCycleTypeEnum.OBD_DRIVING_CYCLE == "obdDrivingCycle"
        assert DiagnosticOperationCycleTypeEnum.OTHER == "other"
        assert DiagnosticOperationCycleTypeEnum.WARMUP == "warmup"

        assert enum.validateEnumValue("ignition") is True
        assert enum.validateEnumValue("obdDrivingCycle") is True
        assert enum.validateEnumValue("other") is True
        assert enum.validateEnumValue("warmup") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticOperationCycleTypeEnum instantiability and getValue.
        """
        enum = DiagnosticOperationCycleTypeEnum()
        enum.setValue(DiagnosticOperationCycleTypeEnum.WARMUP)

        assert enum.getValue() == "warmup"


class TestDiagnosticSignificanceEnum:
    """
    Test class for DiagnosticSignificanceEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.176, p.187
    """

    def test_initialization(self):
        """
        Test DiagnosticSignificanceEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticSignificanceEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "fault",
            "occurence",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticSignificanceEnum member values.
        """
        enum = DiagnosticSignificanceEnum()

        assert DiagnosticSignificanceEnum.FAULT == "fault"
        assert DiagnosticSignificanceEnum.OCCURENCE == "occurence"

        assert enum.validateEnumValue("fault") is True
        assert enum.validateEnumValue("occurence") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticSignificanceEnum instantiability and getValue.
        """
        enum = DiagnosticSignificanceEnum()
        enum.setValue(DiagnosticSignificanceEnum.OCCURENCE)

        assert enum.getValue() == "occurence"


class TestDiagnosticStatusBitHandlingTestFailedSinceLastClearEnum:
    """
    Test class for DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.171, p.184
    """

    def test_initialization(self):
        """
        Test DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "statusBitAgingAndDisplacement",
            "statusBitNormal",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum member values.
        """
        enum = DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum()

        assert DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_AGING_AND_DISPLACEMENT == "statusBitAgingAndDisplacement"
        assert DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL == "statusBitNormal"

        assert enum.validateEnumValue("statusBitAgingAndDisplacement") is True
        assert enum.validateEnumValue("statusBitNormal") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum instantiability and getValue.
        """
        enum = DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum()
        enum.setValue(DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_AGING_AND_DISPLACEMENT)

        assert enum.getValue() == "statusBitAgingAndDisplacement"


class TestDiagnosticTestResultUpdateEnum:
    """
    Test class for DiagnosticTestResultUpdateEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.202, p.205
    """

    def test_initialization(self):
        """
        Test DiagnosticTestResultUpdateEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticTestResultUpdateEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "always",
            "steady",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticTestResultUpdateEnum member values.
        """
        enum = DiagnosticTestResultUpdateEnum()

        assert DiagnosticTestResultUpdateEnum.ALWAYS == "always"
        assert DiagnosticTestResultUpdateEnum.STEADY == "steady"

        assert enum.validateEnumValue("always") is True
        assert enum.validateEnumValue("steady") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticTestResultUpdateEnum instantiability and getValue.
        """
        enum = DiagnosticTestResultUpdateEnum()
        enum.setValue(DiagnosticTestResultUpdateEnum.STEADY)

        assert enum.getValue() == "steady"


class TestDiagnosticUdsSeverityEnum:
    """
    Test class for DiagnosticUdsSeverityEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.177, p.187
    """

    def test_initialization(self):
        """
        Test DiagnosticUdsSeverityEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticUdsSeverityEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "checkAtNextHalt",
            "immediately",
            "maintenanceOnly",
            "noSeverity",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticUdsSeverityEnum member values.
        """
        enum = DiagnosticUdsSeverityEnum()

        assert DiagnosticUdsSeverityEnum.CHECK_AT_NEXT_HALT == "checkAtNextHalt"
        assert DiagnosticUdsSeverityEnum.IMMEDIATELY == "immediately"
        assert DiagnosticUdsSeverityEnum.MAINTENANCE_ONLY == "maintenanceOnly"
        assert DiagnosticUdsSeverityEnum.NO_SEVERITY == "noSeverity"

        assert enum.validateEnumValue("checkAtNextHalt") is True
        assert enum.validateEnumValue("immediately") is True
        assert enum.validateEnumValue("maintenanceOnly") is True
        assert enum.validateEnumValue("noSeverity") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticUdsSeverityEnum instantiability and getValue.
        """
        enum = DiagnosticUdsSeverityEnum()
        enum.setValue(DiagnosticUdsSeverityEnum.NO_SEVERITY)

        assert enum.getValue() == "noSeverity"


class TestDiagnosticWwhObdDtcClassEnum:
    """
    Test class for DiagnosticWwhObdDtcClassEnum functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.179, p.188
    """

    def test_initialization(self):
        """
        Test DiagnosticWwhObdDtcClassEnum initialization with the spec literals in displayed order.
        """
        enum = DiagnosticWwhObdDtcClassEnum()

        assert enum is not None
        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            "demDtcWwhObdClassA",
            "demDtcWwhObdClassB1",
            "demDtcWwhObdClassB2",
            "demDtcWwhObdClassC",
            "demDtcWwhObdClassNoInformation",
        ]

    def test_enum_values(self):
        """
        Test DiagnosticWwhObdDtcClassEnum member values.
        """
        enum = DiagnosticWwhObdDtcClassEnum()

        assert DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_A == "demDtcWwhObdClassA"
        assert DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_B1 == "demDtcWwhObdClassB1"
        assert DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_B2 == "demDtcWwhObdClassB2"
        assert DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_C == "demDtcWwhObdClassC"
        assert DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_NO_INFORMATION == "demDtcWwhObdClassNoInformation"

        assert enum.validateEnumValue("demDtcWwhObdClassA") is True
        assert enum.validateEnumValue("demDtcWwhObdClassB1") is True
        assert enum.validateEnumValue("demDtcWwhObdClassB2") is True
        assert enum.validateEnumValue("demDtcWwhObdClassC") is True
        assert enum.validateEnumValue("demDtcWwhObdClassNoInformation") is True
        assert enum.validateEnumValue("invalid") is False

    def test_get_value(self):
        """
        Test DiagnosticWwhObdDtcClassEnum instantiability and getValue.
        """
        enum = DiagnosticWwhObdDtcClassEnum()
        enum.setValue(DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_NO_INFORMATION)

        assert enum.getValue() == "demDtcWwhObdClassNoInformation"
