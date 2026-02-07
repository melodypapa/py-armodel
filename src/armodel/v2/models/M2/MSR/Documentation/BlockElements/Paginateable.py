from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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
        self._break: Optional["ChapterEnumBreak"] = None

    @property
    def break(self) -> Optional["ChapterEnumBreak"]:
        """Get break (Pythonic accessor)."""
        return self._break

    @break.setter
    def break(self, value: Optional["ChapterEnumBreak"]) -> None:
        """
        Set break with validation.
        
        Args:
            value: The break to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._break = None
            return

        if not isinstance(value, ChapterEnumBreak):
            raise TypeError(
                f"break must be ChapterEnumBreak or None, got {type(value).__name__}"
            )
        self._break = value
        # This attribute denotes the pagination policy.
        # In particular it if the containing text block shall be kept together previous
                # block.
        self._keepWith: Optional["KeepWithPreviousEnum"] = None

    @property
    def keep_with(self) -> Optional["KeepWithPreviousEnum"]:
        """Get keepWith (Pythonic accessor)."""
        return self._keepWith

    @keep_with.setter
    def keep_with(self, value: Optional["KeepWithPreviousEnum"]) -> None:
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

    def getBreak(self) -> "ChapterEnumBreak":
        """
        AUTOSAR-compliant getter for break.
        
        Returns:
            The break value
        
        Note:
            Delegates to break property (CODING_RULE_V2_00017)
        """
        return self.break  # Delegates to property

    def setBreak(self, value: "ChapterEnumBreak") -> "Paginateable":
        """
        AUTOSAR-compliant setter for break with method chaining.
        
        Args:
            value: The break to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to break property setter (gets validation automatically)
        """
        self.break = value  # Delegates to property setter
        return self

    def getKeepWith(self) -> "KeepWithPreviousEnum":
        """
        AUTOSAR-compliant getter for keepWith.
        
        Returns:
            The keepWith value
        
        Note:
            Delegates to keep_with property (CODING_RULE_V2_00017)
        """
        return self.keep_with  # Delegates to property

    def setKeepWith(self, value: "KeepWithPreviousEnum") -> "Paginateable":
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

    def with_break(self, value: Optional["ChapterEnumBreak"]) -> "Paginateable":
        """
        Set break and return self for chaining.
        
        Args:
            value: The break to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_break("value")
        """
        self.break = value  # Use property setter (gets validation)
        return self

    def with_keep_with(self, value: Optional["KeepWithPreviousEnum"]) -> "Paginateable":
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