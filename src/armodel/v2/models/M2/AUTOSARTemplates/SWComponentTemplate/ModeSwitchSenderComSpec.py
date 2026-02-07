from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeSwitchSenderComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to mode
    communication

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ModeSwitchSenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 190, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to "true" the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enhancedMode must be Boolean or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # ModeDeclarationGroupPrototype (of the same Port to which these communication
        # attributes apply.
        self._modeGroup: RefType = None

    @property
    def mode_group(self) -> RefType:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: RefType) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value
        # If this aggregation exists an acknowledgement for the successful processing
        # of the mode switch request is.
        self._modeSwitched: Optional["ModeSwitchedAck"] = None

    @property
    def mode_switched(self) -> Optional["ModeSwitchedAck"]:
        """Get modeSwitched (Pythonic accessor)."""
        return self._modeSwitched

    @mode_switched.setter
    def mode_switched(self, value: Optional["ModeSwitchedAck"]) -> None:
        """
        Set modeSwitched with validation.

        Args:
            value: The modeSwitched to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeSwitched = None
            return

        if not isinstance(value, ModeSwitchedAck):
            raise TypeError(
                f"modeSwitched must be ModeSwitchedAck or None, got {type(value).__name__}"
            )
        self._modeSwitched = value
        # Length of call queue on the mode user side.
        # The queue is the RTE.
        # The value shall be greater or 1.
        # Setting the value of queueLength to 1 implies requests are rejected while
                # another request earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"queueLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    def getModeSwitched(self) -> "ModeSwitchedAck":
        """
        AUTOSAR-compliant getter for modeSwitched.

        Returns:
            The modeSwitched value

        Note:
            Delegates to mode_switched property (CODING_RULE_V2_00017)
        """
        return self.mode_switched  # Delegates to property

    def setModeSwitched(self, value: "ModeSwitchedAck") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for modeSwitched with method chaining.

        Args:
            value: The modeSwitched to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_switched property setter (gets validation automatically)
        """
        self.mode_switched = value  # Delegates to property setter
        return self

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "ModeSwitchSenderComSpec":
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_mode_group(self, value: Optional[RefType]) -> "ModeSwitchSenderComSpec":
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self

    def with_mode_switched(self, value: Optional["ModeSwitchedAck"]) -> "ModeSwitchSenderComSpec":
        """
        Set modeSwitched and return self for chaining.

        Args:
            value: The modeSwitched to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_switched("value")
        """
        self.mode_switched = value  # Use property setter (gets validation)
        return self

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "ModeSwitchSenderComSpec":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self
