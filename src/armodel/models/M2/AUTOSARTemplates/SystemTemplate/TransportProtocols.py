# This module contains AUTOSAR System Template classes for transport protocols
# It defines CAN, DoIP, and LIN transport protocol configurations and connections

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIp import AbstractDoIpLogicAddressProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger, RefType, TimeValue, ARLiteral
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TpConfig(FibexElement, ABC):
    """
    Contains all configuration elements for AUTOSAR TP.
    """

    # TpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.237, p.588
    # Spec verified: R23-11
    # Note: class Note taken from XSD TP-CONFIG group documentation (PDF table has no Note row)
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCommunicationClusterRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCommunicationClusterRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TpConfig:
            raise TypeError("TpConfig is an abstract class.")

        super().__init__(parent, short_name)

        # A TpConfig is existing always in the context of exactly one CommunicationCluster.
        self.communicationClusterRef: Optional[RefType] = None

    def getCommunicationClusterRef(self) -> Optional[RefType]:
        """
        A TpConfig is existing always in the context of exactly one CommunicationCluster.
        """
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value: Optional[RefType]) -> "TpConfig":
        """
        A TpConfig is existing always in the context of exactly one CommunicationCluster.
        A None value is a no-op and does not overwrite an existing communicationClusterRef.
        """
        if value is not None:
            self.communicationClusterRef = value
        return self


