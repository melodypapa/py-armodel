from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName


from typing import List


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


class MultilanguageLongName(ARObject):
    def __init__(self):
        super().__init__()

        self.l4 = []        # type：List[LLongName]

    def addL4(self, l4: LLongName):
        self.l4.append(l4)
        return self

    def getL4s(self) -> List[LLongName]:
        return self.l4