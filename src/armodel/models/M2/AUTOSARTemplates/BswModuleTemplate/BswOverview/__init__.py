"""
This module contains classes for representing AUTOSAR Basic Software (BSW) module overview information.
BSW module overview describes the high-level structure and interfaces of BSW modules,
including their dependencies, behaviors, and data exchanges with other modules.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleDependency
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from typing import List, Optional


class BswModuleDescription(AtpStructureElement):
    """
    Root element for the description of a single BSW module or BSW cluster. In case it describes a BSW module, the short name of this element equals the name of the BSW module.
    """

    # BswModuleDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 3.1, p.29
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleDependencies      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createBswModuleDependency     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addBswModuleDependency        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleDocumentation     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBswModuleDocumentation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExpectedEntryRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExpectedEntryRefs          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addExpectedEntryRef           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getImplementedEntryRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addImplementedEntryRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInternalBehaviors          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInternalBehaviors          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createBswInternalBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModuleId                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModuleId                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedClientServerEntries [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createProvidedClientServerEntry [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedDatas              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createProvidedData            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedModeGroups         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createProvidedModeGroup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReleasedTriggers           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createReleasedTrigger         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiredClientServerEntries [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRequiredClientServerEntry [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiredDatas              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRequiredData            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiredModeGroups         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRequiredModeGroup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiredTriggers           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createRequiredTrigger         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the dependency to another BSW module.
        self.bswModuleDependencies: List[BswModuleDependency] = []

        # This adds a documentation to the BSW module.
        self.bswModuleDocumentation: Optional[SwComponentDocumentation] = None

        # Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry.
        self.expectedEntryRefs: List[RefType] = []

        # Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback.
        self.implementedEntryRefs: List[RefType] = []

        # The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>.
        self.internalBehaviors: List[BswInternalBehavior] = []

        # Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        self.moduleId: Optional[PositiveInteger] = None

        # Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler.
        self.providedClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler.
        self.providedDatas: List[VariableDataPrototype] = []

        # A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.
        self.providedModeGroups: List[ModeDeclarationGroupPrototype] = []

        # A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.
        self.releasedTriggers: List[Trigger] = []

        # Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler.
        self.requiredClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler.
        self.requiredDatas: List[VariableDataPrototype] = []

        # Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler.
        self.requiredModeGroups: List[ModeDeclarationGroupPrototype] = []

        # Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler.
        self.requiredTriggers: List[Trigger] = []

    def getBswModuleDependencies(self) -> List[BswModuleDependency]:
        """
        Describes the dependency to another BSW module.
        """
        return self.bswModuleDependencies

    def createBswModuleDependency(self, short_name: str) -> BswModuleDependency:
        """
        Describes the dependency to another BSW module.

        Args:
            short_name: The short name for the new BSW module dependency

        Returns:
            The created BswModuleDependency instance
        """
        if not self.IsElementExists(short_name):
            dependency = BswModuleDependency(self, short_name)
            self.addElement(dependency)
            self.bswModuleDependencies.append(dependency)
        return self.getElement(short_name)

    def addBswModuleDependency(self, value: BswModuleDependency) -> "BswModuleDescription":
        """
        Describes the dependency to another BSW module.
        Only adds the value if it is not None.

        Args:
            value: BswModuleDependency instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModuleDependencies.append(value)
        return self

    def getBswModuleDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        This adds a documentation to the BSW module.
        """
        return self.bswModuleDocumentation

    def setBswModuleDocumentation(self, value: SwComponentDocumentation) -> "BswModuleDescription":
        """
        This adds a documentation to the BSW module.
        Only sets the value if it is not None.

        Args:
            value: SwComponentDocumentation instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModuleDocumentation = value
        return self

    def getExpectedEntryRefs(self) -> List[RefType]:
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry.
        """
        return self.expectedEntryRefs

    def setExpectedEntryRefs(self, value: List[RefType]) -> "BswModuleDescription":
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry.
        Only sets the value if it is not None.

        Args:
            value: List of RefType to expected entries to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.expectedEntryRefs = value
        return self

    def addExpectedEntryRef(self, value: RefType) -> "BswModuleDescription":
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry.
        Only adds the value if it is not None.

        Args:
            value: RefType to an expected entry to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.expectedEntryRefs.append(value)
        return self

    def getImplementedEntryRefs(self) -> List[RefType]:
        """
        Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback.
        """
        return self.implementedEntryRefs

    def addImplementedEntryRef(self, value: RefType) -> "BswModuleDescription":
        """
        Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback.
        Only adds the value if it is not None.

        Args:
            value: RefType to an implemented entry to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementedEntryRefs.append(value)
        return self

    def getInternalBehaviors(self) -> List[BswInternalBehavior]:
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>.
        """
        return self.internalBehaviors

    def setInternalBehaviors(self, value: List[BswInternalBehavior]) -> "BswModuleDescription":
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>.
        Only sets the value if it is not None.

        Args:
            value: List of BswInternalBehavior instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.internalBehaviors = value
        return self

    def createBswInternalBehavior(self, short_name: str) -> BswInternalBehavior:
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>.

        Args:
            short_name: The short name for the new internal behavior

        Returns:
            The created BswInternalBehavior instance
        """
        if not self.IsElementExists(short_name):
            behavior = BswInternalBehavior(self, short_name)
            self.addElement(behavior)
            self.internalBehaviors.append(behavior)
        return self.getElement(short_name)

    def getModuleId(self) -> Optional[PositiveInteger]:
        """
        Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        """
        return self.moduleId

    def setModuleId(self, value: PositiveInteger) -> "BswModuleDescription":
        """
        Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        Only sets the value if it is not None.

        Args:
            value: The module ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.moduleId = value
        return self

    def getProvidedClientServerEntries(self) -> List[BswModuleClientServerEntry]:
        """
        Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler.
        """
        return self.providedClientServerEntries

    def createProvidedClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler.

        Args:
            short_name: The short name for the new provided client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if not self.IsElementExists(short_name):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.providedClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getProvidedDatas(self) -> List[VariableDataPrototype]:
        """
        Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler.
        """
        return self.providedDatas

    def createProvidedData(self, short_name: str) -> VariableDataPrototype:
        """
        Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler.

        Args:
            short_name: The short name for the new provided data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.providedDatas.append(prototype)
        return self.getElement(short_name)

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.
        """
        return self.providedModeGroups

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.

        Args:
            short_name: The short name for the new provided mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if not self.IsElementExists(short_name):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.providedModeGroups.append(prototype)
        return self.getElement(short_name)

    def getReleasedTriggers(self) -> List[Trigger]:
        """
        A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.
        """
        return self.releasedTriggers

    def createReleasedTrigger(self, short_name: str) -> Trigger:
        """
        A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType.

        Args:
            short_name: The short name for the new released trigger

        Returns:
            The created Trigger instance
        """
        if not self.IsElementExists(short_name):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.releasedTriggers.append(trigger)
        return self.getElement(short_name)

    def getRequiredClientServerEntries(self) -> List[BswModuleClientServerEntry]:
        """
        Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler.
        """
        return self.requiredClientServerEntries

    def createRequiredClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler.

        Args:
            short_name: The short name for the new required client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if not self.IsElementExists(short_name):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.requiredClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getRequiredDatas(self) -> List[VariableDataPrototype]:
        """
        Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler.
        """
        return self.requiredDatas

    def createRequiredData(self, short_name: str) -> VariableDataPrototype:
        """
        Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler.

        Args:
            short_name: The short name for the new required data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredDatas.append(prototype)
        return self.getElement(short_name)

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler.
        """
        return self.requiredModeGroups

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler.

        Args:
            short_name: The short name for the new required mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if not self.IsElementExists(short_name):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredModeGroups.append(prototype)
        return self.getElement(short_name)

    def getRequiredTriggers(self) -> List[Trigger]:
        """
        Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler.
        """
        return self.requiredTriggers

    def createRequiredTrigger(self, short_name: str) -> Trigger:
        """
        Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler.

        Args:
            short_name: The short name for the new required trigger

        Returns:
            The created Trigger instance
        """
        if not self.IsElementExists(short_name):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.requiredTriggers.append(trigger)
        return self.getElement(short_name)
