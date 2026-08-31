from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARNumerical,
    Float,
    AlignmentType,
    Boolean,
    Identifier,
    Integer,
    NativeDeclarationString,
    Numerical,
    PrimitiveIdentifier,
    RefType,
    DisplayFormatString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
    from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisSet


class SwImplPolicyEnum(AREnum):
    """
    Enumeration for software implementation policy.
    * const
        forced implementation such that the running software within the ECU shall not modify it. For example
        implemented with the "const" modifier in C. This can be applied for parameters (not for those in
        NVRAM) as well as argument data prototypes.
    * fixed
        This data element is fixed. In particular this indicates, that it might also be implemented e.g. as in
        place data, (#DEFINE).
    * measurementPoint
        The data element is created for measurement purposes only. The data element is never read directly
        within the ECU software. In contrast to a "standard" data element in an unconnected provide port is,
        this unconnection is guaranteed for measurementPoint data elements.
    * queued
        The content of the data element is queued and the data element has 'event' semantics, i.e. data
        elements are stored in a queue and all data elements are processed in 'first in first out' order. The
        queuing is intended to be implemented by RTE Generator. This value is not applicable for parameters.
    * standard
        This is applicable for all kinds of data elements. For variable data prototypes the 'last is best'
        semantics applies. For parameter there is no specific implementation directive.
    """

    # SwImplPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.45, p.336
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwDataDefProps.swImplPolicy
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    CONST = "const"
    FIXED = "fixed"
    MEASUREMENT_POINT = "measurementPoint"
    QUEUED = "queued"
    STANDARD = "standard"

    def __init__(self):
        super().__init__([SwImplPolicyEnum.CONST, SwImplPolicyEnum.FIXED, SwImplPolicyEnum.MEASUREMENT_POINT, SwImplPolicyEnum.QUEUED, SwImplPolicyEnum.STANDARD])


class SwCalibrationAccessEnum(AREnum):
    """
    Determines the access rights to a data object w.r.t. measurement and calibration.
    """

    # SwCalibrationAccessEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.44, p.335
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwDataDefProps.swCalibrationAccess
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The element will not be accessible via MCD tools, i.e. will not appear in the ASAP file. Tags: atp.EnumerationLiteralIndex=0
    NOT_ACCESSIBLE = "notAccessible"

    # The element will only appear as read-only in an ASAP file. Tags: atp.EnumerationLiteralIndex=1
    READ_ONLY = "readOnly"

    # The element will appear in the ASAP file with both read and write access. Tags: atp.EnumerationLiteralIndex=2
    READ_WRITE = "readWrite"

    def __init__(self):
        super().__init__([SwCalibrationAccessEnum.NOT_ACCESSIBLE, SwCalibrationAccessEnum.READ_ONLY, SwCalibrationAccessEnum.READ_WRITE])


class DisplayPresentationEnum(AREnum):
    """
    This meta-class represents the ability to provide values for controlling the presentation of data within measurement and calibration tools.
    """

    # DisplayPresentationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.107, p.432
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwDataDefProps.displayPresentation
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The presentation of data shall form a continuous graph between data points. Tags: atp.EnumerationLiteralIndex=0
    PRESENTATION_CONTINUOUS = "presentationContinuous"

    # The presentation of data shall be step-shaped between data points. Tags: atp.EnumerationLiteralIndex=1
    PRESENTATION_DISCRETE = "presentationDiscrete"

    def __init__(self):
        super().__init__([DisplayPresentationEnum.PRESENTATION_CONTINUOUS, DisplayPresentationEnum.PRESENTATION_DISCRETE])


class SwBitRepresentation(ARObject):
    """
    Description of the structure of a bit variable: Comprises of the bitPosition in a memory object (e.g. sw HostVariable, which stands parallel to swBitRepresentation) and the numberOfBits . In this way, interrelated memory areas can be described. Non-related memory areas are not supported.
    """

    # SwBitRepresentation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.41, p.333
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBitPosition           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitPosition           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNumberOfBits          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNumberOfBits          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # If the "bit data object" is hosted within another data object (e.g. if the memory can be accessed via byte as well as bit address), this attribute specifies the position of the data object. The count starts at zero (0). Tags: xml.sequenceOffset=20
        self.bitPosition: Optional[Integer] = None

        # Number of bits allocated by a "bit data object" within its host data object. Tags: xml.sequenceOffset=30
        self.numberOfBits: Optional[Integer] = None

    def getBitPosition(self) -> Optional[Integer]:
        """
        If the "bit data object" is hosted within another data object (e.g. if the memory can be accessed via byte as well as bit address), this attribute specifies the position of the data object. The count starts at zero (0).
        """
        return self.bitPosition

    def setBitPosition(self, value: Optional[Integer]) -> "SwBitRepresentation":
        """
        If the "bit data object" is hosted within another data object (e.g. if the memory can be accessed via byte as well as bit address), this attribute specifies the position of the data object. The count starts at zero (0). A None value is a no-op and does not overwrite an existing bitPosition.
        """
        if value is not None:
            self.bitPosition = value
        return self

    def getNumberOfBits(self) -> Optional[Integer]:
        """
        Number of bits allocated by a "bit data object" within its host data object.
        """
        return self.numberOfBits

    def setNumberOfBits(self, value: Optional[Integer]) -> "SwBitRepresentation":
        """
        Number of bits allocated by a "bit data object" within its host data object. A None value is a no-op and does not overwrite an existing numberOfBits.
        """
        if value is not None:
            self.numberOfBits = value
        return self


