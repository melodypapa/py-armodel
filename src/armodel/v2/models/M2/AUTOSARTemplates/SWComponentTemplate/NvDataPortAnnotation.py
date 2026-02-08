from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import GeneralAnnotation
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class NvDataPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain VariableDataPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::NvDataPortAnnotation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of nv data annotated.
        self._variable: RefType = None

    @property
    def variable(self) -> RefType:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: RefType) -> None:
        """
        Set variable with validation.

        Args:
            value: The variable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: RefType) -> "NvDataPortAnnotation":
        """
        AUTOSAR-compliant setter for variable with method chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_variable(self, value: Optional[RefType]) -> "NvDataPortAnnotation":
        """
        Set variable and return self for chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self
