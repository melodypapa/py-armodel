from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class FlexrayFifoConfiguration(ARObject):
    """
    One First In First Out (FIFO) queued receive structure, defining the
    admittance criteria to the FIFO, and mandating the ability to admit messages
    into the FIFO based on Message Id filtering criteria.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology::FlexrayFifoConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Boolean configuration which determines whether or not received in the dynamic
        # segment that don’t message ID will be admitted into the FIFO.
        self._admitWithout: Optional["Boolean"] = None

    @property
    def admit_without(self) -> Optional["Boolean"]:
        """Get admitWithout (Pythonic accessor)."""
        return self._admitWithout

    @admit_without.setter
    def admit_without(self, value: Optional["Boolean"]) -> None:
        """
        Set admitWithout with validation.

        Args:
            value: The admitWithout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._admitWithout = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"admitWithout must be Boolean or None, got {type(value).__name__}"
            )
        self._admitWithout = value
        # FIFO cycle counter acceptance criteria.
        self._baseCycle: Optional["Integer"] = None

    @property
    def base_cycle(self) -> Optional["Integer"]:
        """Get baseCycle (Pythonic accessor)."""
        return self._baseCycle

    @base_cycle.setter
    def base_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set baseCycle with validation.

        Args:
            value: The baseCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"baseCycle must be Integer or None, got {type(value).__name__}"
            )
        self._baseCycle = value
        # Fifo channel admittance criteria.
        self._channel: Optional["FlexrayPhysicalChannel"] = None

    @property
    def channel(self) -> Optional["FlexrayPhysicalChannel"]:
        """Get channel (Pythonic accessor)."""
        return self._channel

    @channel.setter
    def channel(self, value: Optional["FlexrayPhysicalChannel"]) -> None:
        """
        Set channel with validation.

        Args:
            value: The channel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channel = None
            return

        if not isinstance(value, FlexrayPhysicalChannel):
            raise TypeError(
                f"channel must be FlexrayPhysicalChannel or None, got {type(value).__name__}"
            )
        self._channel = value
        # FIFO cycle counter acceptance criteria.
        self._cycleRepetition: Optional["Integer"] = None

    @property
    def cycle_repetition(self) -> Optional["Integer"]:
        """Get cycleRepetition (Pythonic accessor)."""
        return self._cycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional["Integer"]) -> None:
        """
        Set cycleRepetition with validation.

        Args:
            value: The cycleRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleRepetition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"cycleRepetition must be Integer or None, got {type(value).__name__}"
            )
        self._cycleRepetition = value
        # FrFifoDepth configures the maximum number of can be contained in the FIFO.
        self._fifoDepth: Optional["Integer"] = None

    @property
    def fifo_depth(self) -> Optional["Integer"]:
        """Get fifoDepth (Pythonic accessor)."""
        return self._fifoDepth

    @fifo_depth.setter
    def fifo_depth(self, value: Optional["Integer"]) -> None:
        """
        Set fifoDepth with validation.

        Args:
            value: The fifoDepth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fifoDepth = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"fifoDepth must be Integer or None, got {type(value).__name__}"
            )
        self._fifoDepth = value
        # FIFO Frame Id range acceptance criteria.
        self._fifoRange: List["FlexrayFifoRange"] = []

    @property
    def fifo_range(self) -> List["FlexrayFifoRange"]:
        """Get fifoRange (Pythonic accessor)."""
        return self._fifoRange
        # FIFO message identifier acceptance criteria (Mask filter).
        self._msgIdMask: Optional["Integer"] = None

    @property
    def msg_id_mask(self) -> Optional["Integer"]:
        """Get msgIdMask (Pythonic accessor)."""
        return self._msgIdMask

    @msg_id_mask.setter
    def msg_id_mask(self, value: Optional["Integer"]) -> None:
        """
        Set msgIdMask with validation.

        Args:
            value: The msgIdMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msgIdMask = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"msgIdMask must be Integer or None, got {type(value).__name__}"
            )
        self._msgIdMask = value
        # FIFO message identifier acceptance criteria (Match filter).
        self._msgIdMatch: Optional["Integer"] = None

    @property
    def msg_id_match(self) -> Optional["Integer"]:
        """Get msgIdMatch (Pythonic accessor)."""
        return self._msgIdMatch

    @msg_id_match.setter
    def msg_id_match(self, value: Optional["Integer"]) -> None:
        """
        Set msgIdMatch with validation.

        Args:
            value: The msgIdMatch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msgIdMatch = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"msgIdMatch must be Integer or None, got {type(value).__name__}"
            )
        self._msgIdMatch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdmitWithout(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for admitWithout.

        Returns:
            The admitWithout value

        Note:
            Delegates to admit_without property (CODING_RULE_V2_00017)
        """
        return self.admit_without  # Delegates to property

    def setAdmitWithout(self, value: "Boolean") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for admitWithout with method chaining.

        Args:
            value: The admitWithout to set

        Returns:
            self for method chaining

        Note:
            Delegates to admit_without property setter (gets validation automatically)
        """
        self.admit_without = value  # Delegates to property setter
        return self

    def getBaseCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for baseCycle.

        Returns:
            The baseCycle value

        Note:
            Delegates to base_cycle property (CODING_RULE_V2_00017)
        """
        return self.base_cycle  # Delegates to property

    def setBaseCycle(self, value: "Integer") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for baseCycle with method chaining.

        Args:
            value: The baseCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_cycle property setter (gets validation automatically)
        """
        self.base_cycle = value  # Delegates to property setter
        return self

    def getChannel(self) -> "FlexrayPhysicalChannel":
        """
        AUTOSAR-compliant getter for channel.

        Returns:
            The channel value

        Note:
            Delegates to channel property (CODING_RULE_V2_00017)
        """
        return self.channel  # Delegates to property

    def setChannel(self, value: "FlexrayPhysicalChannel") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for channel with method chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel property setter (gets validation automatically)
        """
        self.channel = value  # Delegates to property setter
        return self

    def getCycleRepetition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for cycleRepetition.

        Returns:
            The cycleRepetition value

        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: "Integer") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for cycleRepetition with method chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    def getFifoDepth(self) -> "Integer":
        """
        AUTOSAR-compliant getter for fifoDepth.

        Returns:
            The fifoDepth value

        Note:
            Delegates to fifo_depth property (CODING_RULE_V2_00017)
        """
        return self.fifo_depth  # Delegates to property

    def setFifoDepth(self, value: "Integer") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for fifoDepth with method chaining.

        Args:
            value: The fifoDepth to set

        Returns:
            self for method chaining

        Note:
            Delegates to fifo_depth property setter (gets validation automatically)
        """
        self.fifo_depth = value  # Delegates to property setter
        return self

    def getFifoRange(self) -> List["FlexrayFifoRange"]:
        """
        AUTOSAR-compliant getter for fifoRange.

        Returns:
            The fifoRange value

        Note:
            Delegates to fifo_range property (CODING_RULE_V2_00017)
        """
        return self.fifo_range  # Delegates to property

    def getMsgIdMask(self) -> "Integer":
        """
        AUTOSAR-compliant getter for msgIdMask.

        Returns:
            The msgIdMask value

        Note:
            Delegates to msg_id_mask property (CODING_RULE_V2_00017)
        """
        return self.msg_id_mask  # Delegates to property

    def setMsgIdMask(self, value: "Integer") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for msgIdMask with method chaining.

        Args:
            value: The msgIdMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to msg_id_mask property setter (gets validation automatically)
        """
        self.msg_id_mask = value  # Delegates to property setter
        return self

    def getMsgIdMatch(self) -> "Integer":
        """
        AUTOSAR-compliant getter for msgIdMatch.

        Returns:
            The msgIdMatch value

        Note:
            Delegates to msg_id_match property (CODING_RULE_V2_00017)
        """
        return self.msg_id_match  # Delegates to property

    def setMsgIdMatch(self, value: "Integer") -> "FlexrayFifoConfiguration":
        """
        AUTOSAR-compliant setter for msgIdMatch with method chaining.

        Args:
            value: The msgIdMatch to set

        Returns:
            self for method chaining

        Note:
            Delegates to msg_id_match property setter (gets validation automatically)
        """
        self.msg_id_match = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_admit_without(self, value: Optional["Boolean"]) -> "FlexrayFifoConfiguration":
        """
        Set admitWithout and return self for chaining.

        Args:
            value: The admitWithout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_admit_without("value")
        """
        self.admit_without = value  # Use property setter (gets validation)
        return self

    def with_base_cycle(self, value: Optional["Integer"]) -> "FlexrayFifoConfiguration":
        """
        Set baseCycle and return self for chaining.

        Args:
            value: The baseCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_cycle("value")
        """
        self.base_cycle = value  # Use property setter (gets validation)
        return self

    def with_channel(self, value: Optional["FlexrayPhysicalChannel"]) -> "FlexrayFifoConfiguration":
        """
        Set channel and return self for chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel("value")
        """
        self.channel = value  # Use property setter (gets validation)
        return self

    def with_cycle_repetition(self, value: Optional["Integer"]) -> "FlexrayFifoConfiguration":
        """
        Set cycleRepetition and return self for chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self

    def with_fifo_depth(self, value: Optional["Integer"]) -> "FlexrayFifoConfiguration":
        """
        Set fifoDepth and return self for chaining.

        Args:
            value: The fifoDepth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fifo_depth("value")
        """
        self.fifo_depth = value  # Use property setter (gets validation)
        return self

    def with_msg_id_mask(self, value: Optional["Integer"]) -> "FlexrayFifoConfiguration":
        """
        Set msgIdMask and return self for chaining.

        Args:
            value: The msgIdMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msg_id_mask("value")
        """
        self.msg_id_mask = value  # Use property setter (gets validation)
        return self

    def with_msg_id_match(self, value: Optional["Integer"]) -> "FlexrayFifoConfiguration":
        """
        Set msgIdMatch and return self for chaining.

        Args:
            value: The msgIdMatch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msg_id_match("value")
        """
        self.msg_id_match = value  # Use property setter (gets validation)
        return self
