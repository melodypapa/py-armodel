from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynSubTlvConfig(ARObject):
    """
    Defines the subTLV fields which shall be included in the time sync message.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthTSynSubTlvConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether an AUTOSAR Follow_Up TLV OFS used.
        self._ofsSubTlv: Optional["Boolean"] = None

    @property
    def ofs_sub_tlv(self) -> Optional["Boolean"]:
        """Get ofsSubTlv (Pythonic accessor)."""
        return self._ofsSubTlv

    @ofs_sub_tlv.setter
    def ofs_sub_tlv(self, value: Optional["Boolean"]) -> None:
        """
        Set ofsSubTlv with validation.

        Args:
            value: The ofsSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ofsSubTlv = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"ofsSubTlv must be Boolean or None, got {type(value).__name__}"
            )
        self._ofsSubTlv = value
        # Defines whether an AUTOSAR Follow_Up TLV Status used.
        self._statusSubTlv: Optional["Boolean"] = None

    @property
    def status_sub_tlv(self) -> Optional["Boolean"]:
        """Get statusSubTlv (Pythonic accessor)."""
        return self._statusSubTlv

    @status_sub_tlv.setter
    def status_sub_tlv(self, value: Optional["Boolean"]) -> None:
        """
        Set statusSubTlv with validation.

        Args:
            value: The statusSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._statusSubTlv = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"statusSubTlv must be Boolean or None, got {type(value).__name__}"
            )
        self._statusSubTlv = value
        # Defines whether an AUTOSAR Follow_Up TLV Time used.
        self._timeSubTlv: Optional["Boolean"] = None

    @property
    def time_sub_tlv(self) -> Optional["Boolean"]:
        """Get timeSubTlv (Pythonic accessor)."""
        return self._timeSubTlv

    @time_sub_tlv.setter
    def time_sub_tlv(self, value: Optional["Boolean"]) -> None:
        """
        Set timeSubTlv with validation.

        Args:
            value: The timeSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSubTlv = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"timeSubTlv must be Boolean or None, got {type(value).__name__}"
            )
        self._timeSubTlv = value
        # Defines whether an AUTOSAR Follow_Up TLV UserData used.
        self._userDataSubTlv: Optional["Boolean"] = None

    @property
    def user_data_sub_tlv(self) -> Optional["Boolean"]:
        """Get userDataSubTlv (Pythonic accessor)."""
        return self._userDataSubTlv

    @user_data_sub_tlv.setter
    def user_data_sub_tlv(self, value: Optional["Boolean"]) -> None:
        """
        Set userDataSubTlv with validation.

        Args:
            value: The userDataSubTlv to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._userDataSubTlv = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"userDataSubTlv must be Boolean or None, got {type(value).__name__}"
            )
        self._userDataSubTlv = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOfsSubTlv(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for ofsSubTlv.

        Returns:
            The ofsSubTlv value

        Note:
            Delegates to ofs_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.ofs_sub_tlv  # Delegates to property

    def setOfsSubTlv(self, value: "Boolean") -> "EthTSynSubTlvConfig":
        """
        AUTOSAR-compliant setter for ofsSubTlv with method chaining.

        Args:
            value: The ofsSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to ofs_sub_tlv property setter (gets validation automatically)
        """
        self.ofs_sub_tlv = value  # Delegates to property setter
        return self

    def getStatusSubTlv(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for statusSubTlv.

        Returns:
            The statusSubTlv value

        Note:
            Delegates to status_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.status_sub_tlv  # Delegates to property

    def setStatusSubTlv(self, value: "Boolean") -> "EthTSynSubTlvConfig":
        """
        AUTOSAR-compliant setter for statusSubTlv with method chaining.

        Args:
            value: The statusSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to status_sub_tlv property setter (gets validation automatically)
        """
        self.status_sub_tlv = value  # Delegates to property setter
        return self

    def getTimeSubTlv(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for timeSubTlv.

        Returns:
            The timeSubTlv value

        Note:
            Delegates to time_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.time_sub_tlv  # Delegates to property

    def setTimeSubTlv(self, value: "Boolean") -> "EthTSynSubTlvConfig":
        """
        AUTOSAR-compliant setter for timeSubTlv with method chaining.

        Args:
            value: The timeSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sub_tlv property setter (gets validation automatically)
        """
        self.time_sub_tlv = value  # Delegates to property setter
        return self

    def getUserDataSubTlv(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for userDataSubTlv.

        Returns:
            The userDataSubTlv value

        Note:
            Delegates to user_data_sub_tlv property (CODING_RULE_V2_00017)
        """
        return self.user_data_sub_tlv  # Delegates to property

    def setUserDataSubTlv(self, value: "Boolean") -> "EthTSynSubTlvConfig":
        """
        AUTOSAR-compliant setter for userDataSubTlv with method chaining.

        Args:
            value: The userDataSubTlv to set

        Returns:
            self for method chaining

        Note:
            Delegates to user_data_sub_tlv property setter (gets validation automatically)
        """
        self.user_data_sub_tlv = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ofs_sub_tlv(self, value: Optional["Boolean"]) -> "EthTSynSubTlvConfig":
        """
        Set ofsSubTlv and return self for chaining.

        Args:
            value: The ofsSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ofs_sub_tlv("value")
        """
        self.ofs_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_status_sub_tlv(self, value: Optional["Boolean"]) -> "EthTSynSubTlvConfig":
        """
        Set statusSubTlv and return self for chaining.

        Args:
            value: The statusSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_status_sub_tlv("value")
        """
        self.status_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_time_sub_tlv(self, value: Optional["Boolean"]) -> "EthTSynSubTlvConfig":
        """
        Set timeSubTlv and return self for chaining.

        Args:
            value: The timeSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sub_tlv("value")
        """
        self.time_sub_tlv = value  # Use property setter (gets validation)
        return self

    def with_user_data_sub_tlv(self, value: Optional["Boolean"]) -> "EthTSynSubTlvConfig":
        """
        Set userDataSubTlv and return self for chaining.

        Args:
            value: The userDataSubTlv to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_user_data_sub_tlv("value")
        """
        self.user_data_sub_tlv = value  # Use property setter (gets validation)
        return self
