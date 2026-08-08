from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import SwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector as AssemblySwConnector,
    DelegationSwConnector as DelegationSwConnector,
    SwComponentPrototype as SwComponentPrototype,
    SwConnector as SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable as Identifiable,
    ARElement as ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TRefType as TRefType,
    ARBoolean as ARBoolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ParameterRequireComSpec, QueuedReceiverComSpec, QueuedSenderComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import RPortComSpec, ServerComSpec


class SymbolProps(ImplementationProps):
    # SymbolProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class PortPrototype(AtpPrototype, ABC):
    # PortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getClientServerAnnotations   [x] impl  [ ] docstring  [ ] test
    # [ ] addClientServerAnnotation    [x] impl  [ ] docstring  [ ] test
    # [ ] getDelegatedPortAnnotation   [x] impl  [ ] docstring  [ ] test
    # [ ] setDelegatedPortAnnotation   [x] impl  [ ] docstring  [ ] test
    # [ ] getIoHwAbstractionServerAnnotations [x] impl  [ ] docstring  [ ] test
    # [ ] addIoHwAbstractionServerAnnotation [x] impl  [ ] docstring  [ ] test
    # [ ] getModePortAnnotations       [x] impl  [ ] docstring  [ ] test
    # [ ] addModePortAnnotation        [x] impl  [ ] docstring  [ ] test
    # [ ] getNvDataPortAnnotations     [x] impl  [ ] docstring  [ ] test
    # [ ] addNvDataPortAnnotation      [x] impl  [ ] docstring  [ ] test
    # [ ] getParameterPortAnnotations  [x] impl  [ ] docstring  [ ] test
    # [ ] addParameterPortAnnotation   [x] impl  [ ] docstring  [ ] test
    # [ ] getSenderReceiverAnnotations [x] impl  [ ] docstring  [ ] test
    # [ ] addSenderReceiverAnnotation  [x] impl  [ ] docstring  [ ] test
    # [ ] getTriggerPortAnnotations    [x] impl  [ ] docstring  [ ] test
    # [ ] addTriggerPortAnnotation     [x] impl  [ ] docstring  [ ] test

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
    # AbstractProvidedPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] _validateRPortComSpec        [x] impl  [ ] docstring  [ ] test
    # [ ] addProvidedComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getProvidedComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] getNonqueuedSenderComSpecs   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.providedComSpecs = []  # type: List[PPortComSpec]

    def _validateRPortComSpec(self, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            if com_spec.dataElementRef is None:
                raise ValueError("operation of NonqueuedSenderComSpec is invalid")
            if com_spec.dataElementRef.dest != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError("Invalid operation dest of NonqueuedSenderComSpec")
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
        self.providedComSpecs.append(com_spec)

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        return self.providedComSpecs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedSenderComSpec), self.providedComSpecs)


class AbstractRequiredPortPrototype(PortPrototype):
    # AbstractRequiredPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] _validateRPortComSpec        [x] impl  [ ] docstring  [ ] test
    # [ ] addRequiredComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getRequiredComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] getClientComSpecs            [x] impl  [ ] docstring  [ ] test
    # [ ] getNonqueuedReceiverComSpecs [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.requiredComSpecs = []  # type: List[RPortComSpec]

    def _validateRPortComSpec(self, com_spec: RPortComSpec):
        if isinstance(com_spec, ClientComSpec):
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
        self.requiredComSpecs.append(com_spec)

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        return self.requiredComSpecs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return filter(lambda c: isinstance(c, ClientComSpec), self.requiredComSpecs)

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedReceiverComSpec), self.requiredComSpecs)


class PPortPrototype(AbstractProvidedPortPrototype):
    # PPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getProvidedInterfaceTRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setProvidedInterfaceTRef     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providedInterfaceTRef = None  # type: TRefType

    def getProvidedInterfaceTRef(self):
        return self.providedInterfaceTRef

    def setProvidedInterfaceTRef(self, value):
        self.providedInterfaceTRef = value
        return self


class RPortPrototype(AbstractRequiredPortPrototype):
    # RPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMayBeUnconnected          [x] impl  [ ] docstring  [ ] test
    # [ ] setMayBeUnconnected          [x] impl  [ ] docstring  [ ] test
    # [ ] getRequiredInterfaceTRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setRequiredInterfaceTRef     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.mayBeUnconnected = None  # type: ARBoolean
        self.requiredInterfaceTRef = None  # type: TRefType

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
    # PRPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getProvidedComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] addProvidedComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getRequiredComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] addRequiredComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getProvidedRequiredInterface [x] impl  [ ] docstring  [ ] test
    # [ ] setProvidedRequiredInterface [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.providedComSpecs = []  # type: List[PPortComSpec]
        self.requiredComSpecs = []  # type: List[RPortComSpec]
        self.providedRequiredInterface = None  # type: TRefType

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
    # PortGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addInnerGroupIRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getInnerGroupIRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addOuterPortRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getOuterPortRefs             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._inner_group_iref = []  # type: List[InnerPortGroupInCompositionInstanceRef]
        self._outer_port_ref = []  # type: List[RefType]

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef):
        self._inner_group_iref.append(iref)

    def getInnerGroupIRefs(self) -> List[InnerPortGroupInCompositionInstanceRef]:
        return self._inner_group_iref

    def addOuterPortRef(self, ref: RefType):
        self._outer_port_ref.append(ref)

    def getOuterPortRefs(self) -> List[RefType]:
        return self._outer_port_ref


