from typing import List
from ....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DocumentationBlock(ARObject):
    def __init__(self):
        super().__init__()

        self.ps = []               # type: List[MultiLanguageParagraph]

    def addP(self, p: MultiLanguageParagraph):
        self.ps.append(p)
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        return self.ps

    