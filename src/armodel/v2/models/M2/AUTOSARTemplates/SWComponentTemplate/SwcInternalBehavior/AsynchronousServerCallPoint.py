from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint

class AsynchronousServerCallPoint(ServerCallPoint):
    """
    An AsynchronousServerCallPoint is used for asynchronous invocation of a
    ClientServerOperation. IMPORTANT: a ServerCallPoint cannot be used
    concurrently. Once the client RunnableEntity has made the invocation, the
    ServerCallPoint cannot be used until the call returns (or an error occurs!)
    at which point the ServerCallPoint becomes available again.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::AsynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 581, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
