from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortStructuralElement,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 124, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._assignedTraffic: "PositiveInteger" = None

    @property
    def assigned_traffic(self) -> "PositiveInteger":
        """Get assignedTraffic (Pythonic accessor)."""
        return self._assignedTraffic

    @assigned_traffic.setter
    def assigned_traffic(self, value: "PositiveInteger") -> None:
        """
        Set assignedTraffic with validation.

        Args:
            value: The assignedTraffic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"assignedTraffic must be PositiveInteger, got {type(value).__name__}"
            )
        self._assignedTraffic = value
        # FIFO minimum length in Byte.
        # An actual configuration/ may use a bigger value.
        self._minimumFifo: Optional["PositiveInteger"] = None

    @property
    def minimum_fifo(self) -> Optional["PositiveInteger"]:
        """Get minimumFifo (Pythonic accessor)."""
        return self._minimumFifo

    @minimum_fifo.setter
    def minimum_fifo(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumFifo with validation.

        Args:
            value: The minimumFifo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumFifo = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minimumFifo must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minimumFifo = value
        # Definition of the shaper to be used for the processing of FIFO.
        self._shaper: Optional["CouplingPortAbstract"] = None

    @property
    def shaper(self) -> Optional["CouplingPortAbstract"]:
        """Get shaper (Pythonic accessor)."""
        return self._shaper

    @shaper.setter
    def shaper(self, value: Optional["CouplingPortAbstract"]) -> None:
        """
        Set shaper with validation.

        Args:
            value: The shaper to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shaper = None
            return

        if not isinstance(value, CouplingPortAbstract):
            raise TypeError(
                f"shaper must be CouplingPortAbstract or None, got {type(value).__name__}"
            )
        self._shaper = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedTraffic(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for assignedTraffic.

        Returns:
            The assignedTraffic value

        Note:
            Delegates to assigned_traffic property (CODING_RULE_V2_00017)
        """
        return self.assigned_traffic  # Delegates to property

    def setAssignedTraffic(self, value: "PositiveInteger") -> "CouplingPortFifo":
        """
        AUTOSAR-compliant setter for assignedTraffic with method chaining.

        Args:
            value: The assignedTraffic to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_traffic property setter (gets validation automatically)
        """
        self.assigned_traffic = value  # Delegates to property setter
        return self

    def getMinimumFifo(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumFifo.

        Returns:
            The minimumFifo value

        Note:
            Delegates to minimum_fifo property (CODING_RULE_V2_00017)
        """
        return self.minimum_fifo  # Delegates to property

    def setMinimumFifo(self, value: "PositiveInteger") -> "CouplingPortFifo":
        """
        AUTOSAR-compliant setter for minimumFifo with method chaining.

        Args:
            value: The minimumFifo to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_fifo property setter (gets validation automatically)
        """
        self.minimum_fifo = value  # Delegates to property setter
        return self

    def getShaper(self) -> "CouplingPortAbstract":
        """
        AUTOSAR-compliant getter for shaper.

        Returns:
            The shaper value

        Note:
            Delegates to shaper property (CODING_RULE_V2_00017)
        """
        return self.shaper  # Delegates to property

    def setShaper(self, value: "CouplingPortAbstract") -> "CouplingPortFifo":
        """
        AUTOSAR-compliant setter for shaper with method chaining.

        Args:
            value: The shaper to set

        Returns:
            self for method chaining

        Note:
            Delegates to shaper property setter (gets validation automatically)
        """
        self.shaper = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_traffic(self, value: "PositiveInteger") -> "CouplingPortFifo":
        """
        Set assignedTraffic and return self for chaining.

        Args:
            value: The assignedTraffic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_traffic("value")
        """
        self.assigned_traffic = value  # Use property setter (gets validation)
        return self

    def with_minimum_fifo(self, value: Optional["PositiveInteger"]) -> "CouplingPortFifo":
        """
        Set minimumFifo and return self for chaining.

        Args:
            value: The minimumFifo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_fifo("value")
        """
        self.minimum_fifo = value  # Use property setter (gets validation)
        return self

    def with_shaper(self, value: Optional["CouplingPortAbstract"]) -> "CouplingPortFifo":
        """
        Set shaper and return self for chaining.

        Args:
            value: The shaper to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_shaper("value")
        """
        self.shaper = value  # Use property setter (gets validation)
        return self
