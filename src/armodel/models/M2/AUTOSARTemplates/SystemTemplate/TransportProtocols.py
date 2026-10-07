# This module contains AUTOSAR System Template classes for transport protocols
# It defines CAN, DoIP, and LIN transport protocol configurations and connections

from __future__ import annotations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import AbstractDoIpLogicAddressProps, DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    FlexrayArTpNode,
    FlexrayTpNode,
    FlexrayTpPduPool,
    Identifiable,
    SomeipTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject, FlexrayArTpChannel, FlexrayTpEcu, SomeipTpConnection


class TpConfig(FibexElement, ABC):
    """
    Contains all configuration elements for AUTOSAR TP.

    [constr_9226] Existence of TpConfig.communicationCluster: For each TpConfig, the reference to CommunicationCluster in the role communicationCluster shall exist at the time when the System Description is complete.
    """

    # TpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.237, p.588
    # Note: class Note taken from XSD TP-CONFIG group documentation (PDF table has no Note row)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationClusterRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationClusterRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

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

    def setCommunicationClusterRef(self, value: Optional[RefType]) -> TpConfig:
        """
        A TpConfig is existing always in the context of exactly one CommunicationCluster.
        A None value is a no-op and does not overwrite an existing communicationClusterRef.
        """
        if value is not None:
            self.communicationClusterRef = value
        return self


