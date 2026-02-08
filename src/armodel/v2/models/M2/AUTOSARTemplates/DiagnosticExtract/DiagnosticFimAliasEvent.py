from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticAbstractAliasEvent


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    """
    This meta-class is used to represent a given event semantics. However, the
    name of the actual events used in a specific project is sometimes not
    defined yet, not known or not in the responsibility of the author.
    Therefore, the DiagnosticFimAliasEvent has a reference to the actual
    DiagnosticEvent and by this the final connection is created.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimAliasEvent

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 214, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
