from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class BswDistinguishedPartition(Referrable):
    """
    Each instance of this meta-class represents an abstract partition in which
    context the code of the enclosing BswModuleBehavior can be executed. The
    intended use case is to distinguish between several partitions in order to
    implement different behavior per partition, for example to behave either as
    a master or satellite in a multicore ECU with shared BSW code.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDistinguishedPartition

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 118, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
