from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DdsCpPartition(Identifiable):
    """
    Definition of a DDS Partition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 527, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the DDS Partition Name.
        # ’*’ may be used to default partition.
        self._partitionName: Optional["String"] = None

    @property
    def partition_name(self) -> Optional["String"]:
        """Get partitionName (Pythonic accessor)."""
        return self._partitionName

    @partition_name.setter
    def partition_name(self, value: Optional["String"]) -> None:
        """
        Set partitionName with validation.

        Args:
            value: The partitionName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._partitionName = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"partitionName must be String or None, got {type(value).__name__}"
            )
        self._partitionName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPartitionName(self) -> "String":
        """
        AUTOSAR-compliant getter for partitionName.

        Returns:
            The partitionName value

        Note:
            Delegates to partition_name property (CODING_RULE_V2_00017)
        """
        return self.partition_name  # Delegates to property

    def setPartitionName(self, value: "String") -> "DdsCpPartition":
        """
        AUTOSAR-compliant setter for partitionName with method chaining.

        Args:
            value: The partitionName to set

        Returns:
            self for method chaining

        Note:
            Delegates to partition_name property setter (gets validation automatically)
        """
        self.partition_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_partition_name(self, value: Optional["String"]) -> "DdsCpPartition":
        """
        Set partitionName and return self for chaining.

        Args:
            value: The partitionName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_partition_name("value")
        """
        self.partition_name = value  # Use property setter (gets validation)
        return self
