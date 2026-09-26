from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
    MixedContentForLongName,
    MixedContentForOverviewParagraph,
)


class SingleLanguageLongName(MixedContentForLongName):
    """
    SingleLanguageLongName
    """

    # SingleLanguageLongName method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.7, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The text content of the long name.
        self.value: Optional[String] = None

    def getValue(self) -> Optional[String]:
        """
        The text content of the long name.
        """
        return self.value

    def setValue(self, value: Optional[String]) -> "SingleLanguageLongName":
        """
        The text content of the long name. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class SlOverviewParagraph(MixedContentForOverviewParagraph):
    """
    MixedContentForOverviewParagraph in one particular language. The language is defined by the context. The attribute l is there only for backwards compatibility and shall be ignored.
    """

    # SlOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.70, p.464
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.97, p.350 (legacy l attribute)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getL      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setL      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Table E.70 carries zero attribute rows; the XSD-only `L` XML attribute (attributeGroup
    #  SL-OVERVIEW-PARAGRAPH, L-ENUM--SIMPLE, atp.Status="removed") is merged as an optional
    #  legacy member documented by Table 9.97 (LanguageSpecific.l) — Rule 0019-style combine;
    #  the mixed text rides the AtpMixedString mixin (mixedString) via
    #  readMixedStringText/writeMixedStringText; Table 9.3 base members serialize on the
    #  consuming L-2 element's FT child via readSlOverviewParagraph/writeSlOverviewParagraphContent)

    def __init__(self):
        super().__init__()

        # This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case.
        self.l: Optional[LEnum] = None

    def getL(self) -> Optional[LEnum]:
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case.
        """
        return self.l

    def setL(self, value: Optional[LEnum]) -> "SlOverviewParagraph":
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case. A None value is a no-op and does not overwrite an existing l.
        """
        if value is not None:
            self.l = value
        return self
