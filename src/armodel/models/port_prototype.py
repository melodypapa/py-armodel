from typing import List

from .ar_object import ARBoolean
from .data_dictionary import SwDataDefProps
from .general_structure import ARObject, Identifiable
from .ar_ref import RefType, TRefType
from .communication import CompositeNetworkRepresentation, TransmissionAcknowledgementRequest
from .common_structure import ValueSpecification

from abc import ABCMeta


class PPortComSpec(ARObject, metaclass=ABCMeta):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class 

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self):
        if type(self) == PPortComSpec:
            raise NotImplementedError("PPortComSpec is an abstract class.")
        super().__init__()


class RPortComSpec(ARObject,  metaclass=ABCMeta):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class 

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self):
        if type(self) == RPortComSpec:
            raise NotImplementedError("RPortComSpec is an abstract class.")
        super().__init__()


class ClientComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.operation_ref = None  # type: RefType
    
    @property
    def operationRef(self) -> RefType:
        return self.operation_ref
    
    @operationRef.setter
    def operationRef(self, value:RefType):
        self.operation_ref = value

class ModeSwitchReceiverComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()

        self.mode_group_ref = None # type: RefType

    @property
    def modeGroupRef(self) -> RefType:
        return self.mode_group_ref
    
    @modeGroupRef.setter
    def modeGroupRef(self, value: RefType):
        self.mode_group_ref = value

class NvRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class ParameterRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()
    
        self.parameter_ref = None # type: RefType
        self.init_value = None    # type: ValueSpecification

class ReceiverComSpec(RPortComSpec):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

        self._composite_network_representation = []     # type: List[CompositeNetworkRepresentation]
        self.data_element_ref = None                    # type: RefType
        self.network_representation = None              # type: SwDataDefProps
        self.handle_out_of_range = None                 # type: str
        self.uses_end_to_end_protection = None          # type: ARBoolean     

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self._composite_network_representation.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self._composite_network_representation

class ModeSwitchSenderComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class ParameterProvideComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class SenderComSpec(PPortComSpec):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self._composite_network_representation = []     # type: List[CompositeNetworkRepresentation]
        self.data_element_ref = None                    # type: RefType
        self.network_representation = None              # type: SwDataDefProps
        self.handle_out_of_range = None                 # type: str
        self.transmission_acknowledge = None            # type: TransmissionAcknowledgementRequest 
        self.uses_end_to_end_protection = None          # type: ARBoolean

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self._composite_network_representation.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self._composite_network_representation

class QueuedSenderComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()


class NonqueuedSenderComSpec(SenderComSpec):
    def __init__(self):
        super().__init__()
        # (required)
        self.init_value = None  # type: ValueSpecification 


class ServerComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()

        self.operation_ref = None   # type: RefType
        self.queue_length = None    # type: int


class NonqueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self):
        super().__init__()

        self.alive_timeout = 0
        self.enable_updated = None              # type: ARBoolean
        self.filter = None                      # type: DataFilter
        self.handle_data_status = None          # type: bool
        self.handle_never_received = None       # type: ARBoolean
        self.handel_timeout_type = ""
        self.init_value = None                  # type: ValueSpecification
        self.timeout_substitution = None        # type: ValueSpecification

class QueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self):
        super().__init__()

        self.queue_length = 0


class PortPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AbstractProvidedPortPrototype(PortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_com_specs = []  # type: List[PPortComSpec]

    def _validateRPortComSpec(self, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            if com_spec.data_element_ref == None:
                raise ValueError(
                    "operation of NonqueuedSenderComSpec is invalid")
            if com_spec.data_element_ref.dest != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError(
                    "Invalid operation dest of NonqueuedSenderComSpec")
        elif isinstance(com_spec, ServerComSpec):
            pass
        else:
            raise ValueError("Unsupported com spec")

    def addProvidedComSpec(self, com_spec):
        self._validateRPortComSpec(com_spec)
        self.provided_com_specs.append(com_spec)

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        return self.provided_com_specs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedSenderComSpec), self.provided_com_specs)


class AbstractRequiredPortPrototype(PortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.required_com_specs = []  # type: List[RPortComSpec]

    def _validateRPortComSpec(self, com_spec: RPortComSpec):
        if (isinstance(com_spec, ClientComSpec)):
            if (com_spec.operation_ref == None):
                raise ValueError(
                    "The operation reference of ClientComSpec has not been defined.")
            if (com_spec.operation_ref.dest != "CLIENT-SERVER-OPERATION"):
                raise ValueError("Invalid operation dest of ClientComSpec.")
        elif (isinstance(com_spec, NonqueuedReceiverComSpec)):
            if (com_spec.data_element_ref == None):
                raise ValueError(
                    "The data element reference of NonqueuedReceiverComSpec has not been defined.")
            if (com_spec.data_element_ref.dest != "VARIABLE-DATA-PROTOTYPE"):
                raise ValueError(
                    "Invalid date element dest of NonqueuedReceiverComSpec.")
        elif isinstance(com_spec, QueuedReceiverComSpec):
            pass
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            pass
        elif isinstance(com_spec, ParameterRequireComSpec):
            if com_spec.parameter_ref == None:
                raise ValueError(
                    "The parameter reference of ParameterRequireComSpec has not been defined.")
            if com_spec.parameter_ref.dest != "PARAMETER-DATA-PROTOTYPE":
                raise ValueError(
                    "Invalid parameter dest of ParameterRequireComSpec.")
            if com_spec.init_value == None:
                raise ValueError(
                    "The initial value of ParameterRequireComSpec has not been defined.")
        else:
            raise ValueError("Unsupported RPortComSpec <%s>" % type(com_spec))

    def addRequiredComSpec(self, com_spec: RPortComSpec):
        self._validateRPortComSpec(com_spec)
        self.required_com_specs.append(com_spec)

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        return self.required_com_specs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return filter(lambda c: isinstance(c, ClientComSpec), self.required_com_specs)

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedReceiverComSpec), self.required_com_specs)


class PPortPrototype(AbstractProvidedPortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_interface_tref = TRefType()


class RPortPrototype(AbstractRequiredPortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.required_interface_tref = TRefType()
