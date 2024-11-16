
from typing import List
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class LLongName(ARObject):
    def __init__(self):
        super().__init__()

        self.l = ""
        self.value = ""

class LOverviewParagraph(ARObject):
    def __init__(self):
        super().__init__()

        self.l = ""
        self.value = ""

class MultilanguageLongName(ARObject):
    def __init__(self):
        super().__init__()

        self.l4 = []        # type：List[LLongName]

    def addL4(self, l4: LLongName):
        self.l4.append(l4)
        return self

    def getL4s(self) -> List[LLongName]:
        return self.l4
    
class MultiLanguageParagraph(ARObject):
    def __init__(self):
        super().__init__()

        self.l1 = []        # type: List[LLongName]

    def addL1(self, l1: LLongName):
        self.l1.append(l1)
        return self
    
    def getL1s(self) -> List[LLongName]:
        return self.l1

class MultiLanguageOverviewParagraph(ARObject):
    def __init__(self):
        super().__init__()

        self.l2 = []                # type: List[str]

    def addL2(self, l2: LOverviewParagraph):
        self.l2.append(l2)
        return self

    def getL2s(self) -> List[LOverviewParagraph]:
        return self.l2