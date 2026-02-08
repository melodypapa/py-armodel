from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BswDataReceptionPolicy(ARObject, ABC):
    """
    Specifies the reception policy for the referred data in sender-receiver
    communication over the BSW Scheduler. To be used for inter-partition and/or
    inter-core communication.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 104, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswDataReceptionPolicy:
            raise TypeError("BswDataReceptionPolicy is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data received over the BSW Scheduler using this.
        self._receivedData: RefType = None

    @property
    def received_data(self) -> RefType:
        """Get receivedData (Pythonic accessor)."""
        return self._receivedData

    @received_data.setter
    def received_data(self, value: RefType) -> None:
        """
        Set receivedData with validation.

        Args:
            value: The receivedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receivedData = None
            return

        self._receivedData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReceivedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for receivedData.

        Returns:
            The receivedData value

        Note:
            Delegates to received_data property (CODING_RULE_V2_00017)
        """
        return self.received_data  # Delegates to property

    def setReceivedData(self, value: RefType) -> "BswDataReceptionPolicy":
        """
        AUTOSAR-compliant setter for receivedData with method chaining.

        Args:
            value: The receivedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to received_data property setter (gets validation automatically)
        """
        self.received_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_received_data(self, value: Optional[RefType]) -> "BswDataReceptionPolicy":
        """
        Set receivedData and return self for chaining.

        Args:
            value: The receivedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_received_data("value")
        """
        self.received_data = value  # Use property setter (gets validation)
        return self
