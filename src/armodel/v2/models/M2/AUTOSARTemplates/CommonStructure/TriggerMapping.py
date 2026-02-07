from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TriggerMapping(ARObject):
    """
    Defines the mapping of two particular unequally named Triggers in the given
    context.

    Package: M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration::TriggerMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 134, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A Trigger to be mapped.
        self._firstTrigger: RefType = None

    @property
    def first_trigger(self) -> RefType:
        """Get firstTrigger (Pythonic accessor)."""
        return self._firstTrigger

    @first_trigger.setter
    def first_trigger(self, value: RefType) -> None:
        """
        Set firstTrigger with validation.

        Args:
            value: The firstTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstTrigger = None
            return

        self._firstTrigger = value
        # A Trigger to be mapped.
        self._secondTrigger: RefType = None

    @property
    def second_trigger(self) -> RefType:
        """Get secondTrigger (Pythonic accessor)."""
        return self._secondTrigger

    @second_trigger.setter
    def second_trigger(self, value: RefType) -> None:
        """
        Set secondTrigger with validation.

        Args:
            value: The secondTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondTrigger = None
            return

        self._secondTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for firstTrigger.

        Returns:
            The firstTrigger value

        Note:
            Delegates to first_trigger property (CODING_RULE_V2_00017)
        """
        return self.first_trigger  # Delegates to property

    def setFirstTrigger(self, value: RefType) -> "TriggerMapping":
        """
        AUTOSAR-compliant setter for firstTrigger with method chaining.

        Args:
            value: The firstTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_trigger property setter (gets validation automatically)
        """
        self.first_trigger = value  # Delegates to property setter
        return self

    def getSecondTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for secondTrigger.

        Returns:
            The secondTrigger value

        Note:
            Delegates to second_trigger property (CODING_RULE_V2_00017)
        """
        return self.second_trigger  # Delegates to property

    def setSecondTrigger(self, value: RefType) -> "TriggerMapping":
        """
        AUTOSAR-compliant setter for secondTrigger with method chaining.

        Args:
            value: The secondTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_trigger property setter (gets validation automatically)
        """
        self.second_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_trigger(self, value: Optional[RefType]) -> "TriggerMapping":
        """
        Set firstTrigger and return self for chaining.

        Args:
            value: The firstTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_trigger("value")
        """
        self.first_trigger = value  # Use property setter (gets validation)
        return self

    def with_second_trigger(self, value: Optional[RefType]) -> "TriggerMapping":
        """
        Set secondTrigger and return self for chaining.

        Args:
            value: The secondTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_trigger("value")
        """
        self.second_trigger = value  # Use property setter (gets validation)
        return self
