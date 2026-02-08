from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    AbstractGlobalTimeDomainProps,
)


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Can Global Time specific properties.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::CAN

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 864, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._fupDataIDList: "PositiveInteger" = None

    @property
    def fup_data_id_list(self) -> "PositiveInteger":
        """Get fupDataIDList (Pythonic accessor)."""
        return self._fupDataIDList

    @fup_data_id_list.setter
    def fup_data_id_list(self, value: "PositiveInteger") -> None:
        """
        Set fupDataIDList with validation.

        Args:
            value: The fupDataIDList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"fupDataIDList must be PositiveInteger, got {type(value).__name__}"
            )
        self._fupDataIDList = value
        self._ofnsDataIDList: "PositiveInteger" = None

    @property
    def ofns_data_id_list(self) -> "PositiveInteger":
        """Get ofnsDataIDList (Pythonic accessor)."""
        return self._ofnsDataIDList

    @ofns_data_id_list.setter
    def ofns_data_id_list(self, value: "PositiveInteger") -> None:
        """
        Set ofnsDataIDList with validation.

        Args:
            value: The ofnsDataIDList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ofnsDataIDList must be PositiveInteger, got {type(value).__name__}"
            )
        self._ofnsDataIDList = value
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

    def getFupDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for fupDataIDList.

        Returns:
            The fupDataIDList value

        Note:
            Delegates to fup_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.fup_data_id_list  # Delegates to property

    def setFupDataIDList(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for fupDataIDList with method chaining.

        Args:
            value: The fupDataIDList to set

        Returns:
            self for method chaining

        Note:
            Delegates to fup_data_id_list property setter (gets validation automatically)
        """
        self.fup_data_id_list = value  # Delegates to property setter
        return self

    def getOfnsDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ofnsDataIDList.

        Returns:
            The ofnsDataIDList value

        Note:
            Delegates to ofns_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.ofns_data_id_list  # Delegates to property

    def setOfnsDataIDList(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for ofnsDataIDList with method chaining.

        Args:
            value: The ofnsDataIDList to set

        Returns:
            self for method chaining

        Note:
            Delegates to ofns_data_id_list property setter (gets validation automatically)
        """
        self.ofns_data_id_list = value  # Delegates to property setter
        return self

    def getOfsDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ofsDataIDList.

        Returns:
            The ofsDataIDList value

        Note:
            Delegates to ofs_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.ofs_data_id_list  # Delegates to property

    def setOfsDataIDList(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
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

    def setSyncDataIDList(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
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

    def with_fup_data_id_list(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
        """
        Set fupDataIDList and return self for chaining.

        Args:
            value: The fupDataIDList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fup_data_id_list("value")
        """
        self.fup_data_id_list = value  # Use property setter (gets validation)
        return self

    def with_ofns_data_id_list(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
        """
        Set ofnsDataIDList and return self for chaining.

        Args:
            value: The ofnsDataIDList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ofns_data_id_list("value")
        """
        self.ofns_data_id_list = value  # Use property setter (gets validation)
        return self

    def with_ofs_data_id_list(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
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

    def with_sync_data_id_list(self, value: "PositiveInteger") -> "CanGlobalTimeDomainProps":
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
