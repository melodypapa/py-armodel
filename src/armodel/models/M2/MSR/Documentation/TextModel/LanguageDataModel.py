from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LEnum(ARLiteral):
    """
    Enumeration literal for language-specific values.
    """
    def __init__(self):
        super().__init__()


class LanguageSpecific(ARObject, ABC):
    """
    Abstract base class for language-specific content with language
    identifier and value.
    """
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
    """
    Language-specific overview paragraph element.
    """
    def __init__(self):
        super().__init__()


class LParagraph(LanguageSpecific):
    """
    Language-specific paragraph element.
    """
    def __init__(self):
        super().__init__()


class LLongName(LanguageSpecific):
    """
    Language-specific long name element.
    """
    def __init__(self):
        super().__init__()


class LPlainText(LanguageSpecific):
    """
    Language-specific plain text element.
    """
    def __init__(self):
        super().__init__()
