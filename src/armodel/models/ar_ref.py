from abc import ABCMeta
from .ar_object import ARObject

class RefType(ARObject):
    def __init__(self):
        self.dest = ""
        self.value = ""

class TRefType(RefType):
    def __init__(self):
        super().__init__()
        

class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()
        self.autosar_variable_iref = None
        self.autosar_variable_in_impl_datatype = None # type: ArVariableInImplementationDataInstanceRef
        self.local_variable_ref = None

class AtpInstanceRef(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == AtpInstanceRef:
            raise NotImplementedError("AtpInstanceRef is an abstract class.")
        super().__init__()

class PortInCompositionTypeInstanceRef(AtpInstanceRef, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == PortInCompositionTypeInstanceRef:
            raise NotImplementedError("PortInCompositionTypeInstanceRef is an abstract class.")
        super().__init__()

        self.abstract_context_component_ref = None  # type: RefType
        self.base_ref = None                        # type: RefType
        self.target_port_ref = None                 # type: RefType

class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    def __init__(self):
        super().__init__()
        self.context_component_ref = None   # type: RefType
        self.target_p_port_ref     = None   # type: RefType

class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    def __init__(self):
        super().__init__()
        self.context_component_ref = None   # type: RefType
        self.target_r_port_ref     = None   # type: RefType

class ArVariableInImplementationDataInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()
        self.port_prototype_ref = None          # type: RefType
        self.target_data_prototype_ref = None   # type: RefType

class OperationInAtomicSwcInstanceRef(AtpInstanceRef, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == OperationInAtomicSwcInstanceRef:
            raise NotImplementedError("OperationInAtomicSwcInstanceRef is an abstract class.")
        super().__init__()

class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()
        self.context_p_port_ref = None              # type: RefType
        self.target_provided_operation_ref = None   # type: RefType

class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()
        self.context_r_port_ref = None              # type: RefType
        self.target_required_operation_ref = None   # type: RefType

class VariableInAtomicSwcInstanceRef(AtpInstanceRef, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == OperationInAtomicSwcInstanceRef:
            raise NotImplementedError("OperationInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.context_r_port_ref = None              # type: RefType
        self.target_data_element_ref = None         # type: RefType

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.context_r_port_ref = None              # type: RefType
        self.target_data_element_ref = None         # type: RefType

class RModeInAtomicSwcInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.base_ref = None                                    # type: RefType
        self.context_mode_declaration_group_prototype = None    # type: RefType
        self.context_port = None                                # type: RefType
        self.target_mode_declaration = None                     # type: RefType