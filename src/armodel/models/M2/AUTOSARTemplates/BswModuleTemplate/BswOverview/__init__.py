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
    Represents the description of a single BSW module or BSW cluster in AUTOSAR.
    In case it describes a BSW module, the short name of this element equals the name of the BSW module.
    This is the root element for describing BSW module structure, interfaces, and behavior.
    """
    # BswModuleDescription method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBswModuleDependencies     [x] impl  [x] docstring  [x] test
    # [x] setBswModuleDependencies     [x] impl  [x] docstring  [x] test
    # [x] getBswModuleDocumentation    [x] impl  [x] docstring  [x] test
    # [x] setBswModuleDocumentation    [x] impl  [x] docstring  [x] test
    # [x] getExpectedEntryRefs         [x] impl  [x] docstring  [x] test
    # [x] setExpectedEntryRefs         [x] impl  [x] docstring  [x] test
    # [x] getImplementedEntryRefs      [x] impl  [x] docstring  [x] test
    # [x] addImplementedEntryRef       [x] impl  [x] docstring  [x] test
    # [x] getInternalBehaviors         [x] impl  [x] docstring  [x] test
    # [x] setInternalBehaviors         [x] impl  [x] docstring  [x] test
    # [x] createBswInternalBehavior    [x] impl  [x] docstring  [x] test
    # [x] getModuleId                  [x] impl  [x] docstring  [x] test
    # [x] setModuleId                  [x] impl  [x] docstring  [x] test
    # [x] getProvidedClientServerEntries [x] impl  [x] docstring  [x] test
    # [x] createProvidedClientServerEntry [x] impl  [x] docstring  [x] test
    # [x] getProvidedDatas             [x] impl  [x] docstring  [x] test
    # [x] createProvidedData           [x] impl  [x] docstring  [x] test
    # [x] getProvidedModeGroups        [x] impl  [x] docstring  [x] test
    # [x] createProvidedModeGroup      [x] impl  [x] docstring  [x] test
    # [x] getReleasedTriggers          [x] impl  [x] docstring  [x] test
    # [x] createReleasedTrigger        [x] impl  [x] docstring  [x] test
    # [x] getRequiredClientServerEntries [x] impl  [x] docstring  [x] test
    # [x] createRequiredClientServerEntry [x] impl  [x] docstring  [x] test
    # [x] getRequiredDatas             [x] impl  [x] docstring  [x] test
    # [x] createRequiredData           [x] impl  [x] docstring  [x] test
    # [x] getRequiredModeGroups        [x] impl  [x] docstring  [x] test
    # [x] createRequiredModeGroup      [x] impl  [x] docstring  [x] test
    # [x] getRequiredTriggers          [x] impl  [x] docstring  [x] test
    # [x] createRequiredTrigger        [x] impl  [x] docstring  [x] test


    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module description with a parent and short name.

        Args:
            parent: The parent ARObject that contains this BSW module description
            short_name: The unique short name of this BSW module (equals the module name)
        """
        super().__init__(parent, short_name)

        # Describes the dependency to another BSW module
        self.bswModuleDependencies: List[BswModuleDependency] = []

        # This adds a documentation to the BSW module
        self.bswModuleDocumentation: SwComponentDocumentation = None

        # Indicates an entry which is required by this module.
        # Replacement of outgoingCallback / requiredEntry.
        self.expectedEntryRefs: List[RefType] = []

        # Specifies an entry provided by this module which can be called by other modules.
        # This includes "main" functions, interrupt routines, and callbacks.
        # Replacement of providedEntry / expectedCallback.
        self.implementedEntryRefs: List[RefType] = []

        # The various BswInternalBehaviors associated with a BswModuleDescription
        # can be distributed over several physical files (<<atpSplitable>>).
        self.internalBehaviors: List[BswInternalBehavior] = []

        # Refers to the BSW Module Identifier defined by the AUTOSAR standard.
        # For non-standardized modules, a proprietary identifier can be optionally chosen.
        self.moduleId: PositiveInteger = None

        # Specifies that this module provides a client server entry which can be called
        # from another partition or core. This entry is declared locally to this context
        # and will be connected to the requiredClientServerEntry of another or the same
        # module via the configuration of the BSW Scheduler.
        self.providedClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype provided by this module in order to be read from
        # another partition or core. The providedData is declared locally to this context
        # and will be connected to the requiredData of another or the same module via
        # the configuration of the BSW Scheduler.
        self.providedDatas: List[VariableDataPrototype] = []

        # A set of modes which is owned and provided by this module or cluster. It can be
        # connected to the requiredModeGroups of other modules or clusters via the
        # configuration of the BswScheduler. It can also be synchronized with modes provided
        # via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType
        # or ComplexDeviceDriverSwComponentType.
        self.providedModeGroups: List[ModeDeclarationGroupPrototype] = []

        # A Trigger released by this module or cluster. It can be connected to the
        # requiredTriggers of other modules or clusters via the configuration of the
        # BswScheduler. It can also be synchronized with Triggers provided via ports by an
        # associated ServiceSwComponentType, EcuAbstractionSwComponentType or
        # ComplexDeviceDriverSwComponentType.
        self.releasedTriggers: List[Trigger] = []

        # Specifies that this module requires a client server entry which can be implemented
        # on another partition or core. This entry is declared locally to this context and
        # will be connected to the providedClientServerEntry of another or the same module
        # via the configuration of the BSW Scheduler.
        self.requiredClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype required by this module in order to be provided from
        # another partition or core. The requiredData is declared locally to this context
        # and will be connected to the providedData of another or the same module via the
        # configuration of the BswScheduler.
        self.requiredDatas: List[VariableDataPrototype] = []

        # Specifies that this module or cluster depends on a certain mode group. The
        # requiredModeGroup is local to this context and will be connected to the
        # providedModeGroup of another module or cluster via the configuration of the
        # BswScheduler.
        self.requiredModeGroups: List[ModeDeclarationGroupPrototype] = []

        # Specifies that this module or cluster reacts upon an external trigger. This
        # requiredTrigger is declared locally to this context and will be connected to the
        # providedTrigger of another module or cluster via the configuration of the
        # BswScheduler.
        self.requiredTriggers: List[Trigger] = []

    def getBswModuleDependencies(self) -> List[BswModuleDependency]:
        """
        Gets the list of dependencies to other BSW modules.

        Returns:
            List of BswModuleDependency instances
        """
        return self.bswModuleDependencies

    def setBswModuleDependencies(self, value: List[BswModuleDependency]) -> "BswModuleDescription":
        """
        Sets the list of dependencies to other BSW modules.
        Only sets the value if it is not None.

        Args:
            value: List of BswModuleDependency instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModuleDependencies = value
        return self

    def getBswModuleDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        Gets the documentation attached to this BSW module.

        Returns:
            SwComponentDocumentation instance containing module documentation
        """
        return self.bswModuleDocumentation

    def setBswModuleDocumentation(self, value: SwComponentDocumentation) -> "BswModuleDescription":
        """
        Sets the documentation attached to this BSW module.
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
        Gets the list of expected entry references that this module requires.
        These are entries required by this module
        (replacement of outgoingCallback / requiredEntry).

        Returns:
            List of RefType to expected entries
        """
        return self.expectedEntryRefs

    def setExpectedEntryRefs(self, value: List[RefType]) -> "BswModuleDescription":
        """
        Sets the list of expected entry references that this module requires.
        Only sets the value if it is not None.

        Args:
            value: List of RefType to expected entries to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.expectedEntryRefs = value
        return self

    def getImplementedEntryRefs(self) -> List[RefType]:
        """
        Gets the list of implemented entry references that this module provides.
        These are entries provided by this module which can be called by other modules,
        including "main" functions, interrupt routines, and callbacks
        (replacement of providedEntry / expectedCallback).

        Returns:
            List of RefType to implemented entries
        """
        return self.implementedEntryRefs

    def addImplementedEntryRef(self, value: RefType) -> "BswModuleDescription":
        """
        Adds an implemented entry reference to this module's list.
        These are entries provided by this module which can be called by other modules.
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
        Gets the list of internal behaviors of this BSW module.
        The various BswInternalBehaviors can be distributed over several physical files.

        Returns:
            List of BswInternalBehavior instances
        """
        return self.internalBehaviors

    def setInternalBehaviors(self, value: List[BswInternalBehavior]) -> "BswModuleDescription":
        """
        Sets the list of internal behaviors of this BSW module.
        The various BswInternalBehaviors can be distributed over several physical files.
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
        Creates and adds a BSW internal behavior to this module description.
        This defines how the module behaves internally, including its events and entities.

        Args:
            short_name: The short name for the new internal behavior

        Returns:
            The created BswInternalBehavior instance
        """
        if (not self.IsElementExists(short_name)):
            behavior = BswInternalBehavior(self, short_name)
            self.addElement(behavior)
            self.internalBehaviors.append(behavior)
        return self.getElement(short_name)

    def getModuleId(self) -> Optional[PositiveInteger]:
        """
        Gets the BSW Module Identifier defined by the AUTOSAR standard.
        For non-standardized modules, a proprietary identifier can be optionally chosen.

        Returns:
            Positive integer representing the module ID
        """
        return self.moduleId

    def setModuleId(self, value: PositiveInteger) -> "BswModuleDescription":
        """
        Sets the BSW Module Identifier defined by the AUTOSAR standard.
        For non-standardized modules, a proprietary identifier can be optionally chosen.
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
        Gets the list of client-server entries that this module provides.
        These are entries which can be called from another partition or core, connected to
        the requiredClientServerEntry of another or the same module via the BSW Scheduler.

        Returns:
            List of BswModuleClientServerEntry instances
        """
        return self.providedClientServerEntries

    def createProvidedClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Creates and adds a client-server entry that this module provides to others.
        This is a service interface that this module offers to other modules.

        Args:
            short_name: The short name for the new provided client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if (not self.IsElementExists(short_name)):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.providedClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getProvidedDatas(self) -> List[VariableDataPrototype]:
        """
        Gets the list of data prototypes that this module provides.
        These are data prototypes provided by this module to be read from another partition
        or core, connected to the requiredData of another or the same module via the
        BSW Scheduler.

        Returns:
            List of VariableDataPrototype instances
        """
        return self.providedDatas

    def createProvidedData(self, short_name: str) -> VariableDataPrototype:
        """
        Creates and adds a data prototype that this module provides to others.
        This is a data interface that this module offers to other modules.

        Args:
            short_name: The short name for the new provided data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if (not self.IsElementExists(short_name)):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.providedDatas.append(prototype)
        return self.getElement(short_name)

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        Gets the list of mode group prototypes that this module provides.
        These are a set of modes owned and provided by this module or cluster, connected to
        the requiredModeGroups of other modules or clusters via the BswScheduler.

        Returns:
            List of ModeDeclarationGroupPrototype instances
        """
        return self.providedModeGroups

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        Creates and adds a mode group prototype that this module provides to others.
        This is a mode interface that this module offers to other modules for mode management.

        Args:
            short_name: The short name for the new provided mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if (not self.IsElementExists(short_name)):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.providedModeGroups.append(prototype)
        return self.getElement(short_name)

    def getReleasedTriggers(self) -> List[Trigger]:
        """
        Gets the list of triggers that this module releases.
        These are triggers released by this module or cluster, connected to the
        requiredTriggers of other modules or clusters via the BswScheduler.

        Returns:
            List of Trigger instances
        """
        return self.releasedTriggers

    def createReleasedTrigger(self, short_name: str) -> Trigger:
        """
        Creates and adds a trigger that this module releases to others.
        This is a trigger interface that this module can send to other modules.

        Args:
            short_name: The short name for the new released trigger

        Returns:
            The created Trigger instance
        """
        if (not self.IsElementExists(short_name)):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.releasedTriggers.append(trigger)
        return self.getElement(short_name)

    def getRequiredClientServerEntries(self) -> List[BswModuleClientServerEntry]:
        """
        Gets the list of client-server entries that this module requires.
        These are entries which can be implemented on another partition or core, connected
        to the providedClientServerEntry of another or the same module via the BSW Scheduler.

        Returns:
            List of BswModuleClientServerEntry instances
        """
        return self.requiredClientServerEntries

    def createRequiredClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Creates and adds a client-server entry that this module requires from others.
        This is a service interface that this module needs from other modules.

        Args:
            short_name: The short name for the new required client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if (not self.IsElementExists(short_name)):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.requiredClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getRequiredDatas(self) -> List[VariableDataPrototype]:
        """
        Gets the list of data prototypes that this module requires.
        These are data prototypes required by this module to be provided from another
        partition or core, connected to the providedData of another or the same module via
        the BSW Scheduler.

        Returns:
            List of VariableDataPrototype instances
        """
        return self.requiredDatas

    def createRequiredData(self, short_name: str) -> VariableDataPrototype:
        """
        Creates and adds a data prototype that this module requires from others.
        This is a data interface that this module needs from other modules.

        Args:
            short_name: The short name for the new required data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if (not self.IsElementExists(short_name)):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredDatas.append(prototype)
        return self.getElement(short_name)

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        Gets the list of mode group prototypes that this module requires.
        These indicate a dependency on a certain mode group, connected to the
        providedModeGroup of another module or cluster via the BswScheduler.

        Returns:
            List of ModeDeclarationGroupPrototype instances
        """
        return self.requiredModeGroups

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        Creates and adds a mode group prototype that this module requires from others.
        This is a mode interface that this module needs from other modules for mode management.

        Args:
            short_name: The short name for the new required mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if (not self.IsElementExists(short_name)):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredModeGroups.append(prototype)
        return self.getElement(short_name)

    def getRequiredTriggers(self) -> List[Trigger]:
        """
        Gets the list of triggers that this module requires.
        These indicate that this module or cluster reacts upon an external trigger,
        connected to the providedTrigger of another module or cluster via the BswScheduler.

        Returns:
            List of Trigger instances
        """
        return self.requiredTriggers

    def createRequiredTrigger(self, short_name: str) -> Trigger:
        """
        Creates and adds a trigger that this module requires from others.
        This is a trigger interface that this module needs from other modules.

        Args:
            short_name: The short name for the new required trigger

        Returns:
            The created Trigger instance
        """
        if (not self.IsElementExists(short_name)):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.requiredTriggers.append(trigger)
        return self.getElement(short_name)
