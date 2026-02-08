
class InitEvent(RTEEvent):
    """
    This RTEEvent is supposed to be used for initialization purposes, i.e. for
    starting and restarting a partition. It is not guaranteed that all
    RunnableEntities referenced by this InitEvent are executed before the
    ’regular’ RunnableEntities are executed for the first time. The execution
    order depends on the task mapping.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::InitEvent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 546, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
