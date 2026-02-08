from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ServiceNeeds(Identifiable, ABC):
    """
    This expresses the abstract needs that a Software Component or Basic
    Software Module has on the configuration of an AUTOSAR Service to which it
    will be connected. "Abstract needs" means that the model abstracts from the
    Configuration Parameters of the underlying Basic Software. (cid:53) 227 of
    381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic
    Software Module Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 227, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 306, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 603, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ServiceNeeds:
            raise TypeError("ServiceNeeds is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
