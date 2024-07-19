
from .data_dictionary import SwDataDefProps
from .ar_object import ARObject
from .general_structure import Identifiable


class PerInstanceMemory(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.init_value = None          # type: str
        self.sw_data_def_props = None   # type: SwDataDefProps
        self.type = None                # type: str
        self.type_definition = None     # type: str