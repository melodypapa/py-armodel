from abc import ABC
from typing import Optional

from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    DocumentViewSelectable,
    KeepWithPreviousEnum,
)


class Paginateable(DocumentViewSelectable, ABC):
    """
    This meta-class represents the ability to control the pagination policy when
    creating documents.

    Package: M2::MSR::Documentation::BlockElements::PaginationAndView

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 339, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is Paginateable:
            raise TypeError("Paginateable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows to specify a forced page break at the chapter level.
        # Controls whether a page break should be inserted before or after this element.
        # Origin: AUTOSAR specification attribute 'break'
        # Reason: Renamed to 'chapterBreak' to avoid Python reserved keyword 'break'
        self._chapterBreak: Optional[ChapterEnumBreak] = None

    @property
    def chapter_break(self) -> Optional[ChapterEnumBreak]:
        """Get chapterBreak (Pythonic accessor) - renamed from AUTOSAR 'break' to avoid Python keyword."""
        return self._chapterBreak

    @chapter_break.setter
    def chapter_break(self, value: Optional[ChapterEnumBreak]) -> None:
        """
        Set chapterBreak with validation.

        Args:
            value: The chapterBreak to set (controls page break behavior)

        Raises:
            TypeError: If value type is incorrect

        Note:
            Origin: AUTOSAR specification attribute 'break'
            Reason: Renamed to 'chapterBreak' to avoid Python reserved keyword 'break'
        """
        if value is None:
            self._chapterBreak = None
            return

        if not isinstance(value, ChapterEnumBreak):
            raise TypeError(
                f"chapterBreak must be ChapterEnumBreak or None, got {type(value).__name__}"
            )
        self._chapterBreak = value
        # In particular it if the containing text block shall be kept together previous
                # block.
        self._keepWith: Optional[KeepWithPreviousEnum] = None

    @property
    def keep_with(self) -> Optional[KeepWithPreviousEnum]:
        """Get keepWith (Pythonic accessor)."""
        return self._keepWith

    @keep_with.setter
    def keep_with(self, value: Optional[KeepWithPreviousEnum]) -> None:
        """
        Set keepWith with validation.

        Args:
            value: The keepWith to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepWith = None
            return

        if not isinstance(value, KeepWithPreviousEnum):
            raise TypeError(
                f"keepWith must be KeepWithPreviousEnum or None, got {type(value).__name__}"
            )
        self._keepWith = value

    def with_chapter_break(self, value):
        """
        Set chapter_break and return self for chaining.

        Args:
            value: The chapter_break to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_chapter_break("value")
        """
        self.chapter_break = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBreak(self) -> Optional[ChapterEnumBreak]:
        """
        AUTOSAR-compliant getter for break.

        Returns:
            The break value (page break control)

        Note:
            Delegates to chapter_break property (CODING_RULE_V2_00017)
        """
        return self.chapter_break  # Delegates to property

    def setBreak(self, value: Optional[ChapterEnumBreak]) -> "Paginateable":
        """
        AUTOSAR-compliant setter for break with method chaining.

        Args:
            value: The break to set (page break control)

        Returns:
            self for method chaining

        Note:
            Delegates to chapter_break property setter (gets validation automatically)
        """
        self.chapter_break = value  # Delegates to property setter
        return self

    def getKeepWith(self) -> Optional[KeepWithPreviousEnum]:
        """
        AUTOSAR-compliant getter for keepWith.

        Returns:
            The keepWith value

        Note:
            Delegates to keep_with property (CODING_RULE_V2_00017)
        """
        return self.keep_with  # Delegates to property

    def setKeepWith(self, value: Optional[KeepWithPreviousEnum]) -> "Paginateable":
        """
        AUTOSAR-compliant setter for keepWith with method chaining.

        Args:
            value: The keepWith to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_with property setter (gets validation automatically)
        """
        self.keep_with = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_break(self, value: Optional[ChapterEnumBreak]) -> "Paginateable":
        """
        Set break and return self for chaining.

        Args:
            value: The break to set (page break control)

        Returns:
            self for method chaining

        Example:
            >>> obj.with_break("value")
        """
        self.chapter_break = value  # Use property setter (gets validation)
        return self

    def with_keep_with(self, value: Optional[KeepWithPreviousEnum]) -> "Paginateable":
        """
        Set keepWith and return self for chaining.

        Args:
            value: The keepWith to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_with("value")
        """
        self.keep_with = value  # Use property setter (gets validation)
        return self
