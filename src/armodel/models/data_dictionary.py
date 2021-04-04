from .general_structure import ARObject
from .ar_ref import RefType

class SwDataDefProps(ARObject):
    def __init__(self):
        super().__init__()

        self.base_type_ref = None                   # type: RefType
        self.compu_method_ref = None                # type: RefType
        self.data_constr_ref = None                 # type: RefType
        self.implementation_data_type_ref = None    # type: RefType
        self.sw_impl_policy = ""
        self.sw_calibration_access = ""
        self.sw_pointer_target_props = None         # type: SwPointerTargetProps

class SwPointerTargetProps(ARObject):
    def __init__(self):
        super().__init__()

        self.function_pointer_signature = None      # type: RefType
        self.sw_data_def_props = None               # type: SwDataDefProps
        self.target_category = ""