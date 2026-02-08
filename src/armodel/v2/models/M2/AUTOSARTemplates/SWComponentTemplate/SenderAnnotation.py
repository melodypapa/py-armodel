from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    SenderReceiverAnnotation,
)


class SenderAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a sender port, specifying properties of data elements that
    don’t affect communication or generation of the RTE.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
