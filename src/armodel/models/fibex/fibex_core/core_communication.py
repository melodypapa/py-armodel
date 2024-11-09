from abc import ABCMeta
from typing import List

from ...ar_ref import RefType
from ...ar_object import ARBoolean, ARFloat, ARLiteral, ARNumerical, ARObject, ARPositiveInteger
from ...general_structure import ARElement, Describable, Identifiable

class FibexElement(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == FibexElement:
            raise NotImplementedError("FibexElement is an abstract class.")
        
        super().__init__(parent, short_name)


class PduToFrameMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.packingByteOrder = None                    # type: ARLiteral
        self.pduRef = None                              # type: RefType
        self.startPosition = None                       # type: ARNumerical
        self.updateIndicationBitPosition = None         # type: ARNumerical

    def getPackingByteOrder(self):
        return self.packingByteOrder

    def setPackingByteOrder(self, value):
        self.packingByteOrder = value
        return self

    def getPduRef(self):
        return self.pduRef

    def setPduRef(self, value):
        self.pduRef = value
        return self

    def getStartPosition(self):
        return self.startPosition

    def setStartPosition(self, value):
        self.startPosition = value
        return self
    
    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self

class Frame(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Frame:
            raise NotImplementedError("Frame is an abstract class.")
        
        super().__init__(parent, short_name)

        self.frameLength = None
        self.pduToFrameMappings = []                # type: List[PduToFrameMapping]

    def getFrameLength(self):
        return self.frameLength

    def setFrameLength(self, value):
        self.frameLength = value
        return self

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if (short_name not in self.elements):
            mapping = PduToFrameMapping(self, short_name)
            self.elements[short_name] = mapping
            self.pduToFrameMappings.append(mapping)
        return self.elements[short_name]

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return list(sorted(filter(lambda a: isinstance(a, PduToFrameMapping), self.elements.values()), key= lambda o:o.short_name))
    
class ContainedIPduProps(ARObject):
    def __init__(self):
        super().__init__()

        self.collectionSemantics = None                 # type: ARLiteral
        self.headerIdLongHeader = None                  # type: ARPositiveInteger
        self.headerIdShortHeader = None                 # type: ARPositiveInteger
        self.offset = None                              # type: ARNumerical
        self.timeout = None                             # type: ARNumerical
        self.trigger = None                             # type: ARLiteral
        self.updateIndicationBitPosition = None         # type: ARNumerical

    def getCollectionSemantics(self):
        return self.collectionSemantics

    def setCollectionSemantics(self, value):
        self.collectionSemantics = value
        return self

    def getHeaderIdLongHeader(self):
        return self.headerIdLongHeader

    def setHeaderIdLongHeader(self, value):
        self.headerIdLongHeader = value
        return self

    def getHeaderIdShortHeader(self):
        return self.headerIdShortHeader

    def setHeaderIdShortHeader(self, value):
        self.headerIdShortHeader = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        self.offset = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        self.timeout = value
        return self

    def getTrigger(self):
        return self.trigger

    def setTrigger(self, value):
        self.trigger = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self

class ISignalGroup(FibexElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.comBasedSignalGroupTransformationRef = None            # type: RefType
        self.iSignalRefs = []                                       # type: List[RefType]
        self.systemSignalGroupRef = None
        self.transformationISignalProps = None

    def getComBasedSignalGroupTransformationRef(self):
        return self.comBasedSignalGroupTransformationRef

    def setComBasedSignalGroupTransformationRef(self, value):
        self.comBasedSignalGroupTransformationRef = value
        return self

    def getISignalRefs(self):
        return self.iSignalRefs

    def addISignalRef(self, value):
        self.iSignalRefs.append(value)
        return self

    def getSystemSignalGroupRef(self):
        return self.systemSignalGroupRef

    def setSystemSignalGroupRef(self, value):
        self.systemSignalGroupRef = value
        return self

    def getTransformationISignalProps(self):
        return self.transformationISignalProps

    def setTransformationISignalProps(self, value):
        self.transformationISignalProps = value
        return self


class ISignalIPduGroup(FibexElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.communicationDirection = None
        self.communicationMode = None
        self.containedISignalIPduGroupRefs = []
        self.iSignalIPduRefs = []
        self.nmPduRefs = []

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        self.communicationDirection = value
        return self

    def getCommunicationMode(self):
        return self.communicationMode

    def setCommunicationMode(self, value):
        self.communicationMode = value
        return self

    def getContainedISignalIPduGroupRefs(self):
        return self.containedISignalIPduGroupRefs

    def addContainedISignalIPduGroupRef(self, value):
        self.containedISignalIPduGroupRefs.append(value)
        return self

    def getISignalIPduRefs(self):
        return self.iSignalIPduRefs

    def addISignalIPduRef(self, value):
        self.iSignalIPduRefs.append(value)
        return self

    def getNmPduRefs(self):
        return self.nmPduRefs

    def addNmPduRef(self, value):
        self.nmPduRefs.append(value)
        return self
    
class Pdu(FibexElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Pdu:
            raise NotImplementedError("Pdu is an abstract class.")
        
        super().__init__(parent, short_name)

        self.length = None                  # type: ARNumerical

    def getLength(self):
        return self.length

    def setLength(self, value):
        self.length = value
        return self
    
class IPdu(Pdu, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == IPdu:
            raise NotImplementedError("IPdu is an abstract class.")
        
        super().__init__(parent, short_name)

        self.containedOpduProps = None       # type: ContainedIPduProps

    def getContainedOpduProps(self):
        return self.containedOpduProps

    def setContainedOpduProps(self, value):
        self.containedOpduProps = value
        return self
    
class SecuredIPdu(IPdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
    
class NmPdu(Pdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
    

class NPdu(IPdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DcmIPdu(IPdu):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagPduType = None                                 # type: ARLiteral

    def getDiagPduType(self):
        return self.diagPduType

    def setDiagPduType(self, value):
        self.diagPduType = value
        return self


class IPduTiming(Describable):
    def __init__(self):
        super().__init__()

        self.minimumDelay = None                                # type: TimeValue
        # type: TransmissionModeDeclaration
        self.transmissionModeDeclaration = None

    def getMinimumDelay(self):
        return self.minimumDelay

    def setMinimumDelay(self, value):
        self.minimumDelay = value
        return self

    def getTransmissionModeDeclaration(self):
        return self.transmissionModeDeclaration

    def setTransmissionModeDeclaration(self, value):
        self.transmissionModeDeclaration = value
        return self
    
class ISignalToIPduMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef = None                              # type: RefType
        self.iSignalGroupRef = None                         # type: RefType
        self.packingByteOrder = None                        # type: ByteOrderEnum
        self.startPosition = None                           # type: ARNumerical
        # type: TransferPropertyEnum
        self.transferProperty = None
        self.updateIndicationBitPosition = None             # type: ARNumerical

    def getISignalRef(self):
        return self.iSignalRef

    def setISignalRef(self, value):
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self):
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        self.iSignalGroupRef = value
        return self

    def getPackingByteOrder(self):
        return self.packingByteOrder

    def setPackingByteOrder(self, value):
        self.packingByteOrder = value
        return self

    def getStartPosition(self):
        return self.startPosition

    def setStartPosition(self, value):
        self.startPosition = value
        return self

    def getTransferProperty(self):
        return self.transferProperty

    def setTransferProperty(self, value):
        self.transferProperty = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self

    
class ISignalIPdu(IPdu):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduTimingSpecification = None                     # type: IPduTiming
        self.iSignalToPduMappings = []                          # type: List[ISignalToIPduMapping]
        self.unusedBitPattern = None                            # type: ARNumerical

    def getIPduTimingSpecification(self):
        return self.iPduTimingSpecification

    def setIPduTimingSpecification(self, value):
        self.iPduTimingSpecification = value
        return self

    def getISignalToPduMappings(self):
        return self.iSignalToPduMappings

    def createISignalToPduMappings(self, short_name: str) -> ISignalToIPduMapping:
        if (short_name not in self.elements):
            mapping = ISignalToIPduMapping(self, short_name)
            self.elements[short_name] = mapping
            self.iSignalToPduMappings.append(mapping)
        return self.elements[short_name]

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        self.unusedBitPattern = value
        return self


class ISignal(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformationRef = None
        self.dataTypePolicy = None
        self.iSignalProps = None
        self.iSignalType = None
        self.initValue = None
        self.length = None
        self.networkRepresentationProps = None
        self.systemSignalRef = None                  # type: RefType
        self.timeoutSubstitutionValue = None
        self.transformationISignalProps = []

    def getDataTransformationRef(self):
        return self.dataTransformationRef

    def setDataTransformationRef(self, value):
        self.dataTransformationRef = value
        return self

    def getDataTypePolicy(self):
        return self.dataTypePolicy

    def setDataTypePolicy(self, value):
        self.dataTypePolicy = value
        return self

    def getISignalProps(self):
        return self.iSignalProps

    def setISignalProps(self, value):
        self.iSignalProps = value
        return self

    def getISignalType(self):
        return self.iSignalType

    def setISignalType(self, value):
        self.iSignalType = value
        return self

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getLength(self):
        return self.length

    def setLength(self, value):
        self.length = value
        return self

    def getNetworkRepresentationProps(self):
        return self.networkRepresentationProps

    def setNetworkRepresentationProps(self, value):
        self.networkRepresentationProps = value
        return self

    def getSystemSignalRef(self):
        return self.systemSignalRef

    def setSystemSignalRef(self, value):
        self.systemSignalRef = value
        return self

    def getTimeoutSubstitutionValue(self):
        return self.timeoutSubstitutionValue

    def setTimeoutSubstitutionValue(self, value):
        self.timeoutSubstitutionValue = value
        return self

    def getTransformationISignalProps(self):
        return self.transformationISignalProps

    def addTransformationISignalProps(self, value):
        self.transformationISignalProps.append(value)
        return self
    
class PduTriggering(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduRef = None                         # type: RefType
        self.iPduPortRefs = []                      # type: List[RefType]
        self.iSignalTriggeringRefs = []             # type: List[RefType]
        self.secOcCryptoMappingRef = None           # type: RefType
        self.triggerIPduSendConditions = []         # type: List

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        self.iPduRef = value
        return self

    def getIPduPortRefs(self):
        return self.iPduPortRefs

    def addIPduPortRef(self, value):
        self.iPduPortRefs.append(value)
        return self

    def getISignalTriggeringRefs(self):
        return self.iSignalTriggeringRefs

    def addISignalTriggeringRef(self, value):
        self.iSignalTriggeringRefs.append(value)
        return self

    def getSecOcCryptoMappingRef(self):
        return self.secOcCryptoMappingRef

    def setSecOcCryptoMappingRef(self, value):
        self.secOcCryptoMappingRef = value
        return self

    def getTriggerIPduSendConditions(self):
        return self.triggerIPduSendConditions

    def addTriggerIPduSendCondition(self, value):
        self.triggerIPduSendConditions.append(value)
        return self


class FrameTriggering(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent, short_name):
        if type(self) == FrameTriggering:
            raise NotImplementedError("FrameTriggering is an abstract class.")
        
        super().__init__(parent, short_name)

        self.frameRef = None                        # type: RefType
        self.framePortRefs = []                     # type: List[RefType]
        self.pduTriggeringRefs = []                 # type: List[RefType]

    def getFrameRef(self) -> RefType:
        return self.frameRef

    def setFrameRef(self, value: RefType):
        self.frameRef = value
        return self

    def getFramePortRefs(self) -> List[RefType]:
        return self.framePortRefs

    def addFramePortRef(self, value: RefType):
        self.framePortRefs.append(value)
        return self

    def getPduTriggeringRefs(self) -> RefType:
        return self.pduTriggeringRefs

    def addPduTriggeringRef(self, value: RefType):
        self.pduTriggeringRefs.append(value)
        return self

class SystemSignal(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicLength = None                   # type: ARBoolean
        self.physicalProps = None                   # type: SwDataDefProps

    def getDynamicLength(self):
        return self.dynamicLength

    def setDynamicLength(self, value):
        self.dynamicLength = value
        return self

    def getPhysicalProps(self):
        return self.physicalProps

    def setPhysicalProps(self, value):
        self.physicalProps = value
        return self

class SystemSignalGroup(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.systemSignalRefs = []                  # type: List[RefType]
        self.transformingSystemSignalRef = None     # type: RefType

    def getSystemSignalRefs(self):
        return self.systemSignalRefs

    def addSystemSignalRefs(self, value:RefType):
        self.systemSignalRefs.append(value)
        return self

    def getTransformingSystemSignalRef(self):
        return self.transformingSystemSignalRef

    def setTransformingSystemSignalRef(self, value):
        self.transformingSystemSignalRef = value
        return self

class ISignalTriggering(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef = None                      # type: RefType
        self.iSignalGroupRef = None                 # type: RefType
        self.iSignalPortRefs = []                   # type: List[RefType]

    def getISignalRef(self):
        return self.iSignalRef

    def setISignalRef(self, value):
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self):
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        self.iSignalGroupRef = value
        return self

    def getISignalPortRefs(self):
        return self.iSignalPortRefs

    def addISignalPortRef(self, value):
        self.iSignalPortRefs.append(value)
        return self
