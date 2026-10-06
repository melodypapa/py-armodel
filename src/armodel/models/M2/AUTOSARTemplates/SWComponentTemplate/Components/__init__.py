from __future__ import annotations

import logging

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from typing import List, Optional, TYPE_CHECKING, cast
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TRefType,
    Boolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, NvProvideComSpec, ParameterProvideComSpec, PPortComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NvRequireComSpec, ParameterRequireComSpec, QueuedReceiverComSpec, QueuedSenderComSpec
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
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
        SwcInternalBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
        InnerPortGroupInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
        ConsistencyNeeds,
    )


logger = logging.getLogger(__name__)


class SwComponentType(ARElement, ABC):
    """
    Base class for AUTOSAR software components.
    """

    # SwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.1, p.65
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createConsistencyNeeds        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConsistencyNeeds           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createPPortPrototype          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createRPortPrototype          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createPRPortPrototype         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPorts                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPPortPrototypes            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRPortPrototypes            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPRPortPrototypes           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortPrototypes             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createPortGroup               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortGroups                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwcMappingConstraintRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcMappingConstraintsRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwComponentDocumentation   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addUnitGroupRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnitGroupRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        # This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.
        self.consistencyNeeds: List[ConsistencyNeeds] = []

        # The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
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
        This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.
        Returns the existing ConsistencyNeeds when the short name already exists.
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import ConsistencyNeeds

        if not self.IsReferrableElementExists(short_name, ConsistencyNeeds):
            consistency_needs = ConsistencyNeeds(self, short_name)
            self.addReferrableElement(consistency_needs)
            self.consistencyNeeds.append(consistency_needs)
        return cast(ConsistencyNeeds, self.getReferrableElement(short_name, ConsistencyNeeds))

    def getConsistencyNeeds(self) -> List[ConsistencyNeeds]:
        """
        This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.
        """
        return self.consistencyNeeds

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        """
        The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PPortPrototype when the short name already exists.
        """
        if not self.IsReferrableElementExists(short_name, PPortPrototype):
            prototype = PPortPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.ports.append(prototype)
        return cast(PPortPrototype, self.getReferrableElement(short_name, PPortPrototype))

    def createRPortPrototype(self, short_name: str) -> RPortPrototype:
        """
        The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing RPortPrototype when the short name already exists.
        """
        if not self.IsReferrableElementExists(short_name, RPortPrototype):
            prototype = RPortPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.ports.append(prototype)
        return cast(RPortPrototype, self.getReferrableElement(short_name, RPortPrototype))

    def createPRPortPrototype(self, short_name: str) -> PRPortPrototype:
        """
        The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        Returns the existing PRPortPrototype when the short name already exists.
        """
        if not self.IsReferrableElementExists(short_name, PRPortPrototype):
            prototype = PRPortPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.ports.append(prototype)
        return cast(PRPortPrototype, self.getReferrableElement(short_name, PRPortPrototype))

    def getPorts(self) -> List[PortPrototype]:
        """
        The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.
        """
        return self.ports

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        """
        Convenience getter for the PPortPrototype instances aggregated by this SwComponentType.
        """
        return list(sorted([c for c in self.ports if isinstance(c, PPortPrototype)], key=lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        """
        Convenience getter for the RPortPrototype instances aggregated by this SwComponentType.
        """
        return list(sorted([c for c in self.ports if isinstance(c, RPortPrototype)], key=lambda o: o.short_name))

    def getPRPortPrototypes(self) -> List[PRPortPrototype]:
        """
        Convenience getter for the PRPortPrototype instances aggregated by this SwComponentType.
        """
        return list(sorted([c for c in self.ports if isinstance(c, PRPortPrototype)], key=lambda o: o.short_name))

    def getPortPrototypes(self) -> List[PortPrototype]:
        """
        Convenience getter for all PortPrototype instances aggregated by this SwComponentType.
        """
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.ports), key=lambda o: o.short_name))

    def createPortGroup(self, short_name: str) -> PortGroup:
        """
        A port group being part of this component.
        Returns the existing PortGroup when the short name already exists.
        """
        if not self.IsReferrableElementExists(short_name, PortGroup):
            port_group = PortGroup(self, short_name)
            self.addReferrableElement(port_group)
            self.portGroups.append(port_group)
        return cast(PortGroup, self.getReferrableElement(short_name, PortGroup))

    def getPortGroups(self) -> List[PortGroup]:
        """
        A port group being part of this component.
        """
        return self.portGroups

    def addSwcMappingConstraintRef(self, value: Optional[RefType]) -> SwComponentType:
        """
        Reference to constraints that are valid for this SwComponentType.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.swcMappingConstraintsRefs.append(value)
        return self

    def getSwcMappingConstraintsRefs(self) -> List[RefType]:
        """
        Reference to constraints that are valid for this SwComponentType.
        """
        return self.swcMappingConstraintsRefs

    def getSwComponentDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        This adds a documentation to the SwComponentType.
        """
        return self.swComponentDocumentation

    def setSwComponentDocumentation(self, value: Optional[SwComponentDocumentation]) -> SwComponentType:
        """
        This adds a documentation to the SwComponentType.
        A None value is a no-op and does not overwrite an existing swComponentDocumentation.
        """
        if value is not None:
            self.swComponentDocumentation = value
        return self

    def addUnitGroupRef(self, value: Optional[RefType]) -> SwComponentType:
        """
        This allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.unitGroupRefs.append(value)
        return self

    def getUnitGroupRefs(self) -> List[RefType]:
        """
        This allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.
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

    def addClientServerAnnotation(self, value: Optional[ClientServerAnnotation]) -> PortPrototype:
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

    def setDelegatedPortAnnotation(self, value: Optional[DelegatedPortAnnotation]) -> PortPrototype:
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

    def addIoHwAbstractionServerAnnotation(self, value: Optional[IoHwAbstractionServerAnnotation]) -> PortPrototype:
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

    def addModePortAnnotation(self, value: Optional[ModePortAnnotation]) -> PortPrototype:
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

    def addNvDataPortAnnotation(self, value: Optional[NvDataPortAnnotation]) -> PortPrototype:
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

    def addParameterPortAnnotation(self, value: Optional[ParameterPortAnnotation]) -> PortPrototype:
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

    def addSenderReceiverAnnotation(self, value: Optional[SenderReceiverAnnotation]) -> PortPrototype:
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

    def addTriggerPortAnnotation(self, value: Optional[TriggerPortAnnotation]) -> PortPrototype:
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


