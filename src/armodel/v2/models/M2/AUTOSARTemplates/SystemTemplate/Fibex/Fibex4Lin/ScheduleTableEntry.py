from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ScheduleTableEntry(ARObject, ABC):
    """
    Table entry in a LinScheduleTable. Specifies what will be done in the frame
    slot.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::ScheduleTableEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ScheduleTableEntry:
            raise TypeError("ScheduleTableEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Relative delay between this tableEntry and the start of the the schedule
        # table in seconds.
        self._delay: Optional["TimeValue"] = None

    @property
    def delay(self) -> Optional["TimeValue"]:
        """Get delay (Pythonic accessor)."""
        return self._delay

    @delay.setter
    def delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set delay with validation.

        Args:
            value: The delay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._delay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"delay must be TimeValue or None, got {type(value).__name__}"
            )
        self._delay = value
        # This represents introductory documentation about the entry.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
        # Relative position in the schedule table.
        # The first entry the schedule table is 0.
        self._positionInTable: Optional["Integer"] = None

    @property
    def position_in_table(self) -> Optional["Integer"]:
        """Get positionInTable (Pythonic accessor)."""
        return self._positionInTable

    @position_in_table.setter
    def position_in_table(self, value: Optional["Integer"]) -> None:
        """
        Set positionInTable with validation.

        Args:
            value: The positionInTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._positionInTable = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"positionInTable must be Integer or None, got {type(value).__name__}"
            )
        self._positionInTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for delay.

        Returns:
            The delay value

        Note:
            Delegates to delay property (CODING_RULE_V2_00017)
        """
        return self.delay  # Delegates to property

    def setDelay(self, value: "TimeValue") -> "ScheduleTableEntry":
        """
        AUTOSAR-compliant setter for delay with method chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Note:
            Delegates to delay property setter (gets validation automatically)
        """
        self.delay = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "ScheduleTableEntry":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getPositionInTable(self) -> "Integer":
        """
        AUTOSAR-compliant getter for positionInTable.

        Returns:
            The positionInTable value

        Note:
            Delegates to position_in_table property (CODING_RULE_V2_00017)
        """
        return self.position_in_table  # Delegates to property

    def setPositionInTable(self, value: "Integer") -> "ScheduleTableEntry":
        """
        AUTOSAR-compliant setter for positionInTable with method chaining.

        Args:
            value: The positionInTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to position_in_table property setter (gets validation automatically)
        """
        self.position_in_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_delay(self, value: Optional["TimeValue"]) -> "ScheduleTableEntry":
        """
        Set delay and return self for chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delay("value")
        """
        self.delay = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "ScheduleTableEntry":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_position_in_table(self, value: Optional["Integer"]) -> "ScheduleTableEntry":
        """
        Set positionInTable and return self for chaining.

        Args:
            value: The positionInTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_position_in_table("value")
        """
        self.position_in_table = value  # Use property setter (gets validation)
        return self
