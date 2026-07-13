from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, NameToken, RevisionLabelString, String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguagePlainText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from typing import List


class Modification(ARObject):
    """
    Represents a modification made to a document.
    Base: ARObject
    Aggregated by: DocRevision.modifications
    """
    # Modification method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getChange                    [x] impl  [ ] docstring  [ ] test
    # [ ] setChange                    [x] impl  [ ] docstring  [ ] test
    # [ ] getReason                    [x] impl  [ ] docstring  [ ] test
    # [ ] setReason                    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.change: MultiLanguageOverviewParagraph = None
        self.reason: MultiLanguageOverviewParagraph = None

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
    # DocRevision method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDate                      [x] impl  [ ] docstring  [ ] test
    # [ ] setDate                      [x] impl  [ ] docstring  [ ] test
    # [ ] getIssuedBy                  [x] impl  [ ] docstring  [ ] test
    # [ ] setIssuedBy                  [x] impl  [ ] docstring  [ ] test
    # [ ] getModifications             [x] impl  [ ] docstring  [ ] test
    # [ ] addModification              [x] impl  [ ] docstring  [ ] test
    # [ ] getRevisionLabel             [x] impl  [ ] docstring  [ ] test
    # [ ] setRevisionLabel             [x] impl  [ ] docstring  [ ] test
    # [ ] getRevisionLabelP1           [x] impl  [ ] docstring  [ ] test
    # [ ] setRevisionLabelP1           [x] impl  [ ] docstring  [ ] test
    # [ ] getRevisionLabelP2           [x] impl  [ ] docstring  [ ] test
    # [ ] setRevisionLabelP2           [x] impl  [ ] docstring  [ ] test
    # [ ] getState                     [x] impl  [ ] docstring  [ ] test
    # [ ] setState                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.date: DateTime = None
        self.issuedBy: String = None
        self.modifications: List[Modification] = []
        self.revisionLabel: RevisionLabelString = None
        self.revisionLabelP1: RevisionLabelString = None
        self.revisionLabelP2: RevisionLabelString = None
        self.state: NameToken = None

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
    # AdminData method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDocRevisions              [x] impl  [ ] docstring  [ ] test
    # [ ] addDocRevision               [x] impl  [ ] docstring  [ ] test
    # [ ] getLanguage                  [x] impl  [ ] docstring  [ ] test
    # [ ] setLanguage                  [x] impl  [ ] docstring  [ ] test
    # [ ] getSdgs                      [x] impl  [ ] docstring  [ ] test
    # [ ] addSdg                       [x] impl  [ ] docstring  [ ] test
    # [ ] getUsedLanguages             [x] impl  [ ] docstring  [ ] test
    # [ ] setUsedLanguages             [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.DocRevisions: List[DocRevision] = []
        self.language: LEnum = None
        self.sdgs: List = []
        self.usedLanguages: MultiLanguagePlainText = None

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
