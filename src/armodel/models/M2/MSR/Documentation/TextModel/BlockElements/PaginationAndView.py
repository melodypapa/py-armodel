from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DocumentViewSelectable(ARObject):
    def __init__(self):
        super().__init__()


class Paginateable(DocumentViewSelectable):
    def __init__(self):
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
