"""
AUTOSAR Package - PaginationAndView

Package: M2::MSR::Documentation::BlockElements::PaginationAndView
"""


from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
)


class DocumentViewSelectable(ARObject, ABC):
    """
    This meta-class represents the ability to be dedicated to a particular
    audience or document view.
    
    Package: M2::MSR::Documentation::BlockElements::PaginationAndView::DocumentViewSelectable
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 340, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is DocumentViewSelectable:
            raise TypeError("DocumentViewSelectable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows to denote a semantic information used to identify
                # documentation objects to be customizable document views.
        # It shall be agreement between the involved parties.
        self._si: "NameTokens" = None

    @property
    def si(self) -> "NameTokens":
        """Get si (Pythonic accessor)."""
        return self._si

    @si.setter
    def si(self, value: "NameTokens") -> None:
        """
        Set si with validation.
        
        Args:
            value: The si to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameTokens):
            raise TypeError(
                f"si must be NameTokens, got {type(value).__name__}"
            )
        self._si = value
        # the object appears in all.
        self._view: Optional[ViewTokens] = None

    @property
    def view(self) -> Optional[ViewTokens]:
        """Get view (Pythonic accessor)."""
        return self._view

    @view.setter
    def view(self, value: Optional[ViewTokens]) -> None:
        """
        Set view with validation.
        
        Args:
            value: The view to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._view = None
            return

        if not isinstance(value, ViewTokens):
            raise TypeError(
                f"view must be ViewTokens or None, got {type(value).__name__}"
            )
        self._view = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSi(self) -> "NameTokens":
        """
        AUTOSAR-compliant getter for si.
        
        Returns:
            The si value
        
        Note:
            Delegates to si property (CODING_RULE_V2_00017)
        """
        return self.si  # Delegates to property

    def setSi(self, value: "NameTokens") -> DocumentViewSelectable:
        """
        AUTOSAR-compliant setter for si with method chaining.
        
        Args:
            value: The si to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to si property setter (gets validation automatically)
        """
        self.si = value  # Delegates to property setter
        return self

    def getView(self) -> ViewTokens:
        """
        AUTOSAR-compliant getter for view.
        
        Returns:
            The view value
        
        Note:
            Delegates to view property (CODING_RULE_V2_00017)
        """
        return self.view  # Delegates to property

    def setView(self, value: ViewTokens) -> DocumentViewSelectable:
        """
        AUTOSAR-compliant setter for view with method chaining.
        
        Args:
            value: The view to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to view property setter (gets validation automatically)
        """
        self.view = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_si(self, value: "NameTokens") -> DocumentViewSelectable:
        """
        Set si and return self for chaining.
        
        Args:
            value: The si to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_si("value")
        """
        self.si = value  # Use property setter (gets validation)
        return self

    def with_view(self, value: Optional[ViewTokens]) -> DocumentViewSelectable:
        """
        Set view and return self for chaining.
        
        Args:
            value: The view to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_view("value")
        """
        self.view = value  # Use property setter (gets validation)
        return self



class Paginateable(DocumentViewSelectable, ABC):
    """
    This meta-class represents the ability to control the pagination policy when
    creating documents.
    
    Package: M2::MSR::Documentation::BlockElements::PaginationAndView::Paginateable
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 339, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is Paginateable:
            raise TypeError("Paginateable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes allows to specify a forced page break.
        self._break: Optional[ChapterEnumBreak] = None

    @property
    def chapter_break(self) -> Optional[ChapterEnumBreak]:
        """Get chapter_break (Pythonic accessor) - renamed from AUTOSAR 'break' to avoid Python keyword."""
        return self._chapterBreak

    @chapter_break.setter
    def chapter_break(self, value: Optional[ChapterEnumBreak]) -> None:
        """
        Set chapter_break with validation.

        Args:
            value: The chapter_break to set (controls page break behavior)

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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBreak(self) -> ChapterEnumBreak:
        """
        AUTOSAR-compliant getter for break.
        
        Returns:
            The break value
        
        Note:
            Delegates to break property (CODING_RULE_V2_00017)
        """
        return self.chapter_break  # Delegates to property

    def setBreak(self, value: ChapterEnumBreak) -> Paginateable:
        """
        AUTOSAR-compliant setter for break with method chaining.
        
        Args:
            value: The break to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to break property setter (gets validation automatically)
        """
        self.chapter_break = value  # Delegates to property setter
        return self

    def getKeepWith(self) -> KeepWithPreviousEnum:
        """
        AUTOSAR-compliant getter for keepWith.
        
        Returns:
            The keepWith value
        
        Note:
            Delegates to keep_with property (CODING_RULE_V2_00017)
        """
        return self.keep_with  # Delegates to property

    def setKeepWith(self, value: KeepWithPreviousEnum) -> Paginateable:
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

    def with_break(self, value: Optional[ChapterEnumBreak]) -> Paginateable:
        """
        Set break and return self for chaining.
        
        Args:
            value: The break to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_break("value")
        """
        self.chapter_break = value  # Use property setter (gets validation)
        return self

    def with_keep_with(self, value: Optional[KeepWithPreviousEnum]) -> Paginateable:
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


class ChapterEnumBreak(AREnum):
    """
    ChapterEnumBreak enumeration

This allows to specify the page break policy of a paginatable element. Aggregated by Paginateable.break

Package: M2::MSR::Documentation::BlockElements::PaginationAndView
    """
    # This indicates the a page break shall be applied before the current block.
    chapter_break = "0"

    # This indicates that there is no need to force a page break before this block.
    no_break = "1"



class KeepWithPreviousEnum(AREnum):
    """
    KeepWithPreviousEnum enumeration

This enumerator specifies a page break policy by controlling blocks which shall be kept together. Aggregated by Paginateable.keepWithPrevious

Package: M2::MSR::Documentation::BlockElements::PaginationAndView
    """
    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSAR = "None"

    # This indicates that the block shall be kept together with the previous block.
    keep = "0"

    # This indicates that there is no need to keep the block with the previous one. This is the same as if the attribute itself is missing.
    noKeep = "1"



class ViewTokens(ARLiteral):
    """
    ViewTokens primitive type

This primitive specifies the tokens to specify a documentation view. Tags: xml.xsd.customType=VIEW-TOKENS xml.xsd.pattern=(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)* xml.xsd.type=string Table 9.78: ViewTokens 9.5 Including generated documentation parts [TPS_GST_00336] Including generated Documentation Parts (cid:100)AUTOSAR supports an approach where parts of the documentation are automatically generated and in- cluded at a particular location within the documentation. This support is provided by the so called MSR query mechanism ( MsrQueryP1, MsrQueryP2, MsrQueryTopic1 and MsrQueryChapter). These classes allow to represent the properties of the inclusion as well as the result of the inclusion. Thereby the intermediate results can be visualized and exchanged after the generated parts 340 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 were included. Hence it is not necessary that all parties involved in the project are able to perform the inclusion process. Details are subject to mutual agreement.(cid:99)() «atpMixed» «atpMixed» ChapterModel +chapterContent ChapterContent +topicContent TopicContentOrMsrQuery 0..1 0..1 +topicContent 1 +msrQueryP1 1 «atpMixed» Paginateable TopicContent +msrQueryResultP1 MsrQueryP1 0..1 «atpMixed» +topic1 TopicOrMsrQuery 0..1 «atpVariation,atpSplitable» +topic1 1 +msrQueryTopic1 1 Identifiable MsrQueryResultTopic1 Paginateable Paginateable +topic1 +msrQueryResultTopic1 MsrQueryTopic1 Topic1 0..* 0..1 + helpEntry: String [0..1] {ordered} «atpMixed» +chapter ChapterOrMsrQuery 0..1 «atpVariation,atpSplitable» +chapter 1 +msrQueryChapter 1 Identifiable Paginateable MsrQueryResultChapter +chapterModel Paginateable +chapter +msrQueryResultChapter MsrQueryChapter Chapter 1 0..* 0..1 + helpEntry: String [0..1] {ordered} Figure 9.12: Including generated documentation parts by MsrQuery The following meta-classes represent the alternative of manually edited documentation and included generated parts. 341 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11

Package: M2::MSR::Documentation::BlockElements::PaginationAndView
    """
    pass


