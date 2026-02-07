from abc import ABC
from enum import Enum
from typing import Any, List, Union

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

    def __init__(self) -> None:
        super().__init__([
            CommunicationDirectionType.ENUM_IN,
            CommunicationDirectionType.ENUM_OUT
        ])


class IPduSignalProcessingEnum(AREnum):
    """
    Enumeration defining types of IPDU signal processing,
    specifying whether signal processing is deferred or immediate.
    """
    ENUM_DEFERRED = "deferred"
    ENUM_IMMEDIATE = "immediate"

    def __init__(self) -> None:
        super().__init__([
            IPduSignalProcessingEnum.ENUM_DEFERRED,
            IPduSignalProcessingEnum.ENUM_IMMEDIATE
        ])


class FibexElement(PackageableElement, ABC):
    """
    Abstract base class for FIBEX (FIBer EXchange) elements in the
    AUTOSAR system, providing a common foundation for all communication
    elements defined in the FIBEX format used for exchanging communication
    data between tools.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")

        super().__init__(parent, short_name)


class PduToFrameMapping(Identifiable):
    """
    Defines the mapping between Protocol Data Units (PDUs) and frames,
    specifying how PDUs are embedded within frames including byte order,
    start position, and update indication bit position.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.packingByteOrder: Union[Union[ARLiteral, None] , None] = None
        self.pduRef: Union[Union[RefType, None] , None] = None
        self.startPosition: Union[Union[ARNumerical, None] , None] = None
        self.updateIndicationBitPosition: Union[Union[ARNumerical, None] , None] = None

    def getPackingByteOrder(self) -> Union[Union[ARLiteral, None], None]:
        return self.packingByteOrder

    def setPackingByteOrder(self, value: Union[Union[ARLiteral, None], None]) -> "PduToFrameMapping":
        self.packingByteOrder = value
        return self

    def getPduRef(self) -> Union[Union[RefType, None], None]:
        return self.pduRef

    def setPduRef(self, value: Union[Union[RefType, None], None]) -> "PduToFrameMapping":
        self.pduRef = value
        return self

    def getStartPosition(self) -> Union[Union[ARNumerical, None], None]:
        return self.startPosition

    def setStartPosition(self, value: Union[Union[ARNumerical, None], None]) -> "PduToFrameMapping":
        self.startPosition = value
        return self

    def getUpdateIndicationBitPosition(self) -> Union[Union[ARNumerical, None], None]:
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Union[Union[ARNumerical, None], None]) -> "PduToFrameMapping":
        self.updateIndicationBitPosition = value
        return self


class Frame(FibexElement, ABC):
    """
    Abstract base class for communication frames in the AUTOSAR system,
    defining common properties for different types of communication
    frames including frame length and PDU to frame mappings.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")

        super().__init__(parent, short_name)

        self.frameLength = None
        self.pduToFrameMappings: List[PduToFrameMapping] = []

    def getFrameLength(self) -> Union[int, None]:
        return self.frameLength

    def setFrameLength(self, value: Union[int, None]) -> "Frame":
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

    def __init__(self) -> None:
        super().__init__()

        self.collectionSemantics: Union[Union[ARLiteral, None] , None] = None
        self.headerIdLongHeader: Union[Union[ARPositiveInteger, None] , None] = None
        self.headerIdShortHeader: Union[Union[ARPositiveInteger, None] , None] = None
        self.offset: Union[Union[ARNumerical, None] , None] = None
        self.timeout: Union[Union[ARNumerical, None] , None] = None
        self.trigger: Union[Union[ARLiteral, None] , None] = None
        self.updateIndicationBitPosition: Union[Union[ARNumerical, None] , None] = None

    def getCollectionSemantics(self) -> Union[Union[ARLiteral, None], None]:
        return self.collectionSemantics

    def setCollectionSemantics(self, value: Union[Union[ARLiteral, None], None]) -> "ContainedIPduProps":
        self.collectionSemantics = value
        return self

    def getHeaderIdLongHeader(self) -> Union[Union[ARPositiveInteger, None], None]:
        return self.headerIdLongHeader

    def setHeaderIdLongHeader(self, value: Union[Union[ARPositiveInteger, None], None]) -> "ContainedIPduProps":
        self.headerIdLongHeader = value
        return self

    def getHeaderIdShortHeader(self) -> Union[Union[ARPositiveInteger, None], None]:
        return self.headerIdShortHeader

    def setHeaderIdShortHeader(self, value: Union[Union[ARPositiveInteger, None], None]) -> "ContainedIPduProps":
        self.headerIdShortHeader = value
        return self

    def getOffset(self) -> Union[Union[ARNumerical, None], None]:
        return self.offset

    def setOffset(self, value: Union[Union[ARNumerical, None], None]) -> "ContainedIPduProps":
        self.offset = value
        return self

    def getTimeout(self) -> Union[Union[ARNumerical, None], None]:
        return self.timeout

    def setTimeout(self, value: Union[Union[ARNumerical, None], None]) -> "ContainedIPduProps":
        self.timeout = value
        return self

    def getTrigger(self) -> Union[Union[ARLiteral, None], None]:
        return self.trigger

    def setTrigger(self, value: Union[Union[ARLiteral, None], None]) -> "ContainedIPduProps":
        self.trigger = value
        return self

    def getUpdateIndicationBitPosition(self) -> Union[Union[ARNumerical, None], None]:
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Union[Union[ARNumerical, None], None]) -> "ContainedIPduProps":
        self.updateIndicationBitPosition = value
        return self


class ISignalGroup(FibexElement):
    """
    Defines a group of interaction signals in the communication system,
    specifying relationships between individual signals and system-level
    signal groups with transformation properties.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.comBasedSignalGroupTransformationRefs: List[RefType] = []
        self.iSignalRefs: List[RefType] = []
        self.systemSignalGroupRef = None
        self.transformationISignalProps = None

    def getComBasedSignalGroupTransformationRefs(self) -> List[RefType]:
        return self.comBasedSignalGroupTransformationRefs

    def addComBasedSignalGroupTransformationRef(self, value: RefType) -> "ISignalGroup":
        if value is not None:
            self.comBasedSignalGroupTransformationRefs.append(value)
        return self

    def getISignalRefs(self) -> List[RefType]:
        return self.iSignalRefs

    def addISignalRef(self, value: RefType) -> "ISignalGroup":
        self.iSignalRefs.append(value)
        return self

    def getSystemSignalGroupRef(self) -> Union[RefType, None]:
        return self.systemSignalGroupRef

    def setSystemSignalGroupRef(self, value: Union[RefType, None]) -> "ISignalGroup":
        self.systemSignalGroupRef = value
        return self

    def getTransformationISignalProps(self) -> Union[Any, None]:
        return self.transformationISignalProps

    def setTransformationISignalProps(self, value: Union[Any, None]) -> "ISignalGroup":
        self.transformationISignalProps = value
        return self


