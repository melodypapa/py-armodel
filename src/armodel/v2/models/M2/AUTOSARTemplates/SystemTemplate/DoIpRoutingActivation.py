from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DoIpRoutingActivation(Identifiable):
    """
    This meta-class defines a DoIP routing activation possibility that activates
    the routing to the referenced doIPTargetAddress. This means that the
    diagnostic request messages related to the specified do IPTargetAddress
    received by socketConnections that are referenced by the same DoIpInterface
    that aggregates this DoIpRoutingActivation are activated.

    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 553, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to DoIPTargetAddress which is activated on this
        # DoIpRoutingActivation.
        self._doIpTarget: List["DoIpLogicTarget"] = []

    @property
    def do_ip_target(self) -> List["DoIpLogicTarget"]:
        """Get doIpTarget (Pythonic accessor)."""
        return self._doIpTarget

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpTarget(self) -> List["DoIpLogicTarget"]:
        """
        AUTOSAR-compliant getter for doIpTarget.

        Returns:
            The doIpTarget value

        Note:
            Delegates to do_ip_target property (CODING_RULE_V2_00017)
        """
        return self.do_ip_target  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
