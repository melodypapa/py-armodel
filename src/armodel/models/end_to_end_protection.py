from typing import List

from .ar_ref import VariableDataPrototypeInSystemInstanceRef
from .ar_object import ARObject
from .general_structure import Identifiable


class EndToEndDescription(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                # type: str
        self.counterOffset = None           # type: int
        self.crcOffset = None               # type: int
        self.dataIds = []                   # type: List[int]
        self.dataIdMode = None              # type: int
        self.dataIdNibbleOffset = None      # type: int
        self.dataLength = None              # type: int
        self.maxDeltaCounterInit = None     # type: int
        self.maxNoNewOrRepeatedData = None  # type: int
        self.syncCounterInit = None         # type: int

    def addDataId(self, id: int):
        self.dataIds.append(id)
    
    def getDataIds(self) -> List[int]:
        return sorted(self.dataIds, key = lambda a: a) 

class EndToEndProtectionVariablePrototype(ARObject):
    def __init__(self):
        super().__init__()

        self._receiverIRefs = []            # type: List[VariableDataPrototypeInSystemInstanceRef]
        self.senderIRefs = None             # type: VariableDataPrototypeInSystemInstanceRef
        self.shortLabel = None              # type: str

class EndToEndProtection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.endToEndProfile = None                         # type: EndToEndDescription
        self.endToEndProtectionVariablePrototype = []       # type: List[EndToEndProtectionVariablePrototype]

class EndToEndProtectionSet(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createEndToEndProtection(self, short_name: str) -> EndToEndProtection:
        if (short_name not in self.elements):
            protection = EndToEndProtection(self, short_name)
            self.elements[short_name] = protection
        return self.elements[short_name]
    
    def getEndToEndProtections(self) -> List[EndToEndProtection]:
        return sorted(filter(lambda c: isinstance(c, EndToEndProtection), self.elements.values()), key= lambda e: e.short_name)