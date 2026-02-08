from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractInternalReferenceDef


class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify references within the ECU Configuration Description between
    parameter containers.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 73, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 442, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 189, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Exactly one reference to a parameter container is allowed.
        self._destination: Optional["EcucContainerDef"] = None

    @property
    def destination(self) -> Optional["EcucContainerDef"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["EcucContainerDef"]) -> None:
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

        if not isinstance(value, EcucContainerDef):
            raise TypeError(
                f"destination must be EcucContainerDef or None, got {type(value).__name__}"
            )
        self._destination = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> "EcucContainerDef":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "EcucContainerDef") -> "EcucReferenceDef":
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

    def with_destination(self, value: Optional["EcucContainerDef"]) -> "EcucReferenceDef":
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
