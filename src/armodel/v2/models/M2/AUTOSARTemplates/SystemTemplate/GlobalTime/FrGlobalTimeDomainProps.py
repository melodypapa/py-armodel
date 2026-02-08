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
