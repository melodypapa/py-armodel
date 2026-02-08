from armodel.v2.models.M2.AUTOSARTemplates import AbstractDoIpLogicAddressProps


class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    """
    This meta-class acts as a target for references to the
    DoIpLogicTargetAddress and collects DoIpLogic TargetAddress specific
    settings.

    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP::DoIpLogicTargetAddressProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 556, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
