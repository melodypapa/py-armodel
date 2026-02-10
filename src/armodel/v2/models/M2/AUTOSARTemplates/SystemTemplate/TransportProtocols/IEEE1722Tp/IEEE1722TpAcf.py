"""
AUTOSAR Package - IEEE1722TpAcf

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class IEEE1722TpAcfBus(Identifiable, ABC):
    """
    Abstract class to define various busses to be transported over a IEEE1722TP
    ACF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfBus

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 657, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAcfBus:
            raise TypeError("IEEE1722TpAcfBus is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One part transported over IEEE1722Tp channel.
        # atpVariation.
        self._acfPart: List["IEEE1722TpAcfBusPart"] = []

    @property
    def acf_part(self) -> List["IEEE1722TpAcfBusPart"]:
        """Get acfPart (Pythonic accessor)."""
        return self._acfPart
        # Id of the transported bus over the ACF connection.
        self._busId: Optional["PositiveInteger"] = None

    @property
    def bus_id(self) -> Optional["PositiveInteger"]:
        """Get busId (Pythonic accessor)."""
        return self._busId

    @bus_id.setter
    def bus_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set busId with validation.

        Args:
            value: The busId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"busId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._busId = value

    def with_acf_part(self, value):
        """
        Set acf_part and return self for chaining.

        Args:
            value: The acf_part to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acf_part("value")
        """
        self.acf_part = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcfPart(self) -> List["IEEE1722TpAcfBusPart"]:
        """
        AUTOSAR-compliant getter for acfPart.

        Returns:
            The acfPart value

        Note:
            Delegates to acf_part property (CODING_RULE_V2_00017)
        """
        return self.acf_part  # Delegates to property

    def getBusId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for busId.

        Returns:
            The busId value

        Note:
            Delegates to bus_id property (CODING_RULE_V2_00017)
        """
        return self.bus_id  # Delegates to property

    def setBusId(self, value: "PositiveInteger") -> "IEEE1722TpAcfBus":
        """
        AUTOSAR-compliant setter for busId with method chaining.

        Args:
            value: The busId to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_id property setter (gets validation automatically)
        """
        self.bus_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_id(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfBus":
        """
        Set busId and return self for chaining.

        Args:
            value: The busId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_id("value")
        """
        self.bus_id = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAcfBusPart(Identifiable, ABC):
    """
    Definition of one IEEE1722Tp ACF part transported over the IEEE1722Tp
    channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfBusPart

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 657, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAcfBusPart:
            raise TypeError("IEEE1722TpAcfBusPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether putting this AcfPart to the IEEE1722Tp message triggers
        # immediate sending of the message.
        self._collectionTrigger: Optional["RefType"] = None

    @property
    def collection_trigger(self) -> Optional["RefType"]:
        """Get collectionTrigger (Pythonic accessor)."""
        return self._collectionTrigger

    @collection_trigger.setter
    def collection_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set collectionTrigger with validation.

        Args:
            value: The collectionTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collectionTrigger = None
            return

        self._collectionTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollectionTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for collectionTrigger.

        Returns:
            The collectionTrigger value

        Note:
            Delegates to collection_trigger property (CODING_RULE_V2_00017)
        """
        return self.collection_trigger  # Delegates to property

    def setCollectionTrigger(self, value: "RefType") -> "IEEE1722TpAcfBusPart":
        """
        AUTOSAR-compliant setter for collectionTrigger with method chaining.

        Args:
            value: The collectionTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to collection_trigger property setter (gets validation automatically)
        """
        self.collection_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection_trigger(self, value: Optional[RefType]) -> "IEEE1722TpAcfBusPart":
        """
        Set collectionTrigger and return self for chaining.

        Args:
            value: The collectionTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collection_trigger("value")
        """
        self.collection_trigger = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """
    ACF IEEE1722Tp bus used for CAN transport.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfCan

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 661, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the ACF CAN stream message type.
        self._messageTypeMessageTypeEnum: Optional["IEEE1722TpAcfCan"] = None

    @property
    def message_type_message_type_enum(self) -> Optional["IEEE1722TpAcfCan"]:
        """Get messageTypeMessageTypeEnum (Pythonic accessor)."""
        return self._messageTypeMessageTypeEnum

    @message_type_message_type_enum.setter
    def message_type_message_type_enum(self, value: Optional["IEEE1722TpAcfCan"]) -> None:
        """
        Set messageTypeMessageTypeEnum with validation.

        Args:
            value: The messageTypeMessageTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageTypeMessageTypeEnum = None
            return

        if not isinstance(value, IEEE1722TpAcfCan):
            raise TypeError(
                f"messageTypeMessageTypeEnum must be IEEE1722TpAcfCan or None, got {type(value).__name__}"
            )
        self._messageTypeMessageTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMessageTypeMessageTypeEnum(self) -> "IEEE1722TpAcfCan":
        """
        AUTOSAR-compliant getter for messageTypeMessageTypeEnum.

        Returns:
            The messageTypeMessageTypeEnum value

        Note:
            Delegates to message_type_message_type_enum property (CODING_RULE_V2_00017)
        """
        return self.message_type_message_type_enum  # Delegates to property

    def setMessageTypeMessageTypeEnum(self, value: "IEEE1722TpAcfCan") -> "IEEE1722TpAcfCan":
        """
        AUTOSAR-compliant setter for messageTypeMessageTypeEnum with method chaining.

        Args:
            value: The messageTypeMessageTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_type_message_type_enum property setter (gets validation automatically)
        """
        self.message_type_message_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_message_type_message_type_enum(self, value: Optional["IEEE1722TpAcfCan"]) -> "IEEE1722TpAcfCan":
        """
        Set messageTypeMessageTypeEnum and return self for chaining.

        Args:
            value: The messageTypeMessageTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_type_message_type_enum("value")
        """
        self.message_type_message_type_enum = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    """
    ACF IEEE1722Tp bus used for LIN transport.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfLin

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 666, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CRF base frequency in Hz.
        self._baseFrequency: Optional["PositiveInteger"] = None

    @property
    def base_frequency(self) -> Optional["PositiveInteger"]:
        """Get baseFrequency (Pythonic accessor)."""
        return self._baseFrequency

    @base_frequency.setter
    def base_frequency(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set baseFrequency with validation.

        Args:
            value: The baseFrequency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseFrequency = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"baseFrequency must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._baseFrequency = value
        self._frameSync: Optional["Boolean"] = None

    @property
    def frame_sync(self) -> Optional["Boolean"]:
        """Get frameSync (Pythonic accessor)."""
        return self._frameSync

    @frame_sync.setter
    def frame_sync(self, value: Optional["Boolean"]) -> None:
        """
        Set frameSync with validation.

        Args:
            value: The frameSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameSync = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"frameSync must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._frameSync = value
        self._timestamp: Optional["PositiveInteger"] = None

    @property
    def timestamp(self) -> Optional["PositiveInteger"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timestamp with validation.

        Args:
            value: The timestamp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timestamp must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseFrequency(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for baseFrequency.

        Returns:
            The baseFrequency value

        Note:
            Delegates to base_frequency property (CODING_RULE_V2_00017)
        """
        return self.base_frequency  # Delegates to property

    def setBaseFrequency(self, value: "PositiveInteger") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for baseFrequency with method chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_frequency property setter (gets validation automatically)
        """
        self.base_frequency = value  # Delegates to property setter
        return self

    def getFrameSync(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for frameSync.

        Returns:
            The frameSync value

        Note:
            Delegates to frame_sync property (CODING_RULE_V2_00017)
        """
        return self.frame_sync  # Delegates to property

    def setFrameSync(self, value: "Boolean") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for frameSync with method chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_sync property setter (gets validation automatically)
        """
        self.frame_sync = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "PositiveInteger") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_frequency(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLin":
        """
        Set baseFrequency and return self for chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_frequency("value")
        """
        self.base_frequency = value  # Use property setter (gets validation)
        return self

    def with_frame_sync(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfLin":
        """
        Set frameSync and return self for chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_sync("value")
        """
        self.frame_sync = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLin":
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """
    Definition of one CAN part (frame or frame range) transported over the
    IEEE1722Tp channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfCanPart

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 661, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether standard or extended address format shall be used.
        self._canAddressing: Optional["CanAddressingMode"] = None

    @property
    def can_addressing(self) -> Optional["CanAddressingMode"]:
        """Get canAddressing (Pythonic accessor)."""
        return self._canAddressing

    @can_addressing.setter
    def can_addressing(self, value: Optional["CanAddressingMode"]) -> None:
        """
        Set canAddressing with validation.

        Args:
            value: The canAddressing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canAddressing = None
            return

        if not isinstance(value, CanAddressingMode):
            raise TypeError(
                f"canAddressing must be CanAddressingMode or None, got {type(value).__name__}"
            )
        self._canAddressing = value
        self._canBitRate: Optional["Boolean"] = None

    @property
    def can_bit_rate(self) -> Optional["Boolean"]:
        """Get canBitRate (Pythonic accessor)."""
        return self._canBitRate

    @can_bit_rate.setter
    def can_bit_rate(self, value: Optional["Boolean"]) -> None:
        """
        Set canBitRate with validation.

        Args:
            value: The canBitRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canBitRate = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"canBitRate must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._canBitRate = value
        self._canFrameTx: Optional["CanFrameTxBehavior"] = None

    @property
    def can_frame_tx(self) -> Optional["CanFrameTxBehavior"]:
        """Get canFrameTx (Pythonic accessor)."""
        return self._canFrameTx

    @can_frame_tx.setter
    def can_frame_tx(self, value: Optional["CanFrameTxBehavior"]) -> None:
        """
        Set canFrameTx with validation.

        Args:
            value: The canFrameTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canFrameTx = None
            return

        if not isinstance(value, CanFrameTxBehavior):
            raise TypeError(
                f"canFrameTx must be CanFrameTxBehavior or None, got {type(value).__name__}"
            )
        self._canFrameTx = value
        self._canIdentifier: Optional["RxIdentifierRange"] = None

    @property
    def can_identifier(self) -> Optional["RxIdentifierRange"]:
        """Get canIdentifier (Pythonic accessor)."""
        return self._canIdentifier

    @can_identifier.setter
    def can_identifier(self, value: Optional["RxIdentifierRange"]) -> None:
        """
        Set canIdentifier with validation.

        Args:
            value: The canIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canIdentifier = None
            return

        if not isinstance(value, RxIdentifierRange):
            raise TypeError(
                f"canIdentifier must be RxIdentifierRange or None, got {type(value).__name__}"
            )
        self._canIdentifier = value
        self._sdu: Optional["RefType"] = None

    @property
    def sdu(self) -> Optional["RefType"]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    @sdu.setter
    def sdu(self, value: Optional["RefType"]) -> None:
        """
        Set sdu with validation.

        Args:
            value: The sdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdu = None
            return

        self._sdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanAddressing(self) -> "CanAddressingMode":
        """
        AUTOSAR-compliant getter for canAddressing.

        Returns:
            The canAddressing value

        Note:
            Delegates to can_addressing property (CODING_RULE_V2_00017)
        """
        return self.can_addressing  # Delegates to property

    def setCanAddressing(self, value: "CanAddressingMode") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canAddressing with method chaining.

        Args:
            value: The canAddressing to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_addressing property setter (gets validation automatically)
        """
        self.can_addressing = value  # Delegates to property setter
        return self

    def getCanBitRate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for canBitRate.

        Returns:
            The canBitRate value

        Note:
            Delegates to can_bit_rate property (CODING_RULE_V2_00017)
        """
        return self.can_bit_rate  # Delegates to property

    def setCanBitRate(self, value: "Boolean") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canBitRate with method chaining.

        Args:
            value: The canBitRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_bit_rate property setter (gets validation automatically)
        """
        self.can_bit_rate = value  # Delegates to property setter
        return self

    def getCanFrameTx(self) -> "CanFrameTxBehavior":
        """
        AUTOSAR-compliant getter for canFrameTx.

        Returns:
            The canFrameTx value

        Note:
            Delegates to can_frame_tx property (CODING_RULE_V2_00017)
        """
        return self.can_frame_tx  # Delegates to property

    def setCanFrameTx(self, value: "CanFrameTxBehavior") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canFrameTx with method chaining.

        Args:
            value: The canFrameTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_frame_tx property setter (gets validation automatically)
        """
        self.can_frame_tx = value  # Delegates to property setter
        return self

    def getCanIdentifier(self) -> "RxIdentifierRange":
        """
        AUTOSAR-compliant getter for canIdentifier.

        Returns:
            The canIdentifier value

        Note:
            Delegates to can_identifier property (CODING_RULE_V2_00017)
        """
        return self.can_identifier  # Delegates to property

    def setCanIdentifier(self, value: "RxIdentifierRange") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canIdentifier with method chaining.

        Args:
            value: The canIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_identifier property setter (gets validation automatically)
        """
        self.can_identifier = value  # Delegates to property setter
        return self

    def getSdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    def setSdu(self, value: "RefType") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for sdu with method chaining.

        Args:
            value: The sdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdu property setter (gets validation automatically)
        """
        self.sdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_addressing(self, value: Optional["CanAddressingMode"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canAddressing and return self for chaining.

        Args:
            value: The canAddressing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_addressing("value")
        """
        self.can_addressing = value  # Use property setter (gets validation)
        return self

    def with_can_bit_rate(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canBitRate and return self for chaining.

        Args:
            value: The canBitRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_bit_rate("value")
        """
        self.can_bit_rate = value  # Use property setter (gets validation)
        return self

    def with_can_frame_tx(self, value: Optional["CanFrameTxBehavior"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canFrameTx and return self for chaining.

        Args:
            value: The canFrameTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_frame_tx("value")
        """
        self.can_frame_tx = value  # Use property setter (gets validation)
        return self

    def with_can_identifier(self, value: Optional["RxIdentifierRange"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canIdentifier and return self for chaining.

        Args:
            value: The canIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_identifier("value")
        """
        self.can_identifier = value  # Use property setter (gets validation)
        return self

    def with_sdu(self, value: Optional[RefType]) -> "IEEE1722TpAcfCanPart":
        """
        Set sdu and return self for chaining.

        Args:
            value: The sdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdu("value")
        """
        self.sdu = value  # Use property setter (gets validation)
        return self



class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """
    Definition of one LIN part transported over the IEEE1722Tp channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfLinPart

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 667, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional Lin Id defined in case the Lin Id can not be runtime.
        self._linIdentifier: Optional["PositiveInteger"] = None

    @property
    def lin_identifier(self) -> Optional["PositiveInteger"]:
        """Get linIdentifier (Pythonic accessor)."""
        return self._linIdentifier

    @lin_identifier.setter
    def lin_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set linIdentifier with validation.

        Args:
            value: The linIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"linIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._linIdentifier = value
        self._sdu: Optional["RefType"] = None

    @property
    def sdu(self) -> Optional["RefType"]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    @sdu.setter
    def sdu(self, value: Optional["RefType"]) -> None:
        """
        Set sdu with validation.

        Args:
            value: The sdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdu = None
            return

        self._sdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLinIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for linIdentifier.

        Returns:
            The linIdentifier value

        Note:
            Delegates to lin_identifier property (CODING_RULE_V2_00017)
        """
        return self.lin_identifier  # Delegates to property

    def setLinIdentifier(self, value: "PositiveInteger") -> "IEEE1722TpAcfLinPart":
        """
        AUTOSAR-compliant setter for linIdentifier with method chaining.

        Args:
            value: The linIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_identifier property setter (gets validation automatically)
        """
        self.lin_identifier = value  # Delegates to property setter
        return self

    def getSdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    def setSdu(self, value: "RefType") -> "IEEE1722TpAcfLinPart":
        """
        AUTOSAR-compliant setter for sdu with method chaining.

        Args:
            value: The sdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdu property setter (gets validation automatically)
        """
        self.sdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lin_identifier(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLinPart":
        """
        Set linIdentifier and return self for chaining.

        Args:
            value: The linIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_identifier("value")
        """
        self.lin_identifier = value  # Use property setter (gets validation)
        return self

    def with_sdu(self, value: Optional[RefType]) -> "IEEE1722TpAcfLinPart":
        """
        Set sdu and return self for chaining.

        Args:
            value: The sdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdu("value")
        """
        self.sdu = value  # Use property setter (gets validation)
        return self


class IEEE1722TpAcfCanMessageTypeEnum(AREnum):
    """
    IEEE1722TpAcfCanMessageTypeEnum enumeration

Definition of the ACF CAN stream message type. Tags: atp.Status=candidate Aggregated by IEEE1722TpAcfCan.messageType

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf
    """
    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Defines the ACF CAN stream to use the ACF_CAN message type.
    can = "0"

    # Defines the ACF CAN stream to use the ACF_CAN_BRIEF message type.
    canBrief = "1"
