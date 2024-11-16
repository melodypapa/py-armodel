
from .M2.AUTOSARTemplates.sw_component_template.port_interface.instance_refs import ApplicationCompositeElementInPortInterfaceInstanceRef
from .M2.MSR.data_dictionary.data_def_properties import SwDataDefProps
from .ar_object import ARObject

class TransmissionAcknowledgementRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None     # type: float

class CompositeNetworkRepresentation(ARObject):
    def __init__(self):
        super().__init__()

        self.leaf_element_iref = None           # type: ApplicationCompositeElementInPortInterfaceInstanceRef
        self.network_representation = None      # type: SwDataDefProps
