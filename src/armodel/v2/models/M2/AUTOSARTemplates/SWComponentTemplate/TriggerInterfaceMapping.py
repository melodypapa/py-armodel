from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import PortInterfaceMapping
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TriggerInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of unequal named Triggers in context of two different
    TriggerInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TriggerInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 134, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Mapping of two Trigger in two different TriggerInterface.
        self._triggerMapping: List[RefType] = []

    @property
    def trigger_mapping(self) -> List[RefType]:
        """Get triggerMapping (Pythonic accessor)."""
        return self._triggerMapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTriggerMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for triggerMapping.

        Returns:
            The triggerMapping value

        Note:
            Delegates to trigger_mapping property (CODING_RULE_V2_00017)
        """
        return self.trigger_mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
