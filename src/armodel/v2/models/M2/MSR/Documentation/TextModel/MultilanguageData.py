"""
This module defines multilingual data classes for AUTOSAR documentation.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
    LLongName,
    LOverviewParagraph,
    LPlainText,
)


class PgwideEnum(AREnum):
    def __init__(self) -> None:
        super().__init__(["0", "1"])


class Caption(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.llong_names: List[LLongName] = []

    def addL(self, long_name: LLongName) -> "Caption":
        self.llong_names.append(long_name)
        return self

    def getLs(self) -> List[LLongName]:
        return self.llong_names


class MultiLanguageParagraph(Paginateable):
    def __init__(self) -> None:
        super().__init__()

        self.l1 = []        # type: List[LLongName]

    def addL1(self, l1: LLongName) -> "MultiLanguageParagraph":
        self.l1.append(l1)
        return self

    def getL1s(self) -> List[LLongName]:
        return self.l1


class MultiLanguageOverviewParagraph(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.l2: List[LOverviewParagraph] = []

    def addL2(self, l2: LOverviewParagraph) -> "MultiLanguageOverviewParagraph":
        self.l2.append(l2)
        return self

    def getL2s(self) -> List[LOverviewParagraph]:
        return self.l2


class MultilanguageLongName(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.l4: List[LLongName] = []

    def addL4(self, l4: LLongName) -> "MultilanguageLongName":
        self.l4.append(l4)
        return self

    def getL4s(self) -> List[LLongName]:
        return self.l4

class MultiLanguagePlainText(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.l10s = []                       # type: List[LPlainText]

    def getL10s(self) -> List[LPlainText]:
        return self.l10s

    def addL10(self, value: LPlainText) -> "MultiLanguagePlainText":
        self.l10s.append(value)
        return self


class L5(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()


class MultiLanguageVerbatim(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.l5s: List[L5] = []
        self.allowBreak: Union[bool, None] = None
        self.float: Union[bool, None] = None
        self.helpEntry: Union[String, None] = None
        self.pgwide: Union[String, None] = None

    def getL5s(self) -> List[L5]:
        return self.l5s

    def addL5(self, value: L5) -> "MultiLanguageVerbatim":
        self.l5s.append(value)
        return self

    def getAllowBreak(self) -> Union[bool, None]:
        return self.allowBreak

    def setAllowBreak(self, value: bool) -> "MultiLanguageVerbatim":
        self.allowBreak = value
        return self

    def getFloat(self) -> Union[bool, None]:
        return self.float

    def setFloat(self, value: bool) -> "MultiLanguageVerbatim":
        self.float = value
        return self

    def getHelpEntry(self) -> Union[String, None]:
        return self.helpEntry

    def setHelpEntry(self, value: String) -> "MultiLanguageVerbatim":
        self.helpEntry = value
        return self

    def getPgwide(self) -> Union[String, None]:
        return self.pgwide

    def setPgwide(self, value: String) -> "MultiLanguageVerbatim":
        self.pgwide = value
        return self


__all__ = [
    'MultiLanguageParagraph',
    'MultiLanguageOverviewParagraph',
    'MultilanguageLongName',
    'MultiLanguagePlainText',
    'L5',
    'MultiLanguageVerbatim',
]
