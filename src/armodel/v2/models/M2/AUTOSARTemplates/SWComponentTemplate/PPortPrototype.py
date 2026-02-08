from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.AbstractProvidedPortPrototype import (
    AbstractProvidedPortPrototype,
)


class PPortPrototype(AbstractProvidedPortPrototype):
    """
    Component port providing a certain port interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 68, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2041, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 234, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # isOfType.
        self._provided: Optional["PortInterface"] = None

    @property
    def provided(self) -> Optional["PortInterface"]:
        """Get provided (Pythonic accessor)."""
        return self._provided

    @provided.setter
    def provided(self, value: Optional["PortInterface"]) -> None:
        """
        Set provided with validation.

        Args:
            value: The provided to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provided = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"provided must be PortInterface or None, got {type(value).__name__}"
            )
        self._provided = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvided(self) -> "PortInterface":
        """
        AUTOSAR-compliant getter for provided.

        Returns:
            The provided value

        Note:
            Delegates to provided property (CODING_RULE_V2_00017)
        """
        return self.provided  # Delegates to property

    def setProvided(self, value: "PortInterface") -> "PPortPrototype":
        """
        AUTOSAR-compliant setter for provided with method chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided property setter (gets validation automatically)
        """
        self.provided = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided(self, value: Optional["PortInterface"]) -> "PPortPrototype":
        """
        Set provided and return self for chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided("value")
        """
        self.provided = value  # Use property setter (gets validation)
        return self
