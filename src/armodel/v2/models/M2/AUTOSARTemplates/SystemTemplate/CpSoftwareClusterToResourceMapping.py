from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CpSoftwareClusterToResourceMapping(Identifiable):
    """
    This meta class maps a service resource to CP Software Clusters. By this
    mapping it’s specified whether the Software Cluster has to provide or to
    require the resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 907, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CP Software Cluster providing the resource.
        self._provider: Optional["CpSoftwareCluster"] = None

    @property
    def provider(self) -> Optional["CpSoftwareCluster"]:
        """Get provider (Pythonic accessor)."""
        return self._provider

    @provider.setter
    def provider(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set provider with validation.

        Args:
            value: The provider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provider = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"provider must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._provider = value
        # CP Software Cluster requesting the resource.
        self._requester: List["CpSoftwareCluster"] = []

    @property
    def requester(self) -> List["CpSoftwareCluster"]:
        """Get requester (Pythonic accessor)."""
        return self._requester
        # Service resource for which the mapping applies.
        self._service: Optional["CpSoftwareCluster"] = None

    @property
    def service(self) -> Optional["CpSoftwareCluster"]:
        """Get service (Pythonic accessor)."""
        return self._service

    @service.setter
    def service(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set service with validation.

        Args:
            value: The service to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._service = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"service must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._service = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvider(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for provider.

        Returns:
            The provider value

        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterToResourceMapping":
        """
        AUTOSAR-compliant setter for provider with method chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider property setter (gets validation automatically)
        """
        self.provider = value  # Delegates to property setter
        return self

    def getRequester(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for requester.

        Returns:
            The requester value

        Note:
            Delegates to requester property (CODING_RULE_V2_00017)
        """
        return self.requester  # Delegates to property

    def getService(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for service.

        Returns:
            The service value

        Note:
            Delegates to service property (CODING_RULE_V2_00017)
        """
        return self.service  # Delegates to property

    def setService(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterToResourceMapping":
        """
        AUTOSAR-compliant setter for service with method chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Note:
            Delegates to service property setter (gets validation automatically)
        """
        self.service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterToResourceMapping":
        """
        Set provider and return self for chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider("value")
        """
        self.provider = value  # Use property setter (gets validation)
        return self

    def with_service(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterToResourceMapping":
        """
        Set service and return self for chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service("value")
        """
        self.service = value  # Use property setter (gets validation)
        return self
