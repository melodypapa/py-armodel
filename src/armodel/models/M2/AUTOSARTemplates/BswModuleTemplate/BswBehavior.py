from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..CommonStructure.InternalBehavior import ReentrancyLevelEnum
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from ....ar_ref import RefType
from ....common_structure import ExecutableEntity
from ..GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from abc import ABCMeta
from typing import List

class BswModuleCallPoint(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.contextLimitationRefs = []                 # type: List[RefType]

    def getContextLimitationRefs(self):
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        self.contextLimitationRefs.append(value)
        return self
    
class BswVariableAccess(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedVariableRef = None                     # type: RefType
        self.contextLimitationRefs = []                     # type: List[RefType]

    def getAccessedVariableRef(self):
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value):
        self.accessedVariableRef = value
        return self

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
        self.dataReceivePoints = []                     # type: List[BswVariableAccess]
        self.dataSendPoints = []                        # type: List[BswVariableAccess]
        self.implementedEntryRef = None                 # type: RefType
        self.issuedTriggerRefs = []                     # type: List[RefType]
        self.managedModeGroupRefs = []                  # type: List[RefType]
        self.schedulerNamePrefixRef = None              # type: List[RefType]
    
    def getAccessedModeGroupRefs(self):
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRef(self, value):
        self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        return self.activationPointRefs

    def addActivationPointRef(self, value):
        self.activationPointRefs.append(value)
        return self

    def getCallPoints(self):
        return self.callPoints

    def addCallPoint(self, value):
        self.callPoints.append(value)
        return self

    def getDataReceivePoint(self):
        return self.dataReceivePoints

    def addDataReceivePoint(self, value):
        self.dataReceivePoints.append(value)
        return self

    def getDataSendPoints(self):
        return self.dataSendPoints

    def addDataSendPoint(self, value):
        self.dataSendPoints.append(value)
        return self

    def getImplementedEntryRef(self):
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        self.implementedEntryRef = value
        return self

    def getIssuedTriggerRefs(self):
        return self.issuedTriggerRefs

    def addIssuedTriggerRefs(self, value):
        self.issuedTriggerRefs(value)
        return self

    def getManagedModeGroupRefs(self):
        return self.managedModeGroupRefs

    def addManagedModeGroupRef(self, value):
        self.managedModeGroupRefs = value
        return self

    def getSchedulerNamePrefixRef(self):
        return self.schedulerNamePrefixRef

    def setSchedulerNamePrefixRef(self, value):
        self.schedulerNamePrefixRef = value
        return self

    