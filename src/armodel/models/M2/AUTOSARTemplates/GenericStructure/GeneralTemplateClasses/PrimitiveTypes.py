from abc import ABCMeta
import re

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

