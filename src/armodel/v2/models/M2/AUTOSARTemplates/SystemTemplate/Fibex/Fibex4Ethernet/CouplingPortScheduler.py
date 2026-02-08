from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortStructuralElement


class CouplingPortScheduler(CouplingPortStructuralElement):
    """
    Defines a scheduler for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortScheduler

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 123, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the schedule algorithm to be used.
        self._portSchedulerSchedulerEnum: Optional["EthernetCouplingPort"] = None

    @property
    def port_scheduler_scheduler_enum(self) -> Optional["EthernetCouplingPort"]:
        """Get portSchedulerSchedulerEnum (Pythonic accessor)."""
        return self._portSchedulerSchedulerEnum

    @port_scheduler_scheduler_enum.setter
    def port_scheduler_scheduler_enum(self, value: Optional["EthernetCouplingPort"]) -> None:
        """
        Set portSchedulerSchedulerEnum with validation.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portSchedulerSchedulerEnum = None
            return

        if not isinstance(value, EthernetCouplingPort):
            raise TypeError(
                f"portSchedulerSchedulerEnum must be EthernetCouplingPort or None, got {type(value).__name__}"
            )
        self._portSchedulerSchedulerEnum = value
        # Ordered List of predecessor inputs.
        # The first element has the highest priority.
        # The following elements have.
        self._predecessor: List["CouplingPortStructural"] = []

    @property
    def predecessor(self) -> List["CouplingPortStructural"]:
        """Get predecessor (Pythonic accessor)."""
        return self._predecessor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortSchedulerSchedulerEnum(self) -> "EthernetCouplingPort":
        """
        AUTOSAR-compliant getter for portSchedulerSchedulerEnum.

        Returns:
            The portSchedulerSchedulerEnum value

        Note:
            Delegates to port_scheduler_scheduler_enum property (CODING_RULE_V2_00017)
        """
        return self.port_scheduler_scheduler_enum  # Delegates to property

    def setPortSchedulerSchedulerEnum(self, value: "EthernetCouplingPort") -> "CouplingPortScheduler":
        """
        AUTOSAR-compliant setter for portSchedulerSchedulerEnum with method chaining.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_scheduler_scheduler_enum property setter (gets validation automatically)
        """
        self.port_scheduler_scheduler_enum = value  # Delegates to property setter
        return self

    def getPredecessor(self) -> List["CouplingPortStructural"]:
        """
        AUTOSAR-compliant getter for predecessor.

        Returns:
            The predecessor value

        Note:
            Delegates to predecessor property (CODING_RULE_V2_00017)
        """
        return self.predecessor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port_scheduler_scheduler_enum(self, value: Optional["EthernetCouplingPort"]) -> "CouplingPortScheduler":
        """
        Set portSchedulerSchedulerEnum and return self for chaining.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_scheduler_scheduler_enum("value")
        """
        self.port_scheduler_scheduler_enum = value  # Use property setter (gets validation)
        return self
