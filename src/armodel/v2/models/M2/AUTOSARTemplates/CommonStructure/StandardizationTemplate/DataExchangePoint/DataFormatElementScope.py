from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import SpecElementScope


class DataFormatElementScope(SpecElementScope, ABC):
    """
    This class specifies if a Meta Class, Meta Attribute, Constraint or SdgDef
    is relevant for the Data Exchange Point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::DataFormatElementScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is DataFormatElementScope:
            raise TypeError("DataFormatElementScope is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
