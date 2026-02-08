from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CompositionSw,
    SwComponent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class InnerRunnableEntityGroupInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a nested
    RunnableEntityGroup.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::InnerRunnableEntityGroupInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 956, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the InstanceRef.
        # atpDerived.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target association of the InstanceRef.
        # xml.
        # sequenceOffset=30.
        self._targetRunnable: RefType = None

    @property
    def target_runnable(self) -> RefType:
        """Get targetRunnable (Pythonic accessor)."""
        return self._targetRunnable

    @target_runnable.setter
    def target_runnable(self, value: RefType) -> None:
        """
        Set targetRunnable with validation.

        Args:
            value: The targetRunnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._targetRunnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "InnerRunnableEntityGroupInCompositionInstanceRef":
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

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.

        Returns:
            The contextSw value

        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetRunnable(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetRunnable.

        Returns:
            The targetRunnable value

        Note:
            Delegates to target_runnable property (CODING_RULE_V2_00017)
        """
        return self.target_runnable  # Delegates to property

    def setTargetRunnable(self, value: RefType) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetRunnable with method chaining.

        Args:
            value: The targetRunnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_runnable property setter (gets validation automatically)
        """
        self.target_runnable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
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

    def with_target_runnable(self, value: RefType) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        Set targetRunnable and return self for chaining.

        Args:
            value: The targetRunnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_runnable("value")
        """
        self.target_runnable = value  # Use property setter (gets validation)
        return self
