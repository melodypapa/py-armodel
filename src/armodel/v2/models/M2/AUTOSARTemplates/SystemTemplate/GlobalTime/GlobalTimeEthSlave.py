from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeSlave,
)


class GlobalTimeEthSlave(GlobalTimeSlave):
    """
    This represents the specialization of the GlobalTimeSlave for Ethernet
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not validation of the CRC is.
        self._crcValidated: Optional["GlobalTimeCrc"] = None

    @property
    def crc_validated(self) -> Optional["GlobalTimeCrc"]:
        """Get crcValidated (Pythonic accessor)."""
        return self._crcValidated

    @crc_validated.setter
    def crc_validated(self, value: Optional["GlobalTimeCrc"]) -> None:
        """
        Set crcValidated with validation.

        Args:
            value: The crcValidated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcValidated = None
            return

        if not isinstance(value, GlobalTimeCrc):
            raise TypeError(
                f"crcValidated must be GlobalTimeCrc or None, got {type(value).__name__}"
            )
        self._crcValidated = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcValidated(self) -> "GlobalTimeCrc":
        """
        AUTOSAR-compliant getter for crcValidated.

        Returns:
            The crcValidated value

        Note:
            Delegates to crc_validated property (CODING_RULE_V2_00017)
        """
        return self.crc_validated  # Delegates to property

    def setCrcValidated(self, value: "GlobalTimeCrc") -> "GlobalTimeEthSlave":
        """
        AUTOSAR-compliant setter for crcValidated with method chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_validated property setter (gets validation automatically)
        """
        self.crc_validated = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_validated(self, value: Optional["GlobalTimeCrc"]) -> "GlobalTimeEthSlave":
        """
        Set crcValidated and return self for chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_validated("value")
        """
        self.crc_validated = value  # Use property setter (gets validation)
        return self
