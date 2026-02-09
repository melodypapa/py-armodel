from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class HardwareConfiguration(ARObject):
    """
    Describes in which mode the hardware is operating while needing this
    resource consumption.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 161, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies additional information on the Hardware.
        self._additional: Optional["String"] = None

    @property
    def additional(self) -> Optional["String"]:
        """Get additional (Pythonic accessor)."""
        return self._additional

    @additional.setter
    def additional(self, value: Optional["String"]) -> None:
        """
        Set additional with validation.

        Args:
            value: The additional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._additional = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"additional must be String or None, got {type(value).__name__}"
            )
        self._additional = value
        # Specifies in which mode the processor is operating.
        self._processorMode: Optional["String"] = None

    @property
    def processor_mode(self) -> Optional["String"]:
        """Get processorMode (Pythonic accessor)."""
        return self._processorMode

    @processor_mode.setter
    def processor_mode(self, value: Optional["String"]) -> None:
        """
        Set processorMode with validation.

        Args:
            value: The processorMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processorMode = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"processorMode must be String or None, got {type(value).__name__}"
            )
        self._processorMode = value
        # Specifies the speed the processor is operating.
        self._processorSpeed: Optional["String"] = None

    @property
    def processor_speed(self) -> Optional["String"]:
        """Get processorSpeed (Pythonic accessor)."""
        return self._processorSpeed

    @processor_speed.setter
    def processor_speed(self, value: Optional["String"]) -> None:
        """
        Set processorSpeed with validation.

        Args:
            value: The processorSpeed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processorSpeed = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"processorSpeed must be String or None, got {type(value).__name__}"
            )
        self._processorSpeed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdditional(self) -> "String":
        """
        AUTOSAR-compliant getter for additional.

        Returns:
            The additional value

        Note:
            Delegates to additional property (CODING_RULE_V2_00017)
        """
        return self.additional  # Delegates to property

    def setAdditional(self, value: "String") -> "HardwareConfiguration":
        """
        AUTOSAR-compliant setter for additional with method chaining.

        Args:
            value: The additional to set

        Returns:
            self for method chaining

        Note:
            Delegates to additional property setter (gets validation automatically)
        """
        self.additional = value  # Delegates to property setter
        return self

    def getProcessorMode(self) -> "String":
        """
        AUTOSAR-compliant getter for processorMode.

        Returns:
            The processorMode value

        Note:
            Delegates to processor_mode property (CODING_RULE_V2_00017)
        """
        return self.processor_mode  # Delegates to property

    def setProcessorMode(self, value: "String") -> "HardwareConfiguration":
        """
        AUTOSAR-compliant setter for processorMode with method chaining.

        Args:
            value: The processorMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to processor_mode property setter (gets validation automatically)
        """
        self.processor_mode = value  # Delegates to property setter
        return self

    def getProcessorSpeed(self) -> "String":
        """
        AUTOSAR-compliant getter for processorSpeed.

        Returns:
            The processorSpeed value

        Note:
            Delegates to processor_speed property (CODING_RULE_V2_00017)
        """
        return self.processor_speed  # Delegates to property

    def setProcessorSpeed(self, value: "String") -> "HardwareConfiguration":
        """
        AUTOSAR-compliant setter for processorSpeed with method chaining.

        Args:
            value: The processorSpeed to set

        Returns:
            self for method chaining

        Note:
            Delegates to processor_speed property setter (gets validation automatically)
        """
        self.processor_speed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_additional(self, value: Optional["String"]) -> "HardwareConfiguration":
        """
        Set additional and return self for chaining.

        Args:
            value: The additional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_additional("value")
        """
        self.additional = value  # Use property setter (gets validation)
        return self

    def with_processor_mode(self, value: Optional["String"]) -> "HardwareConfiguration":
        """
        Set processorMode and return self for chaining.

        Args:
            value: The processorMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processor_mode("value")
        """
        self.processor_mode = value  # Use property setter (gets validation)
        return self

    def with_processor_speed(self, value: Optional["String"]) -> "HardwareConfiguration":
        """
        Set processorSpeed and return self for chaining.

        Args:
            value: The processorSpeed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processor_speed("value")
        """
        self.processor_speed = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SoftwareContext(ARObject):
    """
    Specifies the context of the software for this resource consumption.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 163, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the input vector which is used to provide the.
        self._input: Optional["String"] = None

    @property
    def input(self) -> Optional["String"]:
        """Get input (Pythonic accessor)."""
        return self._input

    @input.setter
    def input(self, value: Optional["String"]) -> None:
        """
        Set input with validation.

        Args:
            value: The input to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._input = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"input must be String or None, got {type(value).__name__}"
            )
        self._input = value
        # Specifies the state the software is in when the Execution provided.
        self._state: Optional["String"] = None

    @property
    def state(self) -> Optional["String"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["String"]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"state must be String or None, got {type(value).__name__}"
            )
        self._state = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInput(self) -> "String":
        """
        AUTOSAR-compliant getter for input.

        Returns:
            The input value

        Note:
            Delegates to input property (CODING_RULE_V2_00017)
        """
        return self.input  # Delegates to property

    def setInput(self, value: "String") -> "SoftwareContext":
        """
        AUTOSAR-compliant setter for input with method chaining.

        Args:
            value: The input to set

        Returns:
            self for method chaining

        Note:
            Delegates to input property setter (gets validation automatically)
        """
        self.input = value  # Delegates to property setter
        return self

    def getState(self) -> "String":
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "String") -> "SoftwareContext":
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_input(self, value: Optional["String"]) -> "SoftwareContext":
        """
        Set input and return self for chaining.

        Args:
            value: The input to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_input("value")
        """
        self.input = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["String"]) -> "SoftwareContext":
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self


__all__ = [
    "HardwareConfiguration",
    "SoftwareContext",
]
