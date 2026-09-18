from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType


class AxisIndexType(ARLiteral):
    """
    This meta-class specifies an axis in a curve/map data object. The index satisfies the following convention: • 0 output "axis" • 1 input axis 1 (X input axis e.g. of a CURVE) • 2 input axis 2 (Y input axis e.g. of a MAP) • 3 input axis 3 (Z input axis e.g. of a CUBOID) • 4 input axis 3 (Z4 input axis e.g. of a CUBE_4) • 5 input axis 3 (Z5 input axis e.g. of a CUBE_5) • 6..9 etc. The output "axis" provides access to the output value of the parameter. Note that this access is usually performed via an index according to the input axis. In addition to this, the Values STRING and ARRAY support specific iterations.

    Tags:
        * xml.xsd.customType=AXIS-INDEX-TYPE
        * xml.xsd.pattern=[0-9]+|STRING|ARRAY
        * xml.xsd.type=string
    """

    # AxisIndexType method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.43, p.108
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer


class SwRecordLayoutV(ARObject):
    """
    Variable definition within a record layout including base type, axis,
    and value properties.
    """

    # SwRecordLayoutV method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseTypeRef               [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseTypeRef               [x] impl  [ ] docstring  [ ] test
    # [ ] getDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] setDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] getSwGenericAxisParamTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] setSwGenericAxisParamTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutVAxis       [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutVAxis       [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutVFixValue   [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutVFixValue   [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutVIndex      [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutVIndex      [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutVProp       [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutVProp       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.baseTypeRef = None  # type: RefType
        self.desc = None  # type: MultiLanguageOverviewParagraph
        self.shortLabel = None  # type: ARLiteral
        self.swGenericAxisParamTypeRef = None  # type: RefType
        self.swRecordLayoutVAxis = None  # type: ARNumerical
        self.swRecordLayoutVFixValue = None  # type: ARNumerical
        self.swRecordLayoutVIndex = None  # type: ARLiteral
        self.swRecordLayoutVProp = None  # type: ARLiteral

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
    """
    This is the contents of a RecordLayout which is inserted for every iteration. Note that since this is atp Mixed, multiple properties can be inserted for each iteration.
    """

    # SwRecordLayoutGroupContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.100, p.424
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutGroup [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutGroup [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutV    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutV    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This association allows to support reusable "sub"-record layouts. In particular, the contents of the referenced record layout shall be used as if the record layout group in the referenced record layout was aggregated in the current record layout group. So, semantically it would be equivalent to replace the particular association with an aggregation of the sw RecordLayoutGroup of the referenced SwRecordLayout.
        self.swRecordLayoutRef: Optional[RefType] = None

        # This aggregation provides support for nested iterations. For example, if a map is to be handled, then we might have two nested SwRecordLayoutGroups, one for the x-axis and one for the y-axis. The inner iteration runs faster.
        self.swRecordLayoutGroup: Optional[SwRecordLayoutGroup] = None

        # Particular Value specification for this record layout group.
        self.swRecordLayoutV: Optional[SwRecordLayoutV] = None

    def getSwRecordLayoutRef(self) -> Optional[RefType]:
        """This association allows to support reusable \"sub\"-record layouts. In particular, the contents of the referenced record layout shall be used as if the record layout group in the referenced record layout was aggregated in the current record layout group. So, semantically it would be equivalent to replace the particular association with an aggregation of the sw RecordLayoutGroup of the referenced SwRecordLayout."""
        return self.swRecordLayoutRef

    def setSwRecordLayoutRef(self, value: Optional[RefType]) -> "SwRecordLayoutGroupContent":
        """This association allows to support reusable \"sub\"-record layouts. In particular, the contents of the referenced record layout shall be used as if the record layout group in the referenced record layout was aggregated in the current record layout group. So, semantically it would be equivalent to replace the particular association with an aggregation of the sw RecordLayoutGroup of the referenced SwRecordLayout. A None value is a no-op and does not overwrite an existing swRecordLayoutRef."""
        if value is not None:
            self.swRecordLayoutRef = value
        return self

    def getSwRecordLayoutGroup(self) -> Optional["SwRecordLayoutGroup"]:
        """This aggregation provides support for nested iterations. For example, if a map is to be handled, then we might have two nested SwRecordLayoutGroups, one for the x-axis and one for the y-axis. The inner iteration runs faster."""
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value: Optional["SwRecordLayoutGroup"]) -> "SwRecordLayoutGroupContent":
        """This aggregation provides support for nested iterations. For example, if a map is to be handled, then we might have two nested SwRecordLayoutGroups, one for the x-axis and one for the y-axis. The inner iteration runs faster. A None value is a no-op and does not overwrite an existing swRecordLayoutGroup."""
        if value is not None:
            self.swRecordLayoutGroup = value
        return self

    def getSwRecordLayoutV(self) -> Optional[SwRecordLayoutV]:
        """Particular Value specification for this record layout group."""
        return self.swRecordLayoutV

    def setSwRecordLayoutV(self, value: Optional[SwRecordLayoutV]) -> "SwRecordLayoutGroupContent":
        """Particular Value specification for this record layout group. A None value is a no-op and does not overwrite an existing swRecordLayoutV."""
        if value is not None:
            self.swRecordLayoutV = value
        return self


class SwRecordLayoutGroup(ARObject):
    """
    Group within a record layout defining axis, category, and indexing
    properties.
    """

    # SwRecordLayoutGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCategory                  [x] impl  [ ] docstring  [ ] test
    # [ ] setCategory                  [x] impl  [ ] docstring  [ ] test
    # [ ] getDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] setDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] getSwGenericAxisParamTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] setSwGenericAxisParamTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutComponent   [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutComponent   [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupAxis   [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupAxis   [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupContentType [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupContentType [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupFrom   [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupFrom   [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupIndex  [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupIndex  [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupStep   [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupStep   [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroupTo     [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroupTo     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.category = None  # type: ARLiteral
        self.desc = None  # type: MultiLanguageOverviewParagraph
        self.shortLabel = None  # type: ARLiteral
        self.swGenericAxisParamTypeRef = None  # type: RefType
        self.swRecordLayoutComponent = None  # type: ARLiteral
        self.swRecordLayoutGroupAxis = None  # type: AxisIndexType
        self.swRecordLayoutGroupContentType = None  # type: SwRecordLayoutGroupContent
        self.swRecordLayoutGroupFrom = None  # type: ARLiteral
        self.swRecordLayoutGroupIndex = None  # type: ARLiteral
        self.swRecordLayoutGroupStep = None  # type: Integer
        self.swRecordLayoutGroupTo = None  # type: ARLiteral

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
    """
    Record layout element defining the structure of calibration data in
    memory.
    """

    # SwRecordLayout method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutGroup       [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutGroup       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swRecordLayoutGroup: Optional[SwRecordLayoutGroup] = None

    def getSwRecordLayoutGroup(self):
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value):
        self.swRecordLayoutGroup = value
        return self
