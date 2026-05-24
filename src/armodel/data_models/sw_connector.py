class SwConnectorData:
    """
    Base data class for SW connector data with short name.
    """
    def __init__(self) -> None:
        self.short_name = ""

class DelegationSwConnectorData(SwConnectorData):
    """
    Data for delegation SW connectors with inner and outer port, SWC
    references.
    """
    def __init__(self) -> None:
        super().__init__()

        self.inner_swc = ""
        self.inner_pport = ""
        self.inner_rport = ""
        self.outer_pport = ""
        self.outer_rport = ""

class AssemblySwConnectorData(SwConnectorData):
    """
    Data for assembly SW connectors with provider/requester SWC and port
    references.
    """
    def __init__(self) -> None:
        super().__init__()

        self.provider_swc= ""
        self.p_port = ""
        self.r_swc = ""
        self.r_port = ""        