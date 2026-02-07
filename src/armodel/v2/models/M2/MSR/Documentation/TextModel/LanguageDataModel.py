from abc import ABC
from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class LEnum(ARLiteral):
    def __init__(self) -> None:
        super().__init__()


class LanguageSpecific(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is LanguageSpecific:
            raise TypeError("LanguageSpecific is an abstract class.")

        super().__init__()

        self.l: Union[str, None] = None
        self.value: str = ""

    def getL(self) -> Union[str, None]:
        return self.l

    def setL(self, value: str) -> "LanguageSpecific":
        self.l = value
        return self

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str) -> "LanguageSpecific":
        self.value = value
        return self


class LOverviewParagraph(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()


class LParagraph(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()


class LLongName(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()


class LPlainText(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()
