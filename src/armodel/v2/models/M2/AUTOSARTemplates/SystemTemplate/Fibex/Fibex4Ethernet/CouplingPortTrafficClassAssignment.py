from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class CouplingPortTrafficClassAssignment(Referrable):
    """
    Defines the assignment of Traffic Class to a frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 128, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._priority: "PositiveInteger" = None

    @property
    def priority(self) -> "PositiveInteger":
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: "PositiveInteger") -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger, got {type(value).__name__}"
            )
        self._priority = value
        # Defines the Traffic Class which is assigned.
        self._trafficClass: Optional["PositiveInteger"] = None

    @property
    def traffic_class(self) -> Optional["PositiveInteger"]:
        """Get trafficClass (Pythonic accessor)."""
        return self._trafficClass

    @traffic_class.setter
    def traffic_class(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set trafficClass with validation.

        Args:
            value: The trafficClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficClass = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"trafficClass must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._trafficClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "CouplingPortTrafficClassAssignment":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getTrafficClass(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for trafficClass.

        Returns:
            The trafficClass value

        Note:
            Delegates to traffic_class property (CODING_RULE_V2_00017)
        """
        return self.traffic_class  # Delegates to property

    def setTrafficClass(self, value: "PositiveInteger") -> "CouplingPortTrafficClassAssignment":
        """
        AUTOSAR-compliant setter for trafficClass with method chaining.

        Args:
            value: The trafficClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to traffic_class property setter (gets validation automatically)
        """
        self.traffic_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_priority(self, value: "PositiveInteger") -> "CouplingPortTrafficClassAssignment":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_traffic_class(self, value: Optional["PositiveInteger"]) -> "CouplingPortTrafficClassAssignment":
        """
        Set trafficClass and return self for chaining.

        Args:
            value: The trafficClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traffic_class("value")
        """
        self.traffic_class = value  # Use property setter (gets validation)
        return self
