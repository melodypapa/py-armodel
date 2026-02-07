from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class StreamFilterIEEE1722Tp(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterIEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 139, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match IEEE1722Tp packets with the stream Id as 64bit stream id.
        self._streamId: Optional["PositiveUnlimitedInteger"] = None

    @property
    def stream_id(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get streamId (Pythonic accessor)."""
        return self._streamId

    @stream_id.setter
    def stream_id(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set streamId with validation.

        Args:
            value: The streamId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamId = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"streamId must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._streamId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStreamId(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for streamId.

        Returns:
            The streamId value

        Note:
            Delegates to stream_id property (CODING_RULE_V2_00017)
        """
        return self.stream_id  # Delegates to property

    def setStreamId(self, value: "PositiveUnlimitedInteger") -> "StreamFilterIEEE1722Tp":
        """
        AUTOSAR-compliant setter for streamId with method chaining.

        Args:
            value: The streamId to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_id property setter (gets validation automatically)
        """
        self.stream_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_stream_id(self, value: Optional["PositiveUnlimitedInteger"]) -> "StreamFilterIEEE1722Tp":
        """
        Set streamId and return self for chaining.

        Args:
            value: The streamId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_id("value")
        """
        self.stream_id = value  # Use property setter (gets validation)
        return self
