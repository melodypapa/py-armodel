from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsTransportPriority(ARObject):
    """
    Describes the DDS TRANSPORT_PRIORITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsTransportPriority

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 535, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "TRANSPORT_PRIORITY" chapter of DDS.
        self._transportPriority: Optional["PositiveInteger"] = None

    @property
    def transport_priority(self) -> Optional["PositiveInteger"]:
        """Get transportPriority (Pythonic accessor)."""
        return self._transportPriority

    @transport_priority.setter
    def transport_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set transportPriority with validation.

        Args:
            value: The transportPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"transportPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._transportPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransportPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for transportPriority.

        Returns:
            The transportPriority value

        Note:
            Delegates to transport_priority property (CODING_RULE_V2_00017)
        """
        return self.transport_priority  # Delegates to property

    def setTransportPriority(self, value: "PositiveInteger") -> "DdsTransportPriority":
        """
        AUTOSAR-compliant setter for transportPriority with method chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_priority property setter (gets validation automatically)
        """
        self.transport_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transport_priority(self, value: Optional["PositiveInteger"]) -> "DdsTransportPriority":
        """
        Set transportPriority and return self for chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_priority("value")
        """
        self.transport_priority = value  # Use property setter (gets validation)
        return self
