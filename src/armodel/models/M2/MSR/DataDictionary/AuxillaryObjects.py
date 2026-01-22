from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class SwAddrMethod(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.memoryAllocationKeywordPolicy = None   # type: ARLiteral
        self.options = []                            # type: List[ARLiteral]
        self.sectionInitializationPolicy = None     # type: ARLiteral
        self.sectionType = None                     # type: ARLiteral

    def getMemoryAllocationKeywordPolicy(self):
        return self.memoryAllocationKeywordPolicy

    def setMemoryAllocationKeywordPolicy(self, value):
        self.memoryAllocationKeywordPolicy = value
        return self

    def getOptions(self):
        return self.options

    def addOption(self, value):
        self.options.append(value)
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
