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
        self._value: Optional[Any] = None
        self.shortLabel: Optional[str] = None

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

    def setShortLabel(self, val: Optional[str]):
        """
        Sets the short label for this type.
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
        Gets the short label of this type.

        Returns:
            The short label, or None if not set
        """
        return self.shortLabel


class ARLiteral(ARType):
    """
    Base class for literal AUTOSAR types.
    This class provides functionality for literal values in AUTOSAR models.
    """

    # ARLiteral method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] __str__                      [x] impl  [x] docstring  [ ] test
    # [ ] upper                        [x] impl  [x] docstring  [ ] test

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> Any:
        """Any: The literal value (str for ARLiteral, numeric for subclasses such as Numerical)."""
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
    # (ARNumerical merged into Numerical (2026-09-27): _convertStringToNumberValue/value/__str__
    #  moved here from the removed ARNumerical class; base of Float, PositiveInteger, Integer)

    def __init__(self) -> None:
        super().__init__()

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
    def value(self, val: Optional[Any]):
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


class Float(Numerical):
    """
    An instance of Float is an element from the set of real numbers.

    Tags:
        * xml.xsd.customType=FLOAT
        * xml.xsd.type=double
    """

    # Float method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
    # [ ] __str__                      [x] impl  [ ] docstring  [ ] test
    # (_text/_convertStringToNumberValue/__str__ inherited from Numerical)

    @property
    def value(self) -> Optional[float]:
        """Optional[float]: The floating-point value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Any]):
        if isinstance(val, float):
            self._value = val
        elif isinstance(val, int):
            self._value = val * 1.0
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))


class TimeValue(Float):
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


class UriString(ARLiteral):
    """
    A Uniform Resource Identifier (URI), is a compact string of characters used to identify or name a resource.

    Tags:
        * xml.xsd.customType=URI-STRING
        * xml.xsd.type=string
    """

    # UriString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.66, p.114
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class AlignmentType(ARLiteral):
    """
    This primitive represents the alignment of objects within a memory section. The value is in number of bits or UNKNOWN (deprecated), 8 , 16, 32, 64 UNSPECIFIED, BOOLEAN, or PTR. Typical values for numbers are 8, 16, 32, 64.

    Tags:
        * xml.xsd.customType=ALIGNMENT-TYPE
        * xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]*|0[bB] [0-1]+|0[0-7]*|UNSPECIFIED|UNKNOWN|BOOLEAN|PTR
        * xml.xsd.type=string
    """

    # AlignmentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.3, p.144
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.75, p.165
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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
        * xml.xsd.pattern= ``[a-zA-Z][a-zA-Z0-9]([a-zA-Z0-9]|_[a-zA-Z0-9])*_?``
        * xml.xsd.type=string
    """

    # PrimitiveIdentifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.58, p.112
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class ReferrableSubtypesEnum(ARLiteral):
    """
    This primitive is a proxy for an enum generated by the MMT. It allows to refer to any subclass of Referrable. Due to technical reasons the possible values are not shown in this class table.

    Tags:
        * xml.mds.type=REFERRABLE-SUBTYPES-ENUM
        * xml.xsd.type=string
    """

    # ReferrableSubtypesEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.15, p.73
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class PositiveInteger(Numerical):
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
    # [ ] value                        [x] impl  [x] docstring  [ ] test  [—] reader  [—] writer
    # (_text/_convertStringToNumberValue/__str__ inherited from Numerical)

    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> Optional[int]:
        """Optional[int]: The positive integer value."""
        return self._value

    @value.setter
    def value(self, val: Optional[Any]):
        if isinstance(val, int):
            if val < 0:
                raise ValueError("Invalid Positive Integer <%s>" % val)
            self._value = val
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))


class Boolean(ARType):
    """
    A Boolean value denotes a logical condition that is either 'true' or 'false'. It can be one of "0", "1", "true",
    "false"

    Tags:
        * xml.xsd.customType=BOOLEAN
        * xml.xsd.pattern=0|1|true|false
        * xml.xsd.type=string
    """

    # Boolean method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] _convertNumberToBoolean      [x] impl  [x] docstring  [x] test
    # [x] _convertStringToBoolean      [x] impl  [x] docstring  [x] test
    # [ ] value                        [x] impl  [x] docstring  [ ] test
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


class PositiveUnlimitedInteger(PositiveInteger):
    r"""
    This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal.

    Tags:
        * xml.xsd.customType=POSITIVE-UNLIMITED-INTEGER
        * xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
        * xml.xsd.type=string
    """

    # PositiveUnlimitedInteger method parity checklist:
    # (no methods)


