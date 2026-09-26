"""
This module contains classes for representing AUTOSAR SWC-BSW mapping structures
in the CommonStructure module. SWC-BSW mapping defines relationships between
software component entities and basic software module entities for integration purposes.
"""

from typing import List, Optional, TYPE_CHECKING
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
        PModeGroupInAtomicSwcInstanceRef,
        PTriggerInAtomicSwcTypeInstanceRef,
    )


class SwcBswRunnableMapping(ARObject, VariationPointCapable):
    """
    Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a BSW module (in the case of an AUTOSAR Service, a Complex Driver or an ECU Abstraction). The mapping can be used by a tool to find relevant information on the behavior, e.g. whether the bswEntity shall be running in interrupt context.
    """

    # SwcBswRunnableMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.47, p.110
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswEntityRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswEntityRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcRunnableRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcRunnableRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The mapped BswModuleEntity
        self.bswEntityRef: Optional[RefType] = None

        # The mapped SWC runnable.
        self.swcRunnableRef: Optional[RefType] = None

    def getBswEntityRef(self) -> Optional[RefType]:
        """
        The mapped BswModuleEntity
        """
        return self.bswEntityRef

    def setBswEntityRef(self, value: Optional[RefType]) -> "SwcBswRunnableMapping":
        """
        The mapped BswModuleEntity
        A None value is a no-op and does not overwrite an existing bswEntityRef.
        """
        if value is not None:
            self.bswEntityRef = value
        return self

    def getSwcRunnableRef(self) -> Optional[RefType]:
        """
        The mapped SWC runnable.
        """
        return self.swcRunnableRef

    def setSwcRunnableRef(self, value: Optional[RefType]) -> "SwcBswRunnableMapping":
        """
        The mapped SWC runnable.
        A None value is a no-op and does not overwrite an existing swcRunnableRef.
        """
        if value is not None:
            self.swcRunnableRef = value
        return self


