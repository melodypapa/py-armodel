from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class Caption(MultilanguageReferrable):
    """
    This meta-class represents the ability to express a caption which is a title, and a shortName.
    """

    # Caption method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.18, p.432
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDesc      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10

        Returns:
            The description of the object in question
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "Caption":
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10. A None value is a no-op and does not overwrite an existing desc.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self


__all__ = ["FloatEnum", "PgwideEnum", "Caption"]
