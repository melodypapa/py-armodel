from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.MSR.AsamHdo.SpecialData import Sdg
from typing import List

class AdminData(ARObject):
    def __init__(self):
        super().__init__()

        self.doc_revision = []
        self.language = None
        self.sdg = []
        self.used_languages = None

    def addSdg(self, sdg: Sdg):
        self.sdg.append(sdg)

    def getSdgs(self) -> List[Sdg]:
        return self.sdg