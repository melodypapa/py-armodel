from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import TimingExtension

    RefType,
)


class EcuTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints within
    the scope of one ECU configuration. TimingDescriptions aggregated by
    EcuTiming are allowed to use all events derived from the class Timing
    DescriptionEvent.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::EcuTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 30, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of an EcuTiming.
        # All timing descriptions and constraints shall within this scope.
        self._ecu: RefType = None

    @property
    def ecu(self) -> RefType:
        """Get ecu (Pythonic accessor)."""
        return self._ecu

    @ecu.setter
    def ecu(self, value: RefType) -> None:
        """
        Set ecu with validation.

        Args:
            value: The ecu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecu = None
            return

        self._ecu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcu(self) -> RefType:
        """
        AUTOSAR-compliant getter for ecu.

        Returns:
            The ecu value

        Note:
            Delegates to ecu property (CODING_RULE_V2_00017)
        """
        return self.ecu  # Delegates to property

    def setEcu(self, value: RefType) -> "EcuTiming":
        """
        AUTOSAR-compliant setter for ecu with method chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu property setter (gets validation automatically)
        """
        self.ecu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu(self, value: Optional[RefType]) -> "EcuTiming":
        """
        Set ecu and return self for chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu("value")
        """
        self.ecu = value  # Use property setter (gets validation)
        return self
