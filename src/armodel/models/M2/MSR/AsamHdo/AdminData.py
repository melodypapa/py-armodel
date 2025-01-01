from ....M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum
from ....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from typing import List

class AdminData(ARObject):
    def __init__(self):
        super().__init__()

        self.DocRevisions = []                              # type: List[DocRevision]
        self.language = None                                # type: LEnum
        self.sdgs = []                                      # type: List                       ## Sdg will cause the circular import
        self.usedLanguages = None                           # type: MultiLanguagePlainText

    def getDocRevisions(self):
        return self.DocRevisions

    def setDocRevisions(self, value):
        self.DocRevisions.append(value)
        return self

    def getLanguage(self):
        return self.language

    def setLanguage(self, value):
        self.language = value
        return self

    def getSdgs(self):
        return self.sdgs

    def addSdg(self, value):
        self.sdgs.append(value)
        return self

    def getUsedLanguages(self):
        return self.usedLanguages

    def setUsedLanguages(self, value):
        self.usedLanguages = value
        return self

    