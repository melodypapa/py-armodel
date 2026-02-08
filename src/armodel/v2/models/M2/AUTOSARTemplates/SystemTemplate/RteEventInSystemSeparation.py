from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import RTEEvent
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RteEventInSystemSeparation(Identifiable):
    """
    This meta-class is used to define a separation constraint in the context of
    the System. The referenced RteEvents are not allowed to be mapped into the
    same OsTask.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::RteEventInSystemSeparation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 214, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the same OsTask.
        # by: RteEventInSystem.
        self._rteEventInstanceRef: List["RTEEvent"] = []

    @property
    def rte_event_instance_ref(self) -> List["RTEEvent"]:
        """Get rteEventInstanceRef (Pythonic accessor)."""
        return self._rteEventInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRteEventInstanceRef(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
