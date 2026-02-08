from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationPartition,
    EcuPartition,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """
    Maps ApplicationPartitions to EcuPartitions. With this mapping an OEM has
    the option to predefine an allocation of Software Components to
    EcuPartitions in the System Design phase. The final and complete assignment
    is described in the OS Configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ApplicationPartitionToEcuPartitionMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 201, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to ApplicationPartitions that are mapped to an.
        self._application: List["ApplicationPartition"] = []

    @property
    def application(self) -> List["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # Reference to EcuPartition to which the Application assigned.
        self._ecuPartition: Optional["EcuPartition"] = None

    @property
    def ecu_partition(self) -> Optional["EcuPartition"]:
        """Get ecuPartition (Pythonic accessor)."""
        return self._ecuPartition

    @ecu_partition.setter
    def ecu_partition(self, value: Optional["EcuPartition"]) -> None:
        """
        Set ecuPartition with validation.

        Args:
            value: The ecuPartition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuPartition = None
            return

        if not isinstance(value, EcuPartition):
            raise TypeError(
                f"ecuPartition must be EcuPartition or None, got {type(value).__name__}"
            )
        self._ecuPartition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["ApplicationPartition"]:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getEcuPartition(self) -> "EcuPartition":
        """
        AUTOSAR-compliant getter for ecuPartition.

        Returns:
            The ecuPartition value

        Note:
            Delegates to ecu_partition property (CODING_RULE_V2_00017)
        """
        return self.ecu_partition  # Delegates to property

    def setEcuPartition(self, value: "EcuPartition") -> "ApplicationPartitionToEcuPartitionMapping":
        """
        AUTOSAR-compliant setter for ecuPartition with method chaining.

        Args:
            value: The ecuPartition to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_partition property setter (gets validation automatically)
        """
        self.ecu_partition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_partition(self, value: Optional["EcuPartition"]) -> "ApplicationPartitionToEcuPartitionMapping":
        """
        Set ecuPartition and return self for chaining.

        Args:
            value: The ecuPartition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_partition("value")
        """
        self.ecu_partition = value  # Use property setter (gets validation)
        return self
