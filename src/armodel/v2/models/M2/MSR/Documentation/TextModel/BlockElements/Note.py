from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)


class NoteTypeEnum(AREnum):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__(["note", "warning", "caution", "danger", "important", "tip"])


class Note(Paginateable):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__()

        self.noteType: Union[NoteTypeEnum, None] = None
        self.content: Union[String, None] = None

    def getNoteType(self) -> Union[NoteTypeEnum, None]:
        return self.noteType

    def setNoteType(self, value: NoteTypeEnum) -> "Note":
        self.noteType = value
        return self

    def getContent(self) -> Union[String, None]:
        return self.content

    def setContent(self, value: String) -> "Note":
        self.content = value
        return self


__all__ = [
    'NoteTypeEnum',
    'Note',
]