class CanTpAddress(Identifiable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic Address.
    """

    # CanTpAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.255, p.610
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTpAddress                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpAddress                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpAddressExtensionValue   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpAddressExtensionValue   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # An ECUs TP address on the referenced channel. This represents the diagnostic Address.
        self.tpAddress: Optional[Integer] = None

        # If the mixed addressing format is used, this parameter contains the transport protocol address extension value.
        self.tpAddressExtensionValue: Optional[Integer] = None

    def getTpAddress(self) -> Optional[Integer]:
        """An ECUs TP address on the referenced channel. This represents the diagnostic Address."""
        return self.tpAddress

    def setTpAddress(self, value: Optional[Integer]) -> "CanTpAddress":
        """
        An ECUs TP address on the referenced channel. This represents the diagnostic Address.
        A None value is a no-op and does not overwrite an existing tpAddress.
        """
        if value is not None:
            self.tpAddress = value
        return self

    def getTpAddressExtensionValue(self) -> Optional[Integer]:
        """If the mixed addressing format is used, this parameter contains the transport protocol address extension value."""
        return self.tpAddressExtensionValue

    def setTpAddressExtensionValue(self, value: Optional[Integer]) -> "CanTpAddress":
        """
        If the mixed addressing format is used, this parameter contains the transport protocol address extension value.
        A None value is a no-op and does not overwrite an existing tpAddressExtensionValue.
        """
        if value is not None:
            self.tpAddressExtensionValue = value
        return self


class CanTpChannel(Identifiable):
    """
    Configuration parameters of the CanTp channel.
    """

    # CanTpChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.252, p.608
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getChannelId    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setChannelId    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The id of the channel. The value shall be unique for each channel.
        self.channelId: Optional[PositiveInteger] = None

    def getChannelId(self) -> Optional[PositiveInteger]:
        """The id of the channel. The value shall be unique for each channel."""
        return self.channelId

    def setChannelId(self, value: Optional[PositiveInteger]) -> "CanTpChannel":
        """
        The id of the channel. The value shall be unique for each channel.
        A None value is a no-op and does not overwrite an existing channelId.
        """
        if value is not None:
            self.channelId = value
        return self


class CanTpAddressingFormatType(AREnum):
    """Declares which communication addressing mode is supported."""

    # CanTpAddressingFormatType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.254, p.610
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    # To use extended addressing format. Tags: atp.EnumerationLiteralIndex=0
    ENUM_EXTENDED = "EXTENDED"

    # To use mixed 11bit addressing format. Tags: atp.EnumerationLiteralIndex=1
    ENUM_MIXED = "MIXED"

    # To use mixed 29bit addressing format Tags: atp.EnumerationLiteralIndex=2
    ENUM_MIXED_29BIT = "MIXED-29-BIT"

    # To use normal fixed addressing format Tags: atp.EnumerationLiteralIndex=3
    ENUM_NORMALFIXED = "NORMALFIXED"

    # To use normal addressing format. Tags: atp.EnumerationLiteralIndex=4
    ENUM_STANDARD = "STANDARD"

    def __init__(self):
        super().__init__(
            [
                CanTpAddressingFormatType.ENUM_EXTENDED,
                CanTpAddressingFormatType.ENUM_MIXED,
                CanTpAddressingFormatType.ENUM_MIXED_29BIT,
                CanTpAddressingFormatType.ENUM_NORMALFIXED,
                CanTpAddressingFormatType.ENUM_STANDARD,
            ]
        )


class NetworkTargetAddressType(AREnum):
    """Network Target Address type (see ISO 15765-2)."""

    # NetworkTargetAddressType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.258, p.611
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    # Functional request type Tags: atp.EnumerationLiteralIndex=0
    ENUM_FUNCTIONAL = "FUNCTIONAL"

    # Physical request type Tags: atp.EnumerationLiteralIndex=2
    ENUM_PHYSICAL = "PHYSICAL"

    def __init__(self):
        super().__init__(
            [
                NetworkTargetAddressType.ENUM_FUNCTIONAL,
                NetworkTargetAddressType.ENUM_PHYSICAL,
            ]
        )


class CanTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular communication. The CanTp module routes a Pdu
    through this connection. atpVariation: Derived, because TpNode can vary.
    """

    # CanTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.253 (with Table 6.252 block), p.608-609
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAddressingFormat       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAddressingFormat       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCancellation           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCancellation           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanTpChannelRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanTpChannelRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataPduRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataPduRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFlowControlPduRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFlowControlPduRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxBlockSize           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxBlockSize           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMulticastRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMulticastRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPaddingActivation      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPaddingActivation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReceiverRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addReceiverRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTaType                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTaType                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutBr              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutBr              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutBs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutBs              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutCr              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutCr              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutCs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutCs              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpSduRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpSduRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransmitterRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransmitterRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Declares which communication addressing mode is supported.
        self.addressingFormat: Optional[CanTpAddressingFormatType] = None

        # With this switch Tx Cancellation can be turned on or off. Please note that the Rx Cancellation is always enabled.
        self.cancellation: Optional[Boolean] = None

        # Reference to the CanTpChannel on which this CanTp Connection is realized.
        self.canTpChannelRef: Optional[RefType] = None

        # Reference to an Data NPdu.
        self.dataPduRef: Optional[RefType] = None

        # Reference to the Flow Control NPdu.
        self.flowControlPduRef: Optional[RefType] = None

        # The maximum number of N-PDUs the CanTp receiver allows the sender to send, before waiting for an authorization to continue transmission of the following N-PDUs. For further details on this parameter value see ISO 15765-2 specification. Note: For reasons of buffer length, the CAN Transport Layer can adapt the BS value within the limit of this maximum BS
        self.maxBlockSize: Optional[Integer] = None

        # TP address for 1:n connections.
        self.multicastRef: Optional[RefType] = None

        # This specifies whether or not Sfs, FCs and the last CF shall be padded to 8 bytes length in case it contains less payload. true: The N-PDU received uses padding for SF, FC and the last CF. (N-PDU length is always 8 bytes) false: The N-PDU received does not use padding for SF, CF and the last CF. (N-PDU length is dynamic)
        self.paddingActivation: Optional[Boolean] = None

        # The target of the TP connection.
        self.receiverRefs: List[RefType] = []

        # Network Target Address type.
        self.taType: Optional[ARLiteral] = None

        # Value in seconds of the performance requirement for (N_ Br + N_Ar). N_Br is the elapsed time between the receiving indication of a FF or CF or the transmit confirmation of a FC, until the transmit request of the next FC.
        self.timeoutBr: Optional[TimeValue] = None

        # This parameter defines the timeout for waiting for an FC or AF on the sender side in an 1:1 connection. Specified in seconds.
        self.timeoutBs: Optional[TimeValue] = None

        # This parameter defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        self.timeoutCr: Optional[TimeValue] = None

        # The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU.
        self.timeoutCs: Optional[TimeValue] = None

        # Reference to an IPdu that is segmented by the Transport Protocol.
        self.tpSduRef: Optional[RefType] = None

        # The source of the TP connection.
        self.transmitterRef: Optional[RefType] = None

    def getAddressingFormat(self) -> Optional[CanTpAddressingFormatType]:
        """Declares which communication addressing mode is supported."""
        return self.addressingFormat

    def setAddressingFormat(self, value: Optional[CanTpAddressingFormatType]) -> "CanTpConnection":
        """
        Declares which communication addressing mode is supported.
        A None value is a no-op and does not overwrite an existing addressingFormat.
        """
        if value is not None:
            self.addressingFormat = value
        return self

    def getCancellation(self) -> Optional[Boolean]:
        """With this switch Tx Cancellation can be turned on or off. Please note that the Rx Cancellation is always enabled."""
        return self.cancellation

    def setCancellation(self, value: Optional[Boolean]) -> "CanTpConnection":
        """
        With this switch Tx Cancellation can be turned on or off. Please note that the Rx Cancellation is always enabled.
        A None value is a no-op and does not overwrite an existing cancellation.
        """
        if value is not None:
            self.cancellation = value
        return self

    def getCanTpChannelRef(self) -> Optional[RefType]:
        """Reference to the CanTpChannel on which this CanTp Connection is realized."""
        return self.canTpChannelRef

    def setCanTpChannelRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        Reference to the CanTpChannel on which this CanTp Connection is realized.
        A None value is a no-op and does not overwrite an existing canTpChannelRef.
        """
        if value is not None:
            self.canTpChannelRef = value
        return self

    def getDataPduRef(self) -> Optional[RefType]:
        """Reference to an Data NPdu."""
        return self.dataPduRef

    def setDataPduRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        Reference to an Data NPdu.
        A None value is a no-op and does not overwrite an existing dataPduRef.
        """
        if value is not None:
            self.dataPduRef = value
        return self

    def getFlowControlPduRef(self) -> Optional[RefType]:
        """Reference to the Flow Control NPdu."""
        return self.flowControlPduRef

    def setFlowControlPduRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        Reference to the Flow Control NPdu.
        A None value is a no-op and does not overwrite an existing flowControlPduRef.
        """
        if value is not None:
            self.flowControlPduRef = value
        return self

    def getMaxBlockSize(self) -> Optional[Integer]:
        """The maximum number of N-PDUs the CanTp receiver allows the sender to send, before waiting for an authorization to continue transmission of the following N-PDUs. For further details on this parameter value see ISO 15765-2 specification. Note: For reasons of buffer length, the CAN Transport Layer can adapt the BS value within the limit of this maximum BS"""
        return self.maxBlockSize

    def setMaxBlockSize(self, value: Optional[Integer]) -> "CanTpConnection":
        """
        The maximum number of N-PDUs the CanTp receiver allows the sender to send, before waiting for an authorization to continue transmission of the following N-PDUs. For further details on this parameter value see ISO 15765-2 specification. Note: For reasons of buffer length, the CAN Transport Layer can adapt the BS value within the limit of this maximum BS
        A None value is a no-op and does not overwrite an existing maxBlockSize.
        """
        if value is not None:
            self.maxBlockSize = value
        return self

    def getMulticastRef(self) -> Optional[RefType]:
        """TP address for 1:n connections."""
        return self.multicastRef

    def setMulticastRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        TP address for 1:n connections.
        A None value is a no-op and does not overwrite an existing multicastRef.
        """
        if value is not None:
            self.multicastRef = value
        return self

    def getPaddingActivation(self) -> Optional[Boolean]:
        """This specifies whether or not Sfs, FCs and the last CF shall be padded to 8 bytes length in case it contains less payload. true: The N-PDU received uses padding for SF, FC and the last CF. (N-PDU length is always 8 bytes) false: The N-PDU received does not use padding for SF, CF and the last CF. (N-PDU length is dynamic)"""
        return self.paddingActivation

    def setPaddingActivation(self, value: Optional[Boolean]) -> "CanTpConnection":
        """
        This specifies whether or not Sfs, FCs and the last CF shall be padded to 8 bytes length in case it contains less payload. true: The N-PDU received uses padding for SF, FC and the last CF. (N-PDU length is always 8 bytes) false: The N-PDU received does not use padding for SF, CF and the last CF. (N-PDU length is dynamic)
        A None value is a no-op and does not overwrite an existing paddingActivation.
        """
        if value is not None:
            self.paddingActivation = value
        return self

    def getReceiverRefs(self) -> List[RefType]:
        """The target of the TP connection."""
        return self.receiverRefs

    def addReceiverRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        The target of the TP connection.
        A None value is a no-op and is not appended to receiverRefs.
        """
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getTaType(self) -> Optional[ARLiteral]:
        """Network Target Address type."""
        return self.taType

    def setTaType(self, value: Optional[ARLiteral]) -> "CanTpConnection":
        """
        Network Target Address type.
        A None value is a no-op and does not overwrite an existing taType.
        """
        if value is not None:
            self.taType = value
        return self

    def getTimeoutBr(self) -> Optional[TimeValue]:
        """Value in seconds of the performance requirement for (N_ Br + N_Ar). N_Br is the elapsed time between the receiving indication of a FF or CF or the transmit confirmation of a FC, until the transmit request of the next FC."""
        return self.timeoutBr

    def setTimeoutBr(self, value: Optional[TimeValue]) -> "CanTpConnection":
        """
        Value in seconds of the performance requirement for (N_ Br + N_Ar). N_Br is the elapsed time between the receiving indication of a FF or CF or the transmit confirmation of a FC, until the transmit request of the next FC.
        A None value is a no-op and does not overwrite an existing timeoutBr.
        """
        if value is not None:
            self.timeoutBr = value
        return self

    def getTimeoutBs(self) -> Optional[TimeValue]:
        """This parameter defines the timeout for waiting for an FC or AF on the sender side in an 1:1 connection. Specified in seconds."""
        return self.timeoutBs

    def setTimeoutBs(self, value: Optional[TimeValue]) -> "CanTpConnection":
        """
        This parameter defines the timeout for waiting for an FC or AF on the sender side in an 1:1 connection. Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutBs.
        """
        if value is not None:
            self.timeoutBs = value
        return self

    def getTimeoutCr(self) -> Optional[TimeValue]:
        """This parameter defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds."""
        return self.timeoutCr

    def setTimeoutCr(self, value: Optional[TimeValue]) -> "CanTpConnection":
        """
        This parameter defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutCr.
        """
        if value is not None:
            self.timeoutCr = value
        return self

    def getTimeoutCs(self) -> Optional[TimeValue]:
        """The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU."""
        return self.timeoutCs

    def setTimeoutCs(self, value: Optional[TimeValue]) -> "CanTpConnection":
        """
        The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU.
        A None value is a no-op and does not overwrite an existing timeoutCs.
        """
        if value is not None:
            self.timeoutCs = value
        return self

    def getTpSduRef(self) -> Optional[RefType]:
        """Reference to an IPdu that is segmented by the Transport Protocol."""
        return self.tpSduRef

    def setTpSduRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        Reference to an IPdu that is segmented by the Transport Protocol.
        A None value is a no-op and does not overwrite an existing tpSduRef.
        """
        if value is not None:
            self.tpSduRef = value
        return self

    def getTransmitterRef(self) -> Optional[RefType]:
        """The source of the TP connection."""
        return self.transmitterRef

    def setTransmitterRef(self, value: Optional[RefType]) -> "CanTpConnection":
        """
        The source of the TP connection.
        A None value is a no-op and does not overwrite an existing transmitterRef.
        """
        if value is not None:
            self.transmitterRef = value
        return self


class CanTpEcu(ARObject):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference to exactly one ECUInstance in the topology.
    """

    # CanTpEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.256, p.610
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCycleTimeMainFunction    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCycleTimeMainFunction    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEcuInstanceRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEcuInstanceRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds.
        self.cycleTimeMainFunction: Optional[TimeValue] = None

        # Connection to the ECUInstance in the Topology
        self.ecuInstanceRef: Optional[RefType] = None

    def getCycleTimeMainFunction(self) -> Optional[TimeValue]:
        """The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds."""
        return self.cycleTimeMainFunction

    def setCycleTimeMainFunction(self, value: Optional[TimeValue]) -> "CanTpEcu":
        """
        The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds.
        A None value is a no-op and does not overwrite an existing cycleTimeMainFunction.
        """
        if value is not None:
            self.cycleTimeMainFunction = value
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """Connection to the ECUInstance in the Topology"""
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> "CanTpEcu":
        """
        Connection to the ECUInstance in the Topology
        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self


class CanTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to the Topology description.
    """

    # CanTpNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.257, p.611
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConnectorRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConnectorRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxFcWait       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxFcWait       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStMin           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStMin           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutAr       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutAr       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutAs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutAs       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpAddressRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpAddressRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided).
        self.connectorRef: Optional[RefType] = None

        # This attribute defines the maximum number of flow control PDUs that can be consecutively be transmitted by a receiver.
        self.maxFcWait: Optional[Integer] = None

        # Sets the duration of the minimum time the CanTp sender shall wait between the transmissions of two CF N-PDUs.
        self.stMin: Optional[TimeValue] = None

        # This attribute states the timeout between the PDU transmit request of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface on the receiver side (for FC or AF). Specified in seconds.
        self.timeoutAr: Optional[TimeValue] = None

        # This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds.
        self.timeoutAs: Optional[TimeValue] = None

        # Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        self.tpAddressRef: Optional[RefType] = None

    def getConnectorRef(self) -> Optional[RefType]:
        """Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided)."""
        return self.connectorRef

    def setConnectorRef(self, value: Optional[RefType]) -> "CanTpNode":
        """
        Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided).
        A None value is a no-op and does not overwrite an existing connectorRef.
        """
        if value is not None:
            self.connectorRef = value
        return self

    def getMaxFcWait(self) -> Optional[Integer]:
        """This attribute defines the maximum number of flow control PDUs that can be consecutively be transmitted by a receiver."""
        return self.maxFcWait

    def setMaxFcWait(self, value: Optional[Integer]) -> "CanTpNode":
        """
        This attribute defines the maximum number of flow control PDUs that can be consecutively be transmitted by a receiver.
        A None value is a no-op and does not overwrite an existing maxFcWait.
        """
        if value is not None:
            self.maxFcWait = value
        return self

    def getStMin(self) -> Optional[TimeValue]:
        """Sets the duration of the minimum time the CanTp sender shall wait between the transmissions of two CF N-PDUs."""
        return self.stMin

    def setStMin(self, value: Optional[TimeValue]) -> "CanTpNode":
        """
        Sets the duration of the minimum time the CanTp sender shall wait between the transmissions of two CF N-PDUs.
        A None value is a no-op and does not overwrite an existing stMin.
        """
        if value is not None:
            self.stMin = value
        return self

    def getTimeoutAr(self) -> Optional[TimeValue]:
        """This attribute states the timeout between the PDU transmit request of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface on the receiver side (for FC or AF). Specified in seconds."""
        return self.timeoutAr

    def setTimeoutAr(self, value: Optional[TimeValue]) -> "CanTpNode":
        """
        This attribute states the timeout between the PDU transmit request of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface on the receiver side (for FC or AF). Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutAr.
        """
        if value is not None:
            self.timeoutAr = value
        return self

    def getTimeoutAs(self) -> Optional[TimeValue]:
        """This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds."""
        return self.timeoutAs

    def setTimeoutAs(self, value: Optional[TimeValue]) -> "CanTpNode":
        """
        This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the Can Interface and the corresponding confirmation of the Can Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutAs.
        """
        if value is not None:
            self.timeoutAs = value
        return self

    def getTpAddressRef(self) -> Optional[RefType]:
        """Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection)."""
        return self.tpAddressRef

    def setTpAddressRef(self, value: Optional[RefType]) -> "CanTpNode":
        """
        Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        A None value is a no-op and does not overwrite an existing tpAddressRef.
        """
        if value is not None:
            self.tpAddressRef = value
        return self


class CanTpConfig(TpConfig):
    """
    This element defines exactly one CAN TP Configuration. One CanTpConfig element shall be created for each CAN Network in the System.
    """

    # CanTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.251, p.607
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTpAddresses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCanTpAddress      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpChannels           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCanTpChannel      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpConnections        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTpConnection         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpEcus               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTpEcu                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpNodes              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCanTpNode         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of TP Addresses.
        self.tpAddresses: List[CanTpAddress] = []

        # Configuration of CAN TP channels.
        self.tpChannels: List[CanTpChannel] = []

        # Senders and receivers of CAN TP messages.
        self.tpConnections: List[CanTpConnection] = []

        # Collection of TP Ecus
        self.tpEcus: List[CanTpEcu] = []

        # Senders and receivers of Can TP messages.
        self.tpNodes: List[CanTpNode] = []

    def getTpAddresses(self) -> List[CanTpAddress]:
        """Collection of TP Addresses."""
        return self.tpAddresses

    def createCanTpAddress(self, short_name: str) -> CanTpAddress:
        """Collection of TP Addresses."""
        if not self.IsElementExists(short_name):
            address = CanTpAddress(self, short_name)
            self.addElement(address)
            self.tpAddresses.append(address)
        return self.getElement(short_name)

    def getTpChannels(self) -> List[CanTpChannel]:
        """Configuration of CAN TP channels."""
        return self.tpChannels

    def createCanTpChannel(self, short_name: str) -> CanTpChannel:
        """Configuration of CAN TP channels."""
        if not self.IsElementExists(short_name):
            channel = CanTpChannel(self, short_name)
            self.addElement(channel)
            self.tpChannels.append(channel)
        return self.getElement(short_name)

    def getTpConnections(self) -> List[CanTpConnection]:
        """Senders and receivers of CAN TP messages."""
        return self.tpConnections

    def addTpConnection(self, value: Optional[CanTpConnection]) -> "CanTpConfig":
        """
        Senders and receivers of CAN TP messages.
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpEcus(self) -> List[CanTpEcu]:
        """Collection of TP Ecus"""
        return self.tpEcus

    def addTpEcu(self, value: Optional[CanTpEcu]) -> "CanTpConfig":
        """
        Collection of TP Ecus
        A None value is a no-op and is not appended to tpEcus.
        """
        if value is not None:
            self.tpEcus.append(value)
        return self

    def getTpNodes(self) -> List[CanTpNode]:
        """Senders and receivers of Can TP messages."""
        return self.tpNodes

    def createCanTpNode(self, short_name: str) -> CanTpNode:
        """Senders and receivers of Can TP messages."""
        if not self.IsElementExists(short_name):
            node = CanTpNode(self, short_name)
            self.addElement(node)
            self.tpNodes.append(node)
        return self.getElement(short_name)


