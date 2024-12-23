from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Integer, RefType
from ....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph

class SwRecordLayoutV(ARObject):
    def __init__(self):
        super().__init__()

        self.baseTypeRef = None                         # type: RefType
        self.desc = None                                # type: MultiLanguageOverviewParagraph
        self.shortLabel = None                          # type: ARLiteral
        self.swGenericAxisParamTypeRef = None           # type: RefType
        self.swRecordLayoutVAxis = None                 # type: ARNumerical
        self.swRecordLayoutVFixValue = None             # type: ARNumerical
        self.swRecordLayoutVIndex = None                # type: ARLiteral
        self.swRecordLayoutVProp = None                 # type: ARLiteral

    def getBaseTypeRef(self):
        return self.baseTypeRef

    def setBaseTypeRef(self, value):
        self.baseTypeRef = value
        return self

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        self.desc = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self

    def getSwGenericAxisParamTypeRef(self):
        return self.swGenericAxisParamTypeRef

    def setSwGenericAxisParamTypeRef(self, value):
        self.swGenericAxisParamTypeRef = value
        return self

    def getSwRecordLayoutVAxis(self):
        return self.swRecordLayoutVAxis

    def setSwRecordLayoutVAxis(self, value):
        self.swRecordLayoutVAxis = value
        return self

    def getSwRecordLayoutVFixValue(self):
        return self.swRecordLayoutVFixValue

    def setSwRecordLayoutVFixValue(self, value):
        self.swRecordLayoutVFixValue = value
        return self

    def getSwRecordLayoutVIndex(self):
        return self.swRecordLayoutVIndex

    def setSwRecordLayoutVIndex(self, value):
        self.swRecordLayoutVIndex = value
        return self

    def getSwRecordLayoutVProp(self):
        return self.swRecordLayoutVProp

    def setSwRecordLayoutVProp(self, value):
        self.swRecordLayoutVProp = value
        return self


    
    
class SwRecordLayoutGroupContent(ARObject):
    def __init__(self):
        super().__init__()

        self.swRecordLayoutRef = None                   # type: RefType
        self.swRecordLayoutGroup = None                 # type: SwRecordLayoutGroup
        self.swRecordLayoutV = None                     # type: SwRecordLayoutV

    def getSwRecordLayoutRef(self):
        return self.swRecordLayoutRef

    def setSwRecordLayoutRef(self, value):
        self.swRecordLayoutRef = value
        return self

    def getSwRecordLayoutGroup(self):
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value):
        self.swRecordLayoutGroup = value
        return self

    def getSwRecordLayoutV(self):
        return self.swRecordLayoutV

    def setSwRecordLayoutV(self, value):
        self.swRecordLayoutV = value
        return self


class SwRecordLayoutGroup(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                            # type: ARLiteral
        self.desc = None                                # type: MultiLanguageOverviewParagraph
        self.shortLabel = None                          # type: ARLiteral
        self.swGenericAxisParamTypeRef = None           # type: RefType
        self.swRecordLayoutComponent = None             # type: ARLiteral
        self.swRecordLayoutGroupAxis = None             # type: AxisIndexType
        self.swRecordLayoutGroupContentType = None      # type: SwRecordLayoutGroupContent
        self.swRecordLayoutGroupFrom = None             # type: ARLiteral
        self.swRecordLayoutGroupIndex = None            # type: ARLiteral
        self.swRecordLayoutGroupStep = None             # type: Integer
        self.swRecordLayoutGroupTo = None               # type: ARLiteral 

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value
        return self

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        self.desc = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self

    def getSwGenericAxisParamTypeRef(self):
        return self.swGenericAxisParamTypeRef

    def setSwGenericAxisParamTypeRef(self, value):
        self.swGenericAxisParamTypeRef = value
        return self

    def getSwRecordLayoutComponent(self):
        return self.swRecordLayoutComponent

    def setSwRecordLayoutComponent(self, value):
        self.swRecordLayoutComponent = value
        return self

    def getSwRecordLayoutGroupAxis(self):
        return self.swRecordLayoutGroupAxis

    def setSwRecordLayoutGroupAxis(self, value):
        self.swRecordLayoutGroupAxis = value
        return self

    def getSwRecordLayoutGroupContentType(self):
        return self.swRecordLayoutGroupContentType

    def setSwRecordLayoutGroupContentType(self, value):
        self.swRecordLayoutGroupContentType = value
        return self

    def getSwRecordLayoutGroupFrom(self):
        return self.swRecordLayoutGroupFrom

    def setSwRecordLayoutGroupFrom(self, value):
        self.swRecordLayoutGroupFrom = value
        return self

    def getSwRecordLayoutGroupIndex(self):
        return self.swRecordLayoutGroupIndex

    def setSwRecordLayoutGroupIndex(self, value):
        self.swRecordLayoutGroupIndex = value
        return self

    def getSwRecordLayoutGroupStep(self):
        return self.swRecordLayoutGroupStep

    def setSwRecordLayoutGroupStep(self, value):
        self.swRecordLayoutGroupStep = value
        return self

    def getSwRecordLayoutGroupTo(self):
        return self.swRecordLayoutGroupTo

    def setSwRecordLayoutGroupTo(self, value):
        self.swRecordLayoutGroupTo = value
        return self

class SwRecordLayout(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swRecordLayoutGroup = None                 # type: SwRecordLayoutGroup

    def getSwRecordLayoutGroup(self):
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value):
        self.swRecordLayoutGroup = value
        return self
