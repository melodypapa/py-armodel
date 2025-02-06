from typing import List

from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class Keyword(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.abbrName = None                                # type: NameToken
        self.classifications = []                           # type: List[NameToken]

    def getAbbrName(self):
        return self.abbrName

    def setAbbrName(self, value):
        if value is not None:
            self.abbrName = value
        return self

    def getClassifications(self):
        return self.classifications

    def addClassification(self, value):
        if value is not None:
            self.classifications.append(value)
        return self


class KeywordSet(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.keywords = []                                  # type: List[Keyword]

    def getKeywords(self):
        return self.keywords

    def createKeyword(self, short_name: str) -> Keyword:
        if (not self.IsElementExists(short_name)):
            keyword = Keyword(self, short_name)
            self.addElement(keyword)
            self.keywords.append(keyword)
        return self.getElement(short_name)
