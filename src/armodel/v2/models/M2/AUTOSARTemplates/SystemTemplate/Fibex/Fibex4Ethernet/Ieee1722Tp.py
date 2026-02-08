from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TransportProtocolConfiguration,
)


class Ieee1722Tp(TransportProtocolConfiguration):
    """
    Content Model for IEEE 1722 configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the time when content shall be presented (in The actual absolute time
                # is creation time plus presentation time.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._relative: Optional["TimeValue"] = None

    @property
    def relative(self) -> Optional["TimeValue"]:
        """Get relative (Pythonic accessor)."""
        return self._relative

    @relative.setter
    def relative(self, value: Optional["TimeValue"]) -> None:
        """
        Set relative with validation.

        Args:
            value: The relative to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._relative = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"relative must be TimeValue or None, got {type(value).__name__}"
            )
        self._relative = value
        # IEEE 1722 stream identifier.
        self._streamIdentifier: Optional["PositiveInteger"] = None

    @property
    def stream_identifier(self) -> Optional["PositiveInteger"]:
        """Get streamIdentifier (Pythonic accessor)."""
        return self._streamIdentifier

    @stream_identifier.setter
    def stream_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set streamIdentifier with validation.

        Args:
            value: The streamIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamIdentifier = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"streamIdentifier must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._streamIdentifier = value
        # Protocol type.
        self._subType: Optional["PositiveInteger"] = None

    @property
    def sub_type(self) -> Optional["PositiveInteger"]:
        """Get subType (Pythonic accessor)."""
        return self._subType

    @sub_type.setter
    def sub_type(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set subType with validation.

        Args:
            value: The subType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subType = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"subType must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._subType = value
        # Revision of Ieee1722 standard.
        self._version: Optional["PositiveInteger"] = None

    @property
    def version(self) -> Optional["PositiveInteger"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"version must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRelative(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for relative.

        Returns:
            The relative value

        Note:
            Delegates to relative property (CODING_RULE_V2_00017)
        """
        return self.relative  # Delegates to property

    def setRelative(self, value: "TimeValue") -> "Ieee1722Tp":
        """
        AUTOSAR-compliant setter for relative with method chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Note:
            Delegates to relative property setter (gets validation automatically)
        """
        self.relative = value  # Delegates to property setter
        return self

    def getStreamIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for streamIdentifier.

        Returns:
            The streamIdentifier value

        Note:
            Delegates to stream_identifier property (CODING_RULE_V2_00017)
        """
        return self.stream_identifier  # Delegates to property

    def setStreamIdentifier(self, value: "PositiveInteger") -> "Ieee1722Tp":
        """
        AUTOSAR-compliant setter for streamIdentifier with method chaining.

        Args:
            value: The streamIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_identifier property setter (gets validation automatically)
        """
        self.stream_identifier = value  # Delegates to property setter
        return self

    def getSubType(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for subType.

        Returns:
            The subType value

        Note:
            Delegates to sub_type property (CODING_RULE_V2_00017)
        """
        return self.sub_type  # Delegates to property

    def setSubType(self, value: "PositiveInteger") -> "Ieee1722Tp":
        """
        AUTOSAR-compliant setter for subType with method chaining.

        Args:
            value: The subType to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_type property setter (gets validation automatically)
        """
        self.sub_type = value  # Delegates to property setter
        return self

    def getVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "PositiveInteger") -> "Ieee1722Tp":
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_relative(self, value: Optional["TimeValue"]) -> "Ieee1722Tp":
        """
        Set relative and return self for chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_relative("value")
        """
        self.relative = value  # Use property setter (gets validation)
        return self

    def with_stream_identifier(self, value: Optional["PositiveInteger"]) -> "Ieee1722Tp":
        """
        Set streamIdentifier and return self for chaining.

        Args:
            value: The streamIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_identifier("value")
        """
        self.stream_identifier = value  # Use property setter (gets validation)
        return self

    def with_sub_type(self, value: Optional["PositiveInteger"]) -> "Ieee1722Tp":
        """
        Set subType and return self for chaining.

        Args:
            value: The subType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_type("value")
        """
        self.sub_type = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["PositiveInteger"]) -> "Ieee1722Tp":
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self
