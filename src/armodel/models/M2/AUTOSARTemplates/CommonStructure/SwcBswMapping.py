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

        self.bswEntityRef   = None        # type: RefType
        self.swcRunnableRef = None        # type: RefType


class SwcBswMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bswBehaviorRef = None              # type: RefType
        self._runnableMappings = []
        self.swcBehaviorRef = None              # type: RefType
        self.synchronizedModeGroups = []
        self.synchronizedTriggers = []

    def addRunnableMapping(self, mapping: SwcBswRunnableMapping):
        self._runnableMappings.append(mapping)

    def getRunnableMappings(self) -> List[SwcBswRunnableMapping]:
        return self._runnableMappings