from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class NoteTypeEnum(AREnum):
    """
    This enumerator specifies the type of the note. It can be used to render a note label or even a note icon.
    """

    # NoteTypeEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.28, p.311
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on Note.noteType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This indicates that the note is an alert which shall be considered carefully. Tags: atp.EnumerationLiteralIndex=0
    CAUTION = "caution"
    # This indicates that the note represents an example, e.g. a code example etc. Tags: atp.EnumerationLiteralIndex=1
    EXAMPLE = "example"
    # This indicates that the note represents an exercise for the reader. Tags: atp.EnumerationLiteralIndex=2
    EXERCISE = "exercise"
    # This indicates that the note represents a hint which helps the user for better understanding. Tags: atp.EnumerationLiteralIndex=3
    HINT = "hint"
    # This indicates that the note represents an instruction, e.g. a step by step procedure. Tags: atp.EnumerationLiteralIndex=4
    INSTRUCTION = "instruction"
    # This indicates that the note is something else. The particular type of the note shall then be specified in the label of the note. Tags: atp.EnumerationLiteralIndex=5
    OTHER = "other"
    # This indicates that the note represents which is good to know. It is similar to a hint, but focuses more to good practice than to better understanding. Tags: atp.EnumerationLiteralIndex=6
    TIP = "tip"

    def __init__(self):
        super().__init__(
            (
                NoteTypeEnum.CAUTION,
                NoteTypeEnum.EXAMPLE,
                NoteTypeEnum.EXERCISE,
                NoteTypeEnum.HINT,
                NoteTypeEnum.INSTRUCTION,
                NoteTypeEnum.OTHER,
                NoteTypeEnum.TIP,
            )
        )


class Note(ARObject):
    """
    This represents a note in a documentation, which may be used to highlight specific issues such as hints or caution notes. N.B., Documentation notes can be nested recursively, even if this is not really intended. In case of nested notes e.g. the note icon of inner notes might be omitted while rendering the note.
    """

    # Note method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.27, p.310
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLabel     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLabel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNoteText  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNoteText  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNoteType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNoteType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This label can be used to superseed the default label specified by the noteType attribute. It is in particular useful for noteType="other".
        self.label: Optional[MultilanguageLongName] = None

        # This is the text content of the note.
        self.noteText: Optional["DocumentationBlock"] = None

        # Type of the Note. Default is "HINT"
        self.noteType: Optional[NoteTypeEnum] = None

    def getLabel(self) -> Optional[MultilanguageLongName]:
        """
        This label can be used to superseed the default label specified by the noteType attribute. It is in particular useful for noteType="other".

        Returns:
            The label of the note
        """
        return self.label

    def setLabel(self, value: Optional[MultilanguageLongName]) -> "Note":
        """
        This label can be used to superseed the default label specified by the noteType attribute. It is in particular useful for noteType="other". A None value is a no-op and does not overwrite an existing label.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.label = value
        return self

    def getNoteText(self) -> Optional["DocumentationBlock"]:
        """
        This is the text content of the note.

        Returns:
            The text content of the note
        """
        return self.noteText

    def setNoteText(self, value: Optional["DocumentationBlock"]) -> "Note":
        """
        This is the text content of the note. A None value is a no-op and does not overwrite an existing noteText.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.noteText = value
        return self

    def getNoteType(self) -> Optional[NoteTypeEnum]:
        """
        Type of the Note. Default is "HINT"

        Returns:
            The type of the note
        """
        return self.noteType

    def setNoteType(self, value: Optional[NoteTypeEnum]) -> "Note":
        """
        Type of the Note. Default is "HINT". A None value is a no-op and does not overwrite an existing noteType.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.noteType = value
        return self
