from abc import ABCMeta
from typing import List

from ...GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

from ...CommonStructure.implementation import ImplementationProps
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....ar_ref import RefType, TRefType
from ...GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ..communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec, NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec, ParameterRequireComSpec, QueuedReceiverComSpec, QueuedSenderComSpec, RPortComSpec, ServerComSpec
from .instance_refs import InnerPortGroupInCompositionInstanceRef

class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class PortPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.clientServerAnnotations = []
        self.delegatedPortAnnotation = None
        self.ioHwAbstractionServerAnnotations = []
        self.modePortAnnotations = []
        self.nvDataPortAnnotations = []
        self.parameterPortAnnotations = []
        self.senderReceiverAnnotations = []
        self.triggerPortAnnotations = []

    def getClientServerAnnotations(self):
        return self.clientServerAnnotations

    def addClientServerAnnotation(self, value):
        self.clientServerAnnotations.append(value)
        return self

    def getDelegatedPortAnnotation(self):
        return self.delegatedPortAnnotation

    def setDelegatedPortAnnotation(self, value):
        self.delegatedPortAnnotation = value
        return self

    def getIoHwAbstractionServerAnnotations(self):
        return self.ioHwAbstractionServerAnnotations

    def addIoHwAbstractionServerAnnotation(self, value):
        self.ioHwAbstractionServerAnnotations.append(value)
        return self

    def getModePortAnnotations(self):
        return self.modePortAnnotations

    def addModePortAnnotation(self, value):
        self.modePortAnnotations.append(value)
        return self

    def getNvDataPortAnnotations(self):
        return self.nvDataPortAnnotations

    def addNvDataPortAnnotation(self, value):
        self.nvDataPortAnnotations.append(value)
        return self

    def getParameterPortAnnotations(self):
        return self.parameterPortAnnotations

    def addParameterPortAnnotation(self, value):
        self.parameterPortAnnotations.append(value)
        return self

    def getSenderReceiverAnnotations(self):
        return self.senderReceiverAnnotations

    def addSenderReceiverAnnotation(self, value):
        self.senderReceiverAnnotations.append(value)
        return self

    def getTriggerPortAnnotations(self):
        return self.triggerPortAnnotations

    def addTriggerPortAnnotation(self, value):
        self.triggerPortAnnotations.append(value)
        return self

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
            if com_spec.getOperationRef() is not None:
                if com_spec.getOperationRef().getDest() != "CLIENT-SERVER-OPERATION":
                    raise ValueError("Invalid operation dest of ClientComSpec.")
        elif isinstance(com_spec, NonqueuedReceiverComSpec):
            if com_spec.getDataElementRef() is not None:
                if com_spec.getDataElementRef().getDest() != "VARIABLE-DATA-PROTOTYPE":
                    raise ValueError("Invalid date element dest of NonqueuedReceiverComSpec.")
        elif isinstance(com_spec, QueuedReceiverComSpec):
            pass
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            pass
        elif isinstance(com_spec, ParameterRequireComSpec):
            if com_spec.getParameterRef() is not None:
                if com_spec.getParameterRef().getDest() != "PARAMETER-DATA-PROTOTYPE":
                    raise ValueError("Invalid parameter dest of ParameterRequireComSpec.")
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

        self.providedInterfaceTRef = None           # type: TRefType

    def getProvidedInterfaceTRef(self):
        return self.providedInterfaceTRef

    def setProvidedInterfaceTRef(self, value):
        self.providedInterfaceTRef = value
        return self

class RPortPrototype(AbstractRequiredPortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.mayBeUnconnected = None                # type: ARBoolean
        self.requiredInterfaceTRef = None           # type: TRefType

    def getMayBeUnconnected(self):
        return self.mayBeUnconnected

    def setMayBeUnconnected(self, value):
        self.mayBeUnconnected = value
        return self

    def getRequiredInterfaceTRef(self):
        return self.requiredInterfaceTRef

    def setRequiredInterfaceTRef(self, value):
        self.requiredInterfaceTRef = value
        return self

class PortGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._inner_group_iref = []    # type: List[InnerPortGroupInCompositionInstanceRef]
        self._outer_port_ref = []      # type: List[RefType]

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef):
        self._inner_group_iref.append(iref)

    def getInnerGroupIRefs(self) -> List[InnerPortGroupInCompositionInstanceRef]:
        return self._inner_group_iref
    
    def addOuterPortRef(self, ref: RefType):
        self._outer_port_ref.append(ref)

    def getOuterPortRefs(self) -> List[RefType]:
        return self._outer_port_ref

class SwComponentType(ARElement,  metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        prototype = PPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def createRPortPrototype(self, short_name) -> RPortPrototype:
        prototype = RPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]
    
    def createPortGroup(self, short_name) -> PortGroup:
        port_group = PortGroup(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = port_group
        return self.elements[short_name]

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.elements.values()), key= lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortPrototypes(self) -> List[PortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortGroups(self) -> List[PortGroup]:
        return list(sorted(filter(lambda c: isinstance(c, PortGroup), self.elements.values()), key= lambda o: o.short_name))

