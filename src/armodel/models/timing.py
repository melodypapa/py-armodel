
from abc import ABCMeta
from typing import List

from armodel.models.ar_ref import RefType

from ..models.general_structure import Identifiable
from ..models.ar_object import ARObject

class EOCExecutableEntityRefAbstract(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingConstraint:
            raise NotImplementedError("TimingExtension is an abstract class.")
        
        super().__init__(parent, short_name)
        
class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.successor_refs = []            # List[RefType]

    def addSuccessorRef(self, ref: RefType):
        self.successor_refs.append(ref)

    def getSuccessorRefs(self) -> List[RefType]:
        return self.successor_refs

class TimingConstraint(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingConstraint:
            raise NotImplementedError("TimingExtension is an abstract class.")
        
        super().__init__(parent, short_name)

        self.timing_condition_ref = None                # type: RefType

    @property
    def timingConditionRef(self) -> RefType:
        return self.timing_condition_ref

    @timingConditionRef.setter
    def timingConditionRef(self, ref: RefType):
        self.timing_condition_ref = ref

class ExecutionOrderConstraint(TimingConstraint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ordered_elements = []                      # type: List[EOCExecutableEntityRefAbstract]

    def createEOCExecutableEntityRef(self, short_name: str)-> EOCExecutableEntityRef:
        if short_name not in self.elements:
            entity_ref = EOCExecutableEntityRef(self, short_name)
            self.elements[short_name] = entity_ref
            self.ordered_elements.append(entity_ref)
        return self.elements[short_name]

    def getOrderedElements(self) -> List[EOCExecutableEntityRefAbstract]:
        return self.ordered_elements

class TimingExtension(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingExtension:
            raise NotImplementedError("TimingExtension is an abstract class.")
        
        super().__init__(parent, short_name)

        self.timing_requirements = []           # Type: List[TimingConstraint]

    def createExecutionOrderConstraint(self, short_name: str)-> ExecutionOrderConstraint:
        if short_name not in self.elements:
            constraint = ExecutionOrderConstraint(self, short_name)
            self.elements[short_name] = constraint
            self.timing_requirements.append(constraint)
        return self.elements[short_name]

    def getTimingRequirements(self) -> List[TimingConstraint]:
        return self.timing_requirements

class SwcTiming(TimingExtension):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    
