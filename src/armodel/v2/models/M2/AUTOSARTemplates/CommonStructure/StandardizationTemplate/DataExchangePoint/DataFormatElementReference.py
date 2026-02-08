from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import SpecElementReference


class DataFormatElementReference(SpecElementReference, ABC):
    """
    Superclass of all references to specification elements that have direct
    impact on the data exchange format (Meta-Classes, Meta-Attributes,
    constraints, SdgDefs)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::DataFormatElementReference

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is DataFormatElementReference:
            raise TypeError("DataFormatElementReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
