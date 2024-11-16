
from typing import List

from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....ar_object import ARLiteral
from ....general_structure import Identifiable


class SwAddrMethod(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.memoryAllocationKeywordPolicy = None   # type: ARLiteral
        self.option = []                            # type: List[ARLiteral]
        self.sectionInitializationPolicy = None     # type: ARLiteral
        self.sectionType = None                     # type: ARLiteral

    def getMemoryAllocationKeywordPolicy(self):
        return self.memoryAllocationKeywordPolicy

    def setMemoryAllocationKeywordPolicy(self, value):
        self.memoryAllocationKeywordPolicy = value
        return self

    def getOption(self):
        return self.option

    def addOption(self, value):
        self.option.append(value)
        return self

    def getSectionInitializationPolicy(self):
        return self.sectionInitializationPolicy

    def setSectionInitializationPolicy(self, value):
        self.sectionInitializationPolicy = value
        return self

    def getSectionType(self):
        return self.sectionType

    def setSectionType(self, value):
        self.sectionType = value
        return self