class DoIpLogicAddress(Identifiable):
    """
    Represents a DoIP (Diagnostics over IP) logic address in the system,
    defining the address value and logic address properties for
    DoIP communication endpoints.
    """

    # DoIpLogicAddress method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAddress                   [x] impl  [ ] docstring  [ ] test
    # [ ] setAddress                   [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpLogicAddressProps     [x] impl  [ ] docstring  [ ] test
    # [ ] setDoIpLogicAddressProps     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.address: Integer = None
        self.doIpLogicAddressProps: AbstractDoIpLogicAddressProps = None

    def getAddress(self):
        return self.address

    def setAddress(self, value):
        if value is not None:
            self.address = value
        return self

    def getDoIpLogicAddressProps(self):
        return self.doIpLogicAddressProps

    def setDoIpLogicAddressProps(self, value):
        if value is not None:
            self.doIpLogicAddressProps = value
        return self


class DoIpTpConnection(TpConnection):
    """
    Represents a DoIP transport protocol connection in the system,
    defining source and target address references and SDU
    references for DoIP communication.
    """

    # DoIpTpConnection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpSourceAddressRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setDoIpSourceAddressRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpTargetAddressRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setDoIpTargetAddressRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getTpSduRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] setTpSduRef                  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.doIpSourceAddressRef: RefType = None
        self.doIpTargetAddressRef: RefType = None
        self.tpSduRef: RefType = None

    def getDoIpSourceAddressRef(self):
        return self.doIpSourceAddressRef

    def setDoIpSourceAddressRef(self, value):
        if value is not None:
            self.doIpSourceAddressRef = value
        return self

    def getDoIpTargetAddressRef(self):
        return self.doIpTargetAddressRef

    def setDoIpTargetAddressRef(self, value):
        if value is not None:
            self.doIpTargetAddressRef = value
        return self

    def getTpSduRef(self):
        return self.tpSduRef

    def setTpSduRef(self, value):
        if value is not None:
            self.tpSduRef = value
        return self


