from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAvConnection


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp CRF connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv::IEEE1722TpCrfConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 640, Classic Platform R23-11)
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"baseFrequency must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._baseFrequency = value
        # Definition of the CRF stream pull value.
        self._crfPullEnum: Optional["IEEE1722TpCrfPull"] = None

    @property
    def crf_pull_enum(self) -> Optional["IEEE1722TpCrfPull"]:
        """Get crfPullEnum (Pythonic accessor)."""
        return self._crfPullEnum

    @crf_pull_enum.setter
    def crf_pull_enum(self, value: Optional["IEEE1722TpCrfPull"]) -> None:
        """
        Set crfPullEnum with validation.

        Args:
            value: The crfPullEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crfPullEnum = None
            return

        if not isinstance(value, IEEE1722TpCrfPull):
            raise TypeError(
                f"crfPullEnum must be IEEE1722TpCrfPull or None, got {type(value).__name__}"
            )
        self._crfPullEnum = value
        # Definition of the CRF stream type.
        self._crfTypeEnum: Optional["IEEE1722TpCrfType"] = None

    @property
    def crf_type_enum(self) -> Optional["IEEE1722TpCrfType"]:
        """Get crfTypeEnum (Pythonic accessor)."""
        return self._crfTypeEnum

    @crf_type_enum.setter
    def crf_type_enum(self, value: Optional["IEEE1722TpCrfType"]) -> None:
        """
        Set crfTypeEnum with validation.

        Args:
            value: The crfTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crfTypeEnum = None
            return

        if not isinstance(value, IEEE1722TpCrfType):
            raise TypeError(
                f"crfTypeEnum must be IEEE1722TpCrfType or None, got {type(value).__name__}"
            )
        self._crfTypeEnum = value
        # Defines whether the "fs" (frame sync) shall be enabled.
        # atp.
        # Status=candidate.
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"frameSync must be Boolean or None, got {type(value).__name__}"
            )
        self._frameSync = value
        # CRF timestamp interval as multiple of the baseFrequency.
        # atp.
        # Status=candidate.
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timestamp must be PositiveInteger or None, got {type(value).__name__}"
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

    def setBaseFrequency(self, value: "PositiveInteger") -> "IEEE1722TpCrfConnection":
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

    def getCrfPullEnum(self) -> "IEEE1722TpCrfPull":
        """
        AUTOSAR-compliant getter for crfPullEnum.

        Returns:
            The crfPullEnum value

        Note:
            Delegates to crf_pull_enum property (CODING_RULE_V2_00017)
        """
        return self.crf_pull_enum  # Delegates to property

    def setCrfPullEnum(self, value: "IEEE1722TpCrfPull") -> "IEEE1722TpCrfConnection":
        """
        AUTOSAR-compliant setter for crfPullEnum with method chaining.

        Args:
            value: The crfPullEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to crf_pull_enum property setter (gets validation automatically)
        """
        self.crf_pull_enum = value  # Delegates to property setter
        return self

    def getCrfTypeEnum(self) -> "IEEE1722TpCrfType":
        """
        AUTOSAR-compliant getter for crfTypeEnum.

        Returns:
            The crfTypeEnum value

        Note:
            Delegates to crf_type_enum property (CODING_RULE_V2_00017)
        """
        return self.crf_type_enum  # Delegates to property

    def setCrfTypeEnum(self, value: "IEEE1722TpCrfType") -> "IEEE1722TpCrfConnection":
        """
        AUTOSAR-compliant setter for crfTypeEnum with method chaining.

        Args:
            value: The crfTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to crf_type_enum property setter (gets validation automatically)
        """
        self.crf_type_enum = value  # Delegates to property setter
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

    def setFrameSync(self, value: "Boolean") -> "IEEE1722TpCrfConnection":
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

    def setTimestamp(self, value: "PositiveInteger") -> "IEEE1722TpCrfConnection":
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

    def with_base_frequency(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpCrfConnection":
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

    def with_crf_pull_enum(self, value: Optional["IEEE1722TpCrfPull"]) -> "IEEE1722TpCrfConnection":
        """
        Set crfPullEnum and return self for chaining.

        Args:
            value: The crfPullEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crf_pull_enum("value")
        """
        self.crf_pull_enum = value  # Use property setter (gets validation)
        return self

    def with_crf_type_enum(self, value: Optional["IEEE1722TpCrfType"]) -> "IEEE1722TpCrfConnection":
        """
        Set crfTypeEnum and return self for chaining.

        Args:
            value: The crfTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crf_type_enum("value")
        """
        self.crf_type_enum = value  # Use property setter (gets validation)
        return self

    def with_frame_sync(self, value: Optional["Boolean"]) -> "IEEE1722TpCrfConnection":
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

    def with_timestamp(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpCrfConnection":
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