class ISignalIPduGroup(FibexElement):
    """
    Defines a group of Interaction Protocol Data Units (IPDUs) based on interaction signals,
    specifying communication direction, mode, and references to contained
    IPDU groups and individual IPDUs.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.communicationDirection = None
        self.communicationMode = None
        self.containedISignalIPduGroupRefs: List[RefType] = []
        self.iSignalIPduRefs: List[RefType] = []
        self.nmPduRefs: List[RefType] = []

    def getCommunicationDirection(self) -> Union[Any, None]:
        return self.communicationDirection

    def setCommunicationDirection(self, value: Union[Any, None]) -> "ISignalIPduGroup":
        self.communicationDirection = value
        return self

    def getCommunicationMode(self) -> Union[Any, None]:
        return self.communicationMode

    def setCommunicationMode(self, value: Union[Any, None]) -> "ISignalIPduGroup":
        self.communicationMode = value
        return self

    def getContainedISignalIPduGroupRefs(self) -> List[RefType]:
        return self.containedISignalIPduGroupRefs

    def addContainedISignalIPduGroupRef(self, value: RefType) -> "ISignalIPduGroup":
        self.containedISignalIPduGroupRefs.append(value)
        return self

    def getISignalIPduRefs(self) -> List[RefType]:
        return self.iSignalIPduRefs

    def addISignalIPduRef(self, value: RefType) -> "ISignalIPduGroup":
        self.iSignalIPduRefs.append(value)
        return self

    def getNmPduRefs(self) -> List[RefType]:
        return self.nmPduRefs

    def addNmPduRef(self, value: RefType) -> "ISignalIPduGroup":
        self.nmPduRefs.append(value)
        return self


class Pdu(FibexElement, ABC):
    """
    Abstract base class for Protocol Data Units (PDUs) in the communication system,
    defining common properties such as dynamic length support and length specifications.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")

        super().__init__(parent, short_name)

        self.hasDynamicLength: Union[Union[Boolean, None] , None] = None
        self.length: Union[Union[UnlimitedInteger, None] , None] = None

    def getHasDynamicLength(self) -> Union[ARBoolean, None]:
        return self.hasDynamicLength

    def setHasDynamicLength(self, value: Union[ARBoolean, None]) -> "Pdu":
        if value is not None:
            self.hasDynamicLength = value
        return self

    def getLength(self) -> Union[Union[UnlimitedInteger, None], None]:
        return self.length

    def setLength(self, value: Union[Union[UnlimitedInteger, None], None]) -> "Pdu":
        self.length = value
        return self


