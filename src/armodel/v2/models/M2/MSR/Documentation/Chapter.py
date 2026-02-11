from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.Chapters import ChapterModel


class Chapter(Paginateable):
    """
    This meta-class represents a chapter of a document. Chapters are the primary
    structuring element in documentation.

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 698, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 329, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the overall contents of the chapter.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
        # R23-11.
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

        # The syntax shall be the applied help system respectively help is a
        # concatenated Identifier, but as of now we as an arbitrary string.
        self._helpEntry: Optional[String] = None

    @property
    def help_entry(self) -> Optional[String]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional[String]) -> None:
        """
        Set helpEntry with validation.

        Args:
            value: The helpEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._helpEntry = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"helpEntry must be String or None, got {type(value).__name__}"
            )
        self._helpEntry = value

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

    def setChapterModel(self, value: Optional[ChapterModel]) -> "Chapter":
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

    def getHelpEntry(self) -> Optional[String]:
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: Optional[String]) -> "Chapter":
        """
        AUTOSAR-compliant setter for helpEntry with method chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to help_entry property setter (gets validation automatically)
        """
        self.help_entry = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter_model(self, value: Optional[ChapterModel]) -> "Chapter":
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

    def with_help_entry(self, value: Optional[String]) -> "Chapter":
        """
        Set helpEntry and return self for chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_help_entry("value")
        """
        self.help_entry = value  # Use property setter (gets validation)
        return self
