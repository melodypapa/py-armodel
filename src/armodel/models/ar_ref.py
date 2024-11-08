from abc import ABCMeta
from typing import List
from .ar_object import ARObject

class RefType(ARObject):
    def __init__(self):
        self.dest = ""
        self.value = ""

class TRefType(RefType):
    def __init__(self):
        super().__init__()

class AnyInstanceRef(ARObject):
    def __init__(self):
        super().__init__()

        self.baseRef = None                             # type: RefType
        self.contextElementRef = None                   # type: RefType
        self.targetRef = None                           # type: RefType

    def getBaseRef(self) -> RefType:
        return self.baseRef

    def setBaseRef(self, value: RefType):
        self.baseRef = value
        return self

    def getContextElementRef(self) -> RefType:
        return self.contextElementRef

    def setContextElementRef(self, value: RefType):
        self.contextElementRef = value
        return self

    def getTargetRef(self) -> RefType:
        return self.targetRef

    def setTargetRef(self, value:RefType):
        self.targetRef = value
        return self

class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarVariableIRef = None             # type: VariableInAtomicSWCTypeInstanceRef 
        self.autosarVariableInImplDatatype = None   # type: ArVariableInImplementationDataInstanceRef
        self.localVariableRef = None

    def getAutosarVariableIRef(self):
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self):
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value):
        self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self):
        return self.localVariableRef

    def setLocalVariableRef(self, value):
        self.localVariableRef = value
        return self


class AutosarParameterRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosar_parameter_iref = None          # type: ParameterInAtomicSWCTypeInstanceRef
        self.local_parameter_ref = None             # type: RefType

class AtpInstanceRef(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == AtpInstanceRef:
            raise NotImplementedError("AtpInstanceRef is an abstract class.")
        
        super().__init__()

class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                             # type: RefType
        self.contextDataPrototypeRefs = []              # type: List[RefType]
        self.portPrototypeRef = None                    # type: RefType
        self.rootVariableDataPrototypeRef = None        # type: RefType
        self.targetDataPrototypeRef = None              # type: RefType

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self):
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value):
        self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self


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

        self.base_ref = None                                        # type: RefType
        self.context_mode_declaration_group_prototype_ref = None    # type: RefType
        self.context_port_ref = None                                # type: RefType
        self.target_mode_declaration_ref = None                     # type: RefType

class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.base_ref = None                                        # type: RefType
        self.context_data_prototype_ref = None                      # type: RefType
        self.port_prototype_ref = None                              # type: RefType
        self.root_parameter_data_prototype_ref = None               # type: RefType
        self.target_data_prototype_ref = None                       # type: RefType

class ApplicationCompositeElementInPortInterfaceInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.base_ref = None                                        # type: RefType
        self.context_data_prototype_ref = None                      # type: RefType
        self.root_data_prototype_ref = None                         # type: RefType
        self.target_data_prototype_ref = None                       # type: RefType

class InnerPortGroupInCompositionInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                                        # type: RefType
        self.contextRef = None                                     # type: RefType
        self.targetRef = None                                      # type: RefType

class VariableDataPrototypeInSystemInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.base_ref = None                                        # type: RefType
        self.context_component_refs = []                            # type: List[RefType]
        self.context_composition_ref = None                         # type: RefType
        self.context_port_ref = None                                # type: RefType
        self.target_data_prototype_ref = None                       # type: RefType 

class RModeGroupInAtomicSWCInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.context_r_port = None                                  # type: RefType
        self.target_mode_group = None                               # type: RefType

    @property
    def contextRPort(self) -> RefType:
        return self.context_r_port
    
    @contextRPort.setter
    def contextRPort(self, value: RefType):
        self.context_r_port = value

    @property
    def targetModeGroup(self) -> RefType:
        return self.target_mode_group
    
    @targetModeGroup.setter
    def targetModeGroup(self, value: RefType):
        self.target_mode_group = value
