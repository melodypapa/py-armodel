from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ContainedIPduProps,
    Pdu,
)


class IPdu(Pdu, ABC):
    """
    The IPdu (Interaction Layer Protocol Data Unit) element is used to sum up
    all Pdus that are routed by the PduR.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPdu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 341, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 226, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether this IPdu may be collected inside a.
        self._containedIPdu: Optional["ContainedIPduProps"] = None

    @property
    def contained_i_pdu(self) -> Optional["ContainedIPduProps"]:
        """Get containedIPdu (Pythonic accessor)."""
        return self._containedIPdu

    @contained_i_pdu.setter
    def contained_i_pdu(self, value: Optional["ContainedIPduProps"]) -> None:
        """
        Set containedIPdu with validation.

        Args:
            value: The containedIPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containedIPdu = None
            return

        if not isinstance(value, ContainedIPduProps):
            raise TypeError(
                f"containedIPdu must be ContainedIPduProps or None, got {type(value).__name__}"
            )
        self._containedIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainedIPdu(self) -> "ContainedIPduProps":
        """
        AUTOSAR-compliant getter for containedIPdu.

        Returns:
            The containedIPdu value

        Note:
            Delegates to contained_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_i_pdu  # Delegates to property

    def setContainedIPdu(self, value: "ContainedIPduProps") -> "IPdu":
        """
        AUTOSAR-compliant setter for containedIPdu with method chaining.

        Args:
            value: The containedIPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to contained_i_pdu property setter (gets validation automatically)
        """
        self.contained_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_contained_i_pdu(self, value: Optional["ContainedIPduProps"]) -> "IPdu":
        """
        Set containedIPdu and return self for chaining.

        Args:
            value: The containedIPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_contained_i_pdu("value")
        """
        self.contained_i_pdu = value  # Use property setter (gets validation)
        return self
