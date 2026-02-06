from abc import ABC

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DocumentViewSelectable(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is DocumentViewSelectable:
            raise TypeError("DocumentViewSelectable is an abstract class.")
        super().__init__()


class Paginateable(DocumentViewSelectable, ABC):
    def __init__(self) -> None:
        if type(self) is Paginateable:
            raise TypeError("Paginateable is an abstract class.")
        super().__init__()

        self.chapterBreak: Union[ChapterEnumBreak, None] = None
        self.keepWithPrevious: Union[KeepWithPreviousEnum, None] = None

    def getBreak(self):
        return self.chapterBreak

    def setBreak(self, value):
        if value is not None:
            self.chapterBreak = value
        return self

    def getKeepWithPrevious(self):
        return self.keepWithPrevious

    def setKeepWithPrevious(self, value):
        if value is not None:
            self.keepWithPrevious = value
        return self
