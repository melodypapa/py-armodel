from abc import ABCMeta
from enum import Enum
from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype

class ReentrancyLevelEnum(Enum):
    ENUM_MULTICORE_REENTRANT = "multicoreReentrant"
    ENUM_NON_REENTRANT = "nonReentrant"
    ENUM_SINGLE_CORE_REENTRANT = "singleCoreReentrant"

class ExclusiveArea(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ExecutableEntity(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ExecutableEntity:
            raise NotImplementedError("ExecutableEntity is an abstract class.")

        super().__init__(parent, short_name)

        self.activationReasons = []                 # type: List[ExecutableEntityActivationReason]
        self.canEnterExclusiveAreaRefs = []         # type: List[RefType]  
        self.minimumStartInterval = None            # type: ARFloat
        self.reentrancyLevel = None                 # 
        
        self.swAddrMethodRef = None                 # type: RefType

    def getActivationReasons(self):
        return self.activationReasons

    def addActivationReason(self, value):
        self.activationReasons.append(value)
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

        self.constantMemories = []                          # type: List[ParameterDataPrototype]
        self.constantValueMappingRefs = []                  # type: List[RefType]
        self.dataTypeMappingRefs = []                       # type: List[RefType]
        self.exclusiveAreas = []                            # type: List[ExclusiveArea]
        self.exclusiveAreaNestingOrders = []                # type: List[ExclusiveAreaNestingOrder]
        self.staticMemories = []                            # type: List[VariableDataPrototype]

    def createConstantMemory(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.constantMemories.append(prototype)
        return self.getElement(short_name)

    def getConstantMemories(self) -> List[ParameterDataPrototype]:
        return self.constantMemories

    def addDataTypeMappingRef(self, ref: RefType):
        self.dataTypeMappingRefs.append(ref)

    def getDataTypeMappingRefs(self) -> List[RefType]:
        return self.dataTypeMappingRefs

    def createExclusiveArea(self, short_name: str) -> ExclusiveArea:
        if (short_name not in self.elements):
            area = ExclusiveArea(self, short_name)
            self.addElement(area)
            self.exclusiveAreas.append(area)
        return self.getElement(short_name)

    def getExclusiveAreas(self) -> List[ExclusiveArea]:
        return list(filter(lambda c: isinstance(c, ExclusiveArea), self.elements.values()))
    
    def getStaticMemories(self):
        return self.staticMemories

    def createStaticMemory(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.staticMemories.append(prototype)
        return self.getElement(short_name)

class AbstractEvent(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.activationReasonRepresentationRef = None                       # type: RefType

    def getActivationReasonRepresentationRef(self):
        return self.activationReasonRepresentationRef

    def setActivationReasonRepresentationRef(self, value):
        self.activationReasonRepresentationRef = value
        return self
