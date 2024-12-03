from abc import ABCMeta
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, ARLiteral, DiagRequirementIdString, PositiveInteger, RefType, String, TimeValue

class RoleBasedDataAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.role = None                    # type: ARLiteral
        self.usedDataElement = None         # type: RefType # AutosarVariableRef
        self.usedParameterElement = None    # type: RefType # AutosarParameterRef
        self.used_pim_ref = None            # type: RefType


class ServiceNeeds(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ServiceNeeds:
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
        # type: RamBlockStatusControlEnum
        self.ramBlockStatusControl = None
        self.readonly = None                            # type: Boolean
        # type: NvBlockNeedsReliabilityEnum
        self.reliability = None
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
        # type: NvBlockNeedsWritingPriorityEnum
        self.writingPriority = None

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

class ServiceDependency(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

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

class DiagnosticCapabilityElement(ServiceNeeds, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == DiagnosticCapabilityElement:
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
    
class DiagEventDebounceAlgorithm(ARLiteral):
    def __init__(self):
        super().__init__()

class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.deferringFidRefs = []                                      # type: List[RefType]
        self.diagEventDebounceAlgorithm = None                          # type: DiagEventDebounceAlgorithm
        self.inhibitingFidRef = None                                    # type: RefType
        self.inhibitingSecondaryFidRef = None                           # type: RefType
        self.prestoredFreezeframeStoredInNvm = None                     # type: Boolean
        self.usesMonitorData = None                                     # type: Boolean

    def getDeferringFidRefs(self):
        return self.deferringFidRefs

    def addDeferringFidRef(self, value):
        self.deferringFidRefs.append(value)
        return self

    def getDiagEventDebounceAlgorithm(self):
        return self.diagEventDebounceAlgorithm

    def setDiagEventDebounceAlgorithm(self, value):
        self.diagEventDebounceAlgorithm = value
        return self

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
