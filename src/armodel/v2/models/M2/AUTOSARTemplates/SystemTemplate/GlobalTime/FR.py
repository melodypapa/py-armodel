from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeMaster,
)


class GlobalTimeFrMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for Flexray
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 877, Classic Platform R23-11)
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

    def setCrcSecured(self, value: "GlobalTimeCrcSupport") -> "GlobalTimeFrMaster":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> "GlobalTimeFrMaster":
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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeSlave,
)


class GlobalTimeFrSlave(GlobalTimeSlave):
    """
    This represents the specialization of the GlobalTimeSlave for Flexray
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 878, Classic Platform R23-11)
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
        # Specifies the maximum allowed gap of the sequence between two SYNC resp.
        # two OFS messages.
        self._sequence: Optional["PositiveInteger"] = None

    @property
    def sequence(self) -> Optional["PositiveInteger"]:
        """Get sequence (Pythonic accessor)."""
        return self._sequence

    @sequence.setter
    def sequence(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sequence with validation.

        Args:
            value: The sequence to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sequence = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sequence must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sequence = value

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

    def setCrcValidated(self, value: "GlobalTimeCrc") -> "GlobalTimeFrSlave":
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

    def getSequence(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sequence.

        Returns:
            The sequence value

        Note:
            Delegates to sequence property (CODING_RULE_V2_00017)
        """
        return self.sequence  # Delegates to property

    def setSequence(self, value: "PositiveInteger") -> "GlobalTimeFrSlave":
        """
        AUTOSAR-compliant setter for sequence with method chaining.

        Args:
            value: The sequence to set

        Returns:
            self for method chaining

        Note:
            Delegates to sequence property setter (gets validation automatically)
        """
        self.sequence = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_validated(self, value: Optional["GlobalTimeCrc"]) -> "GlobalTimeFrSlave":
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

    def with_sequence(self, value: Optional["PositiveInteger"]) -> "GlobalTimeFrSlave":
        """
        Set sequence and return self for chaining.

        Args:
            value: The sequence to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sequence("value")
        """
        self.sequence = value  # Use property setter (gets validation)
        return self

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    AbstractGlobalTimeDomainProps,
)


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Flexray GlobalTime specific properties.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 878, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._ofsDataIDList: "PositiveInteger" = None

    @property
    def ofs_data_id_list(self) -> "PositiveInteger":
        """Get ofsDataIDList (Pythonic accessor)."""
        return self._ofsDataIDList

    @ofs_data_id_list.setter
    def ofs_data_id_list(self, value: "PositiveInteger") -> None:
        """
        Set ofsDataIDList with validation.

        Args:
            value: The ofsDataIDList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ofsDataIDList must be PositiveInteger, got {type(value).__name__}"
            )
        self._ofsDataIDList = value
        self._syncDataIDList: "PositiveInteger" = None

    @property
    def sync_data_id_list(self) -> "PositiveInteger":
        """Get syncDataIDList (Pythonic accessor)."""
        return self._syncDataIDList

    @sync_data_id_list.setter
    def sync_data_id_list(self, value: "PositiveInteger") -> None:
        """
        Set syncDataIDList with validation.

        Args:
            value: The syncDataIDList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"syncDataIDList must be PositiveInteger, got {type(value).__name__}"
            )
        self._syncDataIDList = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOfsDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ofsDataIDList.

        Returns:
            The ofsDataIDList value

        Note:
            Delegates to ofs_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.ofs_data_id_list  # Delegates to property

    def setOfsDataIDList(self, value: "PositiveInteger") -> "FrGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for ofsDataIDList with method chaining.

        Args:
            value: The ofsDataIDList to set

        Returns:
            self for method chaining

        Note:
            Delegates to ofs_data_id_list property setter (gets validation automatically)
        """
        self.ofs_data_id_list = value  # Delegates to property setter
        return self

    def getSyncDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncDataIDList.

        Returns:
            The syncDataIDList value

        Note:
            Delegates to sync_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.sync_data_id_list  # Delegates to property

    def setSyncDataIDList(self, value: "PositiveInteger") -> "FrGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for syncDataIDList with method chaining.

        Args:
            value: The syncDataIDList to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_data_id_list property setter (gets validation automatically)
        """
        self.sync_data_id_list = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ofs_data_id_list(self, value: "PositiveInteger") -> "FrGlobalTimeDomainProps":
        """
        Set ofsDataIDList and return self for chaining.

        Args:
            value: The ofsDataIDList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ofs_data_id_list("value")
        """
        self.ofs_data_id_list = value  # Use property setter (gets validation)
        return self

    def with_sync_data_id_list(self, value: "PositiveInteger") -> "FrGlobalTimeDomainProps":
        """
        Set syncDataIDList and return self for chaining.

        Args:
            value: The syncDataIDList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_data_id_list("value")
        """
        self.sync_data_id_list = value  # Use property setter (gets validation)
        return self
