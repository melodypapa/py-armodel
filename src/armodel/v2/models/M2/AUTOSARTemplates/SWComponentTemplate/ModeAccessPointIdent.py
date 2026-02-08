from armodel.v2.models.M2.AUTOSARTemplates import IdentCaption


class ModeAccessPointIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become
    referenced into the meta-class Mode AccessPoint without breaking backwards
    compatibility.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::ModeAccessPointIdent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 852, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
