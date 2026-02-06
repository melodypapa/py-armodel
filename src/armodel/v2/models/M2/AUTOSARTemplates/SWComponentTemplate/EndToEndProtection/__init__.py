"""
This module contains classes for representing AUTOSAR end-to-end protection
mechanisms in the SWComponentTemplate module. It includes classes for
defining end-to-end protection profiles, variables, and protection sets
used to ensure data integrity in communication systems.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    NameToken,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    VariableDataPrototypeInSystemInstanceRef,
)


class EndToEndDescription(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.category: NameToken = None
        self.counterOffset: PositiveInteger = None
        self.crcOffset: PositiveInteger = None
        self.dataIds: List[PositiveInteger] = []
        self.dataIdMode: PositiveInteger = None
        self.dataIdNibbleOffset: PositiveInteger = None
        self.dataLength: PositiveInteger = None
        self.maxDeltaCounterInit: PositiveInteger = None
        self.maxNoNewOrRepeatedData: int = None
        self.syncCounterInit: PositiveInteger = None

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
        # return sorted(self.dataIds, key = lambda a: a.getValue())
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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self._receiverIRefs: List[VariableDataPrototypeInSystemInstanceRef] = []
        self.senderIRef: VariableDataPrototypeInSystemInstanceRef = None
        self.shortLabel: str = None

    def addReceiverIref(self, iref: VariableDataPrototypeInSystemInstanceRef):
        self._receiverIRefs.append(iref)

    def getReceiverIrefs(self) -> List[VariableDataPrototypeInSystemInstanceRef]:
        return self._receiverIRefs


class EndToEndProtectionISignalIPdu(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.dataOffset: Integer = None
        self.iSignalGroupRef: RefType = None
        self.iSignalIPduRef: RefType = None

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

        self.endToEndProfile: EndToEndDescription = None
        self.endToEndProtectionISignalIPdus: List[EndToEndProtectionISignalIPdu] = []
        self.endToEndProtectionVariablePrototypes: List[EndToEndProtectionVariablePrototype] = []

    def getEndToEndProfile(self):
        return self.endToEndProfile

    def setEndToEndProfile(self, value):
        if value is not None:
            self.endToEndProfile = value
        return self

    def getEndToEndProtectionISignalIPdus(self):
        return self.endToEndProtectionISignalIPdus

    def addEndToEndProtectionISignalIPdu(self, value):
        if value is not None:
            self.endToEndProtectionISignalIPdus.append(value)
        return self

    def getEndToEndProtectionVariablePrototypes(self) -> List[EndToEndProtectionVariablePrototype]:
        return self.endToEndProtectionVariablePrototypes

    def addEndToEndProtectionVariablePrototype(self, value: EndToEndProtectionVariablePrototype):
        if value is not None:
            self.endToEndProtectionVariablePrototypes.append(value)
        return self


class EndToEndProtectionSet(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createEndToEndProtection(self, short_name: str) -> EndToEndProtection:
        if not self.IsElementExists(short_name):
            protection = EndToEndProtection(self, short_name)
            self.addElement(protection)
        return self.getElement(short_name, EndToEndProtection)

    def getEndToEndProtections(self) -> List[EndToEndProtection]:
        return sorted(filter(lambda c: isinstance(c, EndToEndProtection), self.elements), key=lambda e: e.short_name)


__all__ = [
    'EndToEndDescription',
    'EndToEndProtectionVariablePrototype',
    'EndToEndProtectionISignalIPdu',
    'EndToEndProtection',
    'EndToEndProtectionSet',
]
