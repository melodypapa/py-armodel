from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class J1939ControllerApplication(ARElement):
    """
    This element represents a J1939 controller application.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::J1939ControllerApplication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 207, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the numerical function id of the application.
        self._functionId: Optional["PositiveInteger"] = None

    @property
    def function_id(self) -> Optional["PositiveInteger"]:
        """Get functionId (Pythonic accessor)."""
        return self._functionId

    @function_id.setter
    def function_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionId with validation.

        Args:
            value: The functionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"functionId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._functionId = value
        # typically typed by a CompositionSwComponentType) that the
                # J1939ControllerApplication.
        # by: ComponentInSystem.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.

        Args:
            value: The swComponent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionId.

        Returns:
            The functionId value

        Note:
            Delegates to function_id property (CODING_RULE_V2_00017)
        """
        return self.function_id  # Delegates to property

    def setFunctionId(self, value: "PositiveInteger") -> "J1939ControllerApplication":
        """
        AUTOSAR-compliant setter for functionId with method chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_id property setter (gets validation automatically)
        """
        self.function_id = value  # Delegates to property setter
        return self

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "J1939ControllerApplication":
        """
        AUTOSAR-compliant setter for swComponent with method chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "J1939ControllerApplication":
        """
        Set functionId and return self for chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_id("value")
        """
        self.function_id = value  # Use property setter (gets validation)
        return self

    def with_sw_component(self, value: Optional["SwComponent"]) -> "J1939ControllerApplication":
        """
        Set swComponent and return self for chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self
