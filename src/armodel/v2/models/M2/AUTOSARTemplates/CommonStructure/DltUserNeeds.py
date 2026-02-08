from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class DltUserNeeds(ServiceNeeds):
    """
    This meta-class specifies the needs on the configuration of the Diagnostic
    Log and Trace module for one SessionId. This class currently contains no
    attributes. An instance of this class is used to find out which
    PortPrototypes of an AtomicSwComponentType belong to this SessionId in order
    to group the request and response PortPrototypes of the same SessionId. The
    actual SessionId value is stored in the PortDefinedArgumentValue of the
    respective PortPrototype specification.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DltUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 817, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
