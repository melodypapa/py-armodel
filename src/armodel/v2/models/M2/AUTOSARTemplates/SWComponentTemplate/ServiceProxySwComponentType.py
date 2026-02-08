
class ServiceProxySwComponentType(AtomicSwComponentType):
    """
    This class provides the ability to express a software-component which
    provides access to an internal service for remote ECUs. It acts as a proxy
    for the service providing access to the service. An important use case is
    the request of vehicle mode switches: Such requests can be communicated via
    sender-receiver interfaces across ECU boundaries, but the mode manager being
    responsible to perform the mode switches is an AUTOSAR Service which is
    located in the Basic Software and is not visible in the VFB view. To handle
    this situation, a ServiceProxySwComponentType will act as proxy for the mode
    manager. It will have R-Ports to be connected with the mode requestors on
    VFB level and Service-Ports to be connected with the local mode manager at
    ECU integration time. Apart from the semantics, a
    ServiceProxySwComponentType has these specific properties: • A prototype of
    it can be mapped to more than one ECUs in the system description. • Exactly
    one additional instance of it will be created in the ECU-Extract per ECU to
    which the prototype has been mapped. • For remote communication, it can have
    only R-Ports with sender-receiver interfaces and 1:n semantics. • There
    shall be no connectors between two prototypes of any
    ServiceProxySwComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ServiceProxySwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 661, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2056, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
