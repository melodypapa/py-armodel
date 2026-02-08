from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticCommonElement
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticCondition(DiagnosticCommonElement, ABC):
    """
    Abstract element for StorageConditions and EnableConditions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticCondition::DiagnosticCondition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 194, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticCondition:
            raise TypeError("DiagnosticCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the initial status for enable or disable of event reports of a
                # diagnostic event.
        # is the initialization after power up (before this reported the first time).
        # of a diagnostic event enabled of a diagnostic event disabled.
        self._initValue: Optional["Boolean"] = None

    @property
    def init_value(self) -> Optional["Boolean"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["Boolean"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"initValue must be Boolean or None, got {type(value).__name__}"
            )
        self._initValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "Boolean") -> "DiagnosticCondition":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["Boolean"]) -> "DiagnosticCondition":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self
