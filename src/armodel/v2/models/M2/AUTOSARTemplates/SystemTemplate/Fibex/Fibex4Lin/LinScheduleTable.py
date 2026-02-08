from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class LinScheduleTable(Identifiable):
    """
    The master task (in the master node) transmits frame headers based on a
    schedule table. The schedule table specifies the identifiers for each header
    and the interval between the start of a frame and the start of the following
    frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 432, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines, where a schedule table shall be proceeded in it has been interrupted
        # by a run-once table or.
        self._resumePosition: Optional["ResumePosition"] = None

    @property
    def resume_position(self) -> Optional["ResumePosition"]:
        """Get resumePosition (Pythonic accessor)."""
        return self._resumePosition

    @resume_position.setter
    def resume_position(self, value: Optional["ResumePosition"]) -> None:
        """
        Set resumePosition with validation.

        Args:
            value: The resumePosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resumePosition = None
            return

        if not isinstance(value, ResumePosition):
            raise TypeError(
                f"resumePosition must be ResumePosition or None, got {type(value).__name__}"
            )
        self._resumePosition = value
        # The schedule table can be executed in two different.
        self._runMode: Optional["RunMode"] = None

    @property
    def run_mode(self) -> Optional["RunMode"]:
        """Get runMode (Pythonic accessor)."""
        return self._runMode

    @run_mode.setter
    def run_mode(self, value: Optional["RunMode"]) -> None:
        """
        Set runMode with validation.

        Args:
            value: The runMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runMode = None
            return

        if not isinstance(value, RunMode):
            raise TypeError(
                f"runMode must be RunMode or None, got {type(value).__name__}"
            )
        self._runMode = value
        # The scheduling table consists of table entries, which slots.
        self._tableEntry: List["ScheduleTableEntry"] = []

    @property
    def table_entry(self) -> List["ScheduleTableEntry"]:
        """Get tableEntry (Pythonic accessor)."""
        return self._tableEntry

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResumePosition(self) -> "ResumePosition":
        """
        AUTOSAR-compliant getter for resumePosition.

        Returns:
            The resumePosition value

        Note:
            Delegates to resume_position property (CODING_RULE_V2_00017)
        """
        return self.resume_position  # Delegates to property

    def setResumePosition(self, value: "ResumePosition") -> "LinScheduleTable":
        """
        AUTOSAR-compliant setter for resumePosition with method chaining.

        Args:
            value: The resumePosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to resume_position property setter (gets validation automatically)
        """
        self.resume_position = value  # Delegates to property setter
        return self

    def getRunMode(self) -> "RunMode":
        """
        AUTOSAR-compliant getter for runMode.

        Returns:
            The runMode value

        Note:
            Delegates to run_mode property (CODING_RULE_V2_00017)
        """
        return self.run_mode  # Delegates to property

    def setRunMode(self, value: "RunMode") -> "LinScheduleTable":
        """
        AUTOSAR-compliant setter for runMode with method chaining.

        Args:
            value: The runMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to run_mode property setter (gets validation automatically)
        """
        self.run_mode = value  # Delegates to property setter
        return self

    def getTableEntry(self) -> List["ScheduleTableEntry"]:
        """
        AUTOSAR-compliant getter for tableEntry.

        Returns:
            The tableEntry value

        Note:
            Delegates to table_entry property (CODING_RULE_V2_00017)
        """
        return self.table_entry  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_resume_position(self, value: Optional["ResumePosition"]) -> "LinScheduleTable":
        """
        Set resumePosition and return self for chaining.

        Args:
            value: The resumePosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resume_position("value")
        """
        self.resume_position = value  # Use property setter (gets validation)
        return self

    def with_run_mode(self, value: Optional["RunMode"]) -> "LinScheduleTable":
        """
        Set runMode and return self for chaining.

        Args:
            value: The runMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_run_mode("value")
        """
        self.run_mode = value  # Use property setter (gets validation)
        return self