class CanTpAddress(Identifiable, VariationPointCapable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic Address.
    """

    # CanTpAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.255, p.610
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddress                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddress                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpAddressExtensionValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddressExtensionValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # An ECUs TP address on the referenced channel. This represents the diagnostic Address.
        self.tpAddress: Optional[Integer] = None

        # If the mixed addressing format is used, this parameter contains the transport protocol address extension value.
        self.tpAddressExtensionValue: Optional[Integer] = None

    def getTpAddress(self) -> Optional[Integer]:
        """An ECUs TP address on the referenced channel. This represents the diagnostic Address."""
        return self.tpAddress

    def setTpAddress(self, value: Optional[Integer]) -> CanTpAddress:
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

    def setTpAddressExtensionValue(self, value: Optional[Integer]) -> CanTpAddress:
        """
        If the mixed addressing format is used, this parameter contains the transport protocol address extension value.
        A None value is a no-op and does not overwrite an existing tpAddressExtensionValue.
        """
        if value is not None:
            self.tpAddressExtensionValue = value
        return self


class CanTpChannel(Identifiable, VariationPointCapable):
    """
    Configuration parameters of the CanTp channel.
    """

    # CanTpChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.252, p.608
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getChannelId [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setChannelId [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The id of the channel. The value shall be unique for each channel.
        self.channelId: Optional[PositiveInteger] = None

    def getChannelId(self) -> Optional[PositiveInteger]:
        """The id of the channel. The value shall be unique for each channel."""
        return self.channelId

    def setChannelId(self, value: Optional[PositiveInteger]) -> CanTpChannel:
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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on CanTpConnection.addressingFormat
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on CanTpConnection.taType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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


class TpAckType(AREnum):
    """Type of Acknowledgement."""

    # TpAckType method parity checklist:
    # Spec: class TpAckType, AUTOSAR_00052.xsd line 144716 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on FlexrayTpConnectionControl.ackType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Acknowledgement with retry. Tags: atp.EnumerationLiteralIndex=0
    ENUM_ACK_WITH_RT = "ACK-WITH-RT"

    # No acknowledgement. Tags: atp.EnumerationLiteralIndex=1
    ENUM_NO_ACK = "NO-ACK"

    def __init__(self):
        super().__init__(
            [
                TpAckType.ENUM_ACK_WITH_RT,
                TpAckType.ENUM_NO_ACK,
            ]
        )


class CanTpConnection(TpConnection, VariationPointCapable):
    """
    A connection identifies the sender and the receiver of this particular communication. The CanTp module routes a Pdu
    through this connection. atpVariation: Derived, because TpNode can vary.
    """

    # CanTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.253 (with Table 6.252 block), p.608-609
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddressingFormat   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressingFormat   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCancellation       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCancellation       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCanTpChannelRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCanTpChannelRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataPduRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataPduRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFlowControlPduRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFlowControlPduRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxBlockSize       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxBlockSize       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMulticastRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMulticastRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPaddingActivation  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPaddingActivation  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceiverRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addReceiverRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTaType             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTaType             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutBr          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutBr          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutBs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutBs          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutCr          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutCr          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutCs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutCs          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpSduRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpSduRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmitterRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmitterRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

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
        self.taType: Optional[NetworkTargetAddressType] = None

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

    def setAddressingFormat(self, value: Optional[CanTpAddressingFormatType]) -> CanTpConnection:
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

    def setCancellation(self, value: Optional[Boolean]) -> CanTpConnection:
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

    def setCanTpChannelRef(self, value: Optional[RefType]) -> CanTpConnection:
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

    def setDataPduRef(self, value: Optional[RefType]) -> CanTpConnection:
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

    def setFlowControlPduRef(self, value: Optional[RefType]) -> CanTpConnection:
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

    def setMaxBlockSize(self, value: Optional[Integer]) -> CanTpConnection:
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

    def setMulticastRef(self, value: Optional[RefType]) -> CanTpConnection:
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

    def setPaddingActivation(self, value: Optional[Boolean]) -> CanTpConnection:
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

    def addReceiverRef(self, value: Optional[RefType]) -> CanTpConnection:
        """
        The target of the TP connection.
        A None value is a no-op and is not appended to receiverRefs.
        """
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getTaType(self) -> Optional[NetworkTargetAddressType]:
        """Network Target Address type."""
        return self.taType

    def setTaType(self, value: Optional[NetworkTargetAddressType]) -> CanTpConnection:
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

    def setTimeoutBr(self, value: Optional[TimeValue]) -> CanTpConnection:
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

    def setTimeoutBs(self, value: Optional[TimeValue]) -> CanTpConnection:
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

    def setTimeoutCr(self, value: Optional[TimeValue]) -> CanTpConnection:
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

    def setTimeoutCs(self, value: Optional[TimeValue]) -> CanTpConnection:
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

    def setTpSduRef(self, value: Optional[RefType]) -> CanTpConnection:
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

    def setTransmitterRef(self, value: Optional[RefType]) -> CanTpConnection:
        """
        The source of the TP connection.
        A None value is a no-op and does not overwrite an existing transmitterRef.
        """
        if value is not None:
            self.transmitterRef = value
        return self


class CanTpEcu(ARObject, VariationPointCapable):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference to exactly one ECUInstance in the topology.
    """

    # CanTpEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.256, p.610
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCycleTimeMainFunction   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCycleTimeMainFunction   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuInstanceRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds.
        self.cycleTimeMainFunction: Optional[TimeValue] = None

        # Connection to the ECUInstance in the Topology
        self.ecuInstanceRef: Optional[RefType] = None

    def getCycleTimeMainFunction(self) -> Optional[TimeValue]:
        """The period between successive calls to the Main Function of the AUTOSAR TP. Specified in seconds."""
        return self.cycleTimeMainFunction

    def setCycleTimeMainFunction(self, value: Optional[TimeValue]) -> CanTpEcu:
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

    def setEcuInstanceRef(self, value: Optional[RefType]) -> CanTpEcu:
        """
        Connection to the ECUInstance in the Topology
        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self


class CanTpNode(Identifiable, VariationPointCapable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to the Topology description.
    """

    # CanTpNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.257, p.611
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConnectorRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConnectorRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxFcWait     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxFcWait     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStMin         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStMin         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutAr     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutAr     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutAs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutAs     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpAddressRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddressRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

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

    def setConnectorRef(self, value: Optional[RefType]) -> CanTpNode:
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

    def setMaxFcWait(self, value: Optional[Integer]) -> CanTpNode:
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

    def setStMin(self, value: Optional[TimeValue]) -> CanTpNode:
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

    def setTimeoutAr(self, value: Optional[TimeValue]) -> CanTpNode:
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

    def setTimeoutAs(self, value: Optional[TimeValue]) -> CanTpNode:
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

    def setTpAddressRef(self, value: Optional[RefType]) -> CanTpNode:
        """
        Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        A None value is a no-op and does not overwrite an existing tpAddressRef.
        """
        if value is not None:
            self.tpAddressRef = value
        return self


class CanTpConfig(TpConfig):
    """
    This element defines exactly one CAN TP Configuration.

    One CanTpConfig element shall be created for each CAN Network in the System.

    [constr_9247] Existence of CanTpConfig.tpAddress: For each CanTpConfig, the aggregation of CanTpAddress in the role tpAddress shall exist at least once at the time when the System Description is complete.
    [constr_9248] Existence of CanTpConfig.tpChannel: For each CanTpConfig, the aggregation of CanTpChannel in the role tpChannel shall exist at least once at the time when the System Description is complete.
    [constr_9249] Existence of CanTpConfig.tpConnection: For each CanTpConfig, the aggregation of CanTpConnection in the role tpConnection shall exist at least once at the time when the System Description is complete.
    [constr_9250] Existence of CanTpConfig.tpEcu: For each CanTpConfig, the aggregation of CanTpEcu in the role tpEcu shall exist at least once at the time when the System Description is complete.
    [constr_9251] Existence of CanTpConfig.tpNode: For each CanTpConfig, the aggregation of CanTpNode in the role tpNode shall exist at least once at the time when the System Description is complete.
    """

    # CanTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.251, p.607
    # Note: class Note taken from XSD CAN-TP-CONFIG complexType documentation (PDF table has no Note row)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddresses       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCanTpAddress   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpChannels        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCanTpChannel   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnections     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpEcus            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpEcu             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpNodes           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCanTpNode      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of TP Addresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpAddresses: List[CanTpAddress] = []

        # Configuration of CAN TP channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel.shortName, tpChannel.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpChannels: List[CanTpChannel] = []

        # Senders and receivers of CAN TP messages. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpConnections: List[CanTpConnection] = []

        # Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.tpEcus: List[CanTpEcu] = []

        # Senders and receivers of Can TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpNodes: List[CanTpNode] = []

    def getTpAddresses(self) -> List[CanTpAddress]:
        """
        Collection of TP Addresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpAddresses

    def createCanTpAddress(self, short_name: str) -> CanTpAddress:
        """
        Collection of TP Addresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, CanTpAddress):
            address = CanTpAddress(self, short_name)
            self.addReferrableElement(address)
            self.tpAddresses.append(address)
        return cast(CanTpAddress, self.getReferrableElement(short_name, CanTpAddress))

    def getTpChannels(self) -> List[CanTpChannel]:
        """
        Configuration of CAN TP channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel.shortName, tpChannel.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpChannels

    def createCanTpChannel(self, short_name: str) -> CanTpChannel:
        """
        Configuration of CAN TP channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel.shortName, tpChannel.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, CanTpChannel):
            channel = CanTpChannel(self, short_name)
            self.addReferrableElement(channel)
            self.tpChannels.append(channel)
        return cast(CanTpChannel, self.getReferrableElement(short_name, CanTpChannel))

    def getTpConnections(self) -> List[CanTpConnection]:
        """
        Senders and receivers of CAN TP messages. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[CanTpConnection]) -> CanTpConfig:
        """
        Senders and receivers of CAN TP messages. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpEcus(self) -> List[CanTpEcu]:
        """
        Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpEcus

    def addTpEcu(self, value: Optional[CanTpEcu]) -> CanTpConfig:
        """
        Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpEcus.
        """
        if value is not None:
            self.tpEcus.append(value)
        return self

    def getTpNodes(self) -> List[CanTpNode]:
        """
        Senders and receivers of Can TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpNodes

    def createCanTpNode(self, short_name: str) -> CanTpNode:
        """
        Senders and receivers of Can TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, CanTpNode):
            node = CanTpNode(self, short_name)
            self.addReferrableElement(node)
            self.tpNodes.append(node)
        return cast(CanTpNode, self.getReferrableElement(short_name, CanTpNode))


class DoIpLogicAddress(Identifiable):
    """
    The logical DoIP address.
    """

    # DoIpLogicAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.207, p.555
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddress                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddress                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpLogicTargetAddressProps  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpLogicTesterAddressProps  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpLogicAddressProps           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The logical DoIP address.
        self.address: Optional[Integer] = None

        # Collection of additional LogicAddress properties.
        self.doIpLogicAddressProps: Optional[AbstractDoIpLogicAddressProps] = None

    def getAddress(self) -> Optional[Integer]:
        """The logical DoIP address."""
        return self.address

    def setAddress(self, value: Optional[Integer]) -> DoIpLogicAddress:
        """
        The logical DoIP address.
        A None value is a no-op and does not overwrite an existing address.
        """
        if value is not None:
            self.address = value
        return self

    def createDoIpLogicTargetAddressProps(self, short_name: str) -> DoIpLogicTargetAddressProps:
        """Collection of additional LogicAddress properties."""
        if self.getDoIpLogicAddressProps() is None:
            self.doIpLogicAddressProps = DoIpLogicTargetAddressProps(self, short_name)
        return cast(DoIpLogicTargetAddressProps, self.getDoIpLogicAddressProps())

    def createDoIpLogicTesterAddressProps(self, short_name: str) -> DoIpLogicTesterAddressProps:
        """Collection of additional LogicAddress properties."""
        if self.getDoIpLogicAddressProps() is None:
            self.doIpLogicAddressProps = DoIpLogicTesterAddressProps(self, short_name)
        return cast(DoIpLogicTesterAddressProps, self.getDoIpLogicAddressProps())

    def getDoIpLogicAddressProps(self) -> Optional[AbstractDoIpLogicAddressProps]:
        """Collection of additional LogicAddress properties."""
        return self.doIpLogicAddressProps


class DoIpTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular communication. The DoIp module routes a tpSdu through this connection.
    """

    # DoIpTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.206, p.555
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDoIpSourceAddressRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDoIpSourceAddressRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpTargetAddressRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDoIpTargetAddressRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpSduRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpSduRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the address of the sender of the tpSdu.
        self.doIpSourceAddressRef: Optional[RefType] = None

        # Reference to the address of the receiver of the tpSdu.
        self.doIpTargetAddressRef: Optional[RefType] = None

        # This reference is used to describe the data exchange between DoIp and the PduR.
        self.tpSduRef: Optional[RefType] = None

    def getDoIpSourceAddressRef(self) -> Optional[RefType]:
        """Reference to the address of the sender of the tpSdu."""
        return self.doIpSourceAddressRef

    def setDoIpSourceAddressRef(self, value: Optional[RefType]) -> DoIpTpConnection:
        """
        Reference to the address of the sender of the tpSdu.
        A None value is a no-op and does not overwrite an existing doIpSourceAddressRef.
        """
        if value is not None:
            self.doIpSourceAddressRef = value
        return self

    def getDoIpTargetAddressRef(self) -> Optional[RefType]:
        """Reference to the address of the receiver of the tpSdu."""
        return self.doIpTargetAddressRef

    def setDoIpTargetAddressRef(self, value: Optional[RefType]) -> DoIpTpConnection:
        """
        Reference to the address of the receiver of the tpSdu.
        A None value is a no-op and does not overwrite an existing doIpTargetAddressRef.
        """
        if value is not None:
            self.doIpTargetAddressRef = value
        return self

    def getTpSduRef(self) -> Optional[RefType]:
        """This reference is used to describe the data exchange between DoIp and the PduR."""
        return self.tpSduRef

    def setTpSduRef(self, value: Optional[RefType]) -> DoIpTpConnection:
        """
        This reference is used to describe the data exchange between DoIp and the PduR.
        A None value is a no-op and does not overwrite an existing tpSduRef.
        """
        if value is not None:
            self.tpSduRef = value
        return self


