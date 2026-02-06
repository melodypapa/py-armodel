from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpPrototype,
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    RefType,
    TRefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    RPortComSpec,
    ServerComSpec,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    DelegationSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
    SwComponentType,
)


class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class PortPrototype(AtpPrototype, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortPrototype:
            raise TypeError("PortPrototype is an abstract class.")
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
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.providedComSpecs = []                  # type: List[PPortComSpec]

    def _validateRPortComSpec(self, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            if com_spec.dataElementRef is None:
                raise ValueError(
                    "operation of NonqueuedSenderComSpec is invalid")
            if com_spec.dataElementRef.dest != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError(
                    "Invalid operation dest of NonqueuedSenderComSpec")
        elif isinstance(com_spec, (ServerComSpec, QueuedSenderComSpec, ModeSwitchSenderComSpec)):
            pass
        else:
            raise ValueError("Unsupported com spec")

    def addProvidedComSpec(self, com_spec):
        self._validateRPortComSpec(com_spec)
        self.providedComSpecs.append(com_spec)

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        return self.providedComSpecs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedSenderComSpec), self.providedComSpecs)


class AbstractRequiredPortPrototype(PortPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.requiredComSpecs = []                          # type: List[RPortComSpec]

    def _validateRPortComSpec(self, com_spec: RPortComSpec):
        if (isinstance(com_spec, ClientComSpec) and
            com_spec.getOperationRef() is not None and
            com_spec.getOperationRef().getDest() != "CLIENT-SERVER-OPERATION"):
            raise ValueError("Invalid operation dest of ClientComSpec.")
        elif (isinstance(com_spec, NonqueuedReceiverComSpec) and
              com_spec.getDataElementRef() is not None and
              com_spec.getDataElementRef().getDest() != "VARIABLE-DATA-PROTOTYPE"):
            raise ValueError("Invalid date element dest of NonqueuedReceiverComSpec.")
        elif isinstance(com_spec, (QueuedReceiverComSpec, ModeSwitchReceiverComSpec)):
            pass
        elif (isinstance(com_spec, ParameterRequireComSpec) and
              com_spec.getParameterRef() is not None and
              com_spec.getParameterRef().getDest() != "PARAMETER-DATA-PROTOTYPE"):
            raise ValueError("Invalid parameter dest of ParameterRequireComSpec.")
        else:
            raise ValueError("Unsupported RPortComSpec <%s>" % type(com_spec))

    def addRequiredComSpec(self, com_spec: RPortComSpec):
        self._validateRPortComSpec(com_spec)
        self.requiredComSpecs.append(com_spec)

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        return self.requiredComSpecs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return filter(lambda c: isinstance(c, ClientComSpec), self.requiredComSpecs)

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedReceiverComSpec), self.requiredComSpecs)


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


class PRPortPrototype(PortPrototype):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.providedComSpecs = []                          # type: List[PPortComSpec]
        self.requiredComSpecs = []                          # type: List[RPortComSpec]
        self.providedRequiredInterface = None               # type: TRefType

    def getProvidedComSpecs(self):
        return self.providedComSpecs

    def addProvidedComSpec(self, value):
        self.providedComSpecs.append(value)
        return self

    def getRequiredComSpecs(self):
        return self.requiredComSpecs

    def addRequiredComSpec(self, value):
        self.requiredComSpecs.append(value)
        return self

    def getProvidedRequiredInterface(self):
        return self.providedRequiredInterface

    def setProvidedRequiredInterface(self, value):
        self.providedRequiredInterface = value
        return self


class PortGroup(AtpStructureElement):
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


class AtomicSwComponentType(SwComponentType, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.internalBehavior: "SwcInternalBehavior" = None
        self.symbolProps: SymbolProps = None

    def getInternalBehavior(self):
        return self.internalBehavior

    def createSwcInternalBehavior(self, short_name) -> "SwcInternalBehavior":
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
            SwcInternalBehavior,
        )
        if (not self.IsElementExists(short_name, SwcInternalBehavior)):
            behavior = SwcInternalBehavior(self, short_name)
            self.addElement(behavior)
            self.internalBehavior = behavior
        return self.getElement(short_name, SwcInternalBehavior)

    def getSymbolProps(self):
        return self.symbolProps

    def setSymbolProps(self, value):
        if value is not None:
            self.symbolProps = value
        return self

    '''
    @property
    def internal_behavior(self) -> "SwcInternalBehavior":
        return next(filter(lambda e: isinstance(e, "SwcInternalBehavior"), self.elements))
    '''


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.hardwareElementRefs = []                                   # List[RefType]

    def getHardwareElementRefs(self):
        return self.hardwareElementRefs

    def addHardwareElementRefs(self, value):
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class ApplicationSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.hardwareElementRefs = []                                   # List[RefType]

    def getHardwareElementRefs(self):
        return self.hardwareElementRefs

    def addHardwareElementRefs(self, value):
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class NvBlockSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bulkNvDataDescriptors = []                                 # type: List[BulkNvDataDescriptor]
        self.nvBlockDescriptors = []                                    # type: List[NvBlockDescriptor]

    def getBulkNvDataDescriptors(self):
        return self.bulkNvDataDescriptors

    def addBulkNvDataDescriptor(self, value):
        if value is not None:
            self.bulkNvDataDescriptors.append(value)
        return self

    def getNvBlockDescriptors(self):
        return self.nvBlockDescriptors

    def setNvBlockDescriptor(self, value):
        if value is not None:
            self.nvBlockDescriptors.append(value)
        return self


class SensorActuatorSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ServiceProxySwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ServiceSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


__all__ = [
    'SymbolProps',
    'PortPrototype',
    'AbstractProvidedPortPrototype',
    'AbstractRequiredPortPrototype',
    'PPortPrototype',
    'RPortPrototype',
    'PRPortPrototype',
    'PortGroup',
    'AtomicSwComponentType',
    'EcuAbstractionSwComponentType',
    'ApplicationSwComponentType',
    'ComplexDeviceDriverSwComponentType',
    'NvBlockSwComponentType',
    'SensorActuatorSwComponentType',
    'ServiceProxySwComponentType',
    'ServiceSwComponentType',
]
