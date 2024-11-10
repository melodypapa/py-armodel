from typing import List

from .m2.autosar_templates.sw_component_template.communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec, QueuedReceiverComSpec, QueuedSenderComSpec, RPortComSpec, ServerComSpec
from .general_structure import ARObject, Identifiable
from .ar_ref import TRefType

class PortPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AbstractProvidedPortPrototype(PortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_com_specs = []  # type: List[PPortComSpec]

    def _validateRPortComSpec(self, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            if com_spec.dataElementRef == None:
                raise ValueError(
                    "operation of NonqueuedSenderComSpec is invalid")
            if com_spec.dataElementRef.dest != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError(
                    "Invalid operation dest of NonqueuedSenderComSpec")
        elif isinstance(com_spec, ServerComSpec):
            pass
        elif isinstance(com_spec, QueuedSenderComSpec):
            pass
        elif isinstance(com_spec, ModeSwitchSenderComSpec):
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
            if (com_spec.operationRef == None):
                raise ValueError(
                    "The operation reference of ClientComSpec has not been defined.")
            if (com_spec.operationRef.dest != "CLIENT-SERVER-OPERATION"):
                raise ValueError("Invalid operation dest of ClientComSpec.")
        elif (isinstance(com_spec, NonqueuedReceiverComSpec)):
            if (com_spec.dataElementRef == None):
                raise ValueError(
                    "The data element reference of NonqueuedReceiverComSpec has not been defined.")
            if (com_spec.dataElementRef.dest != "VARIABLE-DATA-PROTOTYPE"):
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
