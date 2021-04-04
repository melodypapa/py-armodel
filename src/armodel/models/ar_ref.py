from abc import ABCMeta
from .general_structure import ARObject

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

class ProvidedPortPrototypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()
        self.context_component_ref = None   # type: RefType
        self.target_p_port_ref     = None   # type: RefType

class RequiredPortPrototypeInstanceRef(AtpInstanceRef):
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

