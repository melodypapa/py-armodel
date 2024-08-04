from abc import ABCMeta
import re
from typing import Dict, List

import xml.etree.cElementTree as ET


class ARObject(metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("ARObject is an abstract class.")
        
        self.parent = None              # type: ARObject
        self.checksum = None            # type: str

        self.timestamp = None           # type: str
        self.uuid = None                # type: str

    def getTagName(self, tag: str, nsmap: Dict) -> str:
        return tag.replace("{%s}" % nsmap["xmlns"], "")
    
class ARType(metaclass=ABCMeta):
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

class ARNumerical(ARType):
    def __init__(self) -> None:
        super().__init__()

        self._text = None                   # type: str

    def _convertStringToNumberValue(self, value: str) -> int:
        m = re.match(r"0x([0-9a-f]+)", value, re.I)
        if (m):
            return int(m.group(1), 16)
        return int(value)
    
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

class ARFloat(ARType):
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
            self._value = float(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

    def __str__(self) -> str:
        if self._text is not None:
            return self._text
        else:
            return str(self._value)
        
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
                