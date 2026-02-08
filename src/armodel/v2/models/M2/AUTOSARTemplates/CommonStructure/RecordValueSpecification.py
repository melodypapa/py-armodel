from armodel.v2.models.M2.AUTOSARTemplates import CompositeValueSpecification


class RecordValueSpecification(CompositeValueSpecification):
    """
    Specifies the values for a record.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RecordValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 328, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 435, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
