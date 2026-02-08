from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AutosarVariableRef(ARObject):
    """
    This class represents a reference to a variable within AUTOSAR which can be
    one of the following use cases: localVariable: • localVariable which is used
    as whole (e.g. InterRunnableVariable, inputValue for curve) autosarVariable:
    • a variable provided via Port which is used as whole (e.g.
    dataAccesspoints) • an element inside of a composite local variable typed by
    ApplicationDatatype (e.g. inputValue for a curve) • an element inside of a
    composite variable provided via Port and typed by ApplicationDatatype (e.g.
    inputValue for a curve) autosarVariableInImplDatatype: • an element inside
    of a composite local variable typed by ImplementationDatatype (e.g.
    nvramData mapping) • an element inside of a composite variable provided via
    Port and typed by ImplementationDatatype (e.g. inputValue for a curve)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 307, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 315, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is used if the target variable is inside of variableData Prototype typed
                # by an ImplementationDataType.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._autosarVariable: Optional["ArVariableIn"] = None

    @property
    def autosar_variable(self) -> Optional["ArVariableIn"]:
        """Get autosarVariable (Pythonic accessor)."""
        return self._autosarVariable

    @autosar_variable.setter
    def autosar_variable(self, value: Optional["ArVariableIn"]) -> None:
        """
        Set autosarVariable with validation.

        Args:
            value: The autosarVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autosarVariable = None
            return

        if not isinstance(value, ArVariableIn):
            raise TypeError(
                f"autosarVariable must be ArVariableIn or None, got {type(value).__name__}"
            )
        self._autosarVariable = value
        # This reference is used if the variable is local to the current would also be
                # possible to use the instance Such an instance ref would not have a the
                # current instance is the context.
        # local instance is a special case which may provide Therefore an explicit
                # reference is this case.
        self._localVariable: RefType = None

    @property
    def local_variable(self) -> RefType:
        """Get localVariable (Pythonic accessor)."""
        return self._localVariable

    @local_variable.setter
    def local_variable(self, value: RefType) -> None:
        """
        Set localVariable with validation.

        Args:
            value: The localVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localVariable = None
            return

        self._localVariable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutosarVariable(self) -> "ArVariableIn":
        """
        AUTOSAR-compliant getter for autosarVariable.

        Returns:
            The autosarVariable value

        Note:
            Delegates to autosar_variable property (CODING_RULE_V2_00017)
        """
        return self.autosar_variable  # Delegates to property

    def setAutosarVariable(self, value: "ArVariableIn") -> "AutosarVariableRef":
        """
        AUTOSAR-compliant setter for autosarVariable with method chaining.

        Args:
            value: The autosarVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to autosar_variable property setter (gets validation automatically)
        """
        self.autosar_variable = value  # Delegates to property setter
        return self

    def getLocalVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for localVariable.

        Returns:
            The localVariable value

        Note:
            Delegates to local_variable property (CODING_RULE_V2_00017)
        """
        return self.local_variable  # Delegates to property

    def setLocalVariable(self, value: RefType) -> "AutosarVariableRef":
        """
        AUTOSAR-compliant setter for localVariable with method chaining.

        Args:
            value: The localVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_variable property setter (gets validation automatically)
        """
        self.local_variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_autosar_variable(self, value: Optional["ArVariableIn"]) -> "AutosarVariableRef":
        """
        Set autosarVariable and return self for chaining.

        Args:
            value: The autosarVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_autosar_variable("value")
        """
        self.autosar_variable = value  # Use property setter (gets validation)
        return self

    def with_local_variable(self, value: Optional[RefType]) -> "AutosarVariableRef":
        """
        Set localVariable and return self for chaining.

        Args:
            value: The localVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_variable("value")
        """
        self.local_variable = value  # Use property setter (gets validation)
        return self
