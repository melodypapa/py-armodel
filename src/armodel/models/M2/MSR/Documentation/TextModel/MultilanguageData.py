from __future__ import annotations

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph, LPlainText
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum


class MultiLanguageParagraph(Paginateable):
    """
    Multi-language paragraph containing language-specific long name
    entries.
    """

    # MultiLanguageParagraph method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addL1                        [x] impl  [ ] docstring  [ ] test
    # [ ] getL1s                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.l1: List[LLongName] = []

    def addL1(self, l1: LLongName):
        self.l1.append(l1)
        return self

    def getL1s(self) -> List[LLongName]:
        return self.l1


class MultiLanguageOverviewParagraph(ARObject):
    """
    This is the content of a multilingual paragraph in an overview item.
    """

    # MultiLanguageOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.90, p.348
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addL2       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getL2s      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This represents the text in one particular language.
        self.l2: List[LOverviewParagraph] = []

    def addL2(self, l2: Optional[LOverviewParagraph]) -> "MultiLanguageOverviewParagraph":
        """
        This represents the text in one particular language. A None value is a no-op and
        is not appended.
        """
        if l2 is not None:
            self.l2.append(l2)
        return self

    def getL2s(self) -> List[LOverviewParagraph]:
        """
        This represents the text in one particular language.
        """
        return self.l2


class MultilanguageLongName(ARObject):
    """
    Multi-language long name containing language-specific long name
    entries.
    """

    # MultilanguageLongName method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addL4                        [x] impl  [ ] docstring  [ ] test
    # [ ] getL4s                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.l4: List[LLongName] = []

    def addL4(self, l4: LLongName):
        self.l4.append(l4)
        return self

    def getL4s(self) -> List[LLongName]:
        return self.l4


class MultiLanguagePlainText(ARObject):
    """
    This is a multilingual plaint Text. It is intended to be rendered as a paragraph.
    """

    # MultiLanguagePlainText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.95, p.349
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addL10       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getL10s      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is the plain text in one particular language. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.l10s: List[LPlainText] = []

    def getL10s(self) -> List[LPlainText]:
        """
        This is the plain text in one particular language. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false

        Returns:
            The plain texts in particular languages
        """
        return self.l10s

    def addL10(self, value: Optional[LPlainText]) -> "MultiLanguagePlainText":
        """
        This is the plain text in one particular language. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.l10s.append(value)
        return self


class MultiLanguageVerbatim(Paginateable):
    """
    This class represents multilingual Verbatim. Verbatim means, that white-space is maintained. When Verbatim is rendered in PDF or Online media, white-space is obeyed. Blanks are rendered as well as newline characters.
    """

    # MultiLanguageVerbatim method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.5, p.291
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAllowBreak    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowBreak    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFloat         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFloat         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHelpEntry     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHelpEntry     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addL5            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getL5s           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPgwide        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPgwide        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This indicates if the verbatim text might be split on multiple pages. Default is "1".
        self.allowBreak: Optional[NameToken] = None

        # Indicate whether it is allowed to break the element. The following values are allowed:
        self.float: Optional[FloatEnum] = None

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.
        self.helpEntry: Optional[String] = None

        # This the text in one particular language.
        self.l5s: List[LVerbatim] = []

        # Used to indicate wether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide").
        self.pgwide: Optional[PgwideEnum] = None

    def getAllowBreak(self) -> Optional[NameToken]:
        """
        This indicates if the verbatim text might be split on multiple pages. Default is "1".

        Returns:
            Whether the verbatim text might be split on multiple pages
        """
        return self.allowBreak

    def setAllowBreak(self, value: Optional[NameToken]) -> "MultiLanguageVerbatim":
        """
        This indicates if the verbatim text might be split on multiple pages. Default is "1". A None value is a no-op and does not overwrite an existing allowBreak.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.allowBreak = value
        return self

    def getFloat(self) -> Optional[FloatEnum]:
        """
        Indicate whether it is allowed to break the element. The following values are allowed:

        Returns:
            Whether it is allowed to break the element
        """
        return self.float

    def setFloat(self, value: Optional[FloatEnum]) -> "MultiLanguageVerbatim":
        """
        Indicate whether it is allowed to break the element. The following values are allowed:. A None value is a no-op and does not overwrite an existing float.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.float = value
        return self

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator.

        Returns:
            The entry point in an online help system
        """
        return self.helpEntry

    def setHelpEntry(self, value: Optional[String]) -> "MultiLanguageVerbatim":
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. A None value is a no-op and does not overwrite an existing helpEntry.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.helpEntry = value
        return self

    def addL5(self, value: Optional[LVerbatim]) -> "MultiLanguageVerbatim":
        """
        This the text in one particular language. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.l5s.append(value)
        return self

    def getL5s(self) -> List[LVerbatim]:
        """
        This the text in one particular language.

        Returns:
            The texts in particular languages
        """
        return self.l5s

    def getPgwide(self) -> Optional[PgwideEnum]:
        """
        Used to indicate wether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide").

        Returns:
            Whether the figure should take the complete page width
        """
        return self.pgwide

    def setPgwide(self, value: Optional[PgwideEnum]) -> "MultiLanguageVerbatim":
        """
        Used to indicate wether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide"). A None value is a no-op and does not overwrite an existing pgwide.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.pgwide = value
        return self
