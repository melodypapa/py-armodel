from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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


class Sdg(ARObject):
    def __init__(self):
        super().__init__()

        self.gid = ""
        self.sd = []                        # type: List[Sd]
        self.sdgCaption = None
        self.sdgContentsTypes = []          # type: List[Sdg]

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

    def setSdgCaption(self, value):
        self.sdgCaption = value
        return self

    def addSdgContentsType(self, sdg):
        self.sdgContentsTypes.append(sdg)

    def getSdgContentsTypes(self):
        return self.sdgContentsTypes