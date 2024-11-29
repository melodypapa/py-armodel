from abc import ABCMeta
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class LEnum (ARLiteral):
    def __init__(self):
        super().__init__()

class LanguageSpecific(ARObject, metaclass = ABCMeta):
    def __init__(self):
        super().__init__()

        self.l = None                   # type: LEnum
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