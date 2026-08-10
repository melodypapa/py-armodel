from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARNumerical,
    ARFloat,
    AlignmentType,
    Boolean,
    Identifier,
    Integer,
    NativeDeclarationString,
    PrimitiveIdentifier,
    RefType,
    DisplayFormatString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
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


class SwVariableRefProxy(ARObject):
    """
    Proxy class for several kinds of references to a variable.
    """

    # SwVariableRefProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.57, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAutosarVariable       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutosarVariable       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMcDataInstanceVarRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMcDataInstanceVarRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type
        self.autosarVariable: Optional["AutosarVariableRef"] = None

        # This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype.
        self.mcDataInstanceVarRef: Optional[RefType] = None

    def getAutosarVariable(self) -> Optional["AutosarVariableRef"]:
        """
        This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type.
        """
        return self.autosarVariable

    def setAutosarVariable(self, value: Optional["AutosarVariableRef"]) -> "SwVariableRefProxy":
        """
        This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type. A None value is a no-op and does not overwrite an existing autosarVariable.
        """
        if value is not None:
            self.autosarVariable = value
        return self

    def getMcDataInstanceVarRef(self) -> Optional[RefType]:
        """
        This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype.
        """
        return self.mcDataInstanceVarRef

    def setMcDataInstanceVarRef(self, value: Optional[RefType]) -> "SwVariableRefProxy":
        """
        This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype. A None value is a no-op and does not overwrite an existing mcDataInstanceVarRef.
        """
        if value is not None:
            self.mcDataInstanceVarRef = value
        return self


