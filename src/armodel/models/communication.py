
from .ar_object import ARObject

class TransmissionAcknowledgementRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None     # type: float

class CompositeNetworkRepresentation(ARObject):
    def __init__(self):
        super().__init__()

        self.leaf_element = None                # type: ApplicationCompositeElementDataPrototype
        self.network_representation = None      # type: SwDataDefProps
