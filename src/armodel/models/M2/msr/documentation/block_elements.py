from typing import List
from .....models.multilanguage_data import MultiLanguageParagraph
from .....models.ar_object import ARObject

class DocumentationBlock(ARObject):
    def __init__(self):
        super().__init__()

        self.ps = []               # type: List[MultiLanguageParagraph]

    def addP(self, p: MultiLanguageParagraph):
        self.ps.append(p)
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        return self.ps

    