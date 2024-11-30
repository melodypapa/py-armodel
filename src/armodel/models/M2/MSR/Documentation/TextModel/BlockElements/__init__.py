from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.MSR.Documentation.TextModel.BlockElements.ListElements import ListElement
from ......M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from typing import List

class DocumentationBlock(ARObject):
    def __init__(self):
        super().__init__()

        self.ps = []                                # type: List[MultiLanguageParagraph]
        self.lists = []                             # type: List[ListElement]

    def addP(self, p: MultiLanguageParagraph):
        self.ps.append(p)
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        return self.ps
    
    def getLists(self):
        return self.lists

    def addList(self, value):
        self.lists.append(value)
        return self
