from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.Chapters import (
    ChapterContent,
    ChapterOrMsrQuery,
    TopicOrMsrQuery,
)


class ChapterModel(ARObject):
    """
    This is the basic content model of a chapter except the Chapter title. This
    can be utilized in general chapters as well as in predefined chapters. A
    chapter has content on three levels: 1. chapter content 2. topics 3.
    subchapters

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 699, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 329, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a particular subchapter.
        self._chapter: Optional[ChapterOrMsrQuery] = None

    @property
    def chapter(self) -> Optional[ChapterOrMsrQuery]:
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    @chapter.setter
    def chapter(self, value: Optional[ChapterOrMsrQuery]) -> None:
        """
        Set chapter with validation.

        Args:
            value: The chapter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._chapter = None
            return

        if not isinstance(value, ChapterOrMsrQuery):
            raise TypeError(
                f"chapter must be ChapterOrMsrQuery or None, got {type(value).__name__}"
            )
        self._chapter = value
        # directly in the.
        self._chapterContent: Optional[ChapterContent] = None

    @property
    def chapter_content(self) -> Optional[ChapterContent]:
        """Get chapterContent (Pythonic accessor)."""
        return self._chapterContent

    @chapter_content.setter
    def chapter_content(self, value: Optional[ChapterContent]) -> None:
        """
        Set chapterContent with validation.

        Args:
            value: The chapterContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._chapterContent = None
            return

        if not isinstance(value, ChapterContent):
            raise TypeError(
                f"chapterContent must be ChapterContent or None, got {type(value).__name__}"
            )
        self._chapterContent = value
        self._topic1: Optional[TopicOrMsrQuery] = None

    @property
    def topic1(self) -> Optional[TopicOrMsrQuery]:
        """Get topic1 (Pythonic accessor)."""
        return self._topic1

    @topic1.setter
    def topic1(self, value: Optional[TopicOrMsrQuery]) -> None:
        """
        Set topic1 with validation.

        Args:
            value: The topic1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topic1 = None
            return

        if not isinstance(value, TopicOrMsrQuery):
            raise TypeError(
                f"topic1 must be TopicOrMsrQuery or None, got {type(value).__name__}"
            )
        self._topic1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> Optional[ChapterOrMsrQuery]:
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    def setChapter(self, value: Optional[ChapterOrMsrQuery]) -> "ChapterModel":
        """
        AUTOSAR-compliant setter for chapter with method chaining.

        Args:
            value: The chapter to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter property setter (gets validation automatically)
        """
        self.chapter = value  # Delegates to property setter
        return self

    def getChapterContent(self) -> Optional[ChapterContent]:
        """
        AUTOSAR-compliant getter for chapterContent.

        Returns:
            The chapterContent value

        Note:
            Delegates to chapter_content property (CODING_RULE_V2_00017)
        """
        return self.chapter_content  # Delegates to property

    def setChapterContent(self, value: Optional[ChapterContent]) -> "ChapterModel":
        """
        AUTOSAR-compliant setter for chapterContent with method chaining.

        Args:
            value: The chapterContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_content property setter (gets validation automatically)
        """
        self.chapter_content = value  # Delegates to property setter
        return self

    def getTopic1(self) -> Optional[TopicOrMsrQuery]:
        """
        AUTOSAR-compliant getter for topic1.

        Returns:
            The topic1 value

        Note:
            Delegates to topic1 property (CODING_RULE_V2_00017)
        """
        return self.topic1  # Delegates to property

    def setTopic1(self, value: Optional[TopicOrMsrQuery]) -> "ChapterModel":
        """
        AUTOSAR-compliant setter for topic1 with method chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic1 property setter (gets validation automatically)
        """
        self.topic1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter(self, value: Optional[ChapterOrMsrQuery]) -> "ChapterModel":
        """
        Set chapter and return self for chaining.

        Args:
            value: The chapter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter("value")
        """
        self.chapter = value  # Use property setter (gets validation)
        return self

    def with_chapter_content(self, value: Optional[ChapterContent]) -> "ChapterModel":
        """
        Set chapterContent and return self for chaining.

        Args:
            value: The chapterContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_content("value")
        """
        self.chapter_content = value  # Use property setter (gets validation)
        return self

    def with_topic1(self, value: Optional[TopicOrMsrQuery]) -> "ChapterModel":
        """
        Set topic1 and return self for chaining.

        Args:
            value: The topic1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic1("value")
        """
        self.topic1 = value  # Use property setter (gets validation)
        return self
