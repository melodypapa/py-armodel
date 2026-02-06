from abc import ABC
from enum import Enum
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Describable,
    Identifiable,
    PackageableElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARLiteral,
    ARNumerical,
    ARPositiveInteger,
    Boolean,
    ByteOrderEnum,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
    UnlimitedInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    TransmissionModeDeclaration,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)


class CommunicationDirectionType(AREnum):
    """
    Enumeration defining communication direction types,
    specifying whether communication is inbound or outbound.
    """
    ENUM_IN = "in"
    ENUM_OUT = "out"

    def __init__(self):
        super().__init__([
            CommunicationDirectionType.ENUM_IN,
            CommunicationDirectionType.ENUM_OUT
        ])


class IPduSignalProcessingEnum(Enum):
    """
    Enumeration defining types of IPDU signal processing,
    specifying whether signal processing is deferred or immediate.
    """
    ENUM_DEFERRED = "deferred"
    ENUM_IMMEDIATE = "immediate"


class FibexElement(PackageableElement, ABC):
    """
    Abstract base class for FIBEX (FIBer EXchange) elements in the
    AUTOSAR system, providing a common foundation for all communication
    elements defined in the FIBEX format used for exchanging communication
    data between tools.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")

        super().__init__(parent, short_name)


class PduToFrameMapping(Identifiable):
    """
    Defines the mapping between Protocol Data Units (PDUs) and frames,
    specifying how PDUs are embedded within frames including byte order,
    start position, and update indication bit position.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.packingByteOrder: ARLiteral = None
        self.pduRef: RefType = None
        self.startPosition: ARNumerical = None
        self.updateIndicationBitPosition: ARNumerical = None

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


class Frame(FibexElement, ABC):
    """
    Abstract base class for communication frames in the AUTOSAR system,
    defining common properties for different types of communication
    frames including frame length and PDU to frame mappings.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")

        super().__init__(parent, short_name)

        self.frameLength = None
        self.pduToFrameMappings: List[PduToFrameMapping] = []

    def getFrameLength(self):
        return self.frameLength

    def setFrameLength(self, value):
        self.frameLength = value
        return self

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if not self.IsElementExists(short_name):
            mapping = PduToFrameMapping(self, short_name)
            self.addElement(mapping)
            self.pduToFrameMappings.append(mapping)
        return self.getElement(short_name, PduToFrameMapping)

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return sorted(filter(lambda a: isinstance(a, PduToFrameMapping), self.elements), key=lambda o: o.short_name)


class ContainedIPduProps(ARObject):
    """
    Defines properties for contained Interaction Protocol Data Units (IPDUs),
    specifying collection semantics, header IDs, offset, timeout,
    trigger, and update indication bit position properties.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.collectionSemantics: ARLiteral = None
        self.headerIdLongHeader: ARPositiveInteger = None
        self.headerIdShortHeader: ARPositiveInteger = None
        self.offset: ARNumerical = None
        self.timeout: ARNumerical = None
        self.trigger: ARLiteral = None
        self.updateIndicationBitPosition: ARNumerical = None

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
    """
    Defines a group of interaction signals in the communication system,
    specifying relationships between individual signals and system-level
    signal groups with transformation properties.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.comBasedSignalGroupTransformationRefs: List[RefType] = []
        self.iSignalRefs: List[RefType] = []
        self.systemSignalGroupRef = None
        self.transformationISignalProps = None

    def getComBasedSignalGroupTransformationRefs(self):
        return self.comBasedSignalGroupTransformationRefs

    def addComBasedSignalGroupTransformationRef(self, value):
        if value is not None:
            self.comBasedSignalGroupTransformationRefs.append(value)
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
    """
    Defines a group of Interaction Protocol Data Units (IPDUs) based on interaction signals,
    specifying communication direction, mode, and references to contained
    IPDU groups and individual IPDUs.
    """
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


class Pdu(FibexElement, ABC):
    """
    Abstract base class for Protocol Data Units (PDUs) in the communication system,
    defining common properties such as dynamic length support and length specifications.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")

        super().__init__(parent, short_name)

        self.hasDynamicLength: Boolean = None
        self.length: UnlimitedInteger = None

    def getHasDynamicLength(self):
        return self.hasDynamicLength

    def setHasDynamicLength(self, value):
        if value is not None:
            self.hasDynamicLength = value
        return self

    def getLength(self):
        return self.length

    def setLength(self, value):
        self.length = value
        return self