class Integer(Numerical):
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
    # (_text/_convertStringToNumberValue/value/__str__ inherited from Numerical)

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
    * xml.xsd.pattern= ``[a-zA-Z_][a-zA-Z0-9_]*``
    * xml.xsd.type=string
    """

    # CIdentifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.45, p.108
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintValue        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBlueprintValue        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNamePattern           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setNamePattern           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    represents a pattern which:

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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11


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


class Ref(ARLiteral):
    """
    This primitive denotes a name based reference. For detailed syntax see the xsd.pattern. • first slash (relative or absolute reference) [optional] • Identifier [required] • a sequence of slashes and Identifiers [optional] This primitive is used by the meta-model tools to create the references.

    Tags:
        * xml.xsd.customType=REF
        * xml.xsd.pattern=/?[a-zA-Z][a-zA-Z0-9_]{0,127}(/[a-zA-Z][a-zA-Z0-9_]{0,127})*
        * xml.xsd.type=string
    """

    # Ref method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.35, p.318
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBase            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBase            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintValue  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBlueprintValue  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIndex           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setIndex           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # value (the reference path) rides ARLiteral/ARType — no spec row (primitive content);
    # base/blueprintValue/index serialize on AR:REF element content only (XSD attributeGroup REF, AUTOSAR_00052.xsd L96322);
    # the sole src consumer of this class is AbstractEnumerationValueVariationPoint.enumTableRef, typed AR:REF--SIMPLE
    # (value-only, AUTOSAR_00052.xsd L96364) → no reader/writer carrier exists yet.

    def __init__(self):
        super().__init__()

        # This attribute reflects the base to be used for this reference. Tags: xml.attribute=true
        self.base: Optional[Identifier] = None

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        self.blueprintValue: Optional[String] = None

        # This attribute supports the use case to point on specific elements in an array. This is in particular required if arrays are used to implement particular data objects. The counting of array indices starts with the value 0, i.e. the index of the first array element is 0. Tags: xml.attribute=true
        self.index: Optional[PositiveInteger] = None

    def getBase(self) -> Optional[Identifier]:
        """This attribute reflects the base to be used for this reference."""
        return self.base

    def setBase(self, value: Optional[Identifier]) -> "Ref":
        """This attribute reflects the base to be used for this reference. A None value is a no-op and does not overwrite an existing base."""
        if value is not None:
            self.base = value
        return self

    def getBlueprintValue(self) -> Optional[String]:
        """This represents a description that documents how the value shall be defined when deriving objects from the blueprint."""
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[String]) -> "Ref":
        """This represents a description that documents how the value shall be defined when deriving objects from the blueprint. A None value is a no-op and does not overwrite an existing blueprintValue."""
        if value is not None:
            self.blueprintValue = value
        return self

    def getIndex(self) -> Optional[PositiveInteger]:
        """This attribute supports the use case to point on specific elements in an array. This is in particular required if arrays are used to implement particular data objects. The counting of array indices starts with the value 0, i.e. the index of the first array element is 0."""
        return self.index

    def setIndex(self, value: Optional[PositiveInteger]) -> "Ref":
        """This attribute supports the use case to point on specific elements in an array. This is in particular required if arrays are used to implement particular data objects. The counting of array indices starts with the value 0, i.e. the index of the first array element is 0. A None value is a no-op and does not overwrite an existing index."""
        if value is not None:
            self.index = value
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
    * xml.xsd.pattern= ``[0-9a-zA-Z_\-]+``                       # noqa W605
    * xml.xsd.type=string
    """

    # DiagRequirementIdString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.49, p.109
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class ArgumentDirectionEnum(AREnum):
    """
    Use cases: • Arguments in ClientServerOperation can have different directions that need to be formally indicated because they have an impact on how the function signature looks like eventually. • Arguments in BswModuleEntry already determine a function signature, but the direction is used to specify the semantics, especially of pointer arguments.
    """

    # ArgumentDirectionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.9, p.104
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # The argument value is passed to the callee. Tags: atp.EnumerationLiteralIndex=0
    IN = "in"

    # The argument value is passed to the callee but also passed back from the callee to the caller. Tags: atp.EnumerationLiteralIndex=1
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

    Tags:
        * xml.xsd.customType=IP4-ADDRESS-STRING
        * xml.xsd.pattern=(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|ANY        # noqa E501
        * xml.xsd.type=string
    """

    # Ip4AddressString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.51, p.110
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.52, p.110
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class MacAddressString(ARLiteral):
    """
    This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF Alternative notations, e.g. using dash instead of colon, or another grouping of numbers, is not allowed.

    Tags:
        * xml.xsd.customType=MAC-ADDRESS-STRING
        * xml.xsd.pattern=([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
        * xml.xsd.type=string
    """

    # MacAddressString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.53, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class CategoryString(ARLiteral):
    """
    This represents the pattern applicable to categories.
    It is basically the same as Identifier but has a different semantics. Therefore it is modeled as a primitive
    of its own.

    Tags:
        * xml.xsd.customType=CATEGORY-STRING
        * xml.xsd.pattern= ``[a-zA-Z][a-zA-Z0-9_]*``
        * xml.xsd.type=string
    """

    # CategoryString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.47, p.109
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Spec verified: R23-11
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
    # Spec verified: R23-11
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

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
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.48, p.109
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class VerbatimString(ARLiteral):
    """
    This primitive represents a string in which white-space needs to be preserved.

    Tags: xml.xsd.customType=VERBATIM-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve

    Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.66, p.115

    Attributes (per Table 4.67):
    - blueprintValue (String, 0..1, attr): Not implemented (atp.Status=draft)
    - xmlSpace (XmlSpaceEnum, 0..1, attr): Not implemented (deferred to the VerbatimString sync row — XmlSpaceEnum exists since the 2026-09-24 Sd sync; wiring spans the ad-hoc VT/VALUE writer sites)
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class RegularExpression(ARLiteral):
    """
    This is a regular expression as defined in http://www.w3.org/TR/xmlschema-2 As of now it is still produced as a string in XSD.

    Tags:
        * xml.xsd.customType=REGULAR-EXPRESSION
        * xml.xsd.type=string
    """

    # RegularExpression method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.60, p.112
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.65, p.114
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintValue   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setBlueprintValue   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNamePattern      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setNamePattern      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        self.blueprintValue: Optional[str] = None

        # This attribute represents a pattern which shall be used to define the value of the identifier if the CIdentifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate. Tags: xml.attribute=true
        self.namePattern: Optional[str] = None

    def getBlueprintValue(self) -> Optional[str]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint.

        Returns:
            The blueprint value, or None if not set
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: str):
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint.

        Args:
            value: The blueprint value to set

        Returns:
            self for method chaining
        """
        self.blueprintValue = value
        return self

    def getNamePattern(self) -> Optional[str]:
        """
        This attribute represents a pattern which shall be used to define the value of the identifier if the CIdentifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate.

        Returns:
            The name pattern, or None if not set
        """
        return self.namePattern

    def setNamePattern(self, value: str):
        """
        This attribute represents a pattern which shall be used to define the value of the identifier if the CIdentifier in question is part of a blueprint. For more details refer to TPS_StandardizationTemplate.

        Args:
            value: The name pattern to set

        Returns:
            self for method chaining
        """
        self.namePattern = value
        return self


class McdIdentifier(ARLiteral):
    """
    This primitive denotes a name used for measurement and calibration systems and shall follow the restrictions for an ASAM ASAP2 ident. For detailed syntax see the xsd.pattern. The size limitations are not captured.

    McdIdentifiers are random names which may contain characters A through Z, a through z, underscore (_), numerals 0 through 9, points ('.') and brackets ( '[',']' ).
    However, the following limitations apply: the first character must be a letter or an underscore, brackets must occur in pairs at the end of a partial string and must contain a number or an alpha-numerical string (description of the index of an array element).

    Tags:
        * xml.xsd.customType=MCD-IDENTIFIER
        * xml.xsd.pattern= ``[a-zA-Z_][a-zA-Z0-9_]*(\\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\\])*(\\.[a-zA-Z_][a-zA-Z0-9_]*(\\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\\])*)*``
        * xml.xsd.type=string
    """

    # McdIdentifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.54, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class MimeTypeString(ARLiteral):
    """
    This primitive denotes the an Internet media type, originally called a MIME type after MIME and sometimes a Content-type after the name of a header in several protocols whose value is such a type, is a two-part identifier for file formats on the Internet.

    Tags:
        * xml.xsd.customType=MIME-TYPE-STRING
        * xml.xsd.type=string
    """

    # MimeTypeString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.55, p.111
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class NameTokens(ARLiteral):
    """
    This is a white-space separated list of name tokens.

    Tags:
        * xml.xsd.customType=NMTOKENS-STRING
        * xml.xsd.type=NMTOKENS
    """

    # NameTokens method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.56, p.111
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class ViewTokens(ARLiteral):
    """
    This primitive specifies the tokens to specify a documentation view.

    Tags:
        * xml.xsd.customType=VIEW-TOKENS
        * xml.xsd.pattern= ``(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*``
        * xml.xsd.type=string
    """

    # ViewTokens method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.78, p.340
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class AclScopeEnum(AREnum):
    """
    This enumerator represents the scope of a definition in context of access control.
    """

    # AclScopeEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.6, p.384
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This specifies that the AclPermission applies to dependant (in particular referenced) operations / objects as well. Note that this includes the descendant ones. Tags: atp.EnumerationLiteralIndex=0
    DEPENDANT = "dependant"

    # This specifies that the AclPermission applies to descendant operations / objects as well. Tags: atp.EnumerationLiteralIndex=1
    DESCENDANT = "descendant"

    # This is indicates that the AclPermission applies to explicit objects / operations only. Tags: atp.EnumerationLiteralIndex=2
    EXPLICIT = "explicit"

    def __init__(self):
        super().__init__(
            [
                AclScopeEnum.DEPENDANT,
                AclScopeEnum.DESCENDANT,
                AclScopeEnum.EXPLICIT,
            ]
        )


class AdditionalBindingTimeEnum(AREnum):
    pass


class ContainerIPduHeaderTypeEnum(AREnum):
    pass


class ContainerIPduTriggerEnum(AREnum):
    pass


class CouplingElementEnum(AREnum):
    pass


class CryptoServiceKeyGenerationEnum(AREnum):
    pass


class DataConsistencyPolicyEnum(AREnum):
    pass


class DataExchangePointKind(AREnum):
    pass


class DdsDestinationOrderKindEnum(AREnum):
    pass


class DdsDurabilityKindEnum(AREnum):
    pass


class DdsDurabilityServiceHistoryKindEnum(AREnum):
    pass


class DdsHistoryKindEnum(AREnum):
    pass


class DdsLivenessKindEnum(AREnum):
    pass


class DdsOwnershipKindEnum(AREnum):
    pass


class DdsReliabilityKindEnum(AREnum):
    pass


class DefaultValueApplicationStrategyEnum(AREnum):
    pass


class DiagPduType(AREnum):
    pass


class DiagnosticClearDtcLimitationEnum(AREnum):
    """
    Scope of the DEM_ClearDTC Api.
    """

    # DiagnosticClearDtcLimitationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.169, p.183
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # DEM_ClearDtc API accepts all supported DTC values. Tags: atp.EnumerationLiteralIndex=0
    ALL_SUPPORTED_DTCS = "allSupportedDtcs"

    # DEM_ClearDtc API accepts ClearAllDTCs only. Tags: atp.EnumerationLiteralIndex=1
    CLEAR_ALL_DTCS = "clearAllDtcs"

    def __init__(self):
        super().__init__(
            [
                DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS,
                DiagnosticClearDtcLimitationEnum.CLEAR_ALL_DTCS,
            ]
        )


class DiagnosticClearEventAllowedBehaviorEnum(AREnum):
    """
    This enumeration defines the possible behavior for clear event allowed
    """

    # DiagnosticClearEventAllowedBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.150, p.166
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The event status byte keeps unchanged. Tags: atp.EnumerationLiteralIndex=0
    NO_STATUS_BYTE_CHANGE = "noStatusByteChange"

    # The OperationCycle and readiness bits of the event status byte are reset. Tags: atp.EnumerationLiteralIndex=1
    ONLY_THIS_CYCLE_AND_READINESS = "onlyThisCycleAndReadiness"

    def __init__(self):
        super().__init__(
            [
                DiagnosticClearEventAllowedBehaviorEnum.NO_STATUS_BYTE_CHANGE,
                DiagnosticClearEventAllowedBehaviorEnum.ONLY_THIS_CYCLE_AND_READINESS,
            ]
        )


class DiagnosticConnectedIndicatorBehaviorEnum(AREnum):
    """
    Behavior of the indicator.
    """

    # DiagnosticConnectedIndicatorBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.155, p.168
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The indicator blinks when the event has status FAILED. Tags: atp.EnumerationLiteralIndex=0
    BLINK_MODE = "blinkMode"

    # The indicator is active and blinks when the event has status FAILED. Tags: atp.EnumerationLiteralIndex=1
    BLINK_OR_CONTINUOUS_ON_MODE = "blinkOrContinuousOnMode"

    # The indicator is active when the event has status FAILED. Tags: atp.EnumerationLiteralIndex=2
    CONTINUOUS_ON_MODE = "continuousOnMode"

    # Flash Indicator Lamp should be set to "Fast Flash". Tags: atp.EnumerationLiteralIndex=3
    FAST_FLASHING_MODE = "fastFlashingMode"

    # Flash Indicator Lamp should be set to "Slow Flash". Tags: atp.EnumerationLiteralIndex=4
    SLOW_FLASHING_MODE = "slowFlashingMode"

    def __init__(self):
        super().__init__(
            [
                DiagnosticConnectedIndicatorBehaviorEnum.BLINK_MODE,
                DiagnosticConnectedIndicatorBehaviorEnum.BLINK_OR_CONTINUOUS_ON_MODE,
                DiagnosticConnectedIndicatorBehaviorEnum.CONTINUOUS_ON_MODE,
                DiagnosticConnectedIndicatorBehaviorEnum.FAST_FLASHING_MODE,
                DiagnosticConnectedIndicatorBehaviorEnum.SLOW_FLASHING_MODE,
            ]
        )


class DiagnosticDebounceBehaviorEnum(AREnum):
    """
    Event debounce algorithm behavior options.
    """

    # DiagnosticDebounceBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.192, p.199
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The event debounce counter will be frozen with the current value and will not change while a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled. After all related enable conditions are fulfilled and ControlDTCSetting of the related event is enabled again, the event qualification will continue with the next report of the event (i.e. SetEventStatus). Tags: atp.EnumerationLiteralIndex=0
    FREEZE = "freeze"

    # The event debounce counter will be reset to initial value if a related enable condition is not fulfilled or ControlDTCSetting of the related event is disabled. The qualification of the event will be restarted with the next valid event report. Tags: atp.EnumerationLiteralIndex=1
    RESET = "reset"

    def __init__(self):
        super().__init__(
            [
                DiagnosticDebounceBehaviorEnum.FREEZE,
                DiagnosticDebounceBehaviorEnum.RESET,
            ]
        )


class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(AREnum):
    """
    This meta-class contains a list of possible subfunctions for the UDS service 0x2C.
    """

    # DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.96, p.129
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Clear the specified dynamic data identifier. Tags: atp.EnumerationLiteralIndex=0
    CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER = "clearDynamicallyDefineDataIdentifier"

    # The definition of dynamic data identifier shall be done via a reference to a diagnostic data identifier. Tags: atp.EnumerationLiteralIndex=1
    DEFINE_BY_IDENTIFIER = "defineByIdentifier"

    # The definition of dynamic data identifier shall be done via a reference to a memory address. Tags: atp.EnumerationLiteralIndex=2
    DEFINE_BY_MEMORY_ADDRESS = "defineByMemoryAddress"

    def __init__(self):
        super().__init__(
            [
                DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER,
                DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_IDENTIFIER,
                DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_MEMORY_ADDRESS,
            ]
        )


class DiagnosticEventClearAllowedEnum(AREnum):
    """
    Denotes whether clearing of events is allowed.
    """

    # DiagnosticEventClearAllowedEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.153, p.167
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The clearing is allowed unconditionally. Tags: atp.EnumerationLiteralIndex=0
    ALWAYS = "always"

    # In case the clearing of a Diagnostic Event has to be allowed or prohibited through the SWC interface CallbackClearEventAllowed, the SWC has to indicate this by defining appropriate ServiceNeeds (i.e. DiagnosticEventNeeds). Tags: atp.EnumerationLiteralIndex=2
    REQUIRES_CALLBACK_EXECUTION = "requiresCallbackExecution"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventClearAllowedEnum.ALWAYS,
                DiagnosticEventClearAllowedEnum.REQUIRES_CALLBACK_EXECUTION,
            ]
        )


class DiagnosticEventCombinationBehaviorEnum(AREnum):
    """
    Select type of Event Combination support
    """

    # DiagnosticEventCombinationBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.23, p.67
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Event combination on retrieval is used to combine events. For each event an individual event memory entry is created, while reporting the data via UDS, the data is combined. Tags: atp.EnumerationLiteralIndex=1
    EVENT_COMBINATION_ON_RETRIEVAL = "eventCombinationOnRetrieval"

    # Event combination on storage is used to combine events. Only one memory entry exists for each DTC which is also reported via UDS. Tags: atp.EnumerationLiteralIndex=0
    EVENT_COMBINATION_ON_STORAGE = "eventCombinationOnStorage"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_RETRIEVAL,
                DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_STORAGE,
            ]
        )


class DiagnosticEventCombinationReportingBehaviorEnum(AREnum):
    """
    Select reporting format of events. Applicable only for Event Combination on Retrieval.
    """

    # DiagnosticEventCombinationReportingBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.24, p.67
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The reporting order for event combination on retrieval is the chronological storage order of the events Tags: atp.EnumerationLiteralIndex=0
    REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST = "reportingInChronlogicalOrderOldestFirst"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventCombinationReportingBehaviorEnum.REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST,
            ]
        )


class DiagnosticEventDisplacementStrategyEnum(AREnum):
    """
    Defines the displacement strategy.
    """

    # DiagnosticEventDisplacementStrategyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.170, p.183
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Event memory entry displacement is enabled, by consideration of priority active/passive status, and occurrence. Tags: atp.EnumerationLiteralIndex=0
    FULL = "full"

    # Event memory entry displacement is disabled. Tags: atp.EnumerationLiteralIndex=1
    NONE = "none"

    # Event memory entry displacement is enabled, by consideration of priority and occurrence (but without active/passive status). Tags: atp.EnumerationLiteralIndex=2
    PRIO_OCC = "prioOcc"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventDisplacementStrategyEnum.FULL,
                DiagnosticEventDisplacementStrategyEnum.NONE,
                DiagnosticEventDisplacementStrategyEnum.PRIO_OCC,
            ]
        )


class DiagnosticEventKindEnum(AREnum):
    """
    Applicability of the diagnostic event.
    """

    # DiagnosticEventKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.154, p.167
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The event is assigned to a BSW module. Tags: atp.EnumerationLiteralIndex=0
    BSW = "bsw"

    # The event is assigned to a SWC. Tags: atp.EnumerationLiteralIndex=1
    SWC = "swc"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventKindEnum.BSW,
                DiagnosticEventKindEnum.SWC,
            ]
        )


class DiagnosticEventWindowTimeEnum(AREnum):
    """
    This represents the ability to define the semantics of the event window.
    """

    # DiagnosticEventWindowTimeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.104, p.133
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This value specifies that the event window shall stay active for an infinite amount of time (e.g. open window until power off). Tags: atp.EnumerationLiteralIndex=3
    INFINITE_TIME_TO_RESPONSE = "infiniteTimeToResponse"

    # This enumeration value specifies that the server shall send response on event messages until the server is powered down. The server stops sending response on event messages with the power down and will send no more response on event messages after server is up again. Tags: atp.EnumerationLiteralIndex=4
    POWER_WINDOW_TIME = "powerWindowTime"

    def __init__(self):
        super().__init__(
            [
                DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE,
                DiagnosticEventWindowTimeEnum.POWER_WINDOW_TIME,
            ]
        )


class DiagnosticHandleDDDIConfigurationEnum(AREnum):
    """
    This meta-class represents the options for controlling how the configuration of the DynamicallyDefineDataIdentifiers is done in the given context.
    """

    # DiagnosticHandleDDDIConfigurationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.95, p.128
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the configuration of DynamicallyDefineDataIdentifier shall be stored as non-volatile data. Tags: atp.EnumerationLiteralIndex=0
    NON_VOLATILE = "nonVolatile"

    # This indicates that the configuration of DynamicallyDefineDataIdentifier shall be handled as volatile data. Tags: atp.EnumerationLiteralIndex=1
    VOLATILE = "volatile"

    def __init__(self):
        super().__init__(
            [
                DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE,
                DiagnosticHandleDDDIConfigurationEnum.VOLATILE,
            ]
        )


class DiagnosticInhibitionMaskEnum(AREnum):
    """
    This meta-class represents the ability to define different kinds of inhibition mask behavior.
    """

    # DiagnosticInhibitionMaskEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.217, p.216
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This represents the inhibition mask behavior "last failed". Tags: atp.EnumerationLiteralIndex=0
    LAST_FAILED = "lastFailed"

    # This represents the inhibition mask behavior "not tested". Tags: atp.EnumerationLiteralIndex=1
    NOT_TESTED = "notTested"

    # This represents the inhibition mask behavior "tested". Tags: atp.EnumerationLiteralIndex=3
    TESTED = "tested"

    # This represents the inhibition mask behavior "tested and failed". Tags: atp.EnumerationLiteralIndex=2
    TESTED_AND_FAILED = "testedAndFailed"

    def __init__(self):
        super().__init__(
            [
                DiagnosticInhibitionMaskEnum.LAST_FAILED,
                DiagnosticInhibitionMaskEnum.NOT_TESTED,
                DiagnosticInhibitionMaskEnum.TESTED,
                DiagnosticInhibitionMaskEnum.TESTED_AND_FAILED,
            ]
        )


class DiagnosticIumprKindEnum(AREnum):
    """
    This enumeration is used to control the ratio calculation behavior.
    """

    # DiagnosticIumprKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.208, p.210
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The calculation is based on the usage of an API. Tags: atp.EnumerationLiteralIndex=0
    API_BASED = "apiBased"

    # The calculation is based on the usage of an observer. Tags: atp.EnumerationLiteralIndex=1
    OBSERVER_BASED = "observerBased"

    def __init__(self):
        super().__init__(
            [
                DiagnosticIumprKindEnum.API_BASED,
                DiagnosticIumprKindEnum.OBSERVER_BASED,
            ]
        )


class DiagnosticMemoryEntryStorageTriggerEnum(AREnum):
    """
    Trigger types to allocate an event memory entry.
    """

    # DiagnosticMemoryEntryStorageTriggerEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.168, p.183
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Status information of UDS DTC status bit 3 Tags: atp.EnumerationLiteralIndex=0
    CONFIRMED = "confirmed"

    # Threshold to allocate an event memory entry and to capture the Freeze Frame. Tags: atp.EnumerationLiteralIndex=1
    FDC_THRESHOLD = "fdcThreshold"

    # Status information of UDS DTC status bit 0. Tags: atp.EnumerationLiteralIndex=3
    TEST_FAILED = "testFailed"

    def __init__(self):
        super().__init__(
            [
                DiagnosticMemoryEntryStorageTriggerEnum.CONFIRMED,
                DiagnosticMemoryEntryStorageTriggerEnum.FDC_THRESHOLD,
                DiagnosticMemoryEntryStorageTriggerEnum.TEST_FAILED,
            ]
        )


class DiagnosticObdSupportEnum(AREnum):
    """
    This meta-class represents the ability to model the roles in which a participation in OBD is foreseen. At the moment, this applies exclusively to the Dem. However, future extension of the Dcm may require this setting as well.
    """

    # DiagnosticObdSupportEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.206, p.207
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This represent the role "master ECU". Tags: atp.EnumerationLiteralIndex=0
    MASTER_ECU = "masterEcu"

    # This represents the ability to explicitly specify that no participation in OBD is foreseen. Tags: atp.EnumerationLiteralIndex=1
    NO_OBD_SUPPORT = "noObdSupport"

    # This represents the role "primary ECU". Tags: atp.EnumerationLiteralIndex=2
    PRIMARY_ECU = "primaryEcu"

    # This represents the role "secondary ECU". Tags: atp.EnumerationLiteralIndex=3
    SECONDARY_ECU = "secondaryEcu"

    def __init__(self):
        super().__init__(
            [
                DiagnosticObdSupportEnum.MASTER_ECU,
                DiagnosticObdSupportEnum.NO_OBD_SUPPORT,
                DiagnosticObdSupportEnum.PRIMARY_ECU,
                DiagnosticObdSupportEnum.SECONDARY_ECU,
            ]
        )


class DiagnosticOccurrenceCounterProcessingEnum(AREnum):
    """
    The occurrence counter triggering types.
    """

    # DiagnosticOccurrenceCounterProcessingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.20, p.66
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The occurrence counter is incremented when TestFailed bit transitions from 0 to 1 if the fault confirmation was successful (ConfirmedDTC bit is already set). Tags: atp.EnumerationLiteralIndex=0
    CONFIRMED_DTC_BIT = "confirmedDtcBit"

    # The occurrence counter is incremented when TestFailed bit transitions from 0 to 1 (and the fault confirmation is not considered). Tags: atp.EnumerationLiteralIndex=1
    TEST_FAILED_BIT = "testFailedBit"

    def __init__(self):
        super().__init__(
            [
                DiagnosticOccurrenceCounterProcessingEnum.CONFIRMED_DTC_BIT,
                DiagnosticOccurrenceCounterProcessingEnum.TEST_FAILED_BIT,
            ]
        )


class DiagnosticOperationCycleTypeEnum(AREnum):
    """
    Operation cycles types used to identify certain Operation cycles with a certain semantics.
    """

    # DiagnosticOperationCycleTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.197, p.201
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Ignition ON / OFF cycle Tags: atp.EnumerationLiteralIndex=0
    IGNITION = "ignition"

    # OBD Driving cycle Tags: atp.EnumerationLiteralIndex=1
    OBD_DRIVING_CYCLE = "obdDrivingCycle"

    # further operation cycle Tags: atp.EnumerationLiteralIndex=2
    OTHER = "other"

    # OBD Warm up cycle Tags: atp.EnumerationLiteralIndex=5
    WARMUP = "warmup"

    def __init__(self):
        super().__init__(
            [
                DiagnosticOperationCycleTypeEnum.IGNITION,
                DiagnosticOperationCycleTypeEnum.OBD_DRIVING_CYCLE,
                DiagnosticOperationCycleTypeEnum.OTHER,
                DiagnosticOperationCycleTypeEnum.WARMUP,
            ]
        )


class DiagnosticPeriodicRateCategoryEnum(AREnum):
    """
    This meta-class provides possible values for the setting of the periodic rate.
    """

    # DiagnosticPeriodicRateCategoryEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.100, p.131
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This value represents a fast periodic rate. Tags: atp.EnumerationLiteralIndex=0
    PERIODIC_RATE_FAST = "periodicRateFast"

    # This value represents a medium periodic rate. Tags: atp.EnumerationLiteralIndex=1
    PERIODIC_RATE_MEDIUM = "periodicRateMedium"

    # This value represents a slow periodic rate. Tags: atp.EnumerationLiteralIndex=2
    PERIODIC_RATE_SLOW = "periodicRateSlow"

    def __init__(self):
        super().__init__(
            [
                DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST,
                DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM,
                DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW,
            ]
        )


class DiagnosticRecordTriggerEnum(AREnum):
    """
    Triggers to allocate an event memory entry.
    """

    # DiagnosticRecordTriggerEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.182, p.191
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # capture on "Confirmed" Tags: atp.EnumerationLiteralIndex=0
    CONFIRMED = "confirmed"

    # implement custom capture Tags: atp.EnumerationLiteralIndex=4
    CUSTOM = "custom"

    # capture on "FDC Threshold" Tags: atp.EnumerationLiteralIndex=1
    FDC_THRESHOLD = "fdcThreshold"

    # capture on "Pending" Tags: atp.EnumerationLiteralIndex=2
    PENDING = "pending"

    # capture on "Test Failed" Tags: atp.EnumerationLiteralIndex=3
    TEST_FAILED = "testFailed"

    # Test Failed This Operation Cycle. Tags: atp.EnumerationLiteralIndex=5
    TEST_FAILED_THIS_OPERATION_CYCLE = "testFailedThisOperationCycle"

    # Capture on testFailed bit transition 1 -> 0. Tags: atp.EnumerationLiteralIndex=6
    TEST_PASSED = "testPassed"

    def __init__(self):
        super().__init__(
            [
                DiagnosticRecordTriggerEnum.CONFIRMED,
                DiagnosticRecordTriggerEnum.CUSTOM,
                DiagnosticRecordTriggerEnum.FDC_THRESHOLD,
                DiagnosticRecordTriggerEnum.PENDING,
                DiagnosticRecordTriggerEnum.TEST_FAILED,
                DiagnosticRecordTriggerEnum.TEST_FAILED_THIS_OPERATION_CYCLE,
                DiagnosticRecordTriggerEnum.TEST_PASSED,
            ]
        )


class DiagnosticResponseOnEventActionEnum(AREnum):
    """
    This meta-class has the ability to define sub-functions of the UDS service ResponseOnEvent.
    """

    # DiagnosticResponseOnEventActionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.105, p.134
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Clears the configured events. Tags: atp.EnumerationLiteralIndex=2
    CLEAR = "clear"

    # Reports based on change of data identifier. Tags: atp.EnumerationLiteralIndex=6
    ON_CHANGE_OF_DATA_IDENTIFIER = "onChangeOfDataIdentifier"

    # Triggered if data condition is met (e.g. RPM over 5000 1/min). Tags: atp.EnumerationLiteralIndex=8
    ON_COMPARISON_OF_VALUES = "onComparisonOfValues"

    # Reports based on change of DTC status. Tags: atp.EnumerationLiteralIndex=7
    ON_DTC_STATUS_CHANGE = "onDTCStatusChange"

    # Reports the activated events. Tags: atp.EnumerationLiteralIndex=3
    REPORT = "report"

    # Reports the DTC record-related information based on a DTC status change. (Subfunction 0x09) Tags: atp.EnumerationLiteralIndex=5
    REPORT_DTC_RECORD_INFORMATION_ON_DTC_STATUS_CHANGE = "reportDTCRecordInformationOnDtcStatusChange"

    # Triggers the report of the most recent failed or confirmed DTC (Subfunction 0x08). Tags: atp.EnumerationLiteralIndex=4
    REPORT_MOST_RECENT_DTC_ON_STATUS_CHANGE = "reportMostRecentDtcOnStatusChange"

    # Starts the response on event service. Tags: atp.EnumerationLiteralIndex=1
    START = "start"

    # Stops the response on event service. Tags: atp.EnumerationLiteralIndex=0
    STOP = "stop"

    def __init__(self):
        super().__init__(
            [
                DiagnosticResponseOnEventActionEnum.CLEAR,
                DiagnosticResponseOnEventActionEnum.ON_CHANGE_OF_DATA_IDENTIFIER,
                DiagnosticResponseOnEventActionEnum.ON_COMPARISON_OF_VALUES,
                DiagnosticResponseOnEventActionEnum.ON_DTC_STATUS_CHANGE,
                DiagnosticResponseOnEventActionEnum.REPORT,
                DiagnosticResponseOnEventActionEnum.REPORT_DTC_RECORD_INFORMATION_ON_DTC_STATUS_CHANGE,
                DiagnosticResponseOnEventActionEnum.REPORT_MOST_RECENT_DTC_ON_STATUS_CHANGE,
                DiagnosticResponseOnEventActionEnum.START,
                DiagnosticResponseOnEventActionEnum.STOP,
            ]
        )


class DiagnosticResponseToEcuResetEnum(AREnum):
    """
    This enumeration controls the point in time in which a response to the reception of an EcuReset service shall be generated.
    """

    # DiagnosticResponseToEcuResetEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.62, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Answer to EcuReset service should come after the reset. Tags: atp.EnumerationLiteralIndex=0
    RESPOND_AFTER_RESET = "respondAfterReset"

    # Answer to EcuReset service should come before the reset. Tags: atp.EnumerationLiteralIndex=1
    RESPOND_BEFORE_RESET = "respondBeforeReset"

    def __init__(self):
        super().__init__(
            [
                DiagnosticResponseToEcuResetEnum.RESPOND_AFTER_RESET,
                DiagnosticResponseToEcuResetEnum.RESPOND_BEFORE_RESET,
            ]
        )


class DiagnosticSignificanceEnum(AREnum):
    """
    Significance level of a diagnostic event.
    """

    # DiagnosticSignificanceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.176, p.187
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Failure, which affects the component/ECU itself. Tags: atp.EnumerationLiteralIndex=0
    FAULT = "fault"

    # Issue, which indicates additional information concerning insufficient system behavior. Tags: atp.EnumerationLiteralIndex=1
    OCCURENCE = "occurence"

    def __init__(self):
        super().__init__(
            [
                DiagnosticSignificanceEnum.FAULT,
                DiagnosticSignificanceEnum.OCCURENCE,
            ]
        )


class DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum(AREnum):
    """
    This enumeration controls whether the aging and displacement mechanism shall be applied to the 'TestFailedSinceLastClear' status bits.
    """

    # DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.171, p.184
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The "TestFailedSinceLastClear" status bits are reset to 0, if aging or displacement applies. Tags: atp.EnumerationLiteralIndex=0
    STATUS_BIT_AGING_AND_DISPLACEMENT = "statusBitAgingAndDisplacement"

    # Aging and displacement has no impact on the "TestFailedSinceLastClear" status bits. Tags: atp.EnumerationLiteralIndex=1
    STATUS_BIT_NORMAL = "statusBitNormal"

    def __init__(self):
        super().__init__(
            [
                DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_AGING_AND_DISPLACEMENT,
                DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL,
            ]
        )


class DiagnosticTestResultUpdateEnum(AREnum):
    """
    This meta-class represents the ability to define the update behavior of a DiagnosticTestResult.
    """

    # DiagnosticTestResultUpdateEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.202, p.205
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Any DTR result reported by the monitor is used by the Dem. Tags: atp.EnumerationLiteralIndex=0
    ALWAYS = "always"

    # The Dem accepts reported DTRs only when the configured debouncing mechanism is stable at the FAIL or PASS limit. Tags: atp.EnumerationLiteralIndex=1
    STEADY = "steady"

    def __init__(self):
        super().__init__(
            [
                DiagnosticTestResultUpdateEnum.ALWAYS,
                DiagnosticTestResultUpdateEnum.STEADY,
            ]
        )


class DiagnosticTroubleCodeJ1939DtcKindEnum(AREnum):
    """
    This meta-class represents the ability to further specify a J1939 DTC in terms of its semantics.
    """

    # DiagnosticTroubleCodeJ1939DtcKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.222, p.221
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # this represents a DTC that is only relevant for service in a garage, reported by e.g. DM53. Tags: atp.EnumerationLiteralIndex=0
    SERVICE_ONLY = "serviceOnly"

    # This represents a non-specific DTC reported by e.g. DM1. Tags: atp.EnumerationLiteralIndex=1
    STANDARD = "standard"

    def __init__(self):
        super().__init__(
            [
                DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY,
                DiagnosticTroubleCodeJ1939DtcKindEnum.STANDARD,
            ]
        )


class DiagnosticTypeOfDtcSupportedEnum(AREnum):
    """
    Supported Dtc Types
    """

    # DiagnosticTypeOfDtcSupportedEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.21, p.66
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # ISO11992-4 DTC format Tags: atp.EnumerationLiteralIndex=0 xml.name=ISO-11992-4
    ISO11992_4 = "iso11992_4"

    # ISO14229-1 DTC format (3 byte format) Tags: atp.EnumerationLiteralIndex=1 xml.name=ISO-14229-1
    ISO14229_1 = "iso14229_1"

    # ISO15031-6 DTC format (2 byte format) Tags: atp.EnumerationLiteralIndex=2 xml.name=ISO-15031-6
    ISO15031_6 = "iso15031_6"

    # SAEJ1939-73 DTC format Tags: atp.EnumerationLiteralIndex=3 xml.name=SAE-J-1939-73
    SAEJ1939_73 = "saeJ1939_73"

    # SAE_J2012-DA_DTCFormat_00 (3 byte format) Tags: atp.EnumerationLiteralIndex=4 xml.name=SAE-J-2012-DA
    SAEJ2012_DA = "saeJ2012_da"

    def __init__(self):
        super().__init__(
            [
                DiagnosticTypeOfDtcSupportedEnum.ISO11992_4,
                DiagnosticTypeOfDtcSupportedEnum.ISO14229_1,
                DiagnosticTypeOfDtcSupportedEnum.ISO15031_6,
                DiagnosticTypeOfDtcSupportedEnum.SAEJ1939_73,
                DiagnosticTypeOfDtcSupportedEnum.SAEJ2012_DA,
            ]
        )


class DiagnosticTypeOfFreezeFrameRecordNumerationEnum(AREnum):
    """
    FreezeFrame record numeration type
    """

    # DiagnosticTypeOfFreezeFrameRecordNumerationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.172, p.184
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Freeze frame records will be numbered consecutive starting by 1 in their chronological order. Tags: atp.EnumerationLiteralIndex=0
    CALCULATED = "calculated"

    # Freeze frame records will be numbered based on the given configuration in their chronological order. Tags: atp.EnumerationLiteralIndex=1
    CONFIGURED = "configured"

    def __init__(self):
        super().__init__(
            [
                DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CALCULATED,
                DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CONFIGURED,
            ]
        )


class DiagnosticUdsSeverityEnum(AREnum):
    pass


class DiagnosticWwhObdDtcClassEnum(AREnum):
    pass


class EthGlobalTimeMessageFormatEnum(AREnum):
    pass


class FMFeatureSelectionState(AREnum):
    pass


class FlowMeteringColorModeEnum(AREnum):
    pass


class FrArTpAckType(AREnum):
    pass


class GlobalTimeCrcSupportEnum(AREnum):
    pass


class GlobalTimeCrcValidationEnum(AREnum):
    pass


class GlobalTimeIcvSupportEnum(AREnum):
    pass


class GlobalTimeIcvVerificationEnum(AREnum):
    pass


class GlobalTimePortRoleEnum(AREnum):
    pass


class IEEE1722TpAafAes3DataTypeEnum(AREnum):
    pass


class IEEE1722TpAafFormatEnum(AREnum):
    pass


class IEEE1722TpAafNominalRateEnum(AREnum):
    pass


class IEEE1722TpAcfCanMessageTypeEnum(AREnum):
    pass


class IEEE1722TpCrfPullEnum(AREnum):
    pass


class IEEE1722TpCrfTypeEnum(AREnum):
    pass


class IEEE1722TpRvfColorSpaceEnum(AREnum):
    pass


class IEEE1722TpRvfFrameRateEnum(AREnum):
    pass


class IEEE1722TpRvfPixelDepthEnum(AREnum):
    pass


class IEEE1722TpRvfPixelFormatEnum(AREnum):
    pass


class LinChecksumType(AREnum):
    pass


class MappingScopeEnum(AREnum):
    pass


class MaximumMessageLengthType(AREnum):
    pass


class MirroringProtocolEnum(AREnum):
    pass


class RxAcceptContainedIPduEnum(AREnum):
    pass


class SecurityEventContextDataSourceEnum(AREnum):
    pass


class SecurityEventReportingModeEnum(AREnum):
    pass


class SendIndicationEnum(AREnum):
    pass


class SeverityEnum(AREnum):
    pass


class SwcToSwcOperationArgumentsDirectionEnum(AREnum):
    pass


class SwitchStreamFilterActionPortModificationEnum(AREnum):
    pass
