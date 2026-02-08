from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class NetworkSegmentIdentification(ARObject):
    """
    This meta-class represents the ability to identify the PhysicalChannel on a
    system scope in a numerical way. One possible application of this approach
    is the Time Validation.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::NetworkSegmentIdentification

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 859, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the numerical identifier of a on system level
        # scope.
        self._network: Optional["PositiveInteger"] = None

    @property
    def network(self) -> Optional["PositiveInteger"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"network must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._network = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetwork(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "PositiveInteger") -> "NetworkSegmentIdentification":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_network(self, value: Optional["PositiveInteger"]) -> "NetworkSegmentIdentification":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self
