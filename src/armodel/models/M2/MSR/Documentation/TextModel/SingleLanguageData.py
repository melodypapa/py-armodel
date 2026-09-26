from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
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


class SlOverviewParagraph(MixedContentForOverviewParagraph, LanguageSpecific):
    """
    MixedContentForOverviewParagraph in one particular language. The language is defined by the context. The attribute l is there only for backwards compatibility and shall be ignored.
    """

    # SlOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.70, p.464
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table E.70 Attribute rows: none (dash placeholder); the XSD-only
    #  `L` XML attribute (attributeGroup SL-OVERVIEW-PARAGRAPH, L-ENUM--SIMPLE,
    #  atp.Status="removed") and the mixed text ride the inherited LanguageSpecific accessors
    #  getL/setL/getValue/setValue covered by their declaring class checklist; the Table 9.3
    #  Base members are covered by their declaring class checklist and serialize on the
    #  consuming L-2 element's FT child via readSlOverviewParagraph/writeSlOverviewParagraphContent;
    #  getMixedString/setMixedString via the AtpMixedString mixin — stereotype-inherent, no spec rows)

    def __init__(self):
        super().__init__()
