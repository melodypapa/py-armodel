from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TtcanAbsolutelyScheduledTiming(ARObject):
    """
    Each frame in TTCAN is identified by its slot id and communication cycle. A
    description is provided by the usage of AbsolutelyScheduledTiming. A frame
    can be sent multiple times within one communication cycle. For describing
    this case multiple AbsolutelyScheduledTimings have to be used. The main use
    case would be that a frame is sent twice within one communication cycle.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 450, Classic Platform R23-11)
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
        # Where FlexRay counts the slots in the static segment, explicit Tx and Rx time
        # marks.
        self._timeMark: Optional["Integer"] = None

    @property
    def time_mark(self) -> Optional["Integer"]:
        """Get timeMark (Pythonic accessor)."""
        return self._timeMark

    @time_mark.setter
    def time_mark(self, value: Optional["Integer"]) -> None:
        """
        Set timeMark with validation.

        Args:
            value: The timeMark to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeMark = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"timeMark must be Integer or None, got {type(value).__name__}"
            )
        self._timeMark = value
        # Trigger type for this time window.
        self._trigger: RefType = None

    @property
    def trigger(self) -> RefType:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: RefType) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

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

    def setCommunicationCycle(self, value: "CommunicationCycle") -> "TtcanAbsolutelyScheduledTiming":
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

    def getTimeMark(self) -> "Integer":
        """
        AUTOSAR-compliant getter for timeMark.

        Returns:
            The timeMark value

        Note:
            Delegates to time_mark property (CODING_RULE_V2_00017)
        """
        return self.time_mark  # Delegates to property

    def setTimeMark(self, value: "Integer") -> "TtcanAbsolutelyScheduledTiming":
        """
        AUTOSAR-compliant setter for timeMark with method chaining.

        Args:
            value: The timeMark to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_mark property setter (gets validation automatically)
        """
        self.time_mark = value  # Delegates to property setter
        return self

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> "TtcanAbsolutelyScheduledTiming":
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication_cycle(self, value: Optional["CommunicationCycle"]) -> "TtcanAbsolutelyScheduledTiming":
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

    def with_time_mark(self, value: Optional["Integer"]) -> "TtcanAbsolutelyScheduledTiming":
        """
        Set timeMark and return self for chaining.

        Args:
            value: The timeMark to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_mark("value")
        """
        self.time_mark = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional[RefType]) -> "TtcanAbsolutelyScheduledTiming":
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self
