from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    FramePid,
    Integer,
    LinConfigurationEntry,
)


class AssignFrameIdRange(LinConfigurationEntry):
    """
    AssignFrameIdRange generates an assign frame PID range request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::AssignFrameIdRange

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 437, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the request.
        # The frame_PIDs are ordered.
        self._framePid: "FramePid" = None

    @property
    def frame_pid(self) -> "FramePid":
        """Get framePid (Pythonic accessor)."""
        return self._framePid

    @frame_pid.setter
    def frame_pid(self, value: "FramePid") -> None:
        """
        Set framePid with validation.

        Args:
            value: The framePid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, FramePid):
            raise TypeError(
                f"framePid must be FramePid, got {type(value).__name__}"
            )
        self._framePid = value
        # The startIndex sets the index to the first frame to assign a.
        self._startIndex: Optional["Integer"] = None

    @property
    def start_index(self) -> Optional["Integer"]:
        """Get startIndex (Pythonic accessor)."""
        return self._startIndex

    @start_index.setter
    def start_index(self, value: Optional["Integer"]) -> None:
        """
        Set startIndex with validation.

        Args:
            value: The startIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startIndex = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"startIndex must be Integer or None, got {type(value).__name__}"
            )
        self._startIndex = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFramePid(self) -> "FramePid":
        """
        AUTOSAR-compliant getter for framePid.

        Returns:
            The framePid value

        Note:
            Delegates to frame_pid property (CODING_RULE_V2_00017)
        """
        return self.frame_pid  # Delegates to property

    def setFramePid(self, value: "FramePid") -> "AssignFrameIdRange":
        """
        AUTOSAR-compliant setter for framePid with method chaining.

        Args:
            value: The framePid to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_pid property setter (gets validation automatically)
        """
        self.frame_pid = value  # Delegates to property setter
        return self

    def getStartIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for startIndex.

        Returns:
            The startIndex value

        Note:
            Delegates to start_index property (CODING_RULE_V2_00017)
        """
        return self.start_index  # Delegates to property

    def setStartIndex(self, value: "Integer") -> "AssignFrameIdRange":
        """
        AUTOSAR-compliant setter for startIndex with method chaining.

        Args:
            value: The startIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to start_index property setter (gets validation automatically)
        """
        self.start_index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_pid(self, value: "FramePid") -> "AssignFrameIdRange":
        """
        Set framePid and return self for chaining.

        Args:
            value: The framePid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_pid("value")
        """
        self.frame_pid = value  # Use property setter (gets validation)
        return self

    def with_start_index(self, value: Optional["Integer"]) -> "AssignFrameIdRange":
        """
        Set startIndex and return self for chaining.

        Args:
            value: The startIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start_index("value")
        """
        self.start_index = value  # Use property setter (gets validation)
        return self
