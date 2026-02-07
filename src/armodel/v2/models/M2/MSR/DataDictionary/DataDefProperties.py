from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
)
from armodel.v2.models.M2.MSR.Documentation.Annotation import Annotation


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
    CONST = "const"
    FIXED = "fixed"
    MEASUREMENT_POINT = "measurementPoint"
    QUEUED = "queued"
    STANDARD = "standard"

    def __init__(self) -> None:
        super().__init__([
            SwImplPolicyEnum.CONST,
            SwImplPolicyEnum.FIXED,
            SwImplPolicyEnum.MEASUREMENT_POINT,
            SwImplPolicyEnum.QUEUED,
            SwImplPolicyEnum.STANDARD
        ])


class SwDataDefPropsConditional(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    '''
    Patch for the time-stamp
    '''
    def __init__(self) -> None:
        super().__init__()


class SwDataDefProps(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.additionalNativeTypeQualifier = None
        self.annotations = []                               # type: List[Annotation]
        self.baseTypeRef: Union[RefType, None] = None
        self.compuMethodRef: Union[RefType, None] = None
        self.dataConstrRef: Union[RefType, None] = None
        self.displayFormat: Union[ARLiteral, None] = None
        self.displayPresentation: Union[ARLiteral, None] = None
        self.implementationDataTypeRef: Union[RefType, None] = None
        self.invalidValue: Union[ValueSpecification, None] = None
        self.stepSize: Union[ARFloat, None] = None
        self.swAddrMethodRef: Union[RefType, None] = None
        self.swAlignment: Union[ARLiteral, None] = None
        self.swBitRepresentation: Union[ARLiteral, None] = None
        self.swCalibrationAccess: Union[ARLiteral, None] = None
        self.swCalprmAxisSet: Union[SwCalprmAxisSet, None] = None
        self.swComparisonVariables = []
        self.swDataDependency = None
        self.swHostVariable = None
        self.swImplPolicy: Union[ARLiteral, None] = None
        self.swIntendedResolution = None
        self.swInterpolationMethod = None
        self.swIsVirtual = None
        self.swPointerTargetProps: Union[SwPointerTargetProps, None] = None
        self.swRecordLayoutRef: Union[RefType, None] = None
        self.swRefreshTiming = None
        self.swTextProps = None
        self.swValueBlockSize = None
        self.swValueBlockSizeMults = []
        self.unitRef: Union[RefType, None] = None
        self.valueAxisDataTypeRef: Union[RefType, None] = None

        self.conditional = SwDataDefPropsConditional()      # type: SwDataDefPropsConditional

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.functionPointerSignatureRef: Union[RefType, None] = None
        self.swDataDefProps: Union[SwDataDefProps, None] = None
        self.targetCategory: Union[ARLiteral, None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.v: Union[ARFloat, None] = None
        self._vf = []                                       # type: List[ARLiteral]

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
    Represents software text properties in the AUTOSAR model.

    This class is used to define text-related properties for data elements,
    such as encoding and format information.

    Attributes:
        encoding (ARLiteral): The encoding of the text.
        format (ARLiteral): The format of the text.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.encoding: Union[Union[ARLiteral, None] , None] = None
        self.format: Union[Union[ARLiteral, None] , None] = None

    def getEncoding(self) -> ARLiteral:
        return self.encoding

    def setEncoding(self, value: ARLiteral):
        if value is not None:
            self.encoding = value
        return self

    def getFormat(self) -> ARLiteral:
        return self.format

    def setFormat(self, value: ARLiteral):
        if value is not None:
            self.format = value
        return self


class BulkNvDataDescriptor(ARObject):
    """Descriptor for bulk NV data."""
    def __init__(self) -> None:
        super().__init__()
        self.nvBlockDescriptorRefs: List[RefType] = []

    def getNvBlockDescriptorRefs(self):
        return self.nvBlockDescriptorRefs

    def addNvBlockDescriptorRef(self, value):
        if value is not None:
            self.nvBlockDescriptorRefs.append(value)
        return self


class NvBlockDescriptor(ARObject):
    """Descriptor for NV block."""
    def __init__(self) -> None:
        super().__init__()
        self.nvBlockNumber: Union[int, None] = None
        self.nvBlockSize: Union[int, None] = None

    def getNvBlockNumber(self):
        return self.nvBlockNumber

    def setNvBlockNumber(self, value):
        if value is not None:
            self.nvBlockNumber = value
        return self

    def getNvBlockSize(self):
        return self.nvBlockSize

    def setNvBlockSize(self, value):
        if value is not None:
            self.nvBlockSize = value
        return self

