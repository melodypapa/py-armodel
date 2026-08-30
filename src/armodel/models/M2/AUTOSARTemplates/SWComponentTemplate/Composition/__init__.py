from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement, AtpPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    InstanceEventInCompositionInstanceRef,
    PPortInCompositionInstanceRef,
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import RPortInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable as Identifiable,
)


class SwComponentPrototype(AtpPrototype):
    """
    Role of a software component within a composition.
    """

    # SwComponentPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.11, p.77
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTypeTRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTypeTRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Type of the instance. Stereotypes: isOfType
        self.typeTRef: Optional[RefType] = None

    def getTypeTRef(self) -> Optional[RefType]:
        """
        Gets the Type of the instance. Stereotypes: isOfType.

        Returns:
            RefType referencing the SwComponentType, or None if not set
        """
        return self.typeTRef

    def setTypeTRef(self, value: Optional[RefType]) -> "SwComponentPrototype":
        """
        Sets the Type of the instance. Stereotypes: isOfType.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The SwComponentType reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.typeTRef = value
        return self


class SwConnector(AtpStructureElement, ABC):
    """
    The base class for connectors between ports. Connectors have to be identifiable to allow references from the system constraint template.
    """

    # SwConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.12, p.80
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMappingRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMappingRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is SwConnector:
            raise TypeError("SwConnector is an abstract class.")
        super().__init__(parent, short_name)

        # Reference to a PortInterfaceMapping specifying the mapping of unequal named PortInterface elements of the two different PortInterfaces typing the two PortPrototypes which are referenced by the ConnectorPrototype.
        self.mappingRef: Optional[RefType] = None

    def getMappingRef(self) -> Optional[RefType]:
        """
        Gets the reference to a PortInterfaceMapping specifying the mapping of unequal named PortInterface elements of the two different PortInterfaces typing the two PortPrototypes which are referenced by the ConnectorPrototype.

        Returns:
            RefType referencing the PortInterfaceMapping, or None if not set
        """
        return self.mappingRef

    def setMappingRef(self, value: Optional[RefType]) -> "SwConnector":
        """
        Sets the reference to a PortInterfaceMapping specifying the mapping of unequal named PortInterface elements of the two different PortInterfaces typing the two PortPrototypes which are referenced by the ConnectorPrototype.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The PortInterfaceMapping reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mappingRef = value
        return self


class AssemblySwConnector(SwConnector):
    # AssemblySwConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getProviderIRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setProviderIRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getRequesterIRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setRequesterIRef             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providerIRef: PPortInCompositionInstanceRef = None
        self.requesterIRef: RPortInCompositionInstanceRef = None

    def getProviderIRef(self) -> PPortInCompositionInstanceRef:
        return self.providerIRef

    def setProviderIRef(self, value: PPortInCompositionInstanceRef):
        self.providerIRef = value
        return self

    def getRequesterIRef(self) -> RPortInCompositionInstanceRef:
        return self.requesterIRef

    def setRequesterIRef(self, value: RPortInCompositionInstanceRef):
        self.requesterIRef = value
        return self


class DelegationSwConnector(SwConnector):
    # DelegationSwConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInnerPortIRref            [x] impl  [ ] docstring  [ ] test
    # [ ] setInnerPortIRref            [x] impl  [ ] docstring  [ ] test
    # [ ] getOuterPortRef              [x] impl  [ ] docstring  [ ] test
    # [ ] setOuterPortRef              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.innerPortIRref: PortInCompositionTypeInstanceRef = None
        self.outerPortRef: RefType = None

    def getInnerPortIRref(self) -> PortInCompositionTypeInstanceRef:
        return self.innerPortIRref

    def setInnerPortIRref(self, value: PortInCompositionTypeInstanceRef):
        self.innerPortIRref = value
        return self

    def getOuterPortRef(self) -> RefType:
        return self.outerPortRef

    def setOuterPortRef(self, value: RefType):
        self.outerPortRef = value
        return self