class SwCalprmRefProxy(ARObject):
    """
    Proxy class for several kinds of references to a calibration parameter.
    """

    # SwCalprmRefProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.56, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArParameter           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArParameter           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMcDataInstanceRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMcDataInstanceRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the reference to a calibration parameter in an Autosar system.
        self.arParameter: Optional["AutosarParameterRef"] = None

        # This reference is used in the McSupport file to express the final instance of input values etc.
        self.mcDataInstanceRef: Optional[RefType] = None

    def getArParameter(self) -> Optional["AutosarParameterRef"]:
        """
        This represents the reference to a calibration parameter in an Autosar system.
        """
        return self.arParameter

    def setArParameter(self, value: Optional["AutosarParameterRef"]) -> "SwCalprmRefProxy":
        """
        This represents the reference to a calibration parameter in an Autosar system. A None value is a no-op and does not overwrite an existing arParameter.
        """
        if value is not None:
            self.arParameter = value
        return self

    def getMcDataInstanceRef(self) -> Optional[RefType]:
        """
        This reference is used in the McSupport file to express the final instance of input values etc.
        """
        return self.mcDataInstanceRef

    def setMcDataInstanceRef(self, value: Optional[RefType]) -> "SwCalprmRefProxy":
        """
        This reference is used in the McSupport file to express the final instance of input values etc. A None value is a no-op and does not overwrite an existing mcDataInstanceRef.
        """
        if value is not None:
            self.mcDataInstanceRef = value
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

        # This property specifies the calibration parameter which serves as the input axis.
        self.swCalprmRef: Optional[SwCalprmRefProxy] = None

        # This property specifies the variable which is used in the data dependency.
        self.swVariable: Optional[SwVariableRefProxy] = None

    def getSwCalprmRef(self) -> Optional[SwCalprmRefProxy]:
        """
        This property specifies the calibration parameter which serves as the input axis.
        """
        return self.swCalprmRef

    def setSwCalprmRef(self, value: Optional[SwCalprmRefProxy]) -> "SwDataDependencyArgs":
        """
        This property specifies the calibration parameter which serves as the input axis. A None value is a no-op and does not overwrite an existing swCalprmRef.
        """
        if value is not None:
            self.swCalprmRef = value
        return self

    def getSwVariable(self) -> Optional[SwVariableRefProxy]:
        """
        This property specifies the variable which is used in the data dependency.
        """
        return self.swVariable

    def setSwVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDependencyArgs":
        """
        This property specifies the variable which is used in the data dependency. A None value is a no-op and does not overwrite an existing swVariable.
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
    This element describes the interdependencies of data objects, e.g. variables and parameters. Use cases: Calculate the value of a calibration parameter (by the MCD system) from the value(s) of other calibration parameters. Virtual data - that means the data object is not directly in the ecu and this property describes how the "virtual variable" can be computed from the real ones (by the MCD system).
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

        # This element describes the formula with which the dependencies between the participating objects are defined. Tags: xml.sequenceOffset=30
        self.swDataDependencyFormula: Optional[CompuGenericMath] = None

        # Specifies the arguments used in the data dependency. Note that this is 0..1 since the aggregated class is a container (atpMixed). Tags: xml.sequenceOffset=40
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
    The properties of data are summarized in the meta-class SwDataDefProps. This meta-class itself is the superset of all applicable properties.
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
        self.stepSize: Optional[ARFloat] = None

        # This attribute is used to specify the dimensions of a value block (VAL_BLK) for the case that that value block has more than one dimension. The dimensions given in this attribute are ordered such that the first entry represents the first dimension, the second entry represents the second dimension, and so on. For one-dimensional value blocks the attribute swValueBlockSize shall be used and this attribute shall not exist.
        self.swValueBlockSizeMults: List[ARNumerical] = []

        # This aggregation allows to add annotations (yellow pads ...) related to the current data object.
        self.annotations: List[Annotation] = []

        # Addressing method related to this data object. Via an association to the same SwAddrMethod it can be specified that several DataPrototypes shall be located in the same memory without already specifying the memory section itself.
        self.swAddrMethodRef: Optional[RefType] = None

        # The attribute describes the intended alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod.
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

        # This element is used to express that a data object is a comparison variable.
        self.swComparisonVariables: List[SwVariableRefProxy] = []

        # Compu method associated with the containing data object.
        self.compuMethodRef: Optional[RefType] = None

        # Data constraint associated with the containing data object.
        self.dataConstrRef: Optional[RefType] = None

        # This element describes the interdependencies of data objects, e.g. variables and parameters.
        self.swDataDependency: Optional[SwDataDependency] = None

        # This is a display format specifier for the display of values e.g. in documents or in measurement and calibration systems.
        self.displayFormat: Optional[DisplayFormatString] = None

        # This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps.
        self.implementationDataTypeRef: Optional[RefType] = None

        # Proxy class for several kinds of references to a variable.
        self.swHostVariable: Optional[SwVariableRefProxy] = None

        # This indicates the intended implementation policy of the data object.
        self.swImplPolicy: Optional[SwImplPolicyEnum] = None

        # This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved.
        self.additionalNativeTypeQualifier: Optional[NativeDeclarationString] = None

        # This attribute can be used to specify the intended resolution of the data object.
        self.swIntendedResolution: Optional[ARNumerical] = None

        # This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps.
        self.swInterpolationMethod: Optional[Identifier] = None

        # The value which indicates that the data object is invalid.
        self.invalidValue: Optional[ValueSpecification] = None

        # This element distinguishes virtual objects. Virtual objects do not appear in the memory, their derivation is much more dependent on other objects and hence they shall have a swDataDependency.
        self.swIsVirtual: Optional[Boolean] = None

        # Specifies that the containing data object is a pointer to another data object.
        self.swPointerTargetProps: Optional[SwPointerTargetProps] = None

        # Record layout for this data object.
        self.swRecordLayoutRef: Optional[RefType] = None

        # This element specifies the frequency in which the object involved shall be or is called or calculated.
        self.swRefreshTiming: Optional[MultidimensionalTime] = None

        # Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified.
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

    def getStepSize(self) -> Optional[ARFloat]:
        """
        This attribute can be used to define a value which is added to or subtracted from the value of a DataPrototype when using up/down keys while calibrating.
        """
        return self.stepSize

    def setStepSize(self, value: Optional[ARFloat]) -> "SwDataDefProps":
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
        The attribute describes the intended alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod.
        """
        return self.swAlignment

    def setSwAlignment(self, value: Optional[AlignmentType]) -> "SwDataDefProps":
        """
        The attribute describes the intended alignment of the DataPrototype. If the attribute is not defined the alignment is determined by the swBaseType size and the memoryAllocationKeywordPolicy of the referenced SwAddrMethod. A None value is a no-op and does not overwrite an existing swAlignment.
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
        This element is used to express that a data object is a comparison variable.
        """
        return self.swComparisonVariables

    def addSwComparisonVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDefProps":
        """
        This element is used to express that a data object is a comparison variable. Appends a comparison variable. A None value is a no-op.
        """
        if value is not None:
            self.swComparisonVariables.append(value)
        return self

    def getCompuMethodRef(self) -> Optional[RefType]:
        """
        Compu method associated with the containing data object.
        """
        return self.compuMethodRef

    def setCompuMethodRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Compu method associated with the containing data object. A None value is a no-op and does not overwrite an existing compuMethodRef.
        """
        if value is not None:
            self.compuMethodRef = value
        return self

    def getDataConstrRef(self) -> Optional[RefType]:
        """
        Data constraint associated with the containing data object.
        """
        return self.dataConstrRef

    def setDataConstrRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Data constraint associated with the containing data object. A None value is a no-op and does not overwrite an existing dataConstrRef.
        """
        if value is not None:
            self.dataConstrRef = value
        return self

    def getSwDataDependency(self) -> Optional[SwDataDependency]:
        """
        This element describes the interdependencies of data objects, e.g. variables and parameters.
        """
        return self.swDataDependency

    def setSwDataDependency(self, value: Optional[SwDataDependency]) -> "SwDataDefProps":
        """
        This element describes the interdependencies of data objects, e.g. variables and parameters. A None value is a no-op and does not overwrite an existing swDataDependency.
        """
        if value is not None:
            self.swDataDependency = value
        return self

    def getDisplayFormat(self) -> Optional[DisplayFormatString]:
        """
        This is a display format specifier for the display of values e.g. in documents or in measurement and calibration systems.
        """
        return self.displayFormat

    def setDisplayFormat(self, value: Optional[DisplayFormatString]) -> "SwDataDefProps":
        """
        This is a display format specifier for the display of values e.g. in documents or in measurement and calibration systems. A None value is a no-op and does not overwrite an existing displayFormat.
        """
        if value is not None:
            self.displayFormat = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps.
        """
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        This association denotes the ImplementationDataType of a data declaration via its aggregated SwDataDefProps. A None value is a no-op and does not overwrite an existing implementationDataTypeRef.
        """
        if value is not None:
            self.implementationDataTypeRef = value
        return self

    def getSwHostVariable(self) -> Optional[SwVariableRefProxy]:
        """
        Proxy class for several kinds of references to a variable.
        """
        return self.swHostVariable

    def setSwHostVariable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDefProps":
        """
        Proxy class for several kinds of references to a variable. A None value is a no-op and does not overwrite an existing swHostVariable.
        """
        if value is not None:
            self.swHostVariable = value
        return self

    def getSwImplPolicy(self) -> Optional[SwImplPolicyEnum]:
        """
        This indicates the intended implementation policy of the data object.
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value: Optional[SwImplPolicyEnum]) -> "SwDataDefProps":
        """
        This indicates the intended implementation policy of the data object. A None value is a no-op and does not overwrite an existing swImplPolicy.
        """
        if value is not None:
            self.swImplPolicy = value
        return self

    def getAdditionalNativeTypeQualifier(self) -> Optional[NativeDeclarationString]:
        """
        This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved.
        """
        return self.additionalNativeTypeQualifier

    def setAdditionalNativeTypeQualifier(self, value: Optional[NativeDeclarationString]) -> "SwDataDefProps":
        """
        This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved. A None value is a no-op and does not overwrite an existing additionalNativeTypeQualifier.
        """
        if value is not None:
            self.additionalNativeTypeQualifier = value
        return self

    def getSwIntendedResolution(self) -> Optional[ARNumerical]:
        """
        This attribute can be used to specify the intended resolution of the data object.
        """
        return self.swIntendedResolution

    def setSwIntendedResolution(self, value: Optional[ARNumerical]) -> "SwDataDefProps":
        """
        This attribute can be used to specify the intended resolution of the data object. A None value is a no-op and does not overwrite an existing swIntendedResolution.
        """
        if value is not None:
            self.swIntendedResolution = value
        return self

    def getSwInterpolationMethod(self) -> Optional[Identifier]:
        """
        This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps.
        """
        return self.swInterpolationMethod

    def setSwInterpolationMethod(self, value: Optional[Identifier]) -> "SwDataDefProps":
        """
        This is the name of the interpolation method which is implemented by the referenced bswModuleEntry. It corresponds to swInterpolationMethod in SwDataDefProps. A None value is a no-op and does not overwrite an existing swInterpolationMethod.
        """
        if value is not None:
            self.swInterpolationMethod = value
        return self

    def getInvalidValue(self) -> Optional[ValueSpecification]:
        """
        The value which indicates that the data object is invalid.
        """
        return self.invalidValue

    def setInvalidValue(self, value: Optional[ValueSpecification]) -> "SwDataDefProps":
        """
        The value which indicates that the data object is invalid. A None value is a no-op and does not overwrite an existing invalidValue.
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
        Specifies that the containing data object is a pointer to another data object.
        """
        return self.swPointerTargetProps

    def setSwPointerTargetProps(self, value: Optional[SwPointerTargetProps]) -> "SwDataDefProps":
        """
        Specifies that the containing data object is a pointer to another data object. A None value is a no-op and does not overwrite an existing swPointerTargetProps.
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
        This element specifies the frequency in which the object involved shall be or is called or calculated.
        """
        return self.swRefreshTiming

    def setSwRefreshTiming(self, value: Optional[MultidimensionalTime]) -> "SwDataDefProps":
        """
        This element specifies the frequency in which the object involved shall be or is called or calculated. A None value is a no-op and does not overwrite an existing swRefreshTiming.
        """
        if value is not None:
            self.swRefreshTiming = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """
        Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified.
        """
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Physical unit associated with the semantics of this data object. This attribute applies if no compuMethod is specified. A None value is a no-op and does not overwrite an existing unitRef.
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
    Properties for pointer targets including function pointer signature and target category.
    """

    # SwPointerTargetProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.19, p.287
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFunctionPointerSignatureRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFunctionPointerSignatureRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwDataDefProps              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwDataDefProps              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetCategory              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetCategory              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The signature of the function the pointer refers to.
        self.functionPointerSignatureRef: Optional[RefType] = None

        # The properties of the data which is referenced by the pointer.
        self.swDataDefProps: Optional[SwDataDefProps] = None

        # Specifies the category of the target (the object the pointer points to).
        self.targetCategory: Optional[Identifier] = None

    def getFunctionPointerSignatureRef(self) -> Optional[RefType]:
        """
        The signature of the function the pointer refers to.
        """
        return self.functionPointerSignatureRef

    def setFunctionPointerSignatureRef(self, value: Optional[RefType]) -> "SwPointerTargetProps":
        """
        The signature of the function the pointer refers to. A None value is a no-op and does not overwrite an existing functionPointerSignatureRef.
        """
        if value is not None:
            self.functionPointerSignatureRef = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        The properties of the data which is referenced by the pointer.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "SwPointerTargetProps":
        """
        The properties of the data which is referenced by the pointer. A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self

    def getTargetCategory(self) -> Optional[Identifier]:
        """
        Specifies the category of the target (the object the pointer points to).
        """
        return self.targetCategory

    def setTargetCategory(self, value: Optional[Identifier]) -> "SwPointerTargetProps":
        """
        Specifies the category of the target (the object the pointer points to). A None value is a no-op and does not overwrite an existing targetCategory.
        """
        if value is not None:
            self.targetCategory = value
        return self


class ValueList(ARObject):
    """
    List of values with single value and multi-value support.
    """

    # ValueList method parity checklist:
    # [ ] __init__                 [x] impl  [ ] docstring  [x] test  [—] reader  [—] writer
    # [ ] getV                     [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [ ] setV                     [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [ ] addVf                    [x] impl  [ ] docstring  [x] test  [—] reader  [—] writer
    # [ ] getVfs                   [x] impl  [ ] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        self.v: Optional[ARNumerical] = None
        self._vf: List[ARNumerical] = []

    def getV(self) -> Optional[ARNumerical]:
        return self.v

    def setV(self, value: Optional[ARNumerical]) -> "ValueList":
        if value is not None:
            self.v = value
        return self

    def addVf(self, vf: ARNumerical):
        self._vf.append(vf)

    def getVfs(self) -> List[ARNumerical]:
        return sorted(self._vf)


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
