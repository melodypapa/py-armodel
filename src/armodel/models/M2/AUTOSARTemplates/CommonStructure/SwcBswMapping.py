from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class SwcBswRunnableMapping(ARObject):
    def __init__(self):
        '''
            Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a BSW
            module (in the case of an AUTOSAR Service, a Complex Driver or an ECU
            Abstraction). The mapping can be used by a tool to find relevant information on the
            behavior, e.g. whether the bswEntity shall be running in interrupt context.

        '''
        super().__init__()

        self.bswEntityRef = None        # type: RefType
        self.swcRunnableRef = None        # type: RefType

    def getBswEntityRef(self):
        return self.bswEntityRef

    def setBswEntityRef(self, value):
        self.bswEntityRef = value
        return self

    def getSwcRunnableRef(self):
        return self.swcRunnableRef

    def setSwcRunnableRef(self, value):
        self.swcRunnableRef = value
        return self

class SwcBswMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bswBehaviorRef = None              # type: RefType
        self.runnableMappings = []              # type: List[SwcBswRunnableMapping]
        self.swcBehaviorRef = None              # type: RefType
        self.synchronizedModeGroups = []
        self.synchronizedTriggers = []

    def getBswBehaviorRef(self):
        return self.bswBehaviorRef

    def setBswBehaviorRef(self, value):
        self.bswBehaviorRef = value
        return self

    def getRunnableMappings(self):
        return self.runnableMappings

    def addRunnableMapping(self, value):
        self.runnableMappings.append(value)
        return self

    def getSwcBehaviorRef(self):
        return self.swcBehaviorRef

    def setSwcBehaviorRef(self, value):
        self.swcBehaviorRef = value
        return self

    def getSynchronizedModeGroups(self):
        return self.synchronizedModeGroups

    def setSynchronizedModeGroups(self, value):
        self.synchronizedModeGroups = value
        return self

    def getSynchronizedTriggers(self):
        return self.synchronizedTriggers

    def setSynchronizedTriggers(self, value):
        self.synchronizedTriggers = value
        return self