class DoIpTpConfig(TpConfig):
    """
    This element defines exactly one DoIpTp Configuration that is used to configure all DoIPChannels available in a DoIpInterface. Each DoIPChannel describes a connection between a doIpSourceAddress and a doIpTargetAddress and the exchange of DcmIPdus between the PduR and DoIP.
    """

    # DoIpTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.205, p.555
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createDoIpLogicAddress   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpLogicAddresses    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnections         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of logical DoIP Addresses.
        self.doIpLogicAddresses: List[DoIpLogicAddress] = []

        # Collection of unidirectional connections between a source address and a target address.
        self.tpConnections: List[DoIpTpConnection] = []

    def getDoIpLogicAddresses(self) -> List[DoIpLogicAddress]:
        """
        Collection of logical DoIP Addresses.
        """
        return self.doIpLogicAddresses

    def createDoIpLogicAddress(self, short_name: str) -> DoIpLogicAddress:
        """
        Collection of logical DoIP Addresses.
        """
        if not self.IsReferrableElementExists(short_name, DoIpLogicAddress):
            address = DoIpLogicAddress(self, short_name)
            self.addReferrableElement(address)
            self.doIpLogicAddresses.append(address)
        return cast(DoIpLogicAddress, self.getReferrableElement(short_name, DoIpLogicAddress))

    def getTpConnections(self) -> List[DoIpTpConnection]:
        """
        Collection of unidirectional connections between a source address and a target address.
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[DoIpTpConnection]) -> DoIpTpConfig:
        """
        Collection of unidirectional connections between a source address and a target address.
        A None value is a no-op and does not extend the tpConnections list.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self


