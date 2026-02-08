from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DdsDurabilityKindEnum
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsDurability(ARObject):
    """
    Describes the DDS DURABILITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDurability

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 530, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DURABILITY" chapter in DDS.
        self._durabilityKind: Optional["DdsDurabilityKindEnum"] = None

    @property
    def durability_kind(self) -> Optional["DdsDurabilityKindEnum"]:
        """Get durabilityKind (Pythonic accessor)."""
        return self._durabilityKind

    @durability_kind.setter
    def durability_kind(self, value: Optional["DdsDurabilityKindEnum"]) -> None:
        """
        Set durabilityKind with validation.

        Args:
            value: The durabilityKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._durabilityKind = None
            return

        if not isinstance(value, DdsDurabilityKindEnum):
            raise TypeError(
                f"durabilityKind must be DdsDurabilityKindEnum or None, got {type(value).__name__}"
            )
        self._durabilityKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDurabilityKind(self) -> "DdsDurabilityKindEnum":
        """
        AUTOSAR-compliant getter for durabilityKind.

        Returns:
            The durabilityKind value

        Note:
            Delegates to durability_kind property (CODING_RULE_V2_00017)
        """
        return self.durability_kind  # Delegates to property

    def setDurabilityKind(self, value: "DdsDurabilityKindEnum") -> "DdsDurability":
        """
        AUTOSAR-compliant setter for durabilityKind with method chaining.

        Args:
            value: The durabilityKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to durability_kind property setter (gets validation automatically)
        """
        self.durability_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_durability_kind(self, value: Optional["DdsDurabilityKindEnum"]) -> "DdsDurability":
        """
        Set durabilityKind and return self for chaining.

        Args:
            value: The durabilityKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_durability_kind("value")
        """
        self.durability_kind = value  # Use property setter (gets validation)
        return self
