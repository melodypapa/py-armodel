from abc import ABCMeta
import re
from typing import List
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ARType(metaclass = ABCMeta):
    def __init__(self) -> None:
        self.timestamp = None           # type: str   
        self.uuid = None                # type: str
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    def getText(self) -> str:
        return str(self)

class ARNumerical(ARType):
    def __init__(self) -> None:
        super().__init__()

        self._text = None                   # type: str

    def _convertStringToNumberValue(self, value: str) -> int:
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
                m = re.match(r"-?\d+\.\d+", value)
                if m:
                    return float(value)
                return int(value)
        except:
            raise ValueError("Invalid Numerical Type <%s>" % value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: any):
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


class ARFloat(ARNumerical):
    def __init__(self) -> None:
        super().__init__()

        self._text = None                   # type: str

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, val: any):
        if isinstance(val, float):
            self._value = val
        elif isinstance(val, int):
            self._value = val * 1.0
        elif isinstance(val, str):
            self._text = val
            #self._value = float(val)
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
    def __init__(self):
        super().__init__()
        
class TimeValue(ARFloat):
    '''
        This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted
        in the physical unit second.
        Tags:
            * xml.xsd.customType=TIME-VALUE
            * xml.xsd.type=double
    '''

    def __init__(self):
        super().__init__()


class ARLiteral(ARType):
    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> str:
        if self._value is None:
            return ""
        return self._value

    @value.setter
    def value(self, val: any):
        if isinstance(val, str):
            self._value = val
        else:
            self._value = str(val)

    def __str__(self) -> str:
        return self.value

    def upper(self) -> str:
        return self.value.upper()

class AREnum(ARLiteral):
    def __init__(self, enum_values: List[str]):
        super().__init__()
        
        self.enumValues = enum_values                # List[str]

    def getEnumValues(self):
        return self.enumValues

    def setEnumValues(self, values: List[str]):
        self.enumValues = values
        return self

    def validateEnumValue(self, value: str):
        if value in self.enumValues:
            return True
        return False

class String(ARLiteral):
    def __init__(self):
        super().__init__()

class ReferrableSubtypesEnum(ARLiteral):
    def __init__(self):
        super().__init__()

class ARPositiveInteger(ARNumerical):
    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: any):
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
    def __init__(self) -> None:
        super().__init__()

        self._text = None

    def _convertNumberToBoolean(self, value: int) -> bool:
        if value == 0:
            return False
        return True

    def _convertStringToBoolean(self, value: str) -> bool:
        value = value.lower()
        if value == "true" or value == "1":
            return True
        elif value == "false" or value == "0":
            return False
        else:
            return self._convertNumberToBoolean(int(value))

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: any):
        if isinstance(val, bool):
            self._value = val
        elif isinstance(val, int):
            self._value = self._convertNumberToBoolean(val)
            self._text = str(val)
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToBoolean(val)
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
    def __init__(self):
        super().__init__()

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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__()

class CIdentifier(ARLiteral):
    '''
        This datatype represents a string, that follows the rules of C-identifiers.
        
        Tags:
            * xml.xsd.customType=C-IDENTIFIER
            * xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*
            * xml.xsd.type=string
    '''
    def __init__(self):
        super().__init__()

        self.blueprintValue = None
        self.namePattern = None

    def getBlueprintValue(self):
        return self.blueprintValue

    def setBlueprintValue(self, value):
        self.blueprintValue = value
        return self

    def getNamePattern(self):
        return self.namePattern

    def setNamePattern(self, value):
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
    def __init__(self):
        super().__init__()

        self.intervalType = None                # type: str
        self.value = None                       # type: str

    def getIntervalType(self):
        return self.intervalType

    def setIntervalType(self, value):
        self.intervalType = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

class RefType(ARObject):
    def __init__(self):
        self.base = None                        # type: str
        self.dest = None                        # type: str
        self.value = None                       # type: str

    def getBase(self):
        return self.base

    def setBase(self, value):
        self.base = value
        return self

    def getDest(self):
        return self.dest

    def setDest(self, value):
        self.dest = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

class TRefType(RefType):
    def __init__(self):
        super().__init__()

class DiagRequirementIdString(ARLiteral):
    '''
        This string denotes an Identifier for a requirement.

        Tags:
            * xml.xsd.customType=DIAG-REQUIREMENT-ID-STRING
            * xml.xsd.pattern=[0-9a-zA-Z_\-]+
            * xml.xsd.type=string
    '''
    def __init__(self):
        super().__init__()

