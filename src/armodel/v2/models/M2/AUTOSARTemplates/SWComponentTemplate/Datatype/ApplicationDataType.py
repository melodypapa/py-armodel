from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import AutosarDataType


class ApplicationDataType(AutosarDataType, ABC):
    """
    ApplicationDataType defines a data type from the application point of view.
    Especially it should be used whenever something "physical" is at stake. An
    ApplicationDataType represents a set of values as seen in the application
    model, such as measurement units. It does not consider implementation
    details such as bit-size, endianess, etc. It should be possible to model the
    application level aspects of a VFB system by using ApplicationData Types
    only.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationDataType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 302, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 299, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 232, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is ApplicationDataType:
            raise TypeError("ApplicationDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
