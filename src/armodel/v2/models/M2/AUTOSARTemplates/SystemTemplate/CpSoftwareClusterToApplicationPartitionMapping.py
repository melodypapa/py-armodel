from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """
    This meta class defines ApplicationPartitions that are applicable for the
    CpSoftwareCluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterToApplicationPartitionMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 287, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of ApplicationPartitions available in the Cp.
        self._application: List["ApplicationPartition"] = []

    @property
    def application(self) -> List["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # Software Cluster Resource for which the mapping applies.
        self._softwareCluster: Optional["CpSoftwareCluster"] = None

    @property
    def software_cluster(self) -> Optional["CpSoftwareCluster"]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set softwareCluster with validation.

        Args:
            value: The softwareCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._softwareCluster = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"softwareCluster must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._softwareCluster = value

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

    def getSoftwareCluster(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for softwareCluster with method chaining.

        Args:
            value: The softwareCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to software_cluster property setter (gets validation automatically)
        """
        self.software_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_software_cluster(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """
        Set softwareCluster and return self for chaining.

        Args:
            value: The softwareCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software_cluster("value")
        """
        self.software_cluster = value  # Use property setter (gets validation)
        return self
