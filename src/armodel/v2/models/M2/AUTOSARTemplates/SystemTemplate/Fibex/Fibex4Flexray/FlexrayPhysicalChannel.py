from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class FlexrayPhysicalChannel(PhysicalChannel):
    """
    FlexRay specific attributes to the physicalChannel
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayPhysicalChannel
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Name of the channel (Channel A or Channel B).
        self._channelName: Optional["FlexrayChannelName"] = None

    @property
    def channel_name(self) -> Optional["FlexrayChannelName"]:
        """Get channelName (Pythonic accessor)."""
        return self._channelName

    @channel_name.setter
    def channel_name(self, value: Optional["FlexrayChannelName"]) -> None:
        """
        Set channelName with validation.
        
        Args:
            value: The channelName to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channelName = None
            return

        if not isinstance(value, FlexrayChannelName):
            raise TypeError(
                f"channelName must be FlexrayChannelName or None, got {type(value).__name__}"
            )
        self._channelName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChannelName(self) -> "FlexrayChannelName":
        """
        AUTOSAR-compliant getter for channelName.
        
        Returns:
            The channelName value
        
        Note:
            Delegates to channel_name property (CODING_RULE_V2_00017)
        """
        return self.channel_name  # Delegates to property

    def setChannelName(self, value: "FlexrayChannelName") -> "FlexrayPhysicalChannel":
        """
        AUTOSAR-compliant setter for channelName with method chaining.
        
        Args:
            value: The channelName to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to channel_name property setter (gets validation automatically)
        """
        self.channel_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_channel_name(self, value: Optional["FlexrayChannelName"]) -> "FlexrayPhysicalChannel":
        """
        Set channelName and return self for chaining.
        
        Args:
            value: The channelName to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_channel_name("value")
        """
        self.channel_name = value  # Use property setter (gets validation)
        return self