class IPdu(Pdu, ABC):
    """
    Abstract base class for Interaction Protocol Data Units (IPDUs),
    extending the PDU class with contained IPDU properties for
    interaction-based communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")

        super().__init__(parent, short_name)

        self.containedIPduProps: Union[Union[ContainedIPduProps, None] , None] = None

    def getContainedIPduProps(self) -> Union[Union[ContainedIPduProps, None], None]:
        return self.containedIPduProps

    def setContainedIPduProps(self, value: Union[Union[ContainedIPduProps, None], None]) -> "IPdu":
        if value is not None:
            self.containedIPduProps = value
        return self


class SecureCommunicationProps(ARObject):
    """
    Defines properties for secure communication, including authentication
    data freshness, integrity protection, and secured area specifications
    for protected communication channels.
    """

    def __init__(self) -> None:
        super().__init__()

        self.authDataFreshnessLength: Union[Union[PositiveInteger, None] , None] = None
        self.authDataFreshnessStartPosition: Union[Union[PositiveInteger, None] , None] = None
        self.authInfoTxLength: Union[Union[PositiveInteger, None] , None] = None
        self.authenticationBuildAttempts: Union[Union[PositiveInteger, None] , None] = None
        self.authenticationRetries: Union[Union[PositiveInteger, None] , None] = None
        self.dataId: Union[Union[PositiveInteger, None] , None] = None
        self.freshnessValueId: Union[Union[PositiveInteger, None] , None] = None
        self.freshnessValueLength: Union[Union[PositiveInteger, None] , None] = None
        self.freshnessValueTxLength: Union[Union[PositiveInteger, None] , None] = None
        self.messageLinkLength: Union[Union[PositiveInteger, None] , None] = None
        self.messageLinkPosition: Union[Union[PositiveInteger, None] , None] = None
        self.secondaryFreshnessValueId: Union[Union[PositiveInteger, None] , None] = None
        self.securedAreaLength: Union[Union[PositiveInteger, None] , None] = None
        self.securedAreaOffset: Union[Union[PositiveInteger, None] , None] = None

    def getAuthDataFreshnessLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authDataFreshnessLength

    def setAuthDataFreshnessLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.authDataFreshnessLength = value
        return self

    def getAuthDataFreshnessStartPosition(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authDataFreshnessStartPosition

    def setAuthDataFreshnessStartPosition(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.authDataFreshnessStartPosition = value
        return self

    def getAuthInfoTxLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authInfoTxLength

    def setAuthInfoTxLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.authInfoTxLength = value
        return self

    def getAuthenticationBuildAttempts(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authenticationRetries

    def setAuthenticationRetries(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.dataId

    def setDataId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.dataId = value
        return self

    def getFreshnessValueId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueId

    def setFreshnessValueId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.freshnessValueId = value
        return self

    def getFreshnessValueLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getMessageLinkLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.messageLinkLength

    def setMessageLinkLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self) -> Union[Union[PositiveInteger, None], None]:
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredAreaLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.securedAreaLength

    def setSecuredAreaLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.securedAreaLength = value
        return self

    def getSecuredAreaOffset(self) -> Union[Union[PositiveInteger, None], None]:
        return self.securedAreaOffset

    def setSecuredAreaOffset(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationProps":
        if value is not None:
            self.securedAreaOffset = value
        return self


class SecuredIPdu(IPdu):
    """
    Represents a secured Interaction Protocol Data Unit (IPDU) with
    authentication, integrity protection, and other security properties
    for protected communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.authenticationPropsRef: Union[Union[RefType, None] , None] = None
        self.dynamicRuntimeLengthHandling: Union[Union[Boolean, None] , None] = None
        self.freshnessPropsRef: Union[Union[RefType, None] , None] = None
        self.payloadRef: Union[Union[RefType, None] , None] = None
        self.secureCommunicationProps: Union[Union[SecureCommunicationProps, None] , None] = None
        self.useAsCryptographicIPdu: Union[Union[Boolean, None] , None] = None
        self.useSecuredPduHeader = None

    def getAuthenticationPropsRef(self) -> Union[Union[RefType, None], None]:
        return self.authenticationPropsRef

    def setAuthenticationPropsRef(self, value: Union[Union[RefType, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.authenticationPropsRef = value
        return self

    def getDynamicRuntimeLengthHandling(self) -> Union[Union[Boolean, None], None]:
        return self.dynamicRuntimeLengthHandling

    def setDynamicRuntimeLengthHandling(self, value: Union[Union[Boolean, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.dynamicRuntimeLengthHandling = value
        return self

    def getFreshnessPropsRef(self) -> Union[Union[RefType, None], None]:
        return self.freshnessPropsRef

    def setFreshnessPropsRef(self, value: Union[Union[RefType, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.freshnessPropsRef = value
        return self

    def getPayloadRef(self) -> Union[Union[RefType, None], None]:
        return self.payloadRef

    def setPayloadRef(self, value: Union[Union[RefType, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.payloadRef = value
        return self

    def getSecureCommunicationProps(self) -> Union[Union[SecureCommunicationProps, None], None]:
        return self.secureCommunicationProps

    def setSecureCommunicationProps(self, value: Union[Union[SecureCommunicationProps, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.secureCommunicationProps = value
        return self

    def getUseAsCryptographicIPdu(self) -> Union[Union[Boolean, None], None]:
        return self.useAsCryptographicIPdu

    def setUseAsCryptographicIPdu(self, value: Union[Union[Boolean, None], None]) -> "SecuredIPdu":
        if value is not None:
            self.useAsCryptographicIPdu = value
        return self

    def getUseSecuredPduHeader(self) -> Union[ARBoolean, None]:
        return self.useSecuredPduHeader

    def setUseSecuredPduHeader(self, value: Union[ARBoolean, None]) -> "SecuredIPdu":
        if value is not None:
            self.useSecuredPduHeader = value
        return self


class ISignalToIPduMapping(Identifiable):
    """
    Defines the mapping between interaction signals and Interaction Protocol Data Units (IPDUs),
    specifying signal references, byte order, start position, transfer
    properties, and update indication bit position.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.iSignalRef: Union[Union[RefType, None] , None] = None
        self.iSignalGroupRef: Union[Union[RefType, None] , None] = None
        self.packingByteOrder: Union[Union[ByteOrderEnum, None] , None] = None
        self.startPosition: Union[Union[UnlimitedInteger, None] , None] = None
        self.transferProperty = None
        self.updateIndicationBitPosition: Union[Union[UnlimitedInteger, None] , None] = None

    def getISignalRef(self) -> Union[Union[RefType, None], None]:
        return self.iSignalRef

    def setISignalRef(self, value: Union[Union[RefType, None], None]) -> "ISignalToIPduMapping":
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self) -> Union[Union[RefType, None], None]:
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value: Union[Union[RefType, None], None]) -> "ISignalToIPduMapping":
        self.iSignalGroupRef = value
        return self

    def getPackingByteOrder(self) -> Union[Union[ByteOrderEnum, None], None]:
        return self.packingByteOrder

    def setPackingByteOrder(self, value: Union[Union[ByteOrderEnum, None], None]) -> "ISignalToIPduMapping":
        self.packingByteOrder = value
        return self

    def getStartPosition(self) -> Union[Union[UnlimitedInteger, None], None]:
        return self.startPosition

    def setStartPosition(self, value: Union[Union[UnlimitedInteger, None], None]) -> "ISignalToIPduMapping":
        self.startPosition = value
        return self

    def getTransferProperty(self) -> Union[Any, None]:
        return self.transferProperty

    def setTransferProperty(self, value: Union[Any, None]) -> "ISignalToIPduMapping":
        self.transferProperty = value
        return self

    def getUpdateIndicationBitPosition(self) -> Union[Union[UnlimitedInteger, None], None]:
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Union[Union[UnlimitedInteger, None], None]) -> "ISignalToIPduMapping":
        self.updateIndicationBitPosition = value
        return self


class NmPdu(Pdu):
    """
    Represents a Network Management Protocol Data Unit (PDU) used for
    network management communication including node monitoring,
    wake-up, and sleep state management.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.iSignalToIPduMappings: List[ISignalToIPduMapping] = []
        self.nmDataInformation: Union[Union[Boolean, None] , None] = None
        self.nmVoteInformation: Union[Union[Boolean, None] , None] = None
        self.unusedBitPattern: Union[Union[Integer, None] , None] = None

    def getISignalToIPduMappings(self) -> List[ISignalToIPduMapping]:
        return self.iSignalToIPduMappings

    def createISignalToIPduMapping(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToIPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getNmDataInformation(self) -> Union[Union[Boolean, None], None]:
        return self.nmDataInformation

    def setNmDataInformation(self, value: Union[Union[Boolean, None], None]) -> "NmPdu":
        if value is not None:
            self.nmDataInformation = value
        return self

    def getNmVoteInformation(self) -> Union[Union[Boolean, None], None]:
        return self.nmVoteInformation

    def setNmVoteInformation(self, value: Union[Union[Boolean, None], None]) -> "NmPdu":
        if value is not None:
            self.nmVoteInformation = value
        return self

    def getUnusedBitPattern(self) -> Union[Union[Integer, None], None]:
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Union[Union[Integer, None], None]) -> "NmPdu":
        if value is not None:
            self.unusedBitPattern = value
        return self


class NPdu(IPdu):
    """
    Represents a Network Protocol Data Unit (PDU) used for network-level
    communication in the AUTOSAR communication system.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class DcmIPdu(IPdu):
    """
    Represents a Diagnostic Communication Management Interaction Protocol Data Unit (IPDU)
    used for diagnostic communication in the AUTOSAR system.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.diagPduType: Union[Union[ARLiteral, None] , None] = None

    def getDiagPduType(self) -> Union[Union[ARLiteral, None], None]:
        return self.diagPduType

    def setDiagPduType(self, value: Union[Union[ARLiteral, None], None]) -> "DcmIPdu":
        self.diagPduType = value
        return self


class IPduTiming(Describable):
    """
    Defines timing properties for Interaction Protocol Data Units (IPDUs),
    specifying minimum delay and transmission mode declaration for
    timed communication.
    """
    def __init__(self) -> None:
        super().__init__()

        self.minimumDelay: Union[Union[TimeValue, None] , None] = None
        self.transmissionModeDeclaration: Union[Union[TransmissionModeDeclaration, None] , None] = None

    def getMinimumDelay(self) -> Union[Union[TimeValue, None], None]:
        return self.minimumDelay

    def setMinimumDelay(self, value: Union[Union[TimeValue, None], None]) -> "ISignalIPduTiming":
        self.minimumDelay = value
        return self

    def getTransmissionModeDeclaration(self) -> Union[Union[TransmissionModeDeclaration, None], None]:
        return self.transmissionModeDeclaration

    def setTransmissionModeDeclaration(self, value: Union[Union[TransmissionModeDeclaration, None], None]) -> "ISignalIPduTiming":
        self.transmissionModeDeclaration = value
        return self


class ISignalIPdu(IPdu):
    """
    Represents an Interaction Protocol Data Unit (IPDU) based on interaction signals,
    defining timing specifications, signal-to-PDU mappings, and unused
    bit patterns for signal-based communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.iPduTimingSpecification: Union[Union[IPduTiming, None] , None] = None
        self.iSignalToPduMappings: List[ISignalToIPduMapping] = []
        self.unusedBitPattern: Union[Union[Integer, None] , None] = None

    def getIPduTimingSpecification(self) -> Union[Union[IPduTiming, None], None]:
        return self.iPduTimingSpecification

    def setIPduTimingSpecification(self, value: Union[Union[IPduTiming, None], None]) -> "ISignalIPdu":
        self.iPduTimingSpecification = value
        return self

    def getISignalToPduMappings(self) -> List[ISignalToIPduMapping]:
        return self.iSignalToPduMappings

    def createISignalToPduMappings(self, short_name: str) -> ISignalToIPduMapping:
        if not self.IsElementExists(short_name):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getUnusedBitPattern(self) -> Union[Union[Integer, None], None]:
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Union[Union[Integer, None], None]) -> "ISignalIPdu":
        self.unusedBitPattern = value
        return self


class ISignal(FibexElement):
    """
    Represents an interaction signal in the communication system,
    defining data transformation, signal type, initialization values,
    length, and system signal references for signal-based communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.dataTransformationRef = None
        self.dataTypePolicy = None
        self.iSignalProps = None
        self.iSignalType = None
        self.initValue = None
        self.length = None
        self.networkRepresentationProps = None
        self.systemSignalRef: Union[Union[RefType, None] , None] = None
        self.timeoutSubstitutionValue = None
        self.transformationISignalProps: List[Any] = []

    def getDataTransformationRef(self) -> Union[Any, None]:
        return self.dataTransformationRef

    def setDataTransformationRef(self, value: Union[Any, None]) -> "ISignal":
        self.dataTransformationRef = value
        return self

    def getDataTypePolicy(self) -> Union[Any, None]:
        return self.dataTypePolicy

    def setDataTypePolicy(self, value: Union[Any, None]) -> "ISignal":
        self.dataTypePolicy = value
        return self

    def getISignalProps(self) -> Union[Any, None]:
        return self.iSignalProps

    def setISignalProps(self, value: Union[Any, None]) -> "ISignal":
        self.iSignalProps = value
        return self

    def getISignalType(self) -> Union[Any, None]:
        return self.iSignalType

    def setISignalType(self, value: Union[Any, None]) -> "ISignal":
        self.iSignalType = value
        return self

    def getInitValue(self) -> Union[Any, None]:
        return self.initValue

    def setInitValue(self, value: Union[Any, None]) -> "ISignal":
        self.initValue = value
        return self

    def getLength(self) -> Union[Any, None]:
        return self.length

    def setLength(self, value: Union[Any, None]) -> "ISignal":
        self.length = value
        return self

    def getNetworkRepresentationProps(self) -> Union[Any, None]:
        return self.networkRepresentationProps

    def setNetworkRepresentationProps(self, value: Union[Any, None]) -> "ISignal":
        self.networkRepresentationProps = value
        return self

    def getSystemSignalRef(self) -> Union[Union[RefType, None], None]:
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Union[Union[RefType, None], None]) -> "ISignal":
        self.systemSignalRef = value
        return self

    def getTimeoutSubstitutionValue(self) -> Union[Any, None]:
        return self.timeoutSubstitutionValue

    def setTimeoutSubstitutionValue(self, value: Union[Any, None]) -> "ISignal":
        self.timeoutSubstitutionValue = value
        return self

    def getTransformationISignalProps(self) -> List[Any]:
        return self.transformationISignalProps

    def addTransformationISignalProps(self, value: Any) -> "ISignal":
        self.transformationISignalProps.append(value)
        return self


class PduTriggering(Identifiable):
    """
    Defines the triggering mechanism for Protocol Data Units (PDUs),
    specifying PDU references, port references, and trigger conditions
    for PDU transmission and reception.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.iPduRef: Union[Union[RefType, None] , None] = None
        self.iPduPortRefs: List[RefType] = []
        self.iSignalTriggeringRefs: List[RefType] = []
        self.secOcCryptoMappingRef: Union[Union[RefType, None] , None] = None
        self.triggerIPduSendConditions: List[Any] = []

    def getIPduRef(self) -> Union[Union[RefType, None], None]:
        return self.iPduRef

    def setIPduRef(self, value: Union[Union[RefType, None], None]) -> "PduTriggering":
        self.iPduRef = value
        return self

    def getIPduPortRefs(self) -> List[RefType]:
        return self.iPduPortRefs

    def addIPduPortRef(self, value: RefType) -> "PduTriggering":
        self.iPduPortRefs.append(value)
        return self

    def getISignalTriggeringRefs(self) -> List[RefType]:
        # return sorted(self.iSignalTriggeringRefs, key = lambda i: i.getShortValue())
        return self.iSignalTriggeringRefs

    def addISignalTriggeringRef(self, value: RefType) -> "PduTriggering":
        self.iSignalTriggeringRefs.append(value)
        return self

    def getSecOcCryptoMappingRef(self) -> Union[Union[RefType, None], None]:
        return self.secOcCryptoMappingRef

    def setSecOcCryptoMappingRef(self, value: Union[Union[RefType, None], None]) -> "PduTriggering":
        self.secOcCryptoMappingRef = value
        return self

    def getTriggerIPduSendConditions(self) -> List[Any]:
        return self.triggerIPduSendConditions

    def addTriggerIPduSendCondition(self, value: Any) -> "PduTriggering":
        self.triggerIPduSendConditions.append(value)
        return self


class FrameTriggering(Identifiable, ABC):
    """
    Abstract base class for frame triggering mechanisms, defining
    common properties for triggering frame transmission and reception
    including frame references and port references.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")

        super().__init__(parent, short_name)

        self.frameRef: Union[Union[RefType, None] , None] = None
        self.framePortRefs: List[RefType] = []
        self.pduTriggeringRefs: List[RefType] = []

    def getFrameRef(self) -> Union[Union[RefType, None], None]:
        return self.frameRef

    def setFrameRef(self, value: Union[Union[RefType, None], None]) -> "FrameTriggering":
        self.frameRef = value
        return self

    def getFramePortRefs(self) -> List[RefType]:
        return self.framePortRefs

    def addFramePortRef(self, value: RefType) -> "FrameTriggering":
        self.framePortRefs.append(value)
        return self

    def getPduTriggeringRefs(self) -> List[RefType]:
        return self.pduTriggeringRefs

    def addPduTriggeringRef(self, value: RefType) -> "FrameTriggering":
        self.pduTriggeringRefs.append(value)
        return self


class SystemSignal(ARElement):
    """
    Represents a system signal in the AUTOSAR system, defining
    dynamic length properties and physical properties for
    system-level signal communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.dynamicLength: Union[Union[ARBoolean, None] , None] = None
        self.physicalProps: Union[Union[SwDataDefProps, None] , None] = None

    def getDynamicLength(self) -> Union[Union[ARBoolean, None], None]:
        return self.dynamicLength

    def setDynamicLength(self, value: Union[Union[ARBoolean, None], None]) -> "SystemSignal":
        self.dynamicLength = value
        return self

    def getPhysicalProps(self) -> Union[Union[SwDataDefProps, None], None]:
        return self.physicalProps

    def setPhysicalProps(self, value: Union[Union[SwDataDefProps, None], None]) -> "SystemSignal":
        self.physicalProps = value
        return self


class SystemSignalGroup(ARElement):
    """
    Represents a group of system signals, defining relationships
    between individual system signals and transforming signal references
    for grouped signal communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.systemSignalRefs: List[RefType] = []
        self.transformingSystemSignalRef: Union[Union[RefType, None] , None] = None

    def getSystemSignalRefs(self) -> List[RefType]:
        return self.systemSignalRefs

    def addSystemSignalRefs(self, value: RefType) -> "SystemSignalGroup":
        self.systemSignalRefs.append(value)
        return self

    def getTransformingSystemSignalRef(self) -> Union[Union[RefType, None], None]:
        return self.transformingSystemSignalRef

    def setTransformingSystemSignalRef(self, value: Union[Union[RefType, None], None]) -> "SystemSignalGroup":
        self.transformingSystemSignalRef = value
        return self


class ISignalTriggering(Identifiable):
    """
    Defines triggering properties for interaction signals, specifying
    signal references, group references, and port references for
    signal-based communication triggering.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.iSignalRef: Union[Union[RefType, None] , None] = None
        self.iSignalGroupRef: Union[Union[RefType, None] , None] = None
        self.iSignalPortRefs: List[RefType] = []

    def getISignalRef(self) -> Union[Union[RefType, None], None]:
        return self.iSignalRef

    def setISignalRef(self, value: Union[Union[RefType, None], None]) -> "ISignalTriggering":
        self.iSignalRef = value
        return self

    def getISignalGroupRef(self) -> Union[Union[RefType, None], None]:
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value: Union[Union[RefType, None], None]) -> "ISignalTriggering":
        self.iSignalGroupRef = value
        return self

    def getISignalPortRefs(self) -> List[RefType]:
        return self.iSignalPortRefs

    def addISignalPortRef(self, value: RefType) -> "ISignalTriggering":
        self.iSignalPortRefs.append(value)
        return self


class SegmentPosition(ARObject):
    """
    Defines the position of a segment within a communication element,
    specifying byte order, length, and position properties for
    segmented communication.
    """

    def __init__(self) -> None:
        super().__init__()

        self.segmentByteOrder: Union[Union[ByteOrderEnum, None] , None] = None
        self.segmentLength: Union[Union[Integer, None] , None] = None
        self.segmentPosition: Union[Union[Integer, None] , None] = None

    def getSegmentByteOrder(self) -> Union[Union[ByteOrderEnum, None], None]:
        return self.segmentByteOrder

    def setSegmentByteOrder(self, value: Union[Union[ByteOrderEnum, None], None]) -> "SegmentPosition":
        if value is not None:
            self.segmentByteOrder = value
        return self

    def getSegmentLength(self) -> Union[Union[Integer, None], None]:
        return self.segmentLength

    def setSegmentLength(self, value: Union[Union[Integer, None], None]) -> "SegmentPosition":
        if value is not None:
            self.segmentLength = value
        return self

    def getSegmentPosition(self) -> Union[Union[Integer, None], None]:
        return self.segmentPosition

    def setSegmentPosition(self, value: Union[Union[Integer, None], None]) -> "SegmentPosition":
        if value is not None:
            self.segmentPosition = value
        return self


class MultiplexedPart(ARObject, ABC):
    """
    Abstract base class for multiplexed communication parts, defining
    common properties for dynamic and static multiplexed communication
    segments including segment positions.
    """
    def __init__(self) -> None:
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")

        super().__init__()

        self.segmentPositions: List[SegmentPosition] = []

    def getSegmentPositions(self) -> List[SegmentPosition]:
        return self.segmentPositions

    def addSegmentPosition(self, value: SegmentPosition) -> "MultiplexedPart":
        if value is not None:
            self.segmentPositions.append(value)
        return self


class StaticPart(MultiplexedPart):
    """
    Defines a static part of multiplexed communication, specifying
    Interaction Protocol Data Unit (IPDU) references for fixed
    segments in multiplexed communication.
    """
    def __init__(self) -> None:
        super().__init__()

        self.iPduRef: Union[RefType, None] = None

    def getIPduRef(self) -> Union[RefType, None]:
        return self.iPduRef

    def setIPduRef(self, value: Union[RefType, None]) -> "StaticPart":
        if value is not None:
            self.iPduRef = value
        return self


class DynamicPartAlternative(ARObject):
    """
    Defines an alternative for dynamic parts in multiplexed communication,
    specifying selector field codes, initial dynamic part properties,
    and Interaction Protocol Data Unit (IPDU) references.
    """

    def __init__(self) -> None:
        super().__init__()

        self.initialDynamicPart: Union[Boolean, None] = None
        self.iPduRef: Union[RefType, None] = None
        self.selectorFieldCode: Union[Integer, None] = None

    def getInitialDynamicPart(self) -> Union[Boolean, None]:
        return self.initialDynamicPart

    def setInitialDynamicPart(self, value: Union[Boolean, None]) -> "DynamicPartAlternative":
        if value is not None:
            self.initialDynamicPart = value
        return self

    def getIPduRef(self) -> Union[RefType, None]:
        return self.iPduRef

    def setIPduRef(self, value: Union[RefType, None]) -> "DynamicPartAlternative":
        if value is not None:
            self.iPduRef = value
        return self

    def getSelectorFieldCode(self) -> Union[Integer, None]:
        return self.selectorFieldCode

    def setSelectorFieldCode(self, value: Union[Integer, None]) -> "DynamicPartAlternative":
        if value is not None:
            self.selectorFieldCode = value
        return self


class DynamicPart(MultiplexedPart):
    """
    Defines a dynamic part of multiplexed communication, specifying
    alternatives for variable segments in multiplexed communication
    based on selector field values.
    """
    def __init__(self) -> None:
        super().__init__()

        self.dynamicPartAlternatives: List[DynamicPartAlternative] = []

    def getDynamicPartAlternatives(self) -> List[DynamicPartAlternative]:
        return self.dynamicPartAlternatives

    def addDynamicPartAlternative(self, value: DynamicPartAlternative) -> "DynamicPart":
        if value is not None:
            self.dynamicPartAlternatives.append(value)
        return self


class MultiplexedIPdu(IPdu):
    """
    Represents a multiplexed Interaction Protocol Data Unit (IPDU)
    with dynamic and static parts, defining selector field properties
    and trigger modes for multiplexed communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.dynamicPart: Union[DynamicPart, None] = None
        self.selectorFieldByteOrder: Union[ByteOrderEnum, None] = None
        self.selectorFieldLength: Union[Integer, None] = None
        self.selectorFieldStartPosition: Union[Integer, None] = None
        self.staticPart: Union[StaticPart, None] = None
        self.triggerMode: Union[TriggerMode, None] = None
        self.unusedBitPattern: Union[Integer, None] = None

    def getDynamicPart(self) -> Union[DynamicPart, None]:
        return self.dynamicPart

    def setDynamicPart(self, value: Union[DynamicPart, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.dynamicPart = value
        return self

    def getSelectorFieldByteOrder(self) -> Union[ByteOrderEnum, None]:
        return self.selectorFieldByteOrder

    def setSelectorFieldByteOrder(self, value: Union[ByteOrderEnum, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.selectorFieldByteOrder = value
        return self

    def getSelectorFieldLength(self) -> Union[Integer, None]:
        return self.selectorFieldLength

    def setSelectorFieldLength(self, value: Union[Integer, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.selectorFieldLength = value
        return self

    def getSelectorFieldStartPosition(self) -> Union[Integer, None]:
        return self.selectorFieldStartPosition

    def setSelectorFieldStartPosition(self, value: Union[Integer, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.selectorFieldStartPosition = value
        return self

    def getStaticPart(self) -> Union[StaticPart, None]:
        return self.staticPart

    def setStaticPart(self, value: Union[StaticPart, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.staticPart = value
        return self

    def getTriggerMode(self) -> Union["TriggerMode", None]:
        return self.triggerMode

    def setTriggerMode(self, value: Union["TriggerMode", None]) -> "MultiplexedIPdu":
        if value is not None:
            self.triggerMode = value
        return self

    def getUnusedBitPattern(self) -> Union[Integer, None]:
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Union[Integer, None]) -> "MultiplexedIPdu":
        if value is not None:
            self.unusedBitPattern = value
        return self


class GeneralPurposePdu(Pdu):
    """
    Represents a general-purpose Protocol Data Unit (PDU) for flexible
    communication patterns that don't fit into specific PDU categories.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class GeneralPurposeIPdu(IPdu):
    """
    Represents a general-purpose Interaction Protocol Data Unit (IPDU) for flexible
    interaction-based communication patterns that don't fit into specific IPDU categories.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class SecureCommunicationPropsSet(FibexElement):
    """
    Represents a set of secure communication properties that can be grouped
    together to define common security configurations for communication channels.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.secureComProps: List[SecureCommunicationProps] = []


class UserDefinedPdu(Pdu):
    """
    Represents a user-defined Protocol Data Unit (PDU) that allows for custom
    communication patterns defined by the user rather than following standard PDU types.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class UserDefinedIPdu(IPdu):
    """
    Represents a user-defined Interaction Protocol Data Unit (IPDU) that allows for custom
    interaction-based communication patterns defined by the user rather than following standard IPDU types.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Defines authentication properties for secure communication,
    including authentication build attempts, retries, and other
    authentication-related security parameters.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.authenticationBuildAttempts: Union[Union[PositiveInteger, None] , None] = None
        self.authenticationRetries: Union[Union[PositiveInteger, None] , None] = None
        self.dataId: Union[Union[PositiveInteger, None] , None] = None
        self.securedComAuthenticationType: Union[Union[ARLiteral, None] , None] = None

    def getAuthenticationBuildAttempts(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationAuthProps":
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self) -> Union[Union[PositiveInteger, None], None]:
        return self.authenticationRetries

    def setAuthenticationRetries(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationAuthProps":
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.dataId

    def setDataId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationAuthProps":
        if value is not None:
            self.dataId = value
        return self

    def getSecuredComAuthenticationType(self) -> Union[Union[ARLiteral, None], None]:
        return self.securedComAuthenticationType

    def setSecuredComAuthenticationType(self, value: Union[Union[ARLiteral, None], None]) -> "SecureCommunicationAuthProps":
        if value is not None:
            self.securedComAuthenticationType = value
        return self


class SecureCommunicationFreshnessProps(Identifiable):
    """
    Defines freshness properties for secure communication,
    including freshness value IDs, lengths, and other
    freshness-related security parameters to prevent replay attacks.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.freshnessValueId: Union[Union[PositiveInteger, None] , None] = None
        self.freshnessValueLength: Union[Union[PositiveInteger, None] , None] = None
        self.freshnessValueTxLength: Union[Union[PositiveInteger, None] , None] = None
        self.messageLinkLength: Union[Union[PositiveInteger, None] , None] = None
        self.messageLinkPosition: Union[Union[PositiveInteger, None] , None] = None
        self.secondaryFreshnessValueId: Union[Union[PositiveInteger, None] , None] = None
        self.securedComFreshnessType: Union[Union[ARLiteral, None] , None] = None

    def getFreshnessValueId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueId

    def setFreshnessValueId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.freshnessValueId = value
        return self

    def getFreshnessValueLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getMessageLinkLength(self) -> Union[Union[PositiveInteger, None], None]:
        return self.messageLinkLength

    def setMessageLinkLength(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self) -> Union[Union[PositiveInteger, None], None]:
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self) -> Union[Union[PositiveInteger, None], None]:
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value: Union[Union[PositiveInteger, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredComFreshnessType(self) -> Union[Union[ARLiteral, None], None]:
        return self.securedComFreshnessType

    def setSecuredComFreshnessType(self, value: Union[Union[ARLiteral, None], None]) -> "SecureCommunicationFreshnessProps":
        if value is not None:
            self.securedComFreshnessType = value
        return self


__all__ = []


class TriggerMode(AREnum):
    """Enumeration for trigger modes."""
    NONE = "NONE"
    ALWAYS = "ALWAYS"
    ON_CHANGE = "ON-CHANGE"
    def __init__(self) -> None:
        super().__init__([
            TriggerMode.NONE,
            TriggerMode.ALWAYS,
            TriggerMode.ON_CHANGE
        ])

