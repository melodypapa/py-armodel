from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import DataFormatElementReference


class AbstractClassTailoring(DataFormatElementReference, ABC):
    """
    Tailoring of abstract classes in the AUTOSAR meta-model

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AbstractClassTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 101, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractClassTailoring:
            raise TypeError("AbstractClassTailoring is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
