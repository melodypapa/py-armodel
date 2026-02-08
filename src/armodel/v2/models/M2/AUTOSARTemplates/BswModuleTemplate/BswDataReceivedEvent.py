from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswScheduleEvent


class BswDataReceivedEvent(BswScheduleEvent):
    """
    This event is thrown on reception of the referenced data via
    Sender-Receiver-Communication over the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 99, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The received data.
        self._data: RefType = None

    @property
    def data(self) -> RefType:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: RefType) -> None:
        """
        Set data with validation.

        Args:
            value: The data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        self._data = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> RefType:
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: RefType) -> "BswDataReceivedEvent":
        """
        AUTOSAR-compliant setter for data with method chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional[RefType]) -> "BswDataReceivedEvent":
        """
        Set data and return self for chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self
