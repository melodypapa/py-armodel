from typing import List
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat
from ...AUTOSARTemplates.CommonStructure import ValueSpecification
from .CalibrationParameter import SwCalprmAxisSet
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ..Documentation.Annotation import Annotation
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral


class SwDataDefPropsConditional(ARObject):
    '''
    Patch for the time-stamp
    '''
    def __init__(self):
        super().__init__()

class SwDataDefProps(ARObject):
    def __init__(self):
        super().__init__()

        self.additionalNativeTypeQualifier = None           
        self.annotations = []                               # type: List[Annotation]
        self.baseTypeRef = None                             # type: RefType
        self.compuMethodRef = None                          # type: RefType
        self.dataConstrRef = None                           # type: RefType
        self.displayFormat = None                           # type: ARLiteral
        self.displayPresentation = None                     # type: ARLiteral
        self.implementationDataTypeRef = None               # type: RefType
        self.invalidValue = None                            # type: ValueSpecification
        self.stepSize = None                                # type: ARFloat
        self.swAddrMethodRef = None                         # type: RefType
        self.swAlignment = None                             # type: ARLiteral
        self.swBitRepresentation = None                     # type: ARLiteral
        self.swCalibrationAccess = None                     # type: ARLiteral
        self.swCalprmAxisSet = None                         # type: SwCalprmAxisSet
        self.swComparisonVariables = []
        self.swDataDependency = None
        self.swHostVariable = None
        self.swImplPolicy = None                            # type: ARLiteral
        self.swIntendedResolution = None
        self.swInterpolationMethod = None
        self.swIsVirtual = None
        self.swPointerTargetProps = None                    # type: SwPointerTargetProps
        self.swRecordLayoutRef = None                       # type: RefType
        self.swRefreshTiming = None
        self.swTextProps = None
        self.swValueBlockSize = None
        self.swValueBlockSizeMults = []
        self.unitRef = None                                 # type: RefType
        self.valueAxisDataTypeRef = None                    # type: RefType

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
    def __init__(self):
        super().__init__()

        self.functionPointerSignatureRef = None             # type: RefType
        self.swDataDefProps = None                          # type: SwDataDefProps
        self.targetCategory = None                          # type: ARLiteral

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
    def __init__(self):
        super().__init__()

        self.v = None                                       # type: ARFloat
        self._vf = []                                       # type: List[ARLiteral]

    def addVf(self, vf: ARLiteral):
        self._vf.append(vf)

    def getVfs(self) -> List[ARLiteral]:
        return sorted(self._vf)

