from typing import Optional


class CouplingPortShaper(CouplingPortStructuralElement):
    """
    Defines a shaper for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 123, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the increase of credit in bits per second for the.
        self._idleSlope: Optional["PositiveInteger"] = None

    @property
    def idle_slope(self) -> Optional["PositiveInteger"]:
        """Get idleSlope (Pythonic accessor)."""
        return self._idleSlope

    @idle_slope.setter
    def idle_slope(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set idleSlope with validation.

        Args:
            value: The idleSlope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idleSlope = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"idleSlope must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._idleSlope = value
        # Defines the CouplingPortFifo which provides the input to.
        self._predecessorFifo: "CouplingPortFifo" = None

    @property
    def predecessor_fifo(self) -> "CouplingPortFifo":
        """Get predecessorFifo (Pythonic accessor)."""
        return self._predecessorFifo

    @predecessor_fifo.setter
    def predecessor_fifo(self, value: "CouplingPortFifo") -> None:
        """
        Set predecessorFifo with validation.

        Args:
            value: The predecessorFifo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CouplingPortFifo):
            raise TypeError(
                f"predecessorFifo must be CouplingPortFifo, got {type(value).__name__}"
            )
        self._predecessorFifo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdleSlope(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for idleSlope.

        Returns:
            The idleSlope value

        Note:
            Delegates to idle_slope property (CODING_RULE_V2_00017)
        """
        return self.idle_slope  # Delegates to property

    def setIdleSlope(self, value: "PositiveInteger") -> "CouplingPortShaper":
        """
        AUTOSAR-compliant setter for idleSlope with method chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Note:
            Delegates to idle_slope property setter (gets validation automatically)
        """
        self.idle_slope = value  # Delegates to property setter
        return self

    def getPredecessorFifo(self) -> "CouplingPortFifo":
        """
        AUTOSAR-compliant getter for predecessorFifo.

        Returns:
            The predecessorFifo value

        Note:
            Delegates to predecessor_fifo property (CODING_RULE_V2_00017)
        """
        return self.predecessor_fifo  # Delegates to property

    def setPredecessorFifo(self, value: "CouplingPortFifo") -> "CouplingPortShaper":
        """
        AUTOSAR-compliant setter for predecessorFifo with method chaining.

        Args:
            value: The predecessorFifo to set

        Returns:
            self for method chaining

        Note:
            Delegates to predecessor_fifo property setter (gets validation automatically)
        """
        self.predecessor_fifo = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_idle_slope(self, value: Optional["PositiveInteger"]) -> "CouplingPortShaper":
        """
        Set idleSlope and return self for chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idle_slope("value")
        """
        self.idle_slope = value  # Use property setter (gets validation)
        return self

    def with_predecessor_fifo(self, value: "CouplingPortFifo") -> "CouplingPortShaper":
        """
        Set predecessorFifo and return self for chaining.

        Args:
            value: The predecessorFifo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predecessor_fifo("value")
        """
        self.predecessor_fifo = value  # Use property setter (gets validation)
        return self
