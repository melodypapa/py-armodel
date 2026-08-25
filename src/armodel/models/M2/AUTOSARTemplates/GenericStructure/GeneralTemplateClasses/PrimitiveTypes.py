"""
This module contains primitive type classes for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
import re
from typing import List, Optional, Sequence, Union, Any
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class ARType(ABC):
    """
    Abstract base class for all AUTOSAR types.
    This class provides the basic structure for all AUTOSAR type definitions.
    """

    # ARType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [x] docstring  [ ] test
    # [ ] setValue                     [x] impl  [x] docstring  [ ] test
    # [x] getText                      [x] impl  [x] docstring  [x] test

    def __init__(self) -> None:
        self.timestamp: Optional[str] = None
        self.uuid: Optional[str] = None
        self._value: Optional[Any] = None

    @property
    def value(self) -> Optional[Any]:
        """Optional[Any]: The current value of this AUTOSAR type."""
        return self._value

    @value.setter
    def value(self, val: Optional[Any]):
        self._value = val

    def getValue(self) -> Optional[Any]:
        """
        Gets the current value of this AUTOSAR type.

        Returns:
            The current value, or None if not set
        """
        return self.value

    def setValue(self, val: Optional[Any]):
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

    # ARNumerical method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [x] _convertStringToNumberValue  [x] impl  [x] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test
    # [ ] __str__                      [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [x] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [x] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [x] docstring  [ ] test

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
            if value == "true":
                return 1
            elif value == "false":
                return 0
            else:
                m = re.match(r"0x([0-9a-f]+)", value, re.I)
                if m:
                    return int(m.group(1), 16)
                m = re.match(r"0b([\d]+)", value, re.I)
                if m:
                    return int(m.group(1), 2)
                m = re.match(r"^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$", value)
                if m:
                    return float(value)
                return int(value)
        except:  # noqa E722
            raise ValueError("Invalid Numerical Type <%s>" % value)

    @property
    def value(self) -> Optional[Union[int, float]]:
        """Optional[Union[int, float]]: The numerical value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[int, str]]):
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

    def setShortLabel(self, val: Optional[str]):
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

    # ARFloat method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test
    # [ ] __str__                      [x] impl  [ ] docstring  [ ] test

    def __init__(self) -> None:
        super().__init__()

        self._text: Optional[str] = None

    @property
    def value(self) -> Optional[float]:
        """Optional[float]: The floating-point value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[float, int, str]]):
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
    """
    An instance of Float is an element from the set of real numbers.
    Tags:
        * xml.xsd.customType=FLOAT
        * xml.xsd.type=double
    """

    # Float method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class TimeValue(ARFloat):
    """
    This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted
    in the physical unit second.
    Tags:
        * xml.xsd.customType=TIME-VALUE
        * xml.xsd.type=double
    """

    # TimeValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class ARLiteral(ARType):
    """
    Base class for literal AUTOSAR types.
    This class provides functionality for literal values in AUTOSAR models.
    """

    # ARLiteral method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test
    # [ ] __str__                      [x] impl  [ ] docstring  [ ] test
    # [ ] upper                        [x] impl  [x] docstring  [ ] test

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> str:
        """str: The literal value."""
        if self._value is None:
            return ""
        return self._value

    @value.setter
    def value(self, val: Any):
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

    # AREnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] getEnumValues                [x] impl  [x] docstring  [ ] test
    # [x] setEnumValues                [x] impl  [x] docstring  [x] test
    # [x] validateEnumValue            [x] impl  [x] docstring  [x] test

    def __init__(self, enum_values: Sequence[str]):
        super().__init__()

        self.enumValues: Sequence[str] = enum_values

    def getEnumValues(self) -> Sequence[str]:
        """
        Gets the list of possible enum values.

        Returns:
            List of possible enum values
        """
        return self.enumValues

    def setEnumValues(self, values: List[str]):
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
        if value in self.enumValues:
            return True
        return False


class String(ARLiteral):
    """
    This represents a String in which white-space shall be normalized before processing. For example: in order to compare two Strings: • leading and trailing white-space needs to be removed • consecutive white-space (blank, cr, lf, tab) needs to be replaced by one blank.

    Tags:
        * xml.xsd.customType=STRING
        * xml.xsd.type=string
    """

    # String method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.63, p.113
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class AlignmentType(ARLiteral):
    """
    This primitive represents the alignment of objects within a memory section.
    The value is in number of bits or UNKNOWN (deprecated), 8, 16, 32, 64,
    UNSPECIFIED, BOOLEAN, or PTR. Typical values for numbers are 8, 16, 32, 64.

    Tags:
        * xml.xsd.customType=ALIGNMENT-TYPE
        * xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]*|0[bB][0-1]+|0[0-7]*|UNSPECIFIED|UNKNOWN|BOOLEAN|PTR
        * xml.xsd.type=string
    """

    # AlignmentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class SectionInitializationPolicyType(ARLiteral):
    """
    SectionInitializationPolicyType describes the intended initialization of MemorySections. The following values are standardized in AUTOSAR Methodology:
    • INIT : To be used for (explicitly or not explicitly) initialized variables.
    • CLEARED : To be used for not explicitly initialized variables.
    • POWER-ON-CLEARED : To be used for variables that are not explicitly initialized (cleared) during normal start-up. Instead these are cleared only after power on reset.
    Please note that the values are defined similar to the representation of enumeration types in the XML schema to ensure backward compatibility.

    Tags
        * xml.xsd.customType=SECTION-INITIALIZATION-POLICY-TYPE
        * xml.xsd.type=NMTOKEN
    """

    # SectionInitializationPolicyType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.93, p.417
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # To be used for (explicitly or not explicitly) initialized variables.
    INIT = "INIT"

    # To be used for not explicitly initialized variables.
    CLEARED = "CLEARED"

    # To be used for variables that are not explicitly initialized (cleared) during normal start-up. Instead these are cleared only after power on reset.
    POWER_ON_CLEARED = "POWER-ON-CLEARED"

    def __init__(self):
        super().__init__()


class CseCodeType(ARLiteral):
    """
    This primitive represents an ASAM CSE (Codes for Scaling Units) based on the
    definition in the ASAM-MCD-2MC-ASAP2 specification. The particular semantics
    is specified in [TPS_GST_00354].

    Tags:
        * xml.xsd.customType=CSE-CODE-TYPE-STRING
        * xml.xsd.type=unsignedInt
    """

    # CseCodeType method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()


class DisplayFormatString(ARLiteral):
    """
    This is a display format specifier for the display of values e.g. in documents or in measurement and calibration systems. The display format specifier is a subset of the ANSI C printf specifiers with the following form: %[flags] [width] [.prec] type character.

    Tags:
        * xml.xsd.customType=DISPLAY-FORMAT-STRING
        * xml.xsd.type=string
    """

    # DisplayFormatString method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.42, p.334
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class NativeDeclarationString(ARLiteral):
    """
    This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved.

    Tags:
        * xml.xsd.customType=NATIVE-DECLARATION-STRING
        * xml.xsd.type=string
        * xml.xsd.whiteSpace=preserve
    """

    # NativeDeclarationString method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.40, p.333
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class BaseTypeEncodingString(ARLiteral):
    """
    This is the string denotion of a BaseType encoding. It may be refined by specific use-cases. Tags: xml.xsd.customType=BASE-TYPE-ENCODING-STRING xml.xsd.type=string

    Tags:
        * xml.xsd.customType=BASE-TYPE-ENCODING-STRING
        * xml.xsd.type=string
    """

    # BaseTypeEncodingString method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.25, p.291
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class PrimitiveIdentifier(ARLiteral):
    """
    This meta-class has the ability to contain a string. Please note that this meta-class has only been introduced to fix an issue with the generation of attributes on primitives in context with [TPS_XMLSPR_00024].

    Tags:
        * xml.xsd.customType=PRIMITIVE-IDENTIFIER
        * xml.xsd.maxLength=128
        * xml.xsd.pattern=[a-zA-Z]([a-zA-Z0-9]|_[a-zA-Z0-9])*_?
        * xml.xsd.type=string
    """

    # PrimitiveIdentifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.58, p.112
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class ReferrableSubtypesEnum(ARLiteral):
    """
    Represents an enum for referrable subtypes in AUTOSAR models.
    """

    # ReferrableSubtypesEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class ARPositiveInteger(ARNumerical):
    """
    Base class for positive integer AUTOSAR types.
    This class provides functionality for positive integer values in AUTOSAR models.
    """

    # ARPositiveInteger method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> Optional[int]:
        """Optional[int]: The positive integer value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Union[int, str]]):
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

    # ARBoolean method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [x] _convertNumberToBoolean      [x] impl  [x] docstring  [x] test
    # [x] _convertStringToBoolean      [x] impl  [x] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [ ] docstring  [ ] test
    # [ ] __str__                      [x] impl  [ ] docstring  [ ] test

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
        if value == 0:
            return False
        return True

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
    def value(self, val: Optional[Union[bool, int, str]]):
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
    """
    This is an identifier as used in xml, e.g. xml-names. Typical usages are, for example, the names of type
    emitters, protocols, or profiles. For details see NMTOKEN definition on the W3C website
    (https://www.w3.org/TR/xml/#NT-Nmtoken).

    Note: Although NameToken supports a wide range of characters, the actually allowed patterns for a
    certain attribute typed by NameToken may be further restricted by the specification of that attribute.

    Tags:
        * xml.xsd.customType=NMTOKEN-STRING
        * xml.xsd.type=NMTOKEN
    """

    # NameToken method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class PositiveInteger(ARPositiveInteger):
    """
    This is a positive integer which can be denoted in decimal, binary, octal and hexadecimal. The value is between 0 and 4294967295.

    Tags:
        * xml.xsd.customType=POSITIVE-INTEGER
        * xml.xsd.pattern=0|[\\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
        * xml.xsd.type=string
    """

    # PositiveInteger method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.64, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class PositiveUnlimitedInteger(ARPositiveInteger):
    r"""
    This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal.

    Tags:
        * xml.xsd.customType=POSITIVE-UNLIMITED-INTEGER
        * xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
        * xml.xsd.type=string
    """

    # PositiveUnlimitedInteger method parity checklist:
    # (no methods)


