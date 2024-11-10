from abc import ABCMeta
from typing import List


from .....models.ar_object import ARNumerical, ARObject, ARLiteral, ARBoolean, ARPositiveInteger
from .....models.ar_ref import RefType
from .....models.communication import CompositeNetworkRepresentation, TransmissionAcknowledgementRequest
from ...msr.data_dictionary.data_def_properties import SwDataDefProps
from ..common_structure import ValueSpecification

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

        self.modeGroupRef = None                            # type: RefType

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
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
        self.handleOutOfRange = None                    # type: ARLiteral
        self.usesEndToEndProtection = None              # type: ARBoolean     

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self.compositeNetworkRepresentations.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self.compositeNetworkRepresentations

class ModeSwitchSenderComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.enhancedModeApi = None                     # type: ARBoolean
        self.modeGroupRef = None                        # type: RefType
        self.modeSwitchedAck = None                     # type: ModeSwitchedAckRequest
        self.queueLength = None                         # type: ARPositiveInteger

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
