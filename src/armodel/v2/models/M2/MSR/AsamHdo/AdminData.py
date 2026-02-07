from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    NameToken,
    RevisionLabelString,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
    MultiLanguagePlainText,
)


class Modification(ARObject):
    """
    Represents a modification made to a document.
    Base: ARObject
    Aggregated by: DocRevision.modifications
    """

    def __init__(self) -> None:
        super().__init__()

        self.change: Union[Union[MultiLanguageOverviewParagraph, None] , None] = None
        self.reason: Union[Union[MultiLanguageOverviewParagraph, None] , None] = None

    def getChange(self) -> Union[MultiLanguageOverviewParagraph, None]:
        return self.change

    def setChange(self, value: MultiLanguageOverviewParagraph) -> "Modification":
        if value is not None:
            self.change = value
        return self

    def getReason(self) -> Union[MultiLanguageOverviewParagraph, None]:
        return self.reason

    def setReason(self, value: MultiLanguageOverviewParagraph) -> "Modification":
        if value is not None:
            self.reason = value
        return self


class DocRevision(ARObject):
    """
    Represents a single revision of a document with metadata.
    Base: ARObject
    Aggregated by: AdminData.DocRevisions
    """

    def __init__(self) -> None:
        super().__init__()

        self.date: Union[Union[DateTime, None] , None] = None
        self.issuedBy: Union[Union[String, None] , None] = None
        self.modifications: List[Modification] = []
        self.revisionLabel: Union[Union[RevisionLabelString, None] , None] = None
        self.revisionLabelP1: Union[Union[RevisionLabelString, None] , None] = None
        self.revisionLabelP2: Union[Union[RevisionLabelString, None] , None] = None
        self.state: Union[Union[NameToken, None] , None] = None

    def getDate(self) -> Union[DateTime, None]:
        return self.date

    def setDate(self, value: DateTime) -> "DocRevision":
        if value is not None:
            self.date = value
        return self

    def getIssuedBy(self) -> Union[String, None]:
        return self.issuedBy

    def setIssuedBy(self, value: String) -> "DocRevision":
        if value is not None:
            self.issuedBy = value
        return self

    def getModifications(self) -> List[Modification]:
        return self.modifications

    def addModification(self, value: Modification) -> "DocRevision":
        if value is not None:
            self.modifications.append(value)
        return self

    def getRevisionLabel(self) -> Union[RevisionLabelString, None]:
        return self.revisionLabel

    def setRevisionLabel(self, value: RevisionLabelString) -> "DocRevision":
        if value is not None:
            self.revisionLabel = value
        return self

    def getRevisionLabelP1(self) -> Union[RevisionLabelString, None]:
        return self.revisionLabelP1

    def setRevisionLabelP1(self, value: RevisionLabelString) -> "DocRevision":
        if value is not None:
            self.revisionLabelP1 = value
        return self

    def getRevisionLabelP2(self) -> Union[RevisionLabelString, None]:
        return self.revisionLabelP2

    def setRevisionLabelP2(self, value: RevisionLabelString) -> "DocRevision":
        if value is not None:
            self.revisionLabelP2 = value
        return self

    def getState(self) -> Union[NameToken, None]:
        return self.state

    def setState(self, value: NameToken) -> "DocRevision":
        if value is not None:
            self.state = value
        return self


class AdminData(ARObject):
    """
    Container for administrative data including document revisions and language settings.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.DocRevisions: List[DocRevision] = []
        self.language: Union[Union[LEnum, None] , None] = None
        self.sdgs: List = []
        self.usedLanguages: Union[Union[MultiLanguagePlainText, None] , None] = None

    def getDocRevisions(self) -> List[DocRevision]:
        return self.DocRevisions

    def addDocRevision(self, value: DocRevision) -> "AdminData":
        self.DocRevisions.append(value)
        return self

    def getLanguage(self) -> Union[LEnum, None]:
        return self.language

    def setLanguage(self, value: LEnum) -> "AdminData":
        self.language = value
        return self

    def getSdgs(self) -> List:
        return self.sdgs

    def addSdg(self, value) -> "AdminData":
        self.sdgs.append(value)
        return self

    def getUsedLanguages(self) -> Union[MultiLanguagePlainText, None]:
        return self.usedLanguages

    def setUsedLanguages(self, value: MultiLanguagePlainText) -> "AdminData":
        self.usedLanguages = value
        return self
