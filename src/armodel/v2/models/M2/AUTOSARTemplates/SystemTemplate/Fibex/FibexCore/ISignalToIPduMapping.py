from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ISignalToIPduMapping(Identifiable):
    """
    that the exact bit position of the updateIndicationBit Position is linked to
    the value of the attribute packingByte Order because the method of finding
    the bit position is different for the values mostSignificantByteFirst and
    most SignificantByteLast. This means that if the value of packingByteOrder
    is changed while the value of update IndicationBitPosition remains unchanged
    the exact bit position of updateIndicationBitPosition within the enclosing
    ISignalIPdu still undergoes a change. This attribute denotes the least
    significant bit for "Little Endian" and the most significant bit for "Big
    Endian" packed signals within the IPdu (see the description of the
    packingByteOrder attribute). In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. Table 6.14: ISignalToIPduMapping [constr_5322] Value
    range of ISignalToIPduMapping.startPosition (cid:100)The value of
    ISignalToIPduMapping.startPosition shall be in the range of 0..4294967295
    Bits.(cid:99)() Please note that the range of
    ISignalToIPduMapping.startPosition is resc- tricted by [constr_5322] to the
    max value of 4294967295 Bits because of the de- fined range of the
    ComBitPosition parameter that is defined in the COM Config- uration [21].
    [constr_5323] Value range of ISignalToIPduMapping.updateIndicationBit-
    Position (cid:100)The value of ISignalToIPduMapping.updateIndicationBitPosi-
    tion shall be in the range of 0..4294967295 Bits.(cid:99)() Please note that
    the range of ISignalToIPduMapping.updateIndicationBit- Position is
    resctricted by [constr_5323] to the max value of 4294967295 Bits be- cause
    of the defined range of the ComUpdateBitPosition parameter that is defined
    in the COM Configuration [21]. [constr_3514] No two ISignalToIPduMappings
    shall reference the identical ISignal (cid:100)No two ISignalToIPduMappings
    shall reference the identical ISignal in the role iSignal in the scope of
    one System.(cid:99)() 326 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalToIPduMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 325, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a ISignal that is mapped into the ISignal contained in the
                # ISignalGroup shall be an IPdu by an own ISignalToIPduMapping.
        # to the ISignal and to the ISignalGroup in are mutually exclusive.
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.
        
        Args:
            value: The iSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        # Reference to an ISignalGroup that is mapped into the an ISignalToIPduMapping
                # for an ISignal defined, only the UpdateIndicationBitPosition transferProperty
                # is relevant.
        # The startPosition packingByteOrder shall be ignored.
        # contained in the ISignalGroup shall be an IPdu by an own
                # ISignalToIPduMapping.
        # to the ISignal and to the ISignalGroup in are mutually exclusive.
        self._iSignalGroup: RefType = None

    @property
    def i_signal_group(self) -> RefType:
        """Get iSignalGroup (Pythonic accessor)."""
        return self._iSignalGroup

    @i_signal_group.setter
    def i_signal_group(self, value: RefType) -> None:
        """
        Set iSignalGroup with validation.
        
        Args:
            value: The iSignalGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalGroup = None
            return

        self._iSignalGroup = value
        # This parameter defines the order of the bytes of the signal the packing into
                # the SignalIPdu.
        # The byte ordering (MostSignificantByteLast), "Big Endian" "Opaque" can be
                # selected.
        # data endianness conversion shall be Opaque.
        # The value of this attribute impacts position of the signal into the
                # SignalIPdu startPosition attribute description).
        # ISignalGroup the packingByteOrder is irrelevant be ignored.
        self._packingByte: Optional["ByteOrderEnum"] = None

    @property
    def packing_byte(self) -> Optional["ByteOrderEnum"]:
        """Get packingByte (Pythonic accessor)."""
        return self._packingByte

    @packing_byte.setter
    def packing_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set packingByte with validation.
        
        Args:
            value: The packingByte to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packingByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"packingByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._packingByte = value
        # This parameter is necessary to describe the bitposition of within an
                # SignalIPdu.
        # It denotes the least for "Little Endian" and the most significant "Big
                # Endian" packed signals within the IPdu (see of the packingByteOrder
                # attribute).
        # In bit counting is always set to "sawtooth" bit order is set to "Decreasing".
        # The bit counting 0 starts with bit 0 (least significant bit).
        # The most in byte 0 is bit 7.
        # that the way the bytes will be actually sent on does not impact this
                # representation: they will seen by the software as a byte array.
        # mapping for the ISignalGroup is defined, this attribute and shall be ignored.
        self._startPosition: Optional["UnlimitedInteger"] = None

    @property
    def start_position(self) -> Optional["UnlimitedInteger"]:
        """Get startPosition (Pythonic accessor)."""
        return self._startPosition

    @start_position.setter
    def start_position(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set startPosition with validation.
        
        Args:
            value: The startPosition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startPosition = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"startPosition must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._startPosition = value
        # Defines how the referenced ISignal contributes to the of the ISignalIPdu.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._transferProperty: Optional["TransferPropertyEnum"] = None

    @property
    def transfer_property(self) -> Optional["TransferPropertyEnum"]:
        """Get transferProperty (Pythonic accessor)."""
        return self._transferProperty

    @transfer_property.setter
    def transfer_property(self, value: Optional["TransferPropertyEnum"]) -> None:
        """
        Set transferProperty with validation.
        
        Args:
            value: The transferProperty to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transferProperty = None
            return

        if not isinstance(value, TransferPropertyEnum):
            raise TypeError(
                f"transferProperty must be TransferPropertyEnum or None, got {type(value).__name__}"
            )
        self._transferProperty = value
        # The UpdateIndicationBit indicates to the receivers that the (or the signal
                # group) was updated by the sender.
        # is always one bit.
        # The UpdateIndicationBitPosition the position of the update bit within the
                # Signals of a ISignalGroup this attribute is shall be ignored.
        self._update: Optional["UnlimitedInteger"] = None

    @property
    def update(self) -> Optional["UnlimitedInteger"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set update with validation.
        
        Args:
            value: The update to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"update must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> "ISignal":
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: "ISignal") -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for iSignal with method chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    def getISignalGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for iSignalGroup.
        
        Returns:
            The iSignalGroup value
        
        Note:
            Delegates to i_signal_group property (CODING_RULE_V2_00017)
        """
        return self.i_signal_group  # Delegates to property

    def setISignalGroup(self, value: RefType) -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for iSignalGroup with method chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal_group property setter (gets validation automatically)
        """
        self.i_signal_group = value  # Delegates to property setter
        return self

    def getPackingByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for packingByte.
        
        Returns:
            The packingByte value
        
        Note:
            Delegates to packing_byte property (CODING_RULE_V2_00017)
        """
        return self.packing_byte  # Delegates to property

    def setPackingByte(self, value: "ByteOrderEnum") -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for packingByte with method chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to packing_byte property setter (gets validation automatically)
        """
        self.packing_byte = value  # Delegates to property setter
        return self

    def getStartPosition(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for startPosition.
        
        Returns:
            The startPosition value
        
        Note:
            Delegates to start_position property (CODING_RULE_V2_00017)
        """
        return self.start_position  # Delegates to property

    def setStartPosition(self, value: "UnlimitedInteger") -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for startPosition with method chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to start_position property setter (gets validation automatically)
        """
        self.start_position = value  # Delegates to property setter
        return self

    def getTransferProperty(self) -> "TransferPropertyEnum":
        """
        AUTOSAR-compliant getter for transferProperty.
        
        Returns:
            The transferProperty value
        
        Note:
            Delegates to transfer_property property (CODING_RULE_V2_00017)
        """
        return self.transfer_property  # Delegates to property

    def setTransferProperty(self, value: "TransferPropertyEnum") -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for transferProperty with method chaining.
        
        Args:
            value: The transferProperty to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transfer_property property setter (gets validation automatically)
        """
        self.transfer_property = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for update.
        
        Returns:
            The update value
        
        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "UnlimitedInteger") -> "ISignalToIPduMapping":
        """
        AUTOSAR-compliant setter for update with method chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional["ISignal"]) -> "ISignalToIPduMapping":
        """
        Set iSignal and return self for chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_i_signal_group(self, value: Optional[RefType]) -> "ISignalToIPduMapping":
        """
        Set iSignalGroup and return self for chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal_group("value")
        """
        self.i_signal_group = value  # Use property setter (gets validation)
        return self

    def with_packing_byte(self, value: Optional["ByteOrderEnum"]) -> "ISignalToIPduMapping":
        """
        Set packingByte and return self for chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_packing_byte("value")
        """
        self.packing_byte = value  # Use property setter (gets validation)
        return self

    def with_start_position(self, value: Optional["UnlimitedInteger"]) -> "ISignalToIPduMapping":
        """
        Set startPosition and return self for chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_start_position("value")
        """
        self.start_position = value  # Use property setter (gets validation)
        return self

    def with_transfer_property(self, value: Optional["TransferPropertyEnum"]) -> "ISignalToIPduMapping":
        """
        Set transferProperty and return self for chaining.
        
        Args:
            value: The transferProperty to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transfer_property("value")
        """
        self.transfer_property = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["UnlimitedInteger"]) -> "ISignalToIPduMapping":
        """
        Set update and return self for chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self