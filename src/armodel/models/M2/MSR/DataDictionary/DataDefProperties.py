from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, Integer, RefType

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum


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
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    CONST = "const"
    FIXED = "fixed"
    MEASUREMENT_POINT = "measurementPoint"
    QUEUED = "queued"
    STANDARD = "standard"

    def __init__(self):
        super().__init__([SwImplPolicyEnum.CONST, SwImplPolicyEnum.FIXED, SwImplPolicyEnum.MEASUREMENT_POINT, SwImplPolicyEnum.QUEUED, SwImplPolicyEnum.STANDARD])


class SwDataDefPropsConditional(ARObject):
    """
    Patch for the time-stamp
    """

    # SwDataDefPropsConditional method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class SwDataDefProps(ARObject):
    """
    Software data definition properties describing data characteristics
    including type references, calibration parameters, memory addressing,
    and display properties.
    """

    # SwDataDefProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAdditionalNativeTypeQualifier [x] impl  [ ] docstring  [ ] test
    # [ ] setAdditionalNativeTypeQualifier [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotations               [x] impl  [ ] docstring  [ ] test
    # [ ] addAnnotation                [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseTypeRef               [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseTypeRef               [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuMethodRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuMethodRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getDataConstrRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setDataConstrRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getDisplayFormat             [x] impl  [ ] docstring  [ ] test
    # [ ] setDisplayFormat             [x] impl  [ ] docstring  [ ] test
    # [ ] getDisplayPresentation       [x] impl  [ ] docstring  [ ] test
    # [ ] setDisplayPresentation       [x] impl  [ ] docstring  [ ] test
    # [ ] getImplementationDataTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] setImplementationDataTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] getInvalidValue              [x] impl  [ ] docstring  [ ] test
    # [ ] setInvalidValue              [x] impl  [ ] docstring  [ ] test
    # [ ] getStepSize                  [x] impl  [ ] docstring  [ ] test
    # [ ] setStepSize                  [x] impl  [ ] docstring  [ ] test
    # [ ] getSwAddrMethodRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setSwAddrMethodRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getSwAlignment               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwAlignment               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwBitRepresentation       [x] impl  [ ] docstring  [ ] test
    # [ ] setSwBitRepresentation       [x] impl  [ ] docstring  [ ] test
    # [ ] getSwCalibrationAccess       [x] impl  [ ] docstring  [ ] test
    # [ ] setSwCalibrationAccess       [x] impl  [ ] docstring  [ ] test
    # [ ] getSwCalprmAxisSet           [x] impl  [ ] docstring  [ ] test
    # [ ] setSwCalprmAxisSet           [x] impl  [ ] docstring  [ ] test
    # [ ] getSwComparisonVariables     [x] impl  [ ] docstring  [ ] test
    # [ ] setSwComparisonVariables     [x] impl  [ ] docstring  [ ] test
    # [ ] getSwDataDependency          [x] impl  [ ] docstring  [ ] test
    # [ ] setSwDataDependency          [x] impl  [ ] docstring  [ ] test
    # [ ] getSwHostVariable            [x] impl  [ ] docstring  [ ] test
    # [ ] setSwHostVariable            [x] impl  [ ] docstring  [ ] test
    # [ ] getSwImplPolicy              [x] impl  [ ] docstring  [ ] test
    # [ ] setSwImplPolicy              [x] impl  [ ] docstring  [ ] test
    # [ ] getSwIntendedResolution      [x] impl  [ ] docstring  [ ] test
    # [ ] setSwIntendedResolution      [x] impl  [ ] docstring  [ ] test
    # [ ] getSwInterpolationMethod     [x] impl  [ ] docstring  [ ] test
    # [ ] setSwInterpolationMethod     [x] impl  [ ] docstring  [ ] test
    # [ ] getSwIsVirtual               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwIsVirtual               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwPointerTargetProps      [x] impl  [ ] docstring  [ ] test
    # [ ] setSwPointerTargetProps      [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRecordLayoutRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRecordLayoutRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getSwRefreshTiming           [x] impl  [ ] docstring  [ ] test
    # [ ] setSwRefreshTiming           [x] impl  [ ] docstring  [ ] test
    # [ ] getSwTextProps               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwTextProps               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwValueBlockSize          [x] impl  [ ] docstring  [ ] test
    # [ ] setSwValueBlockSize          [x] impl  [ ] docstring  [ ] test
    # [ ] getSwValueBlockSizeMults     [x] impl  [ ] docstring  [ ] test
    # [ ] setSwValueBlockSizeMults     [x] impl  [ ] docstring  [ ] test
    # [ ] getUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getValueAxisDataTypeRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setValueAxisDataTypeRef      [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.additionalNativeTypeQualifier = None
        self.annotations = []  # type: List[Annotation]
        self.baseTypeRef = None  # type: RefType
        self.compuMethodRef = None  # type: RefType
        self.dataConstrRef = None  # type: RefType
        self.displayFormat = None  # type: ARLiteral
        self.displayPresentation = None  # type: ARLiteral
        self.implementationDataTypeRef = None  # type: RefType
        self.invalidValue = None  # type: ValueSpecification
        self.stepSize = None  # type: ARFloat
        self.swAddrMethodRef = None  # type: RefType
        self.swAlignment = None  # type: ARLiteral
        self.swBitRepresentation = None  # type: ARLiteral
        self.swCalibrationAccess = None  # type: ARLiteral
        self.swCalprmAxisSet = None  # type: SwCalprmAxisSet
        self.swComparisonVariables = []
        self.swDataDependency = None
        self.swHostVariable = None
        self.swImplPolicy = None  # type: ARLiteral
        self.swIntendedResolution = None
        self.swInterpolationMethod = None
        self.swIsVirtual = None
        self.swPointerTargetProps = None  # type: SwPointerTargetProps
        self.swRecordLayoutRef = None  # type: RefType
        self.swRefreshTiming = None
        self.swTextProps = None
        self.swValueBlockSize = None
        self.swValueBlockSizeMults = []
        self.unitRef = None  # type: RefType
        self.valueAxisDataTypeRef = None  # type: RefType

        self.conditional = SwDataDefPropsConditional()  # type: SwDataDefPropsConditional

    def getAdditionalNativeTypeQualifier(self):
        return self.additionalNativeTypeQualifier

    def setAdditionalNativeTypeQualifier(self, value):
        self.additionalNativeTypeQualifier = value
        return self

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations

    def addAnnotation(self, annotation: Annotation):
        self.annotations.append(annotation)
        return self

    def getBaseTypeRef(self):
        return self.baseTypeRef

    def setBaseTypeRef(self, value):
        self.baseTypeRef = value
        return self

    def getCompuMethodRef(self):
        return self.compuMethodRef

    def setCompuMethodRef(self, value):
        self.compuMethodRef = value
        return self

    def getDataConstrRef(self):
        return self.dataConstrRef

    def setDataConstrRef(self, value):
        self.dataConstrRef = value
        return self

    def getDisplayFormat(self):
        return self.displayFormat

    def setDisplayFormat(self, value):
        self.displayFormat = value
        return self

    def getDisplayPresentation(self):
        return self.displayPresentation

    def setDisplayPresentation(self, value):
        self.displayPresentation = value
        return self

    def getImplementationDataTypeRef(self):
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value):
        self.implementationDataTypeRef = value
        return self

    def getInvalidValue(self):
        return self.invalidValue

    def setInvalidValue(self, value):
        self.invalidValue = value
        return self

    def getStepSize(self):
        return self.stepSize

    def setStepSize(self, value):
        self.stepSize = value
        return self

    def getSwAddrMethodRef(self):
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        self.swAddrMethodRef = value
        return self

    def getSwAlignment(self):
        return self.swAlignment

    def setSwAlignment(self, value):
        self.swAlignment = value
        return self

    def getSwBitRepresentation(self):
        return self.swBitRepresentation

    def setSwBitRepresentation(self, value):
        self.swBitRepresentation = value
        return self

    def getSwCalibrationAccess(self):
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value):
        self.swCalibrationAccess = value
        return self

    def getSwCalprmAxisSet(self):
        return self.swCalprmAxisSet

    def setSwCalprmAxisSet(self, value):
        self.swCalprmAxisSet = value
        return self

    def getSwComparisonVariables(self):
        return self.swComparisonVariables

    def setSwComparisonVariables(self, value):
        self.swComparisonVariables = value
        return self

    def getSwDataDependency(self):
        return self.swDataDependency

    def setSwDataDependency(self, value):
        self.swDataDependency = value
        return self

    def getSwHostVariable(self):
        return self.swHostVariable

    def setSwHostVariable(self, value):
        self.swHostVariable = value
        return self

    def getSwImplPolicy(self):
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        self.swImplPolicy = value
        return self

    def getSwIntendedResolution(self):
        return self.swIntendedResolution

    def setSwIntendedResolution(self, value):
        self.swIntendedResolution = value
        return self

    def getSwInterpolationMethod(self):
        return self.swInterpolationMethod

    def setSwInterpolationMethod(self, value):
        self.swInterpolationMethod = value
        return self

    def getSwIsVirtual(self):
        return self.swIsVirtual

    def setSwIsVirtual(self, value):
        self.swIsVirtual = value
        return self

    def getSwPointerTargetProps(self):
        return self.swPointerTargetProps

    def setSwPointerTargetProps(self, value):
        self.swPointerTargetProps = value
        return self

    def getSwRecordLayoutRef(self):
        return self.swRecordLayoutRef

    def setSwRecordLayoutRef(self, value):
        self.swRecordLayoutRef = value
        return self

    def getSwRefreshTiming(self):
        return self.swRefreshTiming

    def setSwRefreshTiming(self, value):
        self.swRefreshTiming = value
        return self

    def getSwTextProps(self):
        return self.swTextProps

    def setSwTextProps(self, value):
        self.swTextProps = value
        return self

    def getSwValueBlockSize(self):
        return self.swValueBlockSize

    def setSwValueBlockSize(self, value):
        self.swValueBlockSize = value
        return self

    def getSwValueBlockSizeMults(self):
        return self.swValueBlockSizeMults

    def setSwValueBlockSizeMults(self, value):
        self.swValueBlockSizeMults = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        self.unitRef = value
        return self

    def getValueAxisDataTypeRef(self):
        return self.valueAxisDataTypeRef

    def setValueAxisDataTypeRef(self, value):
        self.valueAxisDataTypeRef = value
        return self


