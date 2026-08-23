from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, NameToken, RevisionLabelString, String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguagePlainText
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg


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
    This meta-class represents the ability to maintain information which relates to revision management of documents or objects.
    """

    # DocRevision method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.17, p.86
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDate               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDate               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIssuedBy           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIssuedBy           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModifications      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addModification       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRevisionLabel      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRevisionLabel      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRevisionLabelP1    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRevisionLabelP1    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRevisionLabelP2    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRevisionLabelP2    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getState              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setState              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies the date and time, when the object in question was released Tags: xml.sequenceOffset=80
        self.date: Optional[DateTime] = None

        # This is the name of an individual or an organization who issued the current revision of the document or document fragment. Tags: xml.sequenceOffset=60
        self.issuedBy: Optional[String] = None

        # This property represents one particular modification in comparison to its predecessor. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=100 xml.typeElement=false xml.typeWrapperElement=false
        self.modifications: List[Modification] = []

        # This attribute represents the version number of the object. Tags: xml.sequenceOffset=20
        self.revisionLabel: Optional[RevisionLabelString] = None

        # This attribute represents the version number of the first predecessor of the object. Tags: xml.sequenceOffset=30
        self.revisionLabelP1: Optional[RevisionLabelString] = None

        # This attribute represents the version number of the second predecessor of the object. This attribute is used if the object is the result of a merge process in which two branches are merged in to one new revision. Tags: xml.sequenceOffset=40
        self.revisionLabelP2: Optional[RevisionLabelString] = None

        # The attribute state represents the current state of the current file according to the configuration management plan. It is a NameToken until possible states are standardized. Tags: xml.sequenceOffset=50
        self.state: Optional[NameToken] = None

    def getDate(self) -> Optional[DateTime]:
        """
        This specifies the date and time, when the object in question was released Tags: xml.sequenceOffset=80
        """
        return self.date

    def setDate(self, value: Optional[DateTime]) -> "DocRevision":
        """
        This specifies the date and time, when the object in question was released Tags: xml.sequenceOffset=80
        A None value is a no-op and does not overwrite an existing date.
        """
        if value is not None:
            self.date = value
        return self

    def getIssuedBy(self) -> Optional[String]:
        """
        This is the name of an individual or an organization who issued the current revision of the document or document fragment. Tags: xml.sequenceOffset=60
        """
        return self.issuedBy

    def setIssuedBy(self, value: Optional[String]) -> "DocRevision":
        """
        This is the name of an individual or an organization who issued the current revision of the document or document fragment. Tags: xml.sequenceOffset=60
        A None value is a no-op and does not overwrite an existing issuedBy.
        """
        if value is not None:
            self.issuedBy = value
        return self

    def getModifications(self) -> List[Modification]:
        """
        This property represents one particular modification in comparison to its predecessor. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=100 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.modifications

    def addModification(self, value: Optional[Modification]) -> "DocRevision":
        """
        This property represents one particular modification in comparison to its predecessor. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=100 xml.typeElement=false xml.typeWrapperElement=false
        """
        if value is not None:
            self.modifications.append(value)
        return self

    def getRevisionLabel(self) -> Optional[RevisionLabelString]:
        """
        This attribute represents the version number of the object. Tags: xml.sequenceOffset=20
        """
        return self.revisionLabel

    def setRevisionLabel(self, value: Optional[RevisionLabelString]) -> "DocRevision":
        """
        This attribute represents the version number of the object. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing revisionLabel.
        """
        if value is not None:
            self.revisionLabel = value
        return self

    def getRevisionLabelP1(self) -> Optional[RevisionLabelString]:
        """
        This attribute represents the version number of the first predecessor of the object. Tags: xml.sequenceOffset=30
        """
        return self.revisionLabelP1

    def setRevisionLabelP1(self, value: Optional[RevisionLabelString]) -> "DocRevision":
        """
        This attribute represents the version number of the first predecessor of the object. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing revisionLabelP1.
        """
        if value is not None:
            self.revisionLabelP1 = value
        return self

    def getRevisionLabelP2(self) -> Optional[RevisionLabelString]:
        """
        This attribute represents the version number of the second predecessor of the object. This attribute is used if the object is the result of a merge process in which two branches are merged in to one new revision. Tags: xml.sequenceOffset=40
        """
        return self.revisionLabelP2

    def setRevisionLabelP2(self, value: Optional[RevisionLabelString]) -> "DocRevision":
        """
        This attribute represents the version number of the second predecessor of the object. This attribute is used if the object is the result of a merge process in which two branches are merged in to one new revision. Tags: xml.sequenceOffset=40
        A None value is a no-op and does not overwrite an existing revisionLabelP2.
        """
        if value is not None:
            self.revisionLabelP2 = value
        return self

    def getState(self) -> Optional[NameToken]:
        """
        The attribute state represents the current state of the current file according to the configuration management plan. It is a NameToken until possible states are standardized. Tags: xml.sequenceOffset=50
        """
        return self.state

    def setState(self, value: Optional[NameToken]) -> "DocRevision":
        """
        The attribute state represents the current state of the current file according to the configuration management plan. It is a NameToken until possible states are standardized. Tags: xml.sequenceOffset=50
        A None value is a no-op and does not overwrite an existing state.
        """
        if value is not None:
            self.state = value
        return self


