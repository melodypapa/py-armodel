"""
This module contains primitive type classes for AUTOSAR models
in the GenericStructure module.

V2 Implementation:
- Absolute imports only
- String annotations for forward references
- TYPE_CHECKING used for circular imports (deviates from CODING_RULE_V2_00002 due to circular dependencies)

Compatible with V1 API.
"""

import re
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    List,
    Optional,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ARType(ABC):
    """
    Abstract base class for all AUTOSAR types.
    This class provides the basic structure for all AUTOSAR type definitions.
    """

    @abstractmethod
    def __init__(self) -> None:
        self.timestamp: Optional[str] = None
        self.uuid: Optional[str] = None
        self._value: Optional[Any] = None

    @property
    def value(self) -> Optional[Any]:
        """Optional[Any]: The current value of this AUTOSAR type."""
        return self._value

    @value.setter
    def value(self, val: Optional[Any]) -> None:
        self._value = val

    def getValue(self) -> Optional[Any]:
        """
        Gets the current value of this AUTOSAR type.

        Returns:
            The current value, or None if not set
        """
        return self.value

    def setValue(self, val: Optional[Any]) -> "ARType":
        """
        Sets the value of this AUTOSAR type.
        Only sets the value if it is not None.

        Args:
            val: The value to set

        Returns:
            self for method chaining
        """
        if val is not None:
            self.value = val
        return self

    def getText(self) -> str:
        """
        Gets the text representation of this type.

        Returns:
            String representation of this type
        """
        return str(self)


class ARNumerical(ARType):
    """
    Base class for numerical AUTOSAR types.
    This class provides functionality for numerical values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()

        self.shortLabel: Optional[str] = None
        self._text: Optional[str] = None

    def _convertStringToNumberValue(self, value: str) -> Union[int, float]:
        """
        Converts a string value to a numerical value.

        Args:
            value: The string value to convert

        Returns:
            The converted numerical value

        Raises:
            ValueError: If the value cannot be converted to a numerical type
        """
        try:
            if value == 'true':
                return 1
            elif value == 'false':
                return 0
            else:
                m = re.match(r"0x([0-9a-f]+)", value, re.I)
                if m:
                    return int(m.group(1), 16)
                m = re.match(r'0b([\d]+)', value, re.I)
                if m:
                    return int(m.group(1), 2)
                m = re.match(r"^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$", value)
                if m:
                    return float(value)
                return int(value)
        except Exception as e:  # noqa E722
            raise ValueError("Invalid Numerical Type <%s>" % value) from e

    @property
    def value(self) -> Optional[Union[int, float]]:
        """Optional[Union[int, float]]: The numerical value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[int, float, str]]) -> None:
        if isinstance(val, int):
            self._value = val
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

    def __str__(self) -> str:
        if self._text is not None:
            return self._text
        else:
            return str(self._value)

    def getValue(self) -> Optional[Union[int, float]]:
        """
        Gets the numerical value of this type.

        Returns:
            The numerical value, or None if not set
        """
        return self.value

    def setShortLabel(self, val: Optional[str]) -> "ARNumerical":
        """
        Sets the short label for this numerical type.
        Only sets the value if it is not None.

        Args:
            val: The short label to set

        Returns:
            self for method chaining
        """
        if val is not None:
            self.shortLabel = val
        return self

    def getShortLabel(self) -> Optional[str]:
        """
        Gets the short label of this numerical type.

        Returns:
            The short label, or None if not set
        """
        return self.shortLabel


class ARFloat(ARNumerical):
    """
    Base class for floating-point AUTOSAR types.
    This class provides functionality for floating-point values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()

        self._text: Optional[str] = None

    @property
    def value(self) -> Optional[float]:
        """Optional[float]: The floating-point value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[float, int, str]]) -> None:
        if isinstance(val, float):
            self._value = val
        elif isinstance(val, int):
            self._value = val * 1.0
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

    def __str__(self) -> str:
        if self._text is not None:
            return self._text
        else:
            return str(self._value)