class SwPointerTargetProps(ARObject):
    """
    Properties for pointer targets including function pointer signature and
    target category.
    """

    # SwPointerTargetProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFunctionPointerSignatureRef [x] impl  [ ] docstring  [ ] test
    # [ ] setFunctionPointerSignatureRef [x] impl  [ ] docstring  [ ] test
    # [ ] getSwDataDefProps            [x] impl  [ ] docstring  [ ] test
    # [ ] setSwDataDefProps            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetCategory            [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetCategory            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.functionPointerSignatureRef = None  # type: RefType
        self.swDataDefProps = None  # type: SwDataDefProps
        self.targetCategory = None  # type: ARLiteral

    def getFunctionPointerSignatureRef(self):
        return self.functionPointerSignatureRef

    def setFunctionPointerSignatureRef(self, value):
        self.functionPointerSignatureRef = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self

    def getTargetCategory(self):
        return self.targetCategory

    def setTargetCategory(self, value):
        self.targetCategory = value
        return self


class ValueList(ARObject):
    """
    List of values with single value and multi-value support.
    """

    # ValueList method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getV                         [x] impl  [ ] docstring  [ ] test
    # [ ] setV                         [x] impl  [ ] docstring  [ ] test
    # [ ] addVf                        [x] impl  [ ] docstring  [ ] test
    # [ ] getVfs                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.v = None  # type: ARFloat
        self._vf = []  # type: List[ARLiteral]

    def getV(self):
        return self.v

    def setV(self, value):
        self.v = value
        return self

    def addVf(self, vf: ARLiteral):
        self._vf.append(vf)

    def getVfs(self) -> List[ARLiteral]:
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

        Returns:
            The array size semantics
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value: Optional[ArraySizeSemanticsEnum]) -> "SwTextProps":
        """
        This attribute controls the semantics of the arraysize for the array representing the string in an Implementation DataType. It is there to support a safe conversion between ApplicationDatatype and ImplementationDatatype, even for variable length strings as required e.g. for Support of SAE J1939. A None value is a no-op and does not overwrite an existing arraySizeSemantics.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getBaseTypeRef(self) -> Optional[RefType]:
        """
        This is the base type of one character in the string. In particular this baseType denotes the intended encoding of the characters in the string on level of ApplicationData Type.

        Returns:
            The base type reference
        """
        return self.baseTypeRef

    def setBaseTypeRef(self, value: Optional[RefType]) -> "SwTextProps":
        """
        This is the base type of one character in the string. In particular this baseType denotes the intended encoding of the characters in the string on level of ApplicationData Type. A None value is a no-op and does not overwrite an existing baseTypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseTypeRef = value
        return self

    def getSwFillCharacter(self) -> Optional[Integer]:
        """
        Filler character for text parameter to pad up to the maximum length swMaxTextSize. The value will be interpreted according to the encoding specified in the associated base type of the data object, e.g. 0x30 (hex) represents the ASCII character zero as filler character and 0 (dec) represents an end of string as filler character. The usage of the fill character depends on the arraySize Semantics.

        Returns:
            The fill character value
        """
        return self.swFillCharacter

    def setSwFillCharacter(self, value: Optional[Integer]) -> "SwTextProps":
        """
        Filler character for text parameter to pad up to the maximum length swMaxTextSize. The value will be interpreted according to the encoding specified in the associated base type of the data object, e.g. 0x30 (hex) represents the ASCII character zero as filler character and 0 (dec) represents an end of string as filler character. The usage of the fill character depends on the arraySize Semantics. A None value is a no-op and does not overwrite an existing swFillCharacter.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swFillCharacter = value
        return self

    def getSwMaxTextSize(self) -> Optional[Integer]:
        """
        Specifies the maximum text size in characters. Note the size in bytes depends on the encoding in the corresponding baseType.

        Returns:
            The maximum text size in characters
        """
        return self.swMaxTextSize

    def setSwMaxTextSize(self, value: Optional[Integer]) -> "SwTextProps":
        """
        Specifies the maximum text size in characters. Note the size in bytes depends on the encoding in the corresponding baseType. A None value is a no-op and does not overwrite an existing swMaxTextSize.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swMaxTextSize = value
        return self
