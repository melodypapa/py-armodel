from __future__ import annotations

from abc import ABC
from typing import List, Optional, TYPE_CHECKING
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement as ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable as Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import (
    VariationPointCapable as VariationPointCapable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TRefType,
    Boolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, NvProvideComSpec, ParameterProvideComSpec, PPortComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ParameterRequireComSpec, QueuedReceiverComSpec, QueuedSenderComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import RPortComSpec, ServerComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DelegatedPortAnnotation,
    IoHwAbstractionServerAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    SenderReceiverAnnotation,
    TriggerPortAnnotation,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
        InnerPortGroupInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
        ConsistencyNeeds,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
        SwComponentDocumentation,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
        SwcInternalBehavior,
    )


class SwComponentType(AtpType, ABC):
    """
    Base class for AUTOSAR software components.
    """

    # SwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.1, p.64
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createConsistencyNeeds       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsistencyNeeds          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createPPortPrototype         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createRPortPrototype         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createPRPortPrototype        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPorts                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPPortPrototypes           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRPortPrototypes           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPRPortPrototypes          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPortPrototypes            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createPortGroup              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPortGroups                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwcMappingConstraintRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwcMappingConstraintsRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addUnitGroupRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnitGroupRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.
        self.consistencyNeeds: List[ConsistencyNeeds] = []

        # The PortPrototypes through which this SwComponent Type can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        self.ports: List[PortPrototype] = []

        # A port group being part of this component.
        self.portGroups: List[PortGroup] = []

        # Reference to constraints that are valid for this SwComponentType.
        self.swcMappingConstraintsRefs: List[RefType] = []

        # This adds a documentation to the SwComponentType.
        self.swComponentDocumentation: Optional[SwComponentDocumentation] = None

        # This allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
        self.unitGroupRefs: List[RefType] = []

    def createConsistencyNeeds(self, short_name: str) -> ConsistencyNeeds:
        """
        Creates a ConsistencyNeeds owned by the enclosing SwComponentType.
        Returns the existing ConsistencyNeeds when the short name already exists.

        Args:
            short_name: The short name of the ConsistencyNeeds

        Returns:
            The created or existing ConsistencyNeeds
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import ConsistencyNeeds

        if not self.IsElementExists(short_name, ConsistencyNeeds):
            consistency_needs = ConsistencyNeeds(self, short_name)
            self.addElement(consistency_needs)
            self.consistencyNeeds.append(consistency_needs)
        return self.getElement(short_name, ConsistencyNeeds)

    def getConsistencyNeeds(self) -> List[ConsistencyNeeds]:
        """
        Gets the collection of ConsistencyNeeds owned by the enclosing SwComponentType.

        Returns:
            List of ConsistencyNeeds instances
        """
        return self.consistencyNeeds

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        """
        Creates a PPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the PPortPrototype

        Returns:
            The created or existing PPortPrototype
        """
        if not self.IsElementExists(short_name, PPortPrototype):
            prototype = PPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, PPortPrototype)

    def createRPortPrototype(self, short_name: str) -> RPortPrototype:
        """
        Creates an RPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing RPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the RPortPrototype

        Returns:
            The created or existing RPortPrototype
        """
        if not self.IsElementExists(short_name, RPortPrototype):
            prototype = RPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, RPortPrototype)

    def createPRPortPrototype(self, short_name: str) -> PRPortPrototype:
        """
        Creates a PRPortPrototype of this SwComponentType. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PRPortPrototype when the short name already exists.

        Args:
            short_name: The short name of the PRPortPrototype

        Returns:
            The created or existing PRPortPrototype
        """
        if not self.IsElementExists(short_name, PRPortPrototype):
            prototype = PRPortPrototype(self, short_name)
            self.addElement(prototype)
            self.ports.append(prototype)
        return self.getElement(short_name, PRPortPrototype)

    def getPorts(self) -> List[PortPrototype]:
        """
        Gets the PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.

        Returns:
            List of PortPrototype instances
        """
        return self.ports

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        """
        Convenience getter for the PPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PPortPrototype instances
        """
        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.ports), key=lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        """
        Convenience getter for the RPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of RPortPrototype instances
        """
        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPRPortPrototypes(self) -> List[PRPortPrototype]:
        """
        Convenience getter for the PRPortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PRPortPrototype instances
        """
        return list(sorted(filter(lambda c: isinstance(c, PRPortPrototype), self.ports), key=lambda o: o.short_name))

    def getPortPrototypes(self) -> List[PortPrototype]:
        """
        Convenience getter for all PortPrototype instances aggregated by this SwComponentType.

        Returns:
            List of PortPrototype instances
        """
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.ports), key=lambda o: o.short_name))

    def createPortGroup(self, short_name: str) -> PortGroup:
        """
        Creates a PortGroup being part of this component.
        Returns the existing PortGroup when the short name already exists.

        Args:
            short_name: The short name of the PortGroup

        Returns:
            The created or existing PortGroup
        """
        if not self.IsElementExists(short_name, PortGroup):
            port_group = PortGroup(self, short_name)
            self.addElement(port_group)
            self.portGroups.append(port_group)
        return self.getElement(short_name, PortGroup)

    def getPortGroups(self) -> List[PortGroup]:
        """
        Gets the PortGroups being part of this component.

        Returns:
            List of PortGroup instances
        """
        return self.portGroups

    def addSwcMappingConstraintRef(self, value: Optional[RefType]) -> "SwComponentType":
        """
        Adds a reference to constraints that are valid for this SwComponentType.
        A None value is a no-op and does not append anything.

        Args:
            value: The SwComponentMappingConstraints reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcMappingConstraintsRefs.append(value)
        return self

    def getSwcMappingConstraintsRefs(self) -> List[RefType]:
        """
        Gets the references to constraints that are valid for this SwComponentType.

        Returns:
            List of RefType instances
        """
        return self.swcMappingConstraintsRefs

    def getSwComponentDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        Gets the documentation that is added to the SwComponentType.

        Returns:
            SwComponentDocumentation, or None if not set
        """
        return self.swComponentDocumentation

    def setSwComponentDocumentation(self, value: Optional[SwComponentDocumentation]) -> "SwComponentType":
        """
        Sets the documentation that is added to the SwComponentType.
        A None value is a no-op and does not overwrite an existing documentation.

        Args:
            value: The SwComponentDocumentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swComponentDocumentation = value
        return self

    def addUnitGroupRef(self, value: Optional[RefType]) -> "SwComponentType":
        """
        Adds a reference which allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
        A None value is a no-op and does not append anything.

        Args:
            value: The UnitGroup reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.unitGroupRefs.append(value)
        return self

    def getUnitGroupRefs(self) -> List[RefType]:
        """
        Gets the references which allow for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.

        Returns:
            List of RefType instances
        """
        return self.unitGroupRefs


class SymbolProps(ImplementationProps):
    """
    This meta-class represents the ability to attach with the symbol attribute a symbolic name that is conform to C language requirements to another meta-class, e.g. AtomicSwComponentType, that is a potential subject to a name clash on the level of RTE source code.
    """

    # SymbolProps method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.21, p.288 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class PortPrototype(AtpPrototype, AtpBlueprintable, VariationPointCapable, ABC):
    """
    Base class for the ports of an AUTOSAR software component. The aggregation of PortPrototypes is subject to variability with the purpose to support the conditional existence of ports.
    """

    # PortPrototype method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.2, p.66 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addClientServerAnnotation       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClientServerAnnotations      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDelegatedPortAnnotation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDelegatedPortAnnotation      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addIoHwAbstractionServerAnnotation [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIoHwAbstractionServerAnnotations [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModePortAnnotation           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModePortAnnotations          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addNvDataPortAnnotation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvDataPortAnnotations        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addParameterPortAnnotation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParameterPortAnnotations     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSenderReceiverAnnotation     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSenderReceiverAnnotations    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTriggerPortAnnotation        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggerPortAnnotations       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PortPrototype:
            raise TypeError("PortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        # Annotation of this PortPrototype with respect to client/server communication.
        self.clientServerAnnotations: List[ClientServerAnnotation] = []

        # Annotations on this delegated port.
        self.delegatedPortAnnotation: Optional[DelegatedPortAnnotation] = None

        # Annotations on this IO Hardware Abstraction port.
        self.ioHwAbstractionServerAnnotations: List[IoHwAbstractionServerAnnotation] = []

        # Annotations on this mode port.
        self.modePortAnnotations: List[ModePortAnnotation] = []

        # Annotations on this non voilatile data port.
        self.nvDataPortAnnotations: List[NvDataPortAnnotation] = []

        # Annotations on this parameter port.
        self.parameterPortAnnotations: List[ParameterPortAnnotation] = []

        # Collection of annotations of this ports sender/receiver communication.
        self.senderReceiverAnnotations: List[SenderReceiverAnnotation] = []

        # Annotations on this trigger port.
        self.triggerPortAnnotations: List[TriggerPortAnnotation] = []

    def getClientServerAnnotations(self) -> List[ClientServerAnnotation]:
        """
        Gets the annotations of this PortPrototype with respect to client/server communication.

        Returns:
            List of ClientServerAnnotation instances
        """
        return self.clientServerAnnotations

    def addClientServerAnnotation(self, value: Optional[ClientServerAnnotation]) -> "PortPrototype":
        """
        Adds an annotation of this PortPrototype with respect to client/server communication.
        A None value is a no-op and does not append anything.

        Args:
            value: The ClientServerAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.clientServerAnnotations.append(value)
        return self

    def getDelegatedPortAnnotation(self) -> Optional[DelegatedPortAnnotation]:
        """
        Gets the annotations on this delegated port.

        Returns:
            DelegatedPortAnnotation, or None if not set
        """
        return self.delegatedPortAnnotation

    def setDelegatedPortAnnotation(self, value: Optional[DelegatedPortAnnotation]) -> "PortPrototype":
        """
        Sets the annotations on this delegated port.
        A None value is a no-op and does not overwrite an existing annotation.

        Args:
            value: The DelegatedPortAnnotation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.delegatedPortAnnotation = value
        return self

    def getIoHwAbstractionServerAnnotations(self) -> List[IoHwAbstractionServerAnnotation]:
        """
        Gets the annotations on this IO Hardware Abstraction port.

        Returns:
            List of IoHwAbstractionServerAnnotation instances
        """
        return self.ioHwAbstractionServerAnnotations

    def addIoHwAbstractionServerAnnotation(self, value: Optional[IoHwAbstractionServerAnnotation]) -> "PortPrototype":
        """
        Adds an annotation on this IO Hardware Abstraction port.
        A None value is a no-op and does not append anything.

        Args:
            value: The IoHwAbstractionServerAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ioHwAbstractionServerAnnotations.append(value)
        return self

    def getModePortAnnotations(self) -> List[ModePortAnnotation]:
        """
        Gets the annotations on this mode port.

        Returns:
            List of ModePortAnnotation instances
        """
        return self.modePortAnnotations

    def addModePortAnnotation(self, value: Optional[ModePortAnnotation]) -> "PortPrototype":
        """
        Adds an annotation on this mode port.
        A None value is a no-op and does not append anything.

        Args:
            value: The ModePortAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modePortAnnotations.append(value)
        return self

    def getNvDataPortAnnotations(self) -> List[NvDataPortAnnotation]:
        """
        Gets the annotations on this non voilatile data port.

        Returns:
            List of NvDataPortAnnotation instances
        """
        return self.nvDataPortAnnotations

    def addNvDataPortAnnotation(self, value: Optional[NvDataPortAnnotation]) -> "PortPrototype":
        """
        Adds an annotation on this non voilatile data port.
        A None value is a no-op and does not append anything.

        Args:
            value: The NvDataPortAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nvDataPortAnnotations.append(value)
        return self

    def getParameterPortAnnotations(self) -> List[ParameterPortAnnotation]:
        """
        Gets the annotations on this parameter port.

        Returns:
            List of ParameterPortAnnotation instances
        """
        return self.parameterPortAnnotations

    def addParameterPortAnnotation(self, value: Optional[ParameterPortAnnotation]) -> "PortPrototype":
        """
        Adds an annotation on this parameter port.
        A None value is a no-op and does not append anything.

        Args:
            value: The ParameterPortAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.parameterPortAnnotations.append(value)
        return self

    def getSenderReceiverAnnotations(self) -> List[SenderReceiverAnnotation]:
        """
        Gets the collection of annotations of this ports sender/receiver communication.

        Returns:
            List of SenderReceiverAnnotation instances
        """
        return self.senderReceiverAnnotations

    def addSenderReceiverAnnotation(self, value: Optional[SenderReceiverAnnotation]) -> "PortPrototype":
        """
        Adds an annotation of this ports sender/receiver communication.
        A None value is a no-op and does not append anything.

        Args:
            value: The SenderReceiverAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.senderReceiverAnnotations.append(value)
        return self

    def getTriggerPortAnnotations(self) -> List[TriggerPortAnnotation]:
        """
        Gets the annotations on this trigger port.

        Returns:
            List of TriggerPortAnnotation instances
        """
        return self.triggerPortAnnotations

    def addTriggerPortAnnotation(self, value: Optional[TriggerPortAnnotation]) -> "PortPrototype":
        """
        Adds an annotation on this trigger port.
        A None value is a no-op and does not append anything.

        Args:
            value: The TriggerPortAnnotation to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerPortAnnotations.append(value)
        return self


class AbstractProvidedPortPrototype(PortPrototype):
    # AbstractProvidedPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] _validateProvidedComSpec     [x] impl  [ ] docstring  [ ] test
    # [ ] addProvidedComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getProvidedComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] getNonqueuedSenderComSpecs   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.providedComSpecs = []  # type: List[PPortComSpec]

    def _validateProvidedComSpec(self, com_spec: PPortComSpec):
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
        elif isinstance(com_spec, NvProvideComSpec):
            pass
        elif isinstance(com_spec, ParameterProvideComSpec):
            pass
        else:
            raise ValueError("Unsupported com spec")

    def addProvidedComSpec(self, com_spec):
        self._validateProvidedComSpec(com_spec)
        self.providedComSpecs.append(com_spec)

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        return self.providedComSpecs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedSenderComSpec), self.providedComSpecs)


class AbstractRequiredPortPrototype(PortPrototype):
    # AbstractRequiredPortPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] _validateRequiredComSpec     [x] impl  [ ] docstring  [ ] test
    # [ ] addRequiredComSpec           [x] impl  [ ] docstring  [ ] test
    # [ ] getRequiredComSpecs          [x] impl  [ ] docstring  [ ] test
    # [ ] getClientComSpecs            [x] impl  [ ] docstring  [ ] test
    # [ ] getNonqueuedReceiverComSpecs [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        self.requiredComSpecs = []  # type: List[RPortComSpec]

    def _validateRequiredComSpec(self, com_spec: RPortComSpec):
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
        self._validateRequiredComSpec(com_spec)
        self.requiredComSpecs.append(com_spec)

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        return self.requiredComSpecs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return filter(lambda c: isinstance(c, ClientComSpec), self.requiredComSpecs)

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return filter(lambda c: isinstance(c, NonqueuedReceiverComSpec), self.requiredComSpecs)


class PPortPrototype(AbstractProvidedPortPrototype):
    """
    Component port providing a certain port interface.
    """

    # PPortPrototype method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.6, p.68 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getProvidedInterfaceTRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setProvidedInterfaceTRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The interface that this port provides. Stereotypes: isOfType
        self.providedInterfaceTRef: Optional[TRefType] = None

    def getProvidedInterfaceTRef(self) -> Optional[TRefType]:
        """
        The interface that this port provides. Stereotypes: isOfType
        """
        return self.providedInterfaceTRef

    def setProvidedInterfaceTRef(self, value: Optional[TRefType]) -> "PPortPrototype":
        """
        The interface that this port provides. Stereotypes: isOfType
        """
        if value is not None:
            self.providedInterfaceTRef = value
        return self


class RPortPrototype(AbstractRequiredPortPrototype):
    """
    Component port requiring a certain port interface.
    """

    # RPortPrototype method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.5, p.68 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMayBeUnconnected             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMayBeUnconnected             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRequiredInterfaceTRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRequiredInterfaceTRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # If set to true, this attribute indicates that the enclosing RPortPrototype may be left unconnected and that this aspect has explicitly been considered in the software-component's design.
        self.mayBeUnconnected: Optional[Boolean] = None

        # The interface that this port requires. Stereotypes: isOfType
        self.requiredInterfaceTRef: Optional[TRefType] = None

    def getMayBeUnconnected(self) -> Optional[Boolean]:
        """
        If set to true, this attribute indicates that the enclosing RPortPrototype may be left unconnected and that this aspect has explicitly been considered in the software-component's design.
        """
        return self.mayBeUnconnected

    def setMayBeUnconnected(self, value: Optional[Boolean]) -> "RPortPrototype":
        """
        If set to true, this attribute indicates that the enclosing RPortPrototype may be left unconnected and that this aspect has explicitly been considered in the software-component's design.
        """
        if value is not None:
            self.mayBeUnconnected = value
        return self

    def getRequiredInterfaceTRef(self) -> Optional[TRefType]:
        """
        The interface that this port requires. Stereotypes: isOfType
        """
        return self.requiredInterfaceTRef

    def setRequiredInterfaceTRef(self, value: Optional[TRefType]) -> "RPortPrototype":
        """
        The interface that this port requires. Stereotypes: isOfType
        """
        if value is not None:
            self.requiredInterfaceTRef = value
        return self


class PRPortPrototype(AbstractProvidedPortPrototype, AbstractRequiredPortPrototype):
    """
    This kind of PortPrototype can take the role of both a required and a provided PortPrototype.
    """

    # PRPortPrototype method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.7, p.68 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getProvidedRequiredInterfaceTRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setProvidedRequiredInterfaceTRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the PortInterface used to type the PRPortPrototype Stereotypes: isOfType
        self.providedRequiredInterfaceTRef: Optional[TRefType] = None

    def getProvidedRequiredInterfaceTRef(self) -> Optional[TRefType]:
        """
        This represents the PortInterface used to type the PRPortPrototype Stereotypes: isOfType
        """
        return self.providedRequiredInterfaceTRef

    def setProvidedRequiredInterfaceTRef(self, value: Optional[TRefType]) -> "PRPortPrototype":
        """
        This represents the PortInterface used to type the PRPortPrototype Stereotypes: isOfType
        If value is None, the existing value is not changed.
        """
        if value is not None:
            self.providedRequiredInterfaceTRef = value
        return self


class PortGroup(AtpStructureElement):
    """
    Group of ports which share a common functionality , e.g. need specific network resources. This information shall be available on the VFB level in order to delegate it properly via compositions. When propagated into the ECU extract, this information is used as input for the configuration of Services like the Communication Manager. A PortGroup is defined locally in a component (which can be a composition) and refers to the "outer" ports belonging to the group as well as to the "inner" groups which propagate this group into the components which are part of a composition. A PortGroup within an atomic SWC cannot be linked to inner groups.
    """

    # PortGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.94, p.203 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addInnerGroupIRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInnerGroupIRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addOuterPortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOuterPortRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. InstanceRef implemented by: InnerPortGroupInCompositionInstanceRef
        self.innerGroupIRefs: List[InnerPortGroupInCompositionInstanceRef] = []

        # Outer PortPrototype of this AtomicSwComponentType which belongs to the group. A port can belong to several groups or to no group at all.
        self.outerPortRefs: List[RefType] = []

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef) -> "PortGroup":
        """
        Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. InstanceRef implemented by: InnerPortGroupInCompositionInstanceRef
        """
        self.innerGroupIRefs.append(iref)
        return self

    def getInnerGroupIRefs(self) -> List[InnerPortGroupInCompositionInstanceRef]:
        """
        Links a PortGroup in a composition to another PortGroup, that is defined in a component which is part of this CompositionSwComponentType. InstanceRef implemented by: InnerPortGroupInCompositionInstanceRef
        """
        return self.innerGroupIRefs

    def addOuterPortRef(self, ref: RefType) -> "PortGroup":
        """
        Outer PortPrototype of this AtomicSwComponentType which belongs to the group. A port can belong to several groups or to no group at all.
        """
        self.outerPortRefs.append(ref)
        return self

    def getOuterPortRefs(self) -> List[RefType]:
        """
        Outer PortPrototype of this AtomicSwComponentType which belongs to the group. A port can belong to several groups or to no group at all.
        """
        return self.outerPortRefs


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
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior

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
    """
    The ECUAbstraction is a special AtomicSwComponentType that resides between a software-component that wants to access ECU periphery and the Microcontroller Abstraction. The EcuAbstractionSwComponentType introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.2, p.647
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHardwareElementRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHardwareElementRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the EcuAbstractionComponentType to the description of the used HwElements.
        self.hardwareElementRefs: List[RefType] = []

    def getHardwareElementRefs(self) -> List[RefType]:
        """
        Gets the references to the descriptions of the used hardware elements.

        Reference from the EcuAbstractionComponentType to the description of the used HwElements.

        Returns:
            List[RefType]: The list of references to the used HwElements
        """
        return self.hardwareElementRefs

    def addHardwareElementRef(self, value: Optional[RefType]) -> "EcuAbstractionSwComponentType":
        """
        Adds a reference to the description of a used hardware element.
        A None value is a no-op and does not append anything.

        Reference from the EcuAbstractionComponentType to the description of the used HwElements.

        Args:
            value: The reference to the used HwElement

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class ApplicationSwComponentType(AtomicSwComponentType):
    """
    The ApplicationSwComponentType is used to represent the application software.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.9, p.71
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """
    The ComplexDeviceDriverSwComponentType is a special AtomicSwComponentType that has direct access to hardware on an ECU and which is therefore linked to a specific ECU or specific hardware. The ComplexDeviceDriverSwComponentType introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.3, p.648
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addHardwareElementRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHardwareElementRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.
        self.hardwareElementRefs: List[RefType] = []

    def getHardwareElementRefs(self) -> List[RefType]:
        """
        Gets the references to the descriptions of the used hardware elements.

        Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.

        Returns:
            List[RefType]: The list of references to the used HwElements
        """
        return self.hardwareElementRefs

    def addHardwareElementRef(self, value: Optional[RefType]) -> "ComplexDeviceDriverSwComponentType":
        """
        Adds a reference to the description of a used hardware element.
        A None value is a no-op and does not append anything.

        Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.

        Args:
            value: The reference to the used HwElement

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self


