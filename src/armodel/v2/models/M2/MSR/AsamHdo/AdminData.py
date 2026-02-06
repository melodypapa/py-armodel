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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.change: Union[Union[MultiLanguageOverviewParagraph, None] , None] = None
        self.reason: Union[Union[MultiLanguageOverviewParagraph, None] , None] = None

    def getChange(self) -> MultiLanguageOverviewParagraph:
        return self.change

    def setChange(self, value: MultiLanguageOverviewParagraph):
        if value is not None:
            self.change = value
        return self

    def getReason(self) -> MultiLanguageOverviewParagraph:
        return self.reason

    def setReason(self, value: MultiLanguageOverviewParagraph):
        if value is not None:
            self.reason = value
        return self


class DocRevision(ARObject):
    """
    Represents a single revision of a document with metadata.
    Base: ARObject
    Aggregated by: AdminData.DocRevisions
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.date: Union[Union[DateTime, None] , None] = None
        self.issuedBy: Union[Union[String, None] , None] = None
        self.modifications: List[Modification] = []
        self.revisionLabel: Union[Union[RevisionLabelString, None] , None] = None
        self.revisionLabelP1: Union[Union[RevisionLabelString, None] , None] = None
        self.revisionLabelP2: Union[Union[RevisionLabelString, None] , None] = None
        self.state: Union[Union[NameToken, None] , None] = None

    def getDate(self) -> DateTime:
        return self.date

    def setDate(self, value: DateTime):
        if value is not None:
            self.date = value
        return self

    def getIssuedBy(self) -> String:
        return self.issuedBy

    def setIssuedBy(self, value: String):
        if value is not None:
            self.issuedBy = value
        return self

    def getModifications(self) -> List[Modification]:
        return self.modifications

    def addModification(self, value: Modification):
        if value is not None:
            self.modifications.append(value)
        return self

    def getRevisionLabel(self) -> RevisionLabelString:
        return self.revisionLabel

    def setRevisionLabel(self, value: RevisionLabelString):
        if value is not None:
            self.revisionLabel = value
        return self

    def getRevisionLabelP1(self) -> RevisionLabelString:
        return self.revisionLabelP1

    def setRevisionLabelP1(self, value: RevisionLabelString):
        if value is not None:
            self.revisionLabelP1 = value
        return self

    def getRevisionLabelP2(self) -> RevisionLabelString:
        return self.revisionLabelP2

    def setRevisionLabelP2(self, value: RevisionLabelString):
        if value is not None:
            self.revisionLabelP2 = value
        return self

    def getState(self) -> NameToken:
        return self.state

    def setState(self, value: NameToken):
        if value is not None:
            self.state = value
        return self


class AdminData(ARObject):
    """
    Container for administrative data including document revisions and language settings.
    Base: ARObject
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.DocRevisions: List[DocRevision] = []
        self.language: Union[Union[LEnum, None] , None] = None
        self.sdgs: List = []
        self.usedLanguages: Union[Union[MultiLanguagePlainText, None] , None] = None

    def getDocRevisions(self) -> List[DocRevision]:
        return self.DocRevisions

    def addDocRevision(self, value: DocRevision):
        self.DocRevisions.append(value)
        return self

    def getLanguage(self):
        return self.language

    def setLanguage(self, value):
        self.language = value
        return self

    def getSdgs(self):
        return self.sdgs

    def addSdg(self, value):
        self.sdgs.append(value)
        return self

    def getUsedLanguages(self):
        return self.usedLanguages

    def setUsedLanguages(self, value):
        self.usedLanguages = value
        return self
