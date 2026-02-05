from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from abc import ABC


class DocumentViewSelectable(ARObject, ABC):
    def __init__(self):
        if type(self) is DocumentViewSelectable:
            raise TypeError("DocumentViewSelectable is an abstract class.")
        super().__init__()


class Paginateable(DocumentViewSelectable, ABC):
    def __init__(self):
        if type(self) is Paginateable:
            raise TypeError("Paginateable is an abstract class.")
        super().__init__()

        self.chapterBreak = None                                # type: ChapterEnumBreak
        self.keepWithPrevious = None                            # type: KeepWithPreviousEnum

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