class PassThroughSwConnector(SwConnector):
    """
    This kind of SwConnector can be used inside a CompositionSwComponentType to connect two delegation PortPrototypes.
    """

    # PassThroughSwConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.15, p.83
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getProvidedOuterPortRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProvidedOuterPortRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiredOuterPortRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequiredOuterPortRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the provided outer delegation Port Prototype of the PassThroughSwConnector.
        self.providedOuterPortRef: Optional[RefType] = None

        # This represents the required outer delegation Port Prototype of the PassThroughSwConnector.
        self.requiredOuterPortRef: Optional[RefType] = None

    def getProvidedOuterPortRef(self) -> Optional[RefType]:
        """
        Gets the provided outer delegation Port Prototype of the PassThroughSwConnector.

        Returns:
            RefType referencing the provided outer delegation Port Prototype, or None if not set
        """
        return self.providedOuterPortRef

    def setProvidedOuterPortRef(self, value: Optional[RefType]) -> "PassThroughSwConnector":
        """
        Sets the provided outer delegation Port Prototype of the PassThroughSwConnector.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The provided outer delegation Port Prototype reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.providedOuterPortRef = value
        return self

    def getRequiredOuterPortRef(self) -> Optional[RefType]:
        """
        Gets the required outer delegation Port Prototype of the PassThroughSwConnector.

        Returns:
            RefType referencing the required outer delegation Port Prototype, or None if not set
        """
        return self.requiredOuterPortRef

    def setRequiredOuterPortRef(self, value: Optional[RefType]) -> "PassThroughSwConnector":
        """
        Sets the required outer delegation Port Prototype of the PassThroughSwConnector.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The required outer delegation Port Prototype reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.requiredOuterPortRef = value
        return self


class InstantiationRTEEventProps(ARObject, ABC):
    """
    This meta-class represents the ability to refine the properties of RTEEvents for particular instances of a software component.
    """

    # InstantiationRTEEventProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.17, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRefinedEventIRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRefinedEventIRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is InstantiationRTEEventProps:
            raise TypeError("InstantiationRTEEventProps is an abstract class.")

        super().__init__()

        # This instance ref denotes the Timing Event for which the period shall be refined on an instance level. InstanceRef implemented by: InstanceEventInCompositionInstanceRef
        self.refinedEventIRef: Optional[InstanceEventInCompositionInstanceRef] = None

        # The main purpose of the shortLabel is to contribute to the splitkey of aggregations that are <<atpSplitable>>.
        self.shortLabel: Optional[Identifier] = None

    def getRefinedEventIRef(self) -> Optional[InstanceEventInCompositionInstanceRef]:
        """
        Gets the instance reference denoting the Timing Event for which the period shall be refined on an instance level.

        Returns:
            InstanceEventInCompositionInstanceRef, or None if not set
        """
        return self.refinedEventIRef

    def setRefinedEventIRef(self, value: Optional[InstanceEventInCompositionInstanceRef]) -> "InstantiationRTEEventProps":
        """
        Sets the instance reference denoting the Timing Event for which the period shall be refined on an instance level.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The InstanceEventInCompositionInstanceRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.refinedEventIRef = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """
        Gets the short label that contributes to the splitkey of aggregations that are <<atpSplitable>>.

        Returns:
            Identifier representing the short label, or None if not set
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "InstantiationRTEEventProps":
        """
        Sets the short label that contributes to the splitkey of aggregations that are <<atpSplitable>>.
        A None value is a no-op and does not overwrite an existing short label.

        Args:
            value: The short label identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortLabel = value
        return self


class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """
    This meta-class represents the ability to refine a timing event for particular instances of a software component. This approach supports an instance specific timing.
    """

    # InstantiationTimingEventProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.16, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPeriod                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPeriod                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute represents the value of the refined activation period.
        self.period: Optional[TimeValue] = None

    def getPeriod(self) -> Optional[TimeValue]:
        """
        Gets the value of the refined activation period.

        Returns:
            TimeValue representing the period, or None if not set
        """
        return self.period

    def setPeriod(self, value: Optional[TimeValue]) -> "InstantiationTimingEventProps":
        """
        Sets the value of the refined activation period.
        A None value is a no-op and does not overwrite an existing period.

        Args:
            value: The period TimeValue to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.period = value
        return self


class CompositionSwComponentType(SwComponentType):
    """
    A CompositionSwComponentType aggregates SwComponentPrototypes (that in turn are typed by SwComponentTypes) as well as SwConnectors for primarily connecting SwComponentPrototypes among each others and towards the surface of the CompositionSwComponentType. By this means, a hierarchical structures of software-components can be created.
    """

    # CompositionSwComponentType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.10, p.75
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createSwComponentPrototype      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getComponents                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createAssemblySwConnector       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createDelegationSwConnector     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createPassThroughSwConnector    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwConnectors                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getAssemblySwConnectors         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDelegationSwConnectors       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPassThroughSwConnectors      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] removeAllAssemblySwConnector    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] removeAllDelegationSwConnector  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] removeAllPassThroughSwConnector [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addConstantValueMappingRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConstantValueMappingRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDataTypeMappingRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypeMappingRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addInstantiationRTEEventProps   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInstantiationRTEEventProps   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPhysicalDimensionMappingRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPhysicalDimensionMappingRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The instantiated components that are part of this composition. The aggregation of SwComponentPrototype is subject to variability with the purpose to support the conditional existence of a SwComponentPrototype. Please be aware: if the conditional existence of SwComponentPrototypes is resolved post-build, the deselected SwComponentPrototypes are still contained in the ECUs build but the instances are inactive in that they are not scheduled by the RTE. The aggregation is marked as atpSplitable in order to allow the addition of service components to the ECU extract during the ECU integration. The use case for having 0 components owned by the CompositionSwComponentType could be to deliver an empty CompositionSwComponentType to e.g. a supplier for filling the internal structure.
        self.components: List[SwComponentPrototype] = []

        # SwConnectors have the principal ability to establish a connection among PortPrototypes. They can have many roles in the context of a CompositionSwComponentType. Details are refined by subclasses. The aggregation of SwConnectors is subject to variability with the purpose to support variant data flow. The aggregation is marked as atpSplitable in order to allow the extension of the ECU extract with AssemblySwConnectors between ApplicationSwComponentTypes and ServiceSwComponentTypes during the ECU integration.
        self.connectors: List[SwConnector] = []

        # Reference to the ConstantSpecificationMapping to be applied for initValues of PPortComSpecs and RPortComSpec.
        self.constantValueMappingRefs: List[RefType] = []

        # Reference to the DataTypeMappingSet to be applied for the used ApplicationDataTypes in PortInterfaces. Background: when developing subsystems it may happen that ApplicationDataTypes are used on the surface of CompositionSwComponentTypes. In this case it would be reasonable to be able to also provide the intended mapping to the ImplementationDataTypes. However, this mapping shall be informal and not technically binding for the implementors mainly because the RTE generator is not concerned about the CompositionSwComponentTypes. Rationale: if the mapping of ApplicationDataTypes on the delegated and inner PortPrototype matches then the mapping to ImplementationDataTypes is not impacting compatibility.
        self.dataTypeMappingRefs: List[RefType] = []

        # This allows to define instantiation specific properties for RTE Events, in particular for instance specific scheduling.
        self.instantiationRTEEventProps: List[InstantiationRTEEventProps] = []

        # This reference identifies the PhysicalDimensionMappingSet that is applicable in the context of the enclosing CompositionSwComponentType. The PhysicalDimensionMappings contained in the PhysicalDimensionMappingSet shall be taken into account for the assessment of the compatibility of PhysicalDimensions in the context of creation of a PortInterfaceMapping in the scope of the CompositionSwComponentType.
        self.physicalDimensionMappingRef: Optional[RefType] = None

    def createSwComponentPrototype(self, short_name: str) -> SwComponentPrototype:
        """
        Creates a SwComponentPrototype that is part of this composition.
        Returns the existing prototype when the short name already exists.

        Args:
            short_name: The short name of the SwComponentPrototype

        Returns:
            The created or existing SwComponentPrototype
        """
        if not self.IsElementExists(short_name, SwComponentPrototype):
            prototype = SwComponentPrototype(self, short_name)
            self.addElement(prototype)
            self.components.append(prototype)
        return self.getElement(short_name, SwComponentPrototype)

    def getComponents(self) -> List[SwComponentPrototype]:
        """
        Gets the instantiated components that are part of this composition.

        Returns:
            List of SwComponentPrototype instances
        """
        return self.components

    def createAssemblySwConnector(self, short_name: str) -> AssemblySwConnector:
        """
        Creates an AssemblySwConnector that connects PortPrototypes of SwComponentPrototypes that are part of the CompositionSwComponentType.
        Returns the existing connector when the short name already exists.

        Args:
            short_name: The short name of the AssemblySwConnector

        Returns:
            The created or existing AssemblySwConnector
        """
        if not self.IsElementExists(short_name, AssemblySwConnector):
            connector = AssemblySwConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, AssemblySwConnector)

    def createDelegationSwConnector(self, short_name: str) -> DelegationSwConnector:
        """
        Creates a DelegationSwConnector that connects from inner PortPrototypes to delegated outer PortPrototypes.
        Returns the existing connector when the short name already exists.

        Args:
            short_name: The short name of the DelegationSwConnector

        Returns:
            The created or existing DelegationSwConnector
        """
        if not self.IsElementExists(short_name, DelegationSwConnector):
            connector = DelegationSwConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, DelegationSwConnector)

    def createPassThroughSwConnector(self, short_name: str) -> PassThroughSwConnector:
        """
        Creates a PassThroughSwConnector.
        Returns the existing connector when the short name already exists.

        Args:
            short_name: The short name of the PassThroughSwConnector

        Returns:
            The created or existing PassThroughSwConnector
        """
        if not self.IsElementExists(short_name, PassThroughSwConnector):
            connector = PassThroughSwConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, PassThroughSwConnector)

    def getSwConnectors(self) -> List[SwConnector]:
        """
        Gets the SwConnectors aggregated by this CompositionSwComponentType.

        Returns:
            List of SwConnector instances
        """
        return self.connectors

    def getAssemblySwConnectors(self) -> List[AssemblySwConnector]:
        """
        Gets the AssemblySwConnectors aggregated by this CompositionSwComponentType.

        Returns:
            List of AssemblySwConnector instances
        """
        return list(sorted(filter(lambda e: isinstance(e, AssemblySwConnector), self.connectors), key=lambda c: c.short_name))

    def getDelegationSwConnectors(self) -> List[DelegationSwConnector]:
        """
        Gets the DelegationSwConnectors aggregated by this CompositionSwComponentType.

        Returns:
            List of DelegationSwConnector instances
        """
        return list(sorted(filter(lambda e: isinstance(e, DelegationSwConnector), self.connectors), key=lambda c: c.short_name))

    def getPassThroughSwConnectors(self) -> List[PassThroughSwConnector]:
        """
        Gets the PassThroughSwConnectors aggregated by this CompositionSwComponentType.

        Returns:
            List of PassThroughSwConnector instances
        """
        return list(sorted(filter(lambda e: isinstance(e, PassThroughSwConnector), self.connectors), key=lambda c: c.short_name))

    def removeAllAssemblySwConnector(self):
        """
        Removes all AssemblySwConnectors aggregated by this CompositionSwComponentType.
        """
        for sw_connector in self.getAssemblySwConnectors():
            self.elements.remove(sw_connector)
            self.connectors.remove(sw_connector)

    def removeAllDelegationSwConnector(self):
        """
        Removes all DelegationSwConnectors aggregated by this CompositionSwComponentType.
        """
        for sw_connector in self.getDelegationSwConnectors():
            self.elements.remove(sw_connector)
            self.connectors.remove(sw_connector)

    def removeAllPassThroughSwConnector(self):
        """
        Removes all PassThroughSwConnectors aggregated by this CompositionSwComponentType.
        """
        for sw_connector in self.getPassThroughSwConnectors():
            self.elements.remove(sw_connector)
            self.connectors.remove(sw_connector)

    def addConstantValueMappingRef(self, ref: Optional[RefType]) -> "CompositionSwComponentType":
        """
        Adds a reference to the ConstantSpecificationMapping to be applied for initValues of PPortComSpecs and RPortComSpec.
        A None value is a no-op and does not append anything.

        Args:
            ref: The ConstantSpecificationMappingSet reference to add

        Returns:
            self for method chaining
        """
        if ref is not None:
            self.constantValueMappingRefs.append(ref)
        return self

    def getConstantValueMappingRefs(self) -> List[RefType]:
        """
        Gets the references to the ConstantSpecificationMappings to be applied for initValues of PPortComSpecs and RPortComSpec.

        Returns:
            List of RefType instances
        """
        return self.constantValueMappingRefs

    def addDataTypeMappingRef(self, ref: Optional[RefType]) -> "CompositionSwComponentType":
        """
        Adds a reference to the DataTypeMappingSet to be applied for the used ApplicationDataTypes in PortInterfaces.
        A None value is a no-op and does not append anything.

        Args:
            ref: The DataTypeMappingSet reference to add

        Returns:
            self for method chaining
        """
        if ref is not None:
            self.dataTypeMappingRefs.append(ref)
        return self

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """
        Gets the references to the DataTypeMappingSets to be applied for the used ApplicationDataTypes in PortInterfaces.

        Returns:
            List of RefType instances
        """
        return self.dataTypeMappingRefs

    def addInstantiationRTEEventProps(self, value: Optional[InstantiationRTEEventProps]) -> "CompositionSwComponentType":
        """
        Adds instantiation specific properties for RTE Events, in particular for instance specific scheduling.
        A None value is a no-op and does not append anything.

        Args:
            value: The InstantiationRTEEventProps to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.instantiationRTEEventProps.append(value)
        return self

    def getInstantiationRTEEventProps(self) -> List[InstantiationRTEEventProps]:
        """
        Gets the instantiation specific properties for RTE Events.

        Returns:
            List of InstantiationRTEEventProps instances
        """
        return self.instantiationRTEEventProps

    def setPhysicalDimensionMappingRef(self, ref: Optional[RefType]) -> "CompositionSwComponentType":
        """
        Sets the reference to the PhysicalDimensionMappingSet that is applicable in the context of the enclosing CompositionSwComponentType.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            ref: The PhysicalDimensionMappingSet reference to set

        Returns:
            self for method chaining
        """
        if ref is not None:
            self.physicalDimensionMappingRef = ref
        return self

    def getPhysicalDimensionMappingRef(self) -> Optional[RefType]:
        """
        Gets the reference to the PhysicalDimensionMappingSet that is applicable in the context of the enclosing CompositionSwComponentType.

        Returns:
            RefType referencing the PhysicalDimensionMappingSet, or None if not set
        """
        return self.physicalDimensionMappingRef

    def removeElement(self, short_name: str, type=None):
        """
        Removes an element from this composition.
        The element is removed both from the elements registry and from the dedicated
        component and connector lists.

        Args:
            short_name: The short name of the element to remove
            type: The type of element to remove (optional)
        """
        item = self.getElement(short_name, type)
        super().removeElement(short_name, type)
        if item is not None:
            if isinstance(item, SwComponentPrototype) and item in self.components:
                self.components.remove(item)
            if isinstance(item, SwConnector) and item in self.connectors:
                self.connectors.remove(item)
