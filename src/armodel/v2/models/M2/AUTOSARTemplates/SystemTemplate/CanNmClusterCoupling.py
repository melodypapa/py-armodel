from typing import List, Optional


class CanNmClusterCoupling(NmClusterCoupling):
    """
    CAN attributes that are valid for each of the referenced (coupled) CAN
    clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 684, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled CAN Clusters.
        self._coupledCluster: List["CanNmCluster"] = []

    @property
    def coupled_cluster(self) -> List["CanNmCluster"]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
        # Enables busload reduction support.
        self._nmBusloadReductionEnabled: Optional["Boolean"] = None

    @property
    def nm_busload_reduction_enabled(self) -> Optional["Boolean"]:
        """Get nmBusloadReductionEnabled (Pythonic accessor)."""
        return self._nmBusloadReductionEnabled

    @nm_busload_reduction_enabled.setter
    def nm_busload_reduction_enabled(self, value: Optional["Boolean"]) -> None:
        """
        Set nmBusloadReductionEnabled with validation.

        Args:
            value: The nmBusloadReductionEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmBusloadReductionEnabled = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmBusloadReductionEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmBusloadReductionEnabled = value
        # Enables the asynchronous transmission of a CanNm upon bus-communication
        # request in.
        self._nmImmediate: Optional["Boolean"] = None

    @property
    def nm_immediate(self) -> Optional["Boolean"]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional["Boolean"]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmImmediate must be Boolean or None, got {type(value).__name__}"
            )
        self._nmImmediate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCoupledCluster(self) -> List["CanNmCluster"]:
        """
        AUTOSAR-compliant getter for coupledCluster.

        Returns:
            The coupledCluster value

        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmBusloadReductionEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmBusloadReductionEnabled.

        Returns:
            The nmBusloadReductionEnabled value

        Note:
            Delegates to nm_busload_reduction_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_busload_reduction_enabled  # Delegates to property

    def setNmBusloadReductionEnabled(self, value: "Boolean") -> "CanNmClusterCoupling":
        """
        AUTOSAR-compliant setter for nmBusloadReductionEnabled with method chaining.

        Args:
            value: The nmBusloadReductionEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_busload_reduction_enabled property setter (gets validation automatically)
        """
        self.nm_busload_reduction_enabled = value  # Delegates to property setter
        return self

    def getNmImmediate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: "Boolean") -> "CanNmClusterCoupling":
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_busload_reduction_enabled(self, value: Optional["Boolean"]) -> "CanNmClusterCoupling":
        """
        Set nmBusloadReductionEnabled and return self for chaining.

        Args:
            value: The nmBusloadReductionEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_busload_reduction_enabled("value")
        """
        self.nm_busload_reduction_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_immediate(self, value: Optional["Boolean"]) -> "CanNmClusterCoupling":
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self
