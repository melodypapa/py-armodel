from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    MixedContentForLongName,
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
