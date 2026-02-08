from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Integer,
    LinFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LinOrderedConfigurableFrame(ARObject):
    """
    With the assignment of the index to a frame a mapping of Pids to Frames is
    possible. This element shall be used for the LIN 2.1 Assign-Frame-PID-Range
    command.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinOrderedConfigurableFrame

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 99, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a Frame that is processed by the slave.
        self._frame: Optional["LinFrame"] = None

    @property
    def frame(self) -> Optional["LinFrame"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["LinFrame"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, LinFrame):
            raise TypeError(
                f"frame must be LinFrame or None, got {type(value).__name__}"
            )
        self._frame = value
        # This attribute is used to order the elements and allows an Pids to
        # ConfigurableFrames that are the slave.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> "LinFrame":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "LinFrame") -> "LinOrderedConfigurableFrame":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "LinOrderedConfigurableFrame":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["LinFrame"]) -> "LinOrderedConfigurableFrame":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_index(self, value: Optional["Integer"]) -> "LinOrderedConfigurableFrame":
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
