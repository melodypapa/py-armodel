from abc import ABC


class ApplicationCompositeDataType(ApplicationDataType, ABC):
    """
    Abstract base class for all application data types composed of other data
    types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationCompositeDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 241, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is ApplicationCompositeDataType:
            raise TypeError("ApplicationCompositeDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