class DoIpTpConfig(TpConfig):
    """
    Represents DoIP transport protocol configuration in the system,
    organizing logic addresses and connections for comprehensive
    DoIP communication setup.
    """

    # DoIpTpConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpLogicAddresses        [x] impl  [ ] docstring  [ ] test
    # [ ] createDoIpLogicAddress       [x] impl  [ ] docstring  [ ] test
    # [ ] getTpConnections             [x] impl  [ ] docstring  [ ] test
    # [ ] addTpConnection              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.doIpLogicAddresses: List[DoIpLogicAddress] = []
        self.tpConnections: List[DoIpTpConnection] = []

    def getDoIpLogicAddresses(self):
        return self.doIpLogicAddresses

    def createDoIpLogicAddress(self, short_name: str):
        if not self.IsElementExists(short_name):
            address = DoIpLogicAddress(self, short_name)
            self.addElement(address)
            self.doIpLogicAddresses.append(address)
        return self.getElement(short_name)

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self


class TpAddress(Identifiable):
    """
    Represents a generic transport protocol address in the system,
    defining the transport address value for communication endpoints.
    """

    # TpAddress method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTpAddress                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTpAddress                 [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.tpAddress: Integer = None

    def getTpAddress(self):
        return self.tpAddress

    def setTpAddress(self, value):
        if value is not None:
            self.tpAddress = value
        return self


