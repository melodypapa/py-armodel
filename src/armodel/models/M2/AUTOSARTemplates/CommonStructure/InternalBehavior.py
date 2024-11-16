from abc import ABCMeta
from enum import Enum
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype

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


class InternalBehavior(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == InternalBehavior:
            raise NotImplementedError("InternalBehavior is an abstract class.")
        super().__init__(parent, short_name)

        self.data_type_mapping_refs = []        # type: List[RefType]                       
        self.constant_memories = []             # type: List[ParameterDataPrototype]

    def addDataTypeMappingRef(self, ref: RefType):
        self.data_type_mapping_refs.append(ref)

    def getDataTypeMappingRefs(self) -> List[RefType]:
        return self.data_type_mapping_refs

    def createExclusiveArea(self, short_name: str) -> ExclusiveArea:
        if (short_name not in self.elements):
            event = ExclusiveArea(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getExclusiveAreas(self) -> List[ExclusiveArea]:
        return list(filter(lambda c: isinstance(c, ExclusiveArea), self.elements.values()))

    def createConstantMemory(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.constant_memories.append(prototype)
        return self.elements[short_name]

    def getConstantMemorys(self) -> List[ParameterDataPrototype]:
        return self.constant_memories