from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class BusMirrorChannelMapping(FibexElement, ABC):
    """
    This element defines a bus mirroring in which the traffic from one
    communication bus (sourceChannel) is forwarded to another one
    (targetChannel).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorChannelMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 697, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BusMirrorChannelMapping:
            raise TypeError("BusMirrorChannelMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the bus mirroring protocol that is in the
        # BusMirrorChannelMapping.
        self._mirroring: Optional["MirroringProtocolEnum"] = None

    @property
    def mirroring(self) -> Optional["MirroringProtocolEnum"]:
        """Get mirroring (Pythonic accessor)."""
        return self._mirroring

    @mirroring.setter
    def mirroring(self, value: Optional["MirroringProtocolEnum"]) -> None:
        """
        Set mirroring with validation.
        
        Args:
            value: The mirroring to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirroring = None
            return

        if not isinstance(value, MirroringProtocolEnum):
            raise TypeError(
                f"mirroring must be MirroringProtocolEnum or None, got {type(value).__name__}"
            )
        self._mirroring = value
        # Defines the sourceChannel from which frames are.
        self._sourceChannel: Optional["BusMirrorChannel"] = None

    @property
    def source_channel(self) -> Optional["BusMirrorChannel"]:
        """Get sourceChannel (Pythonic accessor)."""
        return self._sourceChannel

    @source_channel.setter
    def source_channel(self, value: Optional["BusMirrorChannel"]) -> None:
        """
        Set sourceChannel with validation.
        
        Args:
            value: The sourceChannel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceChannel = None
            return

        if not isinstance(value, BusMirrorChannel):
            raise TypeError(
                f"sourceChannel must be BusMirrorChannel or None, got {type(value).__name__}"
            )
        self._sourceChannel = value
        # Defines the targetChannel to which frames are forwarded.
        self._targetChannel: Optional["BusMirrorChannel"] = None

    @property
    def target_channel(self) -> Optional["BusMirrorChannel"]:
        """Get targetChannel (Pythonic accessor)."""
        return self._targetChannel

    @target_channel.setter
    def target_channel(self, value: Optional["BusMirrorChannel"]) -> None:
        """
        Set targetChannel with validation.
        
        Args:
            value: The targetChannel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetChannel = None
            return

        if not isinstance(value, BusMirrorChannel):
            raise TypeError(
                f"targetChannel must be BusMirrorChannel or None, got {type(value).__name__}"
            )
        self._targetChannel = value
        # Reference to the PduTriggering that is used for of the mirrored frames on the
                # targetChannel.
        # that on FlexRay several targetPduTriggerings used.
        # For all other communication channels only targetPduTriggering is supported.
        # atpVariation.
        self._targetPdu: List[RefType] = []

    @property
    def target_pdu(self) -> List[RefType]:
        """Get targetPdu (Pythonic accessor)."""
        return self._targetPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMirroring(self) -> "MirroringProtocolEnum":
        """
        AUTOSAR-compliant getter for mirroring.
        
        Returns:
            The mirroring value
        
        Note:
            Delegates to mirroring property (CODING_RULE_V2_00017)
        """
        return self.mirroring  # Delegates to property

    def setMirroring(self, value: "MirroringProtocolEnum") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for mirroring with method chaining.
        
        Args:
            value: The mirroring to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mirroring property setter (gets validation automatically)
        """
        self.mirroring = value  # Delegates to property setter
        return self

    def getSourceChannel(self) -> "BusMirrorChannel":
        """
        AUTOSAR-compliant getter for sourceChannel.
        
        Returns:
            The sourceChannel value
        
        Note:
            Delegates to source_channel property (CODING_RULE_V2_00017)
        """
        return self.source_channel  # Delegates to property

    def setSourceChannel(self, value: "BusMirrorChannel") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for sourceChannel with method chaining.
        
        Args:
            value: The sourceChannel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_channel property setter (gets validation automatically)
        """
        self.source_channel = value  # Delegates to property setter
        return self

    def getTargetChannel(self) -> "BusMirrorChannel":
        """
        AUTOSAR-compliant getter for targetChannel.
        
        Returns:
            The targetChannel value
        
        Note:
            Delegates to target_channel property (CODING_RULE_V2_00017)
        """
        return self.target_channel  # Delegates to property

    def setTargetChannel(self, value: "BusMirrorChannel") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for targetChannel with method chaining.
        
        Args:
            value: The targetChannel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_channel property setter (gets validation automatically)
        """
        self.target_channel = value  # Delegates to property setter
        return self

    def getTargetPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for targetPdu.
        
        Returns:
            The targetPdu value
        
        Note:
            Delegates to target_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mirroring(self, value: Optional["MirroringProtocolEnum"]) -> "BusMirrorChannelMapping":
        """
        Set mirroring and return self for chaining.
        
        Args:
            value: The mirroring to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mirroring("value")
        """
        self.mirroring = value  # Use property setter (gets validation)
        return self

    def with_source_channel(self, value: Optional["BusMirrorChannel"]) -> "BusMirrorChannelMapping":
        """
        Set sourceChannel and return self for chaining.
        
        Args:
            value: The sourceChannel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_channel("value")
        """
        self.source_channel = value  # Use property setter (gets validation)
        return self

    def with_target_channel(self, value: Optional["BusMirrorChannel"]) -> "BusMirrorChannelMapping":
        """
        Set targetChannel and return self for chaining.
        
        Args:
            value: The targetChannel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_channel("value")
        """
        self.target_channel = value  # Use property setter (gets validation)
        return self