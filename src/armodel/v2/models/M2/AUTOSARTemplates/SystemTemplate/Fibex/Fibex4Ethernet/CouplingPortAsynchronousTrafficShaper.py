from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SwitchAsynchronous
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """
    Defines an Asynchronous Traffic Shaper (ATS) for the CouplingPort egress
    structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortAsynchronousTrafficShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2012, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum token capacity of the token bucket in bit.
        # atp.
        # Status=candidate.
        self._committedBurst: Optional["PositiveInteger"] = None

    @property
    def committed_burst(self) -> Optional["PositiveInteger"]:
        """Get committedBurst (Pythonic accessor)."""
        return self._committedBurst

    @committed_burst.setter
    def committed_burst(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set committedBurst with validation.

        Args:
            value: The committedBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committedBurst = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"committedBurst must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._committedBurst = value
        # Defines the rate at which the token bucket is refilled with in bit per
        # second.
        self._committed: Optional["PositiveInteger"] = None

    @property
    def committed(self) -> Optional["PositiveInteger"]:
        """Get committed (Pythonic accessor)."""
        return self._committed

    @committed.setter
    def committed(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set committed with validation.

        Args:
            value: The committed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committed = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"committed must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._committed = value
        # Reference to the Traffic Shaper Group this Asynchronous Traffic Shaper is
                # part of.
        # atp.
        # Status=candidate.
        self._trafficShaper: Optional["SwitchAsynchronous"] = None

    @property
    def traffic_shaper(self) -> Optional["SwitchAsynchronous"]:
        """Get trafficShaper (Pythonic accessor)."""
        return self._trafficShaper

    @traffic_shaper.setter
    def traffic_shaper(self, value: Optional["SwitchAsynchronous"]) -> None:
        """
        Set trafficShaper with validation.

        Args:
            value: The trafficShaper to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficShaper = None
            return

        if not isinstance(value, SwitchAsynchronous):
            raise TypeError(
                f"trafficShaper must be SwitchAsynchronous or None, got {type(value).__name__}"
            )
        self._trafficShaper = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommittedBurst(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for committedBurst.

        Returns:
            The committedBurst value

        Note:
            Delegates to committed_burst property (CODING_RULE_V2_00017)
        """
        return self.committed_burst  # Delegates to property

    def setCommittedBurst(self, value: "PositiveInteger") -> "CouplingPortAsynchronousTrafficShaper":
        """
        AUTOSAR-compliant setter for committedBurst with method chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed_burst property setter (gets validation automatically)
        """
        self.committed_burst = value  # Delegates to property setter
        return self

    def getCommitted(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for committed.

        Returns:
            The committed value

        Note:
            Delegates to committed property (CODING_RULE_V2_00017)
        """
        return self.committed  # Delegates to property

    def setCommitted(self, value: "PositiveInteger") -> "CouplingPortAsynchronousTrafficShaper":
        """
        AUTOSAR-compliant setter for committed with method chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed property setter (gets validation automatically)
        """
        self.committed = value  # Delegates to property setter
        return self

    def getTrafficShaper(self) -> "SwitchAsynchronous":
        """
        AUTOSAR-compliant getter for trafficShaper.

        Returns:
            The trafficShaper value

        Note:
            Delegates to traffic_shaper property (CODING_RULE_V2_00017)
        """
        return self.traffic_shaper  # Delegates to property

    def setTrafficShaper(self, value: "SwitchAsynchronous") -> "CouplingPortAsynchronousTrafficShaper":
        """
        AUTOSAR-compliant setter for trafficShaper with method chaining.

        Args:
            value: The trafficShaper to set

        Returns:
            self for method chaining

        Note:
            Delegates to traffic_shaper property setter (gets validation automatically)
        """
        self.traffic_shaper = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_committed_burst(self, value: Optional["PositiveInteger"]) -> "CouplingPortAsynchronousTrafficShaper":
        """
        Set committedBurst and return self for chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed_burst("value")
        """
        self.committed_burst = value  # Use property setter (gets validation)
        return self

    def with_committed(self, value: Optional["PositiveInteger"]) -> "CouplingPortAsynchronousTrafficShaper":
        """
        Set committed and return self for chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed("value")
        """
        self.committed = value  # Use property setter (gets validation)
        return self

    def with_traffic_shaper(self, value: Optional["SwitchAsynchronous"]) -> "CouplingPortAsynchronousTrafficShaper":
        """
        Set trafficShaper and return self for chaining.

        Args:
            value: The trafficShaper to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traffic_shaper("value")
        """
        self.traffic_shaper = value  # Use property setter (gets validation)
        return self
