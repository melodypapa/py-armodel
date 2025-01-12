from ..GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, NameToken, PositiveInteger, RefType
from ..SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from typing import List

class EndToEndDescription(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                # type: NameToken
        self.counterOffset = None           # type: PositiveInteger
        self.crcOffset = None               # type: PositiveInteger
        self.dataIds = []                   # type: List[PositiveInteger]
        self.dataIdMode = None              # type: PositiveInteger
        self.dataIdNibbleOffset = None      # type: PositiveInteger
        self.dataLength = None              # type: PositiveInteger
        self.maxDeltaCounterInit = None     # type: PositiveInteger
        self.maxNoNewOrRepeatedData = None  # type: int
        self.syncCounterInit = None         # type: PositiveInteger

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value
        return self

    def getCounterOffset(self):
        return self.counterOffset

    def setCounterOffset(self, value):
        self.counterOffset = value
        return self

    def getCrcOffset(self):
        return self.crcOffset

    def setCrcOffset(self, value):
        self.crcOffset = value
        return self

    def getDataIds(self) -> List[PositiveInteger]:
        #return sorted(self.dataIds, key = lambda a: a.getValue())
        return self.dataIds

    def addDataId(self, id: PositiveInteger):
        self.dataIds.append(id)
        return self

    def getDataIdMode(self):
        return self.dataIdMode

    def setDataIdMode(self, value):
        self.dataIdMode = value
        return self

    def getDataIdNibbleOffset(self):
        return self.dataIdNibbleOffset

    def setDataIdNibbleOffset(self, value):
        self.dataIdNibbleOffset = value
        return self

    def getDataLength(self):
        return self.dataLength

    def setDataLength(self, value):
        self.dataLength = value
        return self

    def getMaxDeltaCounterInit(self):
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value):
        self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        self.maxNoNewOrRepeatedData = value
        return self

    def getSyncCounterInit(self):
        return self.syncCounterInit

    def setSyncCounterInit(self, value):
        self.syncCounterInit = value
        return self


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

class EndToEndProtectionISignalIPdu(ARObject):
    def __init__(self):
        super().__init__()

        self.dataOffset = None                              # type: Integer
        self.iSignalGroupRef = None                         # type: RefType
        self.iSignalIPduRef = None                          # type: RefType

    def getDataOffset(self):
        return self.dataOffset

    def setDataOffset(self, value):
        self.dataOffset = value
        return self

    def getISignalGroupRef(self):
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        self.iSignalGroupRef = value
        return self

    def getISignalIPduRef(self):
        return self.iSignalIPduRef

    def setISignalIPduRef(self, value):
        self.iSignalIPduRef = value
        return self


class EndToEndProtection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.endToEndProfile = None                         # type: EndToEndDescription
        self.endToEndProtectionISignalIPdus = []            # type: List[EndToEndProtectionISignalIPdu]
        self.endToEndProtectionVariablePrototypes = []      # type: List[EndToEndProtectionVariablePrototype]

    def getEndToEndProfile(self):
        return self.endToEndProfile

    def setEndToEndProfile(self, value):
        self.endToEndProfile = value
        return self

    def getEndToEndProtectionISignalIPdus(self):
        return self.endToEndProtectionISignalIPdus

    def addEndToEndProtectionISignalIPdu(self, value):
        self.endToEndProtectionISignalIPdus.append(value)
        return self

    def getEndToEndProtectionVariablePrototypes(self) -> List[EndToEndProtectionVariablePrototype]:
        return self.endToEndProtectionVariablePrototypes
    
    def addEndToEndProtectionVariablePrototype(self, prototype: EndToEndProtectionVariablePrototype):
        self.endToEndProtectionVariablePrototypes.append(prototype)


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