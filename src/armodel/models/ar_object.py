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

class ARBoolean(ARType):
    def __init__(self) -> None:
        super().__init__()              

        self.value = ""                 # type: bool
class ARLiteral(ARType):
    def __init__(self) -> None:
        super().__init__()              

        self.value = ""                 # type: str

class ARNumerical(ARType):
    def __init__(self) -> None:
        super().__init__()

        self.text = None                # type: str

    def _convertStringToNumberValue(self, value: str) -> int:
        m = re.match(r"0x([0-9a-f]+)", value, re.I)
        if (m):
            return int(m.group(1), 16)
        return int(value)

    @property
    def value(self) -> int:
        if self.text is not None:
            return self._convertStringToNumberValue(self.text)
        return None
    
class ARPositiveInteger(ARNumerical):
    def __init__(self) -> None:
        super().__init__()

    @property
    def text(self) -> str:
        return ARNumerical.text
    
    @text.setter
    def text(self, value: str):
        ARNumerical.text = value

        if ARNumerical.value < 0:
            raise ValueError("Invalid Positiive Integer <%s>" % value)

class ARFloat(ARType):
    def __init__(self) -> None:
        super().__init__()

        self.text = None                # type: str

    @property
    def value(self) -> float:
        if self.text is not None:
            return float(self.text)
        return None

