from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventCom,
)


class TDEventFrame(TDEventCom):
    """
    This is used to describe timing events related to the exchange of frames
    between the communication controller and the bus specific (FlexRay / CAN /
    LIN) Interface BSW module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 67, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._frame: Optional["Frame"] = None

    @property
    def frame(self) -> Optional["Frame"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["Frame"]) -> None:
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

        if not isinstance(value, Frame):
            raise TypeError(
                f"frame must be Frame or None, got {type(value).__name__}"
            )
        self._frame = value
        # The PhysicalChannel on which the Frame is transmitted.
        self._physical: Optional["PhysicalChannel"] = None

    @property
    def physical(self) -> Optional["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value
        # The specific type of this timing event.
        self._tdEventTypeEnum: Optional["TDEventFrameType"] = None

    @property
    def td_event_type_enum(self) -> Optional["TDEventFrameType"]:
        """Get tdEventTypeEnum (Pythonic accessor)."""
        return self._tdEventTypeEnum

    @td_event_type_enum.setter
    def td_event_type_enum(self, value: Optional["TDEventFrameType"]) -> None:
        """
        Set tdEventTypeEnum with validation.

        Args:
            value: The tdEventTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTypeEnum = None
            return

        if not isinstance(value, TDEventFrameType):
            raise TypeError(
                f"tdEventTypeEnum must be TDEventFrameType or None, got {type(value).__name__}"
            )
        self._tdEventTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> "Frame":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "Frame") -> "TDEventFrame":
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

    def getPhysical(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalChannel") -> "TDEventFrame":
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    def getTdEventTypeEnum(self) -> "TDEventFrameType":
        """
        AUTOSAR-compliant getter for tdEventTypeEnum.

        Returns:
            The tdEventTypeEnum value

        Note:
            Delegates to td_event_type_enum property (CODING_RULE_V2_00017)
        """
        return self.td_event_type_enum  # Delegates to property

    def setTdEventTypeEnum(self, value: "TDEventFrameType") -> "TDEventFrame":
        """
        AUTOSAR-compliant setter for tdEventTypeEnum with method chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type_enum property setter (gets validation automatically)
        """
        self.td_event_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["Frame"]) -> "TDEventFrame":
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

    def with_physical(self, value: Optional["PhysicalChannel"]) -> "TDEventFrame":
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_td_event_type_enum(self, value: Optional["TDEventFrameType"]) -> "TDEventFrame":
        """
        Set tdEventTypeEnum and return self for chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type_enum("value")
        """
        self.td_event_type_enum = value  # Use property setter (gets validation)
        return self
