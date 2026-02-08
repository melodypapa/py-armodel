from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ChapterOrMsrQuery(ARObject):
    """
    This meta-class represents the ability to denote a particular chapter or a
    query returning a chapter.

    Package: M2::MSR::Documentation::Chapters

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 342, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This establishes a subschapter.
        # atpVariation.
        self._chapter: "Chapter" = None

    @property
    def chapter(self) -> "Chapter":
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    @chapter.setter
    def chapter(self, value: "Chapter") -> None:
        """
        Set chapter with validation.

        Args:
            value: The chapter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Chapter):
            raise TypeError(
                f"chapter must be Chapter, got {type(value).__name__}"
            )
        self._chapter = value
        # This represents automatically contributed chapters by an msrquery.
        self._msrQuery: "MsrQueryChapter" = None

    @property
    def msr_query(self) -> "MsrQueryChapter":
        """Get msrQuery (Pythonic accessor)."""
        return self._msrQuery

    @msr_query.setter
    def msr_query(self, value: "MsrQueryChapter") -> None:
        """
        Set msrQuery with validation.

        Args:
            value: The msrQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MsrQueryChapter):
            raise TypeError(
                f"msrQuery must be MsrQueryChapter, got {type(value).__name__}"
            )
        self._msrQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    def setChapter(self, value: "Chapter") -> "ChapterOrMsrQuery":
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

    def getMsrQuery(self) -> "MsrQueryChapter":
        """
        AUTOSAR-compliant getter for msrQuery.

        Returns:
            The msrQuery value

        Note:
            Delegates to msr_query property (CODING_RULE_V2_00017)
        """
        return self.msr_query  # Delegates to property

    def setMsrQuery(self, value: "MsrQueryChapter") -> "ChapterOrMsrQuery":
        """
        AUTOSAR-compliant setter for msrQuery with method chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query property setter (gets validation automatically)
        """
        self.msr_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_chapter(self, value: "Chapter") -> "ChapterOrMsrQuery":
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

    def with_msr_query(self, value: "MsrQueryChapter") -> "ChapterOrMsrQuery":
        """
        Set msrQuery and return self for chaining.

        Args:
            value: The msrQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query("value")
        """
        self.msr_query = value  # Use property setter (gets validation)
        return self
