from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """
    Each frame in FlexRay is identified by its slot id and communication cycle.
    A description is provided by the usage of AbsolutelyScheduledTiming. In the
    static segment a frame can be sent multiple times within one communication
    cycle. For describing this case multiple AbsolutelyScheduledTimings have to
    be used. The main use case would be that a frame is sent twice within one
    communication cycle.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 423, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The communication cycle where the frame is sent.
        self._communicationCycle: Optional["CommunicationCycle"] = None

    @property
    def communication_cycle(self) -> Optional["CommunicationCycle"]:
        """Get communicationCycle (Pythonic accessor)."""
        return self._communicationCycle

    @communication_cycle.setter
    def communication_cycle(self, value: Optional["CommunicationCycle"]) -> None:
        """
        Set communicationCycle with validation.

        Args:
            value: The communicationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communicationCycle = None
            return

        if not isinstance(value, CommunicationCycle):
            raise TypeError(
                f"communicationCycle must be CommunicationCycle or None, got {type(value).__name__}"
            )
        self._communicationCycle = value
        # In the static part the SlotID defines the slot in which the transmitted.
        # The SlotID also determines, in FlexrayCluster::numberOfStaticSlots, frame is
                # sent in static or dynamic segment.
        # In part, the slot id is equivalent to a priority.
        # slot ids are all sent until the end of the Higher numbers, which were ignored
                # have to wait one cycle and then shall try again.
        self._slotID: Optional["PositiveInteger"] = None

    @property
    def slot_id(self) -> Optional["PositiveInteger"]:
        """Get slotID (Pythonic accessor)."""
        return self._slotID

    @slot_id.setter
    def slot_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set slotID with validation.

        Args:
            value: The slotID to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slotID = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"slotID must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._slotID = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunicationCycle(self) -> "CommunicationCycle":
        """
        AUTOSAR-compliant getter for communicationCycle.

        Returns:
            The communicationCycle value

        Note:
            Delegates to communication_cycle property (CODING_RULE_V2_00017)
        """
        return self.communication_cycle  # Delegates to property

    def setCommunicationCycle(self, value: "CommunicationCycle") -> "FlexrayAbsolutelyScheduledTiming":
        """
        AUTOSAR-compliant setter for communicationCycle with method chaining.

        Args:
            value: The communicationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication_cycle property setter (gets validation automatically)
        """
        self.communication_cycle = value  # Delegates to property setter
        return self

    def getSlotID(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for slotID.

        Returns:
            The slotID value

        Note:
            Delegates to slot_id property (CODING_RULE_V2_00017)
        """
        return self.slot_id  # Delegates to property

    def setSlotID(self, value: "PositiveInteger") -> "FlexrayAbsolutelyScheduledTiming":
        """
        AUTOSAR-compliant setter for slotID with method chaining.

        Args:
            value: The slotID to set

        Returns:
            self for method chaining

        Note:
            Delegates to slot_id property setter (gets validation automatically)
        """
        self.slot_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication_cycle(self, value: Optional["CommunicationCycle"]) -> "FlexrayAbsolutelyScheduledTiming":
        """
        Set communicationCycle and return self for chaining.

        Args:
            value: The communicationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication_cycle("value")
        """
        self.communication_cycle = value  # Use property setter (gets validation)
        return self

    def with_slot_id(self, value: Optional["PositiveInteger"]) -> "FlexrayAbsolutelyScheduledTiming":
        """
        Set slotID and return self for chaining.

        Args:
            value: The slotID to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slot_id("value")
        """
        self.slot_id = value  # Use property setter (gets validation)
        return self
