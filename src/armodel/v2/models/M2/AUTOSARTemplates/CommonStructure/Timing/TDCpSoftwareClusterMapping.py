from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CpSoftwareCluster,
    TimingDescription,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TDCpSoftwareClusterMapping(Identifiable):
    """
    This is used to specify a mapping between a software cluster that provides
    temporal and dynamic resources and the software clusters that need these
    resources.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterMapping

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 157, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the software cluster that provides the temporal and.
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
        # This is the software cluster that requests the temporal resource.
        self._requestor: List["CpSoftwareCluster"] = []

    @property
    def requestor(self) -> List["CpSoftwareCluster"]:
        """Get requestor (Pythonic accessor)."""
        return self._requestor
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

    def getProvider(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for provider.

        Returns:
            The provider value

        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: "CpSoftwareCluster") -> "TDCpSoftwareClusterMapping":
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

    def getRequestor(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for requestor.

        Returns:
            The requestor value

        Note:
            Delegates to requestor property (CODING_RULE_V2_00017)
        """
        return self.requestor  # Delegates to property

    def getTiming(self) -> "TimingDescription":
        """
        AUTOSAR-compliant getter for timing.

        Returns:
            The timing value

        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def setTiming(self, value: "TimingDescription") -> "TDCpSoftwareClusterMapping":
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

    def with_provider(self, value: Optional["CpSoftwareCluster"]) -> "TDCpSoftwareClusterMapping":
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

    def with_timing(self, value: Optional["TimingDescription"]) -> "TDCpSoftwareClusterMapping":
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
