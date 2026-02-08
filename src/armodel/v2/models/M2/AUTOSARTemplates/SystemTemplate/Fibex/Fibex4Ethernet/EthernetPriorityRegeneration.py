from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class EthernetPriorityRegeneration(Referrable):
    """
    Defines a priority regeneration where the ingressPriority is replaced by
    regeneratedPriority. The ethernetPriorityRegeneration is optional in case no
    priority regeneration shall be performed. In case a
    ethernetPriorityRegeneration is defined it shall have 8 mappings, one for
    each priority.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetPriorityRegeneration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 128, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Message priority of the incoming message.
        self._ingressPriority: Optional["PositiveInteger"] = None

    @property
    def ingress_priority(self) -> Optional["PositiveInteger"]:
        """Get ingressPriority (Pythonic accessor)."""
        return self._ingressPriority

    @ingress_priority.setter
    def ingress_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ingressPriority with validation.

        Args:
            value: The ingressPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ingressPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ingressPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ingressPriority = value
        # Regenerated message priority.
        # 0-7.
        self._regenerated: Optional["PositiveInteger"] = None

    @property
    def regenerated(self) -> Optional["PositiveInteger"]:
        """Get regenerated (Pythonic accessor)."""
        return self._regenerated

    @regenerated.setter
    def regenerated(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set regenerated with validation.

        Args:
            value: The regenerated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._regenerated = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"regenerated must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._regenerated = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIngressPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ingressPriority.

        Returns:
            The ingressPriority value

        Note:
            Delegates to ingress_priority property (CODING_RULE_V2_00017)
        """
        return self.ingress_priority  # Delegates to property

    def setIngressPriority(self, value: "PositiveInteger") -> "EthernetPriorityRegeneration":
        """
        AUTOSAR-compliant setter for ingressPriority with method chaining.

        Args:
            value: The ingressPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to ingress_priority property setter (gets validation automatically)
        """
        self.ingress_priority = value  # Delegates to property setter
        return self

    def getRegenerated(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for regenerated.

        Returns:
            The regenerated value

        Note:
            Delegates to regenerated property (CODING_RULE_V2_00017)
        """
        return self.regenerated  # Delegates to property

    def setRegenerated(self, value: "PositiveInteger") -> "EthernetPriorityRegeneration":
        """
        AUTOSAR-compliant setter for regenerated with method chaining.

        Args:
            value: The regenerated to set

        Returns:
            self for method chaining

        Note:
            Delegates to regenerated property setter (gets validation automatically)
        """
        self.regenerated = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ingress_priority(self, value: Optional["PositiveInteger"]) -> "EthernetPriorityRegeneration":
        """
        Set ingressPriority and return self for chaining.

        Args:
            value: The ingressPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ingress_priority("value")
        """
        self.ingress_priority = value  # Use property setter (gets validation)
        return self

    def with_regenerated(self, value: Optional["PositiveInteger"]) -> "EthernetPriorityRegeneration":
        """
        Set regenerated and return self for chaining.

        Args:
            value: The regenerated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_regenerated("value")
        """
        self.regenerated = value  # Use property setter (gets validation)
        return self
