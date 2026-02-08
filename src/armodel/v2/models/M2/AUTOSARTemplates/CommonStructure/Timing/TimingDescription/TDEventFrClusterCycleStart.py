from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    FlexrayCluster,
    TDEventCycleStart,
)


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """
    This is used to describe the timing event related to a point in time where a
    communication cycle starts on a FlexRay cluster.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventFrClusterCycleStart

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._frCluster: Optional["FlexrayCluster"] = None

    @property
    def fr_cluster(self) -> Optional["FlexrayCluster"]:
        """Get frCluster (Pythonic accessor)."""
        return self._frCluster

    @fr_cluster.setter
    def fr_cluster(self, value: Optional["FlexrayCluster"]) -> None:
        """
        Set frCluster with validation.

        Args:
            value: The frCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frCluster = None
            return

        if not isinstance(value, FlexrayCluster):
            raise TypeError(
                f"frCluster must be FlexrayCluster or None, got {type(value).__name__}"
            )
        self._frCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrCluster(self) -> "FlexrayCluster":
        """
        AUTOSAR-compliant getter for frCluster.

        Returns:
            The frCluster value

        Note:
            Delegates to fr_cluster property (CODING_RULE_V2_00017)
        """
        return self.fr_cluster  # Delegates to property

    def setFrCluster(self, value: "FlexrayCluster") -> "TDEventFrClusterCycleStart":
        """
        AUTOSAR-compliant setter for frCluster with method chaining.

        Args:
            value: The frCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to fr_cluster property setter (gets validation automatically)
        """
        self.fr_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fr_cluster(self, value: Optional["FlexrayCluster"]) -> "TDEventFrClusterCycleStart":
        """
        Set frCluster and return self for chaining.

        Args:
            value: The frCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fr_cluster("value")
        """
        self.fr_cluster = value  # Use property setter (gets validation)
        return self
