from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import EOCExecutableEntityRefAbstract


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """
    This is used to define a reference to an ExecutableEntity If the
    ExecutionOrderConstraint is defined on VFB, System or ECU level, a reference
    to the Sw ComponentPrototype, via the ComponentInCompositionInstanceRef, the
    referenced ExecutableEntity belongs to, shall be provided as context
    information.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::EOCExecutableEntityRef

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 120, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the BSW module instance the BSW module belongs to.
        self._bswModule: Optional["BswImplementation"] = None

    @property
    def bsw_module(self) -> Optional["BswImplementation"]:
        """Get bswModule (Pythonic accessor)."""
        return self._bswModule

    @bsw_module.setter
    def bsw_module(self, value: Optional["BswImplementation"]) -> None:
        """
        Set bswModule with validation.

        Args:
            value: The bswModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModule = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"bswModule must be BswImplementation or None, got {type(value).__name__}"
            )
        self._bswModule = value
        # prototype.
        # by: ComponentIn.
        self._componentCompositionInstanceRef: Optional["SwComponent"] = None

    @property
    def component_composition_instance_ref(self) -> Optional["SwComponent"]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional["SwComponent"]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value
        # The ExecutableEntity whose execution order is restricted contraint.
        self._executable: Optional["ExecutableEntity"] = None

    @property
    def executable(self) -> Optional["ExecutableEntity"]:
        """Get executable (Pythonic accessor)."""
        return self._executable

    @executable.setter
    def executable(self, value: Optional["ExecutableEntity"]) -> None:
        """
        Set executable with validation.

        Args:
            value: The executable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executable = None
            return

        if not isinstance(value, ExecutableEntity):
            raise TypeError(
                f"executable must be ExecutableEntity or None, got {type(value).__name__}"
            )
        self._executable = value
        # The logical successor of an executable entity or a group executable entities.
        self._successor: List["EOCExecutableEntity"] = []

    @property
    def successor(self) -> List["EOCExecutableEntity"]:
        """Get successor (Pythonic accessor)."""
        return self._successor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModule(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for bswModule.

        Returns:
            The bswModule value

        Note:
            Delegates to bsw_module property (CODING_RULE_V2_00017)
        """
        return self.bsw_module  # Delegates to property

    def setBswModule(self, value: "BswImplementation") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for bswModule with method chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module property setter (gets validation automatically)
        """
        self.bsw_module = value  # Delegates to property setter
        return self

    def getComponentCompositionInstanceRef(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: "SwComponent") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    def getExecutable(self) -> "ExecutableEntity":
        """
        AUTOSAR-compliant getter for executable.

        Returns:
            The executable value

        Note:
            Delegates to executable property (CODING_RULE_V2_00017)
        """
        return self.executable  # Delegates to property

    def setExecutable(self, value: "ExecutableEntity") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for executable with method chaining.

        Args:
            value: The executable to set

        Returns:
            self for method chaining

        Note:
            Delegates to executable property setter (gets validation automatically)
        """
        self.executable = value  # Delegates to property setter
        return self

    def getSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for successor.

        Returns:
            The successor value

        Note:
            Delegates to successor property (CODING_RULE_V2_00017)
        """
        return self.successor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module(self, value: Optional["BswImplementation"]) -> "EOCExecutableEntityRef":
        """
        Set bswModule and return self for chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module("value")
        """
        self.bsw_module = value  # Use property setter (gets validation)
        return self

    def with_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> "EOCExecutableEntityRef":
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_executable(self, value: Optional["ExecutableEntity"]) -> "EOCExecutableEntityRef":
        """
        Set executable and return self for chaining.

        Args:
            value: The executable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_executable("value")
        """
        self.executable = value  # Use property setter (gets validation)
        return self
