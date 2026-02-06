from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
)


class MultiLanguageParagraph(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.l1 = []        # type: List[LLongName]

    def addL1(self, l1: LLongName):
        self.l1.append(l1)
        return self

    def getL1s(self) -> List[LLongName]:
        return self.l1


class MultiLanguageOverviewParagraph(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.l2 = []                # type: List[str]

    def addL2(self, l2: LOverviewParagraph):
        self.l2.append(l2)
        return self

    def getL2s(self) -> List[LOverviewParagraph]:
        return self.l2


class MultilanguageLongName(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.l4 = []                            # type：List[LLongName]

    def addL4(self, l4: LLongName):
        self.l4.append(l4)
        return self

    def getL4s(self) -> List[LLongName]:
        return self.l4

class MultiLanguagePlainText(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.l10s = []                       # type: List[LPlainText]

    def getL10s(self):
        return self.l10s

    def addL10(self, value):
        self.l10s.append(value)
        return self