class AdminData(ARObject):
    """
    AdminData represents the ability to express administrative information and custom extensions for an element. This administration information is to be treated as meta-data such as revision id or state of the file. There are basically the following kinds of meta-data • The language and/or used languages. • Revision information covering e.g. revision number, state, release date, changes. Note that this information can be given in general as well as related to a particular company. • Document meta-data specific for a company Beside that a custom extension of model-data is possible by • Special data
    """

    # AdminData method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.16, p.85
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDocRevisions       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDocRevision        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLanguage           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLanguage           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdgs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSdg                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUsedLanguages      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsedLanguages      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This allows to denote information about the current revision of the object. Note that information about previous revisions can also be logged here. The entries shall be sorted descendant by date in order to reflect the history. Therefore the most recent entry representing the current version is denoted first. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=50 xml.typeElement=false xml.typeWrapperElement=false
        self.DocRevisions: List[DocRevision] = []

        # This attribute specifies the master language of the document or the document fragment. The master language is the one in which the document is maintained and from which the other languages are derived from. In particular in case of inconsistencies, the information in the master language is priority. Tags: xml.sequenceOffset=20
        self.language: Optional[LEnum] = None

        # This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data. Stereotypes: atpSplitable Tags: atp.Splitkey=sdg.sdgCaption.shortName xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=60 xml.typeElement=false xml.typeWrapperElement=false
        self.sdgs: List[Sdg] = []

        # This property specifies the languages which are provided in the document. Therefore it should only be specified in the top level admin data. For each language provided in the document there is one entry in MultilanguagePlainText. The content of each entry can be used for illustration of the language. The used language itself depends on the language attribute in the entry. Tags: xml.sequenceOffset=30
        self.usedLanguages: Optional[MultiLanguagePlainText] = None

    def getDocRevisions(self) -> List[DocRevision]:
        """
        This allows to denote information about the current revision of the object. Note that information about previous revisions can also be logged here. The entries shall be sorted descendant by date in order to reflect the history. Therefore the most recent entry representing the current version is denoted first. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=50 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.DocRevisions

    def addDocRevision(self, value: Optional[DocRevision]) -> "AdminData":
        """
        This allows to denote information about the current revision of the object. Note that information about previous revisions can also be logged here. The entries shall be sorted descendant by date in order to reflect the history. Therefore the most recent entry representing the current version is denoted first. Tags: xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=50 xml.typeElement=false xml.typeWrapperElement=false
        """
        if value is not None:
            self.DocRevisions.append(value)
        return self

    def getLanguage(self) -> Optional[LEnum]:
        """
        This attribute specifies the master language of the document or the document fragment. The master language is the one in which the document is maintained and from which the other languages are derived from. In particular in case of inconsistencies, the information in the master language is priority. Tags: xml.sequenceOffset=20
        """
        return self.language

    def setLanguage(self, value: Optional[LEnum]) -> "AdminData":
        """
        This attribute specifies the master language of the document or the document fragment. The master language is the one in which the document is maintained and from which the other languages are derived from. In particular in case of inconsistencies, the information in the master language is priority. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing language.
        """
        if value is not None:
            self.language = value
        return self

    def getSdgs(self) -> List[Sdg]:
        """
        This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data. Stereotypes: atpSplitable Tags: atp.Splitkey=sdg.sdgCaption.shortName xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=60 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.sdgs

    def addSdg(self, value: Optional[Sdg]) -> "AdminData":
        """
        This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data. Stereotypes: atpSplitable Tags: atp.Splitkey=sdg.sdgCaption.shortName xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=60 xml.typeElement=false xml.typeWrapperElement=false
        """
        if value is not None:
            self.sdgs.append(value)
        return self

    def getUsedLanguages(self) -> Optional[MultiLanguagePlainText]:
        """
        This property specifies the languages which are provided in the document. Therefore it should only be specified in the top level admin data. For each language provided in the document there is one entry in MultilanguagePlainText. The content of each entry can be used for illustration of the language. The used language itself depends on the language attribute in the entry. Tags: xml.sequenceOffset=30
        """
        return self.usedLanguages

    def setUsedLanguages(self, value: Optional[MultiLanguagePlainText]) -> "AdminData":
        """
        This property specifies the languages which are provided in the document. Therefore it should only be specified in the top level admin data. For each language provided in the document there is one entry in MultilanguagePlainText. The content of each entry can be used for illustration of the language. The used language itself depends on the language attribute in the entry. Tags: xml.sequenceOffset=30
        A None value is a no-op and does not overwrite an existing usedLanguages.
        """
        if value is not None:
            self.usedLanguages = value
        return self
