from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    RootSwComposition,
    SwComponent,
    System,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ComponentInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::ComponentInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 999, Classic Platform R23-11)
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
        # sequenceOffset=40.
        self._target: "SwComponent" = None

    @property
    def target(self) -> "SwComponent":
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: "SwComponent") -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SwComponent):
            raise TypeError(
                f"target must be SwComponent, got {type(value).__name__}"
            )
        self._target = value

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

    def setBase(self, value: "System") -> "ComponentInSystemInstanceRef":
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

    def setContext(self, value: "RootSwComposition") -> "ComponentInSystemInstanceRef":
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

    def getTarget(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "SwComponent") -> "ComponentInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "ComponentInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "ComponentInSystemInstanceRef":
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

    def with_target(self, value: "SwComponent") -> "ComponentInSystemInstanceRef":
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self
