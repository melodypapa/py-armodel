from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from typing import List

class Sd(ARObject):
    def __init__(self):
        super().__init__()

        self.gid = ""
        self.value = ""

    def getGID(self):
        return self.gid

    def setGID(self, value):
        self.gid = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

class SdgCaption(MultilanguageReferrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.desc = None                                    # type: MultiLanguageOverviewParagraph

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        if value is not None:
            self.desc = value
        return self


class Sdg(ARObject):
    def __init__(self):
        super().__init__()

        self.gid = ""
        self.sd = []                                        # type: List[Sd]
        self.sdgCaption = None                              # type: SdgCaption
        self.sdgContentsTypes = []                          # type: List[Sdg]
        self.sdxRefs = []                                   # type: List[RefType]

    def getGID(self):
        return self.gid

    def setGID(self, value):
        self.gid = value
        return self

    def addSd(self, sd: Sd):
        self.sd.append(sd)
        return self

    def getSds(self) -> List[Sd]:
        return self.sd

    def getSdgCaption(self):
        return self.sdgCaption

    def createSdgCaption(self, short_name: str) -> SdgCaption:
        caption = SdgCaption(self, short_name)
        self.sdgCaption = caption
        return caption

    def getSdgContentsTypes(self):
        return self.sdgContentsTypes
    
    def addSdgContentsType(self, sdg):
        self.sdgContentsTypes.append(sdg)
    
    def getSdxRefs(self):
        return self.sdxRefs

    def addSdxRef(self, value):
        if value is not None:
            self.sdxRefs.append(value)
        return self
