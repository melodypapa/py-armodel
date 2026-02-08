from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwDescriptionEntity,
)


class HwType(HwDescriptionEntity):
    """
    This represents the ability to describe Hardware types on an abstract level.
    The particular types of hardware are distinguished by the category. This
    category determines the applicable attributes. The possible categories and
    attributes are defined in HwCategory.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 17, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 991, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
