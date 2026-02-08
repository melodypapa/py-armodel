from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanTpChannel(Identifiable):
    """
    Configuration parameters of the CanTp channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 608, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The id of the channel.
        # The value shall be unique for each.
        self._channelId: Optional["PositiveInteger"] = None

    @property
    def channel_id(self) -> Optional["PositiveInteger"]:
        """Get channelId (Pythonic accessor)."""
        return self._channelId

    @channel_id.setter
    def channel_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set channelId with validation.

        Args:
            value: The channelId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channelId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"channelId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._channelId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChannelId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for channelId.

        Returns:
            The channelId value

        Note:
            Delegates to channel_id property (CODING_RULE_V2_00017)
        """
        return self.channel_id  # Delegates to property

    def setChannelId(self, value: "PositiveInteger") -> "CanTpChannel":
        """
        AUTOSAR-compliant setter for channelId with method chaining.

        Args:
            value: The channelId to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel_id property setter (gets validation automatically)
        """
        self.channel_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_channel_id(self, value: Optional["PositiveInteger"]) -> "CanTpChannel":
        """
        Set channelId and return self for chaining.

        Args:
            value: The channelId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel_id("value")
        """
        self.channel_id = value  # Use property setter (gets validation)
        return self
