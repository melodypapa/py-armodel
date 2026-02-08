from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractCanCommunicationControllerAttributes,
    Integer,
)


class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """
    This element is used for the specification of the exact CAN Bit Timing
    configuration parameter values.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies propagation delay in time quantas.
        self._propSeg: Optional["Integer"] = None

    @property
    def prop_seg(self) -> Optional["Integer"]:
        """Get propSeg (Pythonic accessor)."""
        return self._propSeg

    @prop_seg.setter
    def prop_seg(self, value: Optional["Integer"]) -> None:
        """
        Set propSeg with validation.

        Args:
            value: The propSeg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propSeg = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"propSeg must be Integer or None, got {type(value).__name__}"
            )
        self._propSeg = value
        # The number of quanta in the Synchronization Jump The (Re-)Synchronization
        # Jump Width how far a resynchronization may move the inside the limits defined
        # by the Phase Buffer compensate for edge phase errors.
        self._syncJumpWidth: Optional["Integer"] = None

    @property
    def sync_jump_width(self) -> Optional["Integer"]:
        """Get syncJumpWidth (Pythonic accessor)."""
        return self._syncJumpWidth

    @sync_jump_width.setter
    def sync_jump_width(self, value: Optional["Integer"]) -> None:
        """
        Set syncJumpWidth with validation.

        Args:
            value: The syncJumpWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncJumpWidth = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"syncJumpWidth must be Integer or None, got {type(value).__name__}"
            )
        self._syncJumpWidth = value
        # Specifies phase segment 1 in time quantas.
        # Phase_Seg1.
        self._timeSeg1: Optional["Integer"] = None

    @property
    def time_seg1(self) -> Optional["Integer"]:
        """Get timeSeg1 (Pythonic accessor)."""
        return self._timeSeg1

    @time_seg1.setter
    def time_seg1(self, value: Optional["Integer"]) -> None:
        """
        Set timeSeg1 with validation.

        Args:
            value: The timeSeg1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg1 = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"timeSeg1 must be Integer or None, got {type(value).__name__}"
            )
        self._timeSeg1 = value
        # Specifies phase segment 2 in time quantas.
        # Phase_Seg2.
        self._timeSeg2: Optional["Integer"] = None

    @property
    def time_seg2(self) -> Optional["Integer"]:
        """Get timeSeg2 (Pythonic accessor)."""
        return self._timeSeg2

    @time_seg2.setter
    def time_seg2(self, value: Optional["Integer"]) -> None:
        """
        Set timeSeg2 with validation.

        Args:
            value: The timeSeg2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg2 = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"timeSeg2 must be Integer or None, got {type(value).__name__}"
            )
        self._timeSeg2 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPropSeg(self) -> "Integer":
        """
        AUTOSAR-compliant getter for propSeg.

        Returns:
            The propSeg value

        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: "Integer") -> "CanControllerConfiguration":
        """
        AUTOSAR-compliant setter for propSeg with method chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Note:
            Delegates to prop_seg property setter (gets validation automatically)
        """
        self.prop_seg = value  # Delegates to property setter
        return self

    def getSyncJumpWidth(self) -> "Integer":
        """
        AUTOSAR-compliant getter for syncJumpWidth.

        Returns:
            The syncJumpWidth value

        Note:
            Delegates to sync_jump_width property (CODING_RULE_V2_00017)
        """
        return self.sync_jump_width  # Delegates to property

    def setSyncJumpWidth(self, value: "Integer") -> "CanControllerConfiguration":
        """
        AUTOSAR-compliant setter for syncJumpWidth with method chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_jump_width property setter (gets validation automatically)
        """
        self.sync_jump_width = value  # Delegates to property setter
        return self

    def getTimeSeg1(self) -> "Integer":
        """
        AUTOSAR-compliant getter for timeSeg1.

        Returns:
            The timeSeg1 value

        Note:
            Delegates to time_seg1 property (CODING_RULE_V2_00017)
        """
        return self.time_seg1  # Delegates to property

    def setTimeSeg1(self, value: "Integer") -> "CanControllerConfiguration":
        """
        AUTOSAR-compliant setter for timeSeg1 with method chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg1 property setter (gets validation automatically)
        """
        self.time_seg1 = value  # Delegates to property setter
        return self

    def getTimeSeg2(self) -> "Integer":
        """
        AUTOSAR-compliant getter for timeSeg2.

        Returns:
            The timeSeg2 value

        Note:
            Delegates to time_seg2 property (CODING_RULE_V2_00017)
        """
        return self.time_seg2  # Delegates to property

    def setTimeSeg2(self, value: "Integer") -> "CanControllerConfiguration":
        """
        AUTOSAR-compliant setter for timeSeg2 with method chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg2 property setter (gets validation automatically)
        """
        self.time_seg2 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_prop_seg(self, value: Optional["Integer"]) -> "CanControllerConfiguration":
        """
        Set propSeg and return self for chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prop_seg("value")
        """
        self.prop_seg = value  # Use property setter (gets validation)
        return self

    def with_sync_jump_width(self, value: Optional["Integer"]) -> "CanControllerConfiguration":
        """
        Set syncJumpWidth and return self for chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_jump_width("value")
        """
        self.sync_jump_width = value  # Use property setter (gets validation)
        return self

    def with_time_seg1(self, value: Optional["Integer"]) -> "CanControllerConfiguration":
        """
        Set timeSeg1 and return self for chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg1("value")
        """
        self.time_seg1 = value  # Use property setter (gets validation)
        return self

    def with_time_seg2(self, value: Optional["Integer"]) -> "CanControllerConfiguration":
        """
        Set timeSeg2 and return self for chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg2("value")
        """
        self.time_seg2 = value  # Use property setter (gets validation)
        return self