class Float(ARFloat):
    '''
        An instance of Float is an element from the set of real numbers.
        Tags:
            * xml.xsd.customType=FLOAT
            * xml.xsd.type=double
    '''
    def __init__(self) -> None:
        super().__init__()


class TimeValue(ARFloat):
    '''
        This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted
        in the physical unit second.
        Tags:
            * xml.xsd.customType=TIME-VALUE
            * xml.xsd.type=double
    '''

    def __init__(self) -> None:
        super().__init__()


class ARLiteral(ARType):
    """
    Base class for literal AUTOSAR types.
    This class provides functionality for literal values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> str:
        """str: The literal value."""
        if self._value is None:
            return ""
        return str(self._value)

    @value.setter
    def value(self, val: Any) -> None:
        if isinstance(val, str):
            self._value = val
        else:
            self._value = str(val)

    def __str__(self) -> str:
        return self.value

    def upper(self) -> str:
        """
        Gets the uppercase representation of this literal.

        Returns:
            Uppercase string representation
        """
        return self.value.upper()


class AREnum(ARLiteral):
    """
    Base class for enumeration AUTOSAR types.
    This class provides functionality for enumeration values in AUTOSAR models.
    """

    def __init__(self, enum_values: List[str]) -> None:
        super().__init__()

        self.enumValues: List[str] = enum_values

    def getEnumValues(self) -> List[str]:
        """
        Gets the list of possible enum values.

        Returns:
            List of possible enum values
        """
        return self.enumValues

    def setEnumValues(self, values: List[str]) -> "AREnum":
        """
        Sets the list of possible enum values.

        Args:
            values: The list of possible enum values to set

        Returns:
            self for method chaining
        """
        self.enumValues = values
        return self

    def validateEnumValue(self, value: str) -> bool:
        """
        Validates if the provided value is one of the allowed enum values.

        Args:
            value: The value to validate

        Returns:
            True if the value is valid, False otherwise
        """
        return value in self.enumValues


class String(ARLiteral):
    """
    Represents a string AUTOSAR type.
    This class provides functionality for string values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()


class DisplayFormatString(ARLiteral):
    """
    Represents a display format string AUTOSAR type.
    This class provides functionality for display format string values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()


class MonotonyEnum(AREnum):
    """
    Represents a monotony enum in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__([
            MonotonyEnum.INCREASE,
            MonotonyEnum.DECREASE,
            MonotonyEnum.STRICT_INCREASE,
            MonotonyEnum.STRICT_DECREASE,
            MonotonyEnum.MONOTONOUS,
            MonotonyEnum.NOT_MONOTONOUS,
        ])

    INCREASE = 'INCREASE'
    DECREASE = 'DECREASE'
    STRICT_INCREASE = 'STRICT_INCREASE'
    STRICT_DECREASE = 'STRICT_DECREASE'
    MONOTONOUS = 'MONOTONOUS'
    NOT_MONOTONOUS = 'NOT_MONOTONOUS'