class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a provided PortPrototype.
    """

    # AbstractProvidedPortPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.4, p.68 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] _validateProvidedComSpec     [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addProvidedComSpec           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedComSpecs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNonqueuedSenderComSpecs   [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        # Provided communication attributes per interface element (data element or operation). Stereotypes: atpSplitable Tags: atp.Splitkey=providedComSpec
        self.providedComSpecs: List[PPortComSpec] = []

    def _validateProvidedComSpec(self, com_spec: PPortComSpec) -> bool:
        if isinstance(com_spec, NonqueuedSenderComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None:
                dest = data_element_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for NonqueuedSenderComSpec.dataElementRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, QueuedSenderComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None:
                dest = data_element_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for QueuedSenderComSpec.dataElementRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, ServerComSpec):
            operation_ref = com_spec.getOperationRef()
            if operation_ref is not None:
                dest = operation_ref.getDest()
                if dest != "CLIENT-SERVER-OPERATION":
                    logger.warning("Invalid DEST for ServerComSpec.operationRef: expected CLIENT-SERVER-OPERATION, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, ModeSwitchSenderComSpec):
            mode_group_ref = com_spec.getModeGroupRef()
            if mode_group_ref is not None:
                dest = mode_group_ref.getDest()
                if dest != "MODE-DECLARATION-GROUP-PROTOTYPE":
                    logger.warning("Invalid DEST for ModeSwitchSenderComSpec.modeGroupRef: expected MODE-DECLARATION-GROUP-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, NvProvideComSpec):
            variable_ref = com_spec.getVariableRef()
            if variable_ref is not None:
                dest = variable_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for NvProvideComSpec.variableRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, ParameterProvideComSpec):
            parameter_ref = com_spec.getParameterRef()
            if parameter_ref is not None:
                dest = parameter_ref.getDest()
                if dest != "PARAMETER-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for ParameterProvideComSpec.parameterRef: expected PARAMETER-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        else:
            logger.warning("Unsupported PPortComSpec <%s>; skipping", type(com_spec).__name__)
            return False
        return True

    def addProvidedComSpec(self, com_spec: Optional[PPortComSpec]) -> AbstractProvidedPortPrototype:
        """
        Provided communication attributes per interface element (data element or operation). Stereotypes: atpSplitable Tags: atp.Splitkey=providedComSpec. A None value is a no-op and does not append anything.
        """
        if com_spec is not None and self._validateProvidedComSpec(com_spec):
            self.providedComSpecs.append(com_spec)
        return self

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        """
        Provided communication attributes per interface element (data element or operation). Stereotypes: atpSplitable Tags: atp.Splitkey=providedComSpec
        """
        return self.providedComSpecs

    def getNonqueuedSenderComSpecs(self) -> List[NonqueuedSenderComSpec]:
        return [c for c in self.providedComSpecs if isinstance(c, NonqueuedSenderComSpec)]


class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a required PortPrototype.
    """

    # AbstractRequiredPortPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.3, p.67 (R23-11; body renders above the caption line)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] _validateRequiredComSpec     [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRequiredComSpec           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredComSpecs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getClientComSpecs            [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNonqueuedReceiverComSpecs [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__(parent, short_name)

        # Required communication attributes, one for each interface element.
        self.requiredComSpecs: List[RPortComSpec] = []

    def _validateRequiredComSpec(self, com_spec: RPortComSpec) -> bool:
        if isinstance(com_spec, ClientComSpec):
            operation_ref = com_spec.getOperationRef()
            if operation_ref is not None:
                dest = operation_ref.getDest()
                if dest != "CLIENT-SERVER-OPERATION":
                    logger.warning("Invalid DEST for ClientComSpec.operationRef: expected CLIENT-SERVER-OPERATION, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, NonqueuedReceiverComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None:
                dest = data_element_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for NonqueuedReceiverComSpec.dataElementRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, QueuedReceiverComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None:
                dest = data_element_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for QueuedReceiverComSpec.dataElementRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            mode_group_ref = com_spec.getModeGroupRef()
            if mode_group_ref is not None:
                dest = mode_group_ref.getDest()
                if dest != "MODE-DECLARATION-GROUP-PROTOTYPE":
                    logger.warning("Invalid DEST for ModeSwitchReceiverComSpec.modeGroupRef: expected MODE-DECLARATION-GROUP-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, ParameterRequireComSpec):
            parameter_ref = com_spec.getParameterRef()
            if parameter_ref is not None:
                dest = parameter_ref.getDest()
                if dest != "PARAMETER-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for ParameterRequireComSpec.parameterRef: expected PARAMETER-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        elif isinstance(com_spec, NvRequireComSpec):
            variable_ref = com_spec.getVariableRef()
            if variable_ref is not None:
                dest = variable_ref.getDest()
                if dest != "VARIABLE-DATA-PROTOTYPE":
                    logger.warning("Invalid DEST for NvRequireComSpec.variableRef: expected VARIABLE-DATA-PROTOTYPE, got %s; skipping ComSpec", dest)
                    return False
        else:
            logger.warning("Unsupported RPortComSpec <%s>; skipping", type(com_spec).__name__)
            return False
        return True

    def addRequiredComSpec(self, com_spec: Optional[RPortComSpec]) -> AbstractRequiredPortPrototype:
        """
        Required communication attributes, one for each interface element. Stereotypes: atpSplitable Tags: atp.Splitkey=requiredComSpec. A None value is a no-op and does not append anything.
        """
        if com_spec is not None and self._validateRequiredComSpec(com_spec):
            self.requiredComSpecs.append(com_spec)
        return self

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        """
        Required communication attributes, one for each interface element. Stereotypes: atpSplitable Tags: atp.Splitkey=requiredComSpec
        """
        return self.requiredComSpecs

    def getClientComSpecs(self) -> List[ClientComSpec]:
        return [c for c in self.requiredComSpecs if isinstance(c, ClientComSpec)]

    def getNonqueuedReceiverComSpecs(self) -> List[NonqueuedReceiverComSpec]:
        return [c for c in self.requiredComSpecs if isinstance(c, NonqueuedReceiverComSpec)]


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

    def setProvidedInterfaceTRef(self, value: Optional[TRefType]) -> PPortPrototype:
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

    def setMayBeUnconnected(self, value: Optional[Boolean]) -> RPortPrototype:
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

    def setRequiredInterfaceTRef(self, value: Optional[TRefType]) -> RPortPrototype:
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
    # Spec verified: R23-11 (2026-09-26, user 9b re-confirmation)
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

    def setProvidedRequiredInterfaceTRef(self, value: Optional[TRefType]) -> PRPortPrototype:
        """
        This represents the PortInterface used to type the PRPortPrototype Stereotypes: isOfType
        If value is None, the existing value is not changed.
        """
        if value is not None:
            self.providedRequiredInterfaceTRef = value
        return self


class PortGroup(AtpStructureElement, VariationPointCapable):
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

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef) -> PortGroup:
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

    def addOuterPortRef(self, ref: RefType) -> PortGroup:
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
    An atomic software component is atomic in the sense that it cannot be further decomposed and distributed across multiple ECUs.
    """

    # AtomicSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.8, p.70
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInternalBehavior          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwcInternalBehavior    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSymbolProps               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSymbolProps            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtomicSwComponentType:
            raise TypeError("AtomicSwComponentType is an abstract class.")
        super().__init__(parent, short_name)

        # The SwcInternalBehaviors owned by an AtomicSwComponentType can be located in a different physical file. Therefore the aggregation is <<atpSplitable>>.
        self.internalBehavior: Optional[SwcInternalBehavior] = None

        # This represents the SymbolProps for the AtomicSwComponentType.
        self.symbolProps: Optional[SymbolProps] = None

    def getInternalBehavior(self) -> Optional[SwcInternalBehavior]:
        """
        The SwcInternalBehaviors owned by an AtomicSwComponentType can be located in a different physical file. Therefore the aggregation is <<atpSplitable>>.
        """
        return self.internalBehavior

    def createSwcInternalBehavior(self, short_name: str) -> SwcInternalBehavior:
        """
        The SwcInternalBehaviors owned by an AtomicSwComponentType can be located in a different physical file. Therefore the aggregation is <<atpSplitable>>.
        Returns the existing SwcInternalBehavior when the short name already exists.
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior

        if not self.IsReferrableElementExists(short_name, SwcInternalBehavior):
            behavior = SwcInternalBehavior(self, short_name)
            self.addReferrableElement(behavior)
            self.internalBehavior = behavior
        return cast(SwcInternalBehavior, self.getReferrableElement(short_name, SwcInternalBehavior))

    def getSymbolProps(self) -> Optional[SymbolProps]:
        """
        This represents the SymbolProps for the AtomicSwComponentType.
        """
        return self.symbolProps

    def createSymbolProps(self, short_name: str) -> SymbolProps:
        """
        This represents the SymbolProps for the AtomicSwComponentType.
        Returns the existing SymbolProps when the short name already exists.
        """
        if not self.IsReferrableElementExists(short_name, SymbolProps):
            symbol_props = SymbolProps(self, short_name)
            self.addReferrableElement(symbol_props)
            self.symbolProps = symbol_props
        return cast(SymbolProps, self.getReferrableElement(short_name, SymbolProps))


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """
    The ECUAbstraction is a special AtomicSwComponentType that resides between a software-component that wants to access ECU periphery and the Microcontroller Abstraction. The EcuAbstractionSwComponentType introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template. Tags: atp.recommendedPackage=SwComponentTypes
    """

    # EcuAbstractionSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.2, p.647
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addHardwareElementRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHardwareElementRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the EcuAbstractionComponentType to the description of the used HwElements.
        self.hardwareElementRefs: List[RefType] = []

    def addHardwareElementRef(self, value: Optional[RefType]) -> EcuAbstractionSwComponentType:
        """
        Reference from the EcuAbstractionComponentType to the description of the used HwElements.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self

    def getHardwareElementRefs(self) -> List[RefType]:
        """
        Reference from the EcuAbstractionComponentType to the description of the used HwElements.
        """
        return self.hardwareElementRefs


class ApplicationSwComponentType(AtomicSwComponentType):
    """
    The ApplicationSwComponentType is used to represent the application software.
    """

    # ApplicationSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.9, p.71
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """
    The ComplexDeviceDriverSwComponentType is a special AtomicSwComponentType that has direct access to hardware on an ECU and which is therefore linked to a specific ECU or specific hardware. The ComplexDeviceDriverSwComponentType introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template. Tags: atp.recommendedPackage=SwComponentTypes
    """

    # ComplexDeviceDriverSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.3, p.648
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addHardwareElementRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHardwareElementRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.
        self.hardwareElementRefs: List[RefType] = []

    def addHardwareElementRef(self, value: Optional[RefType]) -> ComplexDeviceDriverSwComponentType:
        """
        Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.hardwareElementRefs.append(value)
        return self

    def getHardwareElementRefs(self) -> List[RefType]:
        """
        Reference from the ComplexDeviceDriverSwComponentType to the description of the used HwElements.
        """
        return self.hardwareElementRefs


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
        if not self.IsReferrableElementExists(short_name, BulkNvDataDescriptor):
            descriptor = BulkNvDataDescriptor(self, short_name)
            self.addReferrableElement(descriptor)
            self.bulkNvDataDescriptors.append(descriptor)
        return cast(BulkNvDataDescriptor, self.getReferrableElement(short_name, BulkNvDataDescriptor))

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
        if not self.IsReferrableElementExists(short_name, NvBlockDescriptor):
            descriptor = NvBlockDescriptor(self, short_name)
            self.addReferrableElement(descriptor)
            self.nvBlockDescriptors.append(descriptor)
        return cast(NvBlockDescriptor, self.getReferrableElement(short_name, NvBlockDescriptor))


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """
    The SensorActuatorSwComponentType introduces the possibility to link from the software representation of a sensor/actuator to its hardware description provided by the ECU Resource Template. Tags: atp.recommendedPackage=SwComponentTypes
    """

    # SensorActuatorSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 10.1, p.646
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSensorActuatorRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSensorActuatorRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.
        self.sensorActuatorRef: Optional[RefType] = None

    def getSensorActuatorRef(self) -> Optional[RefType]:
        """
        Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.
        """
        return self.sensorActuatorRef

    def setSensorActuatorRef(self, value: Optional[RefType]) -> SensorActuatorSwComponentType:
        """
        Reference from the Sensor Actuator Software Component Type to the description of the actual hardware.

        A None value is a no-op and does not overwrite an existing sensorActuatorRef.
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
    ServiceSwComponentType is used for configuring services for a given ECU. Instances of this class are only to be created in ECU Configuration phase for the specific purpose of the service configuration. Tags: atp.recommendedPackage=SwComponentTypes
    """

    # ServiceSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 11.2, p.659
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ParameterSwComponentType(SwComponentType):
    """
    The ParameterSwComponentType defines parameters and characteristic values accessible via provided Ports. The provided values are the same for all connected SwComponentPrototypes
    """

    # ParameterSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 2.1, p.41
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addConstantMappingRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConstantMappingRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataTypeMappingRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataTypeMappingRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInstantiationDataDefProps   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInstantiationDataDefProps   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the ConstantSpecificationMapping to be applied for the particular ParameterSwComponentType
        self.constantMappingRefs: List[RefType] = []

        # Reference to the DataTypeMapping to be applied for the particular ParameterSwComponentType
        self.dataTypeMappingRefs: List[RefType] = []

        # The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of PortPrototypes
        self.instantiationDataDefProps: List[InstantiationDataDefProps] = []

    def addConstantMappingRef(self, value: Optional[RefType]) -> ParameterSwComponentType:
        """
        Reference to the ConstantSpecificationMapping to be applied for the particular ParameterSwComponentType
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.constantMappingRefs.append(value)
        return self

    def getConstantMappingRefs(self) -> List[RefType]:
        """
        Reference to the ConstantSpecificationMapping to be applied for the particular ParameterSwComponentType
        """
        return self.constantMappingRefs

    def addDataTypeMappingRef(self, value: Optional[RefType]) -> ParameterSwComponentType:
        """
        Reference to the DataTypeMapping to be applied for the particular ParameterSwComponentType
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.dataTypeMappingRefs.append(value)
        return self

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """
        Reference to the DataTypeMapping to be applied for the particular ParameterSwComponentType
        """
        return self.dataTypeMappingRefs

    def addInstantiationDataDefProps(self, value: Optional[InstantiationDataDefProps]) -> ParameterSwComponentType:
        """
        The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of PortPrototypes
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.instantiationDataDefProps.append(value)
        return self

    def getInstantiationDataDefProps(self) -> List[InstantiationDataDefProps]:
        """
        The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of PortPrototypes
        """
        return self.instantiationDataDefProps


from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation  # noqa: E402

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps  # noqa: E402
