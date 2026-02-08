from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """
    An event triggered frame is used as a placeholder to allow multiple slave
    nodes to provide its response. The header of an event triggered frame is
    transmitted when a frame slot allocated to the event triggered frame is
    processed. The publisher of an associated unconditional frame shall only
    transmit the response if at least one of the signals carried in its
    unconditional frame is updated. The LIN Master discovers and purges
    collisions with the collisionResolvingScheduleTable. The event controlled
    frame shall not contain any Pdus.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 430, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the schedule table, which resolves a.
        self._collisionSchedule: Optional["LinScheduleTable"] = None

    @property
    def collision_schedule(self) -> Optional["LinScheduleTable"]:
        """Get collisionSchedule (Pythonic accessor)."""
        return self._collisionSchedule

    @collision_schedule.setter
    def collision_schedule(self, value: Optional["LinScheduleTable"]) -> None:
        """
        Set collisionSchedule with validation.

        Args:
            value: The collisionSchedule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collisionSchedule = None
            return

        if not isinstance(value, LinScheduleTable):
            raise TypeError(
                f"collisionSchedule must be LinScheduleTable or None, got {type(value).__name__}"
            )
        self._collisionSchedule = value
        # A list of slaves can respond to the master request if at one of the signals
                # carried in its unconditional frame For each response a LinFrameTriggering and
                # shall be defined.
        # Within a LIN Frame shall be referenced by only one allows a derivation of the
                # identifier substituted Frame.
        # The identifier is specified in The Unconditional frames an event triggered
                # frame shall: equal length.
        # the same checksum model (i.
        # e.
        # mixing LIN 1.
        # x and frames is not allowed).
        # the first data field to its protected identifier the associated unconditional
                # frame is a unconditional frame in the same or table).
        # published by different slave nodes.
        # not be included directly in the same schedule the event triggered frame is
                # scheduled.
        self._linUnconditional: List["LinUnconditionalFrame"] = []

    @property
    def lin_unconditional(self) -> List["LinUnconditionalFrame"]:
        """Get linUnconditional (Pythonic accessor)."""
        return self._linUnconditional

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollisionSchedule(self) -> "LinScheduleTable":
        """
        AUTOSAR-compliant getter for collisionSchedule.

        Returns:
            The collisionSchedule value

        Note:
            Delegates to collision_schedule property (CODING_RULE_V2_00017)
        """
        return self.collision_schedule  # Delegates to property

    def setCollisionSchedule(self, value: "LinScheduleTable") -> "LinEventTriggeredFrame":
        """
        AUTOSAR-compliant setter for collisionSchedule with method chaining.

        Args:
            value: The collisionSchedule to set

        Returns:
            self for method chaining

        Note:
            Delegates to collision_schedule property setter (gets validation automatically)
        """
        self.collision_schedule = value  # Delegates to property setter
        return self

    def getLinUnconditional(self) -> List["LinUnconditionalFrame"]:
        """
        AUTOSAR-compliant getter for linUnconditional.

        Returns:
            The linUnconditional value

        Note:
            Delegates to lin_unconditional property (CODING_RULE_V2_00017)
        """
        return self.lin_unconditional  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collision_schedule(self, value: Optional["LinScheduleTable"]) -> "LinEventTriggeredFrame":
        """
        Set collisionSchedule and return self for chaining.

        Args:
            value: The collisionSchedule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collision_schedule("value")
        """
        self.collision_schedule = value  # Use property setter (gets validation)
        return self
