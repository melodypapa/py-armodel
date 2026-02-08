from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CpSoftwareCluster,
    TimingDescription,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """
    This is used to assign an unequivocal global resource identification to a
    temporal and dynamic resource.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 158, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specific resource identification assigned to the and dynamic resource.
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
        # The timing description representing the temporal and resource.
        self._timing: Optional["TimingDescription"] = None

    @property
    def timing(self) -> Optional["TimingDescription"]:
        """Get timing (Pythonic accessor)."""
        return self._timing

    @timing.setter
    def timing(self, value: Optional["TimingDescription"]) -> None:
        """
        Set timing with validation.

        Args:
            value: The timing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timing = None
            return

        if not isinstance(value, TimingDescription):
            raise TypeError(
                f"timing must be TimingDescription or None, got {type(value).__name__}"
            )
        self._timing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResource(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: "CpSoftwareCluster") -> "TDCpSoftwareClusterResourceMapping":
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

    def getTiming(self) -> "TimingDescription":
        """
        AUTOSAR-compliant getter for timing.

        Returns:
            The timing value

        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def setTiming(self, value: "TimingDescription") -> "TDCpSoftwareClusterResourceMapping":
        """
        AUTOSAR-compliant setter for timing with method chaining.

        Args:
            value: The timing to set

        Returns:
            self for method chaining

        Note:
            Delegates to timing property setter (gets validation automatically)
        """
        self.timing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_resource(self, value: Optional["CpSoftwareCluster"]) -> "TDCpSoftwareClusterResourceMapping":
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

    def with_timing(self, value: Optional["TimingDescription"]) -> "TDCpSoftwareClusterResourceMapping":
        """
        Set timing and return self for chaining.

        Args:
            value: The timing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing("value")
        """
        self.timing = value  # Use property setter (gets validation)
        return self
