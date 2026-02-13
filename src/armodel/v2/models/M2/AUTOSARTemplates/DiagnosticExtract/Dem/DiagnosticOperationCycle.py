"""
AUTOSAR Package - DiagnosticOperationCycle

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticOperationCycle
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticOperationCycle(DiagnosticCommonElement):
    """
    Definition of an operation cycle that is the base of the event qualifying
    and for Dem scheduling.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticOperationCycle::DiagnosticOperationCycle

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 201, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Operation cycles types for the Dem.
        self._typeCycleTypeEnum: Optional["DiagnosticOperation"] = None

    @property
    def type_cycle_type_enum(self) -> Optional["DiagnosticOperation"]:
        """Get typeCycleTypeEnum (Pythonic accessor)."""
        return self._typeCycleTypeEnum

    @type_cycle_type_enum.setter
    def type_cycle_type_enum(self, value: Optional["DiagnosticOperation"]) -> None:
        """
        Set typeCycleTypeEnum with validation.

        Args:
            value: The typeCycleTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeCycleTypeEnum = None
            return

        if not isinstance(value, DiagnosticOperation):
            raise TypeError(
                f"typeCycleTypeEnum must be DiagnosticOperation or None, got {type(value).__name__}"
            )
        self._typeCycleTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeCycleTypeEnum(self) -> "DiagnosticOperation":
        """
        AUTOSAR-compliant getter for typeCycleTypeEnum.

        Returns:
            The typeCycleTypeEnum value

        Note:
            Delegates to type_cycle_type_enum property (CODING_RULE_V2_00017)
        """
        return self.type_cycle_type_enum  # Delegates to property

    def setTypeCycleTypeEnum(self, value: "DiagnosticOperation") -> DiagnosticOperationCycle:
        """
        AUTOSAR-compliant setter for typeCycleTypeEnum with method chaining.

        Args:
            value: The typeCycleTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_cycle_type_enum property setter (gets validation automatically)
        """
        self.type_cycle_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type_cycle_type_enum(self, value: Optional["DiagnosticOperation"]) -> DiagnosticOperationCycle:
        """
        Set typeCycleTypeEnum and return self for chaining.

        Args:
            value: The typeCycleTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_cycle_type_enum("value")
        """
        self.type_cycle_type_enum = value  # Use property setter (gets validation)
        return self


class DiagnosticOperationCycleTypeEnum(AREnum):
    """
    DiagnosticOperationCycleTypeEnum enumeration

Operation cycles types used to identify certain Operation cycles with a certain semantics. Aggregated by DiagnosticOperationCycle.type

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticOperationCycle
    """
    # Ignition ON / OFF cycle
    ignition = "0"

    # OBD Driving cycle other further operation cycle
    obdDrivingCycle = "2"

    # OBD Warm up cycle
    warmup = "5"
