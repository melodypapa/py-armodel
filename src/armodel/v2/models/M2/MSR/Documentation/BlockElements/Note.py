"""
AUTOSAR Package - Note

Package: M2::MSR::Documentation::BlockElements::Note
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)




class Note(Paginateable):
    """
    This represents a note in a documentation, which may be used to highlight
    specific issues such as hints or caution notes. N.B., Documentation notes
    can be nested recursively, even if this is not really intended. In case of
    nested notes e.g. the note icon of inner notes might be omitted while
    rendering the note.
    
    Package: M2::MSR::Documentation::BlockElements::Note::Note
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 310, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This label can be used to superseed the default label by the noteType
                # attribute.
        # It is in particular noteType="other".
        self._label: Optional["MultilanguageLong"] = None

    @property
    def label(self) -> Optional["MultilanguageLong"]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional["MultilanguageLong"]) -> None:
        """
        Set label with validation.
        
        Args:
            value: The label to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLong):
            raise TypeError(
                f"label must be MultilanguageLong or None, got {type(value).__name__}"
            )
        self._label = value
        # This is the text content of the note.
        self._noteText: "DocumentationBlock" = None

    @property
    def note_text(self) -> "DocumentationBlock":
        """Get noteText (Pythonic accessor)."""
        return self._noteText

    @note_text.setter
    def note_text(self, value: "DocumentationBlock") -> None:
        """
        Set noteText with validation.
        
        Args:
            value: The noteText to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"noteText must be DocumentationBlock, got {type(value).__name__}"
            )
        self._noteText = value
        # Type of the Note.
        # Default is "HINT".
        self._noteType: Optional["NoteTypeEnum"] = None

    @property
    def note_type(self) -> Optional["NoteTypeEnum"]:
        """Get noteType (Pythonic accessor)."""
        return self._noteType

    @note_type.setter
    def note_type(self, value: Optional["NoteTypeEnum"]) -> None:
        """
        Set noteType with validation.
        
        Args:
            value: The noteType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._noteType = None
            return

        if not isinstance(value, NoteTypeEnum):
            raise TypeError(
                f"noteType must be NoteTypeEnum or None, got {type(value).__name__}"
            )
        self._noteType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLabel(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for label.
        
        Returns:
            The label value
        
        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: "MultilanguageLong") -> "Note":
        """
        AUTOSAR-compliant setter for label with method chaining.
        
        Args:
            value: The label to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    def getNoteText(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for noteText.
        
        Returns:
            The noteText value
        
        Note:
            Delegates to note_text property (CODING_RULE_V2_00017)
        """
        return self.note_text  # Delegates to property

    def setNoteText(self, value: "DocumentationBlock") -> "Note":
        """
        AUTOSAR-compliant setter for noteText with method chaining.
        
        Args:
            value: The noteText to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to note_text property setter (gets validation automatically)
        """
        self.note_text = value  # Delegates to property setter
        return self

    def getNoteType(self) -> "NoteTypeEnum":
        """
        AUTOSAR-compliant getter for noteType.
        
        Returns:
            The noteType value
        
        Note:
            Delegates to note_type property (CODING_RULE_V2_00017)
        """
        return self.note_type  # Delegates to property

    def setNoteType(self, value: "NoteTypeEnum") -> "Note":
        """
        AUTOSAR-compliant setter for noteType with method chaining.
        
        Args:
            value: The noteType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to note_type property setter (gets validation automatically)
        """
        self.note_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_label(self, value: Optional["MultilanguageLong"]) -> "Note":
        """
        Set label and return self for chaining.
        
        Args:
            value: The label to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self

    def with_note_text(self, value: "DocumentationBlock") -> "Note":
        """
        Set noteText and return self for chaining.
        
        Args:
            value: The noteText to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_note_text("value")
        """
        self.note_text = value  # Use property setter (gets validation)
        return self

    def with_note_type(self, value: Optional["NoteTypeEnum"]) -> "Note":
        """
        Set noteType and return self for chaining.
        
        Args:
            value: The noteType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_note_type("value")
        """
        self.note_type = value  # Use property setter (gets validation)
        return self


class NoteTypeEnum(AREnum):
    """
    NoteTypeEnum enumeration

This enumerator specifies the type of the note. It can be used to render a note label or even a note icon. Aggregated by Note.noteType

Package: M2::MSR::Documentation::BlockElements::Note
    """
    # This indicates that the note is an alert which shall be considered carefully.
    caution = "0"

    # This indicates that the note represents an example, e.g. a code example etc.
    example = "1"

    # This indicates that the note represents an exercise for the reader.
    exercise = "2"

    # This indicates that the note represents a hint which helps the user for better understanding.
    hint = "3"

    # This indicates that the note represents an instruction, e.g. a step by step procedure.
    instruction = "4"

    # This indicates that the note is something else. The particular type of the note shall then be specified in the label of the note.
    other = "5"

    # This indicates that the note represents which is good to know. It is similar to a hint, but focuses more to good practice than to better understanding.
    tip = "6"