class TpAddress(Identifiable, VariationPointCapable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic Address.

    [constr_9227] Existence of TpAddress.tpAddress: For each TpAddress, the attribute tpAddress shall exist at the time when the System Description is complete.
    """

    # TpAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.238, p.588
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddress  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddress  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # An ECUs TP address on the referenced channel. This represents the diagnostic Address.
        self.tpAddress: Optional[Integer] = None

    def getTpAddress(self) -> Optional[Integer]:
        """An ECUs TP address on the referenced channel. This represents the diagnostic Address."""
        return self.tpAddress

    def setTpAddress(self, value: Optional[Integer]) -> TpAddress:
        """
        An ECUs TP address on the referenced channel. This represents the diagnostic Address.
        A None value is a no-op and does not overwrite an existing tpAddress.
        """
        if value is not None:
            self.tpAddress = value
        return self


class LinTpConnection(TpConnection, VariationPointCapable):
    """
    A LinTP channel represents an internal path for the transmission or reception of a Pdu via LinTp and describes the sender and the receiver of this particular communication. LinTp supports (per Lin Cluster) the configuration of one Rx Tp-SDU and one Tx Tp-SDU per NAD the LinMaster uses to address one or more of its Lin Slaves. To support this an arbitrary number of LinTp Connections shall be described.

    [constr_9260] Existence of LinTpConnection.dataPdu: For each LinTpConnection, the reference to NPdu in the role dataPdu shall exist at the time when the System Description is complete.

    [constr_9261] Existence of LinTpConnection.linTpNSdu: For each LinTpConnection, the reference to IPdu in the role linTpNSdu shall exist at the time when the System Description is complete.

    [constr_9262] Existence of LinTpConnection.receiver: For each LinTpConnection, at least one reference to LinTpNode in the role receiver shall exist at the time when the System Description is complete.

    [constr_9263] Existence of LinTpConnection.transmitter: For each LinTpConnection, the reference to LinTpNode in the role transmitter shall exist at the time when the System Description is complete.

    [constr_5377] IPdu shall only be referenced once from a LinTpConnection in the role linTpNSdu on a LinCluster: Each IPdu that is referenced in the role linTpNSdu from a LinTpConnection that is aggregated by a LinTpConfig that references a LinCluster shall not be referenced in the role linTpNSdu from a different LinTpConnection that is aggregated by a LinTpConfig that references the same LinCluster.
    """

    # LinTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.261, p.616
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataPduRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataPduRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFlowControlRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFlowControlRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLinTpNSduRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLinTpNSduRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMulticastRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMulticastRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addReceiverRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceiverRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getTimeoutAs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutAs        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutCr        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutCr        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutCs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutCs        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmitterRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmitterRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to an NPdu (Single Frame, First Frame or Consecutive Frame). The Single Frame network protocol data unit (SF N_PDU) shall be sent out by the sending network entity and can be received by one or multiple receiving network entities. The Single Frame (SF N_PDU) shall be sent out to transfer a service data unit that can be transferred via a single service request to the data link layer. This network protocol data unit shall be sent to transfer unsegmented messages. The First Frame network protocol data unit (FF N_PDU) identifies the first network protocol data unit (N_PDU) of a segmented message transmitted by a network sending entity and received by a receiving network entity. The Consecutive Frame network protocol data unit (CF N_PDU) transfers segments (N_Data) of the service data unit message data (<MessageData>). All network protocol data units (N_PDUs) transmitted by the sending entity after the First Frame network protocol data unit (FF N_PDU) shall be encoded as Consecutive Frames network protocol data units (CF N_PDUs).
        self.dataPduRef: Optional[RefType] = None

        # Reference to the Flow Control NPdu. The Flow Control network protocol data unit (FC N_PDU) is identified by the Flow Control protocol control information (FC N_PCI). The Flow Control network protocol data unit (FC N_PDU) instructs a sending network entity to start, stop or resume transmission of CF N_PDUs. The Flow Control network protocol data unit shall be sent by the receiving network layer entity to the sending network layer entity, when ready to receive more data, after correct reception of: a) First Frame network protocol data unit (FF N_PDU) b) the last Consecutive Frame network protocol data unit (CF N_PDU) of a block of Consecutive Frames (CF N_ PDU) if further Consecutive Frame network protocol data unit (CF N_PDU) need(s) to be sent.
        self.flowControlRef: Optional[RefType] = None

        # Reference to the IPdu that is segmented by the Transport Protocol.
        self.linTpNSduRef: Optional[RefType] = None

        # TP address for 1:n connections.
        self.multicastRef: Optional[RefType] = None

        # The target of the TP connection.
        self.receiverRefs: List[RefType] = []

        # Time for transmission of the LIN frame (any N-PDU) on the sender side. Specified in seconds.
        self.timeoutAs: Optional[TimeValue] = None

        # This attribute defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        self.timeoutCr: Optional[TimeValue] = None

        # The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU.
        self.timeoutCs: Optional[TimeValue] = None

        # The source of the TP connection.
        self.transmitterRef: Optional[RefType] = None

    def getDataPduRef(self) -> Optional[RefType]:
        """Reference to an NPdu (Single Frame, First Frame or Consecutive Frame). The Single Frame network protocol data unit (SF N_PDU) shall be sent out by the sending network entity and can be received by one or multiple receiving network entities. The Single Frame (SF N_PDU) shall be sent out to transfer a service data unit that can be transferred via a single service request to the data link layer. This network protocol data unit shall be sent to transfer unsegmented messages. The First Frame network protocol data unit (FF N_PDU) identifies the first network protocol data unit (N_PDU) of a segmented message transmitted by a network sending entity and received by a receiving network entity. The Consecutive Frame network protocol data unit (CF N_PDU) transfers segments (N_Data) of the service data unit message data (<MessageData>). All network protocol data units (N_PDUs) transmitted by the sending entity after the First Frame network protocol data unit (FF N_PDU) shall be encoded as Consecutive Frames network protocol data units (CF N_PDUs)."""
        return self.dataPduRef

    def setDataPduRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        Reference to an NPdu (Single Frame, First Frame or Consecutive Frame). The Single Frame network protocol data unit (SF N_PDU) shall be sent out by the sending network entity and can be received by one or multiple receiving network entities. The Single Frame (SF N_PDU) shall be sent out to transfer a service data unit that can be transferred via a single service request to the data link layer. This network protocol data unit shall be sent to transfer unsegmented messages. The First Frame network protocol data unit (FF N_PDU) identifies the first network protocol data unit (N_PDU) of a segmented message transmitted by a network sending entity and received by a receiving network entity. The Consecutive Frame network protocol data unit (CF N_PDU) transfers segments (N_Data) of the service data unit message data (<MessageData>). All network protocol data units (N_PDUs) transmitted by the sending entity after the First Frame network protocol data unit (FF N_PDU) shall be encoded as Consecutive Frames network protocol data units (CF N_PDUs).
        A None value is a no-op and does not overwrite an existing dataPduRef.
        """
        if value is not None:
            self.dataPduRef = value
        return self

    def getFlowControlRef(self) -> Optional[RefType]:
        """Reference to the Flow Control NPdu. The Flow Control network protocol data unit (FC N_PDU) is identified by the Flow Control protocol control information (FC N_PCI). The Flow Control network protocol data unit (FC N_PDU) instructs a sending network entity to start, stop or resume transmission of CF N_PDUs. The Flow Control network protocol data unit shall be sent by the receiving network layer entity to the sending network layer entity, when ready to receive more data, after correct reception of: a) First Frame network protocol data unit (FF N_PDU) b) the last Consecutive Frame network protocol data unit (CF N_PDU) of a block of Consecutive Frames (CF N_ PDU) if further Consecutive Frame network protocol data unit (CF N_PDU) need(s) to be sent."""
        return self.flowControlRef

    def setFlowControlRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        Reference to the Flow Control NPdu. The Flow Control network protocol data unit (FC N_PDU) is identified by the Flow Control protocol control information (FC N_PCI). The Flow Control network protocol data unit (FC N_PDU) instructs a sending network entity to start, stop or resume transmission of CF N_PDUs. The Flow Control network protocol data unit shall be sent by the receiving network layer entity to the sending network layer entity, when ready to receive more data, after correct reception of: a) First Frame network protocol data unit (FF N_PDU) b) the last Consecutive Frame network protocol data unit (CF N_PDU) of a block of Consecutive Frames (CF N_ PDU) if further Consecutive Frame network protocol data unit (CF N_PDU) need(s) to be sent.
        A None value is a no-op and does not overwrite an existing flowControlRef.
        """
        if value is not None:
            self.flowControlRef = value
        return self

    def getLinTpNSduRef(self) -> Optional[RefType]:
        """Reference to the IPdu that is segmented by the Transport Protocol."""
        return self.linTpNSduRef

    def setLinTpNSduRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        Reference to the IPdu that is segmented by the Transport Protocol.
        A None value is a no-op and does not overwrite an existing linTpNSduRef.
        """
        if value is not None:
            self.linTpNSduRef = value
        return self

    def getMulticastRef(self) -> Optional[RefType]:
        """TP address for 1:n connections."""
        return self.multicastRef

    def setMulticastRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        TP address for 1:n connections.
        A None value is a no-op and does not overwrite an existing multicastRef.
        """
        if value is not None:
            self.multicastRef = value
        return self

    def addReceiverRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        The target of the TP connection.
        A None value is a no-op and does not extend the receiverRefs list.
        """
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getReceiverRefs(self) -> List[RefType]:
        """The target of the TP connection."""
        return self.receiverRefs

    def getTimeoutAs(self) -> Optional[TimeValue]:
        """Time for transmission of the LIN frame (any N-PDU) on the sender side. Specified in seconds."""
        return self.timeoutAs

    def setTimeoutAs(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        Time for transmission of the LIN frame (any N-PDU) on the sender side. Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutAs.
        """
        if value is not None:
            self.timeoutAs = value
        return self

    def getTimeoutCr(self) -> Optional[TimeValue]:
        """This attribute defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds."""
        return self.timeoutCr

    def setTimeoutCr(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        This attribute defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutCr.
        """
        if value is not None:
            self.timeoutCr = value
        return self

    def getTimeoutCs(self) -> Optional[TimeValue]:
        """The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU."""
        return self.timeoutCs

    def setTimeoutCs(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU.
        A None value is a no-op and does not overwrite an existing timeoutCs.
        """
        if value is not None:
            self.timeoutCs = value
        return self

    def getTransmitterRef(self) -> Optional[RefType]:
        """The source of the TP connection."""
        return self.transmitterRef

    def setTransmitterRef(self, value: Optional[RefType]) -> LinTpConnection:
        """
        The source of the TP connection.
        A None value is a no-op and does not overwrite an existing transmitterRef.
        """
        if value is not None:
            self.transmitterRef = value
        return self


class LinTpNode(Identifiable, VariationPointCapable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to the Topology description.
    """

    # LinTpNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.260, p.615
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConnectorRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConnectorRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDropNotRequestedNad           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDropNotRequestedNad           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfRespPendingFrames [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfRespPendingFrames [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getP2Max                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setP2Max                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getP2Timing                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setP2Timing                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpAddressRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddressRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, Identifiable, MultilanguageReferrable, Referrable; aggregated by LinTpConfig.tpNode)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided).
        self.connectorRef: Optional[RefType] = None

        # Configures if TP Frames of not requested LIN-Slaves are dropped or not.
        self.dropNotRequestedNad: Optional[Boolean] = None

        # Configures the maximum number of allowed response pending frames.
        self.maxNumberOfRespPendingFrames: Optional[Integer] = None

        # After reception of a response pending frame the P2 timeout counter is reloaded with the timeout time P2max.
        self.p2Max: Optional[TimeValue] = None

        # P2 timeout observation parameter.
        self.p2Timing: Optional[TimeValue] = None

        # Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        self.tpAddressRef: Optional[RefType] = None

    def getConnectorRef(self) -> Optional[RefType]:
        """
        Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided).
        """
        return self.connectorRef

    def setConnectorRef(self, value: Optional[RefType]) -> LinTpNode:
        """
        Association to a CommunicationConnector in the topology description. In a System Description this reference is mandatory. In an ECU Extract this reference is optional (references to ECUs that are not part of the ECU Extract shall be avoided).
        A None value is a no-op and does not overwrite an existing connectorRef.
        """
        if value is not None:
            self.connectorRef = value
        return self

    def getDropNotRequestedNad(self) -> Optional[Boolean]:
        """
        Configures if TP Frames of not requested LIN-Slaves are dropped or not.
        """
        return self.dropNotRequestedNad

    def setDropNotRequestedNad(self, value: Optional[Boolean]) -> LinTpNode:
        """
        Configures if TP Frames of not requested LIN-Slaves are dropped or not.
        A None value is a no-op and does not overwrite an existing dropNotRequestedNad.
        """
        if value is not None:
            self.dropNotRequestedNad = value
        return self

    def getMaxNumberOfRespPendingFrames(self) -> Optional[Integer]:
        """
        Configures the maximum number of allowed response pending frames.
        """
        return self.maxNumberOfRespPendingFrames

    def setMaxNumberOfRespPendingFrames(self, value: Optional[Integer]) -> LinTpNode:
        """
        Configures the maximum number of allowed response pending frames.
        A None value is a no-op and does not overwrite an existing maxNumberOfRespPendingFrames.
        """
        if value is not None:
            self.maxNumberOfRespPendingFrames = value
        return self

    def getP2Max(self) -> Optional[TimeValue]:
        """
        After reception of a response pending frame the P2 timeout counter is reloaded with the timeout time P2max.
        """
        return self.p2Max

    def setP2Max(self, value: Optional[TimeValue]) -> LinTpNode:
        """
        After reception of a response pending frame the P2 timeout counter is reloaded with the timeout time P2max.
        A None value is a no-op and does not overwrite an existing p2Max.
        """
        if value is not None:
            self.p2Max = value
        return self

    def getP2Timing(self) -> Optional[TimeValue]:
        """
        P2 timeout observation parameter.
        """
        return self.p2Timing

    def setP2Timing(self, value: Optional[TimeValue]) -> LinTpNode:
        """
        P2 timeout observation parameter.
        A None value is a no-op and does not overwrite an existing p2Timing.
        """
        if value is not None:
            self.p2Timing = value
        return self

    def getTpAddressRef(self) -> Optional[RefType]:
        """
        Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        """
        return self.tpAddressRef

    def setTpAddressRef(self, value: Optional[RefType]) -> LinTpNode:
        """
        Reference to the TP Address that is used by the TpNode. This reference is optional in case that the multicast TP Address is used (reference from TpConnection).
        A None value is a no-op and does not overwrite an existing tpAddressRef.
        """
        if value is not None:
            self.tpAddressRef = value
        return self


class LinTpConfig(TpConfig):
    """
    This element defines exactly one Lin TP Configuration. One LinTpConfig element shall be created for each Lin Network in the System. Tags: atp.recommendedPackage=TpConfigs
    """

    # LinTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.259, p.614
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddresses     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTpAddress    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnections   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpNodes         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createLinTpNode    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpAddresses: List[TpAddress] = []

        # Configuration of LIN TP channels. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpConnections: List[LinTpConnection] = []

        # Senders and receivers of LIN TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpNodes: List[LinTpNode] = []

    def getTpAddresses(self) -> List[TpAddress]:
        """
        Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpAddresses

    def createTpAddress(self, short_name: str) -> TpAddress:
        """
        Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TpAddress):
            address = TpAddress(self, short_name)
            self.addReferrableElement(address)
            self.tpAddresses.append(address)
        return cast(TpAddress, self.getReferrableElement(short_name, TpAddress))

    def getTpConnections(self) -> List[LinTpConnection]:
        """
        Configuration of LIN TP channels. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[LinTpConnection]) -> LinTpConfig:
        """
        Configuration of LIN TP channels. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpNodes(self) -> List[LinTpNode]:
        """
        Senders and receivers of LIN TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpNodes

    def createLinTpNode(self, short_name: str) -> LinTpNode:
        """
        Senders and receivers of LIN TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, LinTpNode):
            address = LinTpNode(self, short_name)
            self.addReferrableElement(address)
            self.tpNodes.append(address)
        return cast(LinTpNode, self.getReferrableElement(short_name, LinTpNode))


class FlexrayTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay ISO TP Configuration. One FlexrayTpConfig element shall be created for each FlexRay Network in the System that uses Flex Ray Iso Tp. Tags: atp.recommendedPackage=TpConfigs

    [constr_9228] Existence of FlexrayTpConfig.pduPool: For each FlexrayTpConfig, the aggregation of FlexrayTpPduPool in the role pduPool shall exist at least once at the time when the System Description is complete.
    [constr_9229] Existence of FlexrayTpConfig.tpAddress: For each FlexrayTpConfig, the aggregation of TpAddress in the role tpAddress shall exist at least once at the time when the System Description is complete.
    [constr_9230] Existence of FlexrayTpConfig.tpEcu: For each FlexrayTpConfig, the aggregation of FlexrayTpEcu in the role tpEcu shall exist at least once at the time when the System Description is complete.
    """

    # FlexrayTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.239, p.592
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPduPools                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createFlexrayTpPduPool            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpAddresses                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTpAddress                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnections                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnectionControls           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createFlexrayTpConnectionControl  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpEcus                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpEcu                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpNodes                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createFlexrayTpNode               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Configuration of FlexRay TP Pdu Pools. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduPool.shortName, pduPool.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.pduPools: List[FlexrayTpPduPool] = []

        # Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpAddresses: List[TpAddress] = []

        # Configuration of FlexRay TP Connections. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpConnections: List[FlexrayTpConnection] = []

        # Configuration of FlexRay TP Connection Controls. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnectionControl.shortName, tp ConnectionControl.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.tpConnectionControls: List[FlexrayTpConnectionControl] = []

        # Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.tpEcus: List[FlexrayTpEcu] = []

        # Senders and receivers of FlexRay TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpNodes: List[FlexrayTpNode] = []

    def getPduPools(self) -> List[FlexrayTpPduPool]:
        """
        Configuration of FlexRay TP Pdu Pools. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduPool.shortName, pduPool.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.pduPools

    def createFlexrayTpPduPool(self, short_name: str) -> FlexrayTpPduPool:
        """
        Configuration of FlexRay TP Pdu Pools. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduPool.shortName, pduPool.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, FlexrayTpPduPool):
            pool = FlexrayTpPduPool(self, short_name)
            self.addReferrableElement(pool)
            self.pduPools.append(pool)
        return cast(FlexrayTpPduPool, self.getReferrableElement(short_name, FlexrayTpPduPool))

    def getTpAddresses(self) -> List[TpAddress]:
        """
        Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpAddresses

    def createTpAddress(self, short_name: str) -> TpAddress:
        """
        Collection of TpAddresses. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TpAddress):
            address = TpAddress(self, short_name)
            self.addReferrableElement(address)
            self.tpAddresses.append(address)
        return cast(TpAddress, self.getReferrableElement(short_name, TpAddress))

    def getTpConnections(self) -> List[FlexrayTpConnection]:
        """
        Configuration of FlexRay TP Connections. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[FlexrayTpConnection]) -> FlexrayTpConfig:
        """
        Configuration of FlexRay TP Connections. atpVariation: Derived, because TpNode can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection, tpConnection.variation Point.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self

    def getTpConnectionControls(self) -> List[FlexrayTpConnectionControl]:
        """
        Configuration of FlexRay TP Connection Controls. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnectionControl.shortName, tp ConnectionControl.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpConnectionControls

    def createFlexrayTpConnectionControl(self, short_name: str) -> FlexrayTpConnectionControl:
        """
        Configuration of FlexRay TP Connection Controls. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnectionControl.shortName, tp ConnectionControl.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, FlexrayTpConnectionControl):
            control = FlexrayTpConnectionControl(self, short_name)
            self.addReferrableElement(control)
            self.tpConnectionControls.append(control)
        return cast(FlexrayTpConnectionControl, self.getReferrableElement(short_name, FlexrayTpConnectionControl))

    def getTpEcus(self) -> List[FlexrayTpEcu]:
        """
        Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpEcus

    def addTpEcu(self, value: Optional[FlexrayTpEcu]) -> FlexrayTpConfig:
        """
        Collection of TP Ecus atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpEcu, tpEcu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpEcus.
        """
        if value is not None:
            self.tpEcus.append(value)
        return self

    def getTpNodes(self) -> List[FlexrayTpNode]:
        """
        Senders and receivers of FlexRay TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpNodes

    def createFlexrayTpNode(self, short_name: str) -> FlexrayTpNode:
        """
        Senders and receivers of FlexRay TP messages. atpVariation: Derived, because EcuInstance can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, FlexrayTpNode):
            node = FlexrayTpNode(self, short_name)
            self.addReferrableElement(node)
            self.tpNodes.append(node)
        return cast(FlexrayTpNode, self.getReferrableElement(short_name, FlexrayTpNode))


