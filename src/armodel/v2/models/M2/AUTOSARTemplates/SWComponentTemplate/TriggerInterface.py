from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterface,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TriggerInterface(PortInterface):
    """
    A trigger interface declares a number of triggers that can be sent by an
    trigger source.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 109, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Trigger of this trigger interface.
        self._trigger: List[RefType] = []

    @property
    def trigger(self) -> List[RefType]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    def with_trigger(self, value):
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
