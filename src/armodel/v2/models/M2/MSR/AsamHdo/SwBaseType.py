# Import BaseType directly from the module file to avoid circular imports
from armodel.v2.models.M2.MSR.AsamHdo.BaseType import BaseType

class SwBaseType(BaseType):
    """
    This meta-class represents a base type used within ECU software.

    Package: M2::MSR::AsamHdo::BaseTypes

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 337, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 290, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2060, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 210, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
