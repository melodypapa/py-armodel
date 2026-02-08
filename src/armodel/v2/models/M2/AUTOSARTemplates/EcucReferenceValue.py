from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import EcucAbstractReferenceValue
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EcucReferenceValue(EcucAbstractReferenceValue):
    """
    Used to represent a configuration value that has a parameter definition of
    type EcucAbstractReference Def (used for all of its specializations
    excluding EcucInstanceReferenceDef).

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucReferenceValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 132, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the destination of the reference.
        self._value: RefType = None

    @property
    def value(self) -> RefType:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: RefType) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> RefType:
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: RefType) -> "EcucReferenceValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional[RefType]) -> "EcucReferenceValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
