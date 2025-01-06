from abc import ABCMeta
from typing import List
from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from ....M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, ARNumerical, ARPositiveInteger, Boolean, TimeValue
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef

class HandleInvalidEnum(AREnum):
    DONT_INVALIDATE = "dontInvalidate"
    EXTERNAL_REPLACEMENT = "externalReplacement"
    KEEP = "keep"
    REPLACE = "replace"

    def __init__(self):
        super().__init__((
            HandleInvalidEnum.DONT_INVALIDATE,
            HandleInvalidEnum.EXTERNAL_REPLACEMENT,
            HandleInvalidEnum.KEEP,
            HandleInvalidEnum.REPLACE
        ))
    

class PPortComSpec(ARObject, metaclass = ABCMeta):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class 

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self):
        if type(self) == PPortComSpec:
            raise NotImplementedError("PPortComSpec is an abstract class.")
        super().__init__()


class RPortComSpec(ARObject, metaclass = ABCMeta):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class 

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self):
        if type(self) == RPortComSpec:
            raise NotImplementedError("RPortComSpec is an abstract class.")
        
        super().__init__()


class CompositeNetworkRepresentation(ARObject):
    def __init__(self):
        super().__init__()

        self.leafElementIRef = None                 # type: ApplicationCompositeElementInPortInterfaceInstanceRef
        self.networkRepresentation = None           # type: SwDataDefProps

    def getLeafElementIRef(self):
        return self.leafElementIRef

    def setLeafElementIRef(self, value):
        self.leafElementIRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        self.networkRepresentation = value
        return self

class TransmissionAcknowledgementRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None     # type: float


class SenderComSpec(PPortComSpec, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == SenderComSpec:
            raise NotImplementedError("SenderComSpec is an abstract class.")
        
        super().__init__()

        self.compositeNetworkRepresentations = []       # type: List[CompositeNetworkRepresentation]
        self.dataElementRef = None                      # type: RefType
        self.networkRepresentation = None               # type: SwDataDefProps
        self.handleOutOfRange = None                    # type: str
        self.transmissionAcknowledge = None             # type: TransmissionAcknowledgementRequest 
        self.usesEndToEndProtection = None              # type: ARBoolean

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self.compositeNetworkRepresentations.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self.compositeNetworkRepresentations
    
    def getDataElementRef(self):
        return self.dataElementRef

    def setDataElementRef(self, value):
        self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        self.handleOutOfRange = value
        return self

    def getTransmissionAcknowledge(self):
        return self.transmissionAcknowledge

    def setTransmissionAcknowledge(self, value):
        self.transmissionAcknowledge = value
        return self

    def getUsesEndToEndProtection(self):
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        self.usesEndToEndProtection = value
        return self

class QueuedSenderComSpec(SenderComSpec):
    def __init__(self):
        super().__init__()

class NonqueuedSenderComSpec(SenderComSpec):
    def __init__(self):
        super().__init__()
        
        self.initValue = None                               # type: ValueSpecification 

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

class ClientComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.operationRef = None                            # type: RefType

    def getOperationRef(self):
        return self.operationRef

    def setOperationRef(self, value):
        self.operationRef = value
        return self

class ModeSwitchReceiverComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.enhancedModeApi = None                         # type: Boolean
        self.modeGroupRef = None                            # type: RefType
        self.supportsAsynchronousModeSwitch = None          # type: Boolean

    def getEnhancedModeApi(self):
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
        return self
    
    def getSupportsAsynchronousModeSwitch(self):
        return self.supportsAsynchronousModeSwitch

    def setSupportsAsynchronousModeSwitch(self, value):
        self.supportsAsynchronousModeSwitch = value
        return self

class NvRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

class ParameterRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.initValue = None                           # type: ValueSpecification
        self.parameterRef = None                        # type: RefType

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getParameterRef(self):
        return self.parameterRef

    def setParameterRef(self, value):
        self.parameterRef = value
        return self

class ReceiverComSpec(RPortComSpec):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

        self.compositeNetworkRepresentations = []       # type: List[CompositeNetworkRepresentation]
        self.dataElementRef = None                      # type: RefType
        self.networkRepresentation = None               # type: SwDataDefProps
        self.handleOutOfRange = None                    # type: HandleOutOfRangeEnum
        self.handleOutOfRangeStatus = None              # type: HandleOutOfRangeStatusEnum
        self.maxDeltaCounterInit = None                 # type: PositiveInteger
        self.maxNoNewOrRepeatedData = None              # type: PositiveInteger
        self.usesEndToEndProtection = None              # type: ARBoolean     

    def getDataElementRef(self):
        return self.dataElementRef

    def setDataElementRef(self, value):
        self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        self.handleOutOfRange = value
        return self
    
    def getHandleOutOfRangeStatus(self):
        return self.handleOutOfRangeStatus

    def setHandleOutOfRangeStatus(self, value):
        self.handleOutOfRangeStatus = value
        return self

    def getMaxDeltaCounterInit(self):
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value):
        self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        self.maxNoNewOrRepeatedData = value
        return self


    def getUsesEndToEndProtection(self):
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        self.usesEndToEndProtection = value
        return self

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self.compositeNetworkRepresentations.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self.compositeNetworkRepresentations
    
class ModeSwitchedAckRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None                                             # type: TimeValue

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        if value is not None:
            self.timeout = value
        return self

class ModeSwitchSenderComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.enhancedModeApi = None                                     # type: ARBoolean
        self.modeGroupRef = None                                        # type: RefType
        self.modeSwitchedAck = None                                     # type: ModeSwitchedAckRequest
        self.queueLength = None                                         # type: ARPositiveInteger

    def getEnhancedModeApi(self):
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
        return self

    def getModeSwitchedAck(self):
        return self.modeSwitchedAck

    def setModeSwitchedAck(self, value):
        self.modeSwitchedAck = value
        return self

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self



class ParameterProvideComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

class ServerComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()

        self.operationRef = None                    # type: RefType
        self.queueLength = None                     # type: ARNumerical

    def getOperationRef(self):
        return self.operationRef

    def setOperationRef(self, value):
        self.operationRef = value
        return self

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self

class NonqueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self):
        super().__init__()

        self.aliveTimeout = None                # type: ARNumerical
        self.enableUpdated = None               # type: ARBoolean
        self.filter = None                      # type: DataFilter
        self.handleDataStatus = None            # type: ARBoolean
        self.handleNeverReceived = None         # type: ARBoolean
        self.handleTimeoutType = ""
        self.initValue = None                   # type: ValueSpecification
        self.timeoutSubstitution = None         # type: ValueSpecification

    def getAliveTimeout(self):
        return self.aliveTimeout

    def setAliveTimeout(self, value):
        self.aliveTimeout = value
        return self

    def getEnableUpdated(self):
        return self.enableUpdated

    def setEnableUpdated(self, value):
        self.enableUpdated = value
        return self

    def getFilter(self):
        return self.filter

    def setFilter(self, value):
        self.filter = value
        return self

    def getHandleDataStatus(self):
        return self.handleDataStatus

    def setHandleDataStatus(self, value):
        self.handleDataStatus = value
        return self

    def getHandleNeverReceived(self):
        return self.handleNeverReceived

    def setHandleNeverReceived(self, value):
        self.handleNeverReceived = value
        return self

    def getHandleTimeoutType(self):
        return self.handleTimeoutType

    def setHandleTimeoutType(self, value):
        self.handleTimeoutType = value
        return self

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getTimeoutSubstitution(self):
        return self.timeoutSubstitution

    def setTimeoutSubstitution(self, value):
        self.timeoutSubstitution = value
        return self


class QueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self):
        super().__init__()

        self.queueLength = None                    # type: ARPositiveInteger 

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self