class LinTpConnection(TpConnection):
    """
    Represents a LIN transport protocol connection in the system,
    defining PDU references, timeout parameters, and transmitter/
    receiver configurations for LIN TP communication.
    """

    # LinTpConnection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataPduRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataPduRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getFlowControlRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setFlowControlRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getLinTpNSduRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setLinTpNSduRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getMulticastRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setMulticastRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getReceiverRefs              [x] impl  [ ] docstring  [ ] test
    # [ ] addReceiverRef               [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeoutAs                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeoutAs                 [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeoutCr                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeoutCr                 [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeoutCs                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeoutCs                 [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmitterRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setTransmitterRef            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.dataPduRef: RefType = None
        self.flowControlRef: RefType = None
        self.linTpNSduRef: RefType = None
        self.multicastRef: RefType = None
        self.receiverRefs: List[RefType] = []
        self.timeoutAs: TimeValue = None
        self.timeoutCr: TimeValue = None
        self.timeoutCs: TimeValue = None
        self.transmitterRef: RefType = None

    def getDataPduRef(self):
        return self.dataPduRef

    def setDataPduRef(self, value):
        if value is not None:
            self.dataPduRef = value
        return self

    def getFlowControlRef(self):
        return self.flowControlRef

    def setFlowControlRef(self, value):
        if value is not None:
            self.flowControlRef = value
        return self

    def getLinTpNSduRef(self):
        return self.linTpNSduRef

    def setLinTpNSduRef(self, value):
        if value is not None:
            self.linTpNSduRef = value
        return self

    def getMulticastRef(self):
        return self.multicastRef

    def setMulticastRef(self, value):
        if value is not None:
            self.multicastRef = value
        return self

    def getReceiverRefs(self):
        return self.receiverRefs

    def addReceiverRef(self, value):
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getTimeoutAs(self):
        return self.timeoutAs

    def setTimeoutAs(self, value):
        if value is not None:
            self.timeoutAs = value
        return self

    def getTimeoutCr(self):
        return self.timeoutCr

    def setTimeoutCr(self, value):
        if value is not None:
            self.timeoutCr = value
        return self

    def getTimeoutCs(self):
        return self.timeoutCs

    def setTimeoutCs(self, value):
        if value is not None:
            self.timeoutCs = value
        return self

    def getTransmitterRef(self):
        return self.transmitterRef

    def setTransmitterRef(self, value):
        if value is not None:
            self.transmitterRef = value
        return self


