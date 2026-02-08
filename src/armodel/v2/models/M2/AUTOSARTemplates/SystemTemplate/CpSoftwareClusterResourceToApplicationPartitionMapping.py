from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """
    This meta class maps a Software Cluster resource to an Application Partition
    to restrict the usage.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 284, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ApplicationPartition for which the mapping applies.
        self._application: Optional["ApplicationPartition"] = None

    @property
    def application(self) -> Optional["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationPartition"]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationPartition):
            raise TypeError(
                f"application must be ApplicationPartition or None, got {type(value).__name__}"
            )
        self._application = value
        # Software Cluster Resource for which the mapping applies.
        self._resource: Optional["CpSoftwareCluster"] = None

    @property
    def resource(self) -> Optional["CpSoftwareCluster"]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set resource with validation.

        Args:
            value: The resource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resource = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"resource must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._resource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationPartition":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationPartition") -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getResource(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for resource with method chaining.

        Args:
            value: The resource to set

        Returns:
            self for method chaining

        Note:
            Delegates to resource property setter (gets validation automatically)
        """
        self.resource = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationPartition"]) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_resource(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        Set resource and return self for chaining.

        Args:
            value: The resource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource("value")
        """
        self.resource = value  # Use property setter (gets validation)
        return self
