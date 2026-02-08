from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector


class LinCommunicationConnector(CommunicationConnector):
    """
    LIN bus specific communication connector attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 98, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Initial NAD of the LIN slave.
        self._initialNad: Optional["Integer"] = None

    @property
    def initial_nad(self) -> Optional["Integer"]:
        """Get initialNad (Pythonic accessor)."""
        return self._initialNad

    @initial_nad.setter
    def initial_nad(self, value: Optional["Integer"]) -> None:
        """
        Set initialNad with validation.

        Args:
            value: The initialNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialNad must be Integer or None, got {type(value).__name__}"
            )
        self._initialNad = value
        # LinConfigurableFrames shall list all frames (unconditional event-triggered
                # frames and sporadic frames) the slave node.
        # This element is necessary LIN 2.
        # 0 Assign-Frame command.
        self._linConfigurable: List["LinConfigurableFrame"] = []

    @property
    def lin_configurable(self) -> List["LinConfigurableFrame"]:
        """Get linConfigurable (Pythonic accessor)."""
        return self._linConfigurable
        # LinOrderedConfigurableFrames shall list all frames (unconditional frames,
                # event-triggered frames and frames) processed by the slave node.
        # This necessary for the LIN 2.
        # 1.
        self._linOrdered: List["LinOrderedConfigurable"] = []

    @property
    def lin_ordered(self) -> List["LinOrderedConfigurable"]:
        """Get linOrdered (Pythonic accessor)."""
        return self._linOrdered
        # This attribute defines the point in time where a schedule switch is
                # performed.
        # If this attribute is set to false or present, the schedule table shall be
                # switched after the of the active schedule table is ended.
        # If this enabled, the schedule table shall be switched transmission or
                # reception within an entry completed, ensured by status checks for reception.
        self._schedule: Optional["Boolean"] = None

    @property
    def schedule(self) -> Optional["Boolean"]:
        """Get schedule (Pythonic accessor)."""
        return self._schedule

    @schedule.setter
    def schedule(self, value: Optional["Boolean"]) -> None:
        """
        Set schedule with validation.

        Args:
            value: The schedule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._schedule = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"schedule must be Boolean or None, got {type(value).__name__}"
            )
        self._schedule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialNad.

        Returns:
            The initialNad value

        Note:
            Delegates to initial_nad property (CODING_RULE_V2_00017)
        """
        return self.initial_nad  # Delegates to property

    def setInitialNad(self, value: "Integer") -> "LinCommunicationConnector":
        """
        AUTOSAR-compliant setter for initialNad with method chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_nad property setter (gets validation automatically)
        """
        self.initial_nad = value  # Delegates to property setter
        return self

    def getLinConfigurable(self) -> List["LinConfigurableFrame"]:
        """
        AUTOSAR-compliant getter for linConfigurable.

        Returns:
            The linConfigurable value

        Note:
            Delegates to lin_configurable property (CODING_RULE_V2_00017)
        """
        return self.lin_configurable  # Delegates to property

    def getLinOrdered(self) -> List["LinOrderedConfigurable"]:
        """
        AUTOSAR-compliant getter for linOrdered.

        Returns:
            The linOrdered value

        Note:
            Delegates to lin_ordered property (CODING_RULE_V2_00017)
        """
        return self.lin_ordered  # Delegates to property

    def getSchedule(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for schedule.

        Returns:
            The schedule value

        Note:
            Delegates to schedule property (CODING_RULE_V2_00017)
        """
        return self.schedule  # Delegates to property

    def setSchedule(self, value: "Boolean") -> "LinCommunicationConnector":
        """
        AUTOSAR-compliant setter for schedule with method chaining.

        Args:
            value: The schedule to set

        Returns:
            self for method chaining

        Note:
            Delegates to schedule property setter (gets validation automatically)
        """
        self.schedule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinCommunicationConnector":
        """
        Set initialNad and return self for chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_nad("value")
        """
        self.initial_nad = value  # Use property setter (gets validation)
        return self

    def with_schedule(self, value: Optional["Boolean"]) -> "LinCommunicationConnector":
        """
        Set schedule and return self for chaining.

        Args:
            value: The schedule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_schedule("value")
        """
        self.schedule = value  # Use property setter (gets validation)
        return self
