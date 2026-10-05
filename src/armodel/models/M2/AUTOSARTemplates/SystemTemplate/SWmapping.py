# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class SwcToImplMapping(Identifiable, VariationPointCapable):
    """
    Map instances of an AtomicSwComponentType to a specific Implementation.
    """

    # SwcToImplMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.3, p.199
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
