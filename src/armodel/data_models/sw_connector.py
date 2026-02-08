class SwConnectorData:
    def __init__(self) -> None:
        self.short_name = ""

class DelegationSwConnectorData(SwConnectorData):
    def __init__(self) -> None:
        super().__init__()

        self.inner_swc = ""
        self.inner_pport = ""
        self.inner_rport = ""
        self.outer_pport = ""
        self.outer_rport = ""

class AssemblySwConnectorData(SwConnectorData):
    def __init__(self) -> None:
        super().__init__()

        self.provider_swc= ""
        self.p_port = ""
        self.r_swc = ""
        self.r_port = ""
