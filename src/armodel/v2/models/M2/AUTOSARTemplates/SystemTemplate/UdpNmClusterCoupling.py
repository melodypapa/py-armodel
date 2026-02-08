from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmClusterCoupling


class UdpNmClusterCoupling(NmClusterCoupling):
    """
    Udp attributes that are valid for each of the referenced (coupled) UdpNm
    clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 688, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled UdpNm Clusters.
        self._coupledCluster: List["UdpNmCluster"] = []

    @property
    def coupled_cluster(self) -> List["UdpNmCluster"]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
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

    def getCoupledCluster(self) -> List["UdpNmCluster"]:
        """
        AUTOSAR-compliant getter for coupledCluster.

        Returns:
            The coupledCluster value

        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmImmediate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: "Boolean") -> "UdpNmClusterCoupling":
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

    def with_nm_immediate(self, value: Optional["Boolean"]) -> "UdpNmClusterCoupling":
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
