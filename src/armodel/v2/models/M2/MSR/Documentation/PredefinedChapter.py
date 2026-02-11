from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.Chapters import ChapterModel


class PredefinedChapter(ARObject):
    """
    This represents a predefined chapter.

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 330, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the content of the predefined chapter.
        self._chapterModel: Optional[ChapterModel] = None

    @property
    def chapter_model(self) -> Optional[ChapterModel]:
        """Get chapterModel (Pythonic accessor)."""
        return self._chapterModel

    @chapter_model.setter
    def chapter_model(self, value: Optional[ChapterModel]) -> None:
        """
        Set chapterModel with validation.

        Args:
            value: The chapterModel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._chapterModel = None
            return

        if not isinstance(value, ChapterModel):
            raise TypeError(
                f"chapterModel must be ChapterModel or None, got {type(value).__name__}"
            )
        self._chapterModel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapterModel(self) -> Optional[ChapterModel]:
        """
        AUTOSAR-compliant getter for chapterModel.

        Returns:
            The chapterModel value

        Note:
            Delegates to chapter_model property (CODING_RULE_V2_00017)
        """
        return self.chapter_model  # Delegates to property

    def setChapterModel(self, value: Optional[ChapterModel]) -> "PredefinedChapter":
        """
        AUTOSAR-compliant setter for chapterModel with method chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_model property setter (gets validation automatically)
        """
        self.chapter_model = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter_model(self, value: Optional[ChapterModel]) -> "PredefinedChapter":
        """
        Set chapterModel and return self for chaining.

        Args:
            value: The chapterModel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_model("value")
        """
        self.chapter_model = value  # Use property setter (gets validation)
        return self