class FlexrayTpConnection(TpConnection, VariationPointCapable):
    """
    A connection identifies the sender and the receiver of this particular communication. The FlexRayTp module routes a Pdu through this connection. In a System Description the references to the PduPools are mandatory. In an ECU Extract these references can be optional: On unicast connections these references are always mandatory. On multicast the txPduPool is mandatory on the sender side. The rxPduPool is mandatory on the receiver side. On Gateway ECUs both references are mandatory.

    [constr_9231] Existence of FlexrayTpConnection.directTpSdu: For each FlexrayTpConnection, the reference to IPdu in the role directTpSdu shall exist at the time when the System Description is complete.

    [constr_9233] Existence of FlexrayTpConnection.receiver: For each FlexrayTpConnection, the reference to FlexrayTpNode in the role receiver shall exist at least once at the time when the System Description is complete.

    [constr_9234] Existence of FlexrayTpConnection.tpConnectionControl: For each FlexrayTpConnection, the reference to FlexrayTpConnectionControl in the role tpConnectionControl shall exist at the time when the System Description is complete.

    [constr_9235] Existence of FlexrayTpConnection.transmitter: For each FlexrayTpConnection, the reference to FlexrayTpNode in the role transmitter shall exist at the time when the System Description is complete.
    """

    # FlexrayTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.241, p.594
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBandwidthLimitation          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBandwidthLimitation          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDirectTpSduRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDirectTpSduRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMulticastRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMulticastRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addReceiverRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceiverRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getReversedTpSduRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReversedTpSduRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRxPduPoolRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRxPduPoolRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnectionControlRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpConnectionControlRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransmitterRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmitterRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTxPduPoolRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTxPduPoolRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies whether the connection requires a bandwidth limitation or not.
        self.bandwidthLimitation: Optional[Boolean] = None

        # Reference to the IPdu that is segmented by the Transport Protocol.
        self.directTpSduRef: Optional[RefType] = None

        # TP address for 1:n connections.
        self.multicastRef: Optional[RefType] = None

        # The target of the TP connection.
        self.receiverRefs: List[RefType] = []

        # Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction.
        self.reversedTpSduRef: Optional[RefType] = None

        # A connection has a reference to a set of NPdus (FrTpRx PduPool) which are defined for receiving data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the rxPduPool holds the actually received NPdus. In case this connection is applied to the receiver the rxPduPool holds the actually sent NPdus.
        self.rxPduPoolRef: Optional[RefType] = None

        # Reference to the connection control.
        self.tpConnectionControlRef: Optional[RefType] = None

        # The source of the TP connection.
        self.transmitterRef: Optional[RefType] = None

        # A connection has a reference to a set of NPdus (FrTpTx PduPool) which are defined for sending data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the txPduPool holds the actually sent NPdus. In case this connection is applied to the receiver the txPduPool holds the actually received NPdus.
        self.txPduPoolRef: Optional[RefType] = None

    def getBandwidthLimitation(self) -> Optional[Boolean]:
        """
        Specifies whether the connection requires a bandwidth limitation or not.
        """
        return self.bandwidthLimitation

    def setBandwidthLimitation(self, value: Optional[Boolean]) -> FlexrayTpConnection:
        """
        Specifies whether the connection requires a bandwidth limitation or not.
        A None value is a no-op and does not overwrite an existing bandwidthLimitation.
        """
        if value is not None:
            self.bandwidthLimitation = value
        return self

    def getDirectTpSduRef(self) -> Optional[RefType]:
        """
        Reference to the IPdu that is segmented by the Transport Protocol.
        """
        return self.directTpSduRef

    def setDirectTpSduRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        Reference to the IPdu that is segmented by the Transport Protocol.
        A None value is a no-op and does not overwrite an existing directTpSduRef.
        """
        if value is not None:
            self.directTpSduRef = value
        return self

    def getMulticastRef(self) -> Optional[RefType]:
        """
        TP address for 1:n connections.
        """
        return self.multicastRef

    def setMulticastRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        TP address for 1:n connections.
        A None value is a no-op and does not overwrite an existing multicastRef.
        """
        if value is not None:
            self.multicastRef = value
        return self

    def addReceiverRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        The target of the TP connection.
        A None value is a no-op and is not appended to receiverRefs.
        """
        if value is not None:
            self.receiverRefs.append(value)
        return self

    def getReceiverRefs(self) -> List[RefType]:
        """
        The target of the TP connection.
        """
        return self.receiverRefs

    def getReversedTpSduRef(self) -> Optional[RefType]:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction.
        """
        return self.reversedTpSduRef

    def setReversedTpSduRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction.
        A None value is a no-op and does not overwrite an existing reversedTpSduRef.
        """
        if value is not None:
            self.reversedTpSduRef = value
        return self

    def getRxPduPoolRef(self) -> Optional[RefType]:
        """
        A connection has a reference to a set of NPdus (FrTpRx PduPool) which are defined for receiving data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the rxPduPool holds the actually received NPdus. In case this connection is applied to the receiver the rxPduPool holds the actually sent NPdus.
        """
        return self.rxPduPoolRef

    def setRxPduPoolRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        A connection has a reference to a set of NPdus (FrTpRx PduPool) which are defined for receiving data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the rxPduPool holds the actually received NPdus. In case this connection is applied to the receiver the rxPduPool holds the actually sent NPdus.
        A None value is a no-op and does not overwrite an existing rxPduPoolRef.
        """
        if value is not None:
            self.rxPduPoolRef = value
        return self

    def getTpConnectionControlRef(self) -> Optional[RefType]:
        """
        Reference to the connection control.
        """
        return self.tpConnectionControlRef

    def setTpConnectionControlRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        Reference to the connection control.
        A None value is a no-op and does not overwrite an existing tpConnectionControlRef.
        """
        if value is not None:
            self.tpConnectionControlRef = value
        return self

    def getTransmitterRef(self) -> Optional[RefType]:
        """
        The source of the TP connection.
        """
        return self.transmitterRef

    def setTransmitterRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        The source of the TP connection.
        A None value is a no-op and does not overwrite an existing transmitterRef.
        """
        if value is not None:
            self.transmitterRef = value
        return self

    def getTxPduPoolRef(self) -> Optional[RefType]:
        """
        A connection has a reference to a set of NPdus (FrTpTx PduPool) which are defined for sending data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the txPduPool holds the actually sent NPdus. In case this connection is applied to the receiver the txPduPool holds the actually received NPdus.
        """
        return self.txPduPoolRef

    def setTxPduPoolRef(self, value: Optional[RefType]) -> FlexrayTpConnection:
        """
        A connection has a reference to a set of NPdus (FrTpTx PduPool) which are defined for sending data via this particular connection. The following constraint is valid only for the System Extract/ECU Extract: In case this connection is applied to the transmitter the txPduPool holds the actually sent NPdus. In case this connection is applied to the receiver the txPduPool holds the actually received NPdus.
        A None value is a no-op and does not overwrite an existing txPduPoolRef.
        """
        if value is not None:
            self.txPduPoolRef = value
        return self


