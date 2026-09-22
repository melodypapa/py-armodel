from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Identifier, Integer, NameToken, NameTokens, RefType
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


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
    This element specifies which values are stored for the current SwRecordLayoutGroup. If no baseType is present, the SwBaseType referenced initially in the parent SwRecordLayoutGroup is valid. The specification of swRecordLayoutVAxis gives the axis of the values which shall be stored in accordance with the current record layout SwRecordLayoutGroup. In swRecordLayoutVProp one can specify the information which shall be stored.
    """

    # SwRecordLayoutV method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.98, p.422
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseTypeRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseTypeRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDesc                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDesc                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabel                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwGenericAxisParamTypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwGenericAxisParamTypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutVAxis            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutVAxis            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutVFixValue        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutVFixValue        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutVIndex           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutVIndex           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutVProp            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutVProp            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This association allows to refer to a base type in case a specific encoding is intended. If no base type is referred, the base type referenced initially in the corresponding DataPrototype is to be used. Tags: xml.sequenceOffset=30
        self.baseTypeRef: Optional[RefType] = None

        # This aggregation allows for a brief description about the particular record layout value which can help to identify the entry. In-depth documentation should be added to the introduction of the surrounding record layout. Tags: xml.sequenceOffset=20
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This attribute specifies a name which can be used e.g. when ECU code is generated from the record layout value. Tags: xml.sequenceOffset=3
        self.shortLabel: Optional[Identifier] = None

        # This association supports the case that a value from a generic axis definition shall be stored. This value is denoted by a particular generic axis parameter type. Tags: xml.sequenceOffset=70
        self.swGenericAxisParamTypeRef: Optional[RefType] = None

        # This attribute gives the index of the axis of which values that are stored in the record. swRecordVIndex refers to the symbolic names of the iterators for which the axis value shall be stored in the record. In case of nested iterators (mainly for multidimensional objects) the iterator names are specified as whitespace-separated names. These symbolic names relate to swRecordLayoutGroup Index. The iterators are processed from left to right in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if more components are specified than axes exist in the related ApplicationDataType. Tags: xml.sequenceOffset=40
        self.swRecordLayoutVAxis: Optional[AxisIndexType] = None

        # This attribute specifies the filler character for the current record layout, in the form of hex digits. It is also used to specify the fix value for e.g. FIXRIGHTDIFF. Tags: xml.sequenceOffset=80
        self.swRecordLayoutVFixValue: Optional[Integer] = None

        # The symbolic value for iteration, or the symbolic values separated by whitespaces, refer to the symbolic values given in swRecordLayoutGroupIndex . The iterators are processed from left to right, in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if the record layout is referenced by an entity which has less number of axes than index names referenced here. Tags: xml.sequenceOffset=60
        self.swRecordLayoutVIndex: Optional[NameTokens] = None

        # This attribute describes the kind of values to be stored. More details see below. The standardized values foreseen for this attribute are defined in [TPS_SWCT_01489]. Tags: xml.sequenceOffset=50
        self.swRecordLayoutVProp: Optional[NameToken] = None

    def getBaseTypeRef(self) -> Optional[RefType]:
        """This association allows to refer to a base type in case a specific encoding is intended. If no base type is referred, the base type referenced initially in the corresponding DataPrototype is to be used. Tags: xml.sequenceOffset=30"""
        return self.baseTypeRef

    def setBaseTypeRef(self, value: Optional[RefType]) -> "SwRecordLayoutV":
        """This association allows to refer to a base type in case a specific encoding is intended. If no base type is referred, the base type referenced initially in the corresponding DataPrototype is to be used. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing baseTypeRef."""
        if value is not None:
            self.baseTypeRef = value
        return self

    def getDesc(self):
        """This aggregation allows for a brief description about the particular record layout value which can help to identify the entry. In-depth documentation should be added to the introduction of the surrounding record layout. Tags: xml.sequenceOffset=20"""
        return self.desc

    def setDesc(self, value):
        """This aggregation allows for a brief description about the particular record layout value which can help to identify the entry. In-depth documentation should be added to the introduction of the surrounding record layout. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing desc."""
        if value is not None:
            self.desc = value
        return self

    def getShortLabel(self):
        """This attribute specifies a name which can be used e.g. when ECU code is generated from the record layout value. Tags: xml.sequenceOffset=3"""
        return self.shortLabel

    def setShortLabel(self, value):
        """This attribute specifies a name which can be used e.g. when ECU code is generated from the record layout value. Tags: xml.sequenceOffset=3. A None value is a no-op and does not overwrite an existing shortLabel."""
        if value is not None:
            self.shortLabel = value
        return self

    def getSwGenericAxisParamTypeRef(self):
        """This association supports the case that a value from a generic axis definition shall be stored. This value is denoted by a particular generic axis parameter type. Tags: xml.sequenceOffset=70"""
        return self.swGenericAxisParamTypeRef

    def setSwGenericAxisParamTypeRef(self, value):
        """This association supports the case that a value from a generic axis definition shall be stored. This value is denoted by a particular generic axis parameter type. Tags: xml.sequenceOffset=70. A None value is a no-op and does not overwrite an existing swGenericAxisParamTypeRef."""
        if value is not None:
            self.swGenericAxisParamTypeRef = value
        return self

    def getSwRecordLayoutVAxis(self):
        """This attribute gives the index of the axis of which values that are stored in the record. swRecordVIndex refers to the symbolic names of the iterators for which the axis value shall be stored in the record. In case of nested iterators (mainly for multidimensional objects) the iterator names are specified as whitespace-separated names. These symbolic names relate to swRecordLayoutGroup Index. The iterators are processed from left to right in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if more components are specified than axes exist in the related ApplicationDataType. Tags: xml.sequenceOffset=40"""
        return self.swRecordLayoutVAxis

    def setSwRecordLayoutVAxis(self, value):
        """This attribute gives the index of the axis of which values that are stored in the record. swRecordVIndex refers to the symbolic names of the iterators for which the axis value shall be stored in the record. In case of nested iterators (mainly for multidimensional objects) the iterator names are specified as whitespace-separated names. These symbolic names relate to swRecordLayoutGroup Index. The iterators are processed from left to right in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if more components are specified than axes exist in the related ApplicationDataType. Tags: xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing swRecordLayoutVAxis."""
        if value is not None:
            self.swRecordLayoutVAxis = value
        return self

    def getSwRecordLayoutVFixValue(self):
        """This attribute specifies the filler character for the current record layout, in the form of hex digits. It is also used to specify the fix value for e.g. FIXRIGHTDIFF. Tags: xml.sequenceOffset=80"""
        return self.swRecordLayoutVFixValue

    def setSwRecordLayoutVFixValue(self, value):
        """This attribute specifies the filler character for the current record layout, in the form of hex digits. It is also used to specify the fix value for e.g. FIXRIGHTDIFF. Tags: xml.sequenceOffset=80. A None value is a no-op and does not overwrite an existing swRecordLayoutVFixValue."""
        if value is not None:
            self.swRecordLayoutVFixValue = value
        return self

    def getSwRecordLayoutVIndex(self):
        """The symbolic value for iteration, or the symbolic values separated by whitespaces, refer to the symbolic values given in swRecordLayoutGroupIndex . The iterators are processed from left to right, in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if the record layout is referenced by an entity which has less number of axes than index names referenced here. Tags: xml.sequenceOffset=60"""
        return self.swRecordLayoutVIndex

    def setSwRecordLayoutVIndex(self, value):
        """The symbolic value for iteration, or the symbolic values separated by whitespaces, refer to the symbolic values given in swRecordLayoutGroupIndex . The iterators are processed from left to right, in such a manner that they symbolize the loop index from the outside to the inside. It is considered an error if the record layout is referenced by an entity which has less number of axes than index names referenced here. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing swRecordLayoutVIndex."""
        if value is not None:
            self.swRecordLayoutVIndex = value
        return self

    def getSwRecordLayoutVProp(self):
        """This attribute describes the kind of values to be stored. More details see below. The standardized values foreseen for this attribute are defined in [TPS_SWCT_01489]. Tags: xml.sequenceOffset=50"""
        return self.swRecordLayoutVProp

    def setSwRecordLayoutVProp(self, value):
        """This attribute describes the kind of values to be stored. More details see below. The standardized values foreseen for this attribute are defined in [TPS_SWCT_01489]. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing swRecordLayoutVProp."""
        if value is not None:
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
    Defines how the data objects (variables, calibration parameters etc.) are to be stored in the ECU memory. As an example, this definition specifies the sequence of axis points in the ECU memory. Iterations through axis values are stored within the sub-elements swRecordLayoutGroup. Tags: atp.recommendedPackage=SwRecordLayouts
    """

    # SwRecordLayout method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.97, p.421
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwRecordLayoutGroup [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwRecordLayoutGroup [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the top level record layout group. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.swRecordLayoutGroup: Optional[SwRecordLayoutGroup] = None

    def getSwRecordLayoutGroup(self) -> Optional[SwRecordLayoutGroup]:
        """This is the top level record layout group. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false"""
        return self.swRecordLayoutGroup

    def setSwRecordLayoutGroup(self, value: Optional[SwRecordLayoutGroup]) -> "SwRecordLayout":
        """This is the top level record layout group. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false. A None value is a no-op and does not overwrite an existing swRecordLayoutGroup."""
        if value is not None:
            self.swRecordLayoutGroup = value
        return self