class ReferrableSubtypesEnum(ARLiteral):
    """
    Represents an enum for referrable subtypes in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()


class ARPositiveInteger(ARNumerical):
    """
    Base class for positive integer AUTOSAR types.
    This class provides functionality for positive integer values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> Optional[int]:
        """Optional[int]: The positive integer value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[int, float, str]]) -> None:
        if isinstance(val, int):
            if val < 0:
                raise ValueError("Invalid Positive Integer <%s>" % val)
            self._value = val
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))


class ARBoolean(ARType):
    """
    Base class for boolean AUTOSAR types.
    This class provides functionality for boolean values in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__()

        self._text: Optional[str] = None

    def _convertNumberToBoolean(self, value: int) -> bool:
        """
        Converts a numerical value to a boolean value.

        Args:
            value: The numerical value to convert

        Returns:
            Boolean representation of the value
        """
        return value != 0

    def _convertStringToBoolean(self, value: str) -> bool:
        """
        Converts a string value to a boolean value.

        Args:
            value: The string value to convert

        Returns:
            Boolean representation of the value
        """
        value = value.lower()
        if value == "true" or value == "1":
            return True
        elif value == "false" or value == "0":
            return False
        else:
            return self._convertNumberToBoolean(int(value))

    @property
    def value(self) -> Optional[bool]:
        """Optional[bool]: The boolean value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[bool, int, str]]) -> None:
        if isinstance(val, bool):
            self._value = val
        elif isinstance(val, int):
            self._value = self._convertNumberToBoolean(val)
            self._text = str(val)
        elif isinstance(val, str):
            self._value = self._convertStringToBoolean(val.strip())
            self._text = val.strip()
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

    def __str__(self) -> str:
        if self._text is not None:
            return self._text
        else:
            if self._value:
                return "true"
            else:
                return "false"


class NameToken(ARLiteral):
    '''
        This is an identifier as used in xml, e.g. xml-names. Typical usages are, for example, the names of type
        emitters, protocols, or profiles. For details see NMTOKEN definition on the W3C website
        (https://www.w3.org/TR/xml/#NT-Nmtoken).

        Note: Although NameToken supports a wide range of characters, the actually allowed patterns for a
        certain attribute typed by NameToken may be further restricted by the specification of that attribute.

        Tags:
            * xml.xsd.customType=NMTOKEN-STRING
            * xml.xsd.type=NMTOKEN
    '''
    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, other: object) -> bool:
        """
        Compare NameToken with other objects.

        Args:
            other: The object to compare with

        Returns:
            True if the other object is a NameToken with the same value or a string matching the value
        """
        if isinstance(other, NameToken):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        return False


class PositiveInteger(ARPositiveInteger):
    r'''\n
        This is a positive integer which can be denoted in decimal, binary, octal and hexadecimal. The value is
        between 0 and 4294967295.

        Tags:
            * xml.xsd.customType=POSITIVE-INTEGER
            * xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
            * xml.xsd.type=string
        \n
    '''
    def __init__(self) -> None:
        super().__init__()


class PositiveUnlimitedInteger(ARPositiveInteger):
    r'''
        This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal.

        Tags:
            * xml.xsd.customType=POSITIVE-UNLIMITED-INTEGER
            * xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
            * xml.xsd.type=string
    '''


class Integer(ARNumerical):
    r'''
        An instance of Integer is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
        The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers
        can only be expressed in decimal notation
        Range is from -2147483648 and 2147483647.

        Tags:
            * xml.xsd.customType=INTEGER
            * xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class UnlimitedInteger(Integer):
    r'''
        An instance of UnlimitedInteger is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
        The range is limited by constraint 2534.
        The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers
        can only be expressed in decimal notation.

        Tags:
            * xml.xsd.customType=UNLIMITED-INTEGER
            * xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class Boolean(ARBoolean):
    '''
        A Boolean value denotes a logical condition that is either 'true' or 'false'. It can be one of "0", "1", "true",
        "false"

        Tags:
            * xml.xsd.customType=BOOLEAN
            * xml.xsd.pattern=0|1|true|false
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class Identifier(ARLiteral):
    '''
        An Identifier is a string with a number of constraints on its appearance, satisfying the requirements typical
        programming languages define for their Identifiers.
        This datatype represents a string, that can be used as a c-Identifier.
        It shall start with a letter, may consist of letters, digits and underscores.

        Tags:
            * xml.xsd.customType=IDENTIFIER
            * xml.xsd.maxLength=128
            * xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]*
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, other: object) -> bool:
        """
        Compare Identifier with other objects.

        Args:
            other: The object to compare with

        Returns:
            True if the other object is an Identifier with the same value or a string matching the value
        """
        if isinstance(other, Identifier):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        return False


class CIdentifier(ARLiteral):
    '''
        This datatype represents a string, that follows the rules of C-identifiers.

        Tags:
            * xml.xsd.customType=C-IDENTIFIER
            * xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()

        self.blueprintValue: Optional[str] = None
        self.namePattern: Optional[str] = None

    def getBlueprintValue(self) -> Optional[str]:
        """
        Gets the blueprint value of this C identifier.

        Returns:
            The blueprint value, or None if not set
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: str) -> "CIdentifier":
        """
        Sets the blueprint value of this C identifier.

        Args:
            value: The blueprint value to set

        Returns:
            self for method chaining
        """
        self.blueprintValue = value
        return self

    def getNamePattern(self) -> Optional[str]:
        """
        Gets the name pattern of this C identifier.

        Returns:
            The name pattern, or None if not set
        """
        return self.namePattern

    def setNamePattern(self, value: str) -> "CIdentifier":
        """
        Sets the name pattern of this C identifier.

        Args:
            value: The name pattern to set

        Returns:
            self for method chaining
        """
        self.namePattern = value
        return self