class NvBlockSwComponentType(AtomicSwComponentType):
    """
    The NvBlockSwComponentType defines non volatile data which data can be shared between SwComponentPrototypes. The non volatile data of the NvBlockSwComponentType are accessible via provided and required ports.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.4, p.664
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createBulkNvDataDescriptor   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBulkNvDataDescriptors     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createNvBlockDescriptor      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNvBlockDescriptors        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This aggregation formally defines the bulk Nv Blocks that are provided to the application software by the enclosing NvBlockSwComponentType.
        self.bulkNvDataDescriptors: List[BulkNvDataDescriptor] = []

        # Specification of the properties of exactly one NVRAM Block.
        self.nvBlockDescriptors: List[NvBlockDescriptor] = []

    def getBulkNvDataDescriptors(self) -> List[BulkNvDataDescriptor]:
        """
        Gets the bulk NV Data Blocks provided to the application software by this NvBlockSwComponentType.

        This aggregation formally defines the bulk Nv Blocks that are provided to the application software by the enclosing NvBlockSwComponentType.

        Returns:
            List[BulkNvDataDescriptor]: The list of bulk NV data descriptors
        """
        return self.bulkNvDataDescriptors

    def createBulkNvDataDescriptor(self, short_name: str) -> BulkNvDataDescriptor:
        """
        Creates a bulk NV data descriptor of this NvBlockSwComponentType.
        Returns the existing descriptor when the short name already exists.

        This aggregation formally defines the bulk Nv Blocks that are provided to the application software by the enclosing NvBlockSwComponentType.

        Args:
            short_name: The short name of the BulkNvDataDescriptor

        Returns:
            The created or existing BulkNvDataDescriptor
        """
        if not self.IsElementExists(short_name, BulkNvDataDescriptor):
            descriptor = BulkNvDataDescriptor(self, short_name)
            self.addElement(descriptor)
            self.bulkNvDataDescriptors.append(descriptor)
        return self.getElement(short_name, BulkNvDataDescriptor)

    def getNvBlockDescriptors(self) -> List[NvBlockDescriptor]:
        """
        Gets the specification of the properties of the NVRAM Blocks owned by this NvBlockSwComponentType.

        Specification of the properties of exactly one NVRAM Block.

        Returns:
            List[NvBlockDescriptor]: The list of NV block descriptors
        """
        return self.nvBlockDescriptors

    def createNvBlockDescriptor(self, short_name: str) -> NvBlockDescriptor:
        """
        Creates a nvBlockDescriptor of this NvBlockSwComponentType.
        Returns the existing descriptor when the short name already exists.

        Specification of the properties of exactly one NVRAM Block.

        Args:
            short_name: The short name of the NvBlockDescriptor

        Returns:
            The created or existing NvBlockDescriptor
        """
        if not self.IsElementExists(short_name, NvBlockDescriptor):
            descriptor = NvBlockDescriptor(self, short_name)
            self.addElement(descriptor)
            self.nvBlockDescriptors.append(descriptor)
        return self.getElement(short_name, NvBlockDescriptor)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """
    The SensorActuatorSwComponentType introduces the possibility to link from the software representation of a sensor/actuator to its hardware description provided by the ECU Resource Template.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.1, p.646
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSensorActuatorRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSensorActuatorRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.
        self.sensorActuatorRef: Optional[RefType] = None

    def getSensorActuatorRef(self) -> Optional[RefType]:
        """
        Gets the reference to the description of the actual hardware.

        Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.

        Returns:
            Optional[RefType]: The reference to the actual hardware, or None if not set
        """
        return self.sensorActuatorRef

    def setSensorActuatorRef(self, value: Optional[RefType]) -> "SensorActuatorSwComponentType":
        """
        Sets the reference to the description of the actual hardware.
        A None value is a no-op and does not overwrite an existing reference.

        Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.

        Args:
            value: The reference to the actual hardware

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sensorActuatorRef = value
        return self


class ServiceProxySwComponentType(AtomicSwComponentType):
    """
    This class provides the ability to express a software-component which provides access to an internal service for remote ECUs. It acts as a proxy for the service providing access to the service.

    An important use case is the request of vehicle mode switches: Such requests can be communicated via sender-receiver interfaces across ECU boundaries, but the mode manager being responsible to perform the mode switches is an AUTOSAR Service which is located in the Basic Software and is not visible in the VFB view. To handle this situation, a ServiceProxySwComponentType will act as proxy for the mode manager. It will have R-Ports to be connected with the mode requestors on VFB level and Service-Ports to be connected with the local mode manager at ECU integration time.

    Apart from the semantics, a ServiceProxySwComponentType has these specific properties:
    * A prototype of it can be mapped to more than one ECUs in the system description.
    * Exactly one additional instance of it will be created in the ECU-Extract per ECU to which the prototype has been mapped.
    * For remote communication, it can have only R-Ports with sender-receiver interfaces and 1:n semantics.
    * There shall be no connectors between two prototypes of any ServiceProxySwComponentType.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.3, p.661
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ServiceSwComponentType(AtomicSwComponentType):
    """
    ServiceSwComponentType is used for configuring services for a given ECU. Instances of this class are only to be created in ECU Configuration phase for the specific purpose of the service configuration.
    """

    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.2, p.659
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
