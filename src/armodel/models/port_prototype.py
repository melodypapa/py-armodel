from typing import List
from .general_structure import ARObject, Identifiable
from .ar_ref import RefType, TRefType

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


class ModeSwitchReceiverComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class NvRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class ParameterRequireComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class ReceiverComSpec(RPortComSpec):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

        self.data_element_ref = None                # type: RefType
        self.handle_out_of_range = ""
        self.uses_end_to_end_protection = False


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
        self.data_element_ref = None  # type: RefType
        self.handle_out_of_range = ""
        self.uses_end_to_end_protection = False


class QueuedSenderComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()


class NonqueuedSenderComSpec(SenderComSpec):
    def __init__(self):
        super().__init__()
        self.init_value = None  # type: ValueSpecification (required)


class ServerComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()
        self.operation_ref = None  # type: RefType


class NonqueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self):
        super().__init__()

        self.alive_timeout = 0
        self.enable_updated = False
        self.filter = None                  # type: DataFilter
        self.handle_data_status = None      # type: boolean
        self.handle_never_received = False
        self.handel_timeout_type = ""
        self.init_value = None               # type: ValueSpecification
        self.timeout_substitution = None     # type: ValueSpecification


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

        self.provided_com_specs = []  # type: Dict[PPortComSpec]

    def _validateRPortComSpec(self, com_spec: PPortComSpec):
        if (isinstance(com_spec, NonqueuedSenderComSpec)):
            if (com_spec.data_element_ref == None):
                raise ValueError(
                    "opertion of NonqueuedSenderComSpec is invalid")
            if (com_spec.data_element_ref.dest != "VARIABLE-DATA-PROTOTYPE"):
                raise ValueError(
                    "Invalid operation dest of NonqueuedSenderComSpec")
        else:
            raise ValueError("Unspported com spec")

    def addProvidedComSpec(self, com_spec):
        self._validateRPortComSpec(com_spec)
        self.provided_com_specs.append(com_spec)

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        return self.provided_com_specs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return list(filter(lambda c: isinstance(c, NonqueuedSenderComSpec), self.provided_com_specs))


class AbstractRequiredPortPrototype(PortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.required_com_specs = []  # type: Dict[RPortComSpec]

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
        else:
            raise ValueError("Unspported RPortComSpec")

    def addRequiredComSpec(self, com_spec: RPortComSpec):
        self._validateRPortComSpec(com_spec)
        self.required_com_specs.append(com_spec)

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        return self.required_com_specs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return list(filter(lambda c: isinstance(c, ClientComSpec), self.required_com_specs))

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return list(filter(lambda c: isinstance(c, NonqueuedReceiverComSpec), self.required_com_specs))


class PPortPrototype(AbstractProvidedPortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_interface_tref = None  # type:


class RPortPrototype(AbstractRequiredPortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.required_interface_tref = TRefType()
