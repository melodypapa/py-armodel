from typing import List
from abc import ABCMeta
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ......M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint

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


class ExecutionOrderConstraint(TimingConstraint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ordered_elements = []                      # type: List[EOCExecutableEntityRefAbstract]

    def createEOCExecutableEntityRef(self, short_name: str)-> EOCExecutableEntityRef:
        if not self.IsElementExists(short_name):
            entity_ref = EOCExecutableEntityRef(self, short_name)
            self.addElement(entity_ref)
            self.ordered_elements.append(entity_ref)
        return self.getElement(short_name, EOCExecutableEntityRef)

    def getOrderedElements(self) -> List[EOCExecutableEntityRefAbstract]:
        return self.ordered_elements