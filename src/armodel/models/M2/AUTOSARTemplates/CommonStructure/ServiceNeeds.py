from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, AREnum, Boolean, ARLiteral
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagRequirementIdString, Integer, PositiveInteger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, TimeValue


class RoleBasedDataAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.role = None                    # type: ARLiteral
        self.usedDataElement = None         # type: AutosarVariableRef
        self.usedParameterElement = None    # type: AutosarParameterRef
        self.usedPimRef = None              # type: RefType

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getUsedDataElement(self):
        return self.usedDataElement

    def setUsedDataElement(self, value):
        self.usedDataElement = value
        return self

    def getUsedParameterElement(self):
        return self.usedParameterElement

    def setUsedParameterElement(self, value):
        self.usedParameterElement = value
        return self

    def getUsedPimRef(self):
        return self.usedPimRef

    def setUsedPimRef(self, value):
        self.usedPimRef = value
        return self


class ServiceNeeds(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ServiceNeeds:
            raise NotImplementedError("ServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class RamBlockStatusControlEnum(AREnum):
    API = "api"
    NV_RAM_MANAGER = "nvRamManager"

    def __init__(self):
        super().__init__((
            RamBlockStatusControlEnum.API,
            RamBlockStatusControlEnum.NV_RAM_MANAGER,
        ))


class NvBlockNeedsReliabilityEnum(AREnum):
    ERROR_CORRECTION = "errorCorrection"
    ERROR_DETECTION = "errorDetection"
    NO_PROTECTION = "noProtection"

    def __init__(self):
        super().__init__((
            NvBlockNeedsReliabilityEnum.ERROR_CORRECTION,
            NvBlockNeedsReliabilityEnum.ERROR_DETECTION,
            NvBlockNeedsReliabilityEnum.NO_PROTECTION,
        ))


class NvBlockNeedsWritingPriorityEnum(AREnum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"

    def __init__(self):
        super().__init__((
            NvBlockNeedsWritingPriorityEnum.HIGH,
            NvBlockNeedsWritingPriorityEnum.LOW,
            NvBlockNeedsWritingPriorityEnum.MEDIUM,
        ))


class NvBlockNeeds(ServiceNeeds):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calcRamBlockCrc = None                     # type: Boolean
        self.checkStaticBlockId = None                  # type: Boolean
        self.cyclicWritingPeriod = None                 # type: TimeValue
        self.nDataSets = None                           # type: PositiveInteger
        self.nRomBlocks = None                          # type: PositiveInteger
        self.ramBlockStatusControl = None               # type: RamBlockStatusControlEnum
        self.readonly = None                            # type: Boolean
        self.reliability = None                         # type: NvBlockNeedsReliabilityEnum
        self.resistantToChangedSw = None                # type: Boolean
        self.restoreAtStart = None                      # type: Boolean
        self.selectBlockForFirstInitAll = None          # type: Boolean
        self.storeAtShutdown = None                     # type: Boolean
        self.storeCyclic = None                         # type: Boolean
        self.storeEmergency = None                      # type: Boolean
        self.storeImmediate = None                      # type: Boolean
        self.storeOnChange = None                       # type: Boolean
        self.useAutoValidationAtShutDown = None         # type: Boolean
        self.useCRCCompMechanism = None                 # type: Boolean
        self.writeOnlyOnce = None                       # type: Boolean
        self.writeVerification = None                   # type: Boolean
        self.writingFrequency = None                    # type: PositiveInteger
        self.writingPriority = None                     # type: NvBlockNeedsWritingPriorityEnum

    def getCalcRamBlockCrc(self):
        return self.calcRamBlockCrc

    def setCalcRamBlockCrc(self, value):
        self.calcRamBlockCrc = value
        return self

    def getCheckStaticBlockId(self):
        return self.checkStaticBlockId

    def setCheckStaticBlockId(self, value):
        self.checkStaticBlockId = value
        return self

    def getCyclicWritingPeriod(self):
        return self.cyclicWritingPeriod

    def setCyclicWritingPeriod(self, value):
        self.cyclicWritingPeriod = value
        return self

    def getNDataSets(self):
        return self.nDataSets

    def setNDataSets(self, value):
        self.nDataSets = value
        return self

    def getNRomBlocks(self):
        return self.nRomBlocks

    def setNRomBlocks(self, value):
        self.nRomBlocks = value
        return self

    def getRamBlockStatusControl(self):
        return self.ramBlockStatusControl

    def setRamBlockStatusControl(self, value):
        self.ramBlockStatusControl = value
        return self

    def getReadonly(self):
        return self.readonly

    def setReadonly(self, value):
        self.readonly = value
        return self

    def getReliability(self):
        return self.reliability

    def setReliability(self, value):
        self.reliability = value
        return self

    def getResistantToChangedSw(self):
        return self.resistantToChangedSw

    def setResistantToChangedSw(self, value):
        self.resistantToChangedSw = value
        return self

    def getRestoreAtStart(self):
        return self.restoreAtStart

    def setRestoreAtStart(self, value):
        self.restoreAtStart = value
        return self

    def getSelectBlockForFirstInitAll(self):
        return self.selectBlockForFirstInitAll

    def setSelectBlockForFirstInitAll(self, value):
        self.selectBlockForFirstInitAll = value
        return self

    def getStoreAtShutdown(self):
        return self.storeAtShutdown

    def setStoreAtShutdown(self, value):
        self.storeAtShutdown = value
        return self

    def getStoreCyclic(self):
        return self.storeCyclic

    def setStoreCyclic(self, value):
        self.storeCyclic = value
        return self

    def getStoreEmergency(self):
        return self.storeEmergency

    def setStoreEmergency(self, value):
        self.storeEmergency = value
        return self

    def getStoreImmediate(self):
        return self.storeImmediate

    def setStoreImmediate(self, value):
        self.storeImmediate = value
        return self

    def getStoreOnChange(self):
        return self.storeOnChange

    def setStoreOnChange(self, value):
        self.storeOnChange = value
        return self

    def getUseAutoValidationAtShutDown(self):
        return self.useAutoValidationAtShutDown

    def setUseAutoValidationAtShutDown(self, value):
        self.useAutoValidationAtShutDown = value
        return self

    def getUseCRCCompMechanism(self):
        return self.useCRCCompMechanism

    def setUseCRCCompMechanism(self, value):
        self.useCRCCompMechanism = value
        return self

    def getWriteOnlyOnce(self):
        return self.writeOnlyOnce

    def setWriteOnlyOnce(self, value):
        self.writeOnlyOnce = value
        return self

    def getWriteVerification(self):
        return self.writeVerification

    def setWriteVerification(self, value):
        self.writeVerification = value
        return self

    def getWritingFrequency(self):
        return self.writingFrequency

    def setWritingFrequency(self, value):
        self.writingFrequency = value
        return self

    def getWritingPriority(self):
        return self.writingPriority

    def setWritingPriority(self, value):
        self.writingPriority = value
        return self


class RoleBasedDataTypeAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.role = None                                # type: Identifier
        self.usedImplementationDataTypeRef = None       # type: RefType

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getUsedImplementationDataTypeRef(self):
        return self.usedImplementationDataTypeRef

    def setUsedImplementationDataTypeRef(self, value):
        self.usedImplementationDataTypeRef = value
        return self


class ServiceDiagnosticRelevanceEnum(AREnum):
    def __init__(self):
        super().__init__([])
    

class ServiceDependency(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.assignedDataTypes = []                                 # type: List[RoleBasedDataTypeAssignment]
        self.diagnosticRelevance = None                             # type: ServiceDiagnosticRelevanceEnum
        self.symbolicNameProps = None                               # type: SymbolicNameProps

    def getAssignedDataTypes(self):
        return self.assignedDataTypes

    def addAssignedDataType(self, value):
        self.assignedDataTypes.append(value)
        return self

    def getDiagnosticRelevance(self):
        return self.diagnosticRelevance

    def setDiagnosticRelevance(self, value):
        self.diagnosticRelevance = value
        return self

    def getSymbolicNameProps(self):
        return self.symbolicNameProps

    def setSymbolicNameProps(self, value):
        self.symbolicNameProps = value
        return self


class DiagnosticAudienceEnum(AREnum):
    AFTER_MARKET = "aftermarket"
    AFTER_SALES = "afterSales"
    DEVELOPMENT = "development"
    MANUFACTURING = "manufacturing"
    SUPPLIER = "supplier"

    def __init__(self):
        super().__init__((
            DiagnosticAudienceEnum.AFTER_MARKET,
            DiagnosticAudienceEnum.AFTER_SALES,
            DiagnosticAudienceEnum.DEVELOPMENT,
            DiagnosticAudienceEnum.MANUFACTURING,
            DiagnosticAudienceEnum.SUPPLIER,
        ))


class DiagnosticServiceRequestCallbackTypeEnum(AREnum):
    REQUEST_CALLBACK_TYPE_MANUFACTURER = "requestCallbackTypeManufacturer"
    REQUEST_CALLBACK_TYPE_SUPPLIER = "requestCallbackTypeSupplier"

    def __init__(self):
        super().__init__((
            DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER,
            DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_SUPPLIER,
        ))


class DiagnosticCapabilityElement(ServiceNeeds, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagnosticCapabilityElement:
            raise NotImplementedError("DiagnosticCapabilityElement is an abstract class.")
    
        super().__init__(parent, short_name)
       
        self.audiences = []                         # type: List[DiagnosticAudienceEnum]
        self.diagRequirement = None                 # type: DiagRequirementIdString
        self.securityAccessLevel = None             # type: PositiveInteger

    def getAudiences(self):
        return self.audiences

    def addAudience(self, value):
        self.audiences.append(value)
        return self

    def getDiagRequirement(self):
        return self.diagRequirement

    def setDiagRequirement(self, value):
        self.diagRequirement = value
        return self

    def getSecurityAccessLevel(self):
        return self.securityAccessLevel

    def setSecurityAccessLevel(self, value):
        self.securityAccessLevel = value
        return self


class DiagnosticRoutineTypeEnum(AREnum):
    ASYNCHRONOUS = "asynchronous"
    SYNCHRONOUS = "synchronous"

    def __init__(self):
        super().__init__((
            DiagnosticRoutineTypeEnum.ASYNCHRONOUS,
            DiagnosticRoutineTypeEnum.SYNCHRONOUS,
        ))


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.serviceRequestCallbackType = None                                  # type: DiagnosticServiceRequestCallbackTypeEnum

    def getServiceRequestCallbackType(self):
        return self.serviceRequestCallbackType

    def setServiceRequestCallbackType(self, value):
        self.serviceRequestCallbackType = value
        return self


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagRoutineType = None                                             # type: DiagnosticRoutineTypeEnum
        self.RidNumber = None                                                   # type: PositiveInteger

    def getDiagRoutineType(self):
        return self.diagRoutineType

    def setDiagRoutineType(self, value):
        self.diagRoutineType = value
        return self
    
    def getRidNumber(self):
        return self.RidNumber

    def setRidNumber(self, value):
        self.RidNumber = value
        return self


class DiagnosticValueAccessEnum(AREnum):
    READ_ONLY = "readOnly"
    READ_WRITE = "readWrite"
    WRITE_ONLY = "writeOnly"

    def __init__(self):
        super().__init__((
            DiagnosticValueAccessEnum.READ_ONLY,
            DiagnosticValueAccessEnum.READ_WRITE,
            DiagnosticValueAccessEnum.WRITE_ONLY,
        ))


class DiagnosticProcessingStyleEnum(AREnum):
    PROCESSING_STYLE_ASYNCHRONOUS = "processingStyleAsynchronous"
    PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR = "processingStyleAsynchronousWithError"
    PROCESSING_STYLE_SYNCHRONOUS = "processingStyleSynchronous"

    def __init__(self):
        super().__init__((
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS,
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR,
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS,
        ))


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataLength = None                                      # type: PositiveInteger
        self.diagnosticValueAccess = None                           # type: DiagnosticValueAccessEnum
        self.DidNumber = None                                       # type: Integer
        self.fixedLength = None                                     # type: Boolean
        self.processingStyle = None                                 # type: DiagnosticProcessingStyleEnum

    def getDataLength(self):
        return self.dataLength

    def setDataLength(self, value):
        self.dataLength = value
        return self

    def getDiagnosticValueAccess(self):
        return self.diagnosticValueAccess

    def setDiagnosticValueAccess(self, value):
        self.diagnosticValueAccess = value
        return self
    
    def getDidNumber(self):
        return self.DidNumber

    def setDidNumber(self, value):
        self.DidNumber = value
        return self

    def getFixedLength(self):
        return self.fixedLength

    def setFixedLength(self, value):
        self.fixedLength = value
        return self

    def getProcessingStyle(self):
        return self.processingStyle

    def setProcessingStyle(self, value):
        self.processingStyle = value
        return self


class DiagEventDebounceAlgorithm(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DiagEventDebounceAlgorithm:
            raise NotImplementedError("DiagEventDebounceAlgorithm is an abstract class.")

        super().__init__(parent, short_name)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.counterBasedFdcThresholdStorageValue = None                    # type: Integer
        self.counterDecrementStepSize = None                                # type: Integer
        self.counterFailedThreshold = None                                  # type: Integer
        self.counterIncrementStepSize = None                                # type: Integer
        self.counterJumpDown = None                                         # type: Integer
        self.counterJumpDownValue = None                                    # type: Integer
        self.counterJumpUp = None                                           # type: Integer
        self.counterJumpUpValue = None                                      # type: Integer
        self.counterPassedThreshold = None                                  # type: Integer

    def getCounterBasedFdcThresholdStorageValue(self):
        return self.counterBasedFdcThresholdStorageValue

    def setCounterBasedFdcThresholdStorageValue(self, value):
        self.counterBasedFdcThresholdStorageValue = value
        return self

    def getCounterDecrementStepSize(self):
        return self.counterDecrementStepSize

    def setCounterDecrementStepSize(self, value):
        self.counterDecrementStepSize = value
        return self

    def getCounterFailedThreshold(self):
        return self.counterFailedThreshold

    def setCounterFailedThreshold(self, value):
        self.counterFailedThreshold = value
        return self

    def getCounterIncrementStepSize(self):
        return self.counterIncrementStepSize

    def setCounterIncrementStepSize(self, value):
        self.counterIncrementStepSize = value
        return self

    def getCounterJumpDown(self):
        return self.counterJumpDown

    def setCounterJumpDown(self, value):
        self.counterJumpDown = value
        return self

    def getCounterJumpDownValue(self):
        return self.counterJumpDownValue

    def setCounterJumpDownValue(self, value):
        self.counterJumpDownValue = value
        return self

    def getCounterJumpUp(self):
        return self.counterJumpUp

    def setCounterJumpUp(self, value):
        self.counterJumpUp = value
        return self

    def getCounterJumpUpValue(self):
        return self.counterJumpUpValue

    def setCounterJumpUpValue(self, value):
        self.counterJumpUpValue = value
        return self

    def getCounterPassedThreshold(self):
        return self.counterPassedThreshold

    def setCounterPassedThreshold(self, value):
        self.counterPassedThreshold = value
        return self


class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.timeBasedFdcThresholdStorageValue = None                       # type: TimeValue
        self.timeFailedThreshold = None                                     # type: TimeValue
        self.timePassedThreshold = None                                     # type: TimeValue

    def getTimeBasedFdcThresholdStorageValue(self):
        return self.timeBasedFdcThresholdStorageValue

    def setTimeBasedFdcThresholdStorageValue(self, value):
        self.timeBasedFdcThresholdStorageValue = value
        return self

    def getTimeFailedThreshold(self):
        return self.timeFailedThreshold

    def setTimeFailedThreshold(self, value):
        self.timeFailedThreshold = value
        return self

    def getTimePassedThreshold(self):
        return self.timePassedThreshold

    def setTimePassedThreshold(self, value):
        self.timePassedThreshold = value
        return self


class DtcKindEnum(AREnum):
    def __init__(self):
        super().__init__([])


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dtcKind = None                             # type: DtcKindEnum
        self.obdDtcNumber = None                        # type: PositiveInteger
        self.udsDtcNumber = None                        # type: PositiveInteger

    def getDtcKind(self):
        return self.dtcKind

    def setDtcKind(self, value):
        if value is not None:
            self.dtcKind = value
        return self

    def getObdDtcNumber(self):
        return self.obdDtcNumber

    def setObdDtcNumber(self, value):
        if value is not None:
            self.obdDtcNumber = value
        return self

    def getUdsDtcNumber(self):
        return self.udsDtcNumber

    def setUdsDtcNumber(self, value):
        if value is not None:
            self.udsDtcNumber = value
        return self


class DiagnosticClearDtcNotificationEnum(AREnum):
    def __init__(self):
        super().__init__([])


class DtcFormatTypeEnum(AREnum):
    def __init__(self):
        super().__init__([])


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dtcFormatType = None                                                   # type: DtcFormatTypeEnum   # AUTOSAR 4.3.1
        self.notificationTime = None                                                # type: DiagnosticClearDtcNotificationEnum

    def getDtcFormatType(self):
        return self.dtcFormatType

    def setDtcFormatType(self, value):
        if value is not None:
            self.dtcFormatType = value
        return self

    def getNotificationTime(self):
        return self.notificationTime

    def setNotificationTime(self, value):
        if value is not None:
            self.notificationTime = value
        return self


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.deferringFidRefs = []                                      # type: List[RefType]
        self.diagEventDebounceAlgorithm = None                          # type: DiagEventDebounceAlgorithm
        self.inhibitingFidRef = None                                    # type: RefType
        self.inhibitingSecondaryFidRef = None                           # type: RefType
        self.prestoredFreezeframeStoredInNvm = None                     # type: Boolean
        self.usesMonitorData = None                                     # type: Boolean
        self.dtcKind = None                                             # type: ARLiteral
        self.udsDtcNumber = None                                        # type: Integer

    def getDeferringFidRefs(self):
        return self.deferringFidRefs

    def addDeferringFidRef(self, value):
        self.deferringFidRefs.append(value)
        return self
    
    def getDiagEventDebounceAlgorithm(self):
        return self.diagEventDebounceAlgorithm

    def createDiagEventDebounceCounterBased(self, short_name: str):
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceCounterBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)
    
    def createDiagEventDebounceMonitorInternal(self, short_name: str):
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceMonitorInternal(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)

    def createDiagEventDebounceTimeBased(self, short_name: str):
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceTimeBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)
    
    def getInhibitingFidRef(self):
        return self.inhibitingFidRef

    def setInhibitingFidRef(self, value):
        self.inhibitingFidRef = value
        return self

    def getInhibitingSecondaryFidRef(self):
        return self.inhibitingSecondaryFidRef

    def setInhibitingSecondaryFidRef(self, value):
        self.inhibitingSecondaryFidRef = value
        return self

    def getPrestoredFreezeframeStoredInNvm(self):
        return self.prestoredFreezeframeStoredInNvm

    def setPrestoredFreezeframeStoredInNvm(self, value):
        self.prestoredFreezeframeStoredInNvm = value
        return self

    def getUsesMonitorData(self):
        return self.usesMonitorData

    def setUsesMonitorData(self, value):
        self.usesMonitorData = value
        return self

    def getDtcKind(self):
        return self.dtcKind

    def setDtcKind(self, value):
        self.dtcKind = value
        return self

    def getUdsDtcNumber(self):
        return self.udsDtcNumber

    def setUdsDtcNumber(self, value):
        self.udsDtcNumber = value
        return self


class CryptoServiceNeeds(ServiceNeeds):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.algorithmFamily = None                                 # type: String
        self.algorithmMode = None                                   # type: String
        self.cryptoKeyDescription = None                            # type: String
        self.maximumKeyLength = None                                # type: PositiveInteger

    def getAlgorithmFamily(self):
        return self.algorithmFamily

    def setAlgorithmFamily(self, value):
        self.algorithmFamily = value
        return self

    def getAlgorithmMode(self):
        return self.algorithmMode

    def setAlgorithmMode(self, value):
        self.algorithmMode = value
        return self

    def getCryptoKeyDescription(self):
        return self.cryptoKeyDescription

    def setCryptoKeyDescription(self, value):
        self.cryptoKeyDescription = value
        return self

    def getMaximumKeyLength(self):
        return self.maximumKeyLength

    def setMaximumKeyLength(self, value):
        self.maximumKeyLength = value
        return self


class EcuStateMgrUserNeeds(ServiceNeeds):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
