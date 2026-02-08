from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInBswInstanceRef(ARObject):
    """
    Instance reference to be capable of referencing a specific ModeDeclaration
    of a ModeDeclarationGroup Prototype utilized in a BSW module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::ModeInBswInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 38, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the BSW implementation that manifests the.
        self._contextBsw: Optional["BswImplementation"] = None

    @property
    def context_bsw(self) -> Optional["BswImplementation"]:
        """Get contextBsw (Pythonic accessor)."""
        return self._contextBsw

    @context_bsw.setter
    def context_bsw(self, value: Optional["BswImplementation"]) -> None:
        """
        Set contextBsw with validation.

        Args:
            value: The contextBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextBsw = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"contextBsw must be BswImplementation or None, got {type(value).__name__}"
            )
        self._contextBsw = value
        # Specifies the mode declaration group prototype that manifests the context.
        # xml.
        # sequenceOffset=20.
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

    def getContextBsw(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for contextBsw.

        Returns:
            The contextBsw value

        Note:
            Delegates to context_bsw property (CODING_RULE_V2_00017)
        """
        return self.context_bsw  # Delegates to property

    def setContextBsw(self, value: "BswImplementation") -> "ModeInBswInstanceRef":
        """
        AUTOSAR-compliant setter for contextBsw with method chaining.

        Args:
            value: The contextBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_bsw property setter (gets validation automatically)
        """
        self.context_bsw = value  # Delegates to property setter
        return self

    def getContextMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextMode.

        Returns:
            The contextMode value

        Note:
            Delegates to context_mode property (CODING_RULE_V2_00017)
        """
        return self.context_mode  # Delegates to property

    def setContextMode(self, value: RefType) -> "ModeInBswInstanceRef":
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

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> "ModeInBswInstanceRef":
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

    def with_context_bsw(self, value: Optional["BswImplementation"]) -> "ModeInBswInstanceRef":
        """
        Set contextBsw and return self for chaining.

        Args:
            value: The contextBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_bsw("value")
        """
        self.context_bsw = value  # Use property setter (gets validation)
        return self

    def with_context_mode(self, value: Optional[RefType]) -> "ModeInBswInstanceRef":
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

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "ModeInBswInstanceRef":
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
