from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwAddrMethod(AtpBlueprintable):
    """
    Software address method defining memory allocation properties for data
    elements, including initialization policy, section type, and memory
    allocation keyword policy.
    """
    # SwAddrMethod method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMemoryAllocationKeywordPolicy [x] impl  [ ] docstring  [ ] test
    # [ ] setMemoryAllocationKeywordPolicy [x] impl  [ ] docstring  [ ] test
    # [ ] getOptions                   [x] impl  [ ] docstring  [ ] test
    # [ ] addOption                    [x] impl  [ ] docstring  [ ] test
    # [ ] getSectionInitializationPolicy [x] impl  [ ] docstring  [ ] test
    # [ ] setSectionInitializationPolicy [x] impl  [ ] docstring  [ ] test
    # [ ] getSectionType               [x] impl  [ ] docstring  [ ] test
    # [ ] setSectionType               [x] impl  [ ] docstring  [ ] test

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
