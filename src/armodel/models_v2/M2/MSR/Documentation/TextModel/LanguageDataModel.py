from abc import ABC

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class LEnum(ARLiteral):
    def __init__(self):
        super().__init__()


class LanguageSpecific(ARObject, ABC):
    def __init__(self):
        if type(self) is LanguageSpecific:
            raise TypeError("LanguageSpecific is an abstract class.")

        super().__init__()

        self.l = None
        self.value = ""

    def getL(self):
        return self.l

    def setL(self, value):
        self.l = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self


class LOverviewParagraph(LanguageSpecific):
    def __init__(self):
        super().__init__()


class LParagraph(LanguageSpecific):
    def __init__(self):
        super().__init__()


class LLongName(LanguageSpecific):
    def __init__(self):
        super().__init__()


class LPlainText(LanguageSpecific):
    def __init__(self):
        super().__init__()
