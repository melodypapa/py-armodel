from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DdsHistoryKindEnum
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsHistory(ARObject):
    """
    Describes the DDS HISTORY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsHistory

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 537, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "HISTORY" chapter of DDS.
        self._historyKind: Optional["DdsHistoryKindEnum"] = None

    @property
    def history_kind(self) -> Optional["DdsHistoryKindEnum"]:
        """Get historyKind (Pythonic accessor)."""
        return self._historyKind

    @history_kind.setter
    def history_kind(self, value: Optional["DdsHistoryKindEnum"]) -> None:
        """
        Set historyKind with validation.

        Args:
            value: The historyKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._historyKind = None
            return

        if not isinstance(value, DdsHistoryKindEnum):
            raise TypeError(
                f"historyKind must be DdsHistoryKindEnum or None, got {type(value).__name__}"
            )
        self._historyKind = value
        # See "HISTORY" chapter of DDS.
        # atp.
        # Status=candidate.
        self._historyOrder: Optional["PositiveInteger"] = None

    @property
    def history_order(self) -> Optional["PositiveInteger"]:
        """Get historyOrder (Pythonic accessor)."""
        return self._historyOrder

    @history_order.setter
    def history_order(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set historyOrder with validation.

        Args:
            value: The historyOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._historyOrder = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"historyOrder must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._historyOrder = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHistoryKind(self) -> "DdsHistoryKindEnum":
        """
        AUTOSAR-compliant getter for historyKind.

        Returns:
            The historyKind value

        Note:
            Delegates to history_kind property (CODING_RULE_V2_00017)
        """
        return self.history_kind  # Delegates to property

    def setHistoryKind(self, value: "DdsHistoryKindEnum") -> "DdsHistory":
        """
        AUTOSAR-compliant setter for historyKind with method chaining.

        Args:
            value: The historyKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to history_kind property setter (gets validation automatically)
        """
        self.history_kind = value  # Delegates to property setter
        return self

    def getHistoryOrder(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for historyOrder.

        Returns:
            The historyOrder value

        Note:
            Delegates to history_order property (CODING_RULE_V2_00017)
        """
        return self.history_order  # Delegates to property

    def setHistoryOrder(self, value: "PositiveInteger") -> "DdsHistory":
        """
        AUTOSAR-compliant setter for historyOrder with method chaining.

        Args:
            value: The historyOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to history_order property setter (gets validation automatically)
        """
        self.history_order = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_history_kind(self, value: Optional["DdsHistoryKindEnum"]) -> "DdsHistory":
        """
        Set historyKind and return self for chaining.

        Args:
            value: The historyKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_history_kind("value")
        """
        self.history_kind = value  # Use property setter (gets validation)
        return self

    def with_history_order(self, value: Optional["PositiveInteger"]) -> "DdsHistory":
        """
        Set historyOrder and return self for chaining.

        Args:
            value: The historyOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_history_order("value")
        """
        self.history_order = value  # Use property setter (gets validation)
        return self
