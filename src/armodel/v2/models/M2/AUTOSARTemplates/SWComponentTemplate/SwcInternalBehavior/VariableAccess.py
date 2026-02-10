from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class VariableAccess(AbstractAccessPoint):
    """
    The presence of a VariableAccess implies that a RunnableEntity needs access
    to a VariableData Prototype. The kind of access is specified by the role in
    which the class is used.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 351, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 567, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2077, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 256, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the accessed variable.
        self._accessedVariable: RefType = None

    @property
    def accessed_variable(self) -> RefType:
        """Get accessedVariable (Pythonic accessor)."""
        return self._accessedVariable

    @accessed_variable.setter
    def accessed_variable(self, value: RefType) -> None:
        """
        Set accessedVariable with validation.

        Args:
            value: The accessedVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedVariable = None
            return

        self._accessedVariable = value
        # For example, it possible to the communication is intended to cross of an ECU
                # or whether it is intended not to boundary of a single partition.
        self._scope: Optional["VariableAccessScope"] = None

    @property
    def scope(self) -> Optional["VariableAccessScope"]:
        """Get scope (Pythonic accessor)."""
        return self._scope

    @scope.setter
    def scope(self, value: Optional["VariableAccessScope"]) -> None:
        """
        Set scope with validation.

        Args:
            value: The scope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scope = None
            return

        if not isinstance(value, VariableAccessScope):
            raise TypeError(
                f"scope must be VariableAccessScope or None, got {type(value).__name__}"
            )
        self._scope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedVariable.

        Returns:
            The accessedVariable value

        Note:
            Delegates to accessed_variable property (CODING_RULE_V2_00017)
        """
        return self.accessed_variable  # Delegates to property

    def setAccessedVariable(self, value: RefType) -> "VariableAccess":
        """
        AUTOSAR-compliant setter for accessedVariable with method chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to accessed_variable property setter (gets validation automatically)
        """
        self.accessed_variable = value  # Delegates to property setter
        return self

    def getScope(self) -> "VariableAccessScope":
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def setScope(self, value: "VariableAccessScope") -> "VariableAccess":
        """
        AUTOSAR-compliant setter for scope with method chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Note:
            Delegates to scope property setter (gets validation automatically)
        """
        self.scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_variable(self, value: Optional[RefType]) -> "VariableAccess":
        """
        Set accessedVariable and return self for chaining.

        Args:
            value: The accessedVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_variable("value")
        """
        self.accessed_variable = value  # Use property setter (gets validation)
        return self

    def with_scope(self, value: Optional["VariableAccessScope"]) -> "VariableAccess":
        """
        Set scope and return self for chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope("value")
        """
        self.scope = value  # Use property setter (gets validation)
        return self
