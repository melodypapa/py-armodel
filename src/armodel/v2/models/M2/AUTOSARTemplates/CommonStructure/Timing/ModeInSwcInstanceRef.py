from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInSwcInstanceRef(ARObject):
    """
    Instance reference to be capable of referencing a ModeDeclaration at a
    specific Mode Switch Port of a SW-C.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 38, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the SW component representing the base of the.
        self._base: Optional["SwComponentType"] = None

    @property
    def base(self) -> Optional["SwComponentType"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["SwComponentType"]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, SwComponentType):
            raise TypeError(
                f"base must be SwComponentType or None, got {type(value).__name__}"
            )
        self._base = value
        # Specifies the SW component prototype representing the context.
        self._context: List["SwComponent"] = []

    @property
    def context(self) -> List["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # Specifies the mode declaration group prototype that manifests the context.
        # xml.
        # sequenceOffset=40.
        self._contextMode: RefType = None

    @property
    def context_mode(self) -> RefType:
        """Get contextMode (Pythonic accessor)."""
        return self._contextMode

    @context_mode.setter
    def context_mode(self, value: RefType) -> None:
        """
        Set contextMode with validation.

        Args:
            value: The contextMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextMode = None
            return

        self._contextMode = value
        # Specifies the port prototype representing the context.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._contextPort: RefType = None

    @property
    def context_port(self) -> RefType:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: RefType) -> None:
        """
        Set contextPort with validation.

        Args:
            value: The contextPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPort = None
            return

        self._contextPort = value
        # Specifies the specific mode declaration in the given.
        self._targetMode: Optional["ModeDeclaration"] = None

    @property
    def target_mode(self) -> Optional["ModeDeclaration"]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "SwComponentType":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "SwComponentType") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContext(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getContextMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextMode.

        Returns:
            The contextMode value

        Note:
            Delegates to context_mode property (CODING_RULE_V2_00017)
        """
        return self.context_mode  # Delegates to property

    def setContextMode(self, value: RefType) -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextMode with method chaining.

        Args:
            value: The contextMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_mode property setter (gets validation automatically)
        """
        self.context_mode = value  # Delegates to property setter
        return self

    def getContextPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextPort.

        Returns:
            The contextPort value

        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: RefType) -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextPort with method chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_port property setter (gets validation automatically)
        """
        self.context_port = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["SwComponentType"]) -> "ModeInSwcInstanceRef":
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_context_mode(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """
        Set contextMode and return self for chaining.

        Args:
            value: The contextMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_mode("value")
        """
        self.context_mode = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """
        Set contextPort and return self for chaining.

        Args:
            value: The contextPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_port("value")
        """
        self.context_port = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "ModeInSwcInstanceRef":
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
