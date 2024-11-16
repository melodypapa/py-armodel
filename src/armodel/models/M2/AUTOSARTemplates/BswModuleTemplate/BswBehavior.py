from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..CommonStructure.InternalBehavior import ReentrancyLevelEnum
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from ....ar_ref import RefType
from ....common_structure import ExecutableEntity
from ....general_structure import Referrable
from abc import ABCMeta
from typing import List

class BswModuleCallPoint(Referrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.contextLimitationRefs = []                 # type: List[RefType]

    def getContextLimitationRefs(self):
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        self.contextLimitationRefs.append(value)
        return self

class BswModuleEntity(ExecutableEntity, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswModuleEntity:
            raise NotImplementedError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        self.accessedModeGroupRefs = []                 # type: List[RefType]
        self.activationPointRefs = []                   # type: List[RefType]
        self.callPoints = []                            # type: List[BswModuleCallPoint]
        self.canEnterRefs = []                          # type: List[RefType]
        self.exclusiveAreaNestingOrderRefs = []         # type: List[RefType]
        self.minimumStartInterval = None                # type: TimeValue
        self.reentrancyLevel = None                     # type: ReentrancyLevelEnum
        self.implementedEntryRef = None                 # type: RefType
        self.managedModeGroupRefs = []                  # type: List[RefType]

    def getAccessedModeGroupRefs(self):
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRefs(self, value):
        self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        return self.activationPointRefs

    def addActivationPointRefs(self, value):
        self.activationPointRefs.append(value)
        return self

    def getImplementedEntryRef(self):
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        self.implementedEntryRef = value
        return self

    def addManagedModeGroupRef(self, ref: RefType):
        self.managedModeGroupRefs.append(ref)

    def getManagedModeGroupRefs(self) -> List[RefType]:
        return self.managedModeGroupRefs