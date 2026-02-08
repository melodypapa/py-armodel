from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DdsDestinationOrder(ARObject):
    """
    Describes the DDS DESTINATION_ORDER QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 536, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DESTINATION_ORDER" chapter of DDS.
        # Tags: atp.
        # Status=candidate.
        self._destination: Optional["DdsDestinationOrder"] = None

    @property
    def destination(self) -> Optional["DdsDestinationOrder"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["DdsDestinationOrder"]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, DdsDestinationOrder):
            raise TypeError(
                f"destination must be DdsDestinationOrder or None, got {type(value).__name__}"
            )
        self._destination = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> "DdsDestinationOrder":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "DdsDestinationOrder") -> "DdsDestinationOrder":
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional["DdsDestinationOrder"]) -> "DdsDestinationOrder":
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self