class LinTpNode(Identifiable):
    """
    Represents a LIN transport protocol node in the system,
    defining connector references, response pending settings,
    and timing parameters for LIN TP node configuration.
    """

    # LinTpNode method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getConnectorRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setConnectorRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getDropNotRequestedNad       [x] impl  [ ] docstring  [ ] test
    # [ ] setDropNotRequestedNad       [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxNumberOfRespPendingFrames [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxNumberOfRespPendingFrames [x] impl  [ ] docstring  [ ] test
    # [ ] getP2Max                     [x] impl  [ ] docstring  [ ] test
    # [ ] setP2Max                     [x] impl  [ ] docstring  [ ] test
    # [ ] getP2Timing                  [x] impl  [ ] docstring  [ ] test
    # [ ] setP2Timing                  [x] impl  [ ] docstring  [ ] test
    # [ ] getTpAddressRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setTpAddressRef              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.connectorRef: RefType = None
        self.dropNotRequestedNad: Boolean = None
        self.maxNumberOfRespPendingFrames: Integer = None
        self.p2Max: TimeValue = None
        self.p2Timing: TimeValue = None
        self.tpAddressRef: RefType = None

    def getConnectorRef(self):
        return self.connectorRef

    def setConnectorRef(self, value):
        if value is not None:
            self.connectorRef = value
        return self

    def getDropNotRequestedNad(self):
        return self.dropNotRequestedNad

    def setDropNotRequestedNad(self, value):
        if value is not None:
            self.dropNotRequestedNad = value
        return self

    def getMaxNumberOfRespPendingFrames(self):
        return self.maxNumberOfRespPendingFrames

    def setMaxNumberOfRespPendingFrames(self, value):
        if value is not None:
            self.maxNumberOfRespPendingFrames = value
        return self

    def getP2Max(self):
        return self.p2Max

    def setP2Max(self, value):
        if value is not None:
            self.p2Max = value
        return self

    def getP2Timing(self):
        return self.p2Timing

    def setP2Timing(self, value):
        if value is not None:
            self.p2Timing = value
        return self

    def getTpAddressRef(self):
        return self.tpAddressRef

    def setTpAddressRef(self, value):
        if value is not None:
            self.tpAddressRef = value
        return self


