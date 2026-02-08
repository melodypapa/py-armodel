from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import GlobalTimeMaster


class GlobalTimeEthMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for Ethernet
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::GlobalTimeEthMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 866, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not CRC is supported.
        # This is relevant for selected bus systems.
        self._crcSecured: Optional["GlobalTimeCrcSupport"] = None

    @property
    def crc_secured(self) -> Optional["GlobalTimeCrcSupport"]:
        """Get crcSecured (Pythonic accessor)."""
        return self._crcSecured

    @crc_secured.setter
    def crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> None:
        """
        Set crcSecured with validation.

        Args:
            value: The crcSecured to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSecured = None
            return

        if not isinstance(value, GlobalTimeCrcSupport):
            raise TypeError(
                f"crcSecured must be GlobalTimeCrcSupport or None, got {type(value).__name__}"
            )
        self._crcSecured = value
        # This attribute defines the timeout for transmission of Sync messages on
        # Master ports in absence of Sync and Follow_Up messages on Slave.
        self._holdOverTime: Optional["TimeValue"] = None

    @property
    def hold_over_time(self) -> Optional["TimeValue"]:
        """Get holdOverTime (Pythonic accessor)."""
        return self._holdOverTime

    @hold_over_time.setter
    def hold_over_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set holdOverTime with validation.

        Args:
            value: The holdOverTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._holdOverTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"holdOverTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._holdOverTime = value
        # Defines the subTLV fields which shall be included in the message.
        self._subTlvConfig: Optional["EthTSynSubTlvConfig"] = None

    @property
    def sub_tlv_config(self) -> Optional["EthTSynSubTlvConfig"]:
        """Get subTlvConfig (Pythonic accessor)."""
        return self._subTlvConfig

    @sub_tlv_config.setter
    def sub_tlv_config(self, value: Optional["EthTSynSubTlvConfig"]) -> None:
        """
        Set subTlvConfig with validation.

        Args:
            value: The subTlvConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subTlvConfig = None
            return

        if not isinstance(value, EthTSynSubTlvConfig):
            raise TypeError(
                f"subTlvConfig must be EthTSynSubTlvConfig or None, got {type(value).__name__}"
            )
        self._subTlvConfig = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcSecured(self) -> "GlobalTimeCrcSupport":
        """
        AUTOSAR-compliant getter for crcSecured.

        Returns:
            The crcSecured value

        Note:
            Delegates to crc_secured property (CODING_RULE_V2_00017)
        """
        return self.crc_secured  # Delegates to property

    def setCrcSecured(self, value: "GlobalTimeCrcSupport") -> "GlobalTimeEthMaster":
        """
        AUTOSAR-compliant setter for crcSecured with method chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_secured property setter (gets validation automatically)
        """
        self.crc_secured = value  # Delegates to property setter
        return self

    def getHoldOverTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for holdOverTime.

        Returns:
            The holdOverTime value

        Note:
            Delegates to hold_over_time property (CODING_RULE_V2_00017)
        """
        return self.hold_over_time  # Delegates to property

    def setHoldOverTime(self, value: "TimeValue") -> "GlobalTimeEthMaster":
        """
        AUTOSAR-compliant setter for holdOverTime with method chaining.

        Args:
            value: The holdOverTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to hold_over_time property setter (gets validation automatically)
        """
        self.hold_over_time = value  # Delegates to property setter
        return self

    def getSubTlvConfig(self) -> "EthTSynSubTlvConfig":
        """
        AUTOSAR-compliant getter for subTlvConfig.

        Returns:
            The subTlvConfig value

        Note:
            Delegates to sub_tlv_config property (CODING_RULE_V2_00017)
        """
        return self.sub_tlv_config  # Delegates to property

    def setSubTlvConfig(self, value: "EthTSynSubTlvConfig") -> "GlobalTimeEthMaster":
        """
        AUTOSAR-compliant setter for subTlvConfig with method chaining.

        Args:
            value: The subTlvConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_tlv_config property setter (gets validation automatically)
        """
        self.sub_tlv_config = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> "GlobalTimeEthMaster":
        """
        Set crcSecured and return self for chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_secured("value")
        """
        self.crc_secured = value  # Use property setter (gets validation)
        return self

    def with_hold_over_time(self, value: Optional["TimeValue"]) -> "GlobalTimeEthMaster":
        """
        Set holdOverTime and return self for chaining.

        Args:
            value: The holdOverTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hold_over_time("value")
        """
        self.hold_over_time = value  # Use property setter (gets validation)
        return self

    def with_sub_tlv_config(self, value: Optional["EthTSynSubTlvConfig"]) -> "GlobalTimeEthMaster":
        """
        Set subTlvConfig and return self for chaining.

        Args:
            value: The subTlvConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_tlv_config("value")
        """
        self.sub_tlv_config = value  # Use property setter (gets validation)
        return self
