from typing import List

from .M2.AUTOSARTemplates.system_template.instance_refs import VariableDataPrototypeInSystemInstanceRef
from .ar_object import ARNumerical, ARObject
from .general_structure import Identifiable


class EndToEndDescription(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                # type: str
        self.counterOffset = None           # type: int
        self.crcOffset = None               # type: int
        self.dataIds = []                   # type: List[ARNumerical]
        self.dataIdMode = None              # type: int
        self.dataIdNibbleOffset = None      # type: int
        self.dataLength = None              # type: int
        self.maxDeltaCounterInit = None     # type: int
        self.maxNoNewOrRepeatedData = None  # type: int
        self.syncCounterInit = None         # type: int

    def addDataId(self, id: ARNumerical):
        self.dataIds.append(id)
    
    def getDataIds(self) -> List[ARNumerical]:
        return sorted(self.dataIds, key = lambda a: a) 

class EndToEndProtectionVariablePrototype(ARObject):
    def __init__(self):
        super().__init__()

        self._receiverIRefs = []            # type: List[VariableDataPrototypeInSystemInstanceRef]
        self.senderIRef = None             # type: VariableDataPrototypeInSystemInstanceRef
        self.shortLabel = None              # type: str

    def addReceiverIref(self, iref: VariableDataPrototypeInSystemInstanceRef):
        self._receiverIRefs.append(iref)

    def getReceiverIrefs(self) -> List[VariableDataPrototypeInSystemInstanceRef]:
        return self._receiverIRefs

class EndToEndProtection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.endToEndProfile = None                         # type: EndToEndDescription
        self.endToEndProtectionVariablePrototype = []       # type: List[EndToEndProtectionVariablePrototype]

    def addEndToEndProtectionVariablePrototype(self, prototype: EndToEndProtectionVariablePrototype):
        self.endToEndProtectionVariablePrototype.append(prototype)

    def getEndToEndProtectionVariablePrototypes(self) -> List[EndToEndProtectionVariablePrototype]:
        return self.endToEndProtectionVariablePrototype

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