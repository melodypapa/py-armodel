from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class SwRecordLayoutV(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.baseTypeRef: Union[RefType, None] = None
        self.desc: Union[MultiLanguageOverviewParagraph, None] = None
        self.shortLabel: Union[ARLiteral, None] = None
        self.swGenericAxisParamTypeRef: Union[RefType, None] = None
        self.swRecordLayoutVAxis: Union[ARNumerical, None] = None
        self.swRecordLayoutVFixValue: Union[ARNumerical, None] = None
        self.swRecordLayoutVIndex: Union[ARLiteral, None] = None
        self.swRecordLayoutVProp: Union[ARLiteral, None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.swRecordLayoutRef: Union[RefType, None] = None
        self.swRecordLayoutGroup: Union[SwRecordLayoutGroup, None] = None
        self.swRecordLayoutV: Union[SwRecordLayoutV, None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.category: Union[ARLiteral, None] = None
        self.desc: Union[MultiLanguageOverviewParagraph, None] = None
        self.shortLabel: Union[ARLiteral, None] = None
        self.swGenericAxisParamTypeRef: Union[RefType, None] = None
        self.swRecordLayoutComponent: Union[ARLiteral, None] = None
        self.swRecordLayoutGroupAxis: Union[AxisIndexType, None] = None
        self.swRecordLayoutGroupContentType: Union[SwRecordLayoutGroupContent, None] = None
        self.swRecordLayoutGroupFrom: Union[ARLiteral, None] = None
        self.swRecordLayoutGroupIndex: Union[ARLiteral, None] = None
        self.swRecordLayoutGroupStep: Union[Integer, None] = None
        self.swRecordLayoutGroupTo: Union[ARLiteral, None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.swRecordLayoutGroup: Union[SwRecordLayoutGroup, None] = None

    def getSwRecordLayoutGroup(self):
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value):
        self.swRecordLayoutGroup = value
        return self