class AtomicSwComponentType(SwComponentType, ABC):
    """
    An atomic software component is atomic in the sense that it cannot be
    further decomposed and distributed across multiple ECUs.
    """

    # AtomicSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.8, p.70
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getInternalBehavior          [x] impl  [x] docstring  [x] test
    # [x] createSwcInternalBehavior    [x] impl  [x] docstring  [x] test
    # [x] getSymbolProps               [x] impl  [x] docstring  [x] test
    # [x] createSymbolProps            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The SwcInternalBehaviors owned by an AtomicSwComponentType can be
        # located in a different physical file.
        self.internalBehavior: Optional[SwcInternalBehavior] = None

        # This represents the SymbolProps for the AtomicSwComponentType.
        self.symbolProps: Optional[SymbolProps] = None

    def getInternalBehavior(self) -> Optional[SwcInternalBehavior]:
        """
        Gets the SwcInternalBehavior of this atomic software component, which
        describes the relevant aspects of the software-component with respect
        to the RTE.

        Returns:
            The aggregated SwcInternalBehavior, or None if not set
        """
        return self.internalBehavior

    def createSwcInternalBehavior(self, short_name: str) -> SwcInternalBehavior:
        """
        Creates and adds a SwcInternalBehavior with the given short name, or
        returns the existing one if it already exists.

        Args:
            short_name: The short name for the new SwcInternalBehavior

        Returns:
            The created (or existing) SwcInternalBehavior
        """
        if not self.IsElementExists(short_name, SwcInternalBehavior):
            behavior = SwcInternalBehavior(self, short_name)
            self.addElement(behavior)
            self.internalBehavior = behavior
        return self.getElement(short_name, SwcInternalBehavior)

    def getSymbolProps(self) -> Optional[SymbolProps]:
        """
        Gets the SymbolProps for the AtomicSwComponentType, which represent the
        symbolic name used to mitigate name clashes in RTE source code.

        Returns:
            The aggregated SymbolProps, or None if not set
        """
        return self.symbolProps

    def createSymbolProps(self, short_name: str) -> SymbolProps:
        """
        Creates and adds the SymbolProps for the AtomicSwComponentType with the
        given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new SymbolProps

        Returns:
            The created (or existing) SymbolProps
        """
        if not self.IsElementExists(short_name, SymbolProps):
            symbol_props = SymbolProps(self, short_name)
            self.addElement(symbol_props)
            self.symbolProps = symbol_props
        return self.getElement(short_name, SymbolProps)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    # EcuAbstractionSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getHardwareElementRefs       [x] impl  [ ] docstring  [ ] test
    # [ ] addHardwareElementRefs       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.hardwareElementRefs = []  # List[RefType]

    def getHardwareElementRefs(self):
        return self.hardwareElementRefs

    def addHardwareElementRefs(self, value):
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class ApplicationSwComponentType(AtomicSwComponentType):
    # ApplicationSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    # ComplexDeviceDriverSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getHardwareElementRefs       [x] impl  [ ] docstring  [ ] test
    # [ ] addHardwareElementRefs       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.hardwareElementRefs = []  # List[RefType]

    def getHardwareElementRefs(self):
        return self.hardwareElementRefs

    def addHardwareElementRefs(self, value):
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class NvBlockSwComponentType(AtomicSwComponentType):
    # NvBlockSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBulkNvDataDescriptors     [x] impl  [ ] docstring  [ ] test
    # [ ] addBulkNvDataDescriptor      [x] impl  [ ] docstring  [ ] test
    # [ ] getNvBlockDescriptors        [x] impl  [ ] docstring  [ ] test
    # [ ] setNvBlockDescriptor         [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bulkNvDataDescriptors = []  # type: List[BulkNvDataDescriptor]
        self.nvBlockDescriptors = []  # type: List[NvBlockDescriptor]

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
    # SensorActuatorSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ServiceProxySwComponentType(AtomicSwComponentType):
    # ServiceProxySwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ServiceSwComponentType(AtomicSwComponentType):
    # ServiceSwComponentType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