class RevisionLabelString(ARLiteral):
    '''
        This primitive represents an internal AUTOSAR revision label which identifies an engineering object. It
        represents a pattern which
            * supports three integers representing from left to right MajorVersion, MinorVersion, PatchVersion.
            * may add an application specific suffix separated by one of ".", "_", ";".
        Legal patterns are for example:
            * 4.0.0
            * 4.0.0.1234565
            * 4.0.0_vendor specific;13
            * 4.0.0;12
    '''


class Limit(ARObject):
    """
    Represents a limit in AUTOSAR models.
    This class defines limits with interval type and value.
    """

    def __init__(self) -> None:
        super().__init__()

        self.intervalType: Optional[str] = None
        self.value: Optional[str] = None

    def getIntervalType(self) -> Optional[str]:
        """
        Gets the interval type of this limit.

        Returns:
            The interval type, or None if not set
        """
        return self.intervalType

    def setIntervalType(self, value: str) -> "Limit":
        """
        Sets the interval type of this limit.

        Args:
            value: The interval type to set

        Returns:
            self for method chaining
        """
        self.intervalType = value
        return self

    def getValue(self) -> Optional[str]:
        """
        Gets the value of this limit.

        Returns:
            The limit value, or None if not set
        """
        return self.value

    def setValue(self, value: str) -> "Limit":
        """
        Sets the value of this limit.

        Args:
            value: The limit value to set

        Returns:
            self for method chaining
        """
        self.value = value
        return self


class RefType(ARObject):
    """
    Represents a reference type in AUTOSAR models.
    This class defines references with base, destination and value properties.
    """

    def __init__(self) -> None:
        super().__init__()

        self.base: Optional[str] = None
        self.dest: Optional[str] = None
        self.value: Optional[str] = None

    def getBase(self) -> Optional[str]:
        """
        Gets the base of this reference type.

        Returns:
            The base string, or None if not set
        """
        return self.base

    def setBase(self, value: str) -> "RefType":
        """
        Sets the base of this reference type.

        Args:
            value: The base to set

        Returns:
            self for method chaining
        """
        self.base = value
        return self

    def getDest(self) -> Optional[str]:
        """
        Gets the destination of this reference type.

        Returns:
            The destination string, or None if not set
        """
        return self.dest

    def setDest(self, value: str) -> "RefType":
        """
        Sets the destination of this reference type.

        Args:
            value: The destination to set

        Returns:
            self for method chaining
        """
        self.dest = value
        return self

    def getValue(self) -> Optional[str]:
        """
        Gets the value of this reference type.

        Returns:
            The reference value, or None if not set
        """
        return self.value

    def setValue(self, value: str) -> "RefType":
        """
        Sets the value of this reference type.

        Args:
            value: The reference value to set

        Returns:
            self for method chaining
        """
        self.value = value
        return self

    def getShortValue(self) -> str:
        """
        Gets the short value of this reference type.

        Returns:
            The short value as a string

        Raises:
            ValueError: If the value is None
        """
        if self.value is None:
            raise ValueError("Invalid value of RefType")
        m = re.match(r'\/[\w\/]+\/(\w+)', self.value)
        if m:
            return m.group(1)
        return self.value


