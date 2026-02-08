from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::DiagnosticExtract::InstanceRefs::SwcServiceDependencyInSystemInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 369, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._contextRootSw: Optional["RootSwComposition"] = None

    @property
    def context_root_sw(self) -> Optional["RootSwComposition"]:
        """Get contextRootSw (Pythonic accessor)."""
        return self._contextRootSw

    @context_root_sw.setter
    def context_root_sw(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set contextRootSw with validation.

        Args:
            value: The contextRootSw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRootSw = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"contextRootSw must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._contextRootSw = value
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
        # R23-11.
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        self._targetSwc: Optional["SwcService"] = None

    @property
    def target_swc(self) -> Optional["SwcService"]:
        """Get targetSwc (Pythonic accessor)."""
        return self._targetSwc

    @target_swc.setter
    def target_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set targetSwc with validation.

        Args:
            value: The targetSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"targetSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._targetSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRootSw(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for contextRootSw.

        Returns:
            The contextRootSw value

        Note:
            Delegates to context_root_sw property (CODING_RULE_V2_00017)
        """
        return self.context_root_sw  # Delegates to property

    def setContextRootSw(self, value: "RootSwComposition") -> "SwcServiceDependencyInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for contextRootSw with method chaining.

        Args:
            value: The contextRootSw to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_root_sw property setter (gets validation automatically)
        """
        self.context_root_sw = value  # Delegates to property setter
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

    def getTargetSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for targetSwc.

        Returns:
            The targetSwc value

        Note:
            Delegates to target_swc property (CODING_RULE_V2_00017)
        """
        return self.target_swc  # Delegates to property

    def setTargetSwc(self, value: "SwcService") -> "SwcServiceDependencyInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for targetSwc with method chaining.

        Args:
            value: The targetSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_swc property setter (gets validation automatically)
        """
        self.target_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_root_sw(self, value: Optional["RootSwComposition"]) -> "SwcServiceDependencyInSystemInstanceRef":
        """
        Set contextRootSw and return self for chaining.

        Args:
            value: The contextRootSw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_root_sw("value")
        """
        self.context_root_sw = value  # Use property setter (gets validation)
        return self

    def with_target_swc(self, value: Optional["SwcService"]) -> "SwcServiceDependencyInSystemInstanceRef":
        """
        Set targetSwc and return self for chaining.

        Args:
            value: The targetSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_swc("value")
        """
        self.target_swc = value  # Use property setter (gets validation)
        return self