class SwDataDependencyArgs(ARObject):
    """
    This element specifies the elements used in a SwDataDependency.
    """

    # SwDataDependencyArgs method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.59, p.374
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwCalprmRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwCalprmRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwVariable            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwVariable            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies a calibration parameter as an input argument to the dependency.
        self.swCalprmRef: Optional[SwCalprmRefProxy] = None

        # Specifies a variable as an input argument to the dependency.
        self.swVariable: Optional[SwVariableRefProxy] = None

    def getSwCalprmRef(self) -> Optional[SwCalprmRefProxy]:
        """
        Specifies a calibration parameter as an input argument to the dependency.
        """
        return self.swCalprmRef

    def setSwCalprmRef(self, value: Optional[SwCalprmRefProxy]) -> "SwDataDependencyArgs":
        """
        Specifies a calibration parameter as an input argument to the dependency. A None value is a no-op and does not overwrite an existing swCalprmRef.
        """
        if value is not None:
            self.swCalprmRef = value
        return self

    def getSwVariable(self) -> Optional[SwVariableRefProxy]:
        """
        Specifies a variable as an input argument to the dependency.
        """
        return self.swVariable

    def setSwVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDependencyArgs":
        """
        Specifies a variable as an input argument to the dependency. A None value is a no-op and does not overwrite an existing swVariable.
        """
        if value is not None:
            self.swVariable = value
        return self


class CompuGenericMath(ARObject):
    """
    This meta-class represents the ability to specify a generic formula expression.
    """

    # CompuGenericMath method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.60, p.374
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLevel                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLevel                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases.
        self.level: Optional[PrimitiveIdentifier] = None

    def getLevel(self) -> Optional[PrimitiveIdentifier]:
        """
        Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases.
        """
        return self.level

    def setLevel(self, value: Optional[PrimitiveIdentifier]) -> "CompuGenericMath":
        """
        Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases. A None value is a no-op and does not overwrite an existing level.
        """
        if value is not None:
            self.level = value
        return self


class SwDataDependency(ARObject):
    """
    This element describes the interdependencies of data objects, e.g. variables and parameters. Use cases: • Calculate the value of a calibration parameter (by the MCD system) from the value(s) of other calibration parameters. • Virtual data - that means the data object is not directly in the ecu and this property describes how the "virtual variable" can be computed from the real ones (by the MCD system).
    """

    # SwDataDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.58, p.374
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwDataDependencyFormula     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDependencyFormula     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwDataDependencyArgs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDependencyArgs        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This element describes the formula with which the dependencies between the participating objects are defined.
        self.swDataDependencyFormula: Optional[CompuGenericMath] = None

        # Specifies the arguments used in the data dependency. Note that this is 0..1 since the aggregated class is a container (atpMixed).
        self.swDataDependencyArgs: Optional[SwDataDependencyArgs] = None

    def getSwDataDependencyFormula(self) -> Optional[CompuGenericMath]:
        """
        This element describes the formula with which the dependencies between the participating objects are defined.
        """
        return self.swDataDependencyFormula

    def setSwDataDependencyFormula(self, value: Optional[CompuGenericMath]) -> "SwDataDependency":
        """
        This element describes the formula with which the dependencies between the participating objects are defined. A None value is a no-op and does not overwrite an existing swDataDependencyFormula.
        """
        if value is not None:
            self.swDataDependencyFormula = value
        return self

    def getSwDataDependencyArgs(self) -> Optional[SwDataDependencyArgs]:
        """
        Specifies the arguments used in the data dependency. Note that this is 0..1 since the aggregated class is a container (atpMixed).
        """
        return self.swDataDependencyArgs

    def setSwDataDependencyArgs(self, value: Optional[SwDataDependencyArgs]) -> "SwDataDependency":
        """
        Specifies the arguments used in the data dependency. Note that this is 0..1 since the aggregated class is a container (atpMixed). A None value is a no-op and does not overwrite an existing swDataDependencyArgs.
        """
        if value is not None:
            self.swDataDependencyArgs = value
        return self


