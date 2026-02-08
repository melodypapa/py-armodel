from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DdsDeadline(ARObject):
    """
    Describes the DDS DEADLINE QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DEADLINE" chapter of DDS.
        # in seconds.
        self._deadlinePeriod: Optional["Float"] = None

    @property
    def deadline_period(self) -> Optional["Float"]:
        """Get deadlinePeriod (Pythonic accessor)."""
        return self._deadlinePeriod

    @deadline_period.setter
    def deadline_period(self, value: Optional["Float"]) -> None:
        """
        Set deadlinePeriod with validation.

        Args:
            value: The deadlinePeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._deadlinePeriod = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"deadlinePeriod must be Float or None, got {type(value).__name__}"
            )
        self._deadlinePeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeadlinePeriod(self) -> "Float":
        """
        AUTOSAR-compliant getter for deadlinePeriod.

        Returns:
            The deadlinePeriod value

        Note:
            Delegates to deadline_period property (CODING_RULE_V2_00017)
        """
        return self.deadline_period  # Delegates to property

    def setDeadlinePeriod(self, value: "Float") -> "DdsDeadline":
        """
        AUTOSAR-compliant setter for deadlinePeriod with method chaining.

        Args:
            value: The deadlinePeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to deadline_period property setter (gets validation automatically)
        """
        self.deadline_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_deadline_period(self, value: Optional["Float"]) -> "DdsDeadline":
        """
        Set deadlinePeriod and return self for chaining.

        Args:
            value: The deadlinePeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_deadline_period("value")
        """
        self.deadline_period = value  # Use property setter (gets validation)
        return self