class IPdu(Pdu, ABC):
    """
    Abstract base class for Interaction Protocol Data Units (IPDUs),
    extending the PDU class with contained IPDU properties for
    interaction-based communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")

        super().__init__(parent, short_name)

        self.containedIPduProps: ContainedIPduProps = None

    def getContainedIPduProps(self):
        return self.containedIPduProps

    def setContainedIPduProps(self, value):
        if value is not None:
            self.containedIPduProps = value
        return self


class SecureCommunicationProps(ARObject):
    """
    Defines properties for secure communication, including authentication
    data freshness, integrity protection, and secured area specifications
    for protected communication channels.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.authDataFreshnessLength: PositiveInteger = None
        self.authDataFreshnessStartPosition: PositiveInteger = None
        self.authInfoTxLength: PositiveInteger = None
        self.authenticationBuildAttempts: PositiveInteger = None
        self.authenticationRetries: PositiveInteger = None
        self.dataId: PositiveInteger = None
        self.freshnessValueId: PositiveInteger = None
        self.freshnessValueLength: PositiveInteger = None
        self.freshnessValueTxLength: PositiveInteger = None
        self.messageLinkLength: PositiveInteger = None
        self.messageLinkPosition: PositiveInteger = None
        self.secondaryFreshnessValueId: PositiveInteger = None
        self.securedAreaLength: PositiveInteger = None
        self.securedAreaOffset: PositiveInteger = None

    def getAuthDataFreshnessLength(self):
        return self.authDataFreshnessLength

    def setAuthDataFreshnessLength(self, value):
        if value is not None:
            self.authDataFreshnessLength = value
        return self

    def getAuthDataFreshnessStartPosition(self):
        return self.authDataFreshnessStartPosition

    def setAuthDataFreshnessStartPosition(self, value):
        if value is not None:
            self.authDataFreshnessStartPosition = value
        return self

    def getAuthInfoTxLength(self):
        return self.authInfoTxLength

    def setAuthInfoTxLength(self, value):
        if value is not None:
            self.authInfoTxLength = value
        return self

    def getAuthenticationBuildAttempts(self):
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value):
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self):
        return self.authenticationRetries

    def setAuthenticationRetries(self, value):
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self):
        return self.dataId

    def setDataId(self, value):
        if value is not None:
            self.dataId = value
        return self

    def getFreshnessValueId(self):
        return self.freshnessValueId

    def setFreshnessValueId(self, value):
        if value is not None:
            self.freshnessValueId = value
        return self

    def getFreshnessValueLength(self):
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value):
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self):
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value):
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getMessageLinkLength(self):
        return self.messageLinkLength

    def setMessageLinkLength(self, value):
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self):
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value):
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self):
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value):
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredAreaLength(self):
        return self.securedAreaLength

    def setSecuredAreaLength(self, value):
        if value is not None:
            self.securedAreaLength = value
        return self

    def getSecuredAreaOffset(self):
        return self.securedAreaOffset

    def setSecuredAreaOffset(self, value):
        if value is not None:
            self.securedAreaOffset = value
        return self


class SecuredIPdu(IPdu):
    """
    Represents a secured Interaction Protocol Data Unit (IPDU) with
    authentication, integrity protection, and other security properties
    for protected communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.authenticationPropsRef: RefType = None
        self.dynamicRuntimeLengthHandling: Boolean = None
        self.freshnessPropsRef: RefType = None
        self.payloadRef: RefType = None
        self.secureCommunicationProps: SecureCommunicationProps = None
        self.useAsCryptographicIPdu: Boolean = None
        self.useSecuredPduHeader = None

    def getAuthenticationPropsRef(self):
        return self.authenticationPropsRef

    def setAuthenticationPropsRef(self, value):
        if value is not None:
            self.authenticationPropsRef = value
        return self

    def getDynamicRuntimeLengthHandling(self):
        return self.dynamicRuntimeLengthHandling

    def setDynamicRuntimeLengthHandling(self, value):
        if value is not None:
            self.dynamicRuntimeLengthHandling = value
        return self

    def getFreshnessPropsRef(self):
        return self.freshnessPropsRef

    def setFreshnessPropsRef(self, value):
        if value is not None:
            self.freshnessPropsRef = value
        return self

    def getPayloadRef(self):
        return self.payloadRef

    def setPayloadRef(self, value):
        if value is not None:
            self.payloadRef = value
        return self

    def getSecureCommunicationProps(self):
        return self.secureCommunicationProps

    def setSecureCommunicationProps(self, value):
        if value is not None:
            self.secureCommunicationProps = value
        return self

    def getUseAsCryptographicIPdu(self):
        return self.useAsCryptographicIPdu

    def setUseAsCryptographicIPdu(self, value):
        if value is not None:
            self.useAsCryptographicIPdu = value
        return self

    def getUseSecuredPduHeader(self):
        return self.useSecuredPduHeader

    def setUseSecuredPduHeader(self, value):
        if value is not None:
            self.useSecuredPduHeader = value
        return self


class ISignalToIPduMapping(Identifiable):
    """
    Defines the mapping between interaction signals and Interaction Protocol Data Units (IPDUs),
    specifying signal references, byte order, start position, transfer
    properties, and update indication bit position.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef: RefType = None
        self.iSignalGroupRef: RefType = None
        self.packingByteOrder: ByteOrderEnum = None
        self.startPosition: UnlimitedInteger = None
        self.transferProperty = None
        self.updateIndicationBitPosition: UnlimitedInteger = None

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