class LinTpConfig(TpConfig):
    """
    Represents LIN transport protocol configuration in the system,
    organizing addresses, connections, and nodes for comprehensive
    LIN TP communication setup.
    """

    # LinTpConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTpAddresses               [x] impl  [ ] docstring  [ ] test
    # [ ] createTpAddress              [x] impl  [ ] docstring  [ ] test
    # [ ] getTpConnections             [x] impl  [ ] docstring  [ ] test
    # [ ] addTpConnection              [x] impl  [ ] docstring  [ ] test
    # [ ] getTpNodes                   [x] impl  [ ] docstring  [ ] test
    # [ ] createLinTpNode              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.tpAddresses: List[TpAddress] = []
        self.tpConnections: List[LinTpConnection] = []
        self.tpNodes: List[LinTpNode] = []

    def getTpAddresses(self):
        return self.tpAddresses

    def createTpAddress(self, short_name: str):
        if not self.IsElementExists(short_name):
            address = TpAddress(self, short_name)
            self.addElement(address)
            self.tpAddresses.append(address)
        return self.getElement(short_name)

    def getTpConnections(self):
        return self.tpConnections

    def addTpConnection(self, value):
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpNodes(self):
        return self.tpNodes

    def createLinTpNode(self, short_name: str):
        if not self.IsElementExists(short_name):
            address = LinTpNode(self, short_name)
            self.addElement(address)
            self.tpNodes.append(address)
        return self.getElement(short_name)
