from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class FramePid(ARObject):
    """
    Frame_PIDs that are included in the request. The "pid" attribute describes
    the value and the "index" attribute the position of the frame_PID in the
    request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::FramePid

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 437, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to order the frame_PIDs.
        # The values shall be unique within one AssignFrameIdRange.
        self._index: Optional["Integer"] = None

    @property
    def index(self) -> Optional["Integer"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["Integer"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"index must be Integer or None, got {type(value).__name__}"
            )
        self._index = value
        # Frame_PID value.
        self._pid: Optional["PositiveInteger"] = None

    @property
    def pid(self) -> Optional["PositiveInteger"]:
        """Get pid (Pythonic accessor)."""
        return self._pid

    @pid.setter
    def pid(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pid with validation.

        Args:
            value: The pid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pid = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pid must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "FramePid":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getPid(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pid.

        Returns:
            The pid value

        Note:
            Delegates to pid property (CODING_RULE_V2_00017)
        """
        return self.pid  # Delegates to property

    def setPid(self, value: "PositiveInteger") -> "FramePid":
        """
        AUTOSAR-compliant setter for pid with method chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Note:
            Delegates to pid property setter (gets validation automatically)
        """
        self.pid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional["Integer"]) -> "FramePid":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_pid(self, value: Optional["PositiveInteger"]) -> "FramePid":
        """
        Set pid and return self for chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pid("value")
        """
        self.pid = value  # Use property setter (gets validation)
        return self