class Integer(ARNumerical):
    r"""
    An instance of Integer is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
    The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers
    can only be expressed in decimal notation
    Range is from -2147483648 and 2147483647.

    Tags:
        * xml.xsd.customType=INTEGER
        * xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
        * xml.xsd.type=string
    """

    # Integer method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class UnlimitedInteger(Integer):
    r"""
    An instance of UnlimitedInteger is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
    The range is limited by constraint 2534.
    The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers
    can only be expressed in decimal notation.

    Tags:
        * xml.xsd.customType=UNLIMITED-INTEGER
        * xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
        * xml.xsd.type=string
    """

    # UnlimitedInteger method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class Boolean(ARBoolean):
    """
    A Boolean value denotes a logical condition that is either 'true' or 'false'. It can be one of "0", "1", "true",
    "false"

    Tags:
        * xml.xsd.customType=BOOLEAN
        * xml.xsd.pattern=0|1|true|false
        * xml.xsd.type=string
    """

    # Boolean method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class Identifier(ARLiteral):
    """
    An Identifier is a string with a number of constraints on its appearance, satisfying the requirements typical programming languages define for their Identifiers. This datatype represents a string, that can be used as a c-Identifier. It shall start with a letter, may consist of letters, digits and underscores.
    """

    # Identifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.5, p.61
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBlueprintValue   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBlueprintValue   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getNamePattern      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setNamePattern      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint.
        self.blueprintValue: Optional[String] = None

        # This attribute represents a pattern which shall be used to define the value of the identifier if the identifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate.
        self.namePattern: Optional[String] = None

    def getBlueprintValue(self) -> Optional[String]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint.

        Returns:
            The blueprint value, or None if not set
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[String]) -> "Identifier":
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint.

        A None value is a no-op and does not overwrite an existing blueprintValue.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.blueprintValue = value
        return self

    def getNamePattern(self) -> Optional[String]:
        """
        This attribute represents a pattern which shall be used to define the value of the identifier if the identifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate.

        Returns:
            The name pattern, or None if not set
        """
        return self.namePattern

    def setNamePattern(self, value: Optional[String]) -> "Identifier":
        """
        This attribute represents a pattern which shall be used to define the value of the identifier if the identifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate.

        A None value is a no-op and does not overwrite an existing namePattern.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.namePattern = value
        return self


class CIdentifier(ARLiteral):
    """
    This datatype represents a string, that follows the rules of C-identifiers.

    Tags:
        * xml.xsd.customType=C-IDENTIFIER
        * xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*
        * xml.xsd.type=string
    """

    # CIdentifier method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] getBlueprintValue            [x] impl  [x] docstring  [ ] test
    # [ ] setBlueprintValue            [x] impl  [x] docstring  [ ] test
    # [ ] getNamePattern               [x] impl  [x] docstring  [ ] test
    # [ ] setNamePattern               [x] impl  [x] docstring  [ ] test

    def __init__(self):
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

    def setBlueprintValue(self, value: str):
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

    def setNamePattern(self, value: str):
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
    """
    This primitive represents an internal AUTOSAR revision label which identifies an engineering object. It
    represents a pattern which
        * supports three integers representing from left to right MajorVersion, MinorVersion, PatchVersion.
        * may add an application specific suffix separated by one of ".", "_", ";".
    Legal patterns are for example:
        * 4.0.0
        * 4.0.0.1234565
        * 4.0.0_vendor specific;13
        * 4.0.0;12
    """

    # RevisionLabelString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.61, p.113
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — primitive type; value serialized as REVISION-LABEL-STRING via getChildElementOptionalRevisionLabelString / setChildElementOptionalRevisionLabelString
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer


class IntervalTypeEnum(AREnum):
    """
    This enumerator specifies the type of an interval.
    """

    # IntervalTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.88, p.409
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on Limit.intervalType, LimitValueVariationPoint.intervalType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The area is limited by the value given. The value itself is included. Tags: atp.EnumerationLiteralIndex=0
    CLOSED = "closed"

    # The area is limited by the value given. The value itself is not included. Tags: atp.EnumerationLiteralIndex=2
    OPEN = "open"

    def __init__(self):
        super().__init__(
            [
                IntervalTypeEnum.CLOSED,
                IntervalTypeEnum.OPEN,
            ]
        )


class Limit(ARObject):
    """
    This class represents the ability to express a numerical limit. Note that this is in fact a NumericalVariation Point but has the additional attribute intervalType.

    [constr_1191] Value of Limit shall yield a numerical value: After all variability is bound, the content obtained from a limit shall yield a numerical value at the time when the RTE is generated.
    """

    # Limit method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.86, p.408
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIntervalType     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIntervalType     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies the type of the interval. If the attribute is missing the interval shall be considered as "CLOSED".
        self.intervalType: Optional[IntervalTypeEnum] = None

        # This represents the value of the numerical limit.
        self.value: Optional[str] = None

    def getIntervalType(self) -> Optional[IntervalTypeEnum]:
        """
        This specifies the type of the interval. If the attribute is missing the interval shall be considered as "CLOSED".

        Returns:
            The interval type, or None if not set
        """
        return self.intervalType

    def setIntervalType(self, value: Optional[IntervalTypeEnum]) -> "Limit":
        """
        This specifies the type of the interval. If the attribute is missing the interval shall be considered as "CLOSED".

        A None value is a no-op and does not overwrite an existing intervalType.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.intervalType = value
        return self

    def getValue(self) -> Optional[str]:
        """
        This represents the value of the numerical limit.

        Returns:
            The limit value, or None if not set
        """
        return self.value

    def setValue(self, value: Optional[str]) -> "Limit":
        """
        This represents the value of the numerical limit.

        A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class RefType(ARObject):
    """
    Represents a reference type in AUTOSAR models.
    This class defines references with base, destination and value properties.
    """

    # RefType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] getBase                      [x] impl  [x] docstring  [ ] test
    # [ ] setBase                      [x] impl  [x] docstring  [ ] test
    # [ ] getDest                      [x] impl  [x] docstring  [ ] test
    # [ ] setDest                      [x] impl  [x] docstring  [ ] test
    # [ ] getValue                     [x] impl  [x] docstring  [ ] test
    # [ ] setValue                     [x] impl  [x] docstring  [ ] test
    # [x] getShortValue                [x] impl  [x] docstring  [x] test

    def __init__(self):
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

    def setBase(self, value: str):
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

    def setDest(self, value: str):
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

    def setValue(self, value: str):
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
        m = re.match(r"\/[\w\/]+\/(\w+)", self.value)
        if m:
            return m.group(1)
        return self.value


class TRefType(RefType):
    """
    Represents a typed reference type in AUTOSAR models.
    This class extends RefType with additional type-specific functionality.
    """

    # TRefType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class DiagRequirementIdString(ARLiteral):
    r"""
    This string denotes an Identifier for a requirement.

    Tags:
        * xml.xsd.customType=DIAG-REQUIREMENT-ID-STRING
        * xml.xsd.pattern=[0-9a-zA-Z_\-]+                           # noqa W605
        * xml.xsd.type=string
    """

    # DiagRequirementIdString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class ArgumentDirectionEnum(AREnum):
    """
    Use cases: • Arguments in ClientServerOperation can have different directions
    that need to be formally indicated because they have an impact on how the
    function signature looks like eventually. • Arguments in BswModuleEntry
    already determine a function signature, but the direction is used to specify
    the semantics, especially of pointer arguments.
    """

    # ArgumentDirectionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.9, p.104
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The argument value is passed to the callee. Tags: atp.EnumerationLiteralIndex=0
    IN = "in"

    # The argument value is passed to the callee but also passed back from the callee
    # to the caller. Tags: atp.EnumerationLiteralIndex=1
    INOUT = "inout"

    # The argument value is passed from the callee to the caller. Tags: atp.EnumerationLiteralIndex=2
    OUT = "out"

    def __init__(self):
        """
        Initializes an ArgumentDirectionEnum instance with the spec-defined literals.
        """
        super().__init__((ArgumentDirectionEnum.IN, ArgumentDirectionEnum.INOUT, ArgumentDirectionEnum.OUT))


class Ip4AddressString(ARLiteral):
    r"""
    This is used to specify an IP4 address. Notation: 255.255.255.255

    Tags
        * xml.xsd.customType=IP4-ADDRESS-STRING
        * xml.xsd.pattern=(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|ANY        # noqa E501
        * xml.xsd.type=string
    """

    # Ip4AddressString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class Ip6AddressString(ARLiteral):
    r"""
    This is used to specify an IP6 address. Notation: FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
    Alternative notations, short-cuts with duplicate colons like ::, etc. or mixtures using colons and dots, are
    not allowed.

    Tags:
        * xml.xsd.customType=IP6-ADDRESS-STRING
        * xml.xsd.pattern=[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7,7}|ANY
        * xml.xsd.type=string
    """

    # Ip6AddressString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class MacAddressString(ARLiteral):
    """
    This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF
    Alternative notations, e.g. using dash instead of colon, or another grouping of numbers, is not allowed.

    Tags:
        * xml.xsd.customType=MAC-ADDRESS-STRING
        * xml.xsd.pattern=([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
        * xml.xsd.type=string
    """

    # MacAddressString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class CategoryString(ARLiteral):
    """
    This represents the pattern applicable to categories.
    It is basically the same as Identifier but has a different semantics. Therefore it is modeled as a primitive
    of its own.

    Tags:
        * xml.xsd.customType=CATEGORY-STRING
        * xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]*
        * xml.xsd.type=string
    """

    # CategoryString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class AnyServiceInstanceId(ARLiteral):
    r"""
    This is a positive integer or the literal ALL (the value ANY is technically supported but deprecated) which can be denoted in decimal, octal and hexadecimal. The value is between 0 and 65535.

    Tags:
        * xml.xsd.customType=ANY-SERVICE-INSTANCE-ID
        * xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[0-7]*|0[bB][0-1]+|ANY|ALL
        * xml.xsd.type=string
    """

    # AnyServiceInstanceId method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.6, p.423
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class AnyVersionString(ARLiteral):
    r"""
    Tags:
        * xml.xsd.customType=ANY-VERSION-STRING
        * xml.xsd.pattern=[0-9]+|ANY
        * xml.xsd.type=string
    """

    # AnyVersionString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.7, p.423
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class ByteOrderEnum(AREnum):
    """
    When more than one byte is stored in the memory the order of those bytes may differ depending on the architecture of the processing unit. If the least significant byte is stored at the lowest address, this architecture is called little endian and otherwise it is called big endian. ByteOrder is very important in case of communication between different PUs or ECUs.
    """

    # ByteOrderEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.27, p.297
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Most significant byte shall come at the lowest address (also known as BigEndian or as Motorola-Format) Tags: atp.EnumerationLiteralIndex=0
    MOST_SIGNIFICANT_BYTE_FIRST = "mostSignificantByteFirst"

    # Most significant byte shall come highest address (also known as LittleEndian or as Intel-Format) Tags: atp.EnumerationLiteralIndex=1
    MOST_SIGNIFICANT_BYTE_LAST = "mostSignificantByteLast"

    # For opaque data endianness conversion has to be configured to Opaque. See AUTOSAR COM Specification for more details. Tags: atp.EnumerationLiteralIndex=2
    OPAQUE = "opaque"

    def __init__(self):
        super().__init__(
            [
                ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST,
                ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST,
                ByteOrderEnum.OPAQUE,
            ]
        )


class MonotonyEnum(AREnum):
    """
    This enumerator denotes the values for specification of monotony for e.g. curves.
    """

    # MonotonyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.87, p.408
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on InternalConstrs.monotony, PhysConstrs.monotony, SwCalprmAxisTypeProps.monotony
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This indicates that the related curve needs to be monotony decreasing. Tags: atp.EnumerationLiteralIndex=0
    DECREASING = "decreasing"

    # This indicates that the related curve needs to be monotony increasing. Tags: atp.EnumerationLiteralIndex=1
    INCREASING = "increasing"

    # This indicates that the values shall be monotonously decreasing or increasing, depending on the trend set by the first values of the series. Tags: atp.EnumerationLiteralIndex=2
    MONOTONOUS = "monotonous"

    # This indicates that the related curve needs not to be monotony. Tags: atp.EnumerationLiteralIndex=3
    NO_MONOTONY = "noMonotony"

    # This indicates that the related curve needs to be strictly monotony decreasing. Tags: atp.EnumerationLiteralIndex=4
    STRICTLY_DECREASING = "strictlyDecreasing"

    # This indicates that the related curve needs to be strictly monotony increasing. Tags: atp.EnumerationLiteralIndex=5
    STRICTLY_INCREASING = "strictlyIncreasing"

    # This indicates that the values shall be strict monotonously decreasing or increasing, depending on the trend set by the first values of the series. Tags: atp.EnumerationLiteralIndex=6
    STRICT_MONOTONOUS = "strictMonotonous"

    def __init__(self):
        super().__init__(
            [
                MonotonyEnum.DECREASING,
                MonotonyEnum.INCREASING,
                MonotonyEnum.MONOTONOUS,
                MonotonyEnum.NO_MONOTONY,
                MonotonyEnum.STRICTLY_DECREASING,
                MonotonyEnum.STRICTLY_INCREASING,
                MonotonyEnum.STRICT_MONOTONOUS,
            ]
        )


class DateTime(ARLiteral):
    r"""
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
    """

    # DateTime method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class VerbatimString(ARLiteral):
    """
    This primitive represents a string in which white-space needs to be preserved.

    Tags: xml.xsd.customType=VERBATIM-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.66, p.115

    Attributes (per Table 4.67):
    - blueprintValue (String, 0..1, attr): Not implemented (atp.Status=draft)
    - xmlSpace (XmlSpaceEnum, 0..1, attr): Not implemented (missing enum type)
    """

    # VerbatimString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.66–4.67, p.115
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # Spec verified: R23-11

    def __init__(self):
        super().__init__()


class VerbatimStringPlain(ARLiteral):
    """
    This primitive represents a string in which white-space needs to be preserved.
    This primitive is applied in cases where xml:space attribute cannot be provided by
    the primitive type but needs to be provided by the container class. This is in
    particular the case in applications of [TPS_XMLSPR_00024].
    """

    # VerbatimStringPlain method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.68, p.115
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class RegularExpression(ARLiteral):
    """
    Represents a regular expression in AUTOSAR models.
    This class is used for storing and handling regular expression patterns.
    """

    # RegularExpression method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class SymbolString(ARLiteral):
    """
    This meta-class has the ability to contain a string plus an additional namePattern. Please note that this meta-class has only been introduced to fix an issue with the backwards compatibility between R4.0.3 and R4.1.1 in the context of McDataInstance.

    Tags:
        * xml.xsd.customType=SYMBOL-STRING
        * xml.xsd.type=string
    """

    # SymbolString method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class McdIdentifier(ARLiteral):
    """
    This primitive denotes a name used for measurement and calibration systems and shall follow the restrictions for an ASAM ASAP2 ident. For detailed syntax see the xsd.pattern. The size limitations are not captured.

    McdIdentifiers are random names which may contain characters A through Z, a through z, underscore (_), numerals 0 through 9, points ('.') and brackets ( '[',']' ).
    However, the following limitations apply: the first character must be a letter or an underscore, brackets must occur in pairs at the end of a partial string and must contain a number or an alpha-numerical string (description of the index of an array element).

    Tags:
        * xml.xsd.customType=MCD-IDENTIFIER
        * xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*(\\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\\])*(\\.[a-zA-Z_][a-zA-Z0-9_]*(\\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\\])*)*
        * xml.xsd.type=string
    """

    # McdIdentifier method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class Numerical(ARLiteral):
    """
    This primitive specifies a numerical value. It can be denoted in different formats such as Decimal, Octal, Hexadecimal, Float. See the xsd pattern for details. The value can be expressed in octal, hexadecimal, binary representation. Negative numbers can only be expressed in decimal or float notation.

    Tags:
        * xml.xsd.customType=NUMERICAL-VALUE
        * xml.xsd.pattern=(0[xX][0-9a-fA-F]+)|(0[0-7]+)|(0[bB][0-1]+)|(([+\\-]?[1-9][0-9]+(\\.[0-9]+)?|[+\\-]?[0-9](\\.[0-9]+)?)([eE]([+\\-]?)[0-9]+)?)|\\.0|INF|-INF|NaN
        * xml.xsd.type=string
    """

    # Numerical method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.58, p.457
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()
