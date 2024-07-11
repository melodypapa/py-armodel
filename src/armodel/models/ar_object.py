from abc import ABCMeta
from typing import List

class ARObject(metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("ARObject is an abstract class.")
        
        self.parent = None              # type: ARObject
        self.checksum = None            # type: str

        self.timestamp = None           # type: str
        self.uuid = None                # type: str


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

class LLongName(ARObject):
    def __init__(self):
        super().__init__()

        self.l = ""
        self.value = ""

class MultilanguageLongName(ARObject):
    def __init__(self):
        super().__init__()

        self.l4 = []        # type：List[LLongName]

    def add_l4(self, l4: LLongName):
        self.l4.append(l4)

    def get_l4s(self) -> List[LLongName]:
        return self.l4