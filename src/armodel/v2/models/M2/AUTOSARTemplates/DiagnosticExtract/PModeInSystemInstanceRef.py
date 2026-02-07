from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PModeInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs::PModeInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 370, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.

        Args:
            value: The context to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # Tags: xml.
        # sequenceOffset=50.
        self._contextModeGroup: RefType = None

    @property
    def context_mode_group(self) -> RefType:
        """Get contextModeGroup (Pythonic accessor)."""
        return self._contextModeGroup

    @context_mode_group.setter
    def context_mode_group(self, value: RefType) -> None:
        """
        Set contextModeGroup with validation.

        Args:
            value: The contextModeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextModeGroup = None
            return

        self._contextModeGroup = value
        # Tags: xml.
        # sequenceOffset=40.
        self._contextPPortPrototype: Optional["AbstractProvidedPort"] = None

    @property
    def context_p_port_prototype(self) -> Optional["AbstractProvidedPort"]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # Tags: xml.
        # sequenceOffset=60.
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

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "PModeInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getContextModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextModeGroup.

        Returns:
            The contextModeGroup value

        Note:
            Delegates to context_mode_group property (CODING_RULE_V2_00017)
        """
        return self.context_mode_group  # Delegates to property

    def setContextModeGroup(self, value: RefType) -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextModeGroup with method chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_mode_group property setter (gets validation automatically)
        """
        self.context_mode_group = value  # Delegates to property setter
        return self

    def getContextPPortPrototype(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: "AbstractProvidedPort") -> "PModeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
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

    def setTargetMode(self, value: "ModeDeclaration") -> "PModeInSystemInstanceRef":
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

    def with_base(self, value: Optional["System"]) -> "PModeInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "PModeInSystemInstanceRef":
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_mode_group(self, value: Optional[RefType]) -> "PModeInSystemInstanceRef":
        """
        Set contextModeGroup and return self for chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_mode_group("value")
        """
        self.context_mode_group = value  # Use property setter (gets validation)
        return self

    def with_context_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> "PModeInSystemInstanceRef":
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "PModeInSystemInstanceRef":
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
