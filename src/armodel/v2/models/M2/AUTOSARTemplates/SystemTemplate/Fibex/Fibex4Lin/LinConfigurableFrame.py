from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import LinFrame
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class LinConfigurableFrame(ARObject):
    """
    Assignment of messageIds to Frames. This element shall be used for the LIN
    2.0 Assign-Frame command.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinConfigurableFrame

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
        # MessageId for the referenced frame.
        self._messageId: Optional["PositiveInteger"] = None

    @property
    def message_id(self) -> Optional["PositiveInteger"]:
        """Get messageId (Pythonic accessor)."""
        return self._messageId

    @message_id.setter
    def message_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set messageId with validation.

        Args:
            value: The messageId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageId = value

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

    def setFrame(self, value: "LinFrame") -> "LinConfigurableFrame":
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

    def getMessageId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageId.

        Returns:
            The messageId value

        Note:
            Delegates to message_id property (CODING_RULE_V2_00017)
        """
        return self.message_id  # Delegates to property

    def setMessageId(self, value: "PositiveInteger") -> "LinConfigurableFrame":
        """
        AUTOSAR-compliant setter for messageId with method chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_id property setter (gets validation automatically)
        """
        self.message_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["LinFrame"]) -> "LinConfigurableFrame":
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

    def with_message_id(self, value: Optional["PositiveInteger"]) -> "LinConfigurableFrame":
        """
        Set messageId and return self for chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_id("value")
        """
        self.message_id = value  # Use property setter (gets validation)
        return self
