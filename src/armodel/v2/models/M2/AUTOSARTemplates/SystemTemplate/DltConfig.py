from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DltConfig(ARObject):
    """
    This element defines a Dlt configuration for a specific Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::Dlt::DltConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 722, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Ecu representation in the Log And Trace.
        self._dltEcu: Optional["DltEcu"] = None

    @property
    def dlt_ecu(self) -> Optional["DltEcu"]:
        """Get dltEcu (Pythonic accessor)."""
        return self._dltEcu

    @dlt_ecu.setter
    def dlt_ecu(self, value: Optional["DltEcu"]) -> None:
        """
        Set dltEcu with validation.

        Args:
            value: The dltEcu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dltEcu = None
            return

        if not isinstance(value, DltEcu):
            raise TypeError(
                f"dltEcu must be DltEcu or None, got {type(value).__name__}"
            )
        self._dltEcu = value
        # Describes the DltLogChannels that are configured for the output.
        self._dltLogChannel: List["DltLogChannel"] = []

    @property
    def dlt_log_channel(self) -> List["DltLogChannel"]:
        """Get dltLogChannel (Pythonic accessor)."""
        return self._dltLogChannel
        # This attribute defines whether the sessionId is used or.
        self._sessionId: Optional["Boolean"] = None

    @property
    def session_id(self) -> Optional["Boolean"]:
        """Get sessionId (Pythonic accessor)."""
        return self._sessionId

    @session_id.setter
    def session_id(self, value: Optional["Boolean"]) -> None:
        """
        Set sessionId with validation.

        Args:
            value: The sessionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sessionId = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"sessionId must be Boolean or None, got {type(value).__name__}"
            )
        self._sessionId = value
        # This attribute defines whether a timestamp shall be added the Dlt messages or
        # not.
        self._timestamp: Optional["Boolean"] = None

    @property
    def timestamp(self) -> Optional["Boolean"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"timestamp must be Boolean or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltEcu(self) -> "DltEcu":
        """
        AUTOSAR-compliant getter for dltEcu.

        Returns:
            The dltEcu value

        Note:
            Delegates to dlt_ecu property (CODING_RULE_V2_00017)
        """
        return self.dlt_ecu  # Delegates to property

    def setDltEcu(self, value: "DltEcu") -> "DltConfig":
        """
        AUTOSAR-compliant setter for dltEcu with method chaining.

        Args:
            value: The dltEcu to set

        Returns:
            self for method chaining

        Note:
            Delegates to dlt_ecu property setter (gets validation automatically)
        """
        self.dlt_ecu = value  # Delegates to property setter
        return self

    def getDltLogChannel(self) -> List["DltLogChannel"]:
        """
        AUTOSAR-compliant getter for dltLogChannel.

        Returns:
            The dltLogChannel value

        Note:
            Delegates to dlt_log_channel property (CODING_RULE_V2_00017)
        """
        return self.dlt_log_channel  # Delegates to property

    def getSessionId(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for sessionId.

        Returns:
            The sessionId value

        Note:
            Delegates to session_id property (CODING_RULE_V2_00017)
        """
        return self.session_id  # Delegates to property

    def setSessionId(self, value: "Boolean") -> "DltConfig":
        """
        AUTOSAR-compliant setter for sessionId with method chaining.

        Args:
            value: The sessionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to session_id property setter (gets validation automatically)
        """
        self.session_id = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "Boolean") -> "DltConfig":
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

    def with_dlt_ecu(self, value: Optional["DltEcu"]) -> "DltConfig":
        """
        Set dltEcu and return self for chaining.

        Args:
            value: The dltEcu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_ecu("value")
        """
        self.dlt_ecu = value  # Use property setter (gets validation)
        return self

    def with_session_id(self, value: Optional["Boolean"]) -> "DltConfig":
        """
        Set sessionId and return self for chaining.

        Args:
            value: The sessionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_session_id("value")
        """
        self.session_id = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional["Boolean"]) -> "DltConfig":
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
