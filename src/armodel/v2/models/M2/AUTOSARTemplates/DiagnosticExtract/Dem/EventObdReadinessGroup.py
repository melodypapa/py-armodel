from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EventObdReadinessGroup(ARObject):
    """
    This meta-class represents the ability to define the value of attribute
    eventObdReadinessGroup. It is only introduced to allow for a variant
    modeling of this attribute.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::EventObdReadinessGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 176, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the Event OBD Readiness group PID $01 and PID $41
                # computation.
        # This attribute is applicable for emission-related ECUs.
        self._eventObd: Optional["NameToken"] = None

    @property
    def event_obd(self) -> Optional["NameToken"]:
        """Get eventObd (Pythonic accessor)."""
        return self._eventObd

    @event_obd.setter
    def event_obd(self, value: Optional["NameToken"]) -> None:
        """
        Set eventObd with validation.

        Args:
            value: The eventObd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventObd = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"eventObd must be NameToken or None, got {type(value).__name__}"
            )
        self._eventObd = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventObd(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for eventObd.

        Returns:
            The eventObd value

        Note:
            Delegates to event_obd property (CODING_RULE_V2_00017)
        """
        return self.event_obd  # Delegates to property

    def setEventObd(self, value: "NameToken") -> "EventObdReadinessGroup":
        """
        AUTOSAR-compliant setter for eventObd with method chaining.

        Args:
            value: The eventObd to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_obd property setter (gets validation automatically)
        """
        self.event_obd = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_obd(self, value: Optional["NameToken"]) -> "EventObdReadinessGroup":
        """
        Set eventObd and return self for chaining.

        Args:
            value: The eventObd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_obd("value")
        """
        self.event_obd = value  # Use property setter (gets validation)
        return self
