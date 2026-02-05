"""
This module contains classes for representing AUTOSAR Basic Software (BSW) module overview information.
BSW module overview describes the high-level structure and interfaces of BSW modules,
including their dependencies, behaviors, and data exchanges with other modules.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInternalBehavior,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleClientServerEntry,
    BswModuleDependency,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclarationGroupPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import (
    Trigger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
    SwComponentDocumentation,
)


class BswModuleDescription(AtpStructureElement):
    """
    Represents the description of a single BSW module or BSW cluster in AUTOSAR.
    In case it describes a BSW module, the short name of this element equals the name of the BSW module.
    This is the root element for describing BSW module structure, interfaces, and behavior.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module description with a parent and short name.

        Args:
            parent: The parent ARObject that contains this BSW module description
            short_name: The unique short name of this BSW module (equals the module name)
        """
        super().__init__(parent, short_name)

        # List of dependencies this BSW module has on other modules
        self.bswModuleDependencies: List[BswModuleDependency] = []
        # Documentation for this BSW module
        self.bswModuleDocumentation: SwComponentDocumentation = None
        # List of expected entry references that this module expects to be available
        self.expectedEntryRefs: List[RefType] = []
        # List of implemented entry references that this module provides
        self.implementedEntryRefs: List[RefType] = []
        # List of internal behaviors of this BSW module
        self.internalBehaviors: List[BswInternalBehavior] = []
        # Unique module identifier for this BSW module
        self.moduleId: PositiveInteger = None
        # List of client-server entries that this module provides to others
        self.providedClientServerEntries: List[BswModuleClientServerEntry] = []
        # List of data prototypes that this module provides to others
        self.providedDatas: List[VariableDataPrototype] = []
        # List of mode group prototypes that this module provides to others
        self.providedModeGroups: List[ModeDeclarationGroupPrototype] = []
        # List of triggers that this module releases to others
        self.releasedTriggers: List[Trigger] = []
        # List of client-server entries that this module requires from others
        self.requiredClientServerEntries: List[BswModuleClientServerEntry] = []
        # List of data prototypes that this module requires from others
        self.requiredDatas: List[VariableDataPrototype] = []
        # List of mode group prototypes that this module requires from others
        self.requiredModeGroups: List[ModeDeclarationGroupPrototype] = []
        # List of triggers that this module requires from others
        self.requiredTriggers: List[Trigger] = []

    def getBswModuleDependencies(self):
        """
        Gets the list of dependencies this BSW module has on other modules.

        Returns:
            List of BswModuleDependency instances
        """
        return self.bswModuleDependencies

    def setBswModuleDependencies(self, value):
        """
        Sets the list of dependencies this BSW module has on other modules.
        Only sets the value if it is not None.

        Args:
            value: List of BswModuleDependency instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModuleDependencies = value
        return self

    def getBswModuleDocumentation(self):
        """
        Gets the documentation for this BSW module.

        Returns:
            SwComponentDocumentation instance containing module documentation
        """
        return self.bswModuleDocumentation

    def setBswModuleDocumentation(self, value):
        """
        Sets the documentation for this BSW module.
        Only sets the value if it is not None.

        Args:
            value: SwComponentDocumentation instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModuleDocumentation = value
        return self

    def getExpectedEntryRefs(self):
        """
        Gets the list of expected entry references that this module expects to be available.
        These are entries that the module expects to exist in the system but doesn't implement itself.

        Returns:
            List of RefType to expected entries
        """
        return self.expectedEntryRefs

    def setExpectedEntryRefs(self, value):
        """
        Sets the list of expected entry references that this module expects to be available.
        Only sets the value if it is not None.

        Args:
            value: List of RefType to expected entries to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.expectedEntryRefs = value
        return self

    def getImplementedEntryRefs(self):
        """
        Gets the list of implemented entry references that this module provides.
        These are the entries that this module actually implements and makes available to others.

        Returns:
            List of RefType to implemented entries
        """
        return self.implementedEntryRefs

    def addImplementedEntryRef(self, value):
        """
        Adds an implemented entry reference to this module's list.
        These are entries that this module implements and makes available to others.
        Only adds the value if it is not None.

        Args:
            value: RefType to an implemented entry to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementedEntryRefs.append(value)
        return self

    def getInternalBehaviors(self):
        """
        Gets the list of internal behaviors of this BSW module.
        These define how the module behaves internally, including its events and entities.

        Returns:
            List of BswInternalBehavior instances
        """
        return self.internalBehaviors

    def setInternalBehaviors(self, value):
        """
        Sets the list of internal behaviors of this BSW module.
        These define how the module behaves internally, including its events and entities.
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

    def getModuleId(self):
        """
        Gets the unique module identifier for this BSW module.

        Returns:
            Positive integer representing the module ID
        """
        return self.moduleId

    def setModuleId(self, value):
        """
        Sets the unique module identifier for this BSW module.
        Only sets the value if it is not None.

        Args:
            value: The module ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.moduleId = value
        return self

    def getProvidedClientServerEntries(self):
        """
        Gets the list of client-server entries that this module provides to others.
        These are service interfaces that this module offers to other modules.

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

    def getProvidedDatas(self):
        """
        Gets the list of data prototypes that this module provides to others.
        These are data interfaces that this module offers to other modules.

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

    def getProvidedModeGroups(self):
        """
        Gets the list of mode group prototypes that this module provides to others.
        These are mode interfaces that this module offers to other modules for mode management.

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

    def getReleasedTriggers(self):
        """
        Gets the list of triggers that this module releases to others.
        These are trigger interfaces that this module can send to other modules.

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

    def getRequiredClientServerEntries(self):
        """
        Gets the list of client-server entries that this module requires from others.
        These are service interfaces that this module needs from other modules.

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

    def getRequiredDatas(self):
        """
        Gets the list of data prototypes that this module requires from others.
        These are data interfaces that this module needs from other modules.

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

    def getRequiredModeGroups(self):
        """
        Gets the list of mode group prototypes that this module requires from others.
        These are mode interfaces that this module needs from other modules for mode management.

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

    def getRequiredTriggers(self):
        """
        Gets the list of triggers that this module requires from others.
        These are trigger interfaces that this module needs from other modules.

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


__all__ = []
