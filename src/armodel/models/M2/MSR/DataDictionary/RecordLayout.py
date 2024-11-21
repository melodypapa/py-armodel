from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, RefType
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

    def setShortLabel(self, short_label: ARLiteral):
        self.shortLabel = short_label
        return self

    def setBaseTypeRef(self, ref: RefType):
        self.baseTypeRef = ref
        return self

    def setSwRecordLayoutVAxis(self, axis: ARNumerical):
        self.swRecordLayoutVAxis = axis
        return self

    def setSwRecordLayoutVFixValue(self, value: ARNumerical):
        self.swRecordLayoutVFixValue = value
        return self

    def setSwRecordLayoutVIndex(self, index: ARLiteral):
        self.swRecordLayoutVIndex = index
        return self

    def setSwRecordLayoutVProp(self, prop: ARLiteral):
        self.swRecordLayoutVProp = prop
        return self
    
class SwRecordLayoutGroupContent(ARObject):
    def __init__(self):
        super().__init__()

        self.swRecordLayoutRef = None                   # type: RefType
        self.swRecordLayoutGroup = None                 # type: SwRecordLayoutGroup
        self.swRecordLayoutV = None                     # type: SwRecordLayoutV


class SwRecordLayoutGroup(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                            # type: ARLiteral
        self.desc = None                                # type: MultiLanguageOverviewParagraph
        self.shortLabel = None                          # type: ARLiteral
        self.swGenericAxisParamTypeRef = None           # type: RefType
        self.swRecordLayoutComponent = None             # type: ARLiteral
        self.swRecordLayoutGroupAxis = None             # type: ARNumerical
        self.swRecordLayoutGroupContentType = None      # type: SwRecordLayoutGroupContent
        self.swRecordLayoutGroupIndex = None            # type: ARLiteral
        self.swRecordLayoutGroupFrom = None             # type: ARLiteral
        self.swRecordLayoutGroupTo = None               # type: ARLiteral 


    def setCategory(self, category: ARLiteral):
        self.category = category
        return self

    def setDesc(self, desc):
        self.desc = desc
        return self

    def setShortLabel(self, label: ARLiteral):
        self.shortLabel = label
        return self

    def setSwGenericAxisParamTypeRef(self, ref: RefType):
        self.swGenericAxisParamTypeRef = ref
        return self

    def setSwRecordLayoutComponent(self, component: ARLiteral):
        self.swRecordLayoutComponent = component
        return self

    def setSwRecordLayoutGroupAxis(self, axis: ARNumerical):
        self.swRecordLayoutGroupAxis = axis
        return self

    def setSwRecordLayoutGroupIndex(self, index: ARLiteral):
        self.swRecordLayoutGroupIndex = index
        return self

    def setSwRecordLayoutGroupFrom(self, from_value: ARLiteral):
        self.swRecordLayoutGroupFrom = from_value
        return self

    def setSwRecordLayoutGroupTo(self, to_value: ARLiteral):
        self.swRecordLayoutGroupTo = to_value
        return self

    def setSwRecordLayoutGroupContentType(self, content_type: SwRecordLayoutGroupContent):
        self.swRecordLayoutGroupContentType = content_type
        return self




class SwRecordLayout(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swRecordLayoutGroup = None                 # type: SwRecordLayoutGroup

    def setSwRecordLayoutGroup(self, group: SwRecordLayoutGroup):
        self.swRecordLayoutGroup = group
        return self