class SwDataDefProps(ARObject):
    """
    This class is a collection of properties relevant for data objects under various aspects. One could consider this class as a "pattern of inheritance by aggregation". The properties can be applied to all objects of all classes in which SwDataDefProps is aggregated. Note that not all of the attributes or associated elements are useful all of the time. Hence, the process definition (e.g. expressed with an OCL or a Document Control Instance MSR-DCI) has the task of implementing limitations. SwDataDefProps covers various aspects: • Structure of the data element for calibration use cases: is it a single value, a curve, or a map, but also the recordLayouts which specify how such elements are mapped/converted to the DataTypes in the programming language (or in AUTOSAR). This is mainly expressed by properties like swRecordLayout and swCalprmAxisSet • Implementation aspects, mainly expressed by swImplPolicy, swVariableAccessImplPolicy, swAddr Method, swPointerTagetProps, baseType, implementationDataType and additionalNativeTypeQualifier • Access policy for the MCD system, mainly expressed by swCalibrationAccess • Semantics of the data element, mainly expressed by compuMethod and/or unit, dataConstr, invalid Value • Code generation policy provided by swRecordLayout
    """

    # SwDataDefProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.39, p.332
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDisplayPresentation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDisplayPresentation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStepSize                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStepSize                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwValueBlockSizeMults       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwValueBlockSizeMult        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAnnotations                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAnnotation                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwAddrMethodRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwAddrMethodRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwAlignment                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwAlignment                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBaseTypeRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseTypeRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwBitRepresentation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwBitRepresentation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCalibrationAccess         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwCalibrationAccess         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwValueBlockSize            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwValueBlockSize            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCalprmAxisSet             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwCalprmAxisSet             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwTextProps                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwTextProps                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwComparisonVariables       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwComparisonVariable        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCompuMethodRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCompuMethodRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataConstrRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataConstrRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwDataDependency            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDependency            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDisplayFormat               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDisplayFormat               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplementationDataTypeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplementationDataTypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwHostVariable              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwHostVariable              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwImplPolicy                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwImplPolicy                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAdditionalNativeTypeQualifier [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAdditionalNativeTypeQualifier [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwIntendedResolution        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwIntendedResolution        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwInterpolationMethod       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwInterpolationMethod       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInvalidValue                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInvalidValue                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwIsVirtual                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwIsVirtual                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwPointerTargetProps        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwPointerTargetProps        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwRecordLayoutRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwRecordLayoutRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwRefreshTiming             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwRefreshTiming             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnitRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnitRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValueAxisDataTypeRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValueAxisDataTypeRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute controls the presentation of the related data for measurement and calibration tools.
        self.displayPresentation: Optional[DisplayPresentationEnum] = None

        # This attribute can be used to define a value which is added to or subtracted from the value of a DataPrototype when using up/down keys while calibrating.
        self.stepSize: Optional[Float] = None

        # This attribute is used to specify the dimensions of a value block (VAL_BLK) for the case that that value block has more than one dimension. The dimensions given in this attribute are ordered such that the first entry represents the first dimension, the second entry represents the second dimension, and so on. For one-dimensional value blocks the attribute swValueBlockSize shall be used and this attribute shall not exist.
        self.swValueBlockSizeMults: List[ARNumerical] = []

        # This aggregation allows to add annotations (yellow pads ...) related to the current data object.
        self.annotations: List[Annotation] = []

        # Addressing method related to this data object. Via an association to the same SwAddrMethod it can be specified that several DataPrototypes shall be located in the same memory without already specifying the memory section itself.
        self.swAddrMethodRef: Optional[RefType] = None

        # The attribute describes the intended typical alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod.
        self.swAlignment: Optional[AlignmentType] = None

        # Base type associated with the containing data object.
        self.baseTypeRef: Optional[RefType] = None

        # Description of the binary representation in case of a bit variable.
        self.swBitRepresentation: Optional[SwBitRepresentation] = None

        # Specifies the read or write access by MCD tools for this data object.
        self.swCalibrationAccess: Optional[SwCalibrationAccessEnum] = None

        # This represents the size of a Value Block
        self.swValueBlockSize: Optional[ARNumerical] = None

        # This specifies the properties of the axes in case of a curve or map etc. This is mainly applicable to calibration parameters.
        self.swCalprmAxisSet: Optional[SwCalprmAxisSet] = None

        # the specific properties if the data object is a text object.
        self.swTextProps: Optional[SwTextProps] = None

        # Variables used for comparison in an MCD process.
        self.swComparisonVariables: List[SwVariableRefProxy] = []

        # Computation method associated with the semantics of this data object.
        self.compuMethodRef: Optional[RefType] = None

        # Data constraint for this data object.
        self.dataConstrRef: Optional[RefType] = None

        # Describes how the value of the data object has to be calculated from the value of another data object (by the MCD system).
        self.swDataDependency: Optional[SwDataDependency] = None

        # This property describes how a number is to be rendered e.g. in documents or in a measurement and calibration system.
        self.displayFormat: Optional[DisplayFormatString] = None

        # This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps. It is used whenever a data declaration is not directly referring to a base type. Especially • redefinition of an ImplementationDataType via a "typedef" to another ImplementationDatatype • the target type of a pointer (see SwPointerTargetProps), if it does not refer to a base type directly • the data type of an array or record element within an ImplementationDataType, if it does not refer to a base type directly • the data type of an SwServiceArg, if it does not refer to a base type directly
        self.implementationDataTypeRef: Optional[RefType] = None

        # Contains a reference to a variable which serves as a host-variable for a bit variable. Only applicable to bit objects.
        self.swHostVariable: Optional[SwVariableRefProxy] = None

        # Implementation policy for this data object.
        self.swImplPolicy: Optional[SwImplPolicyEnum] = None

        # This attribute is used to declare native qualifiers of the programming language which can neither be deduced from the baseType (e.g. because the data object describes a pointer) nor from other more abstract attributes. Examples are qualifiers like "volatile", "strict" or "enum" of the C-language. All such declarations have to be put into one string.
        self.additionalNativeTypeQualifier: Optional[NativeDeclarationString] = None

        # The purpose of this element is to describe the requested quantization of data objects early on in the design process. The resolution ultimately occurs via the conversion formula present (compuMethod), which specifies the transition from the physical world to the standardized world (and vice-versa) (here, "the slope per bit" is present implicitly in the conversion formula). In the case of a development phase without a fixed conversion formula, a pre-specification can occur through swIntendedResolution. The resolution is specified in the physical domain according to the property "unit".
        self.swIntendedResolution: Optional[ARNumerical] = None

        # This is a keyword identifying the mathematical method to be applied for interpolation. The keyword needs to be related to the interpolation routine which needs to be invoked.
        self.swInterpolationMethod: Optional[Identifier] = None

        # Optional value to express invalidity of the actual data element.
        self.invalidValue: Optional[ValueSpecification] = None

        # This element distinguishes virtual objects. Virtual objects do not appear in the memory, their derivation is much more dependent on other objects and hence they shall have a swDataDependency.
        self.swIsVirtual: Optional[Boolean] = None

        # Specifies that the containing data object is a pointer to another data object. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern).
        self.swPointerTargetProps: Optional[SwPointerTargetProps] = None

        # Record layout for this data object.
        self.swRecordLayoutRef: Optional[RefType] = None

        # This element specifies the frequency in which the object involved shall be or is called or calculated. This timing can be collected from the task in which write access processes to the variable run. But this cannot be done by the MCD system. So this attribute can be used in an early phase to express the desired refresh timing and later on to specify the real refresh timing.
        self.swRefreshTiming: Optional[MultidimensionalTime] = None

        # Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified. If both units (this as well as via compuMethod) are specified the units shall be compatible.
        self.unitRef: Optional[RefType] = None

        # The referenced ApplicationPrimitiveDataType represents the primitive data type of the value axis within a compound primitive (e.g. curve, map). It supersedes CompuMethod, Unit, and BaseType.
        self.valueAxisDataTypeRef: Optional[RefType] = None

    def getDisplayPresentation(self) -> Optional[DisplayPresentationEnum]:
        """
        This attribute controls the presentation of the related data for measurement and calibration tools.
        """
        return self.displayPresentation

    def setDisplayPresentation(self, value: Optional[DisplayPresentationEnum]) -> "SwDataDefProps":
        """
        This attribute controls the presentation of the related data for measurement and calibration tools. A None value is a no-op and does not overwrite an existing displayPresentation.
        """
        if value is not None:
            self.displayPresentation = value
        return self

    def getStepSize(self) -> Optional[Float]:
        """
        This attribute can be used to define a value which is added to or subtracted from the value of a DataPrototype when using up/down keys while calibrating.
        """
        return self.stepSize

    def setStepSize(self, value: Optional[Float]) -> "SwDataDefProps":
        """
        This attribute can be used to define a value which is added to or subtracted from the value of a DataPrototype when using up/down keys while calibrating. A None value is a no-op and does not overwrite an existing stepSize.
        """
        if value is not None:
            self.stepSize = value
        return self

    def getSwValueBlockSizeMults(self) -> List[ARNumerical]:
        """
        This attribute is used to specify the dimensions of a value block (VAL_BLK) for the case that that value block has more than one dimension. The dimensions given in this attribute are ordered such that the first entry represents the first dimension, the second entry represents the second dimension, and so on. For one-dimensional value blocks the attribute swValueBlockSize shall be used and this attribute shall not exist.
        """
        return self.swValueBlockSizeMults

    def addSwValueBlockSizeMult(self, value: Optional[ARNumerical]) -> "SwDataDefProps":
        """
        This attribute is used to specify the dimensions of a value block (VAL_BLK) for the case that that value block has more than one dimension. Appends a dimension to the ordered list. A None value is a no-op.
        """
        if value is not None:
            self.swValueBlockSizeMults.append(value)
        return self

    def getAnnotations(self) -> List[Annotation]:
        """
        This aggregation allows to add annotations (yellow pads ...) related to the current data object.
        """
        return self.annotations

    def addAnnotation(self, annotation: Annotation) -> "SwDataDefProps":
        """
        This aggregation allows to add annotations (yellow pads ...) related to the current data object. A None value is a no-op.
        """
        if annotation is not None:
            self.annotations.append(annotation)
        return self

    def getSwAddrMethodRef(self) -> Optional[RefType]:
        """
        Addressing method related to this data object. Via an association to the same SwAddrMethod it can be specified that several DataPrototypes shall be located in the same memory without already specifying the memory section itself.
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Addressing method related to this data object. Via an association to the same SwAddrMethod it can be specified that several DataPrototypes shall be located in the same memory without already specifying the memory section itself. A None value is a no-op and does not overwrite an existing swAddrMethodRef.
        """
        if value is not None:
            self.swAddrMethodRef = value
        return self

    def getSwAlignment(self) -> Optional[AlignmentType]:
        """
        The attribute describes the intended typical alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod.
        """
        return self.swAlignment

    def setSwAlignment(self, value: Optional[AlignmentType]) -> "SwDataDefProps":
        """
        The attribute describes the intended typical alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod. A None value is a no-op and does not overwrite an existing swAlignment.
        """
        if value is not None:
            self.swAlignment = value
        return self

    def getBaseTypeRef(self) -> Optional[RefType]:
        """
        Base type associated with the containing data object.
        """
        return self.baseTypeRef

    def setBaseTypeRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Base type associated with the containing data object. A None value is a no-op and does not overwrite an existing baseTypeRef.
        """
        if value is not None:
            self.baseTypeRef = value
        return self

    def getSwBitRepresentation(self) -> Optional[SwBitRepresentation]:
        """
        Description of the binary representation in case of a bit variable.
        """
        return self.swBitRepresentation

    def setSwBitRepresentation(self, value: Optional[SwBitRepresentation]) -> "SwDataDefProps":
        """
        Description of the binary representation in case of a bit variable. A None value is a no-op and does not overwrite an existing swBitRepresentation.
        """
        if value is not None:
            self.swBitRepresentation = value
        return self

    def getSwCalibrationAccess(self) -> Optional[SwCalibrationAccessEnum]:
        """
        Specifies the read or write access by MCD tools for this data object.
        """
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value: Optional[SwCalibrationAccessEnum]) -> "SwDataDefProps":
        """
        Specifies the read or write access by MCD tools for this data object. A None value is a no-op and does not overwrite an existing swCalibrationAccess.
        """
        if value is not None:
            self.swCalibrationAccess = value
        return self

    def getSwValueBlockSize(self) -> Optional[ARNumerical]:
        """
        This represents the size of a Value Block
        """
        return self.swValueBlockSize

    def setSwValueBlockSize(self, value: Optional[ARNumerical]) -> "SwDataDefProps":
        """
        This represents the size of a Value Block A None value is a no-op and does not overwrite an existing swValueBlockSize.
        """
        if value is not None:
            self.swValueBlockSize = value
        return self

    def getSwCalprmAxisSet(self) -> Optional[SwCalprmAxisSet]:
        """
        This specifies the properties of the axes in case of a curve or map etc. This is mainly applicable to calibration parameters.
        """
        return self.swCalprmAxisSet

    def setSwCalprmAxisSet(self, value: Optional[SwCalprmAxisSet]) -> "SwDataDefProps":
        """
        This specifies the properties of the axes in case of a curve or map etc. This is mainly applicable to calibration parameters. A None value is a no-op and does not overwrite an existing swCalprmAxisSet.
        """
        if value is not None:
            self.swCalprmAxisSet = value
        return self

    def getSwTextProps(self) -> Optional[SwTextProps]:
        """
        the specific properties if the data object is a text object.
        """
        return self.swTextProps

    def setSwTextProps(self, value: Optional[SwTextProps]) -> "SwDataDefProps":
        """
        the specific properties if the data object is a text object. A None value is a no-op and does not overwrite an existing swTextProps.
        """
        if value is not None:
            self.swTextProps = value
        return self

    def getSwComparisonVariables(self) -> List[SwVariableRefProxy]:
        """
        Variables used for comparison in an MCD process.
        """
        return self.swComparisonVariables

    def addSwComparisonVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDefProps":
        """
        Variables used for comparison in an MCD process. Appends a comparison variable. A None value is a no-op.
        """
        if value is not None:
            self.swComparisonVariables.append(value)
        return self

    def getCompuMethodRef(self) -> Optional[RefType]:
        """
        Computation method associated with the semantics of this data object.
        """
        return self.compuMethodRef

    def setCompuMethodRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Computation method associated with the semantics of this data object. A None value is a no-op and does not overwrite an existing compuMethodRef.
        """
        if value is not None:
            self.compuMethodRef = value
        return self

    def getDataConstrRef(self) -> Optional[RefType]:
        """
        Data constraint for this data object.
        """
        return self.dataConstrRef

    def setDataConstrRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Data constraint for this data object. A None value is a no-op and does not overwrite an existing dataConstrRef.
        """
        if value is not None:
            self.dataConstrRef = value
        return self

    def getSwDataDependency(self) -> Optional[SwDataDependency]:
        """
        Describes how the value of the data object has to be calculated from the value of another data object (by the MCD system).
        """
        return self.swDataDependency

    def setSwDataDependency(self, value: Optional[SwDataDependency]) -> "SwDataDefProps":
        """
        Describes how the value of the data object has to be calculated from the value of another data object (by the MCD system). A None value is a no-op and does not overwrite an existing swDataDependency.
        """
        if value is not None:
            self.swDataDependency = value
        return self

    def getDisplayFormat(self) -> Optional[DisplayFormatString]:
        """
        This property describes how a number is to be rendered e.g. in documents or in a measurement and calibration system.
        """
        return self.displayFormat

    def setDisplayFormat(self, value: Optional[DisplayFormatString]) -> "SwDataDefProps":
        """
        This property describes how a number is to be rendered e.g. in documents or in a measurement and calibration system. A None value is a no-op and does not overwrite an existing displayFormat.
        """
        if value is not None:
            self.displayFormat = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps. It is used whenever a data declaration is not directly referring to a base type. Especially • redefinition of an ImplementationDataType via a "typedef" to another ImplementationDatatype • the target type of a pointer (see SwPointerTargetProps), if it does not refer to a base type directly • the data type of an array or record element within an ImplementationDataType, if it does not refer to a base type directly • the data type of an SwServiceArg, if it does not refer to a base type directly
        """
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps. It is used whenever a data declaration is not directly referring to a base type. Especially • redefinition of an ImplementationDataType via a "typedef" to another ImplementationDatatype • the target type of a pointer (see SwPointerTargetProps), if it does not refer to a base type directly • the data type of an array or record element within an ImplementationDataType, if it does not refer to a base type directly • the data type of an SwServiceArg, if it does not refer to a base type directly. A None value is a no-op and does not overwrite an existing implementationDataTypeRef.
        """
        if value is not None:
            self.implementationDataTypeRef = value
        return self

    def getSwHostVariable(self) -> Optional[SwVariableRefProxy]:
        """
        Contains a reference to a variable which serves as a host-variable for a bit variable. Only applicable to bit objects.
        """
        return self.swHostVariable

    def setSwHostVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDefProps":
        """
        Contains a reference to a variable which serves as a host-variable for a bit variable. Only applicable to bit objects. A None value is a no-op and does not overwrite an existing swHostVariable.
        """
        if value is not None:
            self.swHostVariable = value
        return self

    def getSwImplPolicy(self) -> Optional[SwImplPolicyEnum]:
        """
        Implementation policy for this data object.
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value: Optional[SwImplPolicyEnum]) -> "SwDataDefProps":
        """
        Implementation policy for this data object. A None value is a no-op and does not overwrite an existing swImplPolicy.
        """
        if value is not None:
            self.swImplPolicy = value
        return self

    def getAdditionalNativeTypeQualifier(self) -> Optional[NativeDeclarationString]:
        """
        This attribute is used to declare native qualifiers of the programming language which can neither be deduced from the baseType (e.g. because the data object describes a pointer) nor from other more abstract attributes. Examples are qualifiers like "volatile", "strict" or "enum" of the C-language. All such declarations have to be put into one string.
        """
        return self.additionalNativeTypeQualifier

    def setAdditionalNativeTypeQualifier(self, value: Optional[NativeDeclarationString]) -> "SwDataDefProps":
        """
        This attribute is used to declare native qualifiers of the programming language which can neither be deduced from the baseType (e.g. because the data object describes a pointer) nor from other more abstract attributes. Examples are qualifiers like "volatile", "strict" or "enum" of the C-language. All such declarations have to be put into one string. A None value is a no-op and does not overwrite an existing additionalNativeTypeQualifier.
        """
        if value is not None:
            self.additionalNativeTypeQualifier = value
        return self

    def getSwIntendedResolution(self) -> Optional[ARNumerical]:
        """
        The purpose of this element is to describe the requested quantization of data objects early on in the design process. The resolution ultimately occurs via the conversion formula present (compuMethod), which specifies the transition from the physical world to the standardized world (and vice-versa) (here, "the slope per bit" is present implicitly in the conversion formula). In the case of a development phase without a fixed conversion formula, a pre-specification can occur through swIntendedResolution. The resolution is specified in the physical domain according to the property "unit".
        """
        return self.swIntendedResolution

    def setSwIntendedResolution(self, value: Optional[ARNumerical]) -> "SwDataDefProps":
        """
        The purpose of this element is to describe the requested quantization of data objects early on in the design process. The resolution ultimately occurs via the conversion formula present (compuMethod), which specifies the transition from the physical world to the standardized world (and vice-versa) (here, "the slope per bit" is present implicitly in the conversion formula). In the case of a development phase without a fixed conversion formula, a pre-specification can occur through swIntendedResolution. The resolution is specified in the physical domain according to the property "unit". A None value is a no-op and does not overwrite an existing swIntendedResolution.
        """
        if value is not None:
            self.swIntendedResolution = value
        return self

    def getSwInterpolationMethod(self) -> Optional[Identifier]:
        """
        This is a keyword identifying the mathematical method to be applied for interpolation. The keyword needs to be related to the interpolation routine which needs to be invoked.
        """
        return self.swInterpolationMethod

    def setSwInterpolationMethod(self, value: Optional[Identifier]) -> "SwDataDefProps":
        """
        This is a keyword identifying the mathematical method to be applied for interpolation. The keyword needs to be related to the interpolation routine which needs to be invoked. A None value is a no-op and does not overwrite an existing swInterpolationMethod.
        """
        if value is not None:
            self.swInterpolationMethod = value
        return self

    def getInvalidValue(self) -> Optional[ValueSpecification]:
        """
        Optional value to express invalidity of the actual data element.
        """
        return self.invalidValue

    def setInvalidValue(self, value: Optional[ValueSpecification]) -> "SwDataDefProps":
        """
        Optional value to express invalidity of the actual data element. A None value is a no-op and does not overwrite an existing invalidValue.
        """
        if value is not None:
            self.invalidValue = value
        return self

    def getSwIsVirtual(self) -> Optional[Boolean]:
        """
        This element distinguishes virtual objects. Virtual objects do not appear in the memory, their derivation is much more dependent on other objects and hence they shall have a swDataDependency.
        """
        return self.swIsVirtual

    def setSwIsVirtual(self, value: Optional[Boolean]) -> "SwDataDefProps":
        """
        This element distinguishes virtual objects. Virtual objects do not appear in the memory, their derivation is much more dependent on other objects and hence they shall have a swDataDependency. A None value is a no-op and does not overwrite an existing swIsVirtual.
        """
        if value is not None:
            self.swIsVirtual = value
        return self

    def getSwPointerTargetProps(self) -> Optional[SwPointerTargetProps]:
        """
        Specifies that the containing data object is a pointer to another data object. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern).
        """
        return self.swPointerTargetProps

    def setSwPointerTargetProps(self, value: Optional[SwPointerTargetProps]) -> "SwDataDefProps":
        """
        Specifies that the containing data object is a pointer to another data object. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). A None value is a no-op and does not overwrite an existing swPointerTargetProps.
        """
        if value is not None:
            self.swPointerTargetProps = value
        return self

    def getSwRecordLayoutRef(self) -> Optional[RefType]:
        """
        Record layout for this data object.
        """
        return self.swRecordLayoutRef

    def setSwRecordLayoutRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Record layout for this data object. A None value is a no-op and does not overwrite an existing swRecordLayoutRef.
        """
        if value is not None:
            self.swRecordLayoutRef = value
        return self

    def getSwRefreshTiming(self) -> Optional[MultidimensionalTime]:
        """
        This element specifies the frequency in which the object involved shall be or is called or calculated. This timing can be collected from the task in which write access processes to the variable run. But this cannot be done by the MCD system. So this attribute can be used in an early phase to express the desired refresh timing and later on to specify the real refresh timing.
        """
        return self.swRefreshTiming

    def setSwRefreshTiming(self, value: Optional[MultidimensionalTime]) -> "SwDataDefProps":
        """
        This element specifies the frequency in which the object involved shall be or is called or calculated. This timing can be collected from the task in which write access processes to the variable run. But this cannot be done by the MCD system. So this attribute can be used in an early phase to express the desired refresh timing and later on to specify the real refresh timing. A None value is a no-op and does not overwrite an existing swRefreshTiming.
        """
        if value is not None:
            self.swRefreshTiming = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified. If both units (this as well as via compuMethod) are specified the units shall be compatible.
        """
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified. If both units (this as well as via compuMethod) are specified the units shall be compatible. A None value is a no-op and does not overwrite an existing unitRef.
        """
        if value is not None:
            self.unitRef = value
        return self

    def getValueAxisDataTypeRef(self) -> Optional[RefType]:
        """
        The referenced ApplicationPrimitiveDataType represents the primitive data type of the value axis within a compound primitive (e.g. curve, map). It supersedes CompuMethod, Unit, and BaseType.
        """
        return self.valueAxisDataTypeRef

    def setValueAxisDataTypeRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        The referenced ApplicationPrimitiveDataType represents the primitive data type of the value axis within a compound primitive (e.g. curve, map). It supersedes CompuMethod, Unit, and BaseType. A None value is a no-op and does not overwrite an existing valueAxisDataTypeRef.
        """
        if value is not None:
            self.valueAxisDataTypeRef = value
        return self


class SwPointerTargetProps(ARObject):
    """
    This element defines, that the data object (which is specified by the aggregating element) contains a reference to another data object or to a function in the CPU code. This corresponds to a pointer in the C-language. The attributes of this element describe the category and the detailed properties of the target which is either a data description or a function signature.
    """

    # SwPointerTargetProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.19, p.287
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFunctionPointerSignatureRef [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setFunctionPointerSignatureRef [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSwDataDefProps              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDefProps              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetCategory              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetCategory              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The referenced BswModuleEntry serves as the signature of a function pointer definition. Primary use case: function pointer passed as argument to other function.
        self.functionPointerSignatureRef: Optional[RefType] = None

        # The properties of the target data type.
        self.swDataDefProps: Optional[SwDataDefProps] = None

        # This specifies the category of the target: • In case of a data pointer, it shall specify the category of the referenced data. • In case of a function pointer, it could be used to denote the category of the referenced BswModuleEntry.
        self.targetCategory: Optional[Identifier] = None

    def getFunctionPointerSignatureRef(self) -> Optional[RefType]:
        """
        The referenced BswModuleEntry serves as the signature of a function pointer definition. Primary use case: function pointer passed as argument to other function.
        """
        return self.functionPointerSignatureRef

    def setFunctionPointerSignatureRef(self, value: Optional[RefType]) -> "SwPointerTargetProps":
        """
        The referenced BswModuleEntry serves as the signature of a function pointer definition. Primary use case: function pointer passed as argument to other function. A None value is a no-op and does not overwrite an existing functionPointerSignatureRef.
        """
        if value is not None:
            self.functionPointerSignatureRef = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        The properties of the target data type.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "SwPointerTargetProps":
        """
        The properties of the target data type. A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self

    def getTargetCategory(self) -> Optional[Identifier]:
        """
        This specifies the category of the target: • In case of a data pointer, it shall specify the category of the referenced data. • In case of a function pointer, it could be used to denote the category of the referenced BswModuleEntry.
        """
        return self.targetCategory

    def setTargetCategory(self, value: Optional[Identifier]) -> "SwPointerTargetProps":
        """
        This specifies the category of the target: • In case of a data pointer, it shall specify the category of the referenced data. • In case of a function pointer, it could be used to denote the category of the referenced BswModuleEntry. A None value is a no-op and does not overwrite an existing targetCategory.
        """
        if value is not None:
            self.targetCategory = value
        return self


class ValueList(ARObject):
    """
    This is a generic list of numerical values.
    """

    # ValueList method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.127, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getV                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setV                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addVf                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVfs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is a particular numerical value without variation.
        self.v: Optional[Numerical] = None

        # This is one entry in the list of numerical values
        self._vf: List[Numerical] = []

    def getV(self) -> Optional[Numerical]:
        """
        This is a particular numerical value without variation.

        Returns:
            Optional[Numerical]: This is a particular numerical value without variation., or None if not set
        """
        return self.v

    def setV(self, value: Optional[Numerical]) -> "ValueList":
        """
        This is a particular numerical value without variation.
        A None value is a no-op and does not overwrite an existing v.

        Args:
            value: This is a particular numerical value without variation. to set

        Returns:
            ValueList: self for method chaining
        """
        if value is not None:
            self.v = value
        return self

    def addVf(self, vf: Numerical) -> "ValueList":
        """
        This is one entry in the list of numerical values

        Args:
            vf: This is one entry in the list of numerical values to add

        Returns:
            ValueList: self for method chaining
        """
        self._vf.append(vf)
        return self

    def getVfs(self) -> List[Numerical]:
        """
        This is one entry in the list of numerical values

        Returns:
            List[Numerical]: The list of entries in insertion order (vf is ordered per spec)
        """
        return list(self._vf)


class SwTextProps(ARObject):
    """
    This meta-class expresses particular properties applicable to strings in variables or calibration parameters.
    """

    # SwTextProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.72, p.343
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArraySizeSemantics    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArraySizeSemantics    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBaseTypeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseTypeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwFillCharacter       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwFillCharacter       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwMaxTextSize         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwMaxTextSize         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute controls the semantics of the arraysize for the array representing the string in an Implementation DataType. It is there to support a safe conversion between ApplicationDatatype and ImplementationDatatype, even for variable length strings as required e.g. for Support of SAE J1939.
        self.arraySizeSemantics: Optional[ArraySizeSemanticsEnum] = None

        # This is the base type of one character in the string. In particular this baseType denotes the intended encoding of the characters in the string on level of ApplicationData Type.
        self.baseTypeRef: Optional[RefType] = None

        # Filler character for text parameter to pad up to the maximum length swMaxTextSize. The value will be interpreted according to the encoding specified in the associated base type of the data object, e.g. 0x30 (hex) represents the ASCII character zero as filler character and 0 (dec) represents an end of string as filler character. The usage of the fill character depends on the arraySize Semantics.
        self.swFillCharacter: Optional[Integer] = None

        # Specifies the maximum text size in characters. Note the size in bytes depends on the encoding in the corresponding baseType.
        self.swMaxTextSize: Optional[Integer] = None

    def getArraySizeSemantics(self) -> Optional[ArraySizeSemanticsEnum]:
        """
        This attribute controls the semantics of the arraysize for the array representing the string in an Implementation DataType. It is there to support a safe conversion between ApplicationDatatype and ImplementationDatatype, even for variable length strings as required e.g. for Support of SAE J1939.
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value: Optional[ArraySizeSemanticsEnum]) -> "SwTextProps":
        """
        This attribute controls the semantics of the arraysize for the array representing the string in an Implementation DataType. It is there to support a safe conversion between ApplicationDatatype and ImplementationDatatype, even for variable length strings as required e.g. for Support of SAE J1939. A None value is a no-op and does not overwrite an existing arraySizeSemantics.
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getBaseTypeRef(self) -> Optional[RefType]:
        """
        This is the base type of one character in the string. In particular this baseType denotes the intended encoding of the characters in the string on level of ApplicationData Type.
        """
        return self.baseTypeRef

    def setBaseTypeRef(self, value: Optional[RefType]) -> "SwTextProps":
        """
        This is the base type of one character in the string. In particular this baseType denotes the intended encoding of the characters in the string on level of ApplicationData Type. A None value is a no-op and does not overwrite an existing baseTypeRef.
        """
        if value is not None:
            self.baseTypeRef = value
        return self

    def getSwFillCharacter(self) -> Optional[Integer]:
        """
        Filler character for text parameter to pad up to the maximum length swMaxTextSize. The value will be interpreted according to the encoding specified in the associated base type of the data object, e.g. 0x30 (hex) represents the ASCII character zero as filler character and 0 (dec) represents an end of string as filler character. The usage of the fill character depends on the arraySize Semantics.
        """
        return self.swFillCharacter

    def setSwFillCharacter(self, value: Optional[Integer]) -> "SwTextProps":
        """
        Filler character for text parameter to pad up to the maximum length swMaxTextSize. The value will be interpreted according to the encoding specified in the associated base type of the data object, e.g. 0x30 (hex) represents the ASCII character zero as filler character and 0 (dec) represents an end of string as filler character. The usage of the fill character depends on the arraySize Semantics. A None value is a no-op and does not overwrite an existing swFillCharacter.
        """
        if value is not None:
            self.swFillCharacter = value
        return self

    def getSwMaxTextSize(self) -> Optional[Integer]:
        """
        Specifies the maximum text size in characters. Note the size in bytes depends on the encoding in the corresponding baseType.
        """
        return self.swMaxTextSize

    def setSwMaxTextSize(self, value: Optional[Integer]) -> "SwTextProps":
        """
        Specifies the maximum text size in characters. Note the size in bytes depends on the encoding in the corresponding baseType. A None value is a no-op and does not overwrite an existing swMaxTextSize.
        """
        if value is not None:
            self.swMaxTextSize = value
        return self
