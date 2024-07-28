
from typing import List
from .ar_object import ARObject


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

    def getL4s(self) -> List[LLongName]:
        return self.l4

class MultiLanguageOverviewParagraph(ARObject):
    def __init__(self):
        super().__init__()

        self.l2 = []                # type: List[str]

    def addL2(self, l2: LOverviewParagraph):
        self.l2.append(l2)

    def getL2s(self) -> List[LOverviewParagraph]:
        return self.l2