class FlexrayTpConnectionControl(Identifiable, VariationPointCapable):
    """
    Configuration parameters to control a FlexRay TP connection.
    """

    # FlexrayTpConnectionControl method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.240, p.593
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAckType                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAckType                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxFcWait                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxFcWait                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxNumberOfNpduPerCycle      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxNumberOfNpduPerCycle      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxRetries                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxRetries                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSeparationCycleExponent      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSeparationCycleExponent      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeBr                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeBr                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeBuffer                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeBuffer                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeCs                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeCs                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutAr                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutAr                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutAs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutAs                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutBs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutBs                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeoutCr                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeoutCr                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, Identifiable, MultilanguageReferrable, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This parameter defines the type of acknowledgement which is used for the specific channel.
        self.ackType: Optional[TpAckType] = None

        # This attribute defines the maximum number of Flow Control N-PDUs with FlowState "WAIT".
        self.maxFcWait: Optional[Integer] = None

        # This parameter limits the number of N-Pdus the sender is allowed to transmit within a FlexRay cycle.
        self.maxNumberOfNpduPerCycle: Optional[Integer] = None

        # This parameter defines the maximum number of retries (if retry is configured for the particular channel).
        self.maxRetries: Optional[Integer] = None

        # Exponent to calculate the minimum number of "Separation Cycles" the sender has to wait for the next transmission of an FrTp N-Pdu.
        self.separationCycleExponent: Optional[Integer] = None

        # Time (in seconds) until transmission of the next Flow Control N-PDU.
        self.timeBr: Optional[TimeValue] = None

        # This parameter defines the time of waiting for the next try to get a Tx or Rx buffer. This parameter is equivalent to the temporal distance between two FC.WT N-Pdus in case the buffer request returns busy.
        self.timeBuffer: Optional[TimeValue] = None

        # Time (in seconds) until transmission of the next ConsecutiveFrame NPdu / LastFrame NPdu.
        self.timeCs: Optional[TimeValue] = None

        # This parameter states the timeout between the PDU transmit request of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface on the receiver side (for FC or AF). Specified in seconds.
        self.timeoutAr: Optional[TimeValue] = None

        # This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds.
        self.timeoutAs: Optional[TimeValue] = None

        # This parameter defines the timeout in seconds for waiting for an FC or AF on the sender side in a 1:1 connection.
        self.timeoutBs: Optional[TimeValue] = None

        # This parameter defines the timeout value in seconds for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        self.timeoutCr: Optional[TimeValue] = None

    def getAckType(self) -> Optional[TpAckType]:
        """
        This parameter defines the type of acknowledgement which is used for the specific channel.
        """
        return self.ackType

    def setAckType(self, value: Optional[TpAckType]) -> FlexrayTpConnectionControl:
        """
        This parameter defines the type of acknowledgement which is used for the specific channel.
        A None value is a no-op and does not overwrite an existing ackType.
        """
        if value is not None:
            self.ackType = value
        return self

    def getMaxFcWait(self) -> Optional[Integer]:
        """
        This attribute defines the maximum number of Flow Control N-PDUs with FlowState "WAIT".
        """
        return self.maxFcWait

    def setMaxFcWait(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        This attribute defines the maximum number of Flow Control N-PDUs with FlowState "WAIT".
        A None value is a no-op and does not overwrite an existing maxFcWait.
        """
        if value is not None:
            self.maxFcWait = value
        return self

    def getMaxNumberOfNpduPerCycle(self) -> Optional[Integer]:
        """
        This parameter limits the number of N-Pdus the sender is allowed to transmit within a FlexRay cycle.
        """
        return self.maxNumberOfNpduPerCycle

    def setMaxNumberOfNpduPerCycle(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        This parameter limits the number of N-Pdus the sender is allowed to transmit within a FlexRay cycle.
        A None value is a no-op and does not overwrite an existing maxNumberOfNpduPerCycle.
        """
        if value is not None:
            self.maxNumberOfNpduPerCycle = value
        return self

    def getMaxRetries(self) -> Optional[Integer]:
        """
        This parameter defines the maximum number of retries (if retry is configured for the particular channel).
        """
        return self.maxRetries

    def setMaxRetries(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        This parameter defines the maximum number of retries (if retry is configured for the particular channel).
        A None value is a no-op and does not overwrite an existing maxRetries.
        """
        if value is not None:
            self.maxRetries = value
        return self

    def getSeparationCycleExponent(self) -> Optional[Integer]:
        """
        Exponent to calculate the minimum number of "Separation Cycles" the sender has to wait for the next transmission of an FrTp N-Pdu.
        """
        return self.separationCycleExponent

    def setSeparationCycleExponent(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        Exponent to calculate the minimum number of "Separation Cycles" the sender has to wait for the next transmission of an FrTp N-Pdu.
        A None value is a no-op and does not overwrite an existing separationCycleExponent.
        """
        if value is not None:
            self.separationCycleExponent = value
        return self

    def getTimeBr(self) -> Optional[TimeValue]:
        """
        Time (in seconds) until transmission of the next Flow Control N-PDU.
        """
        return self.timeBr

    def setTimeBr(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Time (in seconds) until transmission of the next Flow Control N-PDU.
        A None value is a no-op and does not overwrite an existing timeBr.
        """
        if value is not None:
            self.timeBr = value
        return self

    def getTimeBuffer(self) -> Optional[TimeValue]:
        """
        This parameter defines the time of waiting for the next try to get a Tx or Rx buffer. This parameter is equivalent to the temporal distance between two FC.WT N-Pdus in case the buffer request returns busy.
        """
        return self.timeBuffer

    def setTimeBuffer(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        This parameter defines the time of waiting for the next try to get a Tx or Rx buffer. This parameter is equivalent to the temporal distance between two FC.WT N-Pdus in case the buffer request returns busy.
        A None value is a no-op and does not overwrite an existing timeBuffer.
        """
        if value is not None:
            self.timeBuffer = value
        return self

    def getTimeCs(self) -> Optional[TimeValue]:
        """
        Time (in seconds) until transmission of the next ConsecutiveFrame NPdu / LastFrame NPdu.
        """
        return self.timeCs

    def setTimeCs(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Time (in seconds) until transmission of the next ConsecutiveFrame NPdu / LastFrame NPdu.
        A None value is a no-op and does not overwrite an existing timeCs.
        """
        if value is not None:
            self.timeCs = value
        return self

    def getTimeoutAr(self) -> Optional[TimeValue]:
        """
        This parameter states the timeout between the PDU transmit request of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface on the receiver side (for FC or AF). Specified in seconds.
        """
        return self.timeoutAr

    def setTimeoutAr(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        This parameter states the timeout between the PDU transmit request of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface on the receiver side (for FC or AF). Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutAr.
        """
        if value is not None:
            self.timeoutAr = value
        return self

    def getTimeoutAs(self) -> Optional[TimeValue]:
        """
        This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds.
        """
        return self.timeoutAs

    def setTimeoutAs(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        This attribute states the timeout between the PDU transmit request for the first PDU of the group used in the current connection of the Transport Layer to the FlexRay Interface and the corresponding confirmation of the Flex Ray Interface (when having sent the last PDU of the group used in this connection) on the sender side (SF-x, FF-x, CF or FC (in case of Transmit Cancellation)). Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutAs.
        """
        if value is not None:
            self.timeoutAs = value
        return self

    def getTimeoutBs(self) -> Optional[TimeValue]:
        """
        This parameter defines the timeout in seconds for waiting for an FC or AF on the sender side in a 1:1 connection.
        """
        return self.timeoutBs

    def setTimeoutBs(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        This parameter defines the timeout in seconds for waiting for an FC or AF on the sender side in a 1:1 connection.
        A None value is a no-op and does not overwrite an existing timeoutBs.
        """
        if value is not None:
            self.timeoutBs = value
        return self

    def getTimeoutCr(self) -> Optional[TimeValue]:
        """
        This parameter defines the timeout value in seconds for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        """
        return self.timeoutCr

    def setTimeoutCr(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        This parameter defines the timeout value in seconds for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds.
        A None value is a no-op and does not overwrite an existing timeoutCr.
        """
        if value is not None:
            self.timeoutCr = value
        return self


class FlexrayArTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay Autosar TP Configuration. One FlexrayArTpConfig element shall be created for each FlexRay Network in the System that uses Flex Ray Autosar TP. Tags: atp.recommendedPackage=TpConfigs
    """

    # FlexrayArTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.245, p.600
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddresses           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTpAddress          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpChannels            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpChannel             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpNodes               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createFlexrayArTpNode    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of TpAddresses. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpAddresses: List[TpAddress] = []

        # Configuration of FlexRay Autosar Transport Protocol channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel, tpChannel.variationPoint.short Label vh.latestBindingTime=postBuild
        self.tpChannels: List[FlexrayArTpChannel] = []

        # Senders and receivers of TP messages. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.tpNodes: List[FlexrayArTpNode] = []

    def getTpAddresses(self) -> List[TpAddress]:
        """
        Collection of TpAddresses. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpAddresses

    def createTpAddress(self, short_name: str) -> TpAddress:
        """
        Collection of TpAddresses. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpAddress.shortName, tpAddress.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TpAddress):
            address = TpAddress(self, short_name)
            self.addReferrableElement(address)
            self.tpAddresses.append(address)
        return cast(TpAddress, self.getReferrableElement(short_name, TpAddress))

    def getTpChannels(self) -> List[FlexrayArTpChannel]:
        """
        Configuration of FlexRay Autosar Transport Protocol channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel, tpChannel.variationPoint.short Label vh.latestBindingTime=postBuild
        """
        return self.tpChannels

    def addTpChannel(self, value: Optional[FlexrayArTpChannel]) -> FlexrayArTpConfig:
        """
        Configuration of FlexRay Autosar Transport Protocol channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpChannel, tpChannel.variationPoint.short Label vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpChannels.
        """
        if value is not None:
            self.tpChannels.append(value)
        return self

    def getTpNodes(self) -> List[FlexrayArTpNode]:
        """
        Senders and receivers of TP messages. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        return self.tpNodes

    def createFlexrayArTpNode(self, short_name: str) -> FlexrayArTpNode:
        """
        Senders and receivers of TP messages. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpNode.shortName, tpNode.variation Point.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, FlexrayArTpNode):
            node = FlexrayArTpNode(self, short_name)
            self.addReferrableElement(node)
            self.tpNodes.append(node)
        return cast(FlexrayArTpNode, self.getReferrableElement(short_name, FlexrayArTpNode))


class FlexrayArTpConnection(TpConnection):
    """
    A connection within a channel identifies the sender and the receiver of this particular communication. The FlexRay Autosar Tp module routes a Pdu through this connection.

    [constr_9244] Existence of FlexrayArTpConnection.directTpSdu: For each FlexrayArTpConnection, the reference to IPdu in the role directTpSdu shall exist at the time when the System Description is complete.

    [constr_9245] Existence of FlexrayArTpConnection.source: For each FlexrayArTpConnection, the reference to FlexrayArTpNode in the role source shall exist at the time when the System Description is complete.

    [constr_9246] Existence of FlexrayArTpConnection.target: For each FlexrayArTpConnection, at least one reference to FlexrayArTpNode in the role target shall exist at the time when the System Description is complete.
    """

    # FlexrayArTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.248, p.603
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConnectionPrioPdus  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConnectionPrioPdus  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDirectTpSduRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDirectTpSduRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMulticastRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMulticastRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReversedTpSduRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReversedTpSduRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addTargetRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This parameter defines the number of PDUs that shall be reserved for this connection when it is active. The range is 1-255.
        self.connectionPrioPdus: Optional[Integer] = None

        # Reference to the IPdu that is segmented by the Transport Protocol. The source address of the transmitted NPdu is determined by the configured source Communication Connector. The target address of the transmitted NPdu is determined by the configured target Communication Connector.
        self.directTpSduRef: Optional[RefType] = None

        # TP address for 1:n connections.
        self.multicastRef: Optional[RefType] = None

        # Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction. The source address of the transmitted NPdu is determined by the configured target Communication Connector. The target address of the transmitted NPdu is determined by the configured source Communication Connector.
        self.reversedTpSduRef: Optional[RefType] = None

        # The source of the TP connection.
        self.sourceRef: Optional[RefType] = None

        # The target of the TP connection.
        self.targetRefs: List[RefType] = []

    def getConnectionPrioPdus(self) -> Optional[Integer]:
        """
        This parameter defines the number of PDUs that shall be reserved for this connection when it is active. The range is 1-255.
        """
        return self.connectionPrioPdus

    def setConnectionPrioPdus(self, value: Optional[Integer]) -> FlexrayArTpConnection:
        """
        This parameter defines the number of PDUs that shall be reserved for this connection when it is active. The range is 1-255.
        A None value is a no-op and does not overwrite an existing connectionPrioPdus.
        """
        if value is not None:
            self.connectionPrioPdus = value
        return self

    def getDirectTpSduRef(self) -> Optional[RefType]:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. The source address of the transmitted NPdu is determined by the configured source Communication Connector. The target address of the transmitted NPdu is determined by the configured target Communication Connector.
        """
        return self.directTpSduRef

    def setDirectTpSduRef(self, value: Optional[RefType]) -> FlexrayArTpConnection:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. The source address of the transmitted NPdu is determined by the configured source Communication Connector. The target address of the transmitted NPdu is determined by the configured target Communication Connector.
        A None value is a no-op and does not overwrite an existing directTpSduRef.
        """
        if value is not None:
            self.directTpSduRef = value
        return self

    def getMulticastRef(self) -> Optional[RefType]:
        """
        TP address for 1:n connections.
        """
        return self.multicastRef

    def setMulticastRef(self, value: Optional[RefType]) -> FlexrayArTpConnection:
        """
        TP address for 1:n connections.
        A None value is a no-op and does not overwrite an existing multicastRef.
        """
        if value is not None:
            self.multicastRef = value
        return self

    def getReversedTpSduRef(self) -> Optional[RefType]:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction. The source address of the transmitted NPdu is determined by the configured target Communication Connector. The target address of the transmitted NPdu is determined by the configured source Communication Connector.
        """
        return self.reversedTpSduRef

    def setReversedTpSduRef(self, value: Optional[RefType]) -> FlexrayArTpConnection:
        """
        Reference to the IPdu that is segmented by the Transport Protocol. If support of both sending and receiving is used, this association references the IPdu used for the additional second direction. The source address of the transmitted NPdu is determined by the configured target Communication Connector. The target address of the transmitted NPdu is determined by the configured source Communication Connector.
        A None value is a no-op and does not overwrite an existing reversedTpSduRef.
        """
        if value is not None:
            self.reversedTpSduRef = value
        return self

    def getSourceRef(self) -> Optional[RefType]:
        """
        The source of the TP connection.
        """
        return self.sourceRef

    def setSourceRef(self, value: Optional[RefType]) -> FlexrayArTpConnection:
        """
        The source of the TP connection.
        A None value is a no-op and does not overwrite an existing sourceRef.
        """
        if value is not None:
            self.sourceRef = value
        return self

    def addTargetRef(self, value: Optional[RefType]) -> FlexrayArTpConnection:
        """
        The target of the TP connection.
        A None value is a no-op and is not appended to targetRefs.
        """
        if value is not None:
            self.targetRefs.append(value)
        return self

    def getTargetRefs(self) -> List[RefType]:
        """
        The target of the TP connection.
        """
        return self.targetRefs


class EthTpConfig(TpConfig):
    """
    This element defines which PduTriggerings shall be handled using "TP" semantics. Tags: atp.recommendedPackage=TpConfigs
    """

    # EthTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.262, p.617
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpConnections     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Senders and receivers of SOME/IP TP messages.
        self.tpConnections: List[EthTpConnection] = []

    def getTpConnections(self) -> List[EthTpConnection]:
        """
        Senders and receivers of SOME/IP TP messages.
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[EthTpConnection]) -> EthTpConfig:
        """
        Senders and receivers of SOME/IP TP messages.
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self


class EthTpConnection(TpConnection):
    """
    A connection identifies which PduTriggerings shall be handled using the "TP" semantics.
    """

    # EthTpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.263, p.618
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addTpSduRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpSduRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to a PduTriggering that shall be transported using the "TP" semantics.
        self.tpSduRefs: List[RefType] = []

    def addTpSduRef(self, value: Optional[RefType]) -> EthTpConnection:
        """
        Reference to a PduTriggering that shall be transported using the "TP" semantics.
        A None value is a no-op and is not appended to tpSduRefs.
        """
        if value is not None:
            self.tpSduRefs.append(value)
        return self

    def getTpSduRefs(self) -> List[RefType]:
        """
        Reference to a PduTriggering that shall be transported using the "TP" semantics.
        """
        return self.tpSduRefs


class SomeipTpConfig(TpConfig):
    """
    This element defines exactly one SOME/IP TP Configuration. Tags: atp.recommendedPackage=TpConfigs
    """

    # SomeipTpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.264, p.619
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpChannels          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSomeipTpChannel  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnections       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTpConnection        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of SomeipTpChannels that are collecting configuration properties that are valid for a collection of SomeipTpConnections.
        self.tpChannels: List[SomeipTpChannel] = []

        # Senders and receivers of SOME/IP TP messages.
        self.tpConnections: List[SomeipTpConnection] = []

    def getTpChannels(self) -> List[SomeipTpChannel]:
        """
        Definition of SomeipTpChannels that are collecting configuration properties that are valid for a collection of SomeipTpConnections.
        """
        return self.tpChannels

    def createSomeipTpChannel(self, short_name: str) -> SomeipTpChannel:
        """
        Definition of SomeipTpChannels that are collecting configuration properties that are valid for a collection of SomeipTpConnections.
        """
        if not self.IsReferrableElementExists(short_name, SomeipTpChannel):
            channel = SomeipTpChannel(self, short_name)
            self.addReferrableElement(channel)
            self.tpChannels.append(channel)
        return cast(SomeipTpChannel, self.getReferrableElement(short_name, SomeipTpChannel))

    def getTpConnections(self) -> List[SomeipTpConnection]:
        """
        Senders and receivers of SOME/IP TP messages.
        """
        return self.tpConnections

    def addTpConnection(self, value: Optional[SomeipTpConnection]) -> SomeipTpConfig:
        """
        Senders and receivers of SOME/IP TP messages.
        A None value is a no-op and is not appended to tpConnections.
        """
        if value is not None:
            self.tpConnections.append(value)
        return self