class SwcBswMapping(ARElement):
    """
    Maps an SwcInternalBehavior to an BswInternalBehavior. This is required to coordinate the API generation and the scheduling for AUTOSAR Service Components, ECU Abstraction Components and Complex Driver Components by the RTE and the BSW scheduling mechanisms.
    """

    # SwcBswMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.46, p.110 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswBehaviorRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswBehaviorRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRunnableMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addRunnableMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcBehaviorRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwcBehaviorRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSynchronizedModeGroups [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSynchronizedModeGroups [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSynchronizedModeGroup  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSynchronizedTriggers   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSynchronizedTriggers   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSynchronizedTrigger    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The mapped BswInternalBehavior
        self.bswBehaviorRef: Optional[RefType] = None

        # A mapping between a pair of SWC and BSW runnables.
        self.runnableMappings: List[SwcBswRunnableMapping] = []

        # The mapped SwcInternalBehavior.
        self.swcBehaviorRef: Optional[RefType] = None

        # A pair of SWC and BSW mode group prototypes to be synchronized by the scheduler.
        self.synchronizedModeGroups: List[SwcBswSynchronizedModeGroupPrototype] = []

        # A pair of SWC and BSW Triggers to be synchronized by the scheduler.
        self.synchronizedTriggers: List[SwcBswSynchronizedTrigger] = []

    def getBswBehaviorRef(self):
        """The mapped BswInternalBehavior"""
        return self.bswBehaviorRef

    def setBswBehaviorRef(self, value):
        """
        Sets the reference to the BSW behavior in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The BSW behavior reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswBehaviorRef = value
        return self

    def getRunnableMappings(self):
        """A mapping between a pair of SWC and BSW runnables."""
        return self.runnableMappings

    def addRunnableMapping(self, value):
        """
        Adds a runnable mapping to this SWC-BSW mapping.

        Args:
            value: The runnable mapping to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.runnableMappings.append(value)
        return self

    def getSwcBehaviorRef(self):
        """The mapped SwcInternalBehavior."""
        return self.swcBehaviorRef

    def setSwcBehaviorRef(self, value):
        """
        Sets the reference to the SWC behavior in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The SWC behavior reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcBehaviorRef = value
        return self

    def getSynchronizedModeGroups(self):
        """A pair of SWC and BSW mode group prototypes to be synchronized by the scheduler."""
        return self.synchronizedModeGroups

    def setSynchronizedModeGroups(self, value):
        """
        Sets the list of synchronized mode groups in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized mode groups list to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.synchronizedModeGroups = value
        return self

    def addSynchronizedModeGroup(self, value) -> "SwcBswMapping":
        """
        Adds a synchronized mode group to this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized mode group to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.synchronizedModeGroups.append(value)
        return self

    def getSynchronizedTriggers(self):
        """A pair of SWC and BSW Triggers to be synchronized by the scheduler."""
        return self.synchronizedTriggers

    def setSynchronizedTriggers(self, value):
        """
        Sets the list of synchronized triggers in this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized triggers list to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.synchronizedTriggers = value
        return self

    def addSynchronizedTrigger(self, value) -> "SwcBswMapping":
        """
        Adds a synchronized trigger to this mapping.
        Only sets the value if it is not None.

        Args:
            value: The synchronized trigger to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.synchronizedTriggers.append(value)
        return self


class SwcBswSynchronizedModeGroupPrototype(ARObject, VariationPointCapable):
    """
    Synchronizes a mode group provided by a component via a port with a mode group provided by a BSW module or cluster.
    """

    # SwcBswSynchronizedModeGroupPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.48, p.162
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBswModeGroupRef           [x] impl  [x] docstring  [x] test
    # [x] setBswModeGroupRef           [x] impl  [x] docstring  [x] test
    # [x] getSwcModeGroupIRef          [x] impl  [x] docstring  [x] test
    # [x] setSwcModeGroupIRef          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the SwcBswSynchronizedModeGroupPrototype with default values.
        """
        super().__init__()

        # The BSW mode group prototype. Referenced BSW mode group prototype shall exist at configuration time (constr_10336).
        self.bswModeGroupRef: Optional[RefType] = None

        # The SWC mode group prototype provided by a particular port. Referenced SWC mode group shall exist at configuration time (constr_10337).
        self.swcModeGroupIRef: Optional["PModeGroupInAtomicSwcInstanceRef"] = None

    def getBswModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the BSW mode group prototype reference.

        Returns:
            Optional[RefType]: The BSW mode group prototype reference
        """
        return self.bswModeGroupRef

    def setBswModeGroupRef(self, value: Optional[RefType]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Sets the BSW mode group prototype reference.
        Only sets the value if it is not None.

        Args:
            value: The BSW mode group prototype reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswModeGroupRef = value
        return self

    def getSwcModeGroupIRef(self) -> Optional["PModeGroupInAtomicSwcInstanceRef"]:
        """
        Gets the SWC mode group instance reference.

        Returns:
            Optional[PModeGroupInAtomicSwcInstanceRef]: The SWC mode group instance reference
        """
        return self.swcModeGroupIRef

    def setSwcModeGroupIRef(self, value: Optional["PModeGroupInAtomicSwcInstanceRef"]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Sets the SWC mode group instance reference.
        Only sets the value if it is not None.

        Args:
            value: The SWC mode group instance reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcModeGroupIRef = value
        return self


class SwcBswSynchronizedTrigger(ARObject, VariationPointCapable):
    """
    Synchronizes a Trigger provided by a component via a port with a Trigger provided by a BSW module or cluster.
    """

    # SwcBswSynchronizedTrigger method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.49, p.111
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBswTriggerRef             [x] impl  [x] docstring  [x] test
    # [x] setBswTriggerRef             [x] impl  [x] docstring  [x] test
    # [x] getSwcTriggerIRef            [x] impl  [x] docstring  [x] test
    # [x] setSwcTriggerIRef            [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the SwcBswSynchronizedTrigger with default values.
        """
        super().__init__()

        # The BSW Trigger. Referenced BSW trigger shall exist at configuration time (constr_10300).
        self.bswTriggerRef: Optional[RefType] = None

        # The SWC Trigger provided by a particular port. InstanceRef implemented by: PTriggerInAtomicSwcTypeInstanceRef.
        # The referenced SWC trigger shall exist at configuration time (constr_10301).
        self.swcTriggerIRef: "PTriggerInAtomicSwcTypeInstanceRef" = None

    def getBswTriggerRef(self) -> Optional[RefType]:
        """
        Gets the reference to the BSW Trigger that is synchronized with the SWC Trigger
        of a component via this mapping. The referenced BSW Trigger shall exist at the
        time the BSW module configuration is finished (constr_10300).

        Returns:
            Optional[RefType]: The BSW trigger reference
        """
        return self.bswTriggerRef

    def setBswTriggerRef(self, value: Optional[RefType]) -> "SwcBswSynchronizedTrigger":
        """
        Sets the reference to the BSW Trigger that is synchronized with the SWC Trigger
        of a component via this mapping. The referenced BSW Trigger shall exist at the
        time the BSW module configuration is finished (constr_10300).
        Only sets the value if it is not None, and returns self for method chaining.

        Args:
            value: The BSW trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswTriggerRef = value
        return self

    def getSwcTriggerIRef(self) -> Optional["PTriggerInAtomicSwcTypeInstanceRef"]:
        """
        Gets the instance reference to the SWC Trigger provided by a particular port
        that is synchronized with the BSW Trigger via this mapping. InstanceRef is
        implemented by PTriggerInAtomicSwcTypeInstanceRef. The referenced SWC Trigger
        shall exist at the time the BSW module configuration is finished (constr_10301).

        Returns:
            Optional[PTriggerInAtomicSwcTypeInstanceRef]: The SWC trigger instance reference
        """
        return self.swcTriggerIRef

    def setSwcTriggerIRef(self, value: Optional["PTriggerInAtomicSwcTypeInstanceRef"]) -> "SwcBswSynchronizedTrigger":
        """
        Sets the instance reference to the SWC Trigger provided by a particular port
        that is synchronized with the BSW Trigger via this mapping. InstanceRef is
        implemented by PTriggerInAtomicSwcTypeInstanceRef. The referenced SWC Trigger
        shall exist at the time the BSW module configuration is finished (constr_10301).
        Only sets the value if it is not None, and returns self for method chaining.

        Args:
            value: The SWC trigger instance reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swcTriggerIRef = value
        return self
