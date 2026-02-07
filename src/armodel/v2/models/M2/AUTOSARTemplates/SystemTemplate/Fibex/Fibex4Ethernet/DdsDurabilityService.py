from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsDurabilityService(ARObject):
    """
    Describes the DDS DURABILITY_SERVICE QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDurabilityService

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 530, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DURABILITY_SERVICE" chapter in DDS.
        # atp.
        # Status=candidate SamplesPer.
        self._durability: Optional["PositiveInteger"] = None

    @property
    def durability(self) -> Optional["PositiveInteger"]:
        """Get durability (Pythonic accessor)."""
        return self._durability

    @durability.setter
    def durability(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set durability with validation.

        Args:
            value: The durability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._durability = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"durability must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._durability = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDurability(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for durability.

        Returns:
            The durability value

        Note:
            Delegates to durability property (CODING_RULE_V2_00017)
        """
        return self.durability  # Delegates to property

    def setDurability(self, value: "PositiveInteger") -> "DdsDurabilityService":
        """
        AUTOSAR-compliant setter for durability with method chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Note:
            Delegates to durability property setter (gets validation automatically)
        """
        self.durability = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_durability(self, value: Optional["PositiveInteger"]) -> "DdsDurabilityService":
        """
        Set durability and return self for chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_durability("value")
        """
        self.durability = value  # Use property setter (gets validation)
        return self
