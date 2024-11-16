from abc import ABCMeta
from enum import Enum
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType

class ReentrancyLevelEnum(Enum):

    multicoreReentrant = "multicoreReentrant"
    nonReentrant = "nonReentrant"
    singleCoreReentrant = "singleCoreReentrant"


class ExclusiveArea(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ExecutableEntity(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ExecutableEntity:
            raise NotImplementedError("ExecutableEntity is an abstract class.")

        super().__init__(parent, short_name)

        self.activationReason = None                # *
        self.minimumStartInterval = None            # type: ARFloat
        self.reentrancyLevel = None                 # 
        self.canEnterExclusiveAreaRefs = []         # type: List[RefType]  
        self.swAddrMethodRef = None                 # type: RefType

    def getActivationReason(self):
        return self.activationReason

    def setActivationReason(self, value):
        self.activationReason = value
        return self

    def getMinimumStartInterval(self):
        return self.minimumStartInterval

    def setMinimumStartInterval(self, value):
        self.minimumStartInterval = value
        return self

    def getReentrancyLevel(self):
        return self.reentrancyLevel

    def setReentrancyLevel(self, value):
        self.reentrancyLevel = value
        return self

    def getSwAddrMethodRef(self):
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        self.swAddrMethodRef = value
        return self

    @property
    def minimumStartIntervalMs(self) -> int:
        if self.minimumStartInterval is not None:
            return int(self.minimumStartInterval.getValue() * 1000)
        return None

    def addCanEnterExclusiveAreaRef(self, ref: RefType):
        self.canEnterExclusiveAreaRefs.append(ref)

    def getCanEnterExclusiveAreaRefs(self):
        return self.canEnterExclusiveAreaRefs