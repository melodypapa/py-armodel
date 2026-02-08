
class ApplicationDeferredDataType(ApplicationDataType):
    """
    A placeholder data type in which the precise application data type is
    deferred to a later stage.

    Package: M2::AUTOSARTemplates::AbstractPlatform::ApplicationDeferredDataType

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 37, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