class TRefType(RefType):
    """
    Represents a typed reference type in AUTOSAR models.
    This class extends RefType with additional type-specific functionality.
    """

    def __init__(self) -> None:
        super().__init__()


class DiagRequirementIdString(ARLiteral):
    r'''
        This string denotes an Identifier for a requirement.

        Tags:
            * xml.xsd.customType=DIAG-REQUIREMENT-ID-STRING
            * xml.xsd.pattern=[0-9a-zA-Z_\-]+                           # noqa W605
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class ArgumentDirectionEnum(AREnum):
    """
    Enumeration for argument direction in AUTOSAR models.
    Defines the direction of arguments in function interfaces.
    """
    IN = "in"
    INOUT = "inout"
    OUT = "out"

    def __init__(self) -> None:
        super().__init__([
            ArgumentDirectionEnum.IN,
            ArgumentDirectionEnum.INOUT,
            ArgumentDirectionEnum.OUT
        ])


class Ip4AddressString(ARLiteral):
    r'''
        This is used to specify an IP4 address. Notation: 255.255.255.255

        Tags
            * xml.xsd.customType=IP4-ADDRESS-STRING
            * xml.xsd.pattern=(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|ANY        # noqa E501
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class Ip6AddressString(ARLiteral):
    r'''
        This is used to specify an IP6 address. Notation: FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
        Alternative notations, short-cuts with duplicate colons like ::, etc. or mixtures using colons and dots, are
        not allowed.

        Tags:
            * xml.xsd.customType=IP6-ADDRESS-STRING
            * xml.xsd.pattern=[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7,7}|ANY
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class MacAddressString(ARLiteral):
    '''
        This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF
        Alternative notations, e.g. using dash instead of colon, or another grouping of numbers, is not allowed.

        Tags:
            * xml.xsd.customType=MAC-ADDRESS-STRING
            * xml.xsd.pattern=([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
            * xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class CategoryString(ARLiteral):
    '''
        This represents the pattern applicable to categories.
        It is basically the same as Identifier but has a different semantics. Therefore it is modeled as a primitive
        of its own.

        Tags:
            * xml.xsd.customType=CATEGORY-STRING
            * xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]*
            * xml.xsd.type=string
        '''
    def __init__(self) -> None:
        super().__init__()


class ByteOrderEnum(AREnum):
    """
    Enumeration for byte order in AUTOSAR models.
    """

    def __init__(self) -> None:
        super().__init__([])


class DateTime(ARLiteral):
    r'''
        A datatype representing a timestamp. The smallest granularity is 1 second.
        This datatype represents a timestamp in the format yyyy-mm-dd followed by an optional time. The lead-in
        character for the time is "T" and the format is hh:mm:ss. In addition, a time zone designator shall be
        specified. The time zone designator can either be "Z" (for UTC) or the time offset to UTC, i.e. (+|-)hh:mm.

        Examples:
            2009-07-23
            2009-07-23T14:38:00+01:00
            2009-07-23T13:38:00Z
        Tags:
            xml.xsd.customType=DATE
            xml.xsd.pattern=([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?
            xml.xsd.type=string
    '''
    def __init__(self) -> None:
        super().__init__()


class VerbatimString(ARLiteral):
    """
    Represents a verbatim string in AUTOSAR models.
    This class is used for strings that should be preserved exactly as written.
    """

    def __init__(self) -> None:
        super().__init__()


class RegularExpression(ARLiteral):
    """
    Represents a regular expression in AUTOSAR models.
    This class is used for storing and handling regular expression patterns.
    """

    def __init__(self) -> None:
        super().__init__()

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value(self, value):
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