class NmPdu(Pdu):
    """
    Represents a Network Management Protocol Data Unit (PDU) used for
    network management communication including node monitoring,
    wake-up, and sleep state management.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.iSignalToIPduMappings: List[ISignalToIPduMapping] = []
        self.nmDataInformation: Boolean = None
        self.nmVoteInformation: Boolean = None
        self.unusedBitPattern: Integer = None

    def getISignalToIPduMappings(self):
        return self.iSignalToIPduMappings

    def createISignalToIPduMapping(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToIPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getNmDataInformation(self):
        return self.nmDataInformation

    def setNmDataInformation(self, value):
        if value is not None:
            self.nmDataInformation = value
        return self

    def getNmVoteInformation(self):
        return self.nmVoteInformation

    def setNmVoteInformation(self, value):
        if value is not None:
            self.nmVoteInformation = value
        return self

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        if value is not None:
            self.unusedBitPattern = value
        return self


class NPdu(IPdu):
    """
    Represents a Network Protocol Data Unit (PDU) used for network-level
    communication in the AUTOSAR communication system.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DcmIPdu(IPdu):
    """
    Represents a Diagnostic Communication Management Interaction Protocol Data Unit (IPDU)
    used for diagnostic communication in the AUTOSAR system.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagPduType: ARLiteral = None

    def getDiagPduType(self):
        return self.diagPduType

    def setDiagPduType(self, value):
        self.diagPduType = value
        return self


class IPduTiming(Describable):
    """
    Defines timing properties for Interaction Protocol Data Units (IPDUs),
    specifying minimum delay and transmission mode declaration for
    timed communication.
    """
    def __init__(self):
        super().__init__()

        self.minimumDelay: TimeValue = None
        self.transmissionModeDeclaration: TransmissionModeDeclaration = None

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


class ISignalIPdu(IPdu):
    """
    Represents an Interaction Protocol Data Unit (IPDU) based on interaction signals,
    defining timing specifications, signal-to-PDU mappings, and unused
    bit patterns for signal-based communication.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduTimingSpecification: IPduTiming = None
        self.iSignalToPduMappings: List[ISignalToIPduMapping] = []
        self.unusedBitPattern: Integer = None

    def getIPduTimingSpecification(self):
        return self.iPduTimingSpecification

    def setIPduTimingSpecification(self, value):
        self.iPduTimingSpecification = value
        return self

    def getISignalToPduMappings(self):
        return self.iSignalToPduMappings

    def createISignalToPduMappings(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        self.unusedBitPattern = value
        return self


class ISignal(FibexElement):
    """
    Represents an interaction signal in the communication system,
    defining data transformation, signal type, initialization values,
    length, and system signal references for signal-based communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformationRef = None
        self.dataTypePolicy = None
        self.iSignalProps = None
        self.iSignalType = None
        self.initValue = None
        self.length = None
        self.networkRepresentationProps = None
        self.systemSignalRef: RefType = None
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
    """
    Defines the triggering mechanism for Protocol Data Units (PDUs),
    specifying PDU references, port references, and trigger conditions
    for PDU transmission and reception.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iPduRef: RefType = None
        self.iPduPortRefs: List[RefType] = []
        self.iSignalTriggeringRefs: List[RefType] = []
        self.secOcCryptoMappingRef: RefType = None
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
        # return sorted(self.iSignalTriggeringRefs, key = lambda i: i.getShortValue())
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


class FrameTriggering(Identifiable, ABC):
    """
    Abstract base class for frame triggering mechanisms, defining
    common properties for triggering frame transmission and reception
    including frame references and port references.
    """
    def __init__(self, parent, short_name):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")

        super().__init__(parent, short_name)

        self.frameRef: RefType = None
        self.framePortRefs: List[RefType] = []
        self.pduTriggeringRefs: List[RefType] = []

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
    """
    Represents a system signal in the AUTOSAR system, defining
    dynamic length properties and physical properties for
    system-level signal communication.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicLength: ARBoolean = None
        self.physicalProps: SwDataDefProps = None

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
    """
    Represents a group of system signals, defining relationships
    between individual system signals and transforming signal references
    for grouped signal communication.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.systemSignalRefs: List[RefType] = []
        self.transformingSystemSignalRef: RefType = None

    def getSystemSignalRefs(self):
        return self.systemSignalRefs

    def addSystemSignalRefs(self, value: RefType):
        self.systemSignalRefs.append(value)
        return self

    def getTransformingSystemSignalRef(self):
        return self.transformingSystemSignalRef

    def setTransformingSystemSignalRef(self, value):
        self.transformingSystemSignalRef = value
        return self


class ISignalTriggering(Identifiable):
    """
    Defines triggering properties for interaction signals, specifying
    signal references, group references, and port references for
    signal-based communication triggering.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.iSignalRef: RefType = None
        self.iSignalGroupRef: RefType = None
        self.iSignalPortRefs: List[RefType] = []

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


class SegmentPosition(ARObject):
    """
    Defines the position of a segment within a communication element,
    specifying byte order, length, and position properties for
    segmented communication.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.segmentByteOrder: ByteOrderEnum = None
        self.segmentLength: Integer = None
        self.segmentPosition: Integer = None

    def getSegmentByteOrder(self):
        return self.segmentByteOrder

    def setSegmentByteOrder(self, value):
        if value is not None:
            self.segmentByteOrder = value
        return self

    def getSegmentLength(self):
        return self.segmentLength

    def setSegmentLength(self, value):
        if value is not None:
            self.segmentLength = value
        return self

    def getSegmentPosition(self):
        return self.segmentPosition

    def setSegmentPosition(self, value):
        if value is not None:
            self.segmentPosition = value
        return self


class MultiplexedPart(ARObject, ABC):
    """
    Abstract base class for multiplexed communication parts, defining
    common properties for dynamic and static multiplexed communication
    segments including segment positions.
    """
    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")

        super().__init__()

        self.segmentPositions = []                                 # type: List[SegmentPosition]

    def getSegmentPositions(self):
        return self.segmentPositions

    def addSegmentPosition(self, value):
        if value is not None:
            self.segmentPositions.append(value)
        return self


class StaticPart(MultiplexedPart):
    """
    Defines a static part of multiplexed communication, specifying
    Interaction Protocol Data Unit (IPDU) references for fixed
    segments in multiplexed communication.
    """
    def __init__(self):
        super().__init__()

        self.iPduRef = None                                         # type: RefType

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self


class DynamicPartAlternative(ARObject):
    """
    Defines an alternative for dynamic parts in multiplexed communication,
    specifying selector field codes, initial dynamic part properties,
    and Interaction Protocol Data Unit (IPDU) references.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        super().__init__()

        self.initialDynamicPart = None                              # type: Boolean
        self.iPduRef = None                                         # type: RefType
        self.selectorFieldCode = None                               # type: Integer

    def getInitialDynamicPart(self):
        return self.initialDynamicPart

    def setInitialDynamicPart(self, value):
        if value is not None:
            self.initialDynamicPart = value
        return self

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self

    def getSelectorFieldCode(self):
        return self.selectorFieldCode

    def setSelectorFieldCode(self, value):
        if value is not None:
            self.selectorFieldCode = value
        return self


class DynamicPart(MultiplexedPart):
    """
    Defines a dynamic part of multiplexed communication, specifying
    alternatives for variable segments in multiplexed communication
    based on selector field values.
    """
    def __init__(self):
        super().__init__()

        self.dynamicPartAlternatives = []                          # type: List[DynamicPartAlternative]

    def getDynamicPartAlternatives(self):
        return self.dynamicPartAlternatives

    def addDynamicPartAlternative(self, value):
        if value is not None:
            self.dynamicPartAlternatives.append(value)
        return self


class MultiplexedIPdu(IPdu):
    """
    Represents a multiplexed Interaction Protocol Data Unit (IPDU)
    with dynamic and static parts, defining selector field properties
    and trigger modes for multiplexed communication.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicPart = None                                     # type: DynamicPart
        self.selectorFieldByteOrder = None                          # type: ByteOrderEnum
        self.selectorFieldLength = None                             # type: Integer
        self.selectorFieldStartPosition = None                      # type: Integer
        self.staticPart = None                                      # type: StaticPart
        self.triggerMode = None                                     # type: TriggerMode
        self.unusedBitPattern = None                                # type: Integer

    def getDynamicPart(self):
        return self.dynamicPart

    def setDynamicPart(self, value):
        if value is not None:
            self.dynamicPart = value
        return self

    def getSelectorFieldByteOrder(self):
        return self.selectorFieldByteOrder

    def setSelectorFieldByteOrder(self, value):
        if value is not None:
            self.selectorFieldByteOrder = value
        return self

    def getSelectorFieldLength(self):
        return self.selectorFieldLength

    def setSelectorFieldLength(self, value):
        if value is not None:
            self.selectorFieldLength = value
        return self

    def getSelectorFieldStartPosition(self):
        return self.selectorFieldStartPosition

    def setSelectorFieldStartPosition(self, value):
        if value is not None:
            self.selectorFieldStartPosition = value
        return self

    def getStaticPart(self):
        return self.staticPart

    def setStaticPart(self, value):
        if value is not None:
            self.staticPart = value
        return self

    def getTriggerMode(self):
        return self.triggerMode

    def setTriggerMode(self, value):
        if value is not None:
            self.triggerMode = value
        return self

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        if value is not None:
            self.unusedBitPattern = value
        return self


class GeneralPurposePdu(Pdu):
    """
    Represents a general-purpose Protocol Data Unit (PDU) for flexible
    communication patterns that don't fit into specific PDU categories.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class GeneralPurposeIPdu(IPdu):
    """
    Represents a general-purpose Interaction Protocol Data Unit (IPDU) for flexible
    interaction-based communication patterns that don't fit into specific IPDU categories.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SecureCommunicationPropsSet(FibexElement):
    """
    Represents a set of secure communication properties that can be grouped
    together to define common security configurations for communication channels.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.secureComProps: List[SecureCommunicationProps] = []


class UserDefinedPdu(Pdu):
    """
    Represents a user-defined Protocol Data Unit (PDU) that allows for custom
    communication patterns defined by the user rather than following standard PDU types.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class UserDefinedIPdu(IPdu):
    """
    Represents a user-defined Interaction Protocol Data Unit (IPDU) that allows for custom
    interaction-based communication patterns defined by the user rather than following standard IPDU types.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Defines authentication properties for secure communication,
    including authentication build attempts, retries, and other
    authentication-related security parameters.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.authenticationBuildAttempts: PositiveInteger = None
        self.authenticationRetries: PositiveInteger = None
        self.dataId: PositiveInteger = None
        self.securedComAuthenticationType: ARLiteral = None

    def getAuthenticationBuildAttempts(self):
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value):
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self):
        return self.authenticationRetries

    def setAuthenticationRetries(self, value):
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self):
        return self.dataId

    def setDataId(self, value):
        if value is not None:
            self.dataId = value
        return self

    def getSecuredComAuthenticationType(self):
        return self.securedComAuthenticationType

    def setSecuredComAuthenticationType(self, value):
        if value is not None:
            self.securedComAuthenticationType = value
        return self


class SecureCommunicationFreshnessProps(Identifiable):
    """
    Defines freshness properties for secure communication,
    including freshness value IDs, lengths, and other
    freshness-related security parameters to prevent replay attacks.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.freshnessValueId: PositiveInteger = None
        self.freshnessValueLength: PositiveInteger = None
        self.freshnessValueTxLength: PositiveInteger = None
        self.messageLinkLength: PositiveInteger = None
        self.messageLinkPosition: PositiveInteger = None
        self.secondaryFreshnessValueId: PositiveInteger = None
        self.securedComFreshnessType: ARLiteral = None

    def getFreshnessValueId(self):
        return self.freshnessValueId

    def setFreshnessValueId(self, value):
        if value is not None:
            self.freshnessValueId = value
        return self

    def getFreshnessValueLength(self):
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value):
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self):
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value):
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getMessageLinkLength(self):
        return self.messageLinkLength

    def setMessageLinkLength(self, value):
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self):
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value):
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self):
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value):
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredComFreshnessType(self):
        return self.securedComFreshnessType

    def setSecuredComFreshnessType(self, value):
        if value is not None:
            self.securedComFreshnessType = value
        return self


__all__ = []
