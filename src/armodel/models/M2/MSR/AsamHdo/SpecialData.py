from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)


class Sd(ARObject):
    """
    Represents special data with a global identifier and value.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()

        self.gid: str = ""
        self.value: str = ""

    def getGID(self) -> str:
        return self.gid

    def setGID(self, value: str):
        self.gid = value
        return self

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
        return self

class SdgCaption(MultilanguageReferrable):
    """
    Represents a caption for special data groups with multilingual description.
    Base: MultilanguageReferrable
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.desc: MultiLanguageOverviewParagraph = None

    def getDesc(self) -> MultiLanguageOverviewParagraph:
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph):
        if value is not None:
            self.desc = value
        return self


class Sdg(ARObject):
    """
    Represents a special data group containing special data items and references.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()

        self.gid: str = ""
        self.sd: List[Sd] = []
        self.sdgCaption: SdgCaption = None
        self.sdgContentsTypes: List[Sdg] = []
        self.sdxRefs: List[RefType] = []

    def getGID(self) -> str:
        return self.gid

    def setGID(self, value: str):
        self.gid = value
        return self

    def addSd(self, sd: Sd):
        self.sd.append(sd)
        return self

    def getSds(self) -> List[Sd]:
        return self.sd

    def getSdgCaption(self) -> SdgCaption:
        return self.sdgCaption

    def createSdgCaption(self, short_name: str) -> SdgCaption:
        caption = SdgCaption(self, short_name)
        self.sdgCaption = caption
        return caption

    def getSdgContentsTypes(self) -> List['Sdg']:
        return self.sdgContentsTypes

    def addSdgContentsType(self, sdg: 'Sdg'):
        self.sdgContentsTypes.append(sdg)

    def getSdxRefs(self) -> List[RefType]:
        return self.sdxRefs

    def addSdxRef(self, value: RefType):
        if value is not None:
            self.sdxRefs.append(value)
        return self
