from abc import ABCMeta
import re

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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


class String(ARLiteral):
    
    pass


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
        if value == "true":
            return True
        elif value == "false":
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
    '''
        This is a positive integer which can be denoted in decimal, binary, octal and hexadecimal. The value is
        between 0 and 4294967295.
        
        Tags:
            * xml.xsd.customType=POSITIVE-INTEGER
            * xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+
            * xml.xsd.type=string
    '''
    def __init__(self):
        super().__init__()

class Integer(ARNumerical):
    '''
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
class Limit(ARObject):
    def __init__(self):
        super().__init__()

        self.intervalType = None       # type: str
        self.value = None               # type: str


class RefType(ARObject):
    def __init__(self):
        self.dest = ""
        self.value = ""

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