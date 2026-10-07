# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class MappingScopeEnum(AREnum):
    """
    Defines the scope for the mapping constraints.
    """

    # MappingScopeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.10, p.204
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ComponentClustering.mappingScope / ComponentSeparation.mappingScope
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The mapping constraint applies to different Cores. Tags: atp.EnumerationLiteralIndex=0
    MAPPING_SCOPE_CORE = "MAPPING-SCOPE-CORE"

    # The mapping constraint applies to different Ecus. Tags: atp.EnumerationLiteralIndex=1
    MAPPING_SCOPE_ECU = "MAPPING-SCOPE-ECU"

    # The mapping constraint applies to different Partitions. Tags: atp.EnumerationLiteralIndex=2
    MAPPING_SCOPE_PARTITION = "MAPPING-SCOPE-PARTITION"

    def __init__(self):
        super().__init__(
            [
                MappingScopeEnum.MAPPING_SCOPE_CORE,
                MappingScopeEnum.MAPPING_SCOPE_ECU,
                MappingScopeEnum.MAPPING_SCOPE_PARTITION,
            ]
        )


class SwcToImplMapping(Identifiable, VariationPointCapable):
    """
    Map instances of an AtomicSwComponentType to a specific Implementation.
    """

    # SwcToImplMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.3, p.199
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addComponentIRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComponentIRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getComponentImplementationRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComponentImplementationRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to the software component instances that are being mapped to the specified Implementation. The targeted SwComponentPrototype needs be of the Atomic SwComponentType being implemented by the referenced Implementation. InstanceRef implemented by: ComponentInSystemInstanceRef
        self.componentIRefs: List[ComponentInSystemInstanceRef] = []

        # Reference to a specific Implementation description. Implementation to be used by the specified SW component instance. This allows to achieve more precise estimates for the resource consumption that results from mapping the instance of an atomic SW component onto an ECU.
        self.componentImplementationRef: Optional[RefType] = None

    def addComponentIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "SwcToImplMapping":
        """
        Reference to the software component instances that are being mapped to the specified Implementation. The targeted SwComponentPrototype needs be of the Atomic SwComponentType being implemented by the referenced Implementation. InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not add to componentIRefs.
        """
        if value is not None:
            self.componentIRefs.append(value)
        return self

    def getComponentIRefs(self) -> List[ComponentInSystemInstanceRef]:
        """
        Reference to the software component instances that are being mapped to the specified Implementation. The targeted SwComponentPrototype needs be of the Atomic SwComponentType being implemented by the referenced Implementation. InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.componentIRefs

    def getComponentImplementationRef(self) -> Optional[RefType]:
        """
        Reference to a specific Implementation description. Implementation to be used by the specified SW component instance. This allows to achieve more precise estimates for the resource consumption that results from mapping the instance of an atomic SW component onto an ECU.
        """
        return self.componentImplementationRef

    def setComponentImplementationRef(self, value: Optional[RefType]) -> "SwcToImplMapping":
        """
        Reference to a specific Implementation description. Implementation to be used by the specified SW component instance. This allows to achieve more precise estimates for the resource consumption that results from mapping the instance of an atomic SW component onto an ECU.

        A None value is a no-op and does not overwrite an existing componentImplementationRef.
        """
        if value is not None:
            self.componentImplementationRef = value
        return self


class SwcToApplicationPartitionMapping(Identifiable, VariationPointCapable):
    """
    Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined.
    """

    # SwcToApplicationPartitionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.4, p.200
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationPartitionRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationPartitionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwComponentPrototypeIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwComponentPrototypeIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to an ApplicationPartition to which a SwComponentPrototype is mapped.
        self.applicationPartitionRef: Optional[RefType] = None

        # References to the software component instances that are mapped to the referenced ApplicationPartition. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ApplicationPartition. If there is additionally a mapping of some SwComponentPrototype INSIDE the Composition to another ApplicationPartition the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef
        self.swComponentPrototypeIRef: Optional[ComponentInSystemInstanceRef] = None

    def getApplicationPartitionRef(self) -> Optional[RefType]:
        """
        Reference to an ApplicationPartition to which a SwComponentPrototype is mapped.
        """
        return self.applicationPartitionRef

    def setApplicationPartitionRef(self, value: Optional[RefType]) -> "SwcToApplicationPartitionMapping":
        """
        Reference to an ApplicationPartition to which a SwComponentPrototype is mapped.

        A None value is a no-op and does not overwrite an existing applicationPartitionRef.
        """
        if value is not None:
            self.applicationPartitionRef = value
        return self

    def getSwComponentPrototypeIRef(self) -> Optional[ComponentInSystemInstanceRef]:
        """
        References to the software component instances that are mapped to the referenced ApplicationPartition. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ApplicationPartition. If there is additionally a mapping of some SwComponentPrototype INSIDE the Composition to another ApplicationPartition the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.swComponentPrototypeIRef

    def setSwComponentPrototypeIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "SwcToApplicationPartitionMapping":
        """
        References to the software component instances that are mapped to the referenced ApplicationPartition. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ApplicationPartition. If there is additionally a mapping of some SwComponentPrototype INSIDE the Composition to another ApplicationPartition the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not overwrite an existing swComponentPrototypeIRef.
        """
        if value is not None:
            self.swComponentPrototypeIRef = value
        return self


class ApplicationPartition(ARElement):
    """
    ApplicationPartition to which SwComponentPrototypes are mapped at a point in time when the corresponding EcuInstance is not yet known or defined. In a later methodology step the Application Partition can be assigned to an EcuPartition. Tags: atp.recommendedPackage=ApplicationPartitions
    """

    # ApplicationPartition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.5, p.201
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SwcToEcuMapping(Identifiable, VariationPointCapable):
    """
    This meta-class is used: • to map SwComponentPrototypes to a specific ECU Instance unit, • optionally to map SwComponentPrototypes to a HwElement with category ProcessingUnit, • optionally to map SwComponentPrototypes typed by SensorActuatorSwComponentType to a Hw Element with category SensorActuator. For each combination of ECUInstance and the optional ProcessingUnit and the optional SensorActuator only one SwcToEcuMapping shall be used.

    [constr_3263] Restriction of usage of SwcToEcuMapping in a System: For all SwcToEcuMappings in a System the following restriction applies: No two SwcToEcuMappings shall have the exact same reference to SwComponentPrototype, EcuInstance, processingUnit, controlledHwElement.

    [constr_3021] Mapping of SensorActuatorSwComponents to SensorActuator HwElements: Only SwComponentPrototypes that are typed by SensorActuatorSwComponentType shall be mapped to a HwElement with category SensorActuator via the controlledHwElement relation.

    [constr_3249] Category of HwElement for SwcToEcuMapping: The HwElement which is referenced from SwcToEcuMapping in the role processingUnit shall be of category "ProcessingUnit".
    """

    # SwcToEcuMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.2, p.197
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addComponentIRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComponentIRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getControlledHwElementRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setControlledHwElementRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuInstanceRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProcessingUnitRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProcessingUnitRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # References to the software component instances that are mapped to the referenced ECUInstance. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ECU. If there is aditionally a mapping of some SwComponent Prototype INSIDE the Composition to another ECU Instance the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef
        self.componentIRefs: List[ComponentInSystemInstanceRef] = []

        # Optional mapping of SwComponentPrototypes that are typed by SensorActuatorSwComponentType to a Hw Element with category SensorActuator.
        self.controlledHwElementRef: Optional[RefType] = None

        # Reference to a specific ECU Instance description.
        self.ecuInstanceRef: Optional[RefType] = None

        # Optional mapping of software components to individual microcontroller cores residing in one ECU. A microcontroller core is described in the ECU Resource Template by the HwElement of HwCategory Processing Unit.
        self.processingUnitRef: Optional[RefType] = None

    def addComponentIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "SwcToEcuMapping":
        """
        References to the software component instances that are mapped to the referenced ECUInstance. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ECU. If there is aditionally a mapping of some SwComponent Prototype INSIDE the Composition to another ECU Instance the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not add to componentIRefs.
        """
        if value is not None:
            self.componentIRefs.append(value)
        return self

    def getComponentIRefs(self) -> List[ComponentInSystemInstanceRef]:
        """
        References to the software component instances that are mapped to the referenced ECUInstance. If the component prototype referenced is a composition, this indicates that all atomic software components within the composition are mapped to the ECU. If there is aditionally a mapping of some SwComponent Prototype INSIDE the Composition to another ECU Instance the inner mapping overrides the outer mapping. InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.componentIRefs

    def getControlledHwElementRef(self) -> Optional[RefType]:
        """
        Optional mapping of SwComponentPrototypes that are typed by SensorActuatorSwComponentType to a Hw Element with category SensorActuator.
        """
        return self.controlledHwElementRef

    def setControlledHwElementRef(self, value: Optional[RefType]) -> "SwcToEcuMapping":
        """
        Optional mapping of SwComponentPrototypes that are typed by SensorActuatorSwComponentType to a Hw Element with category SensorActuator.

        A None value is a no-op and does not overwrite an existing controlledHwElementRef.
        """
        if value is not None:
            self.controlledHwElementRef = value
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Reference to a specific ECU Instance description.
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> "SwcToEcuMapping":
        """
        Reference to a specific ECU Instance description.

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getProcessingUnitRef(self) -> Optional[RefType]:
        """
        Optional mapping of software components to individual microcontroller cores residing in one ECU. A microcontroller core is described in the ECU Resource Template by the HwElement of HwCategory Processing Unit.
        """
        return self.processingUnitRef

    def setProcessingUnitRef(self, value: Optional[RefType]) -> "SwcToEcuMapping":
        """
        Optional mapping of software components to individual microcontroller cores residing in one ECU. A microcontroller core is described in the ECU Resource Template by the HwElement of HwCategory Processing Unit.

        A None value is a no-op and does not overwrite an existing processingUnitRef.
        """
        if value is not None:
            self.processingUnitRef = value
        return self


class ApplicationPartitionToEcuPartitionMapping(Identifiable, VariationPointCapable):
    """
    Maps ApplicationPartitions to EcuPartitions. With this mapping an OEM has the option to predefine an allocation of Software Components to EcuPartitions in the System Design phase. The final and complete assignment is described in the OS Configuration.
    """

    # ApplicationPartitionToEcuPartitionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.6, p.201
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addApplicationPartitionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationPartitionRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEcuPartitionRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuPartitionRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Reference to ApplicationPartitions that are mapped to an EcuPartition.
        self.applicationPartitionRefs: List[RefType] = []

        # Reference to EcuPartition to which the Application Partitions are assigned.
        self.ecuPartitionRef: Optional[RefType] = None

    def addApplicationPartitionRef(self, value: Optional[RefType]) -> "ApplicationPartitionToEcuPartitionMapping":
        """
        Reference to ApplicationPartitions that are mapped to an EcuPartition.

        A None value is a no-op and does not add to applicationPartitionRefs.
        """
        if value is not None:
            self.applicationPartitionRefs.append(value)
        return self

    def getApplicationPartitionRefs(self) -> List[RefType]:
        """
        Reference to ApplicationPartitions that are mapped to an EcuPartition.
        """
        return self.applicationPartitionRefs

    def getEcuPartitionRef(self) -> Optional[RefType]:
        """
        Reference to EcuPartition to which the Application Partitions are assigned.
        """
        return self.ecuPartitionRef

    def setEcuPartitionRef(self, value: Optional[RefType]) -> "ApplicationPartitionToEcuPartitionMapping":
        """
        Reference to EcuPartition to which the Application Partitions are assigned.

        A None value is a no-op and does not overwrite an existing ecuPartitionRef.
        """
        if value is not None:
            self.ecuPartitionRef = value
        return self


class EcuPartition(Identifiable):
    """
    Partitions are used as error containment regions. They permit the grouping of SWCs and resources and allow to describe recovery policies individually for each partition. Partitions can be terminated or restarted during run-time as a result of a detected error.
    """

    # EcuPartition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.7, p.201 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExecInUserMode  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExecInUserMode  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.
        self.execInUserMode: Optional[Boolean] = None

    def getExecInUserMode(self) -> Optional[Boolean]:
        """
        A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.
        """
        return self.execInUserMode

    def setExecInUserMode(self, value: Optional[Boolean]) -> "EcuPartition":
        """
        A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.

        A None value is a no-op and does not overwrite an existing execInUserMode.
        """
        if value is not None:
            self.execInUserMode = value
        return self


class EcuResourceEstimation(ARObject):
    """
    Resource estimations for RTE and BSW of a single ECU instance.
    """

    # EcuResourceEstimation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.43, p.260
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswResourceEstimation   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswResourceEstimation      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEcuInstanceRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIntroduction               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createRteResourceEstimation   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteResourceEstimation      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwCompToEcuMappingRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwCompToEcuMappingRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Estimation for the resource consumption of the basic software.
        self.bswResourceEstimation: Optional[ResourceConsumption] = None

        # Reference to the ECU this estimation is done for.
        self.ecuInstanceRef: Optional[RefType] = None

        # This represents introductory documentation about the ecu resource estimation Tags: xml.sequenceOffset=-10
        self.introduction: Optional[DocumentationBlock] = None

        # Estimation for the resource consumption of the run time environment.
        self.rteResourceEstimation: Optional[ResourceConsumption] = None

        # References to SwcToEcuMappings that have been taken into account for the resource estimations. This way it is possible to define dfferent EcuResourceEstimations with diifferent mappings, e.g. before and after mapping an additional SW component.
        self.swCompToEcuMappingRefs: List[RefType] = []

    def createBswResourceEstimation(self, short_name: str) -> ResourceConsumption:
        """
        Estimation for the resource consumption of the basic software.
        """
        if self.bswResourceEstimation is None:
            self.bswResourceEstimation = ResourceConsumption(self, short_name)
        return self.bswResourceEstimation

    def getBswResourceEstimation(self) -> Optional[ResourceConsumption]:
        """
        Estimation for the resource consumption of the basic software.
        """
        return self.bswResourceEstimation

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Reference to the ECU this estimation is done for.
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> "EcuResourceEstimation":
        """
        Reference to the ECU this estimation is done for.

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the ecu resource estimation Tags: xml.sequenceOffset=-10
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "EcuResourceEstimation":
        """
        This represents introductory documentation about the ecu resource estimation Tags: xml.sequenceOffset=-10

        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def createRteResourceEstimation(self, short_name: str) -> ResourceConsumption:
        """
        Estimation for the resource consumption of the run time environment.
        """
        if self.rteResourceEstimation is None:
            self.rteResourceEstimation = ResourceConsumption(self, short_name)
        return self.rteResourceEstimation

    def getRteResourceEstimation(self) -> Optional[ResourceConsumption]:
        """
        Estimation for the resource consumption of the run time environment.
        """
        return self.rteResourceEstimation

    def addSwCompToEcuMappingRef(self, value: Optional[RefType]) -> "EcuResourceEstimation":
        """
        References to SwcToEcuMappings that have been taken into account for the resource estimations. This way it is possible to define dfferent EcuResourceEstimations with diifferent mappings, e.g. before and after mapping an additional SW component.

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.swCompToEcuMappingRefs.append(value)
        return self

    def getSwCompToEcuMappingRefs(self) -> List[RefType]:
        """
        References to SwcToEcuMappings that have been taken into account for the resource estimations. This way it is possible to define dfferent EcuResourceEstimations with diifferent mappings, e.g. before and after mapping an additional SW component.
        """
        return self.swCompToEcuMappingRefs


class MappingConstraint(ARObject, VariationPointCapable, ABC):
    """
    Different constraints that may be used to limit the mapping of SW components to applicable ECUs, Partitions or Cores depending on the mappingScope attribute.
    """

    # MappingConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.8, p.202
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIntroduction   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self):
        if type(self) is MappingConstraint:
            raise TypeError("MappingConstraint is an abstract class.")

        super().__init__()

        # This represents introductory documentation about the mapping constraint.
        self.introduction: Optional[DocumentationBlock] = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the mapping constraint.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "MappingConstraint":
        """
        This represents introductory documentation about the mapping constraint.

        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self


class ComponentClustering(MappingConstraint):
    """
    Constraint that forces the mapping of all referenced SW component instances to the same ECU, Core, Partition depending on the defined mappingScope attribute. If mappingScope is not specified then mappingScopeEcu shall be assumed.
    """

    # ComponentClustering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.9, p.203
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addClusteredComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClusteredComponentIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMappingScope             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappingScope             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the components that have to be mapped together. InstanceRef implemented by: ComponentInSystemInstanceRef
        self.clusteredComponentIRefs: List[ComponentInSystemInstanceRef] = []

        # This attribute indicates whether the ComponentClustering mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScope Ecu shall be assumed.
        self.mappingScope: Optional[MappingScopeEnum] = None

    def addClusteredComponentIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "ComponentClustering":
        """
        Reference to the components that have to be mapped together. InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not add to clusteredComponentIRefs.
        """
        if value is not None:
            self.clusteredComponentIRefs.append(value)
        return self

    def getClusteredComponentIRefs(self) -> List[ComponentInSystemInstanceRef]:
        """
        Reference to the components that have to be mapped together. InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.clusteredComponentIRefs

    def getMappingScope(self) -> Optional[MappingScopeEnum]:
        """
        This attribute indicates whether the ComponentClustering mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScope Ecu shall be assumed.
        """
        return self.mappingScope

    def setMappingScope(self, value: Optional[MappingScopeEnum]) -> "ComponentClustering":
        """
        This attribute indicates whether the ComponentClustering mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScope Ecu shall be assumed.

        A None value is a no-op and does not overwrite an existing mappingScope.
        """
        if value is not None:
            self.mappingScope = value
        return self


class ComponentSeparation(MappingConstraint):
    """
    Constraint that forces the two referenced SW components (called A and B in the following) not to be mapped to the same ECU, Core, Partition depending on the defined mappingScope attribute. If mapping Scope is not specified then mappingScopeEcu shall be assumed. If a SW component (e.g. A) is a composition, none of the atomic SW components making up the A composition shall be mapped together with any of the atomic SW components making up the B composition. Furthermore, A and B shall be disjoint.
    """

    # ComponentSeparation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.11, p.205
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMappingScope             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMappingScope             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSeparatedComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSeparatedComponentIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute indicates whether the Component Separation mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScopeEcu shall be assumed.
        self.mappingScope: Optional[MappingScopeEnum] = None

        # The two components that have to be mapped to different ECUs InstanceRef implemented by: ComponentInSystemInstanceRef
        self.separatedComponentIRefs: List[ComponentInSystemInstanceRef] = []

    def getMappingScope(self) -> Optional[MappingScopeEnum]:
        """
        This attribute indicates whether the Component Separation mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScopeEcu shall be assumed.
        """
        return self.mappingScope

    def setMappingScope(self, value: Optional[MappingScopeEnum]) -> "ComponentSeparation":
        """
        This attribute indicates whether the Component Separation mapping constraint applies to different ECUs, partitions or cores. If this attribute is not specified then mappingScopeEcu shall be assumed.

        A None value is a no-op and does not overwrite an existing mappingScope.
        """
        if value is not None:
            self.mappingScope = value
        return self

    def addSeparatedComponentIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "ComponentSeparation":
        """
        The two components that have to be mapped to different ECUs InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not add to separatedComponentIRefs.
        """
        if value is not None:
            self.separatedComponentIRefs.append(value)
        return self

    def getSeparatedComponentIRefs(self) -> List[ComponentInSystemInstanceRef]:
        """
        The two components that have to be mapped to different ECUs InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.separatedComponentIRefs


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """
    This meta-class represents the ability to map a J1939ControllerApplication to a J1939NmNode. Note that this is similar but not identical to the mapping of SwComponentPrototypes to EcuInstances; for J1939 the semantics of an EcuInstance itself is basically replaced by a J1939NmNode.
    """

    # J1939ControllerApplicationToJ1939NmNodeMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.12, p.207
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getJ1939ControllerApplicationRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setJ1939ControllerApplicationRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getJ1939NmNodeRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setJ1939NmNodeRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the J1939 Controller Application that is mapped to the referenced J1939NmNode.
        self.j1939ControllerApplicationRef: Optional[RefType] = None

        # J1939NmNode that is the target of the J1939ControllerApplicationTo1939NmNodeMapping.
        self.j1939NmNodeRef: Optional[RefType] = None

    def getJ1939ControllerApplicationRef(self) -> Optional[RefType]:
        """
        Reference to the J1939 Controller Application that is mapped to the referenced J1939NmNode.
        """
        return self.j1939ControllerApplicationRef

    def setJ1939ControllerApplicationRef(self, value: Optional[RefType]) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        Reference to the J1939 Controller Application that is mapped to the referenced J1939NmNode.

        A None value is a no-op and does not overwrite an existing j1939ControllerApplicationRef.
        """
        if value is not None:
            self.j1939ControllerApplicationRef = value
        return self

    def getJ1939NmNodeRef(self) -> Optional[RefType]:
        """
        J1939NmNode that is the target of the J1939ControllerApplicationTo1939NmNodeMapping.
        """
        return self.j1939NmNodeRef

    def setJ1939NmNodeRef(self, value: Optional[RefType]) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """
        J1939NmNode that is the target of the J1939ControllerApplicationTo1939NmNodeMapping.

        A None value is a no-op and does not overwrite an existing j1939NmNodeRef.
        """
        if value is not None:
            self.j1939NmNodeRef = value
        return self
