from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagEventDebounceAlgorithm(Identifiable, ABC):
    """
    This class represents the ability to specify the pre-debounce algorithm
    which is selected and/or required by the particular monitor. This class
    inherits from Identifiable in order to allow further documentation of the
    expected or implemented debouncing and to use the category for the
    identification of the expected / implemented debouncing.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 259, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 756, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagEventDebounceAlgorithm:
            raise TypeError("DiagEventDebounceAlgorithm